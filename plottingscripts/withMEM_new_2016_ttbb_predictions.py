#!/usr/bin/python2
import sys
import os
import imp
import inspect
import optparse
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)

# local imports
import util.analysisClass as analysisClass
import util.configClass as configClass
import util.monitorTools as monitorTools
import util.plotParallel as plotParallel
import util.makePlots as makePlots
import util.haddParallel as haddParallel
import util.checkHistos as checkHistos
import util.makeDatacards as makeDatacards

def main(pyrootdir, opts):
    print ('''
    # ========================================================
    # welcome to main function - defining some variables
    # ========================================================
    ''')
    # name of the analysis (i.e. workdir name)
    name = 'withMEM_final_newJECrun/2016_ttbb_predictions_acceptance'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # signal process
    signalProcess = "ttH"
    nSigSamples   = 0

    # dataera
    dataera = "2016"

    # Name of final discriminator, should not contain underscore
    discrName = ''
    nom_histname_template = "$CHANNEL__$PROCESS"
    syst_histname_template = nom_histname_template + "__$SYSTEMATIC"
    histname_separator = "__"

    # define MEM discriminator variable
    memexp = "(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)"
    # configs
    config          = "legacyAnalysis/samples_2016_ttbb_predictions"
    variable_cfg    = "legacyAnalysis/additionalVariables"
    plot_cfg        = "legacyAnalysis/withMEM_new/withMEM_final_config_crosscheck"
    # plot_cfg        = "legacyAnalysis/DNN_14-05-2020/combined161718_DNNs"
    syst_cfg        = "legacyAnalysis/systs_2016_old_model"
    # syst_cfg        = "legacyAnalysis/no_systs"
    replace_cfg     = "legacyAnalysis/pdf_relic_names"

    sfCorrection = {}
    sfCorrection["sfFile"] =  pyrootdir+"/data/btagSFCorrection/sf_2016_deepJet_combined.root"
    # variables for the correction
    sfCorrection["corrections"] = {}
    sfCorrection["corrections"]["HT_vs_NJet"] = ["Evt_HT_jets", "N_Jets"]
    # in root file sf histograms exist with some naming scheme
    sfCorrection["nameTemplate"] = "$BINNING__$PROCESS__$NAME"
    # SF_ is always preprended by default, that should not be changed
    # $BINNING = "_vs_".join(corrections[X])
    # DANGER: order of variables is important
    # name of corrections to be applied (should match whats defined in syst.csv or samples.py)
    sfCorrection["names"] = ["btag_NOMINAL"]

    # file for rate factors
    #rateFactorsFile = pyrootdir + "/data/rate_factors_onlyinternal_powhegpythia.csv"
    rateFactorsFile = pyrootdir + "/data/rateFactors/ratefactors_new_plotscript_2016.csv"

    # script options
    analysisOptions = {
        # general options
        "usePseudoData":        False,
        "testrun":              False,  # test run with less samples
        "stopAfterCompile":     False,   # stop script after compiling
        # options to activate parts of the script
        "haddFromWildcard":     True,
        "makeDataCards":        False,
        "makeInputDatacards":   False, # create datacards also for all defined plots
        "addData":              True,  # adding real data 
        "makePlots":            False,
        # options for makePlots
        "signalScaling":        -1,
        "lumiLabel":            True,
        "cmslabel":             "private Work",
        "ratio":                "#frac{S+B}{B}",
        "shape":                False,
        "logarithmic":          False,
        "splitLegend":          True,
        "normalize":            False,
        # the skipX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "skipPlotParallel":     opts.skipPlotParallel,
        "skipHaddParallel":     opts.skipHaddParallel,
        "skipHaddFromWildcard": opts.skipHaddFromWildcard,
        "skipHistoCheck":       opts.skipHistoCheck,
        "skipMergeSysts":       opts.skipMergeSysts,
        "skipDatacards":        opts.skipDatacards}

    plotJson = ""#pyrootdir+"/configs/legacyAnalysis/treeJson_2016.json"
    # plotDataBases = [["memDB","/nfs/dust/cms/user/vdlinden/legacyTTH/memes/memTrees/2016/",True]] 
    # memDataBase = "/nfs/dust/cms/user/swieland/ttH_legacy/MEMdatabase/CodeforScriptGenerator/MEMDataBase/MEMDataBase"
    dnnInterface = {"interfacePath":    pyrootdir+"/util/dNNInterfaces/MLfoyInterface.py",
                  "checkpointFiles":  pyrootdir+"/configs/legacyAnalysis/withMEM_new/DNNInputData/"}
    # dnnInterface = None

    # path to datacardMaker directory
    datacardmaker = "/nfs/dust/cms/user/lreuter/forPhilip/datacardMaker"

    print('''
    # ========================================================
    # initializing analysisClass 
    # ========================================================
    ''')

    # save a lot of useful information concerning the analysis
    analysis = analysisClass.analysisConfig(
        workdir         = workdir, 
        pyrootdir       = pyrootdir, 
        signalProcess   = signalProcess, 
        pltcfgName      = config,
        discrName       = discrName,
        dataera         = dataera)

    
    analysis.initAnalysisOptions( analysisOptions )

    pltcfg = analysis.initPlotConfig()
    print ("We will import the following plotconfig: {}".format(analysis.getPlotConfig()))

    # loading monitorTools module locally
    monitor = monitorTools.init(analysis.workdir)
    monitor.printClass(analysis, "init")

    print ('''
    # ========================================================
    # prepare configdata
    # ========================================================
    ''')

    configData = configClass.configData(
        analysisClass   = analysis,
        variable_config = variable_cfg,
        plot_config     = plot_cfg,
        execute_file    = os.path.realpath(inspect.getsourcefile(lambda:0)),
        replace_config  = replace_cfg
        )

    configData.initSystematics(systconfig = syst_cfg)

    configData.initData()

    # get the discriminator plots
    configData.genDiscriminatorPlots(memexp, dnnInterface)
    configData.writeConfigDataToWorkdir()
    monitor.printClass(configData, "init")
    print( '''    
    # ========================================================
    # define additional variables necessary for selection in plotparallel
    # ========================================================
    ''')
    configData.getAddVariables() # also adds DNN variables

    print( '''    
    # ========================================================
    # loading samples and samples data
    # ========================================================
    ''')
    configData.initSamples()

    print( '''
    # ========================================================
    # done with preprocessing
    # ========================================================
    ''')

    # plot everything, except during drawParallel step
    # Create file for data cards
    print( '''
    # ========================================================
    # starting with plotParallel step
    # ========================================================
    ''')
    
    with monitor.Timer("plotParallel"):
        # initialize plotParallel class 
        pP = plotParallel.plotParallel(
            analysis = analysis,
            configData = configData,
            nominalHistKey = nom_histname_template,
            systHistKey = syst_histname_template,
            separator = histname_separator)

        monitor.printClass(pP, "init")
        # set some changed values
        pP.setJson(plotJson)
        # pP.setDataBases(plotDataBases)
        # pP.setMEMDataBase(memDataBase)
        pP.setDNNInterface(dnnInterface)
        pP.setMaxEvts_nom(50000)
        # pP.setMaxEvts_nom(200000)
        pP.setMaxEvts_systs(200000)
        # pP.request_runtime = 60*60*5
        pP.setRateFactorsFile(rateFactorsFile)
        pP.setSampleForVariableSetup(configData.samples[nSigSamples])
        pP.setSFCorrection(sfCorrection)
        pP.setUseFriendTrees(True)

        # run plotParallel
        pP.run()

    pP.checkTermination()
    monitor.printClass(pP, "after plotParallel")

    # hadd histo files before renaming. The histograms are actually already renamed. 
    # But the checkbins thingy will not have been done yet.
    print( '''
    # ========================================================
    # hadding from wildcard
    # ========================================================
    ''')
    with monitor.Timer("haddFilesFromWildCard"):
        haddParallel.haddSplitter( 
            input               = pP.getHaddOutPath(),
            outName             = analysis.ppRootPath,
            subName             = "haddParts",
            nHistosRemainSame   = True,
            skipHadd            = analysis.skipHaddFromWildcard)
     

    pP.setRenameInput()
    if pP.configData.replace_config and not analysis.skipMergeSysts:
        with monitor.Timer("mergeSystematics"):
            print("merging systematics")
            pP.mergeSystematics()

    # Deactivate check bins functionality in renameHistos 
    #   if additional plot variables are added via analysis class
    if os.path.exists( analysis.setRenamedPath(name = "limitInput") ):
        print( "renamed file already exists - skipping renaming histos" )
    else:
        print( '''
        # ========================================================
        # renaming Histograms
        # ========================================================
        ''')

        # in this function the variable self.renameInput is set
        # if hadd files were created during plotParallel
        #       the renameInput is set to pP.getHaddFiles 
        #       (a.k.a. the list of hadd files)
        # if no hadd files were created during plotparallel
        #       the renameInput is set to pp.getOutPath 
        #       (a.ka. the path to output.root)

        with monitor.Timer("checkHistos"):
            checkHistos.checkHistsManager(
                inFiles         = pP.getRenameInput(),
                outFile         = analysis.renamedPath,
                checkBins       = True,
                eps             = 0.0,
                skipHistoCheck  = analysis.skipHistoCheck)


    if analysis.addData:
        print( '''
        # ========================================================
        # adding data with plotParallel
        # ========================================================
        ''')
        with monitor.Timer("addRealData"):
            if analysis.usePseudoData:
                print("adding data_obs histograms as pseudo data")
                # pseudo data without ttbb 5FS
                # pP.addData( samples = configData.samples[:-1], 
                #             discrName = discrName)
                pP.addData( samples = configData.pseudo_data_samples, 
                            discrName = discrName)
                #pP.addData(samples = configData.samples)
            else:
                print("adding data_obs histograms as real data")
                # real data with ttH
                pP.addData( samples = configData.controlSamples, 
                            discrName = discrName)

    

    pP.checkTermination()       
    monitor.printClass(pP, "after plotParallel completely done")

    print("########## DONE WITH PLOTPARALLEL STEP ##########")
    print("at the moment the outputpath is "+str(analysis.renamedPath))
    print("#################################################")

    if analysis.makeDataCards or analysis.makeInputDatacards and not opts.skipDatacards:
        print( '''
        # ========================================================
        # Making Datacards.
        # ========================================================
        ''')
        with monitor.Timer("makeDatacardsParallel"):
            makeDatacards.makeDatacardsParallel(
                filePath            = analysis.renamedPath,
                workdir             = analysis.workdir,
                categories          = configData.getDatacardLabels(analysis.makeInputDatacards),
                doHdecay            = True,
                discrname           = analysis.discrName,
                datacardmaker       = datacardmaker,
                signalTag           = analysis.signalProcess,
                skipDatacards       = analysis.skipDatacards,
                # nominal_key         = nom_histname_template.replace("__$CHANNEL","__finaldiscr_$CHANNEL"),
                # syst_key            = syst_histname_template.replace("__$CHANNEL","__finaldiscr_$CHANNEL")
                nominal_key         = nom_histname_template,
                syst_key            = syst_histname_template
                )
    
    if analysis.makePlots:
        print( '''
        # ========================================================
        # Making Plots
        # ========================================================
        ''')
        with monitor.Timer("makePlots"):
            makePlots.makePlots(configData  = configData,
                                nominal_key = nom_histname_template,
                                syst_key    = syst_histname_template)


    print( '''
    # ========================================================
    # this is the end of the script 
    # ========================================================
    ''')

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("--skipPlotParallel",     dest = "skipPlotParallel",      action = "store_true", default = False)
    parser.add_option("--skipHaddParallel",     dest = "skipHaddParallel",      action = "store_true", default = False)
    parser.add_option("--skipHaddFromWildcard", dest = "skipHaddFromWildcard",  action = "store_true", default = False)
    parser.add_option("--skipHistoCheck",       dest = "skipHistoCheck",        action = "store_true", default = False)
    parser.add_option("--skipMergeSysts",       dest = "skipMergeSysts",        action = "store_true", default = False)
    parser.add_option("--skipDatacards",        dest = "skipDatacards",         action = "store_true", default = False)
    parser.add_option("--skip",                 dest = "skip",                  default = 0,            type = "int",
        help = "skip first INT parallel stages. plotParallel (1), haddParallel (2), haddFromWildcard (3), histoCheck (4), mergeSysts (5), Datacards (6)")

    (opts, args) = parser.parse_args()

    if opts.skip >= 1: opts.skipPlotParallel        = True
    if opts.skip >= 2: opts.skipHaddParallel        = True
    if opts.skip >= 3: opts.skipHaddFromWildcard    = True
    if opts.skip >= 4: opts.skipHistoCheck          = True
    if opts.skip >= 5: opts.skipMergeSysts          = True
    if opts.skip >= 6: opts.skipDatacards           = True


    main(pyrootdir, opts)
