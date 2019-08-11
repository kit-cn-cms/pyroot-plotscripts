import sys
import os
import ROOT
import pandas
import Systematics

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(os.path.dirname(filedir))

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses

# samples
# input path
path_mwassmer = "/nfs/dust/cms/user/mwassmer/MonoTop/ntuples_2018"

ttbarPathS = (
    path_mwassmer
    + "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root"
    + ";"
    + path_mwassmer
    + "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root"
    + ";"
    + path_mwassmer
    + "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/*nominal*.root"
)

# VJetsPathS = (
# path_mwassmer
# + "/DYJets*/*nominal*.root"
# + ";"
# + path_mwassmer
# + "/WJets*/*nominal*.root"
# )

# ttVPathS = (
# path_mwassmer
# + "/TTW*/*nominal*.root"
# + ";"
# + path_mwassmer
# + "/TTZToLLNuNu*/*nominal*.root"
# + ";"
# + path_mwassmer
# + "/TTZToQQ*/*nominal*.root"
# )

# dibosonPathS = (
# path_mwassmer
# + "/WW_*/*nominal*.root"
# + ";"
# + path_mwassmer
# + "/WZ_*/*nominal*.root"
# + ";"
# + path_mwassmer
# + "/ZZ_*/*nominal*.root"
# )

# stpath = path_mwassmer + "/ST_*/*nominal*.root"

# ttHpath = (
# path_mwassmer
# + "/ttHTobb_M125*/*nominal*.root"
# + ";"
# + path_mwassmer
# + "/ttHToNonbb_M125*/*nominal*.root"
# )

# ttZpath = (
# path_mwassmer
# + "/TTZToQQ*/*nominal*.root"
# + ";"
# + path_mwassmer
# + "/TTZToBB*/*nominal*.root"
# + ";"
# + path_mwassmer
# + "/TTZToLLNuNu_M-10*/*nominal*.root"
# + ";"
# )

# SELECTIONS

# need to veto muon events in electron dataset to avoid double counting and vice versa
#sel_MET = (
#    "(1.)"
#)

sel_MET = "((Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_vX == 1) || (Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_vX == 1))"

# select events without huge MuR/MuF weights
# sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'
sel_StrangeMuWeights = "*1.0"


# ======= #
# WEIGHTS #
# ======= #
# defaultWeight = "Weight_GEN_nom*Weight_pu69p2*Weight_CSV"
defaultWeight = "Weight_GEN_nom*Weight_pu69p2"

# pile up weights
pileupWeightUp = "Weight_GEN_nom*Weight_pu69p2Up"
pileupWeightDown = "Weight_GEN_nom*Weight_pu69p2Down"

## lepton scale factors
electronSFs = "((N_TightElectrons==1 && N_LooseElectrons==2)*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0]*LooseElectron_IdentificationSF[1]*LooseElectron_ReconstructionSF[1]+(N_TightElectrons==2 && N_LooseElectrons==2)*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0]*Electron_IdentificationSF[1]*Electron_ReconstructionSF[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0])"
muonSFs = "((N_TightMuons==1 && N_LooseMuons==2)*Muon_IdentificationSF[0]*Muon_IsolationSF[0]*LooseMuon_IdentificationSF[1]*LooseMuon_IsolationSF[1]+(N_TightMuons==2 && N_LooseMuons==2)*Muon_IdentificationSF[0]*Muon_IsolationSF[0]*Muon_IdentificationSF[1]*Muon_IsolationSF[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IdentificationSF[0]*Muon_IsolationSF[0])"

