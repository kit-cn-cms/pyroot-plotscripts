import os
import sys
import re
import subprocess
from collections import Counter

importedFile = "util/scriptgenerator.py"
importedFile = sys.argv[1]
importedFileName = importedFile.split("/")[-1].replace(".py","")
searchedDir = "plottingscripts"
searchedDir = sys.argv[2]
if searchedDir == "-f":
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
    logFile +="-"*50+"\n"
    logFile += "searching for calls in "+str(observedFile)+"\n"
    for key in fncCalls:
        calls = subprocess.Popen("grep '"+str(key)+"(' "+observedFile, shell=True, stdout = subprocess.PIPE).stdout.read()
        calls = calls.split("\n")[:-1]
        fncCalls[key] += len(calls)
        if len(calls) > 0:
            # add import location
            logFile += "now at function "+str(key)+"\n"
            logFile += "command:\n"
            command = 'sed -i -e "s/'+str(key)+'(/'+str(importedFileName)+'.'+str(key)+'(/g" '+str(observedFile)
            logFile += command +"\n"
            a = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE).stdout.read()
            newcalls = subprocess.Popen("grep '"+str(key)+"(' "+observedFile, shell=True, stdout = subprocess.PIPE).stdout.read()
            newcalls = newcalls.split("\n")[:-1]
            logFile += "replaced lines:\n"
            for call in newcalls:
                logFile += "\t"+str(call)+"\n"
            logFile += "\n"
    logFile += "*"*50+"\n"
    logFile += "replacing import line:\n"
    command = 'sed -i -e "s/from '+str(importedFileName)+' import \*/import '+str(importedFileName)+'/g" '+str(observedFile)
    logFile += str(command)+"\n"
    a = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE).stdout.read()
    newlines = subprocess.Popen("grep 'import "+str(importedFileName)+"' "+str(observedFile), shell=True, stdout = subprocess.PIPE).stdout.read()
    newlines = newlines.split("\n")[:-1]
    logFile += "replaced lines:\n"
    for line in newlines:
        logFile += "\t"+str(line)+"\n"

logFile += "="*50+"\n"

for key in fncCalls:
    if fncCalls[key] > 0:
        logFile += str(fncCalls[key]) + "\t" + str(key)+"\n"

with open("replacing_"+importedFileName+"_"+searchedDir.replace("/","-").replace(".py","")+".log", "w") as log:
    log.write(logFile)

print logFile
