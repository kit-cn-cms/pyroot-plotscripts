import os
import sys
import importlib 
import getopt

# local imports       
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import plotClasses

class analysisConfig:
    def __init__(self, workdir, pyrootdir, rootPath, signalProcess = "ttbb", pltcfgName = "pltcfg_ttH18", discrName = "finaldiscr", dataera = "2017"):
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
        self.renamedPath = self.rootPath
    
        self.dataera = dataera
        if not self.dataera in ["2017", "2018", "2017_deepCSV"]:
            sys.exit("invalid dataera")

        self.setDefaults()
        self.setSignalProcess(signalProcess, pltcfgName)

    def setDefaults(self):
        if os.path.exists(self.rootPath):
            self.plotParallel = False
        else:
            self.plotParallel = True

        self.singleExecute = False

        self.drawParallel = True
        self.plotNumber = None
        self.usePseudoData = True
        self.makeDataCards = True
        self.haddFromWildcard = True        
        self.addData = False

        self.makeEventYields = True
        self.makeSimplePlots = True
        self.makeMCControlPlots = True

        self.additionalPlotVariables = []
        self.checkBins = True
        self.optimizedRebinning = ""

        self.opts = None

        self.testrun = False
        self.stopAfterCompile = False
        self.haddParallel = True
        self.skipPlotParallel = False
        self.skipHaddParallel = False
        self.skipHaddFromWildcard = False
        self.skipRenaming = False
        self.skipDatacards = False

        self.crossEvaluation = True

    def setSignalProcess(self, signalProcess, pltcfgName):
        if signalProcess == "ttbb":
            self.signalProcess = "ttbb"
            # lower and upper end of samples
            self.tt_samplesLower = 0
            self.tt_samplesUpper = 5
            print("ttbb was chosen as signal process")
        elif signalProcess == "ttH" or signalProcess == "tth":
            self.signalProcess = "ttH"
        elif signalProcess == "ttZ" or signalProcess == "ttbarZ":
            self.signalProcess = "ttbarZ"
        else:
            print("could not find signalProcess '"+str(signalProcess)+"'. Define it in analysisConfig")
            sys.exit("unknow signalProcess chosen")
        self.plotConfig = pltcfgName
        print("set plotConfig to "+str(self.plotConfig))
        
    def initArguments(self, argv = list()):
        """Evaluate any commandline arguments"""
        try:
            opts, args = getopt.getopt(argv,"hp:",
                ["plot=", "doPlotParallel=", "doDrawParallel=", 
                    "usePseudoData=", "makeEventYields=", "makeDataCards=", 
                    "makeSimplePlots=", "makeMCControlPlots="])
        except getopt.GetoptError:
            print '[scriptname].py -p  <plotnumber> --doPlotParallel= --doDrawParallel= --usePseudoData= --makeEventYields= --makeDataCards= --makeSimplePlots= --makeMCControlPlots='
            sys.exit(2)
        for opt, arg in opts:
            print 'opt: ', opt, ' arg: ', arg, ' found.'
            if opt in ('-h', '--help'):
                print '[scriptname].py -p <plotnumber> --doPlotParallel= --doDrawParallel= --usePseudoData= --makeEventYields= --makeDataCards= --makeSimplePlots= --makeMCControlPlots= --additionalPlotVariables= --optimizedRebinning='
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
            elif opt in ("--usePseudoData"):
                self.setPlotBlinded(arg)
                print "Set usePseudoData option to: ", arg
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

    def initAnalysisOptions(self, analysisOptions = {}):
        for key in analysisOptions:
            if key in ("testrun"):
                self.testrun = bool(analysisOptions[key])
            elif key in ("stopAfterCompile"):
                self.stopAfterCompile = bool(analysisOptions[key])
            elif key in ("haddParallel"):
                self.haddParallel = bool(analysisOptions[key])
            elif key in ("skipPlotParallel"):
                self.skipPlotParallel = bool(analysisOptions[key])
            elif key in ("skipHaddParallel"):
                self.skipHaddParallel = bool(analysisOptions[key])
            elif key in ("skipHaddFromWildcard"):
                self.skipHaddFromWildcard = bool(analysisOptions[key])
            elif key in ("skipRenaming"):
                self.skipRenaming = bool(analysisOptions[key])
            elif key in ("skipDatacards"):
                self.skipDatacards = bool(analysisOptions[key])
            elif key in ("plotNumber"):
                self.setPlotNumber( analysisOptions[key] )
            elif key in ("singleExecute"):
                self.setSingleExecute( analysisOptions[key] )
            elif key in ("plotParallel"):
                self.setDoPlotParallel( analysisOptions[key] )
            elif key in ("drawParallel"):
                self.setDoDrawParallel( analysisOptions[key] )
            elif key in ("usePseudoData"):
                self.setPlotBlinded( analysisOptions[key] )
            elif key in ("makeEventYields"):
                self.setMakeEventYields( analysisOptions[key] )
            elif key in ("makeDataCards"):
                self.setMakeDataCards( analysisOptions[key] )
            elif key in ("makeSimplePlots"):
                self.setMakeSimplePlots( analysisOptions[key] )
            elif key in ("makeMCControlPlots"):
                self.setMakeMCControlPlots( analysisOptions[key] )
            elif key in ("additionalPlotVariables"):
                self.setAdditionalPlotVariables( analysisOptions[key] )
            elif key in ("optimizedRebinning"):
                self.setOptimizedRebinning( analysisOptions[key] )
            elif key in ("haddFromWildcard"):
                self.setHaddFromWildcard( analysisOptions[key] )
            elif key in ("addData"):
                self.setAddData( analysisOptions[key] )
            elif key in ("crossEvaluation"):
                self.setCrossEvaluation( analysisOptions[key] )

    def initPlotConfig(self):
        configdir = self.pyrootdir+"/configs/"
        sys.path.append(configdir)
        self.pltcfg = importlib.import_module( self.plotConfig )
        return self.pltcfg


    ## Setter functions
    def setRenamedPath(self, name = "limitInput"):
        self.renamedPath = self.ppRootPath.replace(".root", "_"+str(name)+".root")
        return self.renamedPath

    def setPlotNumber(self,arg):
        self.plotNumber = int(arg)
        self.workdir += "/drawParallelRuns/run"+str(self.plotNumber)
        if not os.path.exists(self.workdir):
            os.makedirs(self.workdir)

    def setSingleExecute(self, arg):
        self.singleExecute = bool(arg)
        
    def setDoPlotParallel(self,arg):
        self.plotParallel = arg

    def setHaddFromWildcard(self, arg):
        self.haddFromWildcard = arg

    def setDoDrawParallel(self,arg):
        self.drawParallel = arg

    def setPlotBlinded(self,arg):
        self.usePseudoData = arg

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
    
    def setAddData(self, arg):
        self.addData = arg

    def setCrossEvaluation(self, arg):
        print("setting crossEvaluation to {}".format(arg))
        self.crossEvaluation = arg

    def printChosenOptions(self):
        code = "Option, Value\n"
        code +="PlotNumber, " + str(self.plotNumber) + "\n"
        code +="plotParallel, " + str(self.plotParallel) + "\n"
        code +="drawParallel, " + str(self.drawParallel) + "\n"
        code +="usePseudoData, " + str(self.usePseudoData) + "\n"
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

