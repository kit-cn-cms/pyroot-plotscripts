import ROOT
import datetime
class Timer:
    def __init__(self, name):
        self.name = name
        self.file = "/nfs/dust/cms/user/vdlinden/cleanup-plotscript/pyroot-plotscripts/txtfiles/timedata"
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
        
        code =  "+++++++++++++++++++++++++++++++++++++++++++++++\n"
        code += "+ realtime for "+self.name+": "+str(realtime) + "\n"
        code += "+ cputime for  "+self.name+": "+str(cputime) + "\n"
        code += "+++++++++++++++++++++++++++++++++++++++++++++++\n\n"
        print(code)
        with open(self.file, "a+") as f:
            f.write(code)

        if self.name == "main":
            with open(self.file, "a+") as f:
                f.write("\n"+"="*100+"\n")
                f.write("done with main function - exiting the script\n")
                f.write("current time: " + str(datetime.datetime.now()))
                f.write("\n"+"="*100+"\n")
