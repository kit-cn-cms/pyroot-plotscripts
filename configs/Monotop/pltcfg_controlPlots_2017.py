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
path_mwassmer = "/nfs/dust/cms/user/mwassmer/MonoTop/ntuples_2017"

ttbarPathS = (
    path_mwassmer
    + "/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root"
    + ";"
    + path_mwassmer
    + "/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root"
    + ";"
    + path_mwassmer
    + "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root"
)

# SELECTIONS

# need to veto muon events in electron dataset to avoid double counting and vice versa
#sel_MET = (
#    "(1.)"
#)

sel_MET = "1."

# select events without huge MuR/MuF weights
# sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'
sel_StrangeMuWeights = "*1.0"


# ======= #
# WEIGHTS #
# ======= #
# defaultWeight = "Weight_GEN_nom*Weight_pu69p2*Weight_CSV"
defaultWeight = "Weight_GEN_nom"

# csv weights
csvWeightNom = "Weight_CSV"


# pile up weights
pileupWeightNom = "Weight_pu69p2"
pileupWeightUp = "Weight_pu69p2Up"
pileupWeightDown = "Weight_pu69p2Down"

## lepton scale factors
electronSFs = "((N_TightElectrons==1 && N_LooseElectrons==2)*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0]*LooseElectron_IdentificationSF[1]*LooseElectron_ReconstructionSF[1]+(N_TightElectrons==2 && N_LooseElectrons==2)*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0]*Electron_IdentificationSF[1]*Electron_ReconstructionSF[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0]+(N_LooseElectrons==0)*1.)"
muonSFs = "((N_TightMuons==1 && N_LooseMuons==2)*Muon_IdentificationSF[0]*Muon_IsolationSF[0]*LooseMuon_IdentificationSF[1]*LooseMuon_IsolationSF[1]+(N_TightMuons==2 && N_LooseMuons==2)*Muon_IdentificationSF[0]*Muon_IsolationSF[0]*Muon_IdentificationSF[1]*Muon_IsolationSF[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IdentificationSF[0]*Muon_IsolationSF[0]+(N_LooseMuons==0)*1.)"

# top pt weight
topptWeightNom = "Weight_TopPt"

electronSFs_up = "((N_TightElectrons==1 && N_LooseElectrons==2)*Electron_IdentificationSFUp[0]*Electron_ReconstructionSFUp[0]*LooseElectron_IdentificationSFUp[1]*LooseElectron_ReconstructionSFUp[1]+(N_TightElectrons==2 && N_LooseElectrons==2)*Electron_IdentificationSFUp[0]*Electron_ReconstructionSFUp[0]*Electron_IdentificationSFUp[1]*Electron_ReconstructionSFUp[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_IdentificationSFUp[0]*Electron_ReconstructionSFUp[0]+(N_LooseElectrons==0)*1.)"
electronSFs_down = "((N_TightElectrons==1 && N_LooseElectrons==2)*Electron_IdentificationSFDown[0]*Electron_ReconstructionSFDown[0]*LooseElectron_IdentificationSFDown[1]*LooseElectron_ReconstructionSFDown[1]+(N_TightElectrons==2 && N_LooseElectrons==2)*Electron_IdentificationSFDown[0]*Electron_ReconstructionSFDown[0]*Electron_IdentificationSFDown[1]*Electron_ReconstructionSFDown[1]+(N_TightElectrons==1 && N_LooseElectrons==1)*Electron_IdentificationSFDown[0]*Electron_ReconstructionSFDown[0]+(N_LooseElectrons==0)*1.)"
muonSFs_up = "((N_TightMuons==1 && N_LooseMuons==2)*Muon_IdentificationSFUp[0]*Muon_IsolationSFUp[0]*LooseMuon_IdentificationSFUp[1]*LooseMuon_IsolationSFUp[1]+(N_TightMuons==2 && N_LooseMuons==2)*Muon_IdentificationSFUp[0]*Muon_IsolationSFUp[0]*Muon_IdentificationSFUp[1]*Muon_IsolationSFUp[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IdentificationSFUp[0]*Muon_IsolationSFUp[0]+(N_LooseMuons==0)*1.)"
muonSFs_down = "((N_TightMuons==1 && N_LooseMuons==2)*Muon_IdentificationSFDown[0]*Muon_IsolationSFDown[0]*LooseMuon_IdentificationSFDown[1]*LooseMuon_IsolationSFDown[1]+(N_TightMuons==2 && N_LooseMuons==2)*Muon_IdentificationSFDown[0]*Muon_IsolationSFDown[0]*Muon_IdentificationSFDown[1]*Muon_IsolationSFDown[1]+(N_TightMuons==1 && N_LooseMuons==1)*Muon_IdentificationSFDown[0]*Muon_IsolationSFDown[0]+(N_LooseMuons==0)*1.)"