#electronSFs_up = "((N_TightElectrons==1 && N_LooseElectrons==2)*Electron_IdentificationSFUp[0]*Electron_ReconstructionSFUp[0]*LooseElectron_IdentificationSFUp[1]*LooseElectron_ReconstructionSFUp[1]+(N_TightElectrons==2 && N_LooseElectrons==2)*Electron_IdentificationSFUp[0]*Electron_ReconstructionSFUp[0]*Electron_IdentificationSFUp[1]*Electron_ReconstructionSFUp[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_IdentificationSFUp[0]*Electron_ReconstructionSFUp[0])"
#electronSFs_down = "((N_TightElectrons==1 && N_LooseElectrons==2)*Electron_IdentificationSFDown[0]*Electron_ReconstructionSFDown[0]*LooseElectron_IdentificationSFDown[1]*LooseElectron_ReconstructionSFDown[1]+(N_TightElectrons==2 && N_LooseElectrons==2)*Electron_IdentificationSFDown[0]*Electron_ReconstructionSFDown[0]*Electron_IdentificationSFDown[1]*Electron_ReconstructionSFDown[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_IdentificationSFDown[0]*Electron_ReconstructionSFDown[0])"
#muonSFs_up = "((N_TightMuons==1 && N_LooseMuons==2)*Muon_IdentificationSFUp[0]*Muon_IsolationSFUp[0]*LooseMuon_IdentificationSFUp[1]*LooseMuon_IsolationSFUp[1]+(N_TightMuons==2 && N_LooseMuons==2)*Muon_IdentificationSFUp[0]*Muon_IsolationSFUp[0]*Muon_IdentificationSFUp[1]*Muon_IsolationSFUp[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IdentificationSFUp[0]*Muon_IsolationSFUp[0])"
#muonSFs_down = "((N_TightMuons==1 && N_LooseMuons==2)*Muon_IdentificationSFDown[0]*Muon_IsolationSFDown[0]*LooseMuon_IdentificationSFDown[1]*LooseMuon_IsolationSFDown[1]+(N_TightMuons==2 && N_LooseMuons==2)*Muon_IdentificationSFDown[0]*Muon_IsolationSFDown[0]*Muon_IdentificationSFDown[1]*Muon_IsolationSFDown[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IdentificationSFDown[0]*Muon_IsolationSFDown[0])"

## trigger scale factors
## DANGERZONE: ELECTRON TRIGGER NOT ADDED TO NTUPLES YET, USE INTERNAL SFS
## electronTrigger = "("+sel_singleel+"&&(Weight_EleTriggerSF>0.))*Weight_EleTriggerSF"
# electronTrigger = (
# "(" + sel_singleel + "&&(internalEleTriggerWeight>0.))*internalEleTriggerWeight"
# )
# muonTrigger = "(" + sel_singlemu + "&&(Weight_MuonTriggerSF>0.))*Weight_MuonTriggerSF"

## electronTrigger_up = "("+sel_singleel+"&&(Weight_EleTriggerSF_Up>0.))*Weight_EleTriggerSF_Up"
## electronTrigger_down = "("+sel_singleel+"&&(Weight_EleTriggerSF_Down>0.))*Weight_EleTriggerSF_Down"
# electronTrigger_up = (
# "(" + sel_singleel + "&&(internalEleTriggerWeightUp>0.))*internalEleTriggerWeightUp"
# )
# electronTrigger_down = (
# "("
# + sel_singleel
# + "&&(internalEleTriggerWeightDown>0.))*internalEleTriggerWeightDown"
# )
# muonTrigger_up = (
# "(" + sel_singlemu + "&&(Weight_MuonTriggerSF_Up>0.))*Weight_MuonTriggerSF_Up"
# )
# muonTrigger_down = (
# "(" + sel_singlemu + "&&(Weight_MuonTriggerSF_Down>0.))*Weight_MuonTriggerSF_Down"
# )


# dictionary of expressions to replace in systematics csv
weightReplacements = {
    # default weight
    "DEFAULTWEIGHT": defaultWeight,
    # pileup weights
    "PUWEIGHTUP": pileupWeightUp,
    "PUWEIGHTDOWN": pileupWeightDown,
    ## lepton scale factors
    # "LEPTONSFS": "(" + electronSFs + "+" + muonSFs + ")",
    # "ELESFUP": "(" + electronSFs_up + "+" + muonSFs + ")",
    # "ELESFDOWN": "(" + electronSFs_down + "+" + muonSFs + ")",
    # "MUSFUP": "(" + electronSFs + "+" + muonSFs_up + ")",
    # "MUSFDOWN": "(" + electronSFs + "+" + muonSFs_down + ")",
    ## trigger scale factors
    # "TRIGGERSFS": "(" + electronTrigger + "+" + muonTrigger + ")",
    # "ELETRIGSUP": "(" + electronTrigger_up + "+" + muonTrigger + ")",
    # "ELETRIGSDOWN": "(" + electronTrigger_down + "+" + muonTrigger + ")",
    # "MUTRIGSUP": "(" + electronTrigger + "+" + muonTrigger_up + ")",
    # "MUTRIGSDOWN": "(" + electronTrigger + "+" + muonTrigger_down + ")",
    ## do weights for data
    # "DOWEIGHTS": "(DoWeights==1)+(DoWeights==0)*1.0",
}

