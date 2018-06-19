import sys
import os
from subprocess import call
import stat

# local imports
import nafSubmit


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
        undoneShells, undoneCards = cardCheckJobs(shellScripts, datacardFiles)
        if len(undoneShells) > 0 or len(undoneCards) > 0:
            print("datacard making has not terminated sucessfully")
            print("redoing datacard making")
            return makeDatacardsParallel(
                    filePath, outPath, categories, 
                    doHdecay, discrname, datacardmaker,
                    skipDatacards = False)
        else:
            print("datacard making has terminated successfully")
            print("checking BBB files ...")
    else:
        # submitting jobs to batch
        datacardSubmitInterface(shellScripts, datacardFiles)

    # create folder for BBB files
    bbbPath = bbbFiles[0].split("/")[:-1]
    bbbDir = "/".join(bbbPath+["bbbFiles"])
    backupPath = filePath.replace(".root","backup.root")

    if skipDatacards:
        if os.path.exists(bbbDir) and os.path.exists(backupPath):
            print("hadding BBB files probably terminated successfully")
            print("skipping making datacards")
            return
        else:   
            print("hadding BBB files probably did not work")
            print("redoing the hadding")
            
    if not os.path.exists(bbbDir):
        os.makedirs(bbbDir)

    # now hadd the bbb to the inital root file
    print "adding root files with BBB to other histos"
    cmd='mv '+filePath+' '+backupPath
    call( cmd.split(" ") )
    cmd='hadd '+filePath+' '+backupPath+' '+' '.join(bbbFiles)
    call( cmd.split(" ") )


    cmd = 'mv '+"/".join(bbbPath)+'/*BBB*.root '+bbbDir+'/'
    call( cmd.split(" ") )

    print "done creating datacards"
    return
# -------------------------------------------------------------------------------------------------



# -- interface for communication with batch -------------------------------------------------------
def datacardSubmitInterface(shellScripts, datacardFiles, nTries = 0):
    if nTries == 0:
        jobIDs = nafSubmit.submitArrayToNAF(shellScripts, arrayName = "cardmaking")
        nafSubmit.do_qstat(jobIDs)
    elif nTries < 5:
        jobIDs = nafSubmit.submitToNAF(shellScripts)
        nafSubmit.do_qstat(jobIDs)
    else:
        print("making datacards not successfull after 5 tries - ABORTING")
        sys.exit(1)

    # checking output
    undoneShells, undoneCards = datacardCheckJobs(shellScripts, datacardFiles)

    if len(undoneCards) > 0 or len(undoneShells) > 0:
        print("some datacards have not been created - resubmitting as single scripts")
        datacardSubmitInterface(undoneShells, undoneCards, nTries+1)
    else:
        print("making datacards was successfull")
        return


def datacardCheckJobs(shellScripts, datacardFiles):
    print("-"*50)
    print("check if all datacards were created")
    undoneCards = []
    undoneShells = []
    for card, shell in zip(datacardFiles, shellScripts):
        if not os.path.exists(card):
            undoneCards.append(card)
            undoneShells.append(shell)
    print("number of undone datacards: "+str(len(undoneCards)))
    print("-"*50)
    return undoneShells, undoneCards

# -------------------------------------------------------------------------------------------------




# -- making datacards (non parallel) --------------------------------------------------------------
# TODO is this even used anymore?
def makeDatacards(filePath, outPath, 
                categories = None, doHdecay = True,
                discrname = 'finaldiscr', 
                datacardmaker = 'mk_datacard_hdecay13TeV'):

    if categories == None:
        categories = ["ljets_j4_t3", "ljets_j4_t4",
                    "ljets_j5_t3", "ljets_j5_tge4",
                    "ljets_jge6_t2", "ljets_jge6_t3",
                    "ljets_jge6_tge4"]

    hdecay = "_hdecay" if doHdecay else ""
    discr = discrname if doHdecay else "finaldiscr"

    scriptPath = filePath.rsplit("/",1)[0]+'/cardScripts/'
    if not os.path.exists(scriptPath):
        os.makedirs(scriptPath)
    scriptPath += "newCardScript.sh"

    # writing script
    script = "#!/bin/bash \n"

    #cmd = ['mk_datacard_ttbb13TeV', '-d', discr, '-c',' '.join(categories),'-o', outPath+hdecay+'.txt', filePath]
    #call(cmd)
    #script+= " ".join(cmd)+"\n"

    for cat in categories:
        cmd = ['mk_datacard_ttbb13TeV', '-d', discr, '-c', cat, '-o', outPath+'_'+cat+hdecay+'.txt', filePath]
        call(cmd)
        script+= " ".join(cmd)+"\n"

    with open(scriptPath, "w") as cs:
        cs.write(script)
# -------------------------------------------------------------------------------------------------
