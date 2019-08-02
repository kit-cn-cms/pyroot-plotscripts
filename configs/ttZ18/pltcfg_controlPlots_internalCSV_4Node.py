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
path_vdlinden  = "/nfs/dust/cms/user/vdlinden/legacyTTH/ntuples/legacy_2018_ttZ_v2"

ttbarPathS = path_vdlinden+'/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
             path_vdlinden+'/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+\
             path_vdlinden+'/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'

VJetsPathS = path_vdlinden+'/DYJets*/*nominal*.root'+';'+ \
             path_vdlinden+'/WJets*/*nominal*.root'

ttVPathS = path_vdlinden+'/TTW*/*nominal*.root'+';'+ \
           path_vdlinden+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path_vdlinden+'/TTZToQQ*/*nominal*.root'

dibosonPathS = path_vdlinden+'/WW_*/*nominal*.root'+';'+ \
               path_vdlinden+'/WZ_*/*nominal*.root'+';'+ \
               path_vdlinden+'/ZZ_*/*nominal*.root'

stpath = path_vdlinden+'/ST_*/*nominal*.root'

ttHpath = path_vdlinden+'/ttHTobb_M125*/*nominal*.root'+';'+ \
	  path_vdlinden+'/ttHToNonbb_M125*/*nominal*.root'

ttZpath =  path_vdlinden+'/TTZToQQ*/*nominal*.root'+';'+ \
            path_vdlinden+'/TTZToBB*/*nominal*.root'+';'+ \
            path_vdlinden+'/TTZToLLNuNu_M-10*/*nominal*.root'+';'

# SELECTIONS

# need to veto muon events in electron dataset to avoid double counting and vice versa
sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1 && (Triggered_HLT_Ele32_WPTight_Gsf_vX==1))"
sel_singlemu="(N_LooseElectrons==0 && N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1))"

# jet tag base selection
sel_jettag = "(N_Jets>=4 && N_BTagsM>=3)"

# MET base selection
sel_MET="*(Evt_MET_Pt>20.)"
#sel_MET="*1.0"

# select events without huge MuR/MuF weights
#sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'
sel_StrangeMuWeights ="*1.0"


# higgs decay selections
# hcc is uu dd ss cc with ids 1 2 3 4
hccSel='*((abs(GenHiggs_DecProd1_PDGID)==1 && abs(GenHiggs_DecProd2_PDGID)==1) || (abs(GenHiggs_DecProd1_PDGID)==2 && abs(GenHiggs_DecProd2_PDGID)==2) || (abs(GenHiggs_DecProd1_PDGID)==3 && abs(GenHiggs_DecProd2_PDGID)==3) || (abs(GenHiggs_DecProd1_PDGID)==4 && abs(GenHiggs_DecProd2_PDGID)==4) )'
# htt is mumu tautau with ids 13 15
httSel='*((abs(GenHiggs_DecProd1_PDGID)==13 && abs(GenHiggs_DecProd2_PDGID)==13) || (abs(GenHiggs_DecProd1_PDGID)==15 && abs(GenHiggs_DecProd2_PDGID)==15))'
# hgg is gammagamma with id 22
hggSel='*((abs(GenHiggs_DecProd1_PDGID)==22 && abs(GenHiggs_DecProd2_PDGID)==22))'
# hgluglu with id 21
hglugluSel='*((abs(GenHiggs_DecProd1_PDGID)==21 && abs(GenHiggs_DecProd2_PDGID)==21))'
# hww with id 24
hwwSel='*((abs(GenHiggs_DecProd1_PDGID)==24 && abs(GenHiggs_DecProd2_PDGID)==24))'
# hzz with id 23
hzzSel='*((abs(GenHiggs_DecProd1_PDGID)==23 && abs(GenHiggs_DecProd2_PDGID)==23))'
# hzg with id 23 and id 22
hzgSel='*((abs(GenHiggs_DecProd1_PDGID)==23 && abs(GenHiggs_DecProd2_PDGID)==22) || (abs(GenHiggs_DecProd1_PDGID)==22 && abs(GenHiggs_DecProd2_PDGID)==23))'


# ======= # 
# WEIGHTS #
# ======= #
defaultWeight = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2*internalCSVweight"

# pile up weights
pileupWeightUp   = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2Up*internalCSVweight"
pileupWeightDown = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2Down*internalCSVweight"

