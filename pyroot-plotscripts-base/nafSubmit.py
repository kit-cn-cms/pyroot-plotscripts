import sys
import os
import subprocess
import time
import stat
import ROOT
import csv


def writeSubmitCode(script, logdir, isArray = False, nScripts = 0):
  '''
  write the code for condor_submit file

  script: path to .sh-script that should be executed
  logdir: path to directory of logs
  isArray: set True if script is an array script
  nScripts: number of scripts in the array script. Only needed if isArray=True
  '''
  submitPath = script[:-3]+".sub"
  submitScript = script.split("/")[-1][:-3]

  submitCode="universe = vanilla\n"
  submitCode+="should_transfer_files = IF_NEEDED\n"
  submitCode+="executable = /bin/bash\n"
  submitCode+="arguments = " + script + "\n"
  submitCode+="initialdir = "+os.getcwd()+"\n"
  submitCode+="notification = Never\n"
  submitCode+="priority = 0\n"
  submitCode+="request_memory = 5800M\n"
  #submitCode+="request_disk = 5800M\n"

  if isArray:
    submitCode+="error = "+logdir+"/"+submitScript+".$(Cluster)_$(ProcId).err\n"
    submitCode+="output = "+logdir+"/"+submitScript+".$(Cluster)_$(ProcId).out\n"
    #submitCode+="log = "+logdir+"/"+submitScript+".$(Cluster)_$(ProcId).log\n"
    submitCode+="Queue Environment From (\n"
    for taskID in range(nScripts):
      submitCode+="\"SGE_TASK_ID="+str(taskID)+"\"\n"
    submitCode+=")"
  else:
    submitCode+="error = "+logdir+"/"+submitScript+".$(Cluster).err\n"
    submitCode+="output = "+logdir+"/"+submitScript+".$(Cluster).out\n"
    #submitCode+="log = "+logdir+"/"+submitScript+".$(Cluster).log\n"
    submitCode+="queue"

  submitFile = open(submitPath, "w")
  submitFile.write(submitCode)
  submitFile.close()

  return submitPath


