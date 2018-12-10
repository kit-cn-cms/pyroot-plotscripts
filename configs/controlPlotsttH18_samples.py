import os
import sys
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses

def getSamples( pltcfg ):
    return pltcfg.samplesControlPlots
        

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


            if sample.nick.startswith("ttbarPlus") or sample.nick == "ttbarOther":
                for ue_hdamp, ue_hdamp_file in zip(pltcfg.hdamp_ue_systnames_tt_all, pltcfg.hdamp_ue_filenames_tt_all):
                    systSamples.append(
                        plotClasses.Sample(sample.name+ue_hdamp, sample.color, ue_hdamp_file, newSel,
                            sample.nick+ue_hdamp, samDict = pltcfg.sampleDict ))

            if sample.nick == "ttbarOther":
                for ue_hdamp, ue_hdamp_file in zip(pltcfg.hdamp_ue_systnames_tt_lf, pltcfg.hdamp_ue_filenames_tt_lf):
                    systSamples.append(
                        plotClasses.Sample(sample.name+ue_hdamp, sample.color, ue_hdamp_file, newSel,
                            sample.nick+ue_hdamp, samDict = pltcfg.sampleDict ))

            if sample.nick == "ttbarPlusCCbar":
                for ue_hdamp, ue_hdamp_file in zip(pltcfg.hdamp_ue_systnames_tt_cc, pltcfg.hdamp_ue_filenames_tt_cc):
                    systSamples.append(
                        plotClasses.Sample(sample.name+ue_hdamp, sample.color, ue_hdamp_file, newSel,
                            sample.nick+ue_hdamp, samDict = pltcfg.sampleDict ))

            if sample.nick == "ttbarPlusB":
                for ue_hdamp, ue_hdamp_file in zip(pltcfg.hdamp_ue_systnames_tt_b, pltcfg.hdamp_ue_filenames_tt_b):
                    systSamples.append(
                        plotClasses.Sample(sample.name+ue_hdamp, sample.color, ue_hdamp_file, newSel,
                            sample.nick+ue_hdamp, samDict = pltcfg.sampleDict ))

            if sample.nick == "ttbarPlus2B":
                for ue_hdamp, ue_hdamp_file in zip(pltcfg.hdamp_ue_systnames_tt_2b, pltcfg.hdamp_ue_filenames_tt_2b):
                    systSamples.append(
                        plotClasses.Sample(sample.name+ue_hdamp, sample.color, ue_hdamp_file, newSel,
                            sample.nick+ue_hdamp, samDict = pltcfg.sampleDict ))

            if sample.nick == "ttbarPlusBBbar":
                for ue_hdamp, ue_hdamp_file in zip(pltcfg.hdamp_ue_systnames_tt_bb, pltcfg.hdamp_ue_filenames_tt_bb):
                    systSamples.append(
                        plotClasses.Sample(sample.name+ue_hdamp, sample.color, ue_hdamp_file, newSel,
                            sample.nick+ue_hdamp, samDict = pltcfg.sampleDict ))
    return systSamples

def getAllSamples( pltcfg, analysis, samples):
    return getSamples(pltcfg) + getControlSamples(pltcfg) + getSystSamples(pltcfg, analysis, samples)

def getAllSystNames( pltcfg ):
    return pltcfg.weightSystNames

def getOtherSystNames( pltcfg ):
    return pltcfg.otherSystNames

def getWeightSystNames( pltcfg ):
    return pltcfg.weightSystNames

def getSystWeights( pltcfg ):
    return pltcfg.systWeights

