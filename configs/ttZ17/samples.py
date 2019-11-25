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
path  = "/nfs/dust/cms/user/swieland/ttH_legacy/ntupleHadded_2017"

ttbarPathS = path+'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
             path+'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+";"+\
             path+'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx/*nominal*.root'
             #'TTbb_Powheg_Openloops_new_pmx' needs to be added?

VJetsPathS = path+'/DYJets*/*nominal*.root'+';'+ \
             path+'/WJets*/*nominal*.root'

ttWPath  = path+'/TTW*/*nominal*.root'

ttZPath  = path+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path+'TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8_1/*nominal*.root'

dibosonPathS = path+'/WW_*/*nominal*.root'+';'+ \
               path+'/WZ_*/*nominal*.root'+';'+ \
               path+'/ZZ_*/*nominal*.root'

stpath = path+'/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_new_pmx/*nominal*.root'+';'+ \
         path+'/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8*/*nominal*.root'+';'+ \
         path+'/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx*/*nominal*.root'+';'+ \
         path+'/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8*/*nominal*.root'+';'+ \
         path+'/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_new_pmx*/*nominal*.root'
#STH
THWpath = path+'/THW_*ctcvcp*/*nominal*.root'
THQpath = path+'/THQ_*ctcvcp*/*nominal*.root'


ttHpath = path+'/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
	      path+'/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_new_pmx/*nominal*.root'

	  

# ttZpath =  path+'/TTZToQQ*/*nominal*.root'+';'+ \
        #     path+'/TTZToLLNuNu_M-10*/*nominal*.root'+';'

# SELECTIONS

# need to veto muon events in electron dataset to avoid double counting and vice versa
sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1)"# && (Triggered_HLT_Ele32_WPTight_Gsf_2017SeedsX==1 && Triggered_HLT_Ele32_WPTight_Gsf_L1DoubleEG_vX==1))"
# sel_singlemu="(N_LooseElectrons==0 && N_TightMuons==1 && (Triggered_HLT_IsoMu27_vX==1))"
# sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1)"
sel_singlemu="(N_LooseElectrons==0 && N_TightMuons==1)"
# jet tag base selection
sel_jettag = "(N_Jets>=4 && N_BTagsM>=3)"

# MET base selection
sel_MET="*(Evt_MET_Pt>20.)"
#sel_MET="*1.0"

# select events without huge MuR/MuF weights
sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'


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
lumi = '41.5'
TTbbweight='*35.8038266498504*0.43937838'

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
            sel_singlemu+sel_MET+"*"+sel_jettag,
            'SingleMu', samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('SingleEl',ROOT.kBlack,
            path+'/SingleElectron*/*nominal*.root',
            sel_singleel+sel_MET+"*"+sel_jettag,
            'SingleEl', samDict=sampleDict, readTrees=doReadTrees)
]

