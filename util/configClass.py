import pandas
import ast
import ROOT
import os
import sys
import importlib 
import getopt

# local imports       
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import plotClasses
import PDFutils

class analysisConfig:
    def __init__(self, workdir, pyrootdir, rootPath, signalProcess = "ttbb", discrName = "finaldiscr"):
        self.workdir = str(workdir)
        self.pyrootdir = str(pyrootdir)
        self.name = self.workdir.split("/")[-1]
        self.discrName = discrName
        if not os.path.exists(self.workdir):
            print("making workdir at "+str(self.workdir))
            os.makedirs(self.workdir)

        self.rootPath = str(rootPath)
        if self.rootPath == "":
            self.rootPath = self.name+"/limitInput.root"
        self.ppRootPath = self.rootPath
        self.limitPath = self.rootPath

        self.setDefaults()
        self.setSignalProcess(signalProcess)

    def setDefaults(self):
        if os.path.exists(self.rootPath):
            self.plotParallel = False
        else:
            self.plotParallel = True

        self.singleExecute = False

        self.drawParallel = True
        self.plotNumber = None
        self.plotBlinded = False
        self.makeDataCards = True
        
        self.makeEventYields = True
        self.makeSimplePlots = True
        self.makeMCControlPlots = True

        self.additionalPlotVariables = []
        self.checkBins = True
        self.optimizedRebinning = ""

        self.opts = None

        self.cirun = False
        self.stopAfterCompile = False
        self.haddParallel = False
        self.skipPlotParallel = False
        self.useOldRoot = False
        self.skipHaddParallel = False
        self.skipHaddFromWildcard = False
        self.skipRenaming = False
        self.skipDatacards = False

    def setSignalProcess(self, signalProcess):
        if signalProcess == "ttbb":
            self.signalProcess = "ttbb"
            self.plotConfig = "plotconfigttbbSpring17v14"
            # lower and upper end of samples
            self.tt_samplesLower = 0
            self.tt_samplesUpper = 5
            print("ttbb was chosen as signal process")
        elif signalProcess == "ttH" or signalProcess == "tth":
            self.signalProcess = "ttH"
            self.plotBlinded = True
            self.plotConfig = 'pltcfg_v13'
            self.tt_samplesLower = 9
            self.tt_samplesUpper = 14
            print("ttH was chosen as signal process. plotBlinded was set to True")
        elif signalProcess == "DM":
            self.signalProcess = "DM"
            self.plotBlinded = False
            self.plotConfig = "pltcfg_MonoJet"
            print("doing DM analysis")
        else:
            print("could not find signalProcess '"+str(signalProcess)+"'. Define it in analysisConfig")
            sys.exit("unknow signalProcess chosen")


    def initArguments(self, argv = list()):
        """Evaluate any commandline arguments"""
        try:
            opts, args = getopt.getopt(argv,"hp:",
                ["plot=", "doPlotParallel=", "doDrawParallel=", 
                    "plotBlinded=", "makeEventYields=", "makeDataCards=", 
                    "makeSimplePlots=", "makeMCControlPlots="])
        except getopt.GetoptError:
            print '[scriptname].py -p  <plotnumber> --doPlotParallel= --doDrawParallel= --plotBlinded= --makeEventYields= --makeDataCards= --makeSimplePlots= --makeMCControlPlots='
            sys.exit(2)
        for opt, arg in opts:
            print 'opt: ', opt, ' arg: ', arg, ' found.'
            if opt in ('-h', '--help'):
                print '[scriptname].py -p <plotnumber> --doPlotParallel= --doDrawParallel= --plotBlinded= --makeEventYields= --makeDataCards= --makeSimplePlots= --makeMCControlPlots= --additionalPlotVariables= --optimizedRebinning='
                sys.exit()
            elif opt in ("-p","--plotNumber"):
                self.setPlotNumber(arg)
                print "Set plotNumber option to: ", arg
            elif opt in ("--doPlotParallel"):
                self.setDoPlotParallel(arg)
                print "Set doPlotParallel option to: ", arg
            elif opt in ("--doDrawParallel"):
                self.setDoDrawParallel(arg)
                print "Set doDrawParallel option to: ", arg
            elif opt in ("--plotBlinded"):
                self.setPlotBlinded(arg)
                print "Set plotBlinded option to: ", arg
            elif opt in ("--makeEventYields"):
                self.setMakeEventYields(arg)
                print "Set makeEventYields option to: ", arg
            elif opt in ("--makeDataCards"):
                self.setMakeDataCards(arg)
                print "Set makeDataCards option to: ", arg
            elif opt in ("--makeSimplePlots"):
                self.setMakeSimplePlots(arg)
                print "Set makeSimplePlots option to: ", arg
            elif opt in ("--makeMCControlPlots"):
                self.setMakeMCControlPlots(arg)
                print "Set makeMCControlPlots option to: ", arg
            elif opt in ("--additionalPlotVariables"):
                self.setAdditionalPlotVariables(arg)
                print "Set additionalPlotVariables option to: ", arg
            elif opt in ("--optimizedRebinning"):
                self.setOptimizedRebinning(arg)
                print "Set optimizedRebinning option to: ", arg

        return opts

    def initPlotOptions(self, plotOptions = {}):
        for key in plotOptions:
            if key in ("cirun"):
                self.cirun = bool(plotOptions[key])
            elif key in ("stopAfterCompile"):
                self.stopAfterCompile = bool(plotOptions[key])
            elif key in ("haddParallel"):
                self.haddParallel = bool(plotOptions[key])
            elif key in ("skipPlotParallel"):
                self.skipPlotParallel = bool(plotOptions[key])
            elif key in ("skipHaddParallel"):
                self.skipHaddParallel = bool(plotOptions[key])
            elif key in ("skipHaddFromWildcard"):
                self.skipHaddFromWildcard = bool(plotOptions[key])
            elif key in ("skipRenaming"):
                self.skipRenaming = bool(plotOptions[key])
            elif key in ("skipDatacards"):
                self.skipDatacards = bool(plotOptions[key])
            elif key in ("useOldRoot"):
                self.useOldRoot = bool(plotOptions[key])

    def initAnalysisOptions(self, analysisOptions = {}):
        for opt in analysisOptions:
            if opt in ("plotNumber"):
                self.setPlotNumber( analysisOptions[opt] )
            elif opt in ("singleExecute"):
                self.setSingleExecute( analysisOptions[opt] )
            elif opt in ("plotParallel"):
                self.setDoPlotParallel( analysisOptions[opt] )
            elif opt in ("optimizedRebinning"):
                self.setOptimizedRebinning( analysisOptions[opt] )
            elif opt in ("drawParallel"):
                self.setDoDrawParallel( analysisOptions[opt] )
            elif opt in ("plotBlinded"):
                self.setPlotBlinded( analysisOptions[opt] )
            elif opt in ("makeEventYields"):
                self.setMakeEventYields( analysisOptions[opt] )
            elif opt in ("makeDataCards"):
                self.setMakeDataCards( analysisOptions[opt] )
            elif opt in ("makeSimplePlots"):
                self.setMakeSimplePlots( analysisOptions[opt] )
            elif opt in ("makeMCControlPlots"):
                self.setMakeMCControlPlots( analysisOptions[opt] )
            elif opt in ("additionalPlotVariables"):
                self.setAdditionalPlotVariables( analysisOptions[opt] )
            elif opt in ("optimizedRebinning"):
                self.setOptimizedRebinning( analysisOptions[opt] )

    def initPlotConfig(self):
        configdir = self.pyrootdir+"/configs/"
        sys.path.append(configdir)
        self.pltcfg = importlib.import_module( self.plotConfig )
        return self.pltcfg


    ## Setter functions
    def setLimitPath(self, name = "limitInput"):
        self.limitPath = self.ppRootPath.replace(".root", "_"+str(name)+".root")
        return self.limitPath

    def setPlotNumber(self,arg):
        self.plotNumber = int(arg)
        self.workdir += "/drawParallelRuns/run"+str(self.plotNumber)
        if not os.path.exists(self.workdir):
            os.makedirs(self.workdir)

    def setSingleExecute(self, arg):
        self.singleExecute = bool(arg)
        
    def setDoPlotParallel(self,arg):
        self.plotParallel = arg

    def setDoDrawParallel(self,arg):
        self.drawParallel = arg

    def setPlotBlinded(self,arg):
        self.plotBlinded = arg

    def setMakeEventYields(self,arg):
        self.makeEventYields = arg

    def setMakeDataCards(self,arg):
        self.makeDatacards = arg

    def setMakeSimplePlots(self,arg):
        self.makeSimplePlots = arg

    def setMakeMCControlPlots(self,arg):
        self.makeMCControlPlots = arg

    def setAdditionalPlotVariables(self,arg):
        if arg and type(arg) is list:
            print "Activated additional plot variables.\n"
            self.additionalPlotVariables = arg
            print self.additionalPlotVariables
        else:
            print "Could not activate additional plot variables since argument is not a list."

    def setOptimizedRebinning(self,arg):
        self.optimizedRebinning = arg


    def printChosenOptions(self):
        code = "Option, Value\n"
        code +="PlotNumber, " + str(self.plotNumber) + "\n"
        code +="plotParallel, " + str(self.plotParallel) + "\n"
        code +="drawParallel, " + str(self.drawParallel) + "\n"
        code +="plotBlinded, " + str(self.plotBlinded) + "\n"
        code +="makeEventYields, " + str(self.makeEventYields) + "\n"
        code +="makeDataCards, " + str(self.makeDataCards) + "\n"
        code +="makeSimplePlots, " + str(self.makeSimplePlots) + "\n"
        code +="makeMCControlPlots, " + str(self.makeMCControlPlots) + "\n"
        code +="additionalPlotVariables, " + str(self.additionalPlotVariables) + "\n"
        code +="optimizedRebinning, " + str(self.optimizedRebinning)
        print(code)
        with open(self.workdir+"/analysisOptions.csv","w") as f:
            f.write(code)
        print("Options saved to: "+self.workdir+"/analysisOptions.csv")

    def set_ppRootPath(self, name = "output.root"):
        self.ppRootPath = self.workdir+"/"+name
        print("set analysis.ppRootPath to "+str(self.ppRootPath))


    # getters
    def getPlotConfig(self):
        """Return plotconfig module"""
        return self.pltcfg

    def get_ttSamplesLower(self):
        """Return position of ttbar samples in samples list, lower bound"""
        return self.tt_samplesLower

    def get_ttSamplesUpper(self):
        """Return position of ttbar samples in samples list, upper bound"""
        return self.tt_samplesUpper

    def getPlotPath(self):
        if self.plotNumber == None:
            print("this is not the right time to use this")
            return
        splitPath = self.workdir.split("/")[:-2]
        self.plotPath = "/".join(splitPath) + "/outputPlots/"
        if not os.path.exists(self.plotPath):
            os.makedirs(self.plotPath)
        return self.plotPath

