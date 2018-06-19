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
import nafSubmit
import scriptWriter
import haddParallel

###########################
#                         #
# P L O T P A R A L L E L #
#        C L A S S        #
###########################
class plotParallel:
    def __init__(self, workdir, pltcfg, configData, samplesData):
        ''' default init 

        takes workdir path,
        pltcfg module,
        configData module,
        samplesData module
        as arguments '''

        self.workdir = workdir

        # get pyroot-plotscript directory
        self.plotbase = self.workdir.split("/")
        while not self.plotbase[-1] == "pyroot-plotscripts":
            self.plotbase.pop(-1)
        self.plotbase = "/".join(self.plotbase)

        if pltcfg and configData and samplesData:
            # if all modules are defined construct some more variables
            self.rootPath = self.workdir + "/output.root"
            self.analysisName = self.workdir.split("/")[-1]

            self.maxevents = 5000000
            self.configData = configData
            self.samplesData = samplesData
            self.pltcfg = pltcfg

            self.finished = False
            self.haddFiles = None

            # defaults
            self.categoryNames = [""]
            self.categorySelections = ["1."]        
            
            self.systNames = self.pltcfg.weightSystNames
            self.systWeights = self.pltcfg.systWeights

            self.jsonFile = ""
            self.dataBases = []
            self.useDataBases = False
            self.addInterfaces = []
            self.MEPDFCSVFile = ""
            
            self.options = {"cirun": False,
                            "stopAfterCompile": False,
                            "haddParallel": False,
                            "useOldRoot": False,
                            "skipPlotParallel": False,
                            "skipHaddParallel": False}
            
            # check cmssw
            self.cmsswpath = os.environ['CMSSW_BASE']
            if not "CMSSW" in self.cmsswpath:
                print "you need CMSSW for this to work. Exiting!"
                exit(0)
            self.cmsswversion = os.environ['CMSSW_VERSION']

    @classmethod
    def empty(cls, workdir, rootFilePath):
        ''' this class methods initializes an empty class
        used for drawParallel scripts that dont need all the informations '''
        emptycls = plotParallel(workdir,None,None,None)
        emptycls.setEmptyValues(rootFilePath)
        return emptycls

    def setEmptyValues(self, path):
        outPath = path.replace("_limitInput","")
        if os.path.exists(outPath):
            self.outPath = outPath
        else:
            self.outPath = outPath
            #self.outPath = self.workdir + "/output.root"
        self.finished = True

        print("initialized empty plotParallel with outPath set to: "+str(self.outPath))




    
    ## setters functions ##
    def setCatNames(self, categoryNames):
        self.categoryNames = categoryNames

    def setCatSelections(self, categorySelections):
        self.categorySelections = categorySelections

    def setSystNames(self, systNames):
        self.systNames = systNames
    
    def setSystWeights(self, systWeights):
        self.systWeights = systWeights

    def setJson(self, jsonFile):
        self.jsonFile = jsonFile

    def setDataBases(self, dataBases):
        self.dataBases = dataBases
        if self.dataBases != []:
            self.useDataBases = True

    def setAddInterfaces(self, interfaces):
        interfaceCounter = 0
        for interface in interfaces:
            interfaceCounter += 1
            if isinstance( interface, basestring ):
                addModule = "addModule" + str(interfaceCounter)
                print( "loading module: " + str(interface) + " as " + addModule + " module." )
                self.addInterfaces.append( imp.load_source(addModule, interface).theInterface())
            elif isinstance( interface, types.InstanceType ):
                print( "appending class object initiated by user: " + str(interface) )
                self.addInterfaces.append(interface)
            else:
                print( "unknown additional code interface type: " + str(interface) )
        
    def setMEPDFCSV(self, csvfile):
        self.MEPDFCSVFile = csvfile
        
    def setMaxEvts(self, maxevts):
        self.maxevents = maxevts

    def setOptions(self, opts):
        for opt in opts:
            if opt in self.options:
                self.options[opt] = opts[opt]
                print( str(opt) + " set to " + str(opts[opt]))
    



    
    ## getter functions ##
    def getRootPath(self):
        if self.finished:
            return self.rootPath
        else:
            print("plotParallel.run() has not terminated successfully")
            print("                or has not been called yet -- exiting")
            sys.exit()

    def getHaddOutPath(self):
        return self.workdir+"/HaddOutputs/*.root"
    
    def getRenameInput(self):
        return self.renameInput

    def getOutPath(self):
        return self.outPath
    
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

    def setLimitPath(self):
        self.outPath = self.rootPath.replace(".root","_limitInput.root")
        return self.outPath
    

    def setRenameInput(self):
        if self.checkHaddFiles():
            self.renameInput = self.haddFiles
        else:
            self.renameInput = self.outPath



    ## private functions ##
    def globHaddFiles(self):
        allFiles = glob.glob(self.getHaddOutPath())
        allFiles = [f for f in allFiles if not "_renamed_" in f]
        return allFiles






    ## batch system handling ##
    def plotSubmitInterface(self):

        # submit run scripts
        print 'submitting scripts'
        submitOptions = {"PeriodicHold": 1500}
        jobIDs = nafSubmit.submitArrayToNAF(self.runscriptData["scripts"], "PlotPara", submitOptions = submitOptions)
        # monitoring running of jobs
        nafSubmit.do_qstat(jobIDs)

        # checking outputs
        failedJobs = self.plotCheckJobs()
        retries = 0
        maxRetries = 10
        while retries <= maxRetries and len(failedJobs) > 0:
            retries+=1
            print 'the following jobs failed'
            for job in failedJobs:
                print job
            print 'resubmitting as single jobs'
            jobIDs = nafSubmit.submitToNAF(failedJobs, submitOptions = submitOptions)
            nafSubmit.do_qstat(jobIDs)
            failedJobs = self.plotCheckJobs()
            if retries >= maxRetries:
                sys.exit("submission of jobs was not success full after multiple tries - exiting")
    
    def plotCheckJobs(self):
        print("-"*50)
        print("checking job output after plotpara")
        failedJobs=[]
        noCutflow = 0
        wrongEntry = 0
        for script, output, entries in zip(self.runscriptData["scripts"], 
                                            self.runscriptData["outputs"], 
                                            self.runscriptData["entries"]):
            if not os.path.exists(output+'.cutflow.txt'):
                failedJobs.append(script)
                noCutflow += 1
                continue
            f = open(output+'.cutflow.txt')
            processed_entries = -1
            for line in f:
                s = line.split(' : ')
                if len(s) > 2 and 'all' in s[1]:
                    processed_entries = int(s[2])
                    break
            if not entries == processed_entries:
                failedJobs.append(script)
                wrongEntry += 1
        print("jobs without cutflow file: " + str(noCutflow))
        print("jobs with wrong entry in cutflow file: " + str(wrongEntry))
        print("-"*50)
        return failedJobs





    ## main function ##
    def run(self):
        if self.options["skipPlotParallel"]:
            print("skipping plot parallel step, going staight to haddParallel")
            self.scriptsPath = self.workdir + "/plotParaScripts/"
            self.plotPath = self.workdir + "/plotParaPlots/"            
            self.ccPath = self.workdir + "/" + self.analysisName + ".cc"

            print("checking plotParallel outputs first...")
            writer = scriptWriter.scriptWriter(self)
            self.runscriptData = writer.writeRunScripts(writeScripts = False)
            failedJobs = self.plotCheckJobs()

            if len(failedJobs) == 0:
                print("plotParallel output is complete")
                print("proceeding with haddParallel")
                self.haddParallelInterface(writer)
                print("plotParallel.run is finished")
                return 

            else:
                print("plotParallel output is not complete")
                print("proceeding with plotParallel as usual")

        # check whether to use the already existing root file
        if os.path.exists(self.rootPath):
            if self.options["useOldRoot"]:
                if not self.options["haddParallel"]:
                    print("old root file found && no parallel hadding")
                    print("using old root file")
                    self.finished = True
                    return
                else:
                    print("old root file found && parallel hadding activated")
                    print("using old root file and saving haddFiles")
                    self.haddFiles = self.globHaddFiles()
                    print("type of haddFiles: " + str(type(self.haddFiles)) )
                    self.finished = True
                    return
                    
        # moving the old instance of workdir to a backup and copying C-file
        if os.path.exists(self.rootPath):
            oldWorkdir = self.workdir+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            os.rename(self.workdir, oldWorkdir)
            os.makedirs(self.workdir)

            cmd = "cp -v "+oldWorkdir+"/"+self.analysisName+".cc "+self.workdir+"/"+self.analysisName+".cc"
            subprocess.call(cmd, shell = True)
            cmd = "cp -v "+oldWorkdir+"/"+self.analysisName+" "+self.workdir+"/"+self.analysisName+"Backup"
            subprocess.call(cmd, shell = True)
        elif not os.path.exists(self.workdir):
            os.makedirs(self.workdir)

        # creating c++ programm
        self.ccPath = self.workdir + "/" + self.analysisName + ".cc"
        writer = scriptWriter.scriptWriter(self)
        writer.writeCC()

        # create rename script
        # TODO look at rename script code and maybe also move to class
        writer.writeRenameScript()

        # creating output folders
        print( "creating output folders" )
        self.scriptsPath = self.workdir + "/plotParaScripts/"
        self.plotPath = self.workdir + "/plotParaPlots/"
        if not os.path.exists(self.scriptsPath):
            os.makedirs(self.scriptsPath)
        if not os.path.exists(self.plotPath):
            os.makedirs(self.plotPath)

        # creating run script
        print( "creating run scripts" )
        # data consists of {"scripts", "outputs", "entries", "maps"}
        self.runscriptData = writer.writeRunScripts()
        # check if we should stop
        if self.options["stopAfterCompile"]:
            print( "compiling is done and stopAfterCompile option is activated - exiting" )
            self.finished = True
            sys.exit(0)

        # job submission
        self.plotSubmitInterface()
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
    def addData(self, samples, discr = "BDT_ljets"):

        sampleNicks = [s.nick for s in samples]
        rootFile = ROOT.TFile(self.getOutPath(), "UPDATE")
        
        for label in self.configData.getBinlabels():
            histName = str(sampleNicks[0])+"_"+str(discr)+"_"+label
            print("getting "+histName)
            oldHist = rootFile.Get(histName)
            newHist = oldHist.Clone("data_obs_"+discr+"_"+label)
            print("hewHist: "+str(newHist))
            for nick in sampleNicks[1:]:
                sampleName = str(nick)+"_"+discr+"_"+label
                print("doing "+sampleName)
                bufferHist = rootFile.Get(sampleName)
                print("bufferHist: "+str(bufferHist))
                newHist.Add(bufferHist)
            newHist.Write()

        rootFile.Close()

