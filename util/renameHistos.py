import ROOT
import sys
import os
import stat
from subprocess import call

# local imports
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import haddParallel
import nafInterface
utilpath = os.path.dirname(os.path.realpath(__file__))


# -- main function for renaming histograms --------------------------------------------------------
def renameHistos(inFiles, outFile, systNames, checkBins = False, prune = True, Epsilon = 0.0, skipRenaming = False):
    if type(inFiles) == str:
        print("input for rename Histos was string - performing actual renaming")
        renameHistosParallel(inFiles, outFile, systNames, checkBins, prune, Epsilon)
        return 
        

    if skipRenaming:
        print("skip renaming histos was activated")
        print("checking output first ...")
    else:
        print("doing parallel renaming and hadding")
    # create python script
    scriptName, scriptPath = writeRenameScript(outFile, skipRenaming)
    
    outFileList = []
    shellList = []
    
    # adding subfolder to paths for better datastructuring
    splitPath = outFile.split("/")
    outSubDir = "/".join( splitPath[:-1]+ ["renameHistosParts"])
    if not os.path.exists(outSubDir):
            os.makedirs(outSubDir)
    outSubPath = "/".join( splitPath[:-1]+["renameHistosParts", splitPath[-1]])

    # now create the shell scripts
    for iInName, inFile in enumerate(inFiles):
        outFilePath = outSubPath.replace(".root","_"+str(iInName)+".root")
        outFileList.append(outFilePath)

        shellPath = scriptPath+'/rename_'+str(iInName)+'.sh'
        shellList.append(shellPath)

        if not skipRenaming:
            script = "#!/bin/bash \n"
            cmsswpath = os.environ['CMSSW_BASE']
            if cmsswpath != '':
                script += "export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch \n"
                script += "source $VO_CMS_SW_DIR/cmsset_default.sh \n"
                script += "export SCRAM_ARCH="+os.environ['SCRAM_ARCH']+"\n"
                script += 'cd '+cmsswpath+'/src\n'
                script += 'eval `scram runtime -sh`\n'
                script += 'cd - \n'
            script += 'python '+scriptName+' '+inFile+' '+outFilePath+' '
            script += str(int(checkBins))+' '+str(int(prune))+' '+str(float(Epsilon))+' '
            script += ' '.join(systNames)+'\n'

            # writing script to file and chmodding
            with open(shellPath, "w") as sf:
                sf.write(script)
            st = os.stat(shellPath)
            os.chmod(shellPath, st.st_mode | stat.S_IEXEC)


    if skipRenaming:
        undoneJobs, undoneFiles = nafInterface.renameTerminationCheck( shellList, outFileList )
        if len(undoneJobs) > 0 or len(undoneFiles) > 0:
            print("renaming output not complete - redoing renaming")
            return renameHistos(inFiles, outFile, systNames, checkBins, prune, Epsilon, skipRenaming = False)
        else:
            print("renaming histos output complete - skipping rename histos")
    else:
        # submit jobs to batch system
        nafInterface.renameInterface(shellList, outFileList)

    # hadd the renamed scripts
    nHistosRemainSame = False if prune else True
    if skipRenaming:
        print("also check if hadded output exists ...")
    else:
        print("hadding renamed files")
    haddParallel.haddSplitter(input = outFileList,
                        outName = outFile,
                        subName = "renameHistosParts",
                        nHistosRemainSame = nHistosRemainSame,
                        skipHadd = skipRenaming)
    print("done with renaming files")
# -------------------------------------------------------------------------------------------------



# -- writing rename script ------------------------------------------------------------------------
# TODO maybe merge this with the function in scriptWriter
# TODO this function is used in the renameHistos step, the scriptWriter function is used in the plotParallel step.
def writeRenameScript(outFile, skipRenaming):
    scriptName = outFile.rsplit("/",1)[0]+"/renameScript.py"
    scriptPath = outFile.rsplit("/",1)[0]+"/renameScripts/"
    if skipRenaming and os.path.exists(scriptPath) and os.path.exists(scriptName):
        return scriptName, scriptPath

    if not os.path.exists(scriptPath):
        os.makedirs(scriptPath)
    print "creating renamescript here", scriptName

    script = "import ROOT\n"
    script+= "import sys\n"
    script+= "import os\n"
    script+= "sys.path.append('"+utilpath+"')\n"
    script+= "import renameHistos\n\n"

    script+= "inFiles = sys.argv[1]\n"
    script+= "outFile = sys.argv[2]\n"
    script+= "checkBins = int(sys.argv[3])\n"
    script+= "prune = int(sys.argv[4])\n"
    script+= "Epsilon = float(sys.argv[5])\n"
    script+= "systNames = []\n"
    script+= "if len(sys.argv)>6:\n"
    script+= "\tsystNames = sys.argv[6:]\n"
    script+= "renameHistos.renameHistosParallel(inFiles, outFile, systNames, checkBins, prune, Epsilon)\n"
    script+= "print 'renaming done'"

    with open(scriptName, "w") as sf:
        sf.write(script)

    return scriptName, scriptPath
