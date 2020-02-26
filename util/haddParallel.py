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
utilpath = os.path.dirname(os.path.realpath(__file__))
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
        self.inputmap = plotParaClass.runscriptData["maps"]
        self.outputs = plotParaClass.runscriptData["outputs"]
        self.haddParallel = plotParaClass.analysis.haddParallel
        self.workdir = plotParaClass.analysis.workdir
        self.rootPath = plotParaClass.analysis.ppRootPath
        self.haddFiles = plotParaClass.haddFiles

        self.skipHaddParallel = plotParaClass.analysis.skipHaddParallel
        self.RunMode = plotParaClass.RunMode
        if self.skipHaddParallel:
            print("skipping HaddParallel")


    ## private functions ##
    def addHaddFiles(self):
        files = [self.rootPath]
        if self.haddFiles:
            files.extend(self.haddFiles)
        return files


    ## main function ##
    def run(self, writer):
        if self.skipHaddParallel:
            print("skipping haddParallel")
            print("but checking output first ...")



        # this function also handles non-parallel hadding (not used anymore i think)
        if not self.haddParallel:
            # TODO IMPORTANT does this work and make sense??
            print("not doing parallel hadding ...")
            try:
                rootFiles = self.addHaddFiles()
                print("rootFiles: " + str(rootFiles))
                subprocess.check_output( ["hadd"] + rootFiles + self.outputs,
                                            stderr = subprocess.STDOUT )
            except subprocess.CalledProcessError, e:
                print( "hadd failed with the following error:")
                print( e.output)
                sys.exit(-1)

            print("hadd output worked")
            print("returning rootFiles\n" + str(rootFiles) + "\nto plotParallel")
            return rootFiles


        # writing code for hadd script
        # location will be "workdir/haddScript.py"
        writer.writeHaddScript()

        # initializing lists
        outputScripts = []
        outputFiles = []

        # initializing folders    
        self.haddScriptFolder = self.workdir+'/HaddScripts/'
        self.haddOutputFolder = self.workdir+'/HaddOutputs/'
        if not os.path.exists(self.haddScriptFolder):
            os.makedirs(self.haddScriptFolder)
        if not os.path.exists(self.haddOutputFolder):
            os.makedirs(self.haddOutputFolder)
        
        print("-"*40+"\nlooping over samples in samplewiseMaps\n")
        for sample in self.inputmap:
            
            # writing shell script
            scriptname = self.haddScriptFolder+'haddscript_'+sample+'.sh'
            haddedRootName = self.haddOutputFolder+'/'+sample+'_hadded.root'
            haddedLogName = self.haddOutputFolder+'/'+sample+'_hadded.log'
            if not self.skipHaddParallel:
                writer.writeHaddShell(scriptname, haddedRootName, haddedLogName, self.inputmap[sample])

            # add root names and shell names to lists
            outputFiles.append(haddedRootName)
            outputScripts.append(scriptname)
        
        # job submission
        if self.skipHaddParallel:
            undoneJobs, undoneOutFiles = nafInterface.haddTerminationCheck(outputScripts, outputFiles)
            if len(undoneJobs) == 0 and len(undoneOutFiles) == 0:
                print("haddParallel output is complete")
                print("exiting haddParallel")
                return outputFiles
            else:
                print("haddParallel output seems incomplete")
                print("redoing haddParallel")
                self.skipHaddParallel = False
                return self.run(writer)

        nafInterface.haddInterface( outputScripts, outputFiles, mode = self.RunMode)
        print("all jobs have terminated successfully")
        print("="*40)

        return outputFiles





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
    print("nHistos: "+str(nHistos))
    return nHistos

def callHadd(targetFile, inputFiles, force = False, verbosity = 1):
    cmd = "hadd "
    if force:
        cmd += "-f "
    cmd += str(targetFile)+" "
    cmd += " ".join(inputFiles)    

    print('hadding\n' + '\n'.join(inputFiles))
    print('outfile: '+str(targetFile))
    subprocess.call( cmd, shell = True )



# -- main function for hadd handling --------------------------------------------------------------
def haddSplitter(input, outName = "", subName = "",  nHistosRemainSame = False, skipHadd = False, forceHadd = True):
    # determine wheter input is a list or a wildcard
    if type(input) == str:
        print "\nhadding from wildcard\n"
        inFiles = glob.glob(input)
    else:
        print "\nhadding from input list\n"
        inFiles = input

    if skipHadd:
        print("skip hadding was activated")
        print("check output file first ...")
        if not os.path.exists(outName):
            print("output root file does not exist - performing the usual hadding")
            skipHadd = False
    
    if not skipHadd:
        print("#"*50)
        print("haddSplitter input files are:")
        print("\n".join(inFiles))
        print("#"*50 + "\n")

    # boundaries
    filesPerHadd = 50
    nHistosBefore = 0
    nHistosAfter = 0

    # if number of histos should remain the same, count them
    if nHistosRemainSame:
        print "counting histos BEFORE hadding"
        nHistosBefore = countFiles(inFiles)


    if not skipHadd:
        # if number of input files less than filesPerHadd
        # hadd them all at once
        if len(inFiles) < filesPerHadd:
            callHadd( outName, inFiles, force = forceHadd)
        else:
            # lists for managing 
            haddParts = [] # sub parts of hadding, e.g. output_X
            haddFiles = [] # files for a specific sub hadd
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
                if (iFile%(filesPerHadd - 1) == 0 and iFile > 0) or inFile == inFiles[-1]:
                    partName = subPath.replace( ".root", "_part_"+str(len(haddParts))+".root" )
                    haddParts.append( partName )
                    callHadd( partName, haddFiles, force = forceHadd)
                    haddFiles = [] # empty out list for files to hadd for next hadd

            # consistency check
            if len(allFiles) != len(inFiles):
                print("hadding missed some files or used some twice - exiting")
                sys.exit(1)

            # adding the parts together
            print "-"*50
            print "subfiles were hadded, now hadding the whole thing together"
            print "-"*50
            callHadd( outName, haddParts, force = forceHadd)

    # if nhistos supposed to remain the same perform check
    if nHistosRemainSame:
        print "counting histos AFTER hadding"
        nHistosAfter = countFiles( [outName] )
        if nHistosAfter != nHistosBefore:
            print("hadding did not lead to the same number of hists before hadding")
            if skipHadd:
                print("redoing the hadding")
                return haddSplitter(input, outName, subName, nHistosRemainSame, 
                                    skipHadd = False, forceHadd = forceHadd)
            sys.exit(1)
    
    if skipHadd:
        print("hadding output checks out")
        print("skipping the hadd")
    else: 
        print "-"*50
        print "hadding done"
        print "-"*50

    return outName