def condorSubmit(submitPath):
  '''
  submit the previosly generated submit-script to NAF and read out jobID
  submitPath: path to .sub-file

  returns jobID as integer value
  '''
  submitCommand = "condor_submit -terse " + submitPath
  process = subprocess.Popen(submitCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
  output = process.communicate()[0]

  # extracting jobID
  try:
    jobID = int(output.split(".")[0])
  except:
    print("something went wrong with calling the condir_submit command, submission of jobs was not successful")
    print("DEBUG: jobIDstring (= communicate()[0]): " + output)
    exit(0)
  print("JobID = " + str(jobID))
  return jobID


def submitToNAF(scripts):
  '''
  submit list of scripts to NAF
  scripts: list of .sh-scripts to be submitted

  returns jobIDs as list of integers
  '''
  submitclock=ROOT.TStopwatch()
  submitclock.Start()
  jobIDs=[]
  logdir = os.getcwd()+"/logs"
  if not os.path.exists(logdir):
    os.makedirs(logdir)

  for script in scripts:    
    # generating code for condor_submit
    submitPath = writeSubmitCode(script, logdir)

    # submitting script 
    print 'submitting',script
    jobID = condorSubmit(submitPath)
    jobIDs += [jobID]

  submittime=submitclock.RealTime()
  print "submitted ", len(jobIDs), " in ", submittime
  return jobIDs


def submitArrayToNAF(scripts,arrayName=""):
  '''
  submit scripts to NAF as array job
  scripts: list of scripts to be submitted
  arrayName: name of the outputarray

  returns jobID as integer in list
  '''
  submitclock=ROOT.TStopwatch()
  submitclock.Start()
  logdir = os.getcwd()+"/logs"
  print "logdir:", logdir
  if not os.path.exists(logdir):
    os.makedirs(logdir)
  # get nScripts
  nScripts=len(scripts)

  # create arrayscript to be run on the birds. Depending on $SGE_TASK_ID the script will call a different plot/run script to actually run
  # $SGE_TASK_ID still exists in HTCondor system
  scriptPath=scripts[0].rsplit("/",1)[0]
  arrayPath=scriptPath+"/ats_"+arrayName+".sh"
  print "basepath to scripts:", scriptPath

  arrayCode="#!/bin/bash \n"
  arrayCode+="subtasklist=(\n"
  for scr in scripts:
    arrayCode+=scr+" \n"
  arrayCode+=")\n"
  arrayCode+="thescript=${subtasklist[$SGE_TASK_ID]}\n"
  arrayCode+="echo \"${thescript}\"\n"
  arrayCode+=". $thescript"

  arrayFile=open(arrayPath,"w")
  arrayFile.write(arrayCode)
  arrayFile.close()
  st = os.stat(arrayPath)
  os.chmod(arrayPath, st.st_mode | stat.S_IEXEC)
 
  # generating code for condor_submit 
  submitPath = writeSubmitCode(arrayPath,logdir, isArray=True, nScripts=nScripts)

  # submitting script
  print('submitting '+ submitPath)
  jobID = condorSubmit(submitPath)

  submittime=submitclock.RealTime()
  print "submitted 1 array script in ", submittime
  return [jobID]



def do_qstat(jobIDs = False):
  '''
  monitoring of array jobs via condor_q function. Loops condor_q output until all scripts have been terminated
  TODO: what about jobs in 'hold'? not yet considered
  jobIDs: ID of jobs to be monitored (if no argument is given, all jobs of the current NAF user are monitored)
  '''
  allfinished=False
  print "checking job status in condor_q ..."
  command = ["condor_q"]
  if jobIDs:
    command += jobIDs
    command = [str(c) for c in command]
  while not allfinished:
    time.sleep(10)
    a = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
    qstat=a.communicate()[0]
    lines=qstat.split('\n')
    nrunning=0
    # sum all jobs that are still idle or running
    for line in lines:
      if "Total for query" in line:
        joblist = line.split(";")[1]
        states = joblist.split(",")
        jobsRunning = int(states[3].split()[0])
        jobsIdle =  int(states[2].split()[0])
        print(str(jobsRunning) + " jobs running, " + str(jobsIdle) + " jobs idling")
        nrunning = jobsRunning + jobsIdle

    if nrunning == 0:
      print "all jobs are finished"
      allfinished=True

""" Helper function to submit NAF jobs"""
def helperSubmitNAFJobs(scripts,outputs,nEntries):
  '''
  wrapper for submitting PlotPara scripts to NAF
  scripts: list of scripts to submit
  outputs: location of output-ROOTfiles
  nEntries: number of events per ROOTfile (used for checking the successfull termination of all scripts)
  '''
  # submit run scripts
  print 'submitting scripts'
  jobIDs=submitArrayToNAF(scripts, "PlotPara")
  do_qstat(jobIDs)

  # check outputs
  print 'checking outputs'
  failedJobs=checkJobs(scripts,outputs,nEntries)
  retries=0
  maxRetries = 5
  while retries<=maxRetries and len(failedJobs)>0:
    retries+=1
    print 'the following jobs failed'
    for job in failedJobs:
      print job
    if len(failedJobs)>=0.6*len(scripts):
      print "!!!!!\n More Than 60 percent of your jobs failed. Check:\n A) Your code (and logfiles) \n B) The status of the batch stytem e.g. http://bird.desy.de/status/day.html\n !!!!!"
    print 'resubmitting as single jobs'
    jobIDs=submitToNAF(failedJobs)
    do_qstat(jobIDs)
    failedJobs=checkJobs(scripts,outputs,nEntries)
  if retries>=maxRetries:
    sys.exit("submission of jobs was not success full after multiple tries - exiting")
  return True

def checkJobs(scripts,outputs,nEntries):
  '''
  check if jobs have terminated successfully. criterion: generated .root.cutflow.txt files with fitting entries
  scripts: list of scripts to submit
  outputs: location of output-ROOTfiles
  nEntries: number of events per ROOTfile

  returns list of failed jobs
  '''
  failedJobs=[]
  noCutflow = 0
  wrongEntry = 0
  for script,o,n in zip(scripts,outputs,nEntries):
    if not os.path.exists(o+'.cutflow.txt'):
      failedJobs.append(script)
      noCutflow += 1
      continue
    f=open(o+'.cutflow.txt')
    processed_entries=-1
    for line in f:
      s=line.split(' : ')
      if len(s)>2 and 'all' in s[1]:
        processed_entries=int(s[2])
        break
    if not n == processed_entries:
      failedJobs.append(script)
      wrongEntry += 1
  print("jobs without cutflow file: " + str(noCutflow))
  print("jobs with wrong entry in cutflow file: " + str(wrongEntry))
  return failedJobs

