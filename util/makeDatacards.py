import sys
import os
from subprocess import call
import stat

# local imports
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import nafInterface


# -- making data cards (parallel) ----------------------------------------------------------------- 
def makeDatacardsParallel(filePath, outPath, 
                    categories = None, doHdecay = True, 
                    discrname = 'finaldiscr', 
                    datacardmaker = 'mk_datacard_hdecay13TeVPara',
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
            script += datacardmaker+' -d '+' '+discrname+' '+' -c '+cat
            script += ' -o '+outPath+'/'+cat+'_hdecay.txt '+filePath+'\n'

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
                    doHdecay, discrname, datacardmaker,
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
