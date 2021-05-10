import sys
import os
import ROOT
import pandas
import Systematics
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses
import generate_phasespace_corrections

# samples
# input path 
path  = "/nfs/dust/cms/group/ttx-kit/ntuples_ttH/2016/"

ttbarPathS = path+'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
             path+'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
             path+'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'

path_ttbb = path+"/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"+';'+ \
            path+"/TTbb_4f_TTTo2l2nu_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"+';'+ \
            path+"/TTbb_4f_TTToHadronic_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"

path_ttbbSL = path+"/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"
path_ttbbDL = path+"/TTbb_4f_TTTo2l2nu_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"

VJetsPathS = path+'/DYJets*madgraph*/*nominal*.root'+';'+ \
             path+'/WJets*madgraph*/*nominal*.root'

ttVPathS = path+'/TTW*/*nominal*.root'+';'+ \
           path+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path+'/TTZToQQ*/*nominal*.root'

ttWPath = path+'/TTW*/*nominal*.root'
ttZPathS = path+'/TTZ*/*nominal*.root'

dibosonPathS = path+'/WW_*/*nominal*.root'+';'+ \
               path+'/WZ_*/*nominal*.root'+';'+ \
               path+'/ZZ_*/*nominal*.root'

stpath = path+'/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/*nominal*.root'+';'+ \
         path+'/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
         path+'/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
         path+'/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
         path+'/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'
stpath = path+"/ST*/*nominal*.root"

#STH
THWpath = path+'/THW_*ctcvcp*/*nominal*.root'
THQpath = path+'/THQ_*ctcvcp*/*nominal*.root'

ttHpath = path+'/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
	      path+'/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'

ttZpath =  path+'/TTZToQQ*/*nominal*.root'+';'+ \
           path+'/TTZToLLNuNu_M-10*/*nominal*.root'+';'

friendTrees = {
    "MEMDB": "/nfs/dust/cms/group/ttx-kit/Friends_MEM_ttH_fixed/2016/",
    "cpWeights":    "/nfs/dust/cms/group/ttx-kit/friendTrees_tHWeights/2016_new/",
    }
# SELECTIONS

# need to veto muon events in electron dataset to avoid double counting and vice versa
sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1 && Triggered_HLT_Ele27_WPTight_Gsf_vX)"
sel_singlemu="((N_LooseElectrons==0 && N_TightMuons==1) && (Triggered_HLT_IsoMu24_vX || Triggered_HLT_IsoTkMu24_vX))"
# jet tag base selection
sel_jettag = "(N_Jets>=4 && N_BTagsM>=3)"

# MET base selection
sel_MET="*(Evt_MET_Pt>20.)"
#sel_MET="*1.0"

# select events without huge MuR/MuF weights
sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'


# higgs decay selections
# hbb is gammagamma with id 5
hbbSel='*((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5))'
nonhbbSel='*!((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5))'
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
defaultWeight = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2*internalCSVweight*sf__HT_vs_NJet__btag_NOMINAL*Weight_L1ECALPrefire"

# pile up weights
pileupWeightUp   = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2Up*internalCSVweight*sf__HT_vs_NJet__btag_NOMINAL*Weight_L1ECALPrefire"
pileupWeightDown = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2Down*internalCSVweight*sf__HT_vs_NJet__btag_NOMINAL*Weight_L1ECALPrefire"

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
weightReplacements.update(generate_phasespace_corrections.main())

# Lumi weight
lumi = '36.33'

#tHq_XS_scale = "*(0.7927/0.07425)"
#tHW_XS_scale = "*(0.1472/0.01517)"

# DANGERZONE: derived in 2018
# ttbb_4FS_scale = "*(1.2143)"
ttbb_4FS_scale = "*(1.0)"
ttbb_5FS_scale = "*(1.0)"

# nominal weight
nominalweight="NomWeight:=("+defaultWeight+"*"+"("+electronSFs+"+"+muonSFs+")"+"*"+"("+electronTrigger+"+"+muonTrigger+")"+")*(DoWeights==1)+(DoWeights==0)*1.0"

# even selection for sample splitting
evenSel="*(Evt_Odd==0)*2.0"

sampleDict=plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees=True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
]

h_decays= {
    "hbb": hbbSel,
    "hcc": hccSel,
    "htt": httSel,
    "hgg": hggSel,
    "hgluglu": hglugluSel,
    "hww": hwwSel,
    "hzz": hzzSel,
    "hzg": hzgSel
}


samples = []


for dec in h_decays:
    samples += [
    plotClasses.Sample('tHW ('+dec+')',ROOT.kBlue+3,
            THWpath,
            lumi+sel_MET+h_decays[dec],
            'tHW_'+dec,
            samDict=sampleDict, readTrees=doReadTrees, typ = "bkg"),

    plotClasses.Sample('tHq ('+dec+')',ROOT.kBlue+3,
            THQpath,
            lumi+sel_MET+h_decays[dec],
            'tHq_'+dec,
            samDict=sampleDict, readTrees=doReadTrees, typ = "bkg"),
    ]


processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = [p for p in processes if not p == "ttbb_5FS"]
pseudo_data_samples = [x for x in samples if not x.nick == "ttbb_5FS" and not x.typ == "signal"]


plottingsamples = [
     ]

# sort subset of processes in plots. descending order
sortedProcesses = []