# Lumi weight
lumi = "59.7*"

# nominal weight
nominalweight = (
    "NomWeight:=("
    + defaultWeight
    + "*"
    + muonSFs
    + "*"
    + electronSFs
    + ")"
    + "*(DoWeights==1)+(DoWeights==0)*1.0"
    # + electronSFs
    # + "+"
    # + muonSFs
    # + ")"
    # + "*"
    # + "("
    # + electronTrigger
    # + "+"
    # + muonTrigger
    # + ")"
    # + ")*(DoWeights==1)+(DoWeights==0)*1.0"
)


sampleDict = plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees = True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots = [
    plotClasses.Sample(
    "MET",
    ROOT.kBlack,
    path_mwassmer + "/MET*/*nominal*.root",
    sel_MET ,
    "MET",
    samDict=sampleDict,
    readTrees=doReadTrees,
    ),
    #plotClasses.Sample(
    #"SingleEl",
    #ROOT.kBlack,
    #path_mwassmer + "/EGamma*/*nominal*.root",
    #sel_singleel ,
    #"SingleEl",
    #samDict=sampleDict,
    #readTrees=doReadTrees,
    #),
]


# print("limit samples")
samples = [
    # signal samples
    plotClasses.Sample(
        "VectorMonotop_Mphi_2000_Mchi_1500",
        ROOT.kCyan,
        path_mwassmer + "/VectorMonotop_Mphi_2000_Mchi_1500/*nominal*.root",
        # lumi reweighting factor due to stupid cross section calculation
        lumi + sel_MET,
        "VectorMonotop_Mphi_2000_Mchi_1500",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="signal",
    ),
    plotClasses.Sample(
        "t#bar{t}",
        ROOT.kMagenta,
        ttbarPathS,
        lumi + sel_MET,
        "ttbar",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    # minor samples
    plotClasses.Sample(
        "Single Top",
        ROOT.kBlue,
        path_mwassmer + "/ST_*/*nominal*.root",
        lumi + sel_MET,
        "singlet",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "Z(#nu#nu)+jets",
        ROOT.kGreen - 3,
        path_mwassmer + "/ZJetsToNuNu_HT*/*nominal*.root",
        lumi + sel_MET,
        "znunujets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "Z(ll)+jets",
        ROOT.kGreen - 5,
        path_mwassmer + "/DYJetsToLL*/*nominal*.root",
        lumi + sel_MET,
        "zlljets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "W(l#nu)+jets",
        ROOT.kOrange,
        path_mwassmer + "/WJetsToLNu*/*nominal*.root",
        lumi + sel_MET,
        "wlnujets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "QCD",
        ROOT.kBlue - 10,
        path_mwassmer + "/QCD*/*nominal*.root",
        lumi + sel_MET,
        "qcd",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "Diboson",
        ROOT.kAzure + 2,
        path_mwassmer + "/??_TuneCP5_13TeV-pythia8*/*nominal*.root",
        lumi + sel_MET,
        "diboson",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
]

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes = processes
datacard_processes = processes


plottingsamples = [
    # plotClasses.Sample("t#bar{t}Z", ROOT.kCyan,
    #    ttZpath,
    #    lumi+sel_MET+sel_MET,
    #    "ttZ", addsamples = ["ttZbb", "ttZqq", "ttZll"],
    #    samDict = sampleDict, readTrees = doReadTrees, typ = "signal"),
    # plotClasses.Sample(
    # "V+jets",
    # ROOT.kGreen - 3,
    # VJetsPathS,
    # lumi + sel_MET ,
    # "Vjets",
    # addsamples=["wjets", "zjets"],
    # samDict=sampleDict,
    # readTrees=doReadTrees,
    # )
]

# sort subset of processes in plots. descending order
sortedProcesses = []
