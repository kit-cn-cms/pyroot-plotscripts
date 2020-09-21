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
    print (
        """
    # ========================================================
    # welcome to main function - defining some variables
    # ========================================================
    """
    )
    # name of the analysis (i.e. workdir name)
    name = "Monotop_controlplots_had_2016"

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # signal process
    signalProcess = "VectorMonotop_Mphi_2000_Mchi_500"
    nSigSamples = 1

    # dataera
    dataera = "2016"

    # Name of final discriminator, should not contain underscore
    discrName = "finaldiscr"

    # configs
    config = "Monotop/pltcfg_controlPlots_had_2016_sync"
    variable_cfg = "Monotop/additionalVariables"
    plot_cfg = "Monotop/controlPlots_had_2016_sync"
    syst_cfg = "Monotop/systematics_2016"
    
    # file for rate factors
    # rateFactorsFile = pyrootdir + "/data/rate_factors_onlyinternal_powhegpythia.csv"
    # rateFactorsFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/rate_factors_V2.csv"

    # script options
    analysisOptions = {
        # general options
        "usePseudoData": False,
        "testrun": False,  # test run with less samples
        "stopAfterCompile": False,  # stop script after compiling
        # options to activate parts of the script
        "haddFromWildcard": True,
        "makeDataCards": False,
        "addData": True,  # adding data object
        "makePlots": True,
        # options for makePlots
        "signalScaling": -1,
        "lumiLabel": 35.9,
        "CMSlabel": "work in progress",
        "ratio": "#frac{data}{MC Background}",
        "shape": False, # for shape plots
        "normalize": False, # normalize yield to integral 1
        "logarithmic": False,
        "splitLegend": True,
        # the skipX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "skipPlotParallel": opts.skipPlotParallel,
        "skipHaddParallel": opts.skipHaddParallel,
        "skipHaddFromWildcard": opts.skipHaddFromWildcard,
        "skipHistoCheck": opts.skipHistoCheck,
        "skipDatacards": opts.skipDatacards,
    }

    plotJson = ""
    # plotDataBases = [["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_ttH_2018_newJEC",True]]
    # memDataBase = "/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBase_ttH2018/MEMDataBase/MEMDataBase/"
    # dnnInterface = {"interfacePath":    pyrootdir+"/util/dNNInterfaces/MLfoyInterface.py",
    #                "checkpointFiles":  "/nfs/dust/cms/user/vdlinden/legacyTTH/DNNSets/ttZ18_hf_recoVars"}
    dnnInterface = None

    # path to datacardMaker directory
    datacardmaker = "/nfs/dust/cms/user/lreuter/forPhilip/datacardMaker"

    print (
        """
    # ========================================================
    # initializing analysisClass 
    # ========================================================
    """
    )

    # save a lot of useful information concerning the analysis
    analysis = analysisClass.analysisConfig(
        workdir=workdir,
        pyrootdir=pyrootdir,
        signalProcess=signalProcess,
        pltcfgName=config,
        discrName=discrName,
        dataera=dataera,
    )

    analysis.initAnalysisOptions(analysisOptions)

    pltcfg = analysis.initPlotConfig()
    print ("We will import the following plotconfig: ", analysis.getPlotConfig())

    # loading monitorTools module locally
    monitor = monitorTools.init(analysis.workdir)
    monitor.printClass(analysis, "init")

    print (
        """
    # ========================================================
    # prepare configdata
    # ========================================================
    """
    )

    configData = configClass.configData(
        analysisClass=analysis,
        variable_config=variable_cfg,
        plot_config=plot_cfg,
        execute_file=os.path.realpath(inspect.getsourcefile(lambda: 0)),
    )

    configData.initSystematics(systconfig=syst_cfg)

    configData.initData()

    # get the discriminator plots
    memexp = ""
    configData.genDiscriminatorPlots(memexp, dnnInterface)
    configData.writeConfigDataToWorkdir()
    monitor.printClass(configData, "init")
    print (
        """    
    # ========================================================
    # define additional variables necessary for selection in plotparallel
    # ========================================================
    """
    )
    configData.getAddVariables()  # also adds DNN variables

    print (
        """    
    # ========================================================
    # loading samples and samples data
    # ========================================================
    """
    )
    configData.initSamples()
    print (
        """
    # ========================================================
    # done with preprocessing
    # ========================================================
    """
    )

    # plot everything, except during drawParallel step
    # Create file for data cards
    print (
        """
    # ========================================================
    # starting with plotParallel step
    # ========================================================
    """
    )

    with monitor.Timer("plotParallel"):
        # initialize plotParallel class
        pP = plotParallel.plotParallel(analysis=analysis, configData=configData)

        monitor.printClass(pP, "init")
        # set some changed values
        pP.setJson(plotJson)
        # pP.setDataBases(plotDataBases)
        # pP.setMEMDataBase(memDataBase)
        # pP.setDNNInterface(dnnInterface)
        pP.setMaxEvts(100000)
        # pP.setRateFactorsFile(rateFactorsFile)
        pP.setSampleForVariableSetup(configData.samples[nSigSamples])
        
        pP.setCatNames([""])
        pP.setCatSelections(["(Hadr_Recoil_Pt>250.)*(N_AK15Jets>=1)*(N_Jets>=1)*(N_Taus==0)*(N_AK15Jets_SoftDrop==N_AK15Jets)*(DeltaPhi_AK4Jets_Recoil_Larger_0p5)*(CaloMET_PFMET_Recoil_ratio<0.5)*(AK15Jet_CHF[0]>0.1)*(AK15Jet_NHF[0]<0.8)"])

        # run plotParallel
        pP.run()

    pP.checkTermination()
    monitor.printClass(pP, "after plotParallel")

    # hadd histo files before renaming. The histograms are actually already renamed.
    # But the checkbins thingy will not have been done yet.
    print (
        """
    # ========================================================
    # hadding from wildcard
    # ========================================================
    """
    )
    with monitor.Timer("haddFilesFromWildCard"):
        haddParallel.haddSplitter(
            input=pP.getHaddOutPath(),
            outName=analysis.ppRootPath,
            subName="haddParts",
            nHistosRemainSame=True,
            skipHadd=analysis.skipHaddFromWildcard,
        )

    # Deactivate check bins functionality in renameHistos
    #   if additional plot variables are added via analysis class
    if os.path.exists(analysis.setRenamedPath(name="limitInput")):
        print ("renamed file already exists - skipping renaming histos")
    else:
        print (
            """
        # ========================================================
        # renaming Histograms
        # ========================================================
        """
        )

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
                inFiles=pP.getRenameInput(),
                outFile=analysis.renamedPath,
                checkBins=True,
                eps=0.0,
                skipHistoCheck=analysis.skipHistoCheck,
            )

    if analysis.addData:
        print (
            """
        # ========================================================
        # adding data with plotParallel
        # ========================================================
        """
        )
        with monitor.Timer("addRealData"):
            #if analysis.usePseudoData:
                # pseudo data without ttH
                #pP.addData(samples = [sample for sample in configData.samples if sample.typ=="bkg"])
                # pseudo data with signal
                #pP.addData(samples=configData.samples)
            #else:
                # real data
                #pP.addData(samples=configData.controlSamples)
            pP.addData(samples = [sample for sample in configData.samples if sample.typ=="bkg"], is_real_data = False)
            pP.addData(samples=configData.controlSamples, is_real_data = True)

    pP.checkTermination()
    monitor.printClass(pP, "after plotParallel completely done")

    print ("########## DONE WITH PLOTPARALLEL STEP ##########")
    print ("at the moment the outputpath is " + str(analysis.renamedPath))
    print ("#################################################")

    if analysis.makeDataCards:
        print (
            """
        # ========================================================
        # Making Datacards.
        # ========================================================
        """
        )
        with monitor.Timer("makeDatacardsParallel"):
            makeDatacards.makeDatacardsParallel(
                filePath=analysis.renamedPath,
                workdir=analysis.workdir,
                categories=configData.getBinlabels(),
                doHdecay=True,
                discrname=analysis.discrName,
                datacardmaker=datacardmaker,
                signalTag=analysis.signalProcess,
                skipDatacards=analysis.skipDatacards,
            )

    if analysis.makePlots:
        print (
            """
        # ========================================================
        # Making Plots
        # ========================================================
        """
        )
        with monitor.Timer("makePlots"):
            makePlots.makePlots(configData=configData)

    print (
        """
    # ========================================================
    # this is the end of the script 
    # ========================================================
    """
    )


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option(
        "--skipPlotParallel",
        dest="skipPlotParallel",
        action="store_true",
        default=False,
    )
    parser.add_option(
        "--skipHaddParallel",
        dest="skipHaddParallel",
        action="store_true",
        default=False,
    )
    parser.add_option(
        "--skipHaddFromWildcard",
        dest="skipHaddFromWildcard",
        action="store_true",
        default=False,
    )
    parser.add_option(
        "--skipHistoCheck", dest="skipHistoCheck", action="store_true", default=False
    )
    parser.add_option(
        "--skipDatacards", dest="skipDatacards", action="store_true", default=False
    )

    (opts, args) = parser.parse_args()
    main(pyrootdir, opts)
