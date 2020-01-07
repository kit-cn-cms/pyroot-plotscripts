import sys
import os
import ROOT
import pandas
import Systematics
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses

# samples
# input path 
path  = "/nfs/dust/cms/user/vdlinden/legacyTTH/ntuples/legacy_2018_ttH_newJEC/"

path_ttbarSL = path+'/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'

path_ttbarFH = path+'/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'

path_ttbarDL = path+'/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'

path_ttbbSL = path+"/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"

path_ttbbDL = path+"/TTbb_4f_TTTo2l2nu_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"

path_vjets = path+'/DYJets*/*nominal*.root'+';'+ \
             path+'/WJets*/*nominal*.root'

path_ttW = path+'/TTW*/*nominal*.root'

path_ttZ = path+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path+'/TTZToQQ*/*nominal*.root'

path_ttV = path+'/TTW*/*nominal*.root'+";"+ \
           path+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path+'/TTZToQQ*/*nominal*.root'


path_diboson = path+'/WW_*/*nominal*.root'+';'+ \
               path+'/WZ_*/*nominal*.root'+';'+ \
               path+'/ZZ_*/*nominal*.root'

path_st = path+"/ST*/*nominal*.root"

path_ttH = path+'/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
	      path+'/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'

# SELECTIONS
# HFHadronMatcher
sel_ttbb = "*(GenEvt_TTxId_FromProducer>=52)"
sel_ttbj = "*(GenEvt_TTxId_FromProducer==51)"
sel_ttcc = "*(GenEvt_TTxId_FromProducer>=41&&GenEvt_TTxId_FromProducer<=46)"
sel_ttjj = "*(GenEvt_TTxId_FromProducer<41)"



# need to veto muon events in electron dataset to avoid double counting and vice versa
sel_singleel = "( (N_LooseMuons==0 && N_TightElectrons==1 && N_LooseElectrons==1) && (Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX || ( Triggered_HLT_Ele32_WPTight_Gsf_L1DoubleEG_vX && Triggered_HLT_Ele32_WPTight_Gsf_2017SeedsX )) && ( (TightLepton_Pt[0]>30. && TightLepton_Eta[0]<2.1) || (TightLepton_Pt[0]>34. && TightLepton_Eta[0]>2.1 && TightLepton_Eta[0]<2.4) ) && (TightLepton_Eta[0] < 1.444 || TightLepton_Eta[0] >1.566) )"

sel_singlemu = "( (N_LooseElectrons==0 && N_TightMuons==1 && N_LooseMuons==1) && (Triggered_HLT_IsoMu24_vX) && ( TightLepton_Pt[0]>26. && TightLepton_Eta[0]<2.4 ) )"
# jet tag base selection
sel_jettag = "1."

# MET base selection
sel_MET="*1.0"
#sel_MET="*1.0"

# select events without huge MuR/MuF weights
sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'
sel_StrangeMuWeights="*(1.)"

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
TTbbweightSL="*1.0"#'*35.8038266498504*0.4393'
TTbbweightDL="*1.0"#'*35.8038266498504*0.1062'
TTbbweightFH="*1.0"#'*35.8038266498504*0.4545'

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



