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
import limittools

import analysisClass
import plotconfig_v14 as pltcfg
#from configs.plotconfig_v14 import *

def main(pyrootdir, argv):

    # ============================
    # definition of some variables
    # ============================

    # name of the analysis (i.e. workdir name
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

    # ============================
    # initializing analysisClass 
    # ============================

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

    
    ## ============================
    ## NNFlow interface
    ## ============================

    # Create and configure NNFlow interface
    # NNFlowInterfacePath=os.getcwd()+'../util/dNNInterfaces/NNFlowInterface.py'
    # NNFlowInterface = imp.load_source("NNFlowInterface",NNFlowInterfacePath).theInterface()
    # NNFlowInterface.setDebugOutput(True)
    # NNFlowInterface.setModelFolderPath('/nfs/dust/cms/user/mharrend/doktorarbeit/tensorflowModels/neural_network_v3/multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20/model')
    # NNFlowInterface.setModelName('multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20.ckpt')
    # NNFlowInterface.update()
    #
    # print "NNFlowInterfacePath: ", NNFlowInterfacePath
    

    # TODO maybe print chosen functions into a .json file in workdir
    analysis.printChosenOptions()

    # ============================
    # define additional variables necessary for selection in plotparallel
    # ============================
    additionalvariables = tmputils.getAddVariables(pyrootdir = pyrootdir,
                                                    name = configDataBaseName)
    additionalvariables+= scriptgenerator.GetMEPDFadditionalVariablesList(
        "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/rate_factors_onlyinternal_powhegpythia.csv")
    # append variables needed by NNFlow Interface
    #additionalvariables.extend(NNFlowInterface.getAdditionalVariablesList())

    # save addition variables information to workdir and print
    tmputils.saveAddVariablesToWorkdir(workdir, additionalvariables)

    # ============================
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
    # ============================
    configData = tmputils.configData(pyrootdir = pyrootdir, 
                                        name = configDataBaseName, 
                                        usedCategories = usedCategories)
    configData.writeConfigDataToWorkdir(workdir)
    configData.assertData()

    
    # ============================
    # loading samples and samples data
    # 
    # access the information via
    # samplesData.samples
    # samplesData.samples_data
    # samplesData.systsamples
    # ============================     
    samplesData = tmputils.samplesData(pltcfg)
    '''
    samples = pltcfg.samplesLimits
    sample_data = pltcfg.samplesDataControlPlots                    
    systsamples=[]
    '''
    # ============================
    # add systematic samples
    # ============================
    samplesData.addSystSamples(
                        pltcfg.otherSystNames, pltcfg.otherSystFileNames,
                        pathReplace = ["'nominal'","filename"]
                        )
    '''
    for sample in samples:
        for sysname, sysfilename in zip(pltcfg.otherSystNames,pltcfg.otherSystFileNames):
            thisnewsel=sample.selection
            systsamples.append(
                plotutils.Sample(
                    sample.name+sysname, sample.color, 
                    sample.path.replace(
                        "nominal",sysfilename),
                    thisnewsel, sample.nick+sysname, 
                    samDict=pltcfg.sampleDict))
    '''
    ## WARNING: Adjust Slice for samples if changing ttbar contributions
    
    
    # ============================
    # add Parton shower variation samples to systematic samples
    # ============================
    
    nicks = ['ttbarOther', 'ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B']
    samplesData.addSystSamples(
                        pltcfg.PSSystNames, pltcfg.PSSystFileNames,
                        pathReplace = ["pltcfg.ttbarPathS",
                            "'pltcfg.path_additionalSamples+'/ttbar_'+filename+'/*nominal*.root'"],
                        selReplace = ["pltcfg.ttbarMCWeight","'*1.0'"],
                        selReplace2 = ["pltcfg.mcWeight+pltcfg.evenSel","pltcfg.mcWeightAll"],
                        filternicks = nicks)

    #for sample in samples[analysis.getTtbarSamplesLower() : analysis.getTtbarSamplesUpper()]: # only for ttbar samples
    '''
    for sample in samples:
        if sample.nick not in nicks:
          continue
        for sysname, sysfilename in zip(pltcfg.PSSystNames, pltcfg.PSSystFileNames):
            thisoldsel=sample.selection
            thisnewsel=sample.selection.replace(ttbarMCWeight,"*1.0").replace(mcWeight+evenSel,mcWeightAll)
            print "adding sample for ", sysname
            print "selection ", thisnewsel
            print "instead of ", thisoldsel
            systsamples.append(
                plotutils.Sample(
                    sample.name+sysname, sample.color,
                    sample.path.replace(
                        ttbarPathS,path_additionalSamples+"/ttbar_"+sysfilename+"/*nominal*.root"),
                    thisnewsel,sample.nick+sysname,
                    samDict=pltcfg.sampleDict))
    '''
    # ============================
    # add QCD sytematic for QCD sample to systematic samples
    # ============================
    samplesData.addSystSamples(
                        pltcfg.QCDSystNames, pltcfg.QCDSystReplacementStrings,
                        selReplace = ["'internalQCDweight", "filename"],
                        filternames = "QCD")
    '''
    for sample in samples:
        if sample.name!='QCD':
          continue
        for sysname, sysreplacestring in zip(pltcfg.QCDSystNames, pltcfg.QCDSystReplacementStrings):
          thisnewsel=sample.selection.replace("internalQCDweight",sysreplacestring)
          systsamples.append(
            plotutils.Sample(
                sample.name+sysname, sample.color,
                sample.path,
                thisnewsel,sample.nick+sysname,
                samDict=pltcfg.sampleDict))
    '''
    
    # ============================
    # add samples and systsamples
    # ============================
    samplesData.addAllSamples(pltcfg.weightSystNames)
    
    '''
    allsamples=samples+systsamples
    allsystnames=weightSystNames+pltcfg.otherSystNames+pltcfg.PSSystNames+pltcfg.QCDSystNames
    '''

    # define plots
    discriminatorPlots=[]
    print len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
    print len(zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals))
    for discr,b,bl,nb,minx,maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
        discriminatorPlots.append(plotutils.Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b,bl))


    # Check if additional (input) variables should be plotted and if necessary add them here to the discriminatorPlots
    if analysis.additionalPlotVariables:
      # Construct list with additional plot variables, will need name of discrs and plotPreselections for this
      clearTextAdditionalPlotList = analysis.getAdditionalPlotVariables(discrs, plotPreselections, binlabels)
      evalAdditionalPlotList = [eval(x) for x in clearTextAdditionalPlotList]
      discriminatorPlots.extend(evalAdditionalPlotList)
      print "Additional variables added to discriminatorPlots: \n", clearTextAdditionalPlotList


    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel==False or analysis.plotNumber == None :
        #if not os.path.exists(analysis.rootFilePath):
            #print "Doing plotParallel step since root file was not found."
            THEoutputpath=scriptgenerator.plotParallel(name,5000000,discriminatorPlots,samples+samples_data+systsamples,[''],['1.'],weightSystNames,systWeights,additionalvariables,[["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_Spring17_V1",False]],"/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_latestAndGreatest.json",pltcfg.otherSystNames+PSSystNames+QCDSystNames,addCodeInterfacePaths=["../util/dNNInterfaces/dNNInterface_V6.py"],cirun=False,StopAfterCompileStep=False,haddParallel=True)
            if type(THEoutputpath)==str:
              outputpath=THEoutputpath
            else:
              outputpath=THEoutputpath[0]
            if analysis.getActivatedOptimizedRebinning():
              if analysis.getSignalProcess() == 'ttbb':
                # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                plotutils.optimizeBinning(outputpath,signalsamples=[samples[0:3]], backgroundsamples=samples[3:],additionalSamples=samples_data, plots=discriminatorPlots, systnames=allsystnames, minBkgPerBin=2.0, optMode=analysis.getOptimzedRebinning(),considerStatUnc=False, maxBins=20, minBins=2,verbosity=2)
              elif analysis.getSignalProcess() == 'ttH':
                # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. Rest: background samples
                plotutils.optimizeBinning(outputpath,signalsamples=[samples[0]], backgroundsamples=samples[9:],additionalSamples=samples[1:9]+samples_data, plots=discriminatorPlots, systnames=allsystnames, minBkgPerBin=2.0, optMode=analysis.getOptimzedRebinning(),considerStatUnc=False, maxBins=20, minBins=2,verbosity=2)
              else:
                print 'Warning: Could not find signal process.'

            # hadd histo files before renaming. The histograms are actually already renamed. But the checkbins thingy will not have been done yet.
            print "hadding from wildcard"
            scriptgenerator.haddFilesFromWildCard(outputpath,outputpath[:-11]+"/HaddOutputs/*.root",totalNumberOfHistosNeedsToRemainTheSame=True)
            # Deactivate check bins functionality in renameHistos if additional plot variables are added via analysis class
            renamedPath=outputpath[:-5]+'_limitInput.root'
            if os.path.exists(renamedPath):
              #if scriptgenerator.askYesNo('renamedFileExists. Repeat renaming?'):
              #  limittools.renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
              print "renamed file already exists"
            else:
              if type(THEoutputpath)==str:
                limittools.renameHistos(outputpath,renamedPath,allsystnames,checkBins=True,prune=False,Epsilon=0.0)
              else:
                limittools.renameHistos(THEoutputpath[1:],renamedPath,allsystnames,checkBins=True,prune=False,Epsilon=0.0)
            limittools.addRealData(renamedPath,[s.nick for s in samples_data],binlabels,discrname)
            #limittools.addPseudoData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
            #outputpath=outputpath[:-5]+'_limitInput.root'
            outputpath=outputpath[:-5]+'_limitInput.root'
        #else:
            #print "Not doing plotParallel step since root file was found."
            #outputpath=analysis.rootFilePath
        #print "outputpath: ", outputpath
    else:
        # Warning This time output path refers only to output.root
        # ToDo: Fix usage of output path and output limit path
        if not os.path.exists(analysis.rootFilePath[:-16]+'.root'):
            workdir=os.getcwd()+'/workdir/'+name
            outputpath=workdir+'/output.root'
        else:
            outputpath=analysis.rootFilePath[:-16]+'.root'
            
    print outputpath            
    # make datacards
    if (analysis.doDrawParallel==False or analysis.plotNumber == None) and analysis.makeDataCards == True :
        #TODO
        # 1. Implement small Epsilon case
        # 2. Implement consisted Bin-by-Bin uncertainties
        #limittools.addRealData(outputpath,[s.nick for s in samples_data],binlabels,discrname)
        print "Making Data cards."
        limittools.makeDatacardsParallel(outputpath,name+'/'+name+'_datacard',binlabels,doHdecay=True,discrname=discrname,datacardmaker="mk_datacard_JESTest13TeVPara")


    # Invoke drawParallel step
    if analysis.doDrawParallel==True and analysis.plotNumber == None :
        # Hand over opts to keep commandline options
        print 'Starting DrawParallel'
        scriptgenerator.DrawParallel(discriminatorPlots,name,os.path.realpath(inspect.getsourcefile(lambda:0)),analysis.opts)

    # belongs to DrawParallel
    if analysis.doDrawParallel==True and analysis.plotNumber != None :
        discriminatorPlots=[discriminatorPlots[int(analysis.plotNumber)]]



    # Lists needed later, produce them only if needed, so check if subsequent step comes
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and (analysis.makeSimplePlots==True or analysis.makeMCControlPlots==True or analysis.makeEventYields==True):
        print 'Create lists needed later'
        listOfHistoLists=plotutils.createHistoLists_fromSuperHistoFile(outputpath,samples,discriminatorPlots,1)
        lolT=plotutils.transposeLOL(listOfHistoLists)
        listOfHistoListsData=plotutils.createHistoLists_fromSuperHistoFile(outputpath,samples_data,discriminatorPlots,1)

    # plot simple MC plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeSimplePlots==True :
        print "Making simple MC plots."
        plotutils.writeLOLAndOneOnTop(plotutils.transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_controlplots')
        plotutils.writeListOfHistoListsAN(plotutils.transposeLOL([lolT[0]]+lolT[9:]),[samples[0]]+samples[9:],"",name+'/'+name+'_shapes',True,False,False,'histo',False,True,False)


    # Make MC Control plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeMCControlPlots==True :
        print "Making MC Control plots"
        print "skipping"
        lll=plotutils.createLLL_fromSuperHistoFileSyst(outputpath,samples[9:],discriminatorPlots,errorSystNamesNoQCD)
        labels=[plot.label for plot in discriminatorPlots]
        plotutils.plotDataMCanWsyst(listOfHistoListsData,plotutils.transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-2,name,[[lll,3354,ROOT.kBlack,True]],False,labels,True,analysis.plotBlinded)



if __name__ == "__main__":

   MainClock=ROOT.TStopwatch()
   MainClock.Start()
   main(pyrootdir, sys.argv[1:])
   print "TOTAL Elapsed time since beginning of analysis script", MainClock.RealTime()


