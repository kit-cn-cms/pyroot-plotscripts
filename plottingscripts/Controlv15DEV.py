#!/usr/bin/python2
import sys
import os
import imp
import inspect
import ROOT

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)

# local imports
import util.analysisClass as analysisClass
import util.optBinning as optBinning
import util.genPlots as genPlots
import util.configClass as configClass
import util.monitorTools as monitorTools
import util.plotParallel as plotParallel
import util.drawParallel as drawParallel
import util.haddParallel as haddParallel
import util.renameHistos as renameHistos
import util.makeDatacards as makeDatacards

def main(pyrootdir, argv):
    print '''
    # ========================================================
    # welcome to main function - defining some variables
    # ========================================================
    '''
    # name of the analysis (i.e. workdir name)
    name = 'plotControl15'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # creating workdir subfolder
    if not os.path.exists(workdir):
        os.makedirs(workdir)
        print("created workdir at "+str(workdir))
    
    # path to root file
    rootPathForAnalysis = workdir+'/output_syst.root'

    # signal process
    signalProcess = "ttH"

    # Name of final discriminator, should not contain underscore
    discrName = 'finaldiscr'

    # define MEM discriminator variable
    memexp = '(memDBp>0.0)*(memDBp)+(memDBp<=0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # name of the csv files used in configdata folder
    configDataBaseName = "controlPlotsv13"

    # name of plotconfig
    pltcfgName = "v15"

    # file for MEPDFs/LHEWeights
    MEPDFCSVFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/rate_factors_onlyinternal_powhegpythia.csv"

    # script options
    analysisOptions = {
        # general options
        "plotBlinded":          False,  # blind region
        "cirun":                False,  # test run with less samples
        "haddParallel":         False,  # parallel hadding instead of non-parallel
        "useOldRoot":           True,   # use existing root file if it exists (skips plotParallel)
        # options to activate parts of the script
        "optimizedRebinning":   "equalBinWidth",
        "haddFromWildcard":     False,
        "makeDataCards":        False,
        "addData":              False,  # adding real data 
        "singleExecute":        False,  # for non parallel drawing
        "drawParallel":         True,
        # options for drawParallel/singleExecute sub programs
        "makeSimplePlots":      True,   
        "makeMCControlPlots":   True,
        "makeEventYields":      True,
        # the skipX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "skipPlotParallel":     False, 
        "skipHaddParallel":     False,
        "skipHaddFromWildcard": False,  
        "skipRenaming":         False,
        "skipDatacards":        False} 

    # data for plotParallel step
    plotJson = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/treejson_v13.json"
    plotDataBases = []
    plotInterfaces = []

    # datacardmaker
    datacardmaker = "mk_datacard_JESTest13TeVPara"

    #############################################################################
    # there should be no information that needs hard coded adjusting below this #
    #############################################################################

    print '''
    # ========================================================
    # initializing analysisClass 
    # ========================================================
    '''
    analysis = analysisClass.analysisConfig(
        workdir = workdir, 
        pyrootdir = pyrootdir, 
        rootPath = rootPathForAnalysis, 
        signalProcess = signalProcess, 
        pltcfgName = pltcfgName,
        discrName = discrName)

    analysis.initArguments( argv )
    analysis.initAnalysisOptions( analysisOptions )

    pltcfg = analysis.initPlotConfig()
    print "We will import the following plotconfig: ", analysis.getPlotConfig()

    analysis.printChosenOptions()

    # loading monitorTools module locally
    monitor = monitorTools.init(analysis.workdir)      
    monitor.printClass(analysis, "init")

    #print '''    
    # TODO: rework not yet done
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
    configData = configClass.configData(
        analysisClass = analysis,
        configDataBaseName = configDataBaseName)

    configData.initData()

    # get the discriminator plots
    configData.genDiscriminatorPlots(memexp)
    configData.writeConfigDataToWorkdir()
    monitor.printClass(configData, "init")

    print '''    
    # ========================================================
    # define additional variables necessary for selection in plotparallel
    # ========================================================
    '''
    configData.getAddVariables()
    #configData.getMEPDFAddVariables( MEPDFCSVFile )
    # TODO additionalvariables.extend(NNFlowInterface.getAdditionalVariablesList())
    monitor.printClass(configData, "after getting additional Variables")

    # save addition variables information to workdir and print
    configData.printAddVariables()

    if analysis.additionalPlotVariables:
        print '''
        # ========================================================
        # Check if additional (input) variables should be plotted
        # if necessary add them here to the discriminatorPlots
        # ========================================================
        '''
        # Construct list with additional plot variables, 
        # will need name of discrs and plotPreselections for this
        print( "add additional plot variables")
        configData.getAdditionalDiscriminatorPlots()
        monitor.printClass(configData, "after adding additional plot variables")
    

    

    print '''    
    # ========================================================
    # loading samples and samples data
    # ========================================================
    '''
    configData.initSamples()


    print '''
    # ========================================================
    # done with preprocessing
    # ========================================================
    '''


    if analysis.plotNumber == None or analysis.singleExecute:
        # plot everything, except during drawParallel step
        # Create file for data cards
        #if not analysis.drawParallel:
        #if analysis.doDrawParallel == False or analysis.plotNumber == None :
        print '''
        # ========================================================
        # Doing plotParallel step since root file was not found.
        # ========================================================
        '''
        
        with monitor.Timer("plotParallel"):
            # initialize plotParallel class 
            pP = plotParallel.plotParallel(
                analysis = analysis,
                configData = configData)

            monitor.printClass(pP, "init")
            # set some changed values
            pP.setJson(plotJson)
            pP.setDataBases(plotDataBases)
            pP.setAddInterfaces(plotInterfaces)
            # pP.setMEPDFCSV( MEPDFCSVFile )
            # pP.setCatNames([''])
            # pP.setCatSelections(['1.'])
            pP.setMaxEvts(1000000)

            # run plotParallel
            pP.run()

        pP.checkTermination()

        if analysis.optimizedRebinning:
        #if analysis.getActivatedOptimizedRebinning():
            print '''
            # ========================================================
            # Doing OptimizedRebinning
            # ========================================================
            '''
            #TODO rework: call once, and get signalProcess, samples, ... from analysisConfig data
            if analysis.signalProcess == 'ttbb':
                # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                # TODO check the optimizedBinning function and adjust arguments to new structure
                # TODO rework samples splitting to be automated in samplesDataClass?
                # TODO call this only once and determine bkg/signal samples in the function itself
                with monitor.Timer("optimizeBinning"):
                    optBinning.optimizeBinning(
                        infname = analysis.ppRootPath,
                        signalsamples = configData.samples[0:1], 
                        backgroundsamples = configData.samples[1:],
                        additionalSamples = configData.controlSamples, 
                        plots = configData.getDiscriminatorPlots(), 
                        systnames = configData.allSystNames, 
                        minBkgPerBin = 2.0, 
                        optMode = analysis.optimizedRebinning,
                        considerStatUnc = False, 
                        maxBins = 20, 
                        minBins = 2,
                        verbosity = 0)

            elif analysis.signalProcess == 'ttH':
                # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. 
                # Rest: background samples
                with monitor.Timer("optimizeBinning"):
                    optBinning.optimizeBinning(
                        analysis.ppRootPath,
                        signalsamples = [configData.samples[0]], 
                        backgroundsamples = configData.samples[1:],
                        additionalSamples = configData.controlSamples, 
                        plots = configData.getDiscriminatorPlots(), 
                        systnames = configData.allSystNames, 
                        minBkgPerBin = 2.0, 
                        optMode = analysis.optimizedRebinning,
                        considerStatUnc = False, 
                        maxBins = 20, 
                        minBins = 3,
                        verbosity = 0)
            else:
                print("WARNING - could not find signal process")
                print("not doing optimized rebinning")



        # hadd histo files before renaming. The histograms are actually already renamed. 
        # But the checkbins thingy will not have been done yet.
        if analysis.haddFromWildcard:
            print '''
            # ========================================================
            # hadding from wildcard
            # ========================================================
            '''
            with monitor.Timer("haddFilesFromWildCard"):
                haddParallel.haddSplitter( input = pP.getHaddOutPath(),
                    outName = analysis.ppRootPath,
                    subName = "haddParts",
                    nHistosRemainSame = True,
                    skipHadd = analysis.skipHaddFromWildcard)
        


        # Deactivate check bins functionality in renameHistos 
        #   if additional plot variables are added via analysis class
        if os.path.exists( analysis.setRenamedPath(name = "syst") ):
        #if os.path.exists( pP.setRenamedPath() ) and (plotOptions["skipRenaming"] or analysis.plotNumber != None):
            print( "renamed file already exists - skipping renaming histos" )
        elif analysis.skipRenaming:
            print("skipping renaming TODO")
            # WIP rename skip TODO
        else:
            print '''
            # ========================================================
            # renaming Histograms
            # ========================================================
            '''

            pP.setRenameInput()
            # in this function the variable self.renameInput is set
            # if hadd files were created during plotParallel
            #       the renameInput is set to pP.getHaddFiles 
            #       (a.k.a. the list of hadd files)
            # if no hadd files were created during plotparallel
            #       the renameInput is set to pp.getOutPath 
            #       (a.ka. the path to output.root)
            with monitor.Timer("renameHistos"):
                renameHistos.renameHistos(
                    inFiles = pP.getRenameInput(),
                    outFile = analysis.renamedPath,
                    systNames = configData.allSystNames,
                    checkBins = True,
                    prune = False,
                    Epsilon = 0.0,
                    skipRenaming = analysis.skipRenaming)

            if analysis.addData:
                print '''
                # ========================================================
                # adding data with plotParallel
                # ========================================================
                '''
                with monitor.Timer("addRealData"):
                    # real data with ttH
                    pP.addData(samples = configData.controlSamples)
                
                    # pseudo data without ttH
                    # pP.addData(samples = configData.samples[9:])
        

        pP.checkTermination()       
        monitor.printClass(pP, "after plot parallel completely done")

        print("########## DONE WITH PLOTPARALLEL STEP ##########")
        print("at the moment the outputpath is "+str(analysis.renamedPath))
        print("#################################################")

        if analysis.makeDatacards:
        #if (analysis.doDrawParallel==False or analysis.plotNumber == None) and analysis.makeDataCards == True :
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
                    filePath = analysis.renamedPath,
                    outPath = datacardsPath,
                    categories = configData.getBinlabels(),
                    doHdecay = True,
                    discrname = analysis.discrName,
                    datacardmaker = datacardmaker,
                    skipDatacards = analysis.skipDatacards)


        # =============================================================================================
        # Invoke drawParallel step
        # =============================================================================================
        if analysis.drawParallel:
        #if analysis.doDrawParallel==True and analysis.plotNumber == None :
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
    elif analysis.plotNumber != None or analysis.singleExecute:
        print("not doing plotParallel step")
        if analysis.drawParallel:
        #if analysis.doDrawParallel==True and analysis.plotNumber != None :
            print("we have a plotNumber --- changing discriminatorPlots")
            configData.getDiscriminatorPlotByNumber()
            print("the discriminator plots are now:" +str(configData.getDiscriminatorPlots()))


        if analysis.makeSimplePlots or analysis.makeMCControlPlots or analysis.makeEventYields:
        #if (analysis.doDrawParallel==False or analysis.plotNumber != None) and (analysis.makeSimplePlots==True or analysis.makeMCControlPlots==True or analysis.makeEventYields==True):
            print '''
            # ========================================================
            # Creating lists for later use
            # ========================================================
            '''
            gP = genPlots.genPlots( outPath = analysis.renamedPath,
                plots = configData.getDiscriminatorPlots(),
                plotdir = analysis.getPlotPath(),
                rebin = 1)

            histoList = gP.genList(samples = configData.samples, listName = "histoList")
            dataList = gP.genList(samples = configData.controlSamples, listName = "dataList")
            monitor.printClass(gP, "after creating init lists")






        if analysis.makeSimplePlots:
        #if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeSimplePlots==True :
            print '''
            # ========================================================
            # Making simple MC plots
            # ========================================================
            '''
            with monitor.Timer("makingSimpleMCplots"):
                # creating control plots
                controlPlotsOptions = {
                    "factor":           -1,
                    "logscale":         False,
                    "canvasOptions":    "histo",
                    "normalize":        False,
                    "stack":            True, # not default
                    "ratio":            False,
                    "sepaTest":         False}
                gP.makeSimpleControlPlots( 
                    dataConfig = genPlots.Config(name = histoList, index = 1), 
                    options = controlPlotsOptions)

                # creating shape plots
                shapePlotsOptions = {
                    "logscale":         False,
                    "canvasOptions":    "histo",
                    "normalize":        True, # not default
                    "stack":            False,
                    "ratio":            False,
                    "statTest":         False,
                    "sepaTest":         False}
                gP.makeSimpleShapePlots( 
                    dataConfig = genPlots.Config(name = histoList, index = 1), 
                    options = shapePlotsOptions)

                monitor.printClass(gP, "after making simple MC plots")



        if analysis.makeMCControlPlots:
        #if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeMCControlPlots==True :
            print '''
            # ========================================================
            # Making MC Control plots
            # ========================================================
            '''
            with monitor.Timer("makingMCControlPlots"):

                # generate the llloflist internally
                gP.genNestedHistList(
                    #listName = "histoList", listIndex = 1, 
                    dataConfig = genPlots.Config( name = histoList, index = 1 ),
                    systNames = pltcfg.errorSystNames, 
                    outName = histoList)

                monitor.printClass(gP, "after generating nested hist list")
                # set config of llloflist
                nestedHistsConfig = {}
                nestedHistsConfig[histoList] = {
                    "style":            3354, 
                    "color":            ROOT.kBlack, 
                    "doRateSysts":      True}


                #set general plotoption
                controlPlotsOptions = {
                    "factor":           -2, #not default
                    "logscale":         False,
                    "canvasOptions":    "histo",
                    "ratio":            True, # not default
                    "blinded":          analysis.plotBlinded} #not default
                # making the control plots
                gP.makeControlPlots(
                    dataConfig = genPlots.Config(name = dataList, index = 0),
                    controlConfig = genPlots.Config(name = histoList, index = 1),
                    sampleConfig = genPlots.Config(name = histoList, index = 1),
                    headHist = histoList,
                    headSample = histoList,
                    nestedHistsConfig = nestedHistsConfig,
                    options = controlPlotsOptions,
                    outName = "controlPlots")

                controlPlotsOptions["logscale"] = True
                gP.makeControlPlots(
                    dataConfig = genPlots.Config(name = dataList, index = 0),
                    controlConfig = genPlots.Config(name = histoList, index = 1),
                    sampleConfig = genPlots.Config(name = histoList, index = 1),
                    headHist = histoList,
                    headSample = histoList,
                    nestedHistsConfig = nestedHistsConfig,
                    options = controlPlotsOptions,
                    outName = "controlPlots_LOG")


                    #listName = "histoList", listIndex = 1,
                    #dataName = "dataList", nestedHistsConfig = nestedHistsConfig,
                    #options = controlPlotsOptions )

            monitor.printClass(gP, "after making control plots")

        if analysis.makeEventYields:
            print '''
            # ========================================================
            # Making Event Yields
            # ========================================================
            '''
            with monitor.Timer("makeEventYields"):
                gP.makeEventYields(
                    categories = configData.getEventYieldCategories(),
                    listName = histoList, 
                    dataName = dataList, 
                    nameRequirements = ["JT", "N_Jets"]
                    )


if __name__ == "__main__":

    main(pyrootdir, sys.argv[1:])


