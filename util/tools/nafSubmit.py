import re
import sys
import os
import subprocess
import time
import datetime
import stat
import ROOT
default_scheduler = "bird-htc-sched13.desy.de"

def writeSubmitCode(script, logdir, hold = False, isArray = False, nScripts = 0, name = "", options = {}):
    ''' write the code for condor_submit file

    script: path to .sh-script that should be executed
    logdir: path to directory of logs

    hold: bool - should the scripts be initialized in hold state
    isArray: set True if script is an array script
    nScripts: number of scripts in the array script. Only needed if isArray=True
    options: dict of options that differ from default options

    returns basepath to submitFile as string '''

    if name == "":
        name = "plotscript"
    # handling options
    defaults = {"RequestMemory": "1000M",
                "RequestDisk": "1000M",
                "+RequestRuntime": 7200,
                "PeriodicHold": 3600,
                "PeriodicRelease": 5}
    for opt in defaults:
        if opt in options:
            defaults[opt] = options[opt]

  # if hold = True there should not be a periodic release
    if hold:
        defaults["PeriodicRelease"] = None
        print("PeriodicRelease was deactivated because hold = True")

    # writing code
    submitPath = script.replace(".sh",".sub")
    submitScript = script.split("/")[-1].replace(".sh","")
    

    submitCode = ""
    submitCode+= "universe = vanilla\n"
    submitCode+= "should_transfer_files = IF_NEEDED\n"
    submitCode+= "executable = /bin/zsh\n"
    submitCode+= "arguments = " + script + "\n"
    submitCode+= "initialdir = "+os.getcwd()+"\n"
    submitCode+= "notification = Never\n"
    #submitCode+= "priority = 0\n"
    #submitCode+= "RequestMemory = 2000\n"
    #submitCode+= "RequestDisk = 500000\n"
    submitCode+= "run_as_owner = True\n"
    #submitCode+= "job_lease_duration = 60\n"
    submitCode+= "JobBatchName = "+name+"\n"
    for opt in defaults:
        if defaults[opt]:
            if "Request" in opt:
                submitCode+=opt+" = "+str(defaults[opt])+"\n"
            if "PeriodicHold" in opt:
                submitCode+= "periodic_hold = ((JobStatus == 2) && (time() - EnteredCurrentStatus) > "+str(defaults[opt])+")\n"
            if "PeriodicRelease" in opt:
                submitCode+= "periodic_release = ((JobStatus == 5) && (time() - EnteredCurrentStatus) > "+str(defaults[opt])+")\n"  
    if hold:
        submitCode+= "hold = True\n"

    if isArray:
        submitCode+= "error = "+logdir+"/"+submitScript+".$(Cluster)_$(ProcId).err\n"
        submitCode+= "output = "+logdir+"/"+submitScript+".$(Cluster)_$(ProcId).out\n"
        submitCode+= "log = "+logdir+"/"+submitScript+".$(Cluster)_$(ProcId).log\n"
        submitCode+= "Queue Environment From (\n"
        for taskID in range(nScripts):
            submitCode+="\"SGE_TASK_ID="+str(taskID+1)+"\"\n"
        submitCode+=")"
    else:
        submitCode+="error = "+logdir+"/"+submitScript+".$(Cluster).err\n"
        submitCode+="output = "+logdir+"/"+submitScript+".$(Cluster).out\n"
        submitCode+="log = "+logdir+"/"+submitScript+".$(Cluster).log\n"
        submitCode+="queue"

    with open(submitPath, "w") as sF:
        sF.write(submitCode)

    return submitPath

def writeArrayCode(scripts, arrayName):
    ''' writing code for array script

    scripts: list of scripts to be concatenated as array
    arrayName: name of output array script
    
    returns basepath to array script as string'''

    # setting path
    scriptPath=scripts[0].rsplit("/",1)[0]
    arrayscriptpath=scriptPath+"/arrayScript_"+arrayName+".sh"
    print "basepath to scripts:", scriptPath

    # writing script
    arrayCode="#!/bin/bash \n"
    arrayCode+="subtasklist=(\n"
    for scr in scripts:
        arrayCode+=scr+" \n"
    arrayCode+=")\n"
    arrayCode+="thescript=${subtasklist[$SGE_TASK_ID]}\n"
    arrayCode+="echo \"${thescript}\"\n"
    arrayCode+="echo \"$SGE_TASK_ID\"\n"
    arrayCode+=". $thescript"

    with open(arrayscriptpath, "w") as aF:
        aF.write(arrayCode)
    
    # chmodding script
    st = os.stat(arrayscriptpath)
    os.chmod(arrayscriptpath, st.st_mode | stat.S_IEXEC)
    return arrayscriptpath