samples=[
    # signal samples     
    plotClasses.Sample('t#bar{t}+H',ROOT.kRed+1,
            ttHpath,
            lumi+sel_MET,
            'ttH',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+Z',ROOT.kOrange+7,
            ttZPath,
            lumi+sel_MET+evenSel,
            'ttZ',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    
    #plotClasses.Sample('t#bar{t}H (nonbb)',ROOT.kBlue+1,
    #        ttHpath,
    #        lumi+sel_MET,
    #        'ttH_hnonbb',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    #plotClasses.Sample('t#bar{t}H(cc)',ROOT.kBlue+1,
    #        ttHpath,
    #        lumi+sel_MET+hccSel,
    #        'ttH_hcc',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    #plotClasses.Sample('t#bar{t}H(ll)',ROOT.kBlue+1,
    #        ttHpath,
    #        lumi+sel_MET+httSel,
    #        'ttH_htt',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    #plotClasses.Sample('t#bar{t}H(#gamma#gamma)',ROOT.kBlue+1,
    #        ttHpath,
    #        lumi+sel_MET+hggSel,
    #        'ttH_hgg',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    #plotClasses.Sample('t#bar{t}H(gg)',ROOT.kBlue+1,
    #        ttHpath,
    #        lumi+sel_MET+hglugluSel,
    #        'ttH_hgluglu',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    #plotClasses.Sample('t#bar{t}H(WW)',ROOT.kBlue+1,
    #        ttHpath,
    #        lumi+sel_MET+hwwSel,
    #        'ttH_hww',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    #plotClasses.Sample('t#bar{t}H(ZZ)',ROOT.kBlue+1,
    #        ttHpath,
    #        lumi+sel_MET+hzzSel,
    #        'ttH_hzz',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    #plotClasses.Sample('t#bar{t}H(Z#gamma)',ROOT.kBlue+1,
    #        ttHpath,
    #        lumi+sel_MET+hzgSel,
    #        'ttH_hzg',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    
    #plotClasses.Sample('tHW',ROOT.kOrange+1,
    #        THWpath,
    #        lumi+sel_MET,
    #        'tHW',
    #        samDict=sampleDict, readTrees=doReadTrees),
    
    #plotClasses.Sample('tHq',ROOT.kOrange-9,
    #        THQpath,
    #        lumi+sel_MET,
    #        'tHq',
    #        samDict=sampleDict, readTrees=doReadTrees),

    # background samples
# 
    plotClasses.Sample('t#bar{t}+lf',ROOT.kAzure-9,
            ttbarPathS,
            lumi+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttlf',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kAzure+8,
            ttbarPathS,
            lumi+'*(GenEvt_I_TTPlusCC==1&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttcc',
            samDict=sampleDict, readTrees=doReadTrees),

    #plotClasses.Sample('t#bar{t}+b#bar{b} (5FS)',ROOT.kAzure+3,
    #        ttbarPathS,
    #        lumi+'*(GenEvt_I_TTPlusCC==0)*((GenEvt_I_TTPlusBB==1)||(GenEvt_I_TTPlusBB==2)||(GenEvt_I_TTPlusBB==3))'+sel_MET+sel_StrangeMuWeights,
    #        'ttbb_5FS',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kAzure+3,
            path+"/TTbb_Powheg_Openloops_new_pmx/*nominal*.root",
            lumi+TTbbweight+evenSel+'*(GenEvt_I_TTPlusCC==0)*((GenEvt_I_TTPlusBB==1)||(GenEvt_I_TTPlusBB==2)||(GenEvt_I_TTPlusBB==3))'+sel_MET+sel_StrangeMuWeights,
            'ttbb',
            samDict=sampleDict, readTrees=doReadTrees),
    
    #plotClasses.Sample('t#bar{t}+b#bar{b} (5FS)',ROOT.kRed-1,
    #        ttbarPathS,
    #        lumi+'*((GenEvt_I_TTPlusBB==1)||(GenEvt_I_TTPlusBB==2)||(GenEvt_I_TTPlusBB==3))'+sel_MET+sel_StrangeMuWeights,
    #        'ttbb_5FS',
    #        samDict=sampleDict, readTrees=doReadTrees),

    #plotClasses.Sample('t#bar{t}+b',ROOT.kRed-2,
    #        path+"/TTbb_Powheg_Openloops_new_pmx/*nominal*.root",
    #        lumi+TTbbweight+'*(GenEvt_I_TTPlusBB==1)'+sel_MET+sel_StrangeMuWeights,
    #        'ttb',
    #        samDict=sampleDict, readTrees=doReadTrees),

    #plotClasses.Sample('t#bar{t}+2b',ROOT.kRed+2,
    #        path+"/TTbb_Powheg_Openloops_new_pmx/*nominal*.root",
    #        lumi+TTbbweight+'*(GenEvt_I_TTPlusBB==2)'+sel_MET+sel_StrangeMuWeights,
    #        'tt2b',
    #        samDict=sampleDict, readTrees=doReadTrees),

    #plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kRed-5,
    #        path+"/TTbb_Powheg_Openloops_new_pmx/*nominal*.root",
    #        lumi+TTbbweight+'*(GenEvt_I_TTPlusBB==3)'+sel_MET+sel_StrangeMuWeights,
    #        'ttbb_split',
    #        samDict=sampleDict, readTrees=doReadTrees), 
    
    # minor samples
    plotClasses.Sample('t#bar{t}+W',ROOT.kOrange+5,
            ttWPath,
            lumi+sel_MET,
            'ttW',
            samDict=sampleDict, readTrees=doReadTrees),

    #plotClasses.Sample('t#bar{t}Z(b#bar{b})',ROOT.kCyan,
    #        path+'/TTZToBB*/*nominal*.root',
    #        # lumi reweighting factor due to stupid cross section calculation
    #        lumi+"*1.1017"+evenSel+sel_MET,
    #        'ttZbb',
    #        samDict=sampleDict, readTrees=doReadTrees),

    #plotClasses.Sample('t#bar{t}Z(q#bar{q})',ROOT.kSpring+10,
    #        path+'/TTZToQQ*/*nominal*.root',
    #        lumi+"*1.1348"+evenSel+"*(GenEvt_I_TTZ==0)"+sel_MET,
    #        'ttZqq',
    #        samDict=sampleDict, readTrees=doReadTrees),
    
    #plotClasses.Sample('t#bar[t}Z(ll)', ROOT.kGray,
    #        path+'/TTZToLLNuNu_M-10*/*nominal*.root',
    #        lumi+"*1.0237"+evenSel+sel_MET,
    #        'ttZll',
    #        samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t',ROOT.kRed-2,
            stpath,
            lumi+sel_MET,
            'singlet',
            samDict=sampleDict, readTrees=doReadTrees),
 
    plotClasses.Sample('V+jets',ROOT.kGray,
            VJetsPathS,
            lumi+sel_MET,
            'vjets',
            samDict=sampleDict, readTrees=doReadTrees),
    
    #plotClasses.Sample('Z+jets',ROOT.kGreen-3,
    #        path+'/DYJets*/*nominal*.root',
    #        lumi+evenSel+sel_MET,
    #        'zjets',
    #        samDict=sampleDict, readTrees=doReadTrees),
 
    #plotClasses.Sample('W+jets',ROOT.kGreen-7,
    #        path+'/WJets*/*nominal*.root',
    #        lumi+evenSel+sel_MET,
    #        'wjets',
    #        samDict=sampleDict, readTrees=doReadTrees), 
    
