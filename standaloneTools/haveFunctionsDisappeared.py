import re
import os
import subprocess

inFile = "plotutils_save.py"
with open(inFile, "r") as f:
    lines = f.readlines()

fncDefs = []
for line in lines:
    if re.search(r'def\ .*?\(.*?\):', line):
        defline = re.findall(r'def\ .*?\(', line)[0][:-1]
        fncDefs.append(defline)

searchDir = "util"
searchFiles = os.listdir(searchDir)
searchFiles = [searchDir + "/" + f for f in searchFiles if f.endswith(".py")]

uncalledDefs = []
for fnc in fncDefs:
    called = False
    print("-"*50)
    print("searching for "+str(fnc[4:]))
    for sfile in searchFiles:
        cmd = "grep 'def "+str(fnc[4:])+"' "+str(sfile)
        calls = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE).stdout.read()
        if len(calls) > 0:
            print("\tin file "+str(sfile))
            print(calls)
            called = True
    if not called:
        uncalledDefs.append(fnc)

print("those are the uncalled functions:")
print("\n".join(uncalledDefs))
