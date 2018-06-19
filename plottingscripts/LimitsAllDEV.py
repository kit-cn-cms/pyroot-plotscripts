#!/usr/bin/python2
import sys
import getopt
import os
import imp
import inspect
import ROOT
import pandas 
import ast

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])
workdir = pyrootdir+"/"+"workdir"

sys.path.append(pyrootdir+'/util')
sys.path.append(filedir+"/configs")

# local imports
import optBinning
import genPlots
import configClass
import samplesClass
import monitorTools
import plotParallel
import drawParallel
import haddParallel
import renameHistos
import makeDatacards
import analysisClass
import plotconfig_v14 as pltcfg

def main(pyrootdir, argv):
    print '''
    # ========================================================
    # welcome to main function - defining some variables
    # ========================================================
    '''
    # BIG TODO: decide what needs to be initialized by the secondary scripts
    # maybe give some information as an argument instead of doing it all over again
    # initializing everything only takes < 1 minute per script but takes a lot of disk i think

    # name of the analysis (i.e. workdir name)
    name = 'testrun6'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # creating workdir subfolder
    if not os.path.exists(workdir):
        os.makedirs(workdir)
        print("created workdir at "+str(workdir))
    
    # path to root file
    anaRootPath = workdir+'/output_limitInput.root'

    # Name of final discriminator, should not contain underscore
    discrname = 'finaldiscr'

    # define MEM discriminator variable
    # this is not used anymore as the information is written in the csv files in configdata
    # keep it for clarity
    # memexp='(memDBp>0.0)*(memDBp)+(memDBp<=0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # define BDT output variables (not used anymore)
    # bdtweightpath = "/nfs/dust/cms/user/kelmorab/Spring17BDTWeights/"
    # bdtset = "Spring17v2"
    # alternativebdtset = "Spring17v3_ttbb"

    # name of the csv files used in configdata folder
    configDataBaseName = "limitsAllv20"

    # used categories in configdata to be added
    usedCategories = ["JTBDT", "JT2D", "JTMEM", "MultiDNN", "JT_control"] 
    # usedCategories += ["JT2DOPTIMIZED", "JTBDTOPTIMIZED"]
    
    # signal process
    signalProcess = "ttH"

    # options for plotParallel
    plotOptions = {"cirun": True,  "haddParallel": True, "useOldRoot": True, 
        # the skipXXX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "skipPlotParallel": True, 
        "skipHaddParallel": True,
        "skipHaddFromWildcard": True,
        "skipRenaming": True,
        "skipDatacards": False}

    plotJson = "/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_latestAndGreatest.json"
    plotDataBases = [["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_Spring17_V1",False]] 
    plotInterfaces = ["../util/dNNInterfaces/dNNInterface_V6.py"]

    #############################################################################
    # there should be no information that needs hard coded adjusting below this #
    #############################################################################

    print '''
    # ========================================================
    # initializing analysisClass 
    # ========================================================
    '''

    # TODO make the analysisClass more essential - atm it is not really needed
    analysis = analysisClass.Analysis(workdir, argv, anaRootPath, signalProcess = signalProcess)

    #analysis=analysisClass.Analysis(name,argv,
        #'/nfs/dust/cms/user/mharrend/doktorarbeit/latest/ttbb-cutbased-analysis_limitInput.root')
    #analysis=analysisClass.Analysis(name,argv,
        #'/nfs/dust/cms/user/kelmorab/plotscriptsSpring17/Sep17/pyroot-plotscripts/NOTDEFINED/output_limitInput.root ', signalProcess='ttH')
    #analysis=analysisClass.Analysis(name,argv,
        #'/nfs/dust/cms/user/mharrend/doktorarbeit/output20170626-reference/workdir/ttbb-cutbased-analysis/output_limitInput.root')
    
    # TODO these options should be set automatically ?
    analysis.plotBlinded = True
    analysis.makeSimplePlots = True
    analysis.makeMCControlPlots = True
    analysis.makeDataCards = True
    analysis.additionalPlotVariables = False

    # Make sure proper plotconfig is loaded for either ttbb or ttH
    # TODO how is this determined?
    print "We will import the following plotconfig: ", analysis.getPlotConfig()

    # TODO maybe print chosen functions into a .json file in workdir
    analysis.printChosenOptions()

    # loading monitorTools module locally
    monitor = monitorTools.init(analysis.workdir)      

    #print '''    
    ## ========================================================
    ## NNFlow interface
    ## ========================================================
    #'''
    #
    # Create and configure NNFlow interface
    # NNFlowInterfacePath=os.getcwd()+'../util/dNNInterfaces/NNFlowInterface.py'
    # NNFlowInterface = imp.load_source("NNFlowInterface",NNFlowInterfacePath).theInterface()
    # NNFlowInterface.setDebugOutput(True)
    # NNFlowInterface.setModelFolderPath(
    #    '/nfs/dust/cms/user/mharrend/doktorarbeit/tensorflowModels/neural_network_v3/multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20/model')
    # NNFlowInterface.setModelName('multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20.ckpt')
    # NNFlowInterface.update()
    #
    # print "NNFlowInterfacePath: ", NNFlowInterfacePath


    print '''
    # ========================================================
    # prepare configdata
    # ========================================================
    '''

    configData = configClass.configData(pyrootdir = pyrootdir, 
                                    analysisClass = analysis,
                                    configDataBaseName = configDataBaseName, 
                                    usedCategories = usedCategories)

    monitor.printClass(configData, "init")

    # for better information flow, print and assert data
    configData.writeConfigDataToWorkdir(analysis.workdir)
    configData.assertData()
    configData.printLengths()

    # get the discriminator plots
    configData.genDiscriminatorPlots(discrname)
    monitor.printClass(configData, "after genDiscriminatorPlots")

    print '''    
    # ========================================================
    # define additional variables necessary for selection in plotparallel
    # ========================================================
    '''
    configData.getAddVariables()
    configData.getMEPDFAddVariables(
        "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/rate_factors_onlyinternal_powhegpythia.csv")
    # TODO additionalvariables.extend(NNFlowInterface.getAdditionalVariablesList())
    monitor.printClass(configData, "after getting additional Variables")

    # save addition variables information to workdir and print
    configData.printAddVariables(analysis.workdir)

    print '''
    # ========================================================
    # Check if additional (input) variables should be plotted
    # if necessary add them here to the discriminatorPlots
    # ========================================================
    '''
    if analysis.additionalPlotVariables:
        # Construct list with additional plot variables, 
        # will need name of discrs and plotPreselections for this
        print( "add additional plot variables")
        configData.getAdditionalDiscriminatorPlots(analysis)
        monitor.printClass(configData, "after adding additional plot variables")
    

    

    print '''    
    # ========================================================
    # loading samples and samples data
    # ========================================================
    '''
    samplesData = samplesClass.samplesData(pltcfg)
    monitor.printClass(samplesData, "init")
    
    print '''
    # ========================================================
    # add systematic samples
    # ========================================================
    '''
    samplesData.addSystSamples(
                        pltcfg.otherSystNames, pltcfg.otherSystFileNames,
                        pathReplace = ["'nominal'","filename"]
                        )

    ## WARNING: Adjust Slice for samples if changing ttbar contributions (is this still relevant?)
    # TODO systSample adding is still not optimal    
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
    

    monitor.printClass(samplesData, "after adding systsamples")

    print '''
    # ========================================================
    # finish up sample gathering
    # ========================================================
    '''
    samplesData.addAllSamples(addNames = pltcfg.weightSystNames)
    monitor.printClass(samplesData, "after adding all samples together")
    monitor.printClass(analysis, "before plot parallel")




    '''
    ===============================================================================================
    this is where the fun begins
    ===============================================================================================
    '''





    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel == False or analysis.plotNumber == None :
        #if not os.path.exists(analysis.rootFilePath):
            print '''
            # ========================================================
            # Doing plotParallel step since root file was not found.
            # ========================================================
            '''
            
            with monitor.Timer("plotParallel"):
                # initialize plotParallel class 
                pP = plotParallel.plotParallel(workdir = analysis.workdir,
                                        pltcfg = pltcfg,
                                        configData = configData,
                                        samplesData = samplesData)

                monitor.printClass(pP, "init")
                # set some changed values
                pP.setJson(plotJson)
                pP.setDataBases(plotDataBases)
                pP.setAddInterfaces(plotInterfaces)
                pP.setOptions( plotOptions )
    
                # run plotParallel
                monitor.printClass(pP, "before run")
                pP.run()
                monitor.printClass(pP, "after run")



            # if pP.haddFiles is a list we are probably in the first iteration
            # cross check if plotParallel has terminated successfully
            # program exits if not
            pP.checkTermination()
    


            if analysis.getActivatedOptimizedRebinning():
                print '''
                # ========================================================
                # Doing OptimizedRebinning
                # ========================================================
                '''
                if analysis.getSignalProcess() == 'ttbb':
                    # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                    # TODO check the optimizedBinning function and adjust arguments to new structure
                    # TODO rework samples splitting to be automated in samplesDataClass?
                    # TODO call this only once and determine bkg/signal samples in the function itself
                    with monitor.Timer("optimizeBinning"):
                        optBinning.optimizeBinning(
                            pP.getRootPath(),
                            signalsamples = [samplesData.samples[0:3]], 
                            backgroundsamples = samplesData.samples[3:],
                            additionalSamples = samplesData.controlSamples, 
                            plots = configData.getDiscriminatorPlots(), 
                            systnames = samplesData.allNames, 
                            minBkgPerBin = 2.0, 
                            optMode = analysis.getOptimzedRebinning(),
                            considerStatUnc = False, 
                            maxBins = 20, 
                            minBins = 2,
                            verbosity = 2)

                elif analysis.getSignalProcess() == 'ttH':
                    # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. 
                    # Rest: background samples
                    with monitor.Timer("optimizeBinning"):
                        optBinning.optimizeBinning(
                            pP.getRootPath(),
                            signalsamples = [samplesData.samples[0]], 
                            backgroundsamples = samplesData.samples[9:],
                            additionalSamples= samplesData.samples[1:9] + samplesData.controlSamples, 
                            plots = configData.getDiscriminatorPlots(), 
                            systnames = samplesData.allNames, 
                            minBkgPerBin = 2.0, 
                            optMode = analysis.getOptimzedRebinning(),
                            considerStatUnc = False, 
                            maxBins = 20, 
                            minBins = 2,
                            verbosity = 2)
                else:
                    print("WARNING - could not find signal process")
                    print("not doing optimized rebinning")



            # hadd histo files before renaming. The histograms are actually already renamed. 
            # But the checkbins thingy will not have been done yet.
            print '''
            # ========================================================
            # hadding from wildcard
            # ========================================================
            '''
            with monitor.Timer("haddFilesFromWildCard"):
                haddParallel.haddWard( input = pP.getHaddOutPath(),
                                        outName = pP.getRootPath(),
                                        subName = "haddParts",
                                        nHistosRemainSame = True,
                                        skipHadd = plotOptions["skipHaddFromWildcard"] )
             
   



            # Deactivate check bins functionality in renameHistos 
            #   if additional plot variables are added via analysis class
            if os.path.exists( pP.setLimitPath() ) and analysis.plotNumber != None:
                monitor.printClass(pP, "after setlimitPath - true")
                print( "renamed file already exists - skipping renaming histos" )

            else:
                monitor.printClass(pP, "after setlimitPath - false")
                print '''
                # ========================================================
                # renaming Histograms
                # ========================================================
                '''
                # in this function the variable self.renameInput is set
                # if hadd files were created during plotParallel
                #       (which is equivalent to THEoutputpath == list) 
                # the renameInput is set to pP.getHaddFiles (a.k.a. the list of hadd files)
                # if no hadd files were created during plotparallel
                #       (which is equivalent to THEoutputlath == str)
                # the renameInput is set to pp.getOutPath (a.ka. the path to output.root)
                pP.setRenameInput()
                monitor.printClass(pP, "after setting rename input")
                with monitor.Timer("renameHistos"):
                    renameHistos.renameHistos(
                            inFiles = pP.getRenameInput(),
                            outFile = pP.getOutPath(),
                            systNames = samplesData.allNames,
                            checkBins = True,
                            prune = False,
                            Epsilon = 0.0,
                            skipRenaming = plotOptions["skipRenaming"])

            print '''
            # ========================================================
            # adding data with plotParallel
            # ========================================================
            '''
            with monitor.Timer("addRealData"):
                # real data with ttH
                pP.addData(samples = samplesData.controlSamples, discr = discrname)

                # pseudo data without ttH
                # pP.addData(samples = samplesData.samples[9:], discr = discrname)



        # -- plot parallel step is done here --
    else:
        print("not doing plotParallel step")
        # initialize empty plotParalllel instance to reference pP.getOutPath()
        pP = plotParallel.plotParallel.empty(analysis.workdir, analysis.rootFilePath)
        monitor.printClass(pP, "init empty pP")





    print("########## DONE WITH PLOTPARALLEL STEP ##########")
    pP.checkTermination()       
    print("at the moment the outputpath is "+str(pP.getOutPath()))
    print("#################################################")
    monitor.printClass(pP, "after plot parallel completely done")






    if (analysis.doDrawParallel==False or analysis.plotNumber == None) and analysis.makeDataCards == True :
        #limittools.addRealData(outputpath,[s.nick for s in samples_data],binlabels,discrname)
        print '''
        # ========================================================
        # Making Datacards.
        # ========================================================
        '''
        # init datacards path
        datacardsPath = analysis.workdir+"/datacards"
        if not os.path.exists(datacardsPath):
            os.makedirs(datacardsPath)

        with monitor.Timer("makeDatacardsParallel"):
            makeDatacards.makeDatacardsParallel(
                            filePath = pP.getOutPath(),
                            outPath = datacardsPath,
                            categories = configData.getBinlabels(),
                            doHdecay = True,
                            discrname = discrname,
                            datacardmaker = "mk_datacard_JESTest13TeVPara",
                            skipDatacards = plotOptions["skipDatacards"])


    # =============================================================================================
    # Invoke drawParallel step
    # =============================================================================================
    if analysis.doDrawParallel==True and analysis.plotNumber == None :
        print '''
        # ========================================================
        # Starting DrawParallel
        # ========================================================
        '''
        with monitor.Timer("DrawParallel"):
            drawParallel.drawParallel(
                        ListOfPlots = configData.getDiscriminatorPlots(),
                        workdir = analysis.workdir,
                        PathToSelf = os.path.realpath(inspect.getsourcefile(lambda:0)),
                        # Hand over opts to keep commandline options
                        opts = analysis.opts)
        print '''
        # ========================================================
        # this is the end of the script 
        # ========================================================
        '''




    # =============================================================================================
    # everything beyond this point is called by the secondary scripts
    # =============================================================================================
    if analysis.doDrawParallel==True and analysis.plotNumber != None :
        print("we have a plotNumber --- changing discriminatorPlots")
        monitor.printClass(configData, "before adjusting discr plots")
        configData.adjustDiscriminatorPlots()
        monitor.printClass(configData, "after adjusting discr plots")






    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and (analysis.makeSimplePlots==True or analysis.makeMCControlPlots==True or analysis.makeEventYields==True):
        print '''
        # ========================================================
        # Creating lists for later use
        # ========================================================
        '''
        # TODO this sucks - rework in any case, put the information into a DataFrame for example
        gP = genPlots.genPlots( outPath = pP.getOutPath(),
                            plots = configData.getDiscriminatorPlots(),
                            workdir = workdir,
                            rebin = 1)

        gP.genList(samples = samplesData.samples, listName = "histoList")
        gP.genTranspose(listName = "histoList")
        gP.genList(samples = samplesData.controlSamples, listName = "dataList")
        monitor.printClass(gP, "after creating init lists")







    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeSimplePlots==True :
        print '''
        # ========================================================
        # Making simple MC plots
        # ========================================================
        '''
        with monitor.Timer("makingSimpleMCplots"):
            options = {"stack": True}
            gP.makeSimpleControlPlots( listName = "histoList", listIndex = 9, options = options)

            options = {"normalize": True}
            gP.makeSimpleShapePlots( listName = "histoList", listIndex = 9, options = options)

            monitor.printClass(gP, "after making simple MC plots")



    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeMCControlPlots==True :
        print '''
        # ========================================================
        # Making MC Control plots
        # ========================================================
        '''
        with monitor.Timer("makingMCControlPlots"):
            nestedHistsConfig = {}

            # generate the llloflist internally
            gP.genNestedHistList(listName = "histoList", listIndex = 9,
                                        systNames = pltcfg.errorSystNamesNoQCD, 
                                        nestedName = "histoList")

            monitor.printClass(gP, "after generating nested hist list")
            # set config of llloflist
            nestedHistsConfig["histoList"] = {"style": 3354, 
                                            "color": ROOT.kBlack, 
                                            "doRateSysts": False}

            #set general plotoption
            options = {"factor": -2, "ratio": True, "blinded": analysis.plotBlinded}

            # makint the control plots
            gP.makeControlPlots( listName = "histoList", listIndex = 9,
                                        dataName = "dataList", nestedHistsConfig = nestedHistsConfig,
                                        options = options )

            monitor.printClass(plotCass, "after making control plots")



if __name__ == "__main__":

    main(pyrootdir, sys.argv[1:])


