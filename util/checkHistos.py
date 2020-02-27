import ROOT
import sys
import os
import stat

filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import nafInterface
import haddParallel
utilpath = os.path.dirname(os.path.realpath(__file__))

debug = 0

def checkHistsManager(inFiles, outFile, checkBins = False, eps = 0.0, skipHistoCheck = False, RunMode = "NAF"):
    if type(inFiles) == str:
        print("input for checkHistos was string - performing actual check")
        checkHistos(inFiles, outFile, checkBins, eps)
        return

    if skipHistoCheck:
        print("skipping histogram check activated")
        print("checking output first...")


    # creating folder for scripts 
    scriptPath = outFile.rsplit("/",1)[0]+"/checkHistos/"
    if not os.path.exists(scriptPath):
        os.makedirs(scriptPath)
    print("creating folder for histogram check scripts {}".format(scriptPath))

    # creating folder for files
    outSubDir = outFile.rsplit("/",1)[0]+"/checkHistoParts/"
    if not os.path.exists(outSubDir):
        os.makedirs(outSubDir)
    outSubPath = outSubDir+"/"+outFile.split("/")[-1]

    outFileList = []
    shellList = []
    for i, inFile in enumerate(inFiles):
        outFilePath = outSubPath.replace(".root","_{}.root".format(i))
        outFileList.append(outFilePath)

        shellPath = scriptPath+"/checkHistos_{}.sh".format(i)
        shellList.append(shellPath)

        if not skipHistoCheck:
            writeShellScript(shellPath, inFile, outFilePath, checkBins, eps)

    if skipHistoCheck:
        undoneJobs, undoneFiles = nafInterface.checkHistoTerminationCheck( shellList, outFileList)
        if len(undoneJobs) > 0 or len(undoneFiles) > 0:
            print("checking Histograms output not complete - redoing checkHistos")
            return checkHistsManager(inFiles, outFile, checkBins, eps, skipHistoCheck = False, RunMode = RunMode)
        else:
            print("check Histos output complete - skipping")

    else:
        nafInterface.checkHistoInterface(shellList, outFileList, mode = RunMode)
    

    # hadd the checked files
    if skipHistoCheck:
        print("also check if hadded output exists...")
    else:
        print("hadding the checked histogram files")
    haddParallel.haddSplitter(
        input = outFileList,
        outName = outFile,
        subName = "checkHistoParts",
        skipHadd = skipHistoCheck)
    print("done with checking histograms")




def writeShellScript(shellPath, inFile, outFile, checkBins, eps):
    script = """
#!/bin/bash
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH={arch}
cd {cmssw}/src
eval `scram runtime -sh`
cd -
python {utilpath}/checkHistos.py -i {input} -o {out} -e {eps} --checkBins={cB}
""".format(
    arch = os.environ["SCRAM_ARCH"],
    cmssw = os.environ["CMSSW_BASE"],
    utilpath = utilpath, input = inFile,
    out = outFile, eps = eps, cB = checkBins)

    with open(shellPath, "w") as sf:
        sf.write(script)
    st = os.stat(shellPath)
    os.chmod(shellPath, st.st_mode | stat.S_IEXEC)
    

def checkHistos(inFile, outFile, checkBins = False, eps = 0.0):
    # starting the clocks      
    theclock = ROOT.TStopwatch()
    theclock.Start()
    subTimes = []
    subclock = ROOT.TStopwatch()
    subclock.Start()

    cmd = "cp -v {} {}".format(inFile, outFile)
    print(cmd)
    os.system(cmd)

    print("opening root file {}".format(outFile))
    rootFile = ROOT.TFile(outFile, "UPDATE")
    rootKeys = rootFile.GetListOfKeys()

    # getting key names
    keyNames = []
    for iKey, key in enumerate(rootKeys):
        keyNames.append(key.GetName())

    counter = 0
    nPlots = len(rootKeys)
    print("number of plots: {}".format(nPlots))
    
    for iKey, key in enumerate(keyNames):
        if debug>9: print("="*30)
        if debug>9: print("handling key {}".format(key))

        counter += 1
        if counter%1000==0:
            print("checked {}/{} histos.".format(counter, nPlots))
            subTime = subclock.RealTime()
            subTimes.append(subTime)
            subclock.Start()

        histChanged = False
        
        if checkBins:
            thisHist = rootFile.Get(key)
            if debug>19: print("checking bins")
            if debug>19: print("hist min {}".format(thisHist.GetMinimum()))
            
            if thisHist.GetMinimum() < eps:
                if debug>9: print("histogram has bins with entries smaller {}".format(eps))
                nBins = thisHist.GetNbinsX()
                newHist = thisHist.Clone()
                for iBin in range(nBins):
                    if newHist.GetBinContent(iBin+1) <= eps:
                        newHist.SetBinContent(iBin+1, eps)
                        newHist.SetBinError(iBin+1, ROOT.TMath.Sqrt(eps))
                        histChanged = True



        if histChanged:
            print("histogram has changed")
            newHist.Write("", ROOT.TObject.kOverwrite)

    rootFile.Close()
    print("the renaming took {}".format(theclock.RealTime()))
    print("subtimes: {}".format(subTimes))










if __name__ == "__main__":
    import optparse
    parser = optparse.OptionParser()

    parser.add_option("-i",dest="inFile")
    parser.add_option("-o",dest="outFile")
    parser.add_option("-e",dest="epsilon",type="float")
    parser.add_option("--checkBins",dest="checkBins")
    parser.add_option("-d", "--debug", dest = "debug", default = 0)

    (opts, _) = parser.parse_args()
    global debug
    debug = opts.debug
    print(opts.checkBins)
    print(bool(opts.checkBins))
    checkHistos(opts.inFile, opts.outFile, bool(opts.checkBins), opts.epsilon)