samples_splitData = [
    plotClasses.Sample('SingleMuA',ROOT.kBlack,
            path+'/SingleMuon*A/*nominal*.root',
            sel_singlemu+sel_MET,
            'SingleMuA', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleMuB',ROOT.kBlack,
            path+'/SingleMuon*B/*nominal*.root',
            sel_singlemu+sel_MET,
            'SingleMuB', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleMuC',ROOT.kBlack,
            path+'/SingleMuon*C/*nominal*.root',
            sel_singlemu+sel_MET,
            'SingleMuC', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleMuD',ROOT.kBlack,
            path+'/SingleMuon*D/*nominal*.root',
            sel_singlemu+sel_MET,
            'SingleMuD', samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('SingleElA',ROOT.kBlack,
            path+'/EGamma*A/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleElA', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleElB',ROOT.kBlack,
            path+'/EGamma*B/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleElB', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleElC',ROOT.kBlack,
            path+'/EGamma*C/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleElC', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleElD',ROOT.kBlack,
            path+'/EGamma*D/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleElD', samDict=sampleDict, readTrees=doReadTrees),

    ]

#samplesDataControlPlots+=samples_splitData


samples_ttbb_4FS = [
    # ttbb
     plotClasses.Sample('t#bar{t}+b#bar{b} (4FS)',ROOT.kAzure+3,
             path_ttbbSL,
             lumi+TTbbweightSL+sel_ttbb+sel_MET+sel_StrangeMuWeights+"*njet_corr_CSV_tthf",
             'ttbb_4FS_SL',
             samDict=sampleDict, readTrees=doReadTrees),

     plotClasses.Sample('t#bar{t}(DL)+b#bar{b} (4FS)',ROOT.kAzure+3,
             path_ttbbDL,
             lumi+TTbbweightDL+sel_ttbb+sel_MET+sel_StrangeMuWeights+"*njet_corr_CSV_tthf",
             'ttbb_4FS_DL',
             samDict=sampleDict, readTrees=doReadTrees),

    # ttbj 
    plotClasses.Sample('t#bar{t}+bj (4FS)',ROOT.kAzure+9,
             path_ttbbSL,
             lumi+TTbbweightSL+sel_ttbj+sel_MET+sel_StrangeMuWeights+"*njet_corr_CSV_tthf",
             'ttbj_4FS_SL',
             samDict=sampleDict, readTrees=doReadTrees),

     plotClasses.Sample('t#bar{t}(DL)+bj (4FS)',ROOT.kAzure+9,
             path_ttbbDL,
             lumi+TTbbweightDL+sel_ttbj+sel_MET+sel_StrangeMuWeights+"*njet_corr_CSV_tthf",
             'ttbj_4FS_DL',
             samDict=sampleDict, readTrees=doReadTrees),

    ]


samples_ttbb_5FS = [
    #ttbb
    plotClasses.Sample('t#bar{t}+b#bar{b} (5FS)',ROOT.kAzure+3,
            path_ttbarSL,
            lumi+sel_ttbb+sel_MET+sel_StrangeMuWeights+"*njet_corr_CSV_tthf",
            'ttbb_5FS_SL',
            samDict=sampleDict, readTrees=doReadTrees, plot = False), 

    plotClasses.Sample('t#bar{t}(DL)+b#bar{b} (5FS)',ROOT.kTeal,
            path_ttbarDL,
            lumi+sel_ttbb+sel_MET+sel_StrangeMuWeights+"*njet_corr_CSV_tthf",
            'ttbb_5FS_DL',
            samDict=sampleDict, readTrees=doReadTrees, plot = False), 

    # ttbj
    plotClasses.Sample('t#bar{t}(sl)+bj (5FS)',ROOT.kAzure+9,
            path_ttbarSL,
            lumi+sel_ttbj+sel_MET+sel_StrangeMuWeights+"*njet_corr_CSV_tthf",
            'ttbj_5FS_SL',
            samDict=sampleDict, readTrees=doReadTrees, plot = False),

    plotClasses.Sample('t#bar{t}(DL)+bj (5FS)',ROOT.kTeal,
            path_ttbarDL,
            lumi+sel_ttbj+sel_MET+sel_StrangeMuWeights+"*njet_corr_CSV_tthf",
            'ttbj_5FS_DL',
            samDict=sampleDict, readTrees=doReadTrees, plot = False),

    ]


samples_minor_backgrounds = [
    plotClasses.Sample('t',ROOT.kRed-2,
            path_st,
            lumi+sel_MET+"*njet_corr_CSV_others",
            'singlet',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+V',ROOT.kOrange+7,
            path_ttV,
            lumi+sel_MET+"*njet_corr_CSV_others",
            'ttV',
            samDict=sampleDict, readTrees=doReadTrees),

    #plotClasses.Sample('t#bar{t}+Z',ROOT.kOrange+7,
    #        path_ttZ,
    #        lumi+sel_MET,
    #        'ttZ',
    #        samDict=sampleDict, readTrees=doReadTrees),

    #plotClasses.Sample('t#bar{t}+W',ROOT.kOrange-3,
    #         path_ttW,  
    #         lumi+sel_MET,
    #         'ttW',
    #         samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('V+jets',18,
            path_vjets,
            lumi+sel_MET+"*njet_corr_CSV_others",
            'vjets',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('VV',ROOT.kRed+4,
            path_diboson,
            lumi+sel_MET+"*njet_corr_CSV_others",
            'diboson',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+H',ROOT.kRed+1,
            path_ttH,
            lumi+sel_MET+"*njet_corr_CSV_ttH",
            'ttH',
            samDict=sampleDict, readTrees=doReadTrees),     
    ]



samples = [
    plotClasses.Sample('t#bar{t}+jj',ROOT.kAzure-9,
             path_ttbarSL+";"+path_ttbarDL+";"+path_ttbarFH,
             lumi+sel_ttjj+sel_MET+sel_StrangeMuWeights+"*njet_corr_CSV_ttlf",
             'ttjj',
             samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kAzure+8,
             path_ttbarSL+";"+path_ttbarDL+";"+path_ttbarFH,
             lumi+sel_ttcc+sel_MET+sel_StrangeMuWeights+"*njet_corr_CSV_ttcc",
             'ttcc',
             samDict=sampleDict, readTrees=doReadTrees),
    
    #plotClasses.Sample('t#bar{t}(sl)+jj',ROOT.kAzure-9,
    #         path_ttbarSL,
    #         lumi+sel_ttjj+sel_MET+sel_StrangeMuWeights,
    #         'ttjj_SL',
    #         samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    #plotClasses.Sample('t#bar{t}(sl)+c#bar{c}',ROOT.kAzure+8,
    #         path_ttbarSL,
    #         lumi+sel_ttcc+sel_MET+sel_StrangeMuWeights,
    #         'ttcc_SL',
    #         samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    #plotClasses.Sample('t#bar{t} (dilepton)',ROOT.kTeal,
    #         path_ttbarDL,
    #         lumi+sel_MET+sel_StrangeMuWeights,
    #         'ttdl',
    #         samDict=sampleDict, readTrees=doReadTrees),
    ]

samples += samples_minor_backgrounds
samples += samples_ttbb_4FS
samples += samples_ttbb_5FS


processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = processes


plottingsamples = [
#     plotClasses.Sample("t#bar{t}+V", ROOT.kCyan, "", "",
#         "ttV", addsamples = ["ttZ","ttW"],
#         samDict = sampleDict, readTrees = doReadTrees),

#     plotClasses.Sample("V+jets", 18,
#         "vjets", addsamples = ["wjets", "zjets"],
#         samDict = sampleDict, readTrees = doReadTrees)

#    plotClasses.Sample("misc.", 18, "", "",
#        "misc", addsamples ["ttZ", "ttW", "wjets", "zjets", "diboson"],
#        samDict = sampleDict, readTrees = doReadTrees),

#     plotClasses.Sample('t#bar{t}+b#bar{b} (4FS)',ROOT.kAzure+3, "", "",
#             'ttbb_4FS', addsamples = ["ttbb_4FS_DL", "ttbb_4FS_SL"],
#             samDict=sampleDict, readTrees=doReadTrees),

#     plotClasses.Sample('t#bar{t}+bj (4FS)',ROOT.kAzure+9, "", "",
#             'ttbj_4FS', addsamples = ["ttbj_4FS_DL", "ttbj_4FS_SL"],
#             samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample("t#bar{t}+b (DL, 4FS)", ROOT.kTeal, "", "",                                                                
            "ttb_DL_4FS", addsamples = ["ttbb_4FS_DL", "ttbj_4FS_DL"],                                                            
            samDict = sampleDict, readTrees=doReadTrees), 
     ]

# sort subset of processes in plots. descending order
sortedProcesses = ["ttbb_4FS_SL", "ttbj_4FS_SL", "ttjj", "ttcc", "ttbb_4FS_DL", "ttbj_4FS_DL"]
