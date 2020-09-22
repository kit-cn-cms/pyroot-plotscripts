import sys
import os
import ROOT
import pandas
import Systematics
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses
import unfolding_setup
# samples
# input path 
path  = "/nfs/dust/cms/group/ttx-kit/ntuples_ttH/2018/"
# separate ttjets samples
path_ttjets = "/nfs/dust/cms/group/ttx-kit/ntuples_ttbb/2018_2tag/"

path_ttbar = path_ttjets+'/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
             path_ttjets+'/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+";"+ \
             path_ttjets+'/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'
             
path_ttbb = path_ttjets+"/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"+";"+ \
            path_ttjets+"/TTbb_4f_TTTo2l2nu_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"+";"+ \
            path_ttjets+"/TTbb_4f_TTToHadronic_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"



VJetsPathS = path+'/DYJets*madgraphMLM*/*nominal*.root'+';'+ \
             path+'/WJets*madgraphMLM*/*nominal*.root'

ttVPathS = path+'/TTW*/*nominal*.root'+';'+ \
           path+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path+'/TTZToQQ*/*nominal*.root'

ttWPath = path+'/TTW*/*nominal*.root'

dibosonPathS = path+'/WW_*/*nominal*.root'+';'+ \
               path+'/WZ_*/*nominal*.root'+';'+ \
               path+'/ZZ_*/*nominal*.root'

stpath = path+'/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/*nominal*.root'+';'+ \
         path+'/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
         path+'/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
         path+'/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
         path+'/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'
stpath = path+"/ST*/*nominal*.root"


ttHpath = path+'/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
	      path+'/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'

ttZpath =  path+'/TTZToQQ*/*nominal*.root'+';'+ \
           path+'/TTZToLLNuNu_M-10*/*nominal*.root'+';'

friendTrees = {
    "genInfo": "/nfs/dust/cms/group/ttx-kit/ntuples_ttbb/friendTrees/addbb/2018_2tag/"
    }

# SELECTIONS
# need to veto muon events in electron dataset to avoid double counting and vice versa
sel_singleel="((N_TightMuons==0 && N_TightElectrons==1) && (Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX || ( Triggered_HLT_Ele32_WPTight_Gsf_vX )))"
sel_singlemu="(N_TightElectrons==0 && N_TightMuons==1 && Triggered_HLT_IsoMu24_vX)"
# jet tag base selection
sel_jettag = "(1.)"#(N_Jets>=4 && N_BTagsM>=3)"

# MET base selection
sel_MET="*(1.)"#Evt_MET_Pt>20.)"
#sel_MET="*1.0"

# select events without huge MuR/MuF weights
sel_StrangeMuWeights="*(1.)"

# ======= # 
# WEIGHTS #
# ======= #
defaultWeight = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2*internalCSVweight*sf__HT_vs_NJet__btag_NOMINAL"

# pile up weights
pileupWeightUp   = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2Up*internalCSVweight*sf__HT_vs_NJet__btag_NOMINAL"
pileupWeightDown = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2Down*internalCSVweight*sf__HT_vs_NJet__btag_NOMINAL"

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

    # murmuf
    "MURUP":            "(Weight_scale_variation_muR_2p0_muF_1p0*internalNormFactors.at(\"Weight_scale_variation_muR_2p0_muF_1p0\"))",
    "MURDOWN":          "(Weight_scale_variation_muR_0p5_muF_1p0*internalNormFactors.at(\"Weight_scale_variation_muR_0p5_muF_1p0\"))",
    "MUFUP":            "(Weight_scale_variation_muR_1p0_muF_2p0*internalNormFactors.at(\"Weight_scale_variation_muR_1p0_muF_2p0\"))",
    "MUFDOWN":          "(Weight_scale_variation_muR_1p0_muF_0p5*internalNormFactors.at(\"Weight_scale_variation_muR_1p0_muF_0p5\"))",

    # isrfsr
    "ISRUP":            "(GenWeight_isr_Def_up*internalNormFactors.at(\"GenWeight_isr_Def_up\"))",
    "ISRDOWN":          "(GenWeight_isr_Def_down*internalNormFactors.at(\"GenWeight_isr_Def_down\"))",
    "FSRUP":            "(GenWeight_fsr_Def_up*internalNormFactors.at(\"GenWeight_fsr_Def_up\"))",
    "FSRDOWN":          "(GenWeight_fsr_Def_down*internalNormFactors.at(\"GenWeight_fsr_Def_down\"))",
    # do weights for data
    "DOWEIGHTS":        "(DoWeights==1)+(DoWeights==0)*1.0",

    }

# Lumi weight
lumi = '59.7'

