import os
import sys
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses

def getSamples( pltcfg ):
    return pltcfg.samplesLimits

def getControlSamples( pltcfg ):
    return pltcfg.samplesDataControlPlots

def getSystSamples(pltcfg, analysis, samples):
    systSamples = []

    # adding other samples
    for sample in samples:
        for sysName, sysFileName in zip(pltcfg.otherSystNames, pltcfg.otherSystFileNames):
            newSel = sample.selection
            systSamples.append( 
                plotClasses.Sample( 
                    sample.name+sysName, 
                    sample.color, 
                    sample.path.replace("nominal", sysFileName), 
                    newSel, 
                    sample.nick+sysName, 
                    samDict = pltcfg.sampleDict ))

    # adding Parton Shower variation
    for sample in samples:
        if sample.nick not in ["ttbarOther", "ttbarPlusCCbar", "ttbarPlusBBbar", "ttbarPlusB", "ttbarPlus2B"]:
            continue
        for sysName, sysFileName in zip(pltcfg.PSSystNames, pltcfg.PSSystFileNames):
            oldSel = sample.selection
            newSel = sample.selection.replace(pltcfg.ttbarMCWeight, "*1.0").replace(pltcfg.mcWeight+pltcfg.evenSel, pltcfg.mcWeightAll)
            print("adding sample for "+str(sysName))
            print("selection: "+str(newSel))
            print("instead of: "+str(oldSel))
            systSamples.append(
                plotClasses.Sample( 
                    sample.name+sysName, 
                    sample.color, 
                    sample.path.replace(pltcfg.ttbarPathS, pltcfg.path_additionalSamples+"/ttbar_"+sysFileName+"/*nominal*.root"), 
                    newSel, 
                    sample.nick+sysName, 
                    samDict = pltcfg.sampleDict ))

    # adding QCD systematic for QCD sample
    for sample in samples:
        if sample.name != "QCD":
            continue
        for sysName, sysReplaceString in zip(pltcfg.QCDSystNames, pltcfg.QCDSystReplacementStrings):
            newSel = sample.selection.replace("internalQCDweight", sysReplaceString)
            systSamples.append(
                plotClasses.Sample(
                    sample.name+sysName,
                    sample.color,
                    sample.path,
                    newSel,
                    sample.nick+sysName,
                    samDict = pltcfg.sampleDict ))


    return systSamples

def getAllSamples( pltcfg, analysis, samples ):
    return getSamples(pltcfg) + getControlSamples(pltcfg) + getSystSamples(pltcfg, analysis, samples)

def getAllSystNames( pltcfg ):
    return pltcfg.weightSystNames+pltcfg.otherSystNames+pltcfg.PSSystNames+pltcfg.QCDSystNames

def getOtherSystNames( pltcfg ):
    return pltcfg.otherSystNames+pltcfg.PSSystNames+pltcfg.QCDSystNames

def getWeightSystNames( pltcfg ):
    return pltcfg.weightSystNames

def getSystWeights( pltcfg ):
    return pltcfg.systWeights
