import sys
import os
import subprocess
import time
import datetime
import stat
import re
import ROOT
import xml.etree.ElementTree as ET
import variablebox
import plotutils
import glob
import json
import filecmp
import imp
import types
import csv


def writeSubmitCode(script, logdir, isArray = False, nscripts = 0):
  '''
  write the code for condor_submit file

  script: path to .sh-script that should be executed
  logdir: path to directory of logs
  isArray: set True if script is an array script
  nscripts: number of scripts in the array script. Only needed if isArray=True
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

  if isArray:
    submitCode+="error = "+logdir+"/"+submitScript+".$(Cluster)_$(ProcId).err\n"
    submitCode+="output = "+logdir+"/"+submitScript+".$(Cluster)_$(ProcId).out\n"
    #submitCode+="log = "+logdir+"/"+submitScript+".$(Cluster)_$(ProcId).log\n"
    submitCode+="Queue Environment From (\n"
    for taskID in range(nscripts):
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
  submit generated script to NAF and read out jobID
  submitPath: path to .sub-file
  '''
  submitCommand = "condor_submit -terse " + submitPath
  process = subprocess.Popen(submitCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
  output = process.communicate()[0]

  # extracting jobID
  try:
    jobID = int(output.split(".")[0])
  except:
    print("something went wrong with calling the condir_submit command, submission of jobs was not successful")
    print("DEBUG: jobidstring (= communicate()[0]): " + output)
    exit(0)
  print("JobID = " + jobID)
  return jobID



def submitToNAF(scripts):
  '''
  submit list of scripts to NAF
  scripts: list of .sh-scripts to be submitted
  '''
  submitclock=ROOT.TStopwatch()
  submitclock.Start()
  jobids=[]
  logdir = os.getcwd()+"/logs"
  if not os.path.exists(logdir):
    os.makedirs(logdir)
  for script in scripts:
    
    # generating code for condor_submit
    submitPath = writeSubmitCode(script, logdir)

    # submitting script 
    print 'submitting',script
    jobID = condorSubmit(submitPath)

  submittime=submitclock.RealTime()
  print "submitted ", len(jobids), " in ", submittime
  return jobids



def submitArrayToNAF(scripts,arrayName=""):
  '''
  submit scripts to NAF as array job
  scripts: list of scripts to be submitted
  arrayName: name of the outputarray
  '''

  submitclock=ROOT.TStopwatch()
  submitclock.Start()
  jobids=[]
  logdir = os.getcwd()+"/logs"
  print "logdir:", logdir
  if not os.path.exists(logdir):
    os.makedirs(logdir)
  # get nscripts
  nscripts=len(scripts)

  # create arrayscript to be run on the birds. Depinding on $SGE_TASK_ID the script will call a different plot/run script to actually run
  # $SGE_TASK_ID still exists in HTCondor system
  scriptPath=scripts[0].rsplit("/",1)[0]
  print "basepath to scripts:", scriptPath
  arrayPath=scriptPath+"/ats_"+arrayName+".sh"
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
  submitPath = writeSubmitCode(arrayPath,logdir, isArray=True, nscripts)

  # submitting script
  print('submitting '+ submitPath)
  jobID = condorSubmit(submitPath)

  submittime=submitclock.RealTime()
  print "submitted ", len(jobids), " in ", submittime
  return [jobID]



def do_qstat(jobids):
  '''
  monitoring of array jobs via condor_q function. Loops condor_q output until all scripts have been terminated
  TODO: what about jobs in 'hold'? not yet considered
  jobids: ID of jobs to be monitored
  '''
  allfinished=False
  print "checking job status in condor_q ..."
  while not allfinished:
    time.sleep(20)
    a = subprocess.Popen(['condor_q'], stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
    qstat=a.communicate()[0]
    lines=qstat.split('\n')
    nrunning=0
    # sum all jobs that are still idle or running
    for line in lines:
      if "Total for query" in line:
        joblist = line.split(";")[1]
        states = joblist.split(",")
        jobs_running = int(states[3].split()[0])
        jobs_idle =  int(states[2].split()[0])
        print(str(jobs_running) + " jobs running, " + str(jobs_idle) + " jobs idling")
        nrunning = jobs_running + jobs_idle

    if nrunning == 0:
      print "all jobs are finished"
      allfinished=True

""" Helper function to submit NAF jobs"""
def helperSubmitNAFJobs(scripts,outputs,nentries):
  # submit run scripts
  print 'submitting scripts'
  #jobids=submitToNAF(scripts)
  jobids=submitArrayToNAF(scripts, "PlotPara")
  do_qstat(jobids)

  # check outputs
  print 'checking outputs'
  failed_jobs=check_jobs(scripts,outputs,nentries)
  retries=0
  while retries<=3 and len(failed_jobs)>0:
    retries+=1
    print 'the following jobs failed'
    for j in failed_jobs:
      print j
    if len(failed_jobs)>=0.6*len(scripts):
      print "!!!!!\n More Than 60 percent of your jobs failed. Check:\n A) Your code (and logfiles) \n B) The status of the batch stytem e.g. http://bird.desy.de/status/day.html\n !!!!!"
    print 'resubmitting'
    jobids=submitToNAF(failed_jobs)
    do_qstat(jobids)
    failed_jobs=check_jobs(scripts,outputs,nentries)
  if retries>=10:
    print 'could not submit jobs'
    sys.exit()

def check_jobs(scripts,outputs,nentries):
  '''
  check if jobs have terminated successfully. criterion: generated .root.cutflow.txt files with fitting entries
  '''
  failed_jobs=[]
  noCutflow = 0
  wrongEntry = 0
  for script,o,n in zip(scripts,outputs,nentries):
    if not os.path.exists(o+'.cutflow.txt'):
      failed_jobs.append(script)
      noCutflow += 1
      continue
    f=open(o+'.cutflow.txt')
    processed_entries=-1
    for line in f:
      s=line.split(' : ')
      if len(s)>2 and 'all' in s[1]:
        processed_entries=int(s[2])
        break
    if n!=processed_entries:
      failed_jobs.append(script)
      wrongEntry += 1
  print("jobs without cutflow file: " + str(noCutflow))
  print("jobs with wrong entry in cutflow file: " + str(wrongEntry))
  return failed_jobs

