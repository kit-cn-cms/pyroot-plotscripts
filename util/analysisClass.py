import os
import sys
import importlib 
import getopt

# local imports       
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import plotClasses

class analysisConfig:
    def __init__(self, workdir, pyrootdir, signalProcess = "ttH", pltcfgName = "pltcfg_ttH18", discrName = "finaldiscr", dataera = "2018"):
        self.workdir    = str(workdir)
        self.pyrootdir  = str(pyrootdir)
        self.name       = self.workdir.split("/")[-1]
        self.discrName  = discrName

        if not os.path.exists(self.workdir):
            print("making workdir at "+str(self.workdir))
            os.makedirs(self.workdir)

        self.rootPath   = self.workdir+"/output_limitInput.root"

        self.ppRootPath = self.rootPath
        self.renamedPath = self.rootPath
    
        self.dataera = dataera
        if not self.dataera in ["2017", "2018", "2017_deepCSV","2016"]:
            sys.exit("invalid dataera")

        self.setDefaults()
        self.setSignalProcess(signalProcess, pltcfgName)

    def setDefaults(self):
        self.usePseudoData      = True
        self.makeDataCards      = True
        self.makeInputDatacards = False
        self.haddFromWildcard   = True        
        self.addData            = False

        self.makePlots          = False
        self.signalScaling      = False
        self.lumiLabel          = True
        self.privateWork        = False
        self.ratio              = True
        self.logarithmic        = False

        self.testrun            = False
        self.stopAfterCompile   = False
        self.haddParallel       = True

        self.skipPlotParallel       = False
        self.skipHaddParallel       = False
        self.skipHaddFromWildcard   = False
        self.skipHistoCheck         = False
        self.skipMergeSysts         = False
        self.skipDatacards          = False

        self.crossEvaluation    = False

    def setSignalProcess(self, signalProcess, pltcfgName):
        if signalProcess == "ttbb":
            self.signalProcess = "ttbb"
        elif signalProcess == "tthf":
            self.signalProcess = "tthf"
        elif signalProcess == "ttH" or signalProcess == "tth":
            self.signalProcess = "ttH"
        elif signalProcess == "ttZ" or signalProcess == "ttbarZ":
            self.signalProcess = "ttZ"
        else:
            print("non default signal Process chosen, this could lead to errors later in the script (e.g. datacard creation). Setting it anyways.")
            print("signalProcess: {}".format(signalProcess))
            self.signalProcess = signalProcess


        self.plotConfig = pltcfgName
        print("set plotConfig to "+str(self.plotConfig))
        

    # def initAnalysisOptions(self, analysisOptions = {}):
    #     self.testrun = bool(analysisOptions.get("testrun", self.testrun))
    #     self.stopAfterCompile = bool(analysisOptions.get("stopAfterCompile", self.stopAfterCompile))
    #         elif key in ("haddParallel"):
    #             self.haddParallel = bool(analysisOptions[key])
    #         elif key in ("skipPlotParallel"):
    #             self.skipPlotParallel = bool(analysisOptions[key])
    #         elif key in ("skipHaddParallel"):
    #             self.skipHaddParallel = bool(analysisOptions[key])
    #         elif key in ("skipHaddFromWildcard"):
    #             self.skipHaddFromWildcard = bool(analysisOptions[key])
    #         elif key in ("skipHistoCheck"):
    #             self.skipHistoCheck = bool(analysisOptions[key])
    #         elif key in ("skipDatacards"):
    #             self.skipDatacards = bool(analysisOptions[key])
    #         elif key in ("addData"):
    #             self.addData = analysisOptions[key]
    #         elif key in ("crossEvaluation"):
    #             self.crossEvaluation = analysisOptions[key]
    #         elif key in ("signalScaling"):
    #             self.signalScaling = analysisOptions[key]
    #         elif key in ("lumiLabel"):

    #             self.lumiLabel= analysisOptions[key]
    #         elif key in ("CMSlabel"):
    #             self.cmslabel=analysisOptions[key]
    #         elif key in ("ratio"):
    #             self.ratio= analysisOptions[key]
    #         elif key in ("normalize"):
    #             self.normalize= analysisOptions[key]
    #         elif key in ("logarithmic"):
    #             self.logarithmic = analysisOptions[key]
    #         elif key in ("splitLegend"):

    #             self.splitLegend= analysisOptions[key] 
    #         elif key in ("shape"):
    #             self.shape= analysisOptions[key]
    #         elif key in ("makeDataCards"):
    #             self.makeDataCards = analysisOptions[key] 
    #         elif key in ("makePlots"):
    #             self.makePlots = analysisOptions[key] 
    #         elif key in ("usePseudoData"):
    #             self.usePseudoData = analysisOptions[key]
    #         elif key in ("makeInputDatacards"):
    #             self.makeInputDatacards = analysisOptions[key]
    def initAnalysisOptions(self, analysisOptions = {}):
        """
        Overwrite defaults specified in '__init__' and 'SetDefaults'.
        Object '__dict__' contains all variables of instance self
        """
        for key in self.__dict__:
            self.__dict__[key] = analysisOptions.get(key, self.__dict__[key])

    def initPlotConfig(self):
        configdir = self.pyrootdir+"/configs/"+self.plotConfig
        sys.path.append(os.path.dirname(configdir))
        self.pltcfg = importlib.import_module( os.path.basename(configdir) )
        return self.pltcfg

    def getLumi(self):
        lumi = {
            "2016":         "35.9",
            "2017":         "41.5",  
            "2017_deepCSV": "41.5",
            "2018":         "59.7",
        }
        return lumi[self.dataera]


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


