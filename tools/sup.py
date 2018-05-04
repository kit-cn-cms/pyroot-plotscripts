#!/usr/bin/env python
# submits all *.sh files to cluster, either all scripts in a folder or just a list of files
# usage: ./sup.py -f path/to/scripts [script_pattern]
# or ./sup.py arbitrary number of filesnames
import os
import sys
import datetime
from subprocess import call
pattern=''
path=''
files=[]
if len(sys.argv) > 1 and sys.argv[1]=='-f':
    if len(sys.argv) > 2:
        path= sys.argv[2]+'/'
    if len(sys.argv) > 3:
        pattern= sys.argv[3]

    files = [os.path.join(root, name)
             for root, dirs, files in os.walk('./'+path)
             for name in files
             if pattern in name and name.endswith((".sh"))]

else:
    files=sys.argv[1:]

if not os.path.exists('logs'):
    os.makedirs('logs')

for f in files:
    print "checking", f
    # check if array
    inf=open(f,"r")
    lol=list(inf)
    isArray=False
    for l in lol:
      if "#ARRAYMETA: ntasks" in l:
        print l
        print l.replace("\n","").split(" ")
        thisNTasks=l.replace("\n","").split(" ")[-1]
        print f, " is an array job with ", thisNTasks, " subtasks"
        thisNTasks = int(thisNTasks)
        isArray=True
        break
    
    print "writing submit script for condor_submit"
    filename = f.split("/")[-1][:-3]
    submitscriptname = "submit_"+filename+".sub"
    print "submitscriptname:", submitscriptname
    
    submitscriptcode = "universe = vanilla\n"
    submitscriptcode += "should_transfer_files = IF_NEEDED\n"
    submitscriptcode += "executable = /bin/bash\n"
    submitscriptcode += "arguments = " + f +"\n"
    submitscriptcode += "error = logs/" + filename + "_$(Cluster)"
    if isArray:
      submitscriptcode += "_$(ProcId)"
    submitscriptcode += ".err\n"
    submitscriptcode += "output = logs/" + filename + "_$(Cluster)"
    if isArray:
      submitscriptcode += "_$(ProcId)"
    submitscriptcode += ".out\n"
    submitscriptcode += "notification = Never\n"
    submitscriptcode += "priority = 0\n"
    submitscriptcode += "request_memory = 4000M\n"
    submitscriptcode += "request_disk = 4000M\n"
    if isArray:
      submitscriptcode += "Queue Environment From (\n"
      for taskID in range(thisNTasks):
        submitscriptcode += "\"SGE_TASK_ID=" + str(taskID) + "\"\n"
      submitscriptcode += ")"
    else:
      submitscriptcode += "queue"
    
    submitscriptfile = open(submitscriptname,"w")
    submitscriptfile.write(submitscriptcode)
    submitscriptfile.close()

    print "submitting script ", f
    command = "condor_submit " + submitscriptname
    call(command.split())
