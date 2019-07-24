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

#VJetsPathS = (
    #path_mwassmer
    #+ "/DYJets*/*nominal*.root"
    #+ ";"
    #+ path_mwassmer
    #+ "/WJets*/*nominal*.root"
#)

#ttVPathS = (
    #path_mwassmer
    #+ "/TTW*/*nominal*.root"
    #+ ";"
    #+ path_mwassmer
    #+ "/TTZToLLNuNu*/*nominal*.root"
    #+ ";"
    #+ path_mwassmer
    #+ "/TTZToQQ*/*nominal*.root"
#)

#dibosonPathS = (
    #path_mwassmer
    #+ "/WW_*/*nominal*.root"
    #+ ";"
    #+ path_mwassmer
    #+ "/WZ_*/*nominal*.root"
    #+ ";"
    #+ path_mwassmer
    #+ "/ZZ_*/*nominal*.root"
#)

#stpath = path_mwassmer + "/ST_*/*nominal*.root"

#ttHpath = (
    #path_mwassmer
    #+ "/ttHTobb_M125*/*nominal*.root"
    #+ ";"
    #+ path_mwassmer
    #+ "/ttHToNonbb_M125*/*nominal*.root"
#)

#ttZpath = (
    #path_mwassmer
    #+ "/TTZToQQ*/*nominal*.root"
    #+ ";"
    #+ path_mwassmer
    #+ "/TTZToBB*/*nominal*.root"
    #+ ";"
    #+ path_mwassmer
    #+ "/TTZToLLNuNu_M-10*/*nominal*.root"
    #+ ";"
#)

# SELECTIONS

# need to veto muon events in electron dataset to avoid double counting and vice versa
sel_signal = "*(N_LooseMuons==0 && N_LooseElectrons==0 && N_LoosePhotons==0)"


# select events without huge MuR/MuF weights
# sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'
sel_StrangeMuWeights = "*1.0"


# ======= #
# WEIGHTS #
# ======= #
#defaultWeight = "Weight_GEN_nom*Weight_pu69p2*Weight_CSV"
defaultWeight = "Weight_GEN_nom*Weight_pu69p2"

# pile up weights
#pileupWeightUp = "Weight_GEN_nom*Weight_pu69p2Up*Weight_CSV"
#pileupWeightDown = "Weight_GEN_nom*Weight_pu69p2Down*Weight_CSV"

## lepton scale factors
#electronSFs = "((N_TightElectrons==1)&&(Electron_IdentificationSF[0]>0.)&&(Electron_ReconstructionSF[0]>0.))*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0]"
#muonSFs = "((N_TightMuons==1)&&(Muon_IdentificationSF[0]>0.)&&(Muon_IsolationSF[0]>0.))*Muon_IdentificationSF[0]*Muon_IsolationSF[0]"

#electronSFs_up = "((N_TightElectrons==1)&&(Electron_IdentificationSFUp[0]>0.)&&(Electron_ReconstructionSFUp[0]>0.))*Electron_IdentificationSFUp[0]*Electron_ReconstructionSFUp[0]"
#electronSFs_down = "((N_TightElectrons==1)&&(Electron_IdentificationSFDown[0]>0.)&&(Electron_ReconstructionSFDown[0]>0.))*Electron_IdentificationSFDown[0]*Electron_ReconstructionSFDown[0]"
#muonSFs_up = "((N_TightMuons==1)&&(Muon_IdentificationSFUp[0]>0.)&&(Muon_IsolationSFUp[0]>0.))*Muon_IdentificationSFUp[0]*Muon_IsolationSFUp[0]"
#muonSFs_down = "((N_TightMuons==1)&&(Muon_IdentificationSFDown[0]>0.)&&(Muon_IsolationSFDown[0]>0.))*Muon_IdentificationSFDown[0]*Muon_IsolationSFDown[0]"

## trigger scale factors
## DANGERZONE: ELECTRON TRIGGER NOT ADDED TO NTUPLES YET, USE INTERNAL SFS
## electronTrigger = "("+sel_singleel+"&&(Weight_EleTriggerSF>0.))*Weight_EleTriggerSF"
#electronTrigger = (
    #"(" + sel_singleel + "&&(internalEleTriggerWeight>0.))*internalEleTriggerWeight"
#)
#muonTrigger = "(" + sel_singlemu + "&&(Weight_MuonTriggerSF>0.))*Weight_MuonTriggerSF"

## electronTrigger_up = "("+sel_singleel+"&&(Weight_EleTriggerSF_Up>0.))*Weight_EleTriggerSF_Up"
## electronTrigger_down = "("+sel_singleel+"&&(Weight_EleTriggerSF_Down>0.))*Weight_EleTriggerSF_Down"
#electronTrigger_up = (
    #"(" + sel_singleel + "&&(internalEleTriggerWeightUp>0.))*internalEleTriggerWeightUp"
#)
#electronTrigger_down = (
    #"("
    #+ sel_singleel
    #+ "&&(internalEleTriggerWeightDown>0.))*internalEleTriggerWeightDown"
#)
#muonTrigger_up = (
    #"(" + sel_singlemu + "&&(Weight_MuonTriggerSF_Up>0.))*Weight_MuonTriggerSF_Up"
