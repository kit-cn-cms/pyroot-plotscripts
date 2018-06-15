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

###########################
#                         #
# H A D D P A R A L L E L #
#        C L A S S        #
###########################
class haddParallel:
    def __init__(self, plotParaClass):
        ''' default init for parallel hadding
        takes class instance of plotParallel as input
        inherits the needed functions '''
        self.inputmap = plotParaClass.runscriptTuple[-1]
        self.outputs = plotParaClass.runscriptTuple[1]
        self.haddParallel = plotParaClass.options["haddParallel"]    
        self.workdir = plotParaClass.workdir
        self.rootPath = plotParaClass.rootPath





    ## private functions ##
    def addHaddFiles(self):
        files = [self.rootPath]
        if self.haddFiles:
            files.extend(self.haddFiles)
        return files




        
    ## batch system handling ##
    def haddSubmitInterface(self, listOfOutScripts, listOfOutFiles):
        firstTry = True
        nJobsDone = 0
        nTries = 0

        jobsToSubmit = listOfOutScripts
        outfilesFromSubmit = listOfOutFiles
        
        while len(jobsToSubmit) > 0 or len(outfilesFromSubmit) > 0 or nJobsDone != len(listOfOutFiles):
            nTries += 1
            if nTries >= 15:
                print("hadding did not work after 15 tries. ABORTING")
                exit(1)
            if firstTry:
                print("submitting haddParallel scripts")
                jobids = nafSubmit.submitArrayToNAF(jobsToSubmit, "haddPara")
                nafSubmit.do_qstat(jobids)
                firstTry = False            
            else:
                print("hadding did not work the last time - resubmitting as single scripts")
                jobids = nafSubmit.submitToNAF(jobsToSubmit)
                nafSubmit.do_qstat(jobids)
            
            # check if each hadd worked
            jobsToSubmit, outfilesFromSubmit, nJobsDone = self.haddCheckJobs(listOfOutScripts, listOfOutFiles)

    def haddCheckJobs(self, listOfOutScripts, listOfOutFiles):
        jobsToSubmit = []
        outfilesFromSubmit = []
        nJobsDone = 0

        noFile = 0
        wrongEntry = 0
        wrongLen = 0
        for job, jobscript in zip(listOfOutFiles,listOfOutScripts):
            isOk = True
            log = job.replace(".root", ".log")
            if os.path.exists(job) and os.path.exists(log):
                with open(log, "r") as logf:
                    jobfile = list(logf)
                if len(jobfile) == 1:
                    if jobfile[0] != "OK":
                        isOk = False
                        wrongEntry += 1
                else:
                    isOk = False
                    wrongLen += 1
            else:
                isOk = False
                noFile += 1

            if isOk:
                nJobsDone += 1
            else:
                jobsToSubmit.append(jobscript)
                outfilesFromSubmit.append(job)

        print("done checking job outputs after haddpara - results:")
        print("jobs without log file: " + str(noFile))
        print("jobs with wrong log file: " +str(wrongLen))
        print("jobs with ERROR in log file: " + str(wrongEntry))
        print("-"*50)
        return jobsToSubmit, outfilesFromSubmit, nJobsDone






    ## main function ##
    def run(self, writer):
        if not self.haddParallel:
            print("not doing parallel hadding ...")
            try:
                rootFiles = self.addHaddFiles()
                subprocess.check_output( ["hadd", rootFiles] + self.outputs,
                                            stderr = subprocess.STDOUT )
            except subprocess.CalledProcessorError, e:
                print( "hadd failed with the following error:")
                print( e.output)
                sys.exit(-1)

            print("hadd output worked")
            return rootFiles

        # doing the actual harallel histogram adding
        writer.writeHaddScript()

        # initializing lists
        listOfOutScripts = []
        listOfOutFiles = []

        # initializing folder        
        self.haddScriptFolder = self.workdir+'/HaddScripts/'
        self.haddOutputFolder = self.workdir+'/HaddOutputs/'
        if not os.path.exists(self.haddScriptFolder):
            os.makedirs(self.haddScriptFolder)
        if not os.path.exists(self.haddOutputFolder):
            os.makedirs(self.haddOutputFolder)
        
        print("looping over samples in samplewiseMaps")
        for sample in self.inputmap:
            print sample
            
            # writing shell script
            scriptname = self.haddScriptFolder+'haddscript_'+sample+'.sh'
            haddedRootName = self.haddOutputFolder+'/'+sample+'_hadded.root'
            haddedLogName = self.haddOutputFolder+'/'+sample+'_hadded.log'
            writer.writeHaddShell(scriptname, haddedRootName, haddedLogName, self.inputmap[sample])

            # add root names and shell names to lists
            listOfOutFiles.append(haddedRootName)
            listOfOutScripts.append(scriptname)
        
        # job submission
        self.haddSubmitInterface(listOfOutScripts, listOfOutFiles)
        print("all jobs have terminated successfully")
        print("="*40)

        return listOfOutFiles