bosonWeightNom = "1."#"internalBosonWeight"

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
    "PUWEIGHTNOM": pileupWeightNom,
    "PUWEIGHTUP": pileupWeightUp,
    "PUWEIGHTDOWN": pileupWeightDown,
    # csv weight
    "CSVWEIGHTNOM": csvWeightNom,
    # top pt weight
    "TOPPTWEIGHTNOM": topptWeightNom,
    # lepton scale factors
    "ELESFNOM": electronSFs,
    "ELESFUP": electronSFs_up,
    "ELESFDOWN": electronSFs_down,
    "MUSFNOM": muonSFs,
    "MUSFUP": muonSFs_up,
    "MUSFDOWN": muonSFs_down,
    "BOSONWEIGHTNOM": bosonWeightNom,
    ## trigger scale factors
    # "TRIGGERSFS": "(" + electronTrigger + "+" + muonTrigger + ")",
    # "ELETRIGSUP": "(" + electronTrigger_up + "+" + muonTrigger + ")",
    # "ELETRIGSDOWN": "(" + electronTrigger_down + "+" + muonTrigger + ")",
    # "MUTRIGSUP": "(" + electronTrigger + "+" + muonTrigger_up + ")",
    # "MUTRIGSDOWN": "(" + electronTrigger + "+" + muonTrigger_down + ")",
    ## do weights for data
    "DOWEIGHTS": "(DoWeights==1)+(DoWeights==0)*1.0",
}

# Lumi weight
lumi = "41.5*"

# nominal weight
nominalweight = (
    "NomWeight:=("
    + defaultWeight
    + "*"
    + pileupWeightNom
    + "*"
    + csvWeightNom
    + "*"
    + topptWeightNom
    + "*"
    + muonSFs
    + "*"
    + electronSFs
    + "*"
    + bosonWeightNom
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
    "(N_LooseElectrons==0) && (N_LooseMuons==0)" ,
    "MET",
    samDict=sampleDict,
    readTrees=doReadTrees,
    ),
    plotClasses.Sample(
    "SingleEl",
    ROOT.kBlack,
    path_mwassmer + "/SingleElectron*/*nominal*.root",
    "N_LooseElectrons>0",
    #"(N_TightElectrons==1) && (N_LooseElectrons==1) && ((Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1) || (Triggered_HLT_Ele32_WPTight_Gsf_vX==1))" ,
    "SingleEl",
    samDict=sampleDict,
    readTrees=doReadTrees,
    ),
    plotClasses.Sample(
    "SingleMu",
    ROOT.kBlack,
    path_mwassmer + "/SingleMuon*/*nominal*.root",
    "N_LooseMuons>0",
    #"(N_TightMuons==1) && (N_LooseMuons==1) && (Triggered_HLT_IsoMu24_vX==1)" ,
    "SingleMu",
    samDict=sampleDict,
    readTrees=doReadTrees,
    ),
]


# print("limit samples")
samples = [
    # signal samples
    plotClasses.Sample(
        "#splitline{VectorMonotop}{M_{#phi}=2000 M_{#chi}=500}",
        ROOT.kCyan,
        path_mwassmer + "/VectorMonotop_Mphi_2000_Mchi_500/*nominal*.root",
        # lumi reweighting factor due to stupid cross section calculation
        lumi + sel_MET,
        "VectorMonotop_Mphi_2000_Mchi_500",
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
        path_mwassmer + "/DYJetsToLL_M-50_HT*/*nominal*.root",
        lumi + sel_MET,
        "zlljets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="bkg",
    ),
    plotClasses.Sample(
        "W(l#nu)+jets",
        ROOT.kOrange,
        path_mwassmer + "/WJetsToLNu_HT*/*nominal*.root",
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
        path_mwassmer + "/??_TuneCP5*/*nominal*.root",
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
