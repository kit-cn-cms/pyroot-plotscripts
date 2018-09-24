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

sys.path.append(pyrootdir)

# local imports
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
    name = 'testLimitsAll'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # creating workdir subfolder
    if not os.path.exists(workdir):
        os.makedirs(workdir)
        print("created workdir at "+str(workdir))
    
    # path to root file
    # how is this name determined in different script types?
    rootPathForAnalysis = workdir+'/output_limitInput.root'

    # signal process
    signalProcess = "ttH"

    # Name of final discriminator, should not contain underscore
    discrName = 'finaldiscr'

    # define MEM discriminator variable
    memexp = '(memDBp>0.0)*(memDBp)+(memDBp<=0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # name of the csv files used in configdata folder
    configDataBaseName = "limitsAllv20"

    # options for plotParallel
    # TODO: this list contains both lists below
    #       but is not used yet - need to implement into analysisClass
    options = {
        # options for analysis in general
        "singleExecute":        False,
        "plotBlinded":          True,
        "cirun":                False,
        # options for steps in script
        "optimizedRebinning":   True,
        "haddParallel":         True,
        "addData":              True,
        "drawParallel":         True,
        "makeSimplePlots":      True,
        "makeDataCards":        True,
        "makeMCControlPlots":   True,
        "makeEventYields":      False,
        # options for trying to skip steps
        "useOldRoot":           False,
        "skipPlotParallel":     False,
        "skipHaddParallel":     False,  
        "skipHaddFromWildcard": False,
        "skipRenaming":         False,
        "skipDatacards":        False}
        
    plotOptions = {
        "cirun":                False,  
        "haddParallel":         True, 
        "useOldRoot":           False,
        # the skipXXX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "skipPlotParallel":     False,
        "skipHaddParallel":     False,
        "skipHaddFromWildcard": False,
        "skipRenaming":         False,
        "skipDatacards":        False}

    # general analysis Options
    analysisOptions = {
        "singleExecute":        False,
        "optimizedRebinning":   False,
        "plotBlinded":          True,
        "makeSimplePlots":      True,
        "makeMCControlPlots":   True,
        "makeDataCards":        True,
        "makeEventYields":      False,
        "drawParallel":         True,
        "addData":              False}

    #plotJson = "/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_latestAndGreatest.json"
    plotJson = "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/Summer18_2017data/treejson_v13.json"
    plotDataBases = [["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_Spring17_V1",False]] 
    plotInterfaces = ["../util/dNNInterfaces/dNNInterface_V6.py"]

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

    # TODO make the analysisClass more essential - atm it is not really needed
    analysis = configClass.analysisConfig(
        workdir = workdir, pyrootdir = pyrootdir, rootPath = rootPathForAnalysis, 
        signalProcess = signalProcess, discrName = discrName)

    analysis.initArguments( argv )
    analysis.initPlotOptions( plotOptions )
    analysis.initAnalysisOptions( analysisOptions )

    pltcfg = analysis.initPlotConfig()
    print "We will import the following plotconfig: ", analysis.getPlotConfig()

    analysis.printChosenOptions()

    # loading monitorTools module locally
    monitor = monitorTools.init(analysis.workdir)
    monitor.printClass(analysis, "init")

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

    configData = configClass.configData(
        analysisClass = analysis,
        configDataBaseName = configDataBaseName)

    configData.initData()
    monitor.printClass(configData, "init")

    # get the discriminator plots
    configData.genDiscriminatorPlots(memexp)
    configData.writeConfigDataToWorkdir()
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
    configData.printAddVariables()

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
            pP.setCatNames([''])
            pP.setCatSelections(['1.'])
            # pP.setMaxEvts(...)

            # run plotParallel
            pP.run()



        # if pP.haddFiles is a list we are probably in the first iteration
        # cross check if plotParallel has terminated successfully
        # program exits if not
        pP.checkHaddFiles()
        pP.checkTermination()

        monitor.printClass(pP, "after plotParallel")

        if analysis.optimizedRebinning:
        #if analysis.getActivatedOptimizedRebinning():
            print '''
            # ========================================================
            # Doing OptimizedRebinning
            # ========================================================
            '''
            #TODO rework
            if analysis.signalProcess == 'ttbb':
                # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                # TODO check the optimizedBinning function and adjust arguments to new structure
                # TODO rework samples splitting to be automated in samplesDataClass?
                # TODO call this only once and determine bkg/signal samples in the function itself
                with monitor.Timer("optimizeBinning"):
                    optBinning.optimizeBinning(
                        infname = analysis.ppRootPath,
                        signalsamples = [configData.samples[0:3]], 
                        backgroundsamples = configData.samples[3:],
                        additionalSamples = configData.controlSamples, 
                        plots = configData.getDiscriminatorPlots(), 
                        systnames = configData.allSystNames, 
                        minBkgPerBin = 2.0, 
                        optMode = analysis.optimzedRebinning,
                        considerStatUnc = False, 
                        maxBins = 20, 
                        minBins = 2,
                        verbosity = 2)

            elif analysis.signalProcess == 'ttH':
                # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. 
                # Rest: background samples
                with monitor.Timer("optimizeBinning"):
                    optBinning.optimizeBinning(
                        analysis.ppRootPath,
                        signalsamples = [configData.samples[0]], 
                        backgroundsamples = configData.samples[9:],
                        additionalSamples= configData.samples[1:9] + configData.controlSamples, 
                        plots = configData.getDiscriminatorPlots(), 
                        systnames = configData.allSystNames, 
                        minBkgPerBin = 2.0, 
                        optMode = analysis.optimizedRebinning,
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
            haddParallel.haddSplitter( input = pP.getHaddOutPath(),
                outName = analysis.ppRootPath,
                subName = "haddParts",
                nHistosRemainSame = True,
                skipHadd = analysis.skipHaddFromWildcard)
         


        # Deactivate check bins functionality in renameHistos 
        #   if additional plot variables are added via analysis class
        if os.path.exists( analysis.setLimitPath(name = "limitInput") ):
        #if os.path.exists( pP.setLimitPath() ) and (plotOptions["skipRenaming"] or analysis.plotNumber != None):
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
                    inFiles = pP.getRenameInput(),
                    outFile = analysis.limitPath,
                    systNames = configData.allSystNames,
                    checkBins = True,
                    prune = False,
                    Epsilon = 0.0,
                    skipRenaming = analysis.skipRenaming)

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
        monitor.printClass(pP, "after plotParallel completely done")

        print("########## DONE WITH PLOTPARALLEL STEP ##########")
        print("at the moment the outputpath is "+str(analysis.limitPath))
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
                    filePath = analysis.limitPath,
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
            gP = genPlots.genPlots( outPath = analysis.limitPath,
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
                    "factor": -1,
                    "logscale": False,
                    "canvasOptions": "histo",
                    "normalize": False,
                    "stack": True, # not default
                    "ratio": False,
                    "sepaTest": False}
                gP.makeSimpleControlPlots( listName = histoList, listIndex = 9, options = controlPlotsOptions)

                # creating shape plots
                shapePlotsOptions = {
                    "logscale": False,
                    "canvasOptions": "histo",
                    "normalize": True, # not default
                    "stack": False,
                    "ratio": False,
                    "statTest": False,
                    "sepaTest": False}
                gP.makeSimpleShapePlots( listName = dataList, listIndex = 9, options = shapePlotsOptions)

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
                gP.genNestedHistList(listName = histoList, listIndex = 9, 
                    systNames = pltcfg.errorSystNamesNoQCD, 
                    outName = "histoList")

                monitor.printClass(gP, "after generating nested hist list")
                # set config of llloflist
                nestedHistsConfig = {}
                nestedHistsConfig["histoList"] = {
                    "style": 3354, 
                    "color": ROOT.kBlack, 
                    "doRateSysts": False}


                #set general plotoption
                controlPlotsOptions = {
                    "factor": -2, #not default
                    "logscale": False,
                    "canvasOptions": "histo",
                    "ratio": True, # not default
                    "blinded": analysis.plotBlinded} #not default
                # makint the control plots
                gP.makeControlPlots(
                    dataConfig = genPlots.Config(name = dataList, index = 0),
                    controlConfig = genPlots.Config(name = histoList, index = 9),
                    sampleConfig = genPlots.Config(name = histoList, index = 9),
                    headHist = histoList,
                    headSample = histoList,
                    nestedHistsConfig = nestedHistsConfig,
                    options = controlPlotsOptions)

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
                    nameRequirement = "JT"
                    )


if __name__ == "__main__":

    main(pyrootdir, sys.argv[1:])


