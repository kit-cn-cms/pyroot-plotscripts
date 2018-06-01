import ROOT

class Timer:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.time = ROOT.TStopwatch()
        self.time.Start()
    def __exit__(self, type, value, traceback):
        realtime = self.time.RealTime()
        cputime = self.time.CpuTime()
        self.time.Stop()
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        print("realtime for "+self.name+": "+str(realtime))
        print("cputime for  "+self.name+": "+str(cputime))
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