def condorSubmit(submitPath):
    ''' submit the previosly generated submit-script to NAF and read out jobID
    submitPath: path to .sub-file

    returns jobID as integer value
    '''

    # creating command    
    submitCommand = "condor_submit -terse "+submitPath
    tries = 0
    jobID = None
    while not jobID:
        # submitting
        print(submitCommand)
        process = subprocess.Popen(submitCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        process.wait()
        output = process.communicate()
        # trying to extract jobID
        try:
            jobID = int(output[0].split(".")[0])
        except:
            print("something went wrong with calling the condir_submit command, submission of jobs was not successful")
            print("DEBUG:")
            print(output)
            tries += 1
            jobID = None
            time.sleep(60)
        if tries > 10:
            print("job submission was not successful after ten tries - exiting without JOBID")
            sys.exit(-1)
    print("JobID = " + str(jobID))
    # option to remove the created submit-scripts
    #os.system("rm "+submitPath) 

    return jobID

def setupRelease(oldJIDs, newJIDs):
    ''' writes and executes code to monitor the running of jobs. releases new jobs when old ones are finished

    oldJIDs: list of jobs that need to be finished before new jobs are queued up in batch system
    newJIDs: list of jobs that wait on old jobs to be finished before being queued up in batch system

    returns ID of release job as list
    '''

    # setting paths
    releasePath = os.getcwd()+"/release"
    for ID in newJIDs:
        releasePath += "_"+str(ID)
    releaseShellPath = releasePath +".sh"
    releasePath +=".sh"
    
    basedir = os.path.dirname(os.path.realpath(__file__))

    # writing code
    releaseCode = "#!/bin/bash\n"
    releaseCode += "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n"
    releaseCode += "source $VO_CMS_SW_DIR/cmsset_default.sh\n"
    releaseCode += "cd /nfs/dust/cms/user/kelmorab/combineCMSSW/CMSSW_8_1_0/src\n"
    releaseCode += "eval `scram runtime -sh`\n"
    releaseCode += "cd "+os.getcwd()+"\n"
    releaseCode += "script=\"\n"
    releaseCode += "import sys\n"
    releaseCode += "basedir = '"+basedir+"'\n"
    releaseCode += "if not basedir in sys.path:\n"
    releaseCode += "\tsys.path.append(basedir)\n"
    releaseCode += "from nafSubmit import monitorJobStatus\n"
    releaseCode += "import os\n"
    releaseCode += "monitorJobStatus("+str(oldJIDs)+")\n"
    releaseCode += "os.system('condor_release"
    for ID in newJIDs:
        releaseCode += " "+str(ID)
    releaseCode += "')\n"
    releaseCode += "\"\n"
    releaseCode += "python -c \"$script\"\n"
    releaseCode += "rm -- \"$0\"\n"

    with open(releasePath, "w") as releaseFile:
        releaseFile.write(releaseCode)

    # chmodding script
    st = os.stat(releasePath)
    os.chmod(releasePath, st.st_mode | stat.S_IEXEC)
    
    #submitting release file
    releaseID = submitToNAF([releasePath])
    os.system("rm "+releasePath[:-3]+".sub")

    return releaseID

def submitToNAF(scripts, holdIDs = None, submitOptions = {}):
    ''' submit list of scripts to NAF

    scripts: list of .sh-scripts to be submitted
    holdIDs: list of jobIDs that need to be finished before queueing the new scripts
    submitOptions: dictionary of options that differ from default options (set in writeSubmitCode)

    returns jobIDs as list of integers '''

    submitclock=ROOT.TStopwatch()
    submitclock.Start()
    jobIDs=[]

    # setting paths
    workdir = scripts[0].split("/")[:-1]
    logdir = "/".join(workdir)+"/logs"
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    # determine hold
    hold = True if holdIDs else False

    for script in scripts:        
        # generating code for condor_submit
        submitPath = writeSubmitCode(script, logdir, hold, options = submitOptions)

        # submitting script 
        print 'submitting',script
        jobID = condorSubmit(submitPath)
        jobIDs += [jobID]

    submittime=submitclock.RealTime()
    print "submitted ", len(jobIDs), " in ", submittime

    if hold:
        # add the release script if hold = True
        print("the scripts were submitted in hold state - creating release script")
        releaseID = setupRelease(holdIDs, jobIDs)
        jobIDs += releaseID

    return jobIDs

def submitArrayToNAF(scripts, arrayName="", holdIDs=None, submitOptions = {}):
    ''' submit scripts to NAF as array job

    scripts: list of scripts to be submitted
    arrayName: name of the outputarray
    holdIDs: list of jobIDs that need to be finished before queueing the new script
    submitOptions: dictionary of options that differ from default options (set in writeSubmitCode)

    returns jobID as integer in list
    '''
    submitclock=ROOT.TStopwatch()
    submitclock.Start()
    workdir = scripts[0].split("/")[:-1]
    logdir = "/".join(workdir)+"/logs"
    print "logdir:", logdir
    if not os.path.exists(logdir):
         os.makedirs(logdir)
    # get nScripts
    nScripts=len(scripts)
    
    # generate code for array script
    arrayscriptpath = writeArrayCode(scripts, arrayName)
    # generating code for condor_submit 
    hold = True if holdIDs else False
    submitPath = writeSubmitCode(arrayscriptpath, logdir, hold = hold, isArray=True, nScripts=nScripts, name = arrayName, options = submitOptions)

    # submitting script
    print('submitting '+ submitPath)
    jobIDs = [condorSubmit(submitPath)]
    
    submittime=submitclock.RealTime()
    print "submitted", len(jobIDs), "scrips in", submittime
    
    if hold:
        print("the script was submitted in hold state - creating release script")
        releaseID = setupRelease(holdIDs, jobIDs)
        jobIDs += releaseID

    return jobIDs

def monitorJobStatus(jobIDs = None):
    ''' monitoring of jobs via condor_q function. Loops condor_q output until all scripts have been terminated
    jobIDs: list of IDs of jobs to be monitored (if no argument is given, all jobs of the current NAF user are monitored)
    hold: if set True also waits on jobs in hold state to be finished
    
    no return '''

    allfinished=False
    errorcount = 0
    print "checking job status in condor_q ..."
    command = ["condor_q"]
    # adding jobIDs to command
    if jobIDs:
        command += jobIDs
        command = [str(c) for c in command]
    command += ["-totals"]#, "|", "grep", "'Total for query'"]
    sTime = time.time()

    # counts
    times = []
    runs = []
    idles = []
    helds = []
    totals = []
    while not allfinished:
        time.sleep(300)
        # calling condor_q command
        a = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
        a.wait()
        qstat = a.communicate()[0]
        nrunning = 0
        querylines = [line for line in qstat.split("\n") if "Total for query" in line]

        # check if query matches
        if len(querylines) == 0:
            errorcount += 1
            # sometimes condor_q is not reachable - if this happens a lot something is probably wrong
            print("line does not match query")
            if errorcount == 30:
                print("something is off - condor_q has not worked for 15 minutes ...")
                time.sleep(120)
            if errorcount == 100:
                print("this does not work anymore - removing jobs")
                command[0] = "condor_rm"
                a = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, stdin = subprocess.PIPE)
                return
            continue

        errorcount = 0
        # sum all jobs that are still idle or running
        jobsRunning = 0
        jobsIdle        = 0
        jobsHeld        = 0
        for line in querylines:
            jobsRunning += int(re.findall(r'\ [0-9]+\ running', line)[0][1:-8])
            jobsIdle += int(re.findall(r'\ [0-9]+\ idle', line)[0][1:-5])
            jobsHeld += int(re.findall(r'\ [0-9]+\ held', line)[0][1:-5])

        nrunning += jobsRunning + jobsIdle + jobsHeld
        print("{:4d} running | {:4d} idling | {:4d} held |\t total: {:4d}".format(jobsRunning, jobsIdle, jobsHeld, nrunning))

        if nrunning == 0:
            print("waiting on no more jobs - exiting loop")
            allfinished=True

    print("all jobs are finished - exiting monitorJobStatus")
    return
