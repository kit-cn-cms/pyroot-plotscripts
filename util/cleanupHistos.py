import os
import sys
import ROOT

filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+"/tools")
import Systematics

debug = 0

def cleanupHistos(inFile, outFile, process, systcsv):
    # starting the clocks      
    theclock = ROOT.TStopwatch()
    theclock.Start()
    subTimes = []
    subclock = ROOT.TStopwatch()
    subclock.Start()

    systematics = Systematics.Systematics(systcsv)

    isVariation = False
    if "Up" in process or "Down" in process:
        print("process name {0} has uncertainty".format(process))
        isVariation = True
        
    isDataSample = False
    dataSamples = ["SingleMu", "SingleEl", "EGamma","MET"]
    if process in dataSamples:
        print("process name {} suggests that this is a data sample (will delete all systematics)".format(process))
        isDataSample = True


    # get all systematics
    systNames = systematics.get_all_weight_systs()
    systNames+= systematics.get_all_variation_systs()
    systNames+= systematics.get_all_rate_systs()
    print("all systematics:")
    print("\n".join(systNames))

    procSysts = []
    if not isDataSample:
        # get systematics for the process
        systematics.getSystematicsForProcesses([process])
        procSysts+= systematics.get_weight_systs(process)
        procSysts+= systematics.get_variation_systs(process)
        procSysts+= systematics.get_shape_systs(process)
    print("\nsystematics for process {}".format(process))
    print("\n".join(procSysts))

    # copying file
    cmd = "cp -v {} {}".format(inFile, outFile)
    print(cmd)
    os.system(cmd)

    # opening file and getting keys
    print("opening root file {}".format(inFile))
    rootFile = ROOT.TFile(inFile, "UPDATE")
    rootKeys = rootFile.GetListOfKeys()

    # getting key names
    keyNames = []
    for iKey, key in enumerate(rootKeys):
        keyNames.append(key.GetName())

    counter = 0
    nPlots = len(rootKeys)
    print("number of plots: {}".format(nPlots))

    # iterating over every key and renaming/deleting it if neccessary
    for iKey, key in enumerate(keyNames):
        if debug>9: print("="*30)
        if debug>9: print("handling key {}".format(key))

        counter += 1
        if counter%1000==0:
            print("cleaned up {}/{} plots.".format(counter, nPlots))
            subTime = subclock.RealTime()
            subTimes.append(subTime)
            subclock.Start()

        # init empty stuff
        thisName = key
        thisHist = None
        newName  = thisName

        # delete dummy variables
        if "dummy" in thisName:
            if debug>9: print("Deleting {};1".format(thisName))
            rootFile.Delete(thisName)
            continue

        # get number of systematics in name and move systs to back of name
        # this is needed for variated samples, where the naming scheme is
        # PROCESS_VARIATIONNAME_VARIABLENAME_OTHERSYSTS
        # shoud be
        # PROCESS_VARIABLENAME_VARIATIONNAME_OTHERSYSTS
        nSysts = 0
        currentSysts = []
        for syst in systNames:
            if syst in newName:
                currentSysts.append(syst)
                newName = newName.replace(syst, "")
                newName+= syst
                nSysts += 1

        # remove histogram if more than two systematics in name
        if nSysts>1:
            if debug>9: print("Deleting {};1 (has {} systematics)".format(thisName, nSysts))
            rootFile.Delete(thisName+";1")
            continue

        # remove systematic variations from data
        if isDataSample and nSysts>0:
            if debug>9: print("Deleting {};1 (sample is data and has systematics)".format(thisName))
            rootFile.Delete(thisName+";1")
            continue

        # check if systematic should be considered for process
        if nSysts>0:
            currentSyst = currentSysts[0]
            if currentSyst not in procSysts:
                if debug>9: print("Deleting {};1 (systematic {} not in list of systs for process {})".format(thisName, currentSyst, process))
                rootFile.Delete(thisName+";1")
                continue
    
        
        # update histogram if has new name
        if newName != thisName:
            thisHist = rootFile.Get(thisName)
            rootFile.Delete(thisName+";1")
            if debug>9: print("changed {} to {}".format(thisName, newName))
            thisHist.SetName(newName)
            thisHist.Write()

    keysAfter = len(rootFile.GetListOfKeys())
    rootFile.Close()
    print("the renaming took {}".format(theclock.RealTime()))
    print("subtimes: "+str(subTimes))
    print("{}/{} histograms left".format(keysAfter, nPlots))

    return nPlots, keysAfter