class catData:
    def __init__(self):
        self.discrs = []
        self.nhistobins = []
        self.minxvals = []
        self.maxxvals = []
        self.categories = []

        self.plotPreselections = []
        self.binlabels = []

class configData:
    def __init__(self, analysisClass, configDataBaseName = ""):

        print("loading configdata ...")
        # name of files in config
        self.basename = configDataBaseName
        self.analysis = analysisClass
        self.pltcfg = self.analysis.getPlotConfig()
        self.cfgdir = self.analysis.pyrootdir + "/configs/"
        self.plotNumber = analysisClass.plotNumber
        self.Data = None

    def initData(self):
        self.Data = catData()

    def getData():
        return self.Data

    def writeConfigDataToWorkdir(self):
        if self.Data == None:
            print("there is no config data")
            return

        with open(self.analysis.workdir+"/configData.csv", "w") as csvf:
            csvf.write("categories,nhistobins,minxvals,maxxvals,discrs")
            for i in range(len(self.Data.categories)):
                line = "\n"
                line+= str(self.Data.categories[i])+";"
                line+= str(self.Data.nhistobins[i])+";"
                line+= str(self.Data.minxvals[i])+";"
                line+= str(self.Data.maxxvals[i])+";"
                line+= str(self.Data.discrs[i])
                csvf.write(line)
        print("wrote config data to workdir")
        print("path: "+str(self.analysis.workdir+"/configData.csv"))
        return

    def genDiscriminatorPlots(self, memexp):
        sys.path.append(self.cfgdir)
        fileName = self.basename+"_plots"
        configdatafile = importlib.import_module( fileName )
        configdatafile.memexp = memexp

        self.discriminatorPlots = configdatafile.getDiscriminatorPlots(self.Data, self.analysis.discrName)
        self.evtYieldCategories = configdatafile.evtYieldCategories()


    def getDiscriminatorPlotByNumber(self):
        # select the discr plots for a certain plot number
        self.discriminatorPlotByNumber = [self.discriminatorPlots[int(self.analysis.plotNumber)]]
        print("this is the new discriminatorPlot:")
        print(self.discriminatorPlotByNumber)



    def getDiscriminatorPlots(self):
        # if discriminatorPlot
        if not self.analysis.plotNumber == None:
            return self.discriminatorPlotByNumber
        else:
            return self.discriminatorPlots

    def getBinlabels(self):
        return self.Data.binlabels

    def getAddVariables(self, BDTWeightPath, BDTSet):
        sys.path.append(self.cfgdir)
        fileName = self.basename+"_addVariables"
        print("getting additional variables from "+str(fileName))
        addVarModule = importlib.import_module( fileName )
        self.addVars = addVarModule.getAddVars( BDTWeightPath, BDTSet )

    def getMEPDFAddVariables(self, csvfile):
        self.addVars += PDFutils.GetMEPDFadditionalVariablesList(csvfile)

    def printAddVariables(self):
        with open(self.analysis.workdir+"/additionalVariables.csv", "w") as csvf:
            csvf.write("addVars")
            for var in self.addVars:
                csvf.write("\n"+var)
        print("-"*50)
        print("all additional variables:")
        for var in self.addVars:
            print(var)
        print("additional variables saved to "+self.analysis.workdir+"/additionalVariables.csv")
        print("-"*50)
        return

    def getAdditionalDiscriminatorPlots(self, alwaysExecute = False):
        """ Function creates plot list for additional (input) variables
        Function checks if additionalPlotVariablesMap.py file exists.
        If yes, then it will try to use it for determination of the 
            amount of bins and the bin range of the plots.
            In case some variable cannot be mapped, 
            the variable will be added to existing file and user will get warned.
        If no, then it will construct such a dict and stop the further execution.
        
        mapFile is a dict with additionalPlotVariable as key and numberOfBins, 
            binLowerEdge, binUpperEdge as values contained in list
        """

        # Create dictionary for discriminators and preselections using additionalPlotVariables
        # Dictionary contains    additionalPlotVariable, numberOfBins, binLowerEdge, 
        #                        binUpperEdge ,discr, preselection, binLabel,            

        additionalPlotVarsDict_fromArgs = {}
        for index, row in self.Data.iterrows():
            for additionalPlotVariable in self.additionalPlotVariables:
                # Use fullVarName as key in class dict while additionalPlotVariable is key in map file
                fullVarName = row["discrs"] + '_' + row["binlabels"] + '_' + additionalPlotVariable
                additionalPlotVarsDict_fromArgs[fullVarName] = [additionalPlotVariable, 10, 0, 150, 
                            row["discrs"], row["plotPreselections"], row["binlabels"]]
        print("number of additional plot variables gathered from argv: " + \
                str(len(additionalPlotVarsDict_fromArgs)))
        
        # Stop further execution if dict file did not exist, 
        # map could not be read or variable could not be mapped.
        stopFurtherExecution = False

        # Try to open map (dict) file and read dict
        additionalPlotVarsDict_fromFile = {}
        # TODO adjust path
        if os.path.isfile('additionalPlotVariablesMap.py'):
            print 'Found additionalPlotVariablesMap.py file. Will try to open it now.'
            with open('additionalPlotVariablesMap.py') as mapFile:
                additionalPlotVarsDict_fromFile = eval(mapFile.read())
            if not additionalPlotVarsDict_fromFile:
                print "Could not read map from additionalPlotVariablesMap.py file or file is empty."
                print "Will update existing one and stop further execution."
                stopFurtherExecution = True
        else:
            print 'Did not find additionalPlotVariablesMap.py file. Will create one and stop further execution.'
            stopFurtherExecution = True
        print("number of additional plot variables gathered from file: " + \
                str(len(additionalPlotVarsDict_fromFile)))
        

        # Compare internal map with map from file and add additional keys if necessary
        print "Comparing map from additionalPlotVariablesMap.py file (or empty dict) \
                with internal map of additional plot variables."
        print "If necessary, adding keys from internal map to map file."
        missingKeysInFile = set()
        for classKey in additionalPlotVarsDict_fromArgs.keys():
            # Check for missing additionalPlotVariable description in map file
            # In map file additionalPlotVariable is the key while in class fullVarName
            mapFileKey = additionalPlotVarsDict_fromArgs[classKey][0]
            if not mapFileKey in additionalPlotVarsDict_fromFile:
                missingKeysInFile.add(mapFileKey)
            # otherwise replace internal key/value pair with external one
            else:
                # retrieve full value list
                tmpList = additionalPlotVarsDict_fromArgs[classKey]
                # and replace content with stored content
                # numberOfBins replacement
                tmpList[1] = additionalPlotVarsDict_fromFile[mapFileKey][0]
                # binLowerEdge replacement
                tmpList[2] = additionalPlotVarsDict_fromFile[mapFileKey][1]
                # binUpperEdge replacement
                tmpList[3] = additionalPlotVarsDict_fromFile[mapFileKey][2]
                additionalPlotVarsDict_fromArgs[classKey] = tmpList
        if missingKeysInFile:
            print "Found keys missing in map from file and required for plotting additional variables:"
            print missingKeysInFile 
            print "Will add keys to map file using default values."
            print "Afterwards will stop further execution."
            # Add missing keys to mapFile dictionary
            for missingKey in missingKeysInFile:
                additionalPlotVarsDict_fromFile[missingKey] = [10,0,150]
            stopFurtherExecution = True


        # Dedicated sort function, so that writen out dict is sorted    
        def sortByUsingLastPart(elem):
            return elem.rsplit('_')[-1]

        # Write dictionary to file
        with open('additionalPlotVariablesMap.py', 'w') as mapFile:
            mapFile.write('{\n')
            # sort dict and write entry for each additionalPlotVariable in file
            for mapFileKey in sorted(additionalPlotVarsDict_fromFile.iterkeys(), key=sortByUsingLastPart):
                # list contains numberOfBins, binLowerEdge, binUpperEdge
                tmpList = additionalPlotVarsDict_fromFile[mapFileKey]
                mapFile.write("""'""" + mapFileKey + """': [ """ + str(tmpList[0]) + ', ' + \
                                str(tmpList[1]) + ', ' + str(tmpList[2])    + """ ],\n""")
            mapFile.write('}')

        if stopFurtherExecution and not alwaysExecute:
            sys.exit('Stopping execution since mapping for additional variable plotting was not successful. \
                        \n Check the file additionalPlotVariablesMap.py and adjust it accordingly.')

        # construct list containing all additionalPlotVariables
        plotList = []
        for classKey in additionalPlotVarsDict_fromArgs.keys():
            currList = additionalPlotVarsDict_fromArgs[classKey]
            # Construct full var name, currList: additionalPlotVariable, numberOfBins, binLowerEdge, binUpperEdge, discr, preselection, binLabel
            fullVarName = currList[4] + '_' + currList[6] + '_' + currList[0]
            plotString = '''Plot(ROOT.TH1F("''' + fullVarName + '''", "add. var. (''' + fullVarName +  \
                         ''')",''' + str(currList[1]) + ',' + str(currList[2]) + ',' + str(currList[3]) + \
                         '''),"''' + currList[0] + '''","''' + currList[5] + '''","''' + currList[6] + '''")'''
            plotList.append(plotString)

        # Set variable to deactivate checkBins functionality in renameHistos, because otherwise it will take a long time.
        self.analysis.checkBins = False
        print "Set checkBins variable to false. Make sure, this variable is used in renameHistos."

        print "before adding stuff", self.discriminatorPlots
        # adding plots to discriminator plots 
        evaluatedPlotList = [eval(plt) for plt in plotList]
        self.discriminatorPlots.extend(evaluatedPlotList)
    
        print "after adding stuff", self.discriminatorPlots
        print("additional plots added to discriminatorPlots:")
        for plt in plotList:
            print(plt)


    def initSamples(self):
        # TODO: find a better naming sceme for the lists of samples/names/weights
        # they are used at many different places and it is not at all obvious which are used where and what they really contain

        sys.path.append(self.cfgdir)
        fileName = self.basename+"_samples"

        # imports file in cfgdir with given name as samplesData file
        # this file should have a function
        #       getSamples, getControlSamples, getSystSamples
        # where the samples lists are created, and functions
        #       getAllSystNames, getWeightSystNames, getOtherSystNames
        # where lists of names are created, and functions
        #       getSystWeights
        # where lists of weights are created
        samplesData = importlib.import_module( fileName )
        
        # list of samples
        self.samples = samplesData.getSamples( self.pltcfg )
        
        # list of controlsamples used in 'allSamples' list
        self.controlSamples = samplesData.getControlSamples( self.pltcfg )
        # list of systematic samples used in 'allSamples' and 'allSystSamples' list
        self.systSamples = samplesData.getSystSamples( self.pltcfg, self.analysis, self.samples )
        

        # list of samples used to write C program       
        self.allSamples = samplesData.getAllSamples( self.pltcfg, self.analysis, self.samples )
        # TODO is this used anywhere?
        #self.allSystSamples = samples + systSamples


        # list of samples used e.g. in renameHistos       
        self.allSystNames = samplesData.getAllSystNames( self.pltcfg )
        # list of syst names used in plotParallel
        self.weightSystNames = samplesData.getWeightSystNames( self.pltcfg )
        # list of syst names used in plotParallel
        self.otherSystNames = samplesData.getOtherSystNames( self.pltcfg )

        # list of syst weights used in plotParallel
        self.systWeights = samplesData.getSystWeights( self.pltcfg )


    def getEventYieldCategories(self):
        return self.evtYieldCategories