#     plotClasses.Sample('t#bar{t}+W',ROOT.kBlue-10,
#             path+'/TTW*/*nominal*.root',  
#             lumi+evenSel+sel_MET,
#             'ttW',
#             samDict=sampleDict, readTrees=doReadTrees),


    plotClasses.Sample('VV',ROOT.kAzure-7,
            dibosonPathS,
            lumi+sel_MET,
            'diboson',
            samDict=sampleDict, readTrees=doReadTrees),

]

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = processes


plottingsamples = [
#     plotClasses.Sample("t#bar{t}+V", ROOT.kSpring+10,
#         "",
#         lumi+evenSel+sel_MET,
#         "ttV", addsamples = ["ttZ","ttW"],
#         samDict = sampleDict, readTrees = doReadTrees),
    plotClasses.Sample("misc.", 18,
        "", "", "misc", addsamples = ["diboson", "vjets", "ttW"],
        samDict = sampleDict, readTrees = doReadTrees),

    #plotClasses.Sample("V+jets", ROOT.kGreen-3,
    #    VJetsPathS,
    #    lumi+evenSel+sel_MET,
    #    "Vjets", addsamples = ["wjets", "zjets"],
    #    samDict = sampleDict, readTrees = doReadTrees)
    ]

# sort subset of processes in plots. descending order
sortedProcesses = ["ttZ", "ttH", "ttlf", "ttcc", "ttbb", "singlet", "misc"]

