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


cmssw_head = """
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH={scram_arch}
cd {cmsswpath}/src
eval `scram runtime -sh`
cd -
"""

script_template = """#!/bin/bash
{cmssw_info}
python {script_path} {options}
"""


# -- making data cards (parallel) ----------------------------------------------------------------- 
def makeDatacardsParallel(filePath, workdir, 
                    categories = None, doHdecay = True, 
                    discrname = 'finaldiscr', 
                    datacardmaker = ' ',
                    datacardcsv=' ',
                    skipDatacards = False,
                    signalTag = "ttH",
                    nominal_key = None,
                    syst_key = None):

    # init directory for scripts
    datacardcsv=workdir+"/datacard.csv"
    if not os.path.exists(datacardcsv):
        print("WARNING: datacardcsv does not exist here: " + datacardcsv)
        print("workdir: " + workdir)
    outPath = workdir+"/datacards"
    if not os.path.exists(outPath):
        os.makedirs(outPath)

    scriptPath = filePath.rsplit("/",1)[0]+'/cardmakingscripts/'
    if not os.path.exists(scriptPath):
        os.makedirs(scriptPath)
    cmsswpath = os.environ['CMSSW_BASE']

    if skipDatacards:
        print("skipping datacard making activated")
        print("checking output first ...")


    shellScripts = []
    #bbbFiles = []
    datacardFiles = []

    # writing shell script
    for cat in categories:
        scriptName = scriptPath+'/cardmaker_datacard_'+cat+'.sh'
        datacard = outPath+"/"+cat+"_hdecay.txt"

        datacardFiles.append(datacard)
        shellScripts.append(scriptName)
        #bbbFiles.append(filePath.replace(".root","BBB_"+cat+".root"))
        
        if not skipDatacards:
            cmssw_info = ''
            if cmsswpath != '':
                cmssw_info = cmssw_head.format(scram_arch  = os.environ['SCRAM_ARCH'],
                                            cmsswpath   = cmsswpath)
            #--categoryName=CATEGORYNAME --rootfile=FILE --outputfile=FILE --directory=PATH -csvfile=FILE
            scriptdir = os.path.join(filedir,'DatacardScript.py')
            if not os.path.exists(scriptdir):
                sys.exit("ERROR: Could not find script in '{}'".format(scriptdir))
            options = []
            options += ('--categoryname='+cat).split()
            options += ('--rootfile='+filePath).split()

            datacard_name = "{}_hdecay.txt".format(cat)
            options += ('--outputfile={}'.format(os.path.join(outPath, datacard_name))).split()

            options += ('--directory='+datacardmaker).split()
            options += ('--signaltag='+signalTag).split()
            options += ('--csvfile='+datacardcsv).split()
            if not nominal_key is None:
                options += ('--nominal_key='+"'"+nominal_key+"'").split()
            if not syst_key is None:
                options += ('--syst_key='+"'"+syst_key+"'").split()
            
            script = script_template.format(
                cmssw_info  = cmssw_info,
                script_path = scriptdir,
                options     = " ".join(options)
            )
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
    #removeBinByBinFiles(bbbFiles, filePath)
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

    
