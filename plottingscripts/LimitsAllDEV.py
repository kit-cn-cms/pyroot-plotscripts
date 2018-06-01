#!/usr/bin/python2

import sys
import getopt
import os
import imp
#import importlib
import inspect
import ROOT
import pandas 
import ast
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])
workdir = pyrootdir+"/"+"workdir"
sys.path.append(pyrootdir+'/util')
sys.path.append(filedir+"/configs")
import scriptgenerator
import plotutils
import tmputils
import runTimer
import limittools

import analysisClass
import plotconfig_v14 as pltcfg

def main(pyrootdir, argv):
    print '''
    # ========================================================
    # welcome to main function - defining some variables
    # ========================================================
    '''

    # name of the analysis (i.e. workdir name)
    name='limits_All_v30'
    workdir = pyrootdir + "/workdir/" + name
    if not os.path.exists(workdir):
        os.makedirs(workdir)
        print("created workdir at "+str(workdir))
        
    # path to root file
    anaRootPath=workdir+'/output_limitInput.root'

    # Name of final discriminator, should not contain underscore
    discrname='finaldiscr'

    # define MEM discriminator variable
    # this is not used anymore as the information is written in the csv files in configdata
    # keep it for clarity
    memexp='(memDBp>0.0)*(memDBp)+(memDBp<=0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # define BDT output variables
    bdtweightpath="/nfs/dust/cms/user/kelmorab/Spring17BDTWeights/"
    bdtset="Spring17v2"
    alternativebdtset="Spring17v3_ttbb"

    # name of the csv files used in configdata folder
    configDataBaseName = "limitsAllv20"

    # used categories in configdata to be added
    usedCategories = ["JTBDT", "JT2D", "JTMEM", "MultiDNN", "JT_control"] 
    # usedCategories += ["JT2DOPTIMIZED", "JTBDTOPTIMIZED"]

    print '''
    # ========================================================
    # initializing analysisClass 
    # ========================================================
    '''

    # TODO make the analysisClass more essential - atm it is not really needed
    analysis=analysisClass.Analysis(name,argv,anaRootPath,signalProcess='ttH')
    #analysis=analysisClass.Analysis(name,argv,
        #'/nfs/dust/cms/user/mharrend/doktorarbeit/latest/ttbb-cutbased-analysis_limitInput.root')
    #analysis=analysisClass.Analysis(name,argv,
        #'/nfs/dust/cms/user/kelmorab/plotscriptsSpring17/Sep17/pyroot-plotscripts/NOTDEFINED/output_limitInput.root ', signalProcess='ttH')
    #analysis=analysisClass.Analysis(name,argv,
        #'/nfs/dust/cms/user/mharrend/doktorarbeit/output20170626-reference/workdir/ttbb-cutbased-analysis/output_limitInput.root')
    
    # TODO these options should be set automatically ?
    analysis.plotBlinded=True
    analysis.makeSimplePlots=True
    analysis.makeMCControlPlots=True
    analysis.makeDataCards=True
    analysis.additionalPlotVariables=False

    # Make sure proper plotconfig is loaded for either ttbb or ttH
    # TODO how is this determined?
    print "We will import the following plotconfig: ", analysis.getPlotConfig()

    # TODO maybe print chosen functions into a .json file in workdir
    analysis.printChosenOptions()

    print '''    
    ## ========================================================
    ## NNFlow interface
    ## ========================================================
    '''

    # Create and configure NNFlow interface
    # NNFlowInterfacePath=os.getcwd()+'../util/dNNInterfaces/NNFlowInterface.py'
    # NNFlowInterface = imp.load_source("NNFlowInterface",NNFlowInterfacePath).theInterface()
    # NNFlowInterface.setDebugOutput(True)
    # NNFlowInterface.setModelFolderPath('/nfs/dust/cms/user/mharrend/doktorarbeit/tensorflowModels/neural_network_v3/multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20/model')
    # NNFlowInterface.setModelName('multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20.ckpt')
    # NNFlowInterface.update()
    #
    # print "NNFlowInterfacePath: ", NNFlowInterfacePath

    print '''    
    # ========================================================
    # define additional variables necessary for selection in plotparallel
    # ========================================================
    '''
    additionalvariables = tmputils.getAddVariables(pyrootdir = pyrootdir,
                                                    name = configDataBaseName)
    additionalvariables+= scriptgenerator.GetMEPDFadditionalVariablesList(
        "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/rate_factors_onlyinternal_powhegpythia.csv")
    #additionalvariables.extend(NNFlowInterface.getAdditionalVariablesList())

    # save addition variables information to workdir and print
    tmputils.saveAddVariablesToWorkdir(workdir, additionalvariables)

    print '''
    # ========================================================
    # prepare configdata
    #
    # access the information via
    # configData.categories
    # configData.nhistobins
    # configData.minxvals
    # configData.maxxvals
    # configData.discrs
    # configData.plotPreselection
    # configData.binlabels
    # ========================================================
    '''

    configData = tmputils.configData(pyrootdir = pyrootdir, 
                                        name = configDataBaseName, 
                                        usedCategories = usedCategories)
    configData.writeConfigDataToWorkdir(workdir)
    configData.assertData()


    print '''    
    # ========================================================
    # loading samples and samples data
    # 
    # access the information via
    # samplesData.samples
    # samplesData.samples_data
    # samplesData.systsamples
    # ========================================================
    '''
    samplesData = tmputils.samplesData(pltcfg)
    
    print '''
    # ========================================================
    # add systematic samples
    # ========================================================
    '''
    samplesData.addSystSamples(
                        pltcfg.otherSystNames, pltcfg.otherSystFileNames,
                        pathReplace = ["'nominal'","filename"]
                        )
    ## WARNING: Adjust Slice for samples if changing ttbar contributions
    
    print '''
    # ========================================================
    # add Parton shower variation samples to systematic samples
    # ========================================================
    '''
    nicks = ['ttbarOther', 'ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B']
    samplesData.addSystSamples(
                        pltcfg.PSSystNames, pltcfg.PSSystFileNames,
                        pathReplace = ["self.pltcfg.ttbarPathS",
                            "'self.pltcfg.path_additionalSamples+'/ttbar_'+filename+'/*nominal*.root'"],
                        selReplace = ["self.pltcfg.ttbarMCWeight","'*1.0'"],
                        selReplace2 = ["self.pltcfg.mcWeight+self.pltcfg.evenSel","self.pltcfg.mcWeightAll"],
                        filternicks = nicks)

    #for sample in samples[analysis.getTtbarSamplesLower() : analysis.getTtbarSamplesUpper()]: # only for ttbar samples
    print '''
    # ========================================================
    # add QCD sytematic for QCD sample to systematic samples
    # ========================================================
    '''
    samplesData.addSystSamples(
                        pltcfg.QCDSystNames, pltcfg.QCDSystReplacementStrings,
                        selReplace = ["'internalQCDweight'", "filename"],
                        filtername = "QCD")
    
    print '''
    # ========================================================
    # add samples and systsamples
    # ========================================================
    '''
    samplesData.addAllSamples(pltcfg.weightSystNames)
    
    print '''
    # ========================================================
    # define discriminator plots
    #
    # accessible via configData.discriminatorPlots
    # ========================================================
    '''
    configData.printLengths()
    configData.genDiscriminatorPlots(discrname)

    
    print '''
    # ========================================================
    # Check if additional (input) variables should be plotted and if necessary add them here to the discriminatorPlots
    #
    # new plots (evaluated) accesible via configData.additionalPlotList
    # ========================================================
    '''
    # TODO rework this function as it is atm half in analysisClass and half in new tmputils class
    if analysis.additionalPlotVariables:
        #  Construct list with additional plot variables, will need name of discrs and plotPreselections for this
        print( "add additional plot variables")
        clearTextAdditionalPlotList = analysis.getAdditionalPlotVariables(configData.discrs, configData.plotPreselections, configData.binlabels)
        configData.addAdditionalDiscriminatorPlots(clearTextAdditionalPlotList)

    
    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel==False or analysis.plotNumber == None :
        #if not os.path.exists(analysis.rootFilePath):
            print '''
            # ========================================================
            # Doing plotParallel step since root file was not found.
            # ========================================================
            '''
            dataBases = [["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_Spring17_V1",False]]
            treeInformationJsonFile = "/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_latestAndGreatest.json"
            addCodeInterfacePaths = ["../util/dNNInterfaces/dNNInterface_V6.py"]
            
            # timing plotParallel
            with runTimer.Timer("plotParallel"):
                # TODO rewrite plotParallel - this is the main part of the script
                plotParaOut = scriptgenerator.plotParallel(
                            name = name,
                            maxevents = 5000000,
                            plots = configData.discriminatorPlots,
                            samples = samplesData.allsamples,
                            catnames = [''], catselections = ["1."],
                            systnames = pltcfg.weightSystNames, systweights = pltcfg.systWeights,
                            additionalvariables = additionalvariables,
                            dataBases = dataBases,
                            treeInformationJsonFile = treeInformationJsonFile,
                            otherSystnames = samplesData.systnames,
                            addCodeInterfacePaths = addCodeInterfacePaths,
                            cirun = False,
                            StopAfterCompileStep = False,
                            haddParallel = True)

            # in the first iteration of plotParallel plotParaOut is a list where the first argument is the outputpath of the rootfile
            if type(plotParaOut)==str:
              outputpath=plotParaOut
            else:
              outputpath=plotParaOut[0]


            if analysis.getActivatedOptimizedRebinning():
                print '''
                # ========================================================
                # Doing OptimizedRebinning
                # ========================================================
                '''
                if analysis.getSignalProcess() == 'ttbb':
                    # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                    # TODO check the optimizedBinning function and adjust arguments to new structure
                    with runTimer.Timer("optimizeBinning"):
                        plotutils.optimizeBinning(outputpath,
                                            signalsamples=[samples[0:3]], 
                                            backgroundsamples=samples[3:],
                                            additionalSamples=samples_data, 
                                            plots=discriminatorPlots, 
                                            systnames=allsystnames, 
                                            minBkgPerBin=2.0, 
                                            optMode=analysis.getOptimzedRebinning(),
                                            considerStatUnc=False, 
                                            maxBins=20, 
                                            minBins=2,
                                            verbosity=2)

                elif analysis.getSignalProcess() == 'ttH':
                    # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. Rest: background samples
                    with runTimer.Timer("optimizeBinning"):
                        plotutils.optimizeBinning(outputpath,
                                            signalsamples=[samples[0]], 
                                            backgroundsamples=samples[9:],
                                            additionalSamples=samples[1:9]+samples_data, 
                                            plots=discriminatorPlots, 
                                            systnames=allsystnames, 
                                            minBkgPerBin=2.0, 
                                            optMode=analysis.getOptimzedRebinning(),
                                            considerStatUnc=False, 
                                            maxBins=20, 
                                            minBins=2,
                                            verbosity=2)
                else:
                    print 'Warning: Could not find signal process.'



            # hadd histo files before renaming. The histograms are actually already renamed. But the checkbins thingy will not have been done yet.
            print '''
            # ========================================================
            # hadding from wildcard
            # ========================================================
            '''
            # TODO look at this function and adjust arguments
            with runTimer.Timer("haddFilesFromWildCard"):
                scriptgenerator.haddFilesFromWildCard(outputpath,
                                                    outputpath[:-11]+"/HaddOutputs/*.root",
                                                    totalNumberOfHistosNeedsToRemainTheSame=True)

            
            # Deactivate check bins functionality in renameHistos if additional plot variables are added via analysis class
            renamedPath=outputpath[:-5]+'_limitInput.root'
            if os.path.exists(renamedPath):
                print "renamed file already exists"
            else:
                print '''
                # ========================================================
                # renaming Histograms
                # ========================================================
                '''
                if type(plotParaOut)==str:
                    # TODO this option is not chosen in the default run - adjust variables + look at function
                    with runTimer.Timer("renameHistos"):
                        limittools.renameHistos(
                                outputpath,
                                renamedPath,
                                allsystnames,
                                checkBins=True,
                                prune=False,
                                Epsilon=0.0)

                else:
                    # TODO this option is chosen in the first run -  adjust variables + look at function
                    with runTimer.Timer("renameHistos"):
                        limittools.renameHistos(
                                plotParaOut[1:],
                                renamedPath,
                                allsystnames,
                                checkBins=True,
                                prune=False,
                                Epsilon=0.0)

            print '''
            # ========================================================
            # adding real data with limittools
            # ========================================================
            '''
            with runTimer.Timer("addRealData"):
                limittools.addRealData(
                            renamedPath,
                            [s.nick for s in samples_data],
                            binlabels,
                            discrname)

            #limittools.addPseudoData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
            #outputpath=outputpath[:-5]+'_limitInput.root'
            outputpath=outputpath[:-5]+'_limitInput.root'

        #else:
            #print "Not doing plotParallel step since root file was found."
            #outputpath=analysis.rootFilePath
        #print "outputpath: ", outputpath
    else:
        print "not doing plotParallel step"
        # Warning This time output path refers only to output.root
        # ToDo: Fix usage of output path and output limit path
        if not os.path.exists(analysis.rootFilePath[:-16]+'.root'):
            workdir=os.getcwd()+'/../workdir/'+name
            outputpath=workdir+'/output.root'
        else:
            outputpath=analysis.rootFilePath[:-16]+'.root'
     
    print("###### DONE WITH PLOTPARALLEL STEP ######")       
    print("at the moment the outputpath is "+str(outputpath))
    print("#########################################")


    # make datacards
    if (analysis.doDrawParallel==False or analysis.plotNumber == None) and analysis.makeDataCards == True :
        #TODO
        # 1. Implement small Epsilon case
        # 2. Implement consisted Bin-by-Bin uncertainties
        #limittools.addRealData(outputpath,[s.nick for s in samples_data],binlabels,discrname)
        print '''
        # ========================================================
        # Making Data cards.
        # ========================================================
        '''
        # TODO look at function and update variables
        with runTimer.Timer("makeDatacardsParallel"):
            limittools.makeDatacardsParallel(outputpath,
                            name+'/'+name+'_datacard',
                            binlabels,
                            doHdecay=True,
                            discrname=discrname,
                            datacardmaker="mk_datacard_JESTest13TeVPara")


    # =======================================================================================================
    # Invoke drawParallel step
    # =======================================================================================================
    if analysis.doDrawParallel==True and analysis.plotNumber == None :
        # Hand over opts to keep commandline options
        print '''
        # ========================================================
        # Starting DrawParallel
        # ========================================================
        '''
        # TODO look at function and update variables
        with runTimer.Timer("DrawParallel"):
            scriptgenerator.DrawParallel(discriminatorPlots,
                                name,
                                os.path.realpath(inspect.getsourcefile(lambda:0)),
                                analysis.opts)

    # belongs to DrawParallel
    if analysis.doDrawParallel==True and analysis.plotNumber != None :
        print("we have a plotNumber --- changing discriminatorPlots")
        discriminatorPlots=[discriminatorPlots[int(analysis.plotNumber)]]
    # =======================================================================================================


    # Lists needed later, produce them only if needed, so check if subsequent step comes
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and (analysis.makeSimplePlots==True or analysis.makeMCControlPlots==True or analysis.makeEventYields==True):
        print '''
        # ========================================================
        # Creating lists for later use
        # ========================================================
        '''
        # TODO this sucks - rework in any case
        with runTimer.Timer("adjustingLists"):
            listOfHistoLists = plotutils.createHistoLists_fromSuperHistoFile(outputpath,samples,discriminatorPlots,1)
            lolT=plotutils.transposeLOL(listOfHistoLists)
            listOfHistoListsData = plotutils.createHistoLists_fromSuperHistoFile(outputpath,samples_data,discriminatorPlots,1)


    # plot simple MC plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeSimplePlots==True :
        print '''
        # ========================================================
        # Making simple MC plots
        # ========================================================
        print '''
        # TODO this sucks - rework in any case
        with runTimer.Timer("simpleMCplots"):
            plotutils.writeLOLAndOneOnTop(plotutils.transposeLOL(lolT[9:]),
                                            samples[9:],
                                            lolT[0],
                                            samples[0],
                                            -1,
                                            name+'/'+name+'_controlplots')

            plotutils.writeListOfHistoListsAN(plotutils.transposeLOL([lolT[0]]+lolT[9:]),
                                            [samples[0]]+samples[9:],
                                            "",
                                            name+'/'+name+'_shapes',
                                            True, False, False, 'histo', False, True, False)


    # Make MC Control plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeMCControlPlots==True :
        print '''
        # ========================================================
        # Making MC Control plots
        # ========================================================
        '''
        # TODO this sucks - rework in any case
        with runTimer.Timer("MCControlPlots"):
            lll=plotutils.createLLL_fromSuperHistoFileSyst(outputpath,
                                            samples[9:],
                                            discriminatorPlots,
                                            errorSystNamesNoQCD)

            labels=[plot.label for plot in discriminatorPlots]
            plotutils.plotDataMCanWsyst(listOfHistoListsData,
                                            plotutils.transposeLOL(lolT[9:]),
                                            samples[9:],
                                            lolT[0],
                                            samples[0],
                                            -2,
                                            name,
                                            [[lll,3354,ROOT.kBlack,True]],
                                            False,
                                            labels,
                                            True,
                                            analysis.plotBlinded)



if __name__ == "__main__":

    with runTimer.Timer("main"):
        main(pyrootdir, sys.argv[1:])