# lepton scale factors
electronSFs = "((N_TightElectrons==1)&&(Electron_IdentificationSF[0]>0.)&&(Electron_ReconstructionSF[0]>0.))*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0]"
muonSFs     = "((N_TightMuons==1)&&(Muon_IdentificationSF[0]>0.)&&(Muon_IsolationSF[0]>0.))*Muon_IdentificationSF[0]*Muon_IsolationSF[0]"

electronSFs_up      = "((N_TightElectrons==1)&&(Electron_IdentificationSFUp[0]>0.)&&(Electron_ReconstructionSFUp[0]>0.))*Electron_IdentificationSFUp[0]*Electron_ReconstructionSFUp[0]"
electronSFs_down    = "((N_TightElectrons==1)&&(Electron_IdentificationSFDown[0]>0.)&&(Electron_ReconstructionSFDown[0]>0.))*Electron_IdentificationSFDown[0]*Electron_ReconstructionSFDown[0]"
muonSFs_up          = "((N_TightMuons==1)&&(Muon_IdentificationSFUp[0]>0.)&&(Muon_IsolationSFUp[0]>0.))*Muon_IdentificationSFUp[0]*Muon_IsolationSFUp[0]"
muonSFs_down        = "((N_TightMuons==1)&&(Muon_IdentificationSFDown[0]>0.)&&(Muon_IsolationSFDown[0]>0.))*Muon_IdentificationSFDown[0]*Muon_IsolationSFDown[0]"

# trigger scale factors
# DANGERZONE: ELECTRON TRIGGER NOT ADDED TO NTUPLES YET, USE INTERNAL SFS
#electronTrigger = "("+sel_singleel+"&&(Weight_EleTriggerSF>0.))*Weight_EleTriggerSF"
electronTrigger = "("+sel_singleel+"&&(internalEleTriggerWeight>0.))*internalEleTriggerWeight"
muonTrigger = "("+sel_singlemu+"&&(Weight_MuonTriggerSF>0.))*Weight_MuonTriggerSF"

#electronTrigger_up = "("+sel_singleel+"&&(Weight_EleTriggerSF_Up>0.))*Weight_EleTriggerSF_Up"
#electronTrigger_down = "("+sel_singleel+"&&(Weight_EleTriggerSF_Down>0.))*Weight_EleTriggerSF_Down"
electronTrigger_up = "("+sel_singleel+"&&(internalEleTriggerWeightUp>0.))*internalEleTriggerWeightUp"
electronTrigger_down = "("+sel_singleel+"&&(internalEleTriggerWeightDown>0.))*internalEleTriggerWeightDown"
muonTrigger_up = "("+sel_singlemu+"&&(Weight_MuonTriggerSF_Up>0.))*Weight_MuonTriggerSF_Up"
muonTrigger_down = "("+sel_singlemu+"&&(Weight_MuonTriggerSF_Down>0.))*Weight_MuonTriggerSF_Down"


# dictionary of expressions to replace in systematics csv
weightReplacements = {
    # default weight
    "DEFAULTWEIGHT":    defaultWeight,

    # pileup weights
    "PUWEIGHTUP":       pileupWeightUp,
    "PUWEIGHTDOWN":     pileupWeightDown,

    # lepton scale factors
    "LEPTONSFS":        "("+electronSFs+"+"+muonSFs+")",
    "ELESFUP":          "("+electronSFs_up+"+"+muonSFs+")",
    "ELESFDOWN":        "("+electronSFs_down+"+"+muonSFs+")",
    "MUSFUP":           "("+electronSFs+"+"+muonSFs_up+")",
    "MUSFDOWN":         "("+electronSFs+"+"+muonSFs_down+")",

    # trigger scale factors
    "TRIGGERSFS":       "("+electronTrigger+"+"+muonTrigger+")",
    "ELETRIGSUP":       "("+electronTrigger_up+"+"+muonTrigger+")",
    "ELETRIGSDOWN":     "("+electronTrigger_down+"+"+muonTrigger+")",
    "MUTRIGSUP":        "("+electronTrigger+"+"+muonTrigger_up+")",
    "MUTRIGSDOWN":      "("+electronTrigger+"+"+muonTrigger_down+")",

    # do weights for data
    "DOWEIGHTS":        "(DoWeights==1)+(DoWeights==0)*1.0",

    }

# Lumi weight
lumi = '59.7'

