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

        self.signalScaling=      False
        self.lumiLabel=True
        self.privateWork= False
        self.ratio=True
        self.logarithmic=False

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
                self.haddFromWildcard= analysisOptions[key] 
            elif key in ("addData"):
                self.addData = analysisOptions[key]
            elif key in ("crossEvaluation"):
                self.crossEvaluation= analysisOptions[key]
            elif key in ("signalScaling"):
                self.signalScaling= analysisOptions[key]
            elif key in ("lumiLabel"):
                self.lumiLabel= bool(analysisOptions[key])
            elif key in ("privateWork"):
                self.privateWork= bool(analysisOptions[key])
            elif key in ("ratio"):
                self.ratio= analysisOptions[key]
            elif key in ("logarithmic"):
                self.logarithmic= analysisOptions[key]


    def initPlotConfig(self):
        configdir = self.pyrootdir+"/configs/"
        sys.path.append(configdir)
        self.pltcfg = importlib.import_module( self.plotConfig )
        return self.pltcfg


    ## Setter functions
    def setRenamedPath(self, name = "limitInput"):
        self.renamedPath = self.ppRootPath.replace(".root", "_"+str(name)+".root")
        return self.renamedPath

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