# -------------------------------------------------------------------------------------------------
# function for hadding files - independent of haddParallel class
# -------------------------------------------------------------------------------------------------
def countFiles(inFiles):
    nHistos = 0
    for inFile in inFiles:
        tFile = ROOT.TFile( inFile, "READ" )
        keys = tFile.GetListOfKeys()
        nHistos += len(keys)
        tFile.Close()
    return nHistos

def callHadd(targetFile, inputFiles):
    cmd = ["hadd", targetFile] + inputFiles
    print "_"*40
    print "hadding "+"\n".join(inputFiles)
    print "\ntarget file: "+str(targetFile)
    print "-"*40
    subprocess.call( cmd )

def haddWard(input, outName = "", subName = "",  nHistosRemainSame = False):
    # determine wheter input is a list or a wildcard
    print "_"*50
    if type(input) == str:
        print "hadding from wildcard"
        inFiles = glob.glob(input)
    else:
        print "hadding from input list"
        inFiles = input

    haddclock = ROOT.TStopwatch()
    haddclock.Start()

    # boundaries
    filesPerHadd = 100
    nHistosBefore = 0
    nHistosAfter = 0

    # if number of histos should remain the same, count them
    if nHistosRemainSame:
        print "counting histos BEFORE hadding"
        nHistosBefore = countFiles(inFiles)

    # if number of input files less than filesPerHadd
    # hadd them all at once
    if len(inFiles) < filesPerHadd:
        callHadd( outName, inFiles )
    else:
        # lists for managing 
        haddParts = []
        haddFiles = []
        allFiles = []
        
        # create subfolder for haddFiles
        splitPath = outName.split("/")
        subPath = "/".join( splitPath[:-1] + [subName] )    
        if not os.path.exists(subPath):
            os.makedirs(subPath)
        subPath = "/".join( splitPath[:-1] + [subName, splitPath[-1]] )

        # loop over files
        for iFile, inFile in enumerate(inFiles):
            haddFiles.append(inFile)
            allFiles.append(inFile)

            # if filesPerHadd or end reached perform hadding
            if iFile%(filesPerHadd - 1) == 0 or inFile == inFiles[-1]:
                partName = subPath.replace( ".root", "_part_"+str(len(haddParts))+".root" )
                haddParts.append( partName )
                callHadd( partName, haddFiles )
                haddFiles = []

        # consistency check
        if len(allFiles) != len(inFiles):
            print("hadding missed some files or used some twice - exiting")
            sys.exit(1)

        # adding the parts together
        print "-"*40
        print "subfiles were hadded, now hadding the whole thing together"
        print "-"*40

        callHadd( outName, haddParts )

    # if nhistos supposed to remain the same perform check
    if nHistosRemainSame:
        print "counting histos AFTER hadding"
        nHistosAfter = countFiles( [outName] )
        if nHistosAfter != nHistosBefore:
            print("hadding did not lead to the same number of hists before hadding")
            sys.exit(1)
    
    print "-"*50
    print "hadding done"
    haddTime = haddclock.RealTime()
    print "hadding took " + str(haddTime)
    print "-"*50
    return outName