kfactor_zjets = "*1.23"
kfactor_wjets = "*1.21"
#tHq_XS_scale = "*(0.7927/0.07425)"
#tHW_XS_scale = "*(0.1472/0.01517)"
ttbb_FH_scale = "(17.3853/16.2728)"
ttbb_SL_scale = "(15.7322/15.7286)"
ttbb_DL_scale = "(3.5378/3.8024)"

# DANGERZONE: derived in 2018
ttbb_4FS_scale = "*((N_GenTopLep==0)*"+ttbb_FH_scale+"+(N_GenTopLep==1)*"+ttbb_SL_scale+"+(N_GenTopLep==2)*"+ttbb_DL_scale+")"

# nominal weight
nominalweight="NomWeight:=("+defaultWeight+"*"+"("+electronSFs+"+"+muonSFs+")"+"*"+"("+electronTrigger+"+"+muonTrigger+")"+")*(DoWeights==1)+(DoWeights==0)*1.0"

# even selection for sample splitting
evenSel="*(Evt_Odd==0)*2.0"

sampleDict=plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees=True


# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
    plotClasses.Sample('SingleMu',ROOT.kBlack,
            path+'/SingleMuon*/*nominal*.root',
            sel_singlemu+sel_MET,
            'SingleMu', samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('SingleEl',ROOT.kBlack,
            path+'/EGamma*/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleEl', samDict=sampleDict, readTrees=doReadTrees)
]

samples_ttbb = [
     plotClasses.Sample('t#bar{t}+B',ROOT.kOrange,
             path_ttbb,
             lumi+'*(GenEvt_I_TTPlusBB>=1)'+ttbb_4FS_scale+sel_MET,
             'ttbb',
             samDict=sampleDict, readTrees=doReadTrees),
    ]

extendSystematics = {}

samples_minor_backgrounds = [
    plotClasses.Sample('t',ROOT.kAzure,
            stpath,
            lumi+sel_MET,
            'singlet',
            samDict=sampleDict, readTrees=doReadTrees),

     plotClasses.Sample('t#bar{t}+H',ROOT.kRed,
             ttHpath,
             lumi+sel_MET,
             'ttH',
             samDict=sampleDict, readTrees=doReadTrees),     

    plotClasses.Sample('t#bar{t}+Z',ROOT.kCyan,
            ttZpath,
            lumi+sel_MET,
            'ttZ',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+W',ROOT.kBlue,
             ttWPath,  
             lumi+sel_MET,
             'ttW',
             samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('Z+jets',ROOT.kGreen-3,
            path+'/DYJets*HT*/*nominal*.root',
            lumi+sel_MET+kfactor_zjets,
            'zjets',
            samDict=sampleDict, readTrees=doReadTrees),
 
    plotClasses.Sample('W+jets',ROOT.kGreen-7,
            path+'/WJets*HT*/*nominal*.root',
            lumi+sel_MET+kfactor_wjets,
            'wjets',
            samDict=sampleDict, readTrees=doReadTrees), 

    plotClasses.Sample('VV',ROOT.kViolet,
            dibosonPathS,
            lumi+sel_MET,
            'diboson',
            samDict=sampleDict, readTrees=doReadTrees),
    ]

samples_ttnonbb = [
    # ttbar 5FS default background samples
    plotClasses.Sample('t#bar{t}+jj',ROOT.kOrange+9,
            path_ttbar,
            lumi+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttjj',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kOrange+7,
            path_ttbar,
            lumi+'*(GenEvt_I_TTPlusCC==1)'+sel_MET+sel_StrangeMuWeights,
            'ttcc',
            samDict=sampleDict, readTrees=doReadTrees),
    ]

samples = samples_ttbb
samples += samples_ttnonbb
samples += samples_minor_backgrounds



processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = [p for p in processes if not (p == "ttbb" or p == "ttbb_5FS")]
pseudo_data_samples = [x for x in samples if not p.startswith("ttbb_")]

plottingsamples = [
    plotClasses.Sample("t#bar{t}+X", ROOT.kRed, "", "",
        "ttX", addsamples = ["ttZ","ttW","ttH"],
        samDict = sampleDict, readTrees = doReadTrees),

    plotClasses.Sample("misc.", 18, "", "",
        "vjets", addsamples = ["diboson", "wjets", "zjets"],
        samDict = sampleDict, readTrees = doReadTrees),

    # plotClasses.Sample("misc.", 18, "", "",
    #    "misc", addsamples ["ttZ", "ttW", "wjets", "zjets", "diboson"],
    #    samDict = sampleDict, readTrees = doReadTrees)
     ]

# sort subset of processes in plots. descending order
sortedProcesses = ["ttB", "ttbb", "bkg_ttbb", "ttbj", "tt2b", "ttb", "ttcc", "ttjj", "ttX"]
