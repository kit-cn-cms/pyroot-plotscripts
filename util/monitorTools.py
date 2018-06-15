import ROOT
import datetime
import subprocess
import os
import sys

def init(workdir):
    # copying monitorTools instance to workdir
    pathtoself = os.path.dirname(os.path.abspath(__file__))
    workdirself = workdir+"/monitorToolsLocal.py"
    cmd = "cp "+pathtoself+"/monitorTools.py "+workdirself
    print "copy command:", cmd
    subprocess.call(cmd, shell=True)
    
    #replace placeholders in monitorTools with     
    timerfile = workdir+"/timings.log"
    timerfile = timerfile.replace("/","\\/")
    cmd = 'sed -i -e "s/TIMERPLACEHOLDER/'+timerfile+'/g" '+workdirself
    print "timer command", cmd
    subprocess.call(cmd, shell=True)

    classfile = workdir+"/classvars.log"
    classfile = classfile.replace("/","\\/")
    cmd = 'sed -i -e "s/CLASSPLACEHOLDER/'+classfile+'/g" '+workdirself
    print "class command", cmd
    subprocess.call(cmd, shell=True)

    # initialize the local monitor tool module
    sys.path.append(workdir)
    import monitorToolsLocal as mTL
    print "type", type(mTL)
    
    # return the module so it can be used in file
    return mTL

class Timer:
    def __init__(self, name):
        self.name = name
        self.file = "TIMERPLACEHOLDER"
    def __enter__(self):
        self.time = ROOT.TStopwatch()
        self.time.Start()
        if self.name == "main":
            with open(self.file, "a+") as f:
                f.write("="*100+"\ncalling main function - starting the script\n")
                f.write("current time: " + str(datetime.datetime.now()))
                f.write("\n"+"="*100+"\n")
    def __exit__(self, type, value, traceback):
        realtime = self.time.RealTime()
        cputime = self.time.CpuTime()
        self.time.Stop()
        
        code =  "+"*100+"\n"
        code += "+ realtime for "+self.name+": "+str(realtime) + "\n"
        code += "+ cputime  for "+self.name+": "+str(cputime) + "\n"
        code += "+"*100+"\n\n"
        print(code)
        with open(self.file, "a+") as f:
            f.write(code)

        if self.name == "main":
            with open(self.file, "a+") as f:
                f.write("\n"+"="*100+"\n")
                f.write("done with main function - exiting the script\n")
                f.write("current time: " + str(datetime.datetime.now()))
                f.write("\n"+"="*100+"\n")



def printClass(c, name):
    variables = vars(c)
    code = "*"*50+"\n"
    code+= "variables for class "+str(c)+" at '"+str(name)+"' written\n"
    code+= "*"*50+"\n"
    print code
    for key in variables:
        code += "."*20+"\n"
        code += "key:       "+str(key)+"\n"
        code += "value:     "+str(variables[key])+"\n"
        code += "type:      "+str(type(variables[key]))+"\n"
        code += "."*20+"\n"
    code+= "="*50+"\n"*5
    with open("CLASSPLACEHOLDER", "a+") as f:
        f.write(code)
    
