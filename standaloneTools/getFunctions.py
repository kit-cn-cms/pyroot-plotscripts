import os
import sys
import re
import subprocess
from collections import Counter

importedFile = "util/scriptgenerator.py"
importedFile = sys.argv[1]
searchedDir = "plottingscripts"
searchedDir = sys.argv[2]
if sys.argv[2] == "-f":
    observedFiles = [sys.argv[3]]
    searchedDir = "_".join(observedFiles)
else:
    observedFiles = os.listdir(searchedDir)
    observedFiles = [searchedDir+"/"+f for f in observedFiles if f.endswith(".py")]

logFile = "searching for function calls of file "+str(importedFile)+" in directory "+str(searchedDir)
logFile += "\n"+"="*50+"\n"

functions = subprocess.Popen("grep 'def ' "+importedFile, shell = True, stdout = subprocess.PIPE).stdout.read()

functions = functions.split("\n")
fncCalls = {}
for fnc in functions:
    if re.search(r'def\ .*\(.*\):', fnc):
        fncName = re.findall(r'def\ .*?\(', fnc)[0][4:-1]
        fncCalls[fncName] = 0

for observedFile in observedFiles:
    logFile += "searching for calls in "+str(observedFile)+"\n"
    for key in fncCalls:
        calls = subprocess.Popen("grep '"+str(key)+"(' "+observedFile, shell=True, stdout = subprocess.PIPE).stdout.read()
        calls = calls.split("\n")[:-1]
        fncCalls[key] += len(calls)

logFile += "="*50+"\n"

for key in fncCalls:
    if fncCalls[key] > 0:
        logFile += str(fncCalls[key]) + "\t" + str(key)+"\n"

with open("get_"+importedFile.split("/")[-1].replace(".py","")+"_"+searchedDir.replace("/","-").replace(".py","")+".log", "w") as log:
    log.write(logFile)

print logFile