# -------------------------------------------------------------------------------------------------




# -- actual rename function -----------------------------------------------------------------------
def renameHistosParallel(inFile, outFile, systNames, checkBins = False, prune = False, plotParaCall = False, Epsilon = 0.0):
    print ("RenameHistosStep: checking bins set to "+str(checkBins))
    # starting the clocks      
    theclock = ROOT.TStopwatch()
    theclock.Start()
    subTimes = []
    subclock = ROOT.TStopwatch()
    subclock.Start()
    
    print("#"*30)
    print("systNames:")
    print("\n".join(systNames))
    print("#"*30)

    cmd = ["cp", "-v", inFile, outFile]
    print("calling" + " ".join(cmd))
    call( cmd )

    # opening outFile
    print("opening root file "+str(inFile))
    rootFile = ROOT.TFile(inFile, "UPDATE")
    print("list of keys:")
    rootKeys = rootFile.GetListOfKeys()
    for k in rootKeys:
        print(k)
    print("-"*10)

    objectList = []
    keyNames = []

    for iKey, key in enumerate(rootKeys):       
        keyNames.append(key.GetName())

    counter = 0
    nPlots = len(rootKeys)

    print("number of plots: "+str(nPlots))

    for iKey, key in enumerate(keyNames):
        histChanged = False
        counter += 1
        
        # occasionally print time
        printstep = 1000
        if counter%printstep == 0:
            print ("renamed "+str(counter)+"/"+str(nPlots)+" plots.")
            subTime = subclock.RealTime()
            print("time for "+str(printstep)+" plots: "+str(subTime))
            subTimes.append(subTime)
            subclock.Start()

        # init empt rootHisto and newKey for comparisons
        thisName = key
        thisHist = None
        newName = thisName

        # dont need dummy variables
        if "dummy" in thisName:
            if prune:
                print("Deleting "+str(thisName)+";1")
                rootFile.Delete(thisName+";1")  
            continue

        # looping over systs and adjusting keys
        nSysts = 0
        for syst in systNames:
            if syst in newName:
                newName = newName.replace(syst, "")
                newName+= syst
                nSysts += 1

        # check nSysts
        print("nSysts: {} - Checking: {}".format(nSysts, thisName))        

        # do not need histograms with more than two systs
        if nSysts > 2:
            if not plotParaCall and prune:
                print("Deleting "+str(thisName)+";1")
                rootFile.Delete(thisName+";1")
                continue

            elif plotParaCall and ("JES" in thisName or "JER" in thisName or "_ttH_scaleFSR" in thisName or "_ttH_scaleISR" in thisName or \
                "_ttH_FSR" in thisName or "_ttH_ISR" in thisName or "_ttH_hdamp" in thisName or "ttH_ue" in thisName or \
                "_ttHbb_scaleFSR" in thisName or "_ttHbb_scaleISR" in thisName or "_ttHbb_FSR" in thisName or \
                "_ttHbb_ISR" in thisName or "_ttHbb_HDAMP" in thisName or "ttHbb_UE" in thisName or \
                (("CMS_scale" in thisName or "CMS_res_" in thisName) and \
                ("_jUp" in thisName or "_jDown" in thisName or "_j_2017Up" in thisName or "_j_2017Down" in thisName)) or \
                "_CMS_ttH_QCDScaleFactor" in thisName or "_CMS_ttHbbFROMTREES" in thisName):
                
                thisHist = rootFile.Get(thisName)
                objectList.append(thisHist)
                print(str(nSysts)+" systs - removing "+str(thisName))
                rootFile.Delete(thisName)
                rootFile.Delete(thisName+";1")
                continue


        if plotParaCall and ("SingleMu" in thisName or "SingleEl" in thisName) and nSysts > 2:
            thisHist = rootFile.Get(thisName)
            objectList.append(thisHist)
            print(str(nSysts)+" systs - removing "+str(thisName))
            rootFile.Delete(thisName)
            rootFile.Delete(thisName+";1")
            continue



        deleted = False
        # these samples to not have Gen systs at the moment -> delete the histos
        samplesWithoutGenSysts = [
            "diboson","ttbarW","ttbarZ","ttV","SingleTop","Vjets","zjets","wjets","singlet"]

        for sampleName in samplesWithoutGenSysts:
            if thisName.startswith(sampleName):
                if "CMS_ttHbb_ISR" in thisName or "CMS_ttHbb_FSR" in thisName or \
                    "CMS_ttHbb_scaleMuR" in thisName or "CMS_ttHbb_PDF" in thisName:
                    if plotParaCall or prune:
                        print("Deleting "+str(thisName)+";1")
                        thisHist = rootFile.Get(thisName)
                        objectList.append(thisHist)
                        rootFile.Delete(thisName)
                        rootFile.Delete(thisName+";1")
                        deleted = True
        if deleted: continue


        # filter histos with uncertainties not belonging to this specific sample
        deleted = False
        ttbarSamples = ["ttbarOther","ttbarPlus2B","ttbarPlusB","ttbarPlusCCbar","ttbarPlusBBbar"]
        for sampleName in ttbarSamples:
            if thisName.startswith(sampleName+"_"):
                for sampleName2 in ttbarSamples:
                    if sampleName2 == sampleName: continue
                    if (sampleName2+"Up" in thisName or sampleName2+"Down" in thisName) \
                        and not thisName.startswith(sampleName2+"_"):
                        if plotParaCall or prune:
                            print("Deleting "+str(thisName)+";1")
                            thisHist = rootFile.Get(thisName)
                            objectList.append(thisHist)
                            rootFile.Delete(thisName)
                            rootFile.Delete(thisName+";1")
                            deleted = True
        if deleted: continue                               


        if not plotParaCall:
            newHist = ""
            # only load histogram if it is really needed
            if checkBins or (newname != thisName) or thisName.startswith("QQCD_"):
                thisHist = rootFile.Get(thisName)

            if checkBins or thisName.startswith("QCD_"):
                if thisName.startswith("QCD_"):
                    nBins = thisHist.GetNbinsX()
                    newHist = thisHist.Clone()
                    objectList.append( newHist )
                    QCDEpsilon = 0.001

                    if "QCDScaleFactorDown" in thisName:
                        QCDEpsilon *= 0.5

                    for iBin in range(nBins):
                        if newHist.GetBinContent(iBin+1) <= 0.0:
                            newHist.setBin(iBin, QCDEpsilon)
                            histChanged = True

                elif thisHist.GetMinimum() < Epsilon:
                    nBins = thisHist.GetNbinsX()
                    newHist = thisHist.Clone()
                    objectList.append( newHist )
                    for iBin in range(nBins):
                        if newHist.GetBinContent(iBin+1) <= 0:
                            newHist.setBin(iBin, Epsilon)
                            histChanged = True

        if newName != thisName:
            if plotParaCall:
                thisHist = rootFile.Get(thisName)
                objectList.append(thisHist)
                rootFile.Delete(thisName+";1")
            print("changed "+str(thisName)+" to "+str(newName))
            thisHist.SetName(newName)
            thisHist.Write()

        if not plotParaCall and histChanged:
            print("histogram has changed"+str(thisName)+" "+str(newName))
            newHist.SetName(newName)
            newHist.Write("", ROOT.TObject.kOverwrite)

    rootFile.Close()
    #infile.Close()        
    print("the renaming took "+str(theclock.RealTime()))
    print("subtimes: "+str(subTimes))



def setBin(self, iBin, Epsilon):
    print("negative or zero bins in " + str(self))
    print("setting bin "+str(iBin+1)+" from "+\
        str(self.GetBinnContent(iBin+1))+" +- "+str(self.GetBinError(iBin+1)) + \
        " to " +\
        str(Epsilon)+" +- "+str(math.sqrt(Epsilon)))
    self.SetBinContent(iBin+1, Epsilon)
    self.SetBinError(iBin+1, ROOT.TMath.Sqrt(Epsilon))


