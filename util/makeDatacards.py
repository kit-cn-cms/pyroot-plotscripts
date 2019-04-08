import sys
import os
import glob
from subprocess import call
from fnmatch import filter
import stat

# local imports
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import nafInterface


# -- making data cards (parallel) ----------------------------------------------------------------- 
def makeDatacardsParallel(filePath, outPath, 
                    categories = None, doHdecay = True, 
                    discrname = 'finaldiscr', ,
                    datacardmaker = ' ',
                    datacardcsv=' ',
                    skipDatacards = False):

    # init directory for scripts
    scriptPath = filePath.rsplit("/",1)[0]+'/cardmakingscripts/'
    if not os.path.exists(scriptPath):
        os.makedirs(scriptPath)
    cmsswpath = os.environ['CMSSW_BASE']

    if skipDatacards:
        print("skipping datacard making activated")
        print("checking output first ...")


    shellScripts = []
    bbbFiles = []
    datacardFiles = []

    # writing shell script
    for cat in categories:
        scriptName = scriptPath+'/cardmaker_datacard_'+cat+'.sh'
        datacard = outPath+"/"+cat+"_hdecay.txt"

        datacardFiles.append(datacard)
        shellScripts.append(scriptName)
        bbbFiles.append(filePath.replace(".root","BBB_"+cat+".root"))
        
        if not skipDatacards:
            script = "#!/bin/bash \n"
            if cmsswpath != '':
                script += "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
                script += "source $VO_CMS_SW_DIR/cmsset_default.sh \n"
                script += "export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
                script += 'cd '+cmsswpath+'/src\n'
                script += 'eval `scram runtime -sh`\n'
                script += 'cd - \n'
            #--categoryName=CATEGORYNAME --rootfile=FILE --outputfile=FILE --directory=PATH -csvfile=FILE
            script += 'python '+filedir+'/DatacardScript.py '
            script += '--categoryname='+cat+' '
            script += '--rootfile='+filePath+' '
            script += '--outputfile='+outPath+'/'+cat+'_hdecay.txt '
            script += '--directory='+datacardmaker+' '
            script += '--csvfile='+datacardcsv+' \n'

            # saving and chmodding script
            with open(scriptName, "w") as dcs:
                dcs.write(script)
            st = os.stat(scriptName)
            os.chmod(scriptName, st.st_mode | stat.S_IEXEC)
    
    if skipDatacards:
        undoneShells, undoneCards = nafInterface.datacardTerminationCheck(shellScripts, datacardFiles)
        if len(undoneShells) > 0 or len(undoneCards) > 0:
            print("datacard making has not terminated sucessfully")
            print("redoing datacard making")
            return makeDatacardsParallel(
                    filePath, outPath, categories, 
                    doHdecay, discrname, datacardmaker,datacardcsv,
                    skipDatacards = False)
        else:
            print("datacard making has terminated successfully")
            return 
    
    # submitting datacardmaking scripts
    nafInterface.datacardInterface(shellScripts, datacardFiles)
    
    # hadding binbybin files to output
    #haddBinByBinFiles(bbbFiles, filePath)
    # remove empty binbybin files
    removeBinByBinFiles(bbbFiles, filePath)
    print "done creating datacards"
    
def haddBinByBinFiles(bbbFiles, filePath):
    # create folder for BBB files
    bbbPath = bbbFiles[0].split("/")[:-1]
    bbbDir = "/".join(bbbPath+["binbybinFiles"])
    backupPath = filePath.replace(".root","backup.root")
            
    if not os.path.exists(bbbDir):
        os.makedirs(bbbDir)

    # now hadd the bbb to the inital root file
    print("adding binbybin root files to other histos")
    print("(binbybin files were created during parallel datacard making)")
    cmd = ["mv", filePath, backupPath]
    call(cmd)
    cmd = ["hadd", filePath, backupPath]
    cmd += bbbFiles
    call(cmd)

    # moving BBB files to subdir
    for bbb in bbbFiles:
        print("moving "+str(bbb))
        cmd = ["mv", bbb, bbbDir+"/"]
        call(cmd)

def removeBinByBinFiles(bbbFiles, filePath):
    print("removing binbybin files")
    for bbb in bbbFiles:
        print("removing "+str(bbb))
        cmd = ["rm", bbb]
        call(cmd)

    
# -------------------------------------------------------------------------------------------------

# WIP class for peforming fits
# TODO
#   - combine datacards 
#   - create workspaces
#   - perform asimov fit
class performFits:
    def __init__(self, datacards, datacardmaker = None):
        self.datacards = datacards
        if isinstance(self.datacards, basestring):
            self.datacards = glob.glob(self.datacards)

        self.dcmaker = datacardmaker
        if not self.dcmaker:
            self.dcmaker = "/nfs/dust/cms/user/pkeicher/projects/datacardMaker/src"
        if not self.dcmaker in sys.path:
            sys.path.append(self.dcmaker)
        from datacardMaker import datacardMaker
        self.dcmaker = datacardMaker()
        self.dcmaker.replace_files = True

        self.getListOfNuisances()


    def getListOfNuisances(self):
        card = self.datacards[0]

        with open(card, "r") as infile:
            lines = list(infile)

        print("nuisances:")
        nuisances = []
        for l in lines:
            split = l.split(" ")

            if split[0] == "shapes": continue
            if "lnN" in l or "shape" in l:
                if "#" in split: continue
                name = split[0]
                print(name)
                nuisances.append(name)
        
        self.nuisances = nuisances

    
    def removeUncertainties(self):
        removal_list = []
        removal_list = list(set(removal_list + filter(self.nuisances, "*HDAMP")))
        #removal_list = list(set(removal_list + filter(self.nuisances, "*UE")))
        #removal_list = list(set(removal_list + filter(self.nuisances, "*scaleMu*")))
        from analysisObject import analysisObject        

        removed_cards = []
        for card in self.datacards:
            card = os.path.abspath(card)
            aO = analysisObject(pathToDatacard = card)

            for cat in aO:
                # add data obs line
                aO[cat].observation = "data_obs"
           
                aO.delete_uncertainties_for_all_processes(removal_list)
                basename = os.path.basename(card)
                dirname  = os.path.dirname(card)
                new_card = os.path.join(dirname, "removed_"+basename)
    
                d = datacardMaker(analysis = aO, outputpath = new_card)
                removed_cards.append(new_card)

        self.datacards = removed_cards

    def addAutoMC(self, evtThreshold = 0, includeSignal = 0, histMode = 1):
        for card in self.datacards:
            newlines = []
            with open(card, "r+") as infile:
                lines = infile.read().splitlines()
                categories = []
                for n, line in enumerate(lines):
                    if n!=len(lines) and line.startswith("bin") and lines[n+1].startswith("observation"):
                        categories = line.split()[1:]
                        print("found categories:\n"+str(categories))
                    if not "BDTbin" in line:
                        if line.startswith("kmax"):
                            entries = line.split()
                            entries[1] = "*"
                            line = " ".join(entries)
                        newlines.append(line)
                    else:
                        print("skipping line "+line)
                for cat in categories:
                    automc = cat+" autoMCStats {} {} {}".format(
                        evtThreshold, includeSignal, histMode)
                    if automc in lines: continue
                    print("writing line "+automc)
                    newlines.append(automc)
            with open(d, "w") as newfile:
                newfile.write("\n".join(newlines))

    #def createFitScripts(self):
    #pass
        # TODO
        #   - find out which datacards to combine
        #   - write one shell script for each combined datacard
        #   - load cmssw version from philip
        #   - use combineCards.py
        #   - create workspace with do_workspaces
        #   - start combine fits
















