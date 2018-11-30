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
        self.MEPDFCSVFile = ""
        self.useLHEWeights = False
        
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
        interfaceCounter = 0
        for interface in interfaces:
            interfaceCounter += 1
            if isinstance( interface, basestring ):
                addModule = "addModule" + str(interfaceCounter)
                print( "loading module: " + str(interface) + " as " + addModule + " module." )
                self.addInterfaces.append( imp.load_source(addModule, interface).theInterface(self.analysis.workdir))
            elif isinstance( interface, types.InstanceType ):
                print( "appending class object initiated by user: " + str(interface) )
                self.addInterfaces.append(interface)
            else:
                print( "unknown additional code interface type: " + str(interface) )
        
    def setMEPDFCSV(self, csvfile):
        self.MEPDFCSVFile = csvfile
        self.useLHEWeights = True
        print("set MEPDFCSVFile to "+str(csvfile)+" and useLHEWeights to TRUE")
    
    def setUseLHEWeights(self, use_lhe):
        self.useLHEWeights = use_lhe
        print("set useLHEWeights to "+str(use_lhe))
       
    def setMaxEvts(self, maxevts):
        self.maxevents = maxevts
        print("set maxevents to "+str(maxevts))

    def setRenameInput(self):
        if self.checkHaddFiles():
            self.renameInput = self.haddFiles
        else:
            self.renameInput = self.analysis.renamedPath
        print("set renameInput to "+str(self.renameInput))

    
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
        self.scriptsPath = self.analysis.workdir + "/ppScripts/"
        self.plotPath = self.analysis.workdir + "/ppPlots/"

        # check output if skipping activated
        if self.analysis.skipPlotParallel:
            print("skip plotParallel has been activated")
            print("this only skips the naf submission for the output files that already exist")
         
        print("ppRootPath: "+str(self.analysis.ppRootPath))   
        # check what to do if rootFile already exists
        if os.path.exists(self.analysis.ppRootPath):
            # if useOldRoot is activated the old file is used with out checking its content
            # TODO: implement sanity check
            if self.analysis.useOldRoot:
                print("using old root file")
                print("using old root file and saving haddFiles")
                self.haddFiles = self.globHaddFiles()
                print("type of haddFiles: " + str(type(self.haddFiles)) )
                self.finished = True
                print("exiting plotParallel")
                return 
           
            else:
                # moving the old instance of workdir to a backup and copying C-file
                oldWorkdir = self.analysis.workdir+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                os.rename(self.analysis.workdir, oldWorkdir)
                os.makedirs(self.analysis.workdir)

                cmd = "cp -v "+oldWorkdir+"/"+self.analysis.name+".cc "+self.analysis.workdir+"/"+self.analysis.name+".cc"
                subprocess.call(cmd, shell = True)
                cmd = "cp -v "+oldWorkdir+"/"+self.analysis.name+" "+self.analysis.workdir+"/"+self.analysis.name+"Backup"
                subprocess.call(cmd, shell = True)

        elif not os.path.exists(self.analysis.workdir):
            os.makedirs(self.analysis.workdir)

        # creating c++ programm
        self.ccPath = self.analysis.workdir + "/" + self.analysis.name + ".cc"
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
        
        # debug prints
        scripts = self.runscriptData["scripts"]
        outputs = self.runscriptData["outputs"]
        entries = self.runscriptData["entries"]
        for index in range(len(scripts)):
            print("{:<10} | {:<150}\n\t{}".format(entries[index], scripts[index], outputs[index])) 


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
        rootFile = ROOT.TFile(self.getOutPath(), "UPDATE")
        
        for label in self.configData.getBinlabels():
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

