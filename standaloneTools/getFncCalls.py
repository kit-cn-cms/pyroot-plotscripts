import subprocess
import sys
import re

searchedfile = sys.argv[1]

grep = subprocess.Popen("grep 'def ' "+searchedfile, shell = True, stdout = subprocess.PIPE).stdout.read()

grep = grep.split("\n")
functions = []
for fnc in grep:
    if re.search(r'def\ .*\(.*\):', fnc):
        fncName = re.findall(r'def\ .*?\(', fnc)[0][4:-1]
        functions+= [fncName]


sw = {}
pdf = {}
for fnc in functions:

    calls = subprocess.Popen("grep "+fnc+" *.py", shell = True, stdout = subprocess.PIPE).stdout.read()
    calls += subprocess.Popen("grep "+fnc+" util/*.py", shell = True, stdout = subprocess.PIPE).stdout.read()
    calls += subprocess.Popen("grep "+fnc+" plottingscripts/*.py", shell = True, stdout = subprocess.PIPE).stdout.read()
    calls = calls.split("\n")
    calls = [call for call in calls if not "def " in call and not "scriptgenerator_save" in call and not "plot_" in call]
    calls = "\n".join(calls)
    if "scriptWriter" in calls: 
        sw[fnc] = calls
    else:
        pdf[fnc] = calls

print "function calls from script writer"
for fnc in sw:
    print "function "+fnc+"\n\n"
    print sw[fnc]
    print "-"*50
print "="*50
print "other calls"
for fnc in pdf:
    print "function "+fnc+"\n\n"
    print pdf[fnc]
    print "-"*50
        