#)
#muonTrigger_down = (
    #"(" + sel_singlemu + "&&(Weight_MuonTriggerSF_Down>0.))*Weight_MuonTriggerSF_Down"
#)


# dictionary of expressions to replace in systematics csv
weightReplacements = {
    # default weight
    "DEFAULTWEIGHT": defaultWeight,
    # pileup weights
    #"PUWEIGHTUP": pileupWeightUp,
    #"PUWEIGHTDOWN": pileupWeightDown,
    ## lepton scale factors
    #"LEPTONSFS": "(" + electronSFs + "+" + muonSFs + ")",
    #"ELESFUP": "(" + electronSFs_up + "+" + muonSFs + ")",
    #"ELESFDOWN": "(" + electronSFs_down + "+" + muonSFs + ")",
    #"MUSFUP": "(" + electronSFs + "+" + muonSFs_up + ")",
    #"MUSFDOWN": "(" + electronSFs + "+" + muonSFs_down + ")",
    ## trigger scale factors
    #"TRIGGERSFS": "(" + electronTrigger + "+" + muonTrigger + ")",
    #"ELETRIGSUP": "(" + electronTrigger_up + "+" + muonTrigger + ")",
    #"ELETRIGSDOWN": "(" + electronTrigger_down + "+" + muonTrigger + ")",
    #"MUTRIGSUP": "(" + electronTrigger + "+" + muonTrigger_up + ")",
    #"MUTRIGSDOWN": "(" + electronTrigger + "+" + muonTrigger_down + ")",
    ## do weights for data
    #"DOWEIGHTS": "(DoWeights==1)+(DoWeights==0)*1.0",
}

# Lumi weight
lumi = "59.7"

# nominal weight
nominalweight = (
    "NomWeight:=("
    + defaultWeight
    #+ "*"
    + ")"
    #+ electronSFs
    #+ "+"
    #+ muonSFs
    #+ ")"
    #+ "*"
    #+ "("
    #+ electronTrigger
    #+ "+"
    #+ muonTrigger
    #+ ")"
    #+ ")*(DoWeights==1)+(DoWeights==0)*1.0"
)


sampleDict = plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees = True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots = [
    #plotClasses.Sample(
        #"SingleMu",
        #ROOT.kBlack,
        #path_mwassmer + "/SingleMuon*/*nominal*.root",
        #sel_singlemu ,
        #"SingleMu",
        #samDict=sampleDict,
        #readTrees=doReadTrees,
    #),
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
    #plotClasses.Sample(
        #"VectorMonotop_Mphi_2000_Mchi_1500",
        #ROOT.kCyan,
        #path_mwassmer + "ntuples_2018//*nominal*.root",
        ## lumi reweighting factor due to stupid cross section calculation
        #lumi + sel_signal ,
        #"VectorMonotop_Mphi_2000_Mchi_1500",
        #samDict=sampleDict,
        #readTrees=doReadTrees,
        #typ="signal",
    #),
    plotClasses.Sample(
        "t#bar{t}",
        ROOT.kMagenta,
        ttbarPathS,
        lumi + sel_signal ,
        "ttbar",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="signal",
    ),
    # minor samples
    #plotClasses.Sample(
        #"Single Top",
        #ROOT.kMagenta,
        #stpath,
        #lumi + sel_signal ,
        #"singlet",
        #samDict=sampleDict,
        #readTrees=doReadTrees,
    #),
    plotClasses.Sample(
        "Z(#nu#nu)+jets",
        ROOT.kGreen - 3,
        path_mwassmer + "/ZJetsToNuNu_HT*/*nominal*.root",
        lumi + sel_signal ,
        "znunujets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="signal",
    ),
    plotClasses.Sample(
        "W(l#nu)+jets",
        ROOT.kGreen - 7,
        path_mwassmer + "/WJetsToLNu*/*nominal*.root",
        lumi + sel_signal ,
        "wlnujets",
        samDict=sampleDict,
        readTrees=doReadTrees,
        typ="signal",
    ),
    #plotClasses.Sample(
        #"t#bar{t}+W",
        #ROOT.kBlue - 10,
        #path_mwassmer + "/TTW*/*nominal*.root",
        #lumi + sel_signal ,
        #"ttbarW",
        #samDict=sampleDict,
        #readTrees=doReadTrees,
    #),
    #plotClasses.Sample(
        #"Diboson",
        #ROOT.kAzure + 2,
        #dibosonPathS,
        #lumi + sel_signal ,
        #"diboson",
        #samDict=sampleDict,
        #readTrees=doReadTrees,
    #),
]

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes = processes
datacard_processes = processes


plottingsamples = [
    # plotClasses.Sample("t#bar{t}Z", ROOT.kCyan,
    #    ttZpath,
    #    lumi+sel_signal+sel_MET,
    #    "ttZ", addsamples = ["ttZbb", "ttZqq", "ttZll"],
    #    samDict = sampleDict, readTrees = doReadTrees, typ = "signal"),
    #plotClasses.Sample(
        #"V+jets",
        #ROOT.kGreen - 3,
        #VJetsPathS,
        #lumi + sel_signal ,
        #"Vjets",
        #addsamples=["wjets", "zjets"],
        #samDict=sampleDict,
        #readTrees=doReadTrees,
    #)
]
