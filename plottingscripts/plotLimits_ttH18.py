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
import util.configClass as configClass
import util.monitorTools as monitorTools
import util.plotParallel as plotParallel
import util.makePlots as makePlots
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
    name = 'ttHplottingv3'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # creating workdir subfolder
    if not os.path.exists(workdir):
        os.makedirs(workdir)
        print("created workdir at "+str(workdir))
    
    # path to root file
    rootPathForAnalysis = workdir+'/output_limitInput.root'

    # signal process
    signalProcess = "ttH"

    # dataera
    dataera = "2018"

    # Name of final discriminator, should not contain underscore
    discrName = 'finaldiscr'

    # define MEM discriminator variable
    memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # configs
    config          = "pltcfg_ttH18"
    variable_cfg    = "ttH18_addVariables"
    plot_cfg        = "ttH18_discrPlots"
    syst_cfg        = "ttH18_systematics"

    # file for rate factors
    #rateFactorsFile = pyrootdir + "/data/rate_factors_onlyinternal_powhegpythia.csv"
    rateFactorsFile = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/rate_factors_V2.csv"

    # script options
    analysisOptions = {
        # general options
        "usePseudoData":        False,
        "testrun":              False,  # test run with less samples
        "stopAfterCompile":     False,   # stop script after compiling
        # options to activate parts of the script
        "haddFromWildcard":     True,
        "makeDataCards":        False,
        "addData":              True,  # adding real data 
        "makePlots":            True,
        # options for makePlots
        "signalScaling":        -1,
        "lumiLabel":            True,
        "privateWork":          True,
        "ratio":                "#frac{data}{MC Background}",
        "logarithmic":          False,
        # the skipX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "skipPlotParallel":     True,
        "skipHaddParallel":     True,
        "skipHaddFromWildcard": True,
        "skipRenaming":         True,
        "skipDatacards":        True}

    plotJson = "/nfs/dust/cms/user/vdlinden/TreeJsonFiles/treeJson_ttZ_2018_v1.json"
    #plotDataBases = [["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_ttH_2018_newJEC",True]] 
    #memDataBase = "/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBase_ttH2018/MEMDataBase/MEMDataBase/"
    dnnInterface = {"interfacePath":    pyrootdir+"/util/dNNInterfaces/MLfoyInterface.py",
                    "checkpointFiles":  "/nfs/dust/cms/user/vdlinden/legacyTTH/DNNSets/ttH18"}

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

    if analysis.plotNumber == None:
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
            #pP.setDataBases(plotDataBases)
            #pP.setMEMDataBase(memDataBase)
            pP.setDNNInterface(dnnInterface)
            pP.setMaxEvts(500000)
            pP.setRateFactorsFile(rateFactorsFile)
            pP.setSampleForVariableSetup(configData.samples[8])

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
                    pP.addData(samples = configData.samples[8:])
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
        # Invoke makePlots step
        # =============================================================================================
        if analysis.makePlots:
            print '''
            # ========================================================
            # Making Plots
            # ========================================================
            '''
            # this step reexecutes this top level script once for each discriminator plot
            with monitor.Timer("makePlots"):
                makePlots.makePlots(
                    configData=configData
                    )
            print '''
            # ========================================================
            # this is the end of the script 
            # ========================================================
            '''

if __name__ == "__main__":

    main(pyrootdir, sys.argv[1:])


