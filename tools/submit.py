#"/usr/bin/env python
# use this script to submit all *.sh files to the cluster
# usage:
# python submit.py -f path/to/script/folder [patterns]
# python submit.py filename1 filename2 ...
import sys
import os
import re
from subprocess import call

# read given arguments
if len(sys.argv) < 2:
    sys.exit("need at least one argument, try --help")
if "--help" in sys.argv or "-h" in sys.argv:
    print("this script is used to submit shell files to the cluster")
    print("it can only be used on HTC clusters")
    print("at the moment (May 2018) these are 'naf-cms11.desy.de' and 'naf-cms12.desy.de'")
    print("-"*70)
    print("how to use:")
    print("submitting a single script or a list of scripts:")
    print("\tpython submit.py path/file1 path/file2 ...\n")
    print("submitting all scrpits in a folder:")
    print("\tpython submit.py -f path/to/folder\n")
    print("only submit files in a folder following a specific pattern, e.g. '_test':")
    print("\tpython submit.py -f path/to/folder 'pattern'\n")
    print("submit all jobs together as an array (only for non-array jobs, i.e. no inception!):")
    print("\tpython submit.py -a desired/array/name.sh file1.sh file2.sh")
    print("\tpython submit-py -a desired/array/name.sh -f path/to/folder 'pattern'")
    sys.exit()

if "-a" in sys.argv:
    index = sys.argv.index("-a")
    arrayName = sys.argv[index+1]
    arraySubmit = True
else:
    arraySubmit = False

if "-f" in sys.argv:
    index = sys.argv.index("-f")
    filepath = sys.argv[index+1]+"/"
    pattern = ""
    if len(sys.argv) > index+2:
        pattern = sys.argv[index+2]
    files = [os.path.join(root, name)
            for root, dirs, files in os.walk("./"+filepath)
            for name in files
            if pattern in name and name.endswith((".sh"))]
else:
    files = sys.argv[3:] if arraySubmit else sys.argv[1:]

# create log directory
if not os.path.exists("logs"):
    os.makedirs("logs")

# function to check if script is an array script
def checkArray(script):
    with open(script, "r") as s:
        scr = s.read()
    arraymeta = re.search("#ARRAYMETA:\ ntasks\ [0-9]+", scr)
    if arraymeta:
        nTasks = arraymeta.group()[19:]
        print(script+"is an array job with "+nTasks+" subtasks.")
        return True, int(nTasks)
    else:
        return False, None

# function to write code for condor_submit submission
def writeSubmitCode(script, isArray, nTasks):
    submitPath = script[:-3]+".sub"
    fileName = script.split("/")[-1][:-3]

    submitCode = "universe = vanilla\n"
    #submitCode += "should_transfer_files = IF_NEEDED\n"
    submitCode += "executable = /bin/bash\n"
    submitCode += "arguments = " + script + "\n"
    #submitCode += "notification = Never\n"
    #submitCode += "priority = 0\n"
    #submitCode += "request_memory = 4000M\n"
    #submitCode += "request_disk = 4000M\n"
    if isArray:
        submitCode += "error = logs/" + fileName + "_$(Cluster)_$(ProcId).err\n"
        submitCode += "output = logs/" + fileName + "_$(Cluster)_$(ProcID).out\n"
        #submitCode += "log = logs/" + fileName + "_$(Cluster)_$(ProcId).log\n"
        submitCode += "Queue Environment From (\n"
        for taskID in range(nTasks):
            submitCode += "\"SGE_TASK_ID=" + str(taskID) + "\"\n"
        submitCode += ")"
    else:
        submitCode += "error = logs/" + fileName + "_$(Cluster).err\n"
        submitCode += "output = logs/" + fileName + "_$(Cluster).out\n"
        #submitCode += "log = logs/" + fileName + "_$(Cluster).log\n"
        submitCode += "queue"

    with open(submitPath,"w") as submitFile:
        submitFile.write(submitCode)
    
    return submitPath

def writeArrayScript(files):
    arrayCode = "#!/bin/bash\n"
    arrayCode += "#ARRAYMETA: ntasks "+str(len(files))+"\n"
    arrayCode += "subtasklist=(\n"
    for f in files:
        arrayCode += f+"\n"
    arrayCode += ")\n"
    arrayCode += "thescript=${subtasklist[$SGE_TASK_ID]}\n"
    arrayCode += "echo \"${thescript}\"\n"
    arrayCode += ". $thescript"

    with open(arrayName, "w") as arrayFile:
        arrayFile.write(arrayCode)

    return arrayName

# submitting files
if arraySubmit:
    print("writing array script")
    arrayName = writeArrayScript(files)
    print("writing submit script")
    submitName = writeSubmitCode(arrayName, True, len(files))
    print("submitting script")
    command = "condor_submit "+submitName
    call(command.split())
    sys.exit()

for f in files:
    # check if script is an array script
    isArray, nTasks = checkArray(f)
    
    print("writing submit script for "+f)
    submitName = writeSubmitCode(f, isArray, nTasks)

    print("submitting script "+submitName)
    command = "condor_submit "+submitName
    call(command.split())    
        
