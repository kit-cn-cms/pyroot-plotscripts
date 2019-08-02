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
    print '''
    # ========================================================
    # welcome to main function - defining some variables
    # ========================================================
    '''
    # name of the analysis (i.e. workdir name)
    name = 'ttZ18_5NodeDNN_hf_binning3_v2'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # signal process
    signalProcess = "ttZ"
    nSigSamples   = 3

    # dataera
    dataera = "2018"
    
    # Name of final discriminator, should not contain underscore
    discrName = 'finaldiscr'

    # define MEM discriminator variable
    memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # configs
    config          = "ttZ18/pltcfg_discrPlots_internalCSV_hf"
    variable_cfg    = "ttZ18/additionalVariables"
    plot_cfg        = "ttZ18/discrPlots_5Node_binning3"
    syst_cfg        = "ttZ18/systematics_internalCSV_hf"

    # file for rate factors1
    #rateFactorsFile = pyrootdir + "/data/rate_factors_onlyinternal_powhegpythia.csv"
    #rateFactorsFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/rate_factors_V2.csv"
    rateFactorsFile = "/nfs/dust/cms/user/vdlinden/legacyTTH/ratefactors/ratefactors_2018.csv"


    # script options
    analysisOptions = {
        # general options
        "usePseudoData":        True,
        "testrun":              False,  # test run with less samples
        "stopAfterCompile":     False,  # stop script after compiling
        # options to activate parts of the script
        "haddFromWildcard":     True,
        "makeDataCards":        True,
        "makeInputDatacards":   False, # create datacards also for all defined plots
        "addData":              True,  # adding real data
        "makePlots":            True,
        # options for makePlots
        "signalScaling":        -1,
        "lumiLabel":            True,
        "privateWork":          True,
        "ratio":                "#frac{data}{MC Background}",
        "logarithmic":          False,
        "splitLegend":          True,
        # the skipX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "skipPlotParallel":     opts.skipPlotParallel,
        "skipHaddParallel":     opts.skipHaddParallel,
        "skipHaddFromWildcard": opts.skipHaddFromWildcard,
        "skipHistoCheck":       opts.skipHistoCheck,
        "skipDatacards":        opts.skipDatacards}

    plotJson = "/nfs/dust/cms/user/vdlinden/TreeJsonFiles/treeJson_ttZ_2018_v4.json"
    #plotDataBases = [["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_ttH_2018_newJEC",True]] 
    #memDataBase = "/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBase_ttH2018/MEMDataBase/MEMDataBase/"
    dnnInterface = {"interfacePath":    pyrootdir+"/util/dNNInterfaces/MLfoyInterface.py",
                    "checkpointFiles":  "/nfs/dust/cms/user/vdlinden/legacyTTH/DNNSets/ttZ_5Node_top30_v1"}

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
        signalProcess   = signalProcess, 
        pltcfgName      = config,
        discrName       = discrName,
        dataera         = dataera)

    
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
    configData.getAddVariables() # also adds DNN variables

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
            analysis    = analysis,
            configData  = configData)

        monitor.printClass(pP, "init")
        # set some changed values
        pP.setJson(plotJson)
        #pP.setDataBases(plotDataBases)
        #pP.setMEMDataBase(memDataBase)
        pP.setDNNInterface(dnnInterface)
        pP.setMaxEvts(500000)
        pP.setRateFactorsFile(rateFactorsFile)
        pP.setSampleForVariableSetup(configData.samples[nSigSamples])

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
        haddParallel.haddSplitter( 
            input               = pP.getHaddOutPath(),
            outName             = analysis.ppRootPath,
            subName             = "haddParts",
            nHistosRemainSame   = True,
            skipHadd            = analysis.skipHaddFromWildcard)
     


    # Deactivate check bins functionality in renameHistos 
    #   if additional plot variables are added via analysis class
    if os.path.exists( analysis.setRenamedPath(name = "limitInput") ):
        print( "renamed file already exists - skipping renaming histos" )
    else:
        print '''
        # ========================================================
        # checking Histograms
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
        with monitor.Timer("checkHistos"):
            checkHistos.checkHistsManager(
                inFiles         = pP.getRenameInput(),
                outFile         = analysis.renamedPath,
                checkBins       = True,
                eps             = 0.0,
                skipHistoCheck  = analysis.skipHistoCheck)

    if analysis.addData:
        print '''
        # ========================================================
        # adding data with plotParallel
        # ========================================================
        '''
        with monitor.Timer("addRealData"):
            if analysis.usePseudoData:
                # pseudo data without ttH
                #pP.addData(samples = configData.samples[nSigSamples:])
                # pseudo data with signal
                pP.addData(samples = configData.samples)
            else:
                # real data with ttH
                pP.addData(samples = configData.controlSamples)

    

    pP.checkTermination()       
    monitor.printClass(pP, "after plotParallel completely done")

    print("########## DONE WITH PLOTPARALLEL STEP ##########")
    print("at the moment the outputpath is "+str(analysis.renamedPath))
    print("#################################################")

    if analysis.makeDataCards or analysis.makeInputDatacards:
        print '''
        # ========================================================
        # Making Datacards.
        # ========================================================
        '''
        with monitor.Timer("makeDatacardsParallel"):
            makeDatacards.makeDatacardsParallel(
                filePath            = analysis.renamedPath,
                workdir             = analysis.workdir,
                categories          = configData.getDatacardLabels(analysis.makeInputDatacards),
                doHdecay            = True,
                discrname           = analysis.discrName,
                datacardmaker       = datacardmaker,
                signalTag           = analysis.signalProcess,
                skipDatacards       = analysis.skipDatacards)

    if analysis.makePlots:
        print '''
        # ========================================================
        # Making Plots
        # ========================================================
        '''
        with monitor.Timer("makePlots"):
            makePlots.makePlots(configData = configData)


    print '''
    # ========================================================
    # this is the end of the script 
    # ========================================================
    '''

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("--skipPlotParallel",     dest = "skipPlotParallel",      action = "store_true", default = False)
    parser.add_option("--skipHaddParallel",     dest = "skipHaddParallel",      action = "store_true", default = False)
    parser.add_option("--skipHaddFromWildcard", dest = "skipHaddFromWildcard",  action = "store_true", default = False)
    parser.add_option("--skipHistoCheck",       dest = "skipHistoCheck",        action = "store_true", default = False)
    parser.add_option("--skipDatacards",        dest = "skipDatacards",         action = "store_true", default = False)
    parser.add_option("--skip",                 dest = "skip",                  default = 0,            type = "int",
        help = "skip first INT parallel stages. plotParallel (1), haddParallel (2), haddFromWildcard (3), histoCheck (4), Datacards (5)")

    (opts, args) = parser.parse_args()

    if opts.skip >= 1: opts.skipPlotParallel        = True
    if opts.skip >= 2: opts.skipHaddParallel        = True
    if opts.skip >= 3: opts.skipHaddFromWildcard    = True
    if opts.skip >= 4: opts.skipHistoCheck          = True
    if opts.skip >= 5: opts.skipDatacards           = True


    main(pyrootdir, opts)


