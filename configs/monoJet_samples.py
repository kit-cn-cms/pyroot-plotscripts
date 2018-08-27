import os
import sys
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses

def setSamples( pltcfg ):
    return pltcfg.samples_background + pltcfg.samples_signal

def setControlSamples( pltcfg ):
    return pltcfg.samplesDataControlPlots

def gatherSamples(pltcfg, analysis, samples):

    systSamples = []

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



    return systSamples

def getAllSystNames( pltcfg ):
    return pltcfg.weightSystNames + pltcfg.BosonSystNames + pltcfg.ZvvBosonSystNames + pltcfg.ZllBosonSystNames + pltcfg.WBosonSystNames + pltcfg.otherSystNames

def getOtherSystNames( pltcfg ):
    return pltcfg.otherSystNames

def getWeightSystNames( pltcfg ):
    return pltcfg.weightSystNames + pltcfg.BosonSystNames + pltcfg.ZvvBosonSystNames + pltcfg.ZllBosonSystNames + pltcfg.WBosonSystNames

def getSystWeights( pltcfg ):
    return pltcfg.systWeights + pltcfg.BosonWeights + pltcfg.ZvvBosonWeights + pltcfg.ZllBosonWeights + pltcfg.WBosonWeights
