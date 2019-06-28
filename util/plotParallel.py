import sys
import os
import subprocess
import datetime
import stat
import ROOT
import glob
import imp 
import types

# local imports
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import nafInterface
import scriptWriter
import haddParallel

###########################
#                         #
# P L O T P A R A L L E L #
#        C L A S S        #
###########################
class plotParallel:
    def __init__(self, analysis, configData):
        ''' default init 

        takes analysisConfig class,
        configData class,
        as arguments '''
        self.analysis = analysis
        self.analysis.set_ppRootPath("output.root")

        self.configData = configData

        # status variables
        self.finished = False
        self.haddFiles = None

        # init defaults
        self.initDefaults()

    def initDefaults(self):
        self.maxevents = 5000000
        self.categoryNames = [""]
        self.categorySelections = ["1."]        
        
        self.systNames = self.configData.weightSystNames
        self.systWeights = self.configData.systWeights

        self.jsonFile = ""
        self.dataBases = []
        self.memDBpath = ""
        self.useDataBases = False
        self.addInterfaces = []
        self.rateFactorsFile = None
        self.useGenWeightNormMap = False
        self.sampleForVariableSetup = None

        # check cmssw
        self.cmsswpath = os.environ['CMSSW_BASE']
        if not "CMSSW" in self.cmsswpath:
            print "you need CMSSW for this to work. Exiting!"
            exit(0)
        self.cmsswversion = os.environ['CMSSW_VERSION']


    
    ## setters functions ##
    def setCatNames(self, categoryNames):
        self.categoryNames = categoryNames
        print("set categoryNames to "+str(categoryNames))

    def setCatSelections(self, categorySelections):
        self.categorySelections = categorySelections
        print("set categorySelections to "+str(categorySelections))

    def setJson(self, jsonFile):
        self.jsonFile = jsonFile
        print("set jsonFile to "+str(jsonFile))

    def setDataBases(self, dataBases):
        self.dataBases = dataBases
        print("set dataBases to "+str(dataBases))
        if self.dataBases != []:
            self.useDataBases = True
            print("set useDataBases to True")

    def setMEMDataBase(self, db_path):
        self.memDBpath = db_path
        print("set path for MEM DataBase to "+str(db_path))

    def setAddInterfaces(self, interfaces):
        interfaceCounter = len(self.addInterfaces)
        for interface in interfaces:
            interfaceCounter += 1
            if isinstance( interface, basestring ):
                addModule = "addModule" + str(interfaceCounter)
                print( "loading module: " + str(interface) + " as " + addModule + " module." )
                self.addInterfaces.append(imp.load_source(addModule, interface).theInterface(self.analysis.workdir))
            elif isinstance( interface, types.InstanceType ):
                print( "appending class object initiated by user: " + str(interface) )
                self.addInterfaces.append(interface)
            else:
                print( "unknown additional code interface type: " + str(interface) )
    
    def setDNNInterface(self, interfaceConfig):
        interfacePath = interfaceConfig["interfacePath"]
        checkpointFiles = interfaceConfig["checkpointFiles"]
        addModule = "addModule"+str(len(self.addInterfaces)+1)
        print("loading module "+str(interfacePath)+" as "+addModule+" module.")
        self.addInterfaces.append(
            imp.load_source(addModule, interfacePath).theInterface(
                self.analysis.workdir, checkpointFiles, 
                crossEvaluation = self.analysis.crossEvaluation))

    def setRateFactorsFile(self, csvfile):
        self.rateFactorsFile = csvfile
        self.setUseGenWeightNormMap(True)
        print("set rateFactorsFile to "+str(csvfile))
    
    def setUseGenWeightNormMap(self, use_genWeightNormMap):
        self.useGenWeightNormMap = use_genWeightNormMap
        print("set useGenWeightNormMap to "+str(use_genWeightNormMap))
       
    def setMaxEvts(self, maxevts):
        self.maxevents = maxevts
        print("set maxevents to "+str(maxevts))

    def setRenameInput(self):
        if self.checkHaddFiles():
            self.renameInput = self.haddFiles
        else:
            self.renameInput = self.analysis.renamedPath
        print("set renameInput to "+str(self.renameInput))
    
    def setSampleForVariableSetup(self, sample):
        self.sampleForVariableSetup = sample
        print("using "+str(sample)+" for variable setup in scriptWriter")
    
    ## getter functions ##
    def getHaddOutPath(self):
        return self.analysis.workdir+"/HaddOutputs/*.root"
    
    def getOutPath(self):
        return self.analysis.renamedPath
    
    ## other public functions ##
    def checkTermination(self):
        if self.finished:
            print("plotParallel was finished successfully")
            return True
        else:
            print("plotParallel was not finished successfully or has not been run at all - exiting")
            sys.exit(-1)

    def checkHaddFiles(self):
        if self.haddFiles:
            return True
        else:
            return False

    def getRenameInput(self):
        return self.renameInput

    def globHaddFiles(self):
        allFiles = glob.glob(self.getHaddOutPath())
        allFiles = [f for f in allFiles if not "_renamed_" in f]
        return allFiles





    ## main function ##
    def run(self):
        # creating paths and folders
        self.scriptsPath = self.analysis.workdir + "/plotParallelScripts/"
        self.plotPath = self.analysis.workdir + "/plotParallelOutputs/"

        # check output if skipping activated
        if self.analysis.skipPlotParallel:
            print("skip plotParallel has been activated")
            print("this only skips the naf submission for the output files that already exist")
         
        print("ppRootPath: "+str(self.analysis.ppRootPath))   
        # check what to do if rootFile already exists
        self.ccPath = self.analysis.workdir + "/" + self.analysis.name + ".cc"

        # creating c++ programm
        writer = scriptWriter.scriptWriter(self)
        writer.writeCC()

        # create rename script
        writer.writeRenameScript()

        # creating output folders
        print( "creating output folders" )
        if not os.path.exists(self.scriptsPath):
            os.makedirs(self.scriptsPath)
        if not os.path.exists(self.plotPath):
            os.makedirs(self.plotPath)

        # creating run script
        print( "creating run scripts" )
        # runscriptData consists of {"scripts", "outputs", "entries", "maps"}
        self.runscriptData = writer.writeRunScripts()
        
        # check if we should stop
        if self.analysis.stopAfterCompile:
            print( "compiling is done and stopAfterCompile option is activated - exiting" )
            self.finished = True
            sys.exit(0)

        # job submission
        nafInterface.plotInterface(self.runscriptData, skipPlotParallel = self.analysis.skipPlotParallel)
        print("all jobs have terminated successfully")
        print("="*40)

        # starting on hadd output
        # TODO maybe split this completely and add another instance into limitsall
        print("now we can start the hadd output\n")
        self.haddParallelInterface(writer)
        print("plotParallel.run is finished")
        return

    def haddParallelInterface(self, writer):
        # init haddParallel class
        hP = haddParallel.haddParallel(self)

        # run hadd parallel
        self.haddFiles = hP.run(writer)
        print("type of haddFiles: " + str(type(self.haddFiles)) )
        self.finished = True
        return 


    # -- adding pseudo and real data --------------------------------------------------------------
    def addData(self, samples):

        sampleNicks = [s.nick for s in samples]
        print(sampleNicks)
        rootFile = ROOT.TFile(self.getOutPath(), "UPDATE")
        
        for label in self.configData.getBinlabels():
            print("doing {}".format(label))
            histName = str(sampleNicks[0])+"_"+str(self.analysis.discrName)+"_"+label
            print("getting "+histName)
            oldHist = rootFile.Get(histName)
            newHist = oldHist.Clone("data_obs_"+self.analysis.discrName+"_"+label)
            print("hewHist: "+str(newHist))
            for nick in sampleNicks[1:]:
                sampleName = str(nick)+"_"+self.analysis.discrName+"_"+label
                print("doing "+sampleName)
                bufferHist = rootFile.Get(sampleName)
                print("bufferHist: "+str(bufferHist))
                newHist.Add(bufferHist)
            newHist.Write()

        rootFile.Close()