# nominal weight
nominalweight="NomWeight:=("+defaultWeight+"*"+"("+electronSFs+"+"+muonSFs+")"+"*"+"("+electronTrigger+"+"+muonTrigger+")"+")*(DoWeights==1)+(DoWeights==0)*1.0"

# even selection for sample splitting
evenSel="*1.0"

sampleDict=plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees=True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
    plotClasses.Sample('SingleMu',ROOT.kBlack,
            path_vdlinden+'/SingleMuon*/*nominal*.root',
            sel_singlemu+sel_MET,
            'SingleMu', samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('SingleEl',ROOT.kBlack,
            path_vdlinden+'/EGamma*/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleEl', samDict=sampleDict, readTrees=doReadTrees)
]

print "samples"

#print "limit samples"
samples = [
    # signal samples     
    plotClasses.Sample('t#bar{t}Z(b#bar{b})',ROOT.kOrange+7,
            path_vdlinden+'/TTZToBB*/*nominal*.root',
            # lumi reweighting factor due to stupid cross section calculation
            lumi+"*1.087"+evenSel+sel_MET,
            'ttZbb',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}Z(q#bar{q})',ROOT.kOrange+7,
            path_vdlinden+'/TTZToQQ*/*nominal*.root',
            lumi+evenSel+"*(GenEvt_I_TTZ==0)"+sel_MET,
            'ttZqq',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}Z(ll)', ROOT.kOrange+7,
            path_vdlinden+'/TTZToLLNuNu_M-10*/*nominal*.root',
            lumi+"*1.006"+evenSel+sel_MET,
            'ttZll',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    # background samples

    plotClasses.Sample('t#bar{t}+lf',ROOT.kAzure-9,
            ttbarPathS,
            lumi+evenSel+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttlf',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kAzure+9,
            ttbarPathS,
            lumi+evenSel+'*(GenEvt_I_TTPlusCC==1)'+sel_MET+sel_StrangeMuWeights,
            'ttcc',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+b',ROOT.kAzure+8,
            ttbarPathS,
            lumi+evenSel+'*(GenEvt_I_TTPlusBB==1)'+sel_MET+sel_StrangeMuWeights,
            'ttb',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+2b',ROOT.kAzure+3,
            ttbarPathS,
            lumi+evenSel+'*(GenEvt_I_TTPlusBB==2)'+sel_MET+sel_StrangeMuWeights,
            'tt2b',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kAzure+4,
            ttbarPathS,
            lumi+evenSel+'*(GenEvt_I_TTPlusBB==3)'+sel_MET+sel_StrangeMuWeights,
            'ttbb',
            samDict=sampleDict, readTrees=doReadTrees),

    # minor samples

    plotClasses.Sample('Single Top',ROOT.kRed-2,
            stpath,
            lumi+evenSel+sel_MET,
            'singlet',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('Z+jets',ROOT.kGreen-3,
            path_vdlinden+'/DYJets*/*nominal*.root',
            lumi+evenSel+sel_MET,
            'zjets',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('W+jets',ROOT.kGreen-7,
            path_vdlinden+'/WJets*/*nominal*.root',
            lumi+evenSel+sel_MET,
            'wjets',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+W',ROOT.kBlue-10,
            path_vdlinden+'/TTW*/*nominal*.root',
            lumi+evenSel+sel_MET,
            'ttW',
            samDict=sampleDict, readTrees=doReadTrees),


    plotClasses.Sample('Diboson',ROOT.kAzure+2,
            dibosonPathS,
            lumi+evenSel+sel_MET,
            'diboson',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}H',ROOT.kRed+1,
            ttHpath,
            lumi+evenSel+sel_MET,
            'ttH',
            samDict=sampleDict, readTrees=doReadTrees),
]

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = processes

plottingsamples = [
    plotClasses.Sample("t#bar{t}Z", ROOT.kOrange+7,
        ttZpath,
        lumi+evenSel+sel_MET,
        "ttZ", addsamples = ["ttZbb", "ttZqq", "ttZll"],
        samDict = sampleDict, readTrees = doReadTrees, typ = "signal"),

    plotClasses.Sample("misc.", ROOT.kGray,
        "", "", "misc", addsamples = ["wjets", "zjets", "diboson", "ttW"],
        samDict = sampleDict, readTrees = doReadTrees)
    ]

# sort subset of processes in plots. descending order
sortedProcesses = ["ttlf", "ttcc", "ttb", "tt2b", "ttbb", "singlet", "ttH", "misc"]

