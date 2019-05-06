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
    name = 'ttHAnalysis_2017_LegacyStrategyBaseline'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # creating workdir subfolder
    if not os.path.exists(workdir):
        os.makedirs(workdir)
        print("created workdir at "+str(workdir))
    
    # path to root file
    rootPathForAnalysis = workdir+'/output_limitInput.root'

    # dataera
    dataera = "2017_deepCSV"

    # signal process
    signalProcess = "ttH"

    # Name of final discriminator, should not contain underscore
    discrName = 'finaldiscr'

    # define MEM discriminator variable
    memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # configs
    config          = "pltcfg_ttH17"
    variable_cfg    = "ttH17_addVariables"
    plot_cfg        = "LegacyStrategyStudyBaseline_Plots"
    syst_cfg        = "LegacyStrategyStudy_Systematics"

    # file for rate factors
    #rateFactorsFile = pyrootdir + "/data/rate_factors_onlyinternal_powhegpythia.csv"
    rateFactorsFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/rate_factors_V2.csv"

    # script options
    analysisOptions = {
        # general options
        "usePseudoData":          False,  # blind region
        "testrun":              False,  # test run with less samples
        "stopAfterCompile":     False,   # stop script after compiling
        # options to activate parts of the script
        "haddFromWildcard":     True,
        "makeDataCards":        True,
        "addData":              True,  # adding data 
        "drawParallel":         True,
        # options for drawParallel/singleExecute sub programs
        "makeSimplePlots":      True,
        "makeMCControlPlots":   True,
        "makeEventYields":      True,
        # the skipX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "skipPlotParallel":     True,
        "skipHaddParallel":     True,
        "skipHaddFromWildcard": True,
        "skipRenaming":         True,
        "skipDatacards":        False}

    plotJson = "/nfs/dust/cms/user/swieland/ttH/pyroot-plotscripts/LegacyStudy_treejson.json"
    plotDataBases = [["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_ttH_2018_newJEC",True]] 
    memDataBase = "/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBase_ttH2018/MEMDataBase/MEMDataBase/"
    dnnInterface = {"interfacePath":    pyrootdir+"/util/dNNInterfaces/MLfoyInterface.py",
                    "checkpointFiles":  "/nfs/dust/cms/user/swieland/ttH/LegacyStudy/DNNs/BaseLine/"}

    # path to datacardMaker directory
    datacardmaker = "/nfs/dust/cms/user/lreuter/forPhilip/datacardMaker"

    print '''
    # ========================================================
    # initializing analysisClass 
    # ========================================================
    '''

    # save a lot of useful information concerning the analysis
    analysis = analysisClass.analysisConfig(
        workdir         = workdir, 
        pyrootdir       = pyrootdir, 
        rootPath        = rootPathForAnalysis, 
        signalProcess   = signalProcess, 
        pltcfgName      = config,
        discrName       = discrName,
        dataera         = dataera)

    analysis.initArguments( argv )
    analysis.initAnalysisOptions( analysisOptions )

    pltcfg = analysis.initPlotConfig()
    print "We will import the following plotconfig: ", analysis.getPlotConfig()

    # loading monitorTools module locally
    monitor = monitorTools.init(analysis.workdir)
    monitor.printClass(analysis, "init")

    print '''
    # ========================================================
    # prepare configdata
    # ========================================================
    '''

    configData = configClass.configData(
        analysisClass   = analysis,
        variable_config = variable_cfg,
        plot_config     = plot_cfg,
        execute_file    = os.path.realpath(inspect.getsourcefile(lambda:0)))

    configData.initSystematics(systconfig = syst_cfg)

    configData.initData()

    # get the discriminator plots
    configData.genDiscriminatorPlots(memexp, dnnInterface)
    configData.writeConfigDataToWorkdir()
    monitor.printClass(configData, "init")

    print '''    
    # ========================================================
    # define additional variables necessary for selection in plotparallel
    # ========================================================
    '''
    configData.getAddVariables()

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

    if analysis.plotNumber == None:
        # plot everything, except during drawParallel step
        # Create file for data cards
        print '''
        # ========================================================
        # starting with plotParallel step
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
            pP.setMEMDataBase(memDataBase)
            pP.setDNNInterface(dnnInterface)
            pP.setMaxEvts(1000000)
            pP.setRateFactorsFile(rateFactorsFile)
            pP.setSampleForVariableSetup(configData.samples[9])

            # run plotParallel
            pP.run()

        pP.checkTermination()
        monitor.printClass(pP, "after plotParallel")



        # hadd histo files before renaming. The histograms are actually already renamed. 
        # But the checkbins thingy will not have been done yet.
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
        if os.path.exists( analysis.setRenamedPath(name = "limitInput") ):
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
            #       (which is equivalent to THEoutputpath == list) 
            #       the renameInput is set to pP.getHaddFiles 
            #       (a.k.a. the list of hadd files)
            # if no hadd files were created during plotparallel
            #       (which is equivalent to THEoutputlath == str)
            #       the renameInput is set to pp.getOutPath 
            #       (a.ka. the path to output.root)
            print(pP.getRenameInput())
            print(analysis.renamedPath)

            with monitor.Timer("renameHistos"):
                renameHistos.renameHistos(
                    inFiles         = pP.getRenameInput(),
                    outFile         = analysis.renamedPath,
                    systNames       = configData.allSystNames,
                    checkBins       = True,
                    prune           = True,
                    Epsilon         = 0.0,
                    skipRenaming    = analysis.skipRenaming)

        if analysis.addData:
            print '''
            # ========================================================
            # adding data with plotParallel
            # ========================================================
            '''
            with monitor.Timer("addRealData"):
                if analysis.usePseudoData:
                    # pseudo data without ttH
                    pP.addData(samples = configData.samples[9:])
                else:
                    # real data with ttH
                    pP.addData(samples = configData.controlSamples)

        

        pP.checkTermination()       
        monitor.printClass(pP, "after plotParallel completely done")

        print("########## DONE WITH PLOTPARALLEL STEP ##########")
        print("at the moment the outputpath is "+str(analysis.renamedPath))
        print("#################################################")

        if analysis.makeDatacards:
            print '''
            # ========================================================
            # Making Datacards.
            # ========================================================
            '''
            with monitor.Timer("makeDatacardsParallel"):
                makeDatacards.makeDatacardsParallel(
                    filePath            = analysis.renamedPath,
                    workdir             = analysis.workdir,
                    categories          = configData.getBinlabels(),
                    doHdecay            = True,
                    discrname           = analysis.discrName,
                    datacardmaker       = datacardmaker,
                    skipDatacards       = analysis.skipDatacards)


        # =============================================================================================
        # Invoke drawParallel step
        # =============================================================================================
        if analysis.drawParallel:
            print '''
            # ========================================================
            # Starting DrawParallel
            # ========================================================
            '''
            # this step reexecutes this top level script once for each discriminator plot
            with monitor.Timer("DrawParallel"):
                drawParallel.drawParallel(
                    ListOfPlots = configData.getDiscriminatorPlots(),
                    workdir     = analysis.workdir,
                    PathToSelf  = os.path.realpath(inspect.getsourcefile(lambda:0)),
                    # Hand over opts to keep commandline options
                    opts        = analysis.opts)
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
            print("we have a plotNumber --- changing discriminatorPlots")
            configData.getDiscriminatorPlotByNumber()

        if analysis.makeSimplePlots or analysis.makeMCControlPlots or analysis.makeEventYields:
            print '''
            # ========================================================
            # Creating lists for later use
            # ========================================================
            '''
            gP = genPlots.genPlots( 
                outPath = analysis.renamedPath,
                plots   = configData.getDiscriminatorPlots(),
                plotdir = analysis.getPlotPath(),
                rebin   = 1)

            histoList       = gP.genList(samples = configData.samples)
            dataList        = gP.genList(samples = configData.controlSamples)
            pseudodataList  = gP.genList(samples = [configData.samples[0]]+configData.samples[9:])
            monitor.printClass(gP, "after creating init lists")





# 
        if analysis.makeSimplePlots:
            print '''
            # ========================================================
            # Making simple MC plots
            # ========================================================
            '''
            with monitor.Timer("makingSimpleMCplots"):
                # creating control plots
                controlPlotOptions = {
                    "factor":           -1,
                    "logscale":         False,
                    "canvasOptions":    "histo",
                    "normalize":        False,
                    "stack":            True, # not default
                    "ratio":            False,
                    "sepaTest":         False}
                sampleConfig = genPlots.Config(
                    histograms  = histoList,
                    sampleIndex = 9)
                gP.makeSimpleControlPlots( sampleConfig, controlPlotOptions )

                # creating shape plots
                shapePlotOptions = {
                    "logscale":         False,
                    "canvasOptions":    "histo",
                    "normalize":        True, # not default
                    "stack":            False,
                    "ratio":            False,
                    "statTest":         False,
                    "sepaTest":         False}
                sampleConfig = genPlots.Config(
                    histograms  = dataList,
                    sampleIndex = 9)
                gP.makeSimpleShapePlots( sampleConfig, shapePlotOptions )

                monitor.printClass(gP, "after making simple MC plots")



        if analysis.makeMCControlPlots:
            print '''
            # ========================================================
            # Making MC Control plots
            # ========================================================
            '''
            with monitor.Timer("makingMCControlPlots"):
                sampleConfig = genPlots.Config(
                    histograms  = histoList,
                    sampleIndex = 9)

                # generate the llloflist internally
                sampleConfig.genNestedHistList(
                    genPlotsClass = gP,
                    systNames = configData.plots)
                sampleConfig.setErrorbandConfig({
                    "style":        3354, 
                    "color":        ROOT.kBlack, 
                    "doRateSysts":  False})
        
                if analysis.usePseudoData:
                    pseudodataConfig = genPlots.Config(
                        histograms  = pseudodataList,
                        sampleIndex = 0)

                    #set general plotoption
                    controlPlotOptions = {
                        "factor":           -2, #not default
                        "logscale":         False,
                        "canvasOptions":    "histo",
                        "ratio":            True, # not default
                        "blinded":          False} #not default
                    # making the control plots
                    gP.makeControlPlots(
                        sampleConfig = sampleConfig,
                        dataConfig   = pseudodataConfig,
                        options      = controlPlotOptions,
                        outName      = "controlPlots_pseudodata")


                    controlPlotOptions["logscale"] = True
                    gP.makeControlPlots(
                        sampleConfig = sampleConfig,
                        dataConfig   = pseudodataConfig,
                        options      = controlPlotOptions,
                        outName      = "controlPlots_pseudodata_LOG")

                else:
                    dataConfig = genPlots.Config(
                        histograms  = dataList,
                        sampleIndex = 0)

                    #set general plotoption
                    controlPlotOptions = {
                        "factor":           -2, #not default
                        "logscale":         False,
                        "canvasOptions":    "histo",
                        "ratio":            True, # not default
                        "blinded":          False} #not default
                    # making the control plots
                    gP.makeControlPlots(
                        sampleConfig = sampleConfig,
                        dataConfig   = dataConfig,
                        options      = controlPlotOptions,
                        outName      = "controlPlots_data")


                    controlPlotOptions["logscale"] = True
                    gP.makeControlPlots(
                        sampleConfig = sampleConfig,
                        dataConfig   = dataConfig,
                        options      = controlPlotOptions,
                        outName      = "controlPlots_data_LOG")
                    

            monitor.printClass(gP, "after making control plots")

        if analysis.makeEventYields:
            print '''
            # ========================================================
            # Making Event Yields
            # ========================================================
            '''
            with monitor.Timer("makeEventYields"):
                gP.makeEventYields(
                    categories    = configData.getEventYieldCategories(),
                    samplesConfig = histoList,
                    dataConfig    = pseudodataList,
                    nameRequirements = ["node"]
                    )


if __name__ == "__main__":

    main(pyrootdir, sys.argv[1:])


