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
path  = "/nfs/dust/cms/user/vdlinden/legacyTTH/ntuples/nobtags/2017/"
Datapath  = "/nfs/dust/cms/user/swieland/ttH_legacy/ntupleHadded_2017_JECgroups/"

#ttbarPathS = path+'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'
ttbarPathS = path+'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
             path+'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+\
             path+'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx/*nominal*.root'

VJetsPathS = path+'/DYJets*/*nominal*.root'+';'+ \
             path+'/WJets*/*nominal*.root'


path_ttbb = path+"/TTbb_Powheg_Openloops_new_pmx/*nominal*.root"+';'+ \
            path+"/TTbb_Powheg_Openloops_DL/*nominal*.root"+";"+ \
            path+"/TTbb_4f_TTToHadronic_TuneCP5-Powheg-Openloops-Pythia8/*nominal*.root"

path_ttbbSL = path+"/TTbb_Powheg_Openloops_new_pmx/*nominal*.root"
path_ttbbDL = path+"/TTbb_Powheg_Openloops_DL/*nominal*.root"

ttVPathS = path+'/TTW*/*nominal*.root'+';'+ \
           path+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path+'/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/*nominal*.root'


ttZPathS = path+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path+'/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/*nominal*.root'

ttWPath = path+'/TTW*/*nominal*.root'

dibosonPathS = path+'/WW_*/*nominal*.root'+';'+ \
               path+'/WZ_*/*nominal*.root'+';'+ \
               path+'/ZZ_*/*nominal*.root'

stpath = path+'/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_new_pmx/*nominal*.root'+';'+ \
         path+'/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8*/*nominal*.root'+';'+ \
         path+'/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx*/*nominal*.root'+';'+ \
         path+'/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8*/*nominal*.root'+';'+ \
         path+'/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_new_pmx*/*nominal*.root'
#stpath = path+"/ST*/*nominal*.root"

#STH
THWpath = path+'/THW_*ctcvcp*/*nominal*.root'
THQpath = path+'/THQ_*ctcvcp*/*nominal*.root'


ttHpath = path+'/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8*/*nominal*.root'+';'+ \
	      path+'/ttHToNonbb_M125*/*nominal*.root'

# SELECTIONS

# need to veto muon events in electron dataset to avoid double counting and vice versa
#sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1)"# && (Triggered_HLT_Ele32_WPTight_Gsf_2017SeedsX==1 && Triggered_HLT_Ele32_WPTight_Gsf_L1DoubleEG_vX==1))"
sel_singleel="((N_LooseMuons==0 && N_TightElectrons==1) && (Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX || ( Triggered_HLT_Ele32_WPTight_Gsf_L1DoubleEG_vX && Triggered_HLT_Ele32_WPTight_Gsf_2017SeedsX )))"
sel_singlemu="(N_LooseElectrons==0 && N_TightMuons==1 && (Triggered_HLT_IsoMu27_vX))"
# jet tag base selection
sel_jettag = "(N_Jets>=4)"

# MET base selection
sel_MET="*(Evt_MET_Pt>20)"
#sel_MET="*1.0"

# select events without huge MuR/MuF weights
sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'


# higgs decay selections
# hbb is gammagamma with id 5
hbbSel='*((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5))'
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
defaultWeight = sel_jettag+"*Weight_GEN_nom"

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
    "PILEUPWEIGHT":     "Weight_pu69p2",
    "PUWEIGHTUP":       pileupWeightUp,
    "PUWEIGHTDOWN":     pileupWeightDown,

    # lepton scale factors
    "ELECTRONSF":       "({})".format(electronSFs),
    "MUONSF":           "({})".format(muonSFs),
    "LEPTONSFS":        "("+electronSFs+"+"+muonSFs+")",
    "ELESFUP":          "("+electronSFs_up+"+"+muonSFs+")",
    "ELESFDOWN":        "("+electronSFs_down+"+"+muonSFs+")",
    "MUSFUP":           "("+electronSFs+"+"+muonSFs_up+")",
    "MUSFDOWN":         "("+electronSFs+"+"+muonSFs_down+")",

    # trigger scale factors
    "ELECTRONTRIGSFS": "({})".format(electronTrigger),
    "MUONTRIGSFS":   "({})".format(muonTrigger),
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

# DANGERZONE: derived in January 2020
ttbb_4FS_scale = "*(1.0)"
ttbb_5FS_scale = "*(1.0)"

#tHq_XS_scale = "*(0.7927/0.07425)"
#tHW_XS_scale = "*(0.1472/0.01517)"

tH_SM_rwgt = "*(Weight_rwgt_12/Weight_GEN_nom)"
tH_5_rwgt = "*(Weight_rwgt_5/Weight_GEN_nom)"

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
            Datapath+'/SingleMuon*/*nominal*.root',
            sel_singlemu+sel_MET,
            'SingleMu', samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('SingleEl',ROOT.kBlack,
            Datapath+'/SingleElectron*/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleEl', samDict=sampleDict, readTrees=doReadTrees)
]



samples_splitData = [
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
    plotClasses.Sample('SingleMuE',ROOT.kBlack,
            path+'/SingleMuon*E/*nominal*.root',
            sel_singlemu+sel_MET,
            'SingleMuE', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleMuF',ROOT.kBlack,
            path+'/SingleMuon*F/*nominal*.root',
            sel_singlemu+sel_MET,
            'SingleMuF', samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('SingleElB',ROOT.kBlack,
            path+'/SingleElectron*B/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleElB', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleElC',ROOT.kBlack,
            path+'/SingleElectron*C/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleElC', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleElD',ROOT.kBlack,
            path+'/SingleElectron*D/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleElD', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleElE',ROOT.kBlack,
            path+'/SingleElectron*E/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleElE', samDict=sampleDict, readTrees=doReadTrees),
    plotClasses.Sample('SingleElF',ROOT.kBlack,
            path+'/SingleElectron*F/*nominal*.root',
            sel_singleel+sel_MET,
            'SingleElF', samDict=sampleDict, readTrees=doReadTrees),
    ]

# samplesDataControlPlots+=samples_splitData

samples_ttH_decay = [
    plotClasses.Sample('t#bar{t}H (bb)',ROOT.kBlue+1,
            ttHpath,
            lumi+sel_MET+hbbSel,
            'ttH_hbb',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),     
    #plotClasses.Sample('t#bar{t}H (nonbb)',ROOT.kBlue+1,
    #         ttHpath,
    #         lumi+sel_MET,
    #         'ttH',
    #         samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    plotClasses.Sample('t#bar{t}H(cc)',ROOT.kBlue+1,
            ttHpath,
            lumi+sel_MET+hccSel,
            'ttH_hcc',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    plotClasses.Sample('t#bar{t}H(ll)',ROOT.kBlue+1,
            ttHpath,
            lumi+sel_MET+httSel,
            'ttH_htt',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    plotClasses.Sample('t#bar{t}H(#gamma#gamma)',ROOT.kBlue+1,
            ttHpath,
            lumi+sel_MET+hggSel,
            'ttH_hgg',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    plotClasses.Sample('t#bar{t}H(gg)',ROOT.kBlue+1,
            ttHpath,
            lumi+sel_MET+hglugluSel,
            'ttH_hgluglu',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    plotClasses.Sample('t#bar{t}H(WW)',ROOT.kBlue+1,
            ttHpath,
            lumi+sel_MET+hwwSel,
            'ttH_hww',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    plotClasses.Sample('t#bar{t}H(ZZ)',ROOT.kBlue+1,
            ttHpath,
            lumi+sel_MET+hzzSel,
            'ttH_hzz',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    plotClasses.Sample('t#bar{t}H(Z#gamma)',ROOT.kBlue+1,
            ttHpath,
            lumi+sel_MET+hzgSel,
            'ttH_hzg',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    ]



samples_tH = [
    # ITC case
    #plotClasses.Sample('tHW (ITC)',ROOT.kBlue+3,
    #        THWpath,
    #        lumi+tHW_XS_scale+sel_MET,
    #        'tHW_ITC',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = False),

    #plotClasses.Sample('tHq (ITC)',ROOT.kBlue+6,
    #        THQpath,
    #        lumi+tHq_XS_scale+sel_MET,
    #        'tHQ_ITC',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = False),

    # SM case
    plotClasses.Sample('tHW (SM)',ROOT.kBlue+3,
            THWpath,
            lumi+tH_SM_rwgt+sel_MET,
            'tHW_hbb',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('tHq (SM)',ROOT.kBlue+6,
            THQpath,
            lumi+tH_SM_rwgt+sel_MET,
            'tHq_hbb',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    # point 5
    #plotClasses.Sample('tHW (5)',ROOT.kBlue+3,
    #        THWpath,
    #        lumi+tHW_XS_scale+tH_5_rwgt+sel_MET,
    #        'tHW_5',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = False),

    #plotClasses.Sample('tHq (5)',ROOT.kBlue+6,
    #        THQpath,
    #        lumi+tHq_XS_scale+tH_5_rwgt+sel_MET,
    #        'tHQ_5',
    #        samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = False),


    ]




samples_ttbb_4FS = [
     plotClasses.Sample('t#bar{t}+b#bar{b} (4FS)',ROOT.kRed+3,
             path_ttbb,
             lumi+evenSel+ttbb_4FS_scale+'*((GenEvt_I_TTPlusBB==1)||(GenEvt_I_TTPlusBB==2)||(GenEvt_I_TTPlusBB==3))'+sel_MET+sel_StrangeMuWeights,
             'ttbb',
             samDict=sampleDict, readTrees=doReadTrees),
    ]



samples_ttbar_hf_spilt = [
     plotClasses.Sample('t#bar{t}+b',ROOT.kRed-2,
             ttbarPathS,
             lumi+evenSel+'*(GenEvt_I_TTPlusBB==1)'+sel_MET+sel_StrangeMuWeights,
             'ttbarPlusB',
             samDict=sampleDict, readTrees=doReadTrees),

     plotClasses.Sample('t#bar{t}+2b',ROOT.kRed+2,
             ttbarPathS,
             lumi+evenSel+'*(GenEvt_I_TTPlusBB==2)'+sel_MET+sel_StrangeMuWeights,
             'ttbarPlus2B',
             samDict=sampleDict, readTrees=doReadTrees),

     plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,
             ttbarPathS,
             lumi+evenSel+'*(GenEvt_I_TTPlusBB==3)'+sel_MET+sel_StrangeMuWeights,
             'ttbarPlusBBbar',
             samDict=sampleDict, readTrees=doReadTrees), 
    ]


samples_minor_backgrounds = [
    plotClasses.Sample('t',ROOT.kMagenta,
            stpath,
            lumi+sel_MET,
            'singlet',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+Z',ROOT.kCyan,
           ttZPathS,
           lumi+sel_MET,
           'ttbarZ',
           samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+W',ROOT.kBlue-10,
            ttWPath,  
            lumi+sel_MET,
            'ttbarW',
            samDict=sampleDict, readTrees=doReadTrees),

#     plotClasses.Sample('t#bar{t}+V',ROOT.kCyan,
        #     ttVPathS,
        #     lumi+sel_MET,
        #     'ttV',
        #     samDict=sampleDict, readTrees=doReadTrees),
 
    plotClasses.Sample('Z+jets',ROOT.kGreen-3,
           path+'/DYJets*/*nominal*.root',
           lumi+sel_MET,
           'zjets',
           samDict=sampleDict, readTrees=doReadTrees),
 
    plotClasses.Sample('W+jets',ROOT.kGreen-7,
           path+'/WJets*/*nominal*.root',
           lumi+sel_MET,
           'wjets',
           samDict=sampleDict, readTrees=doReadTrees), 

    #plotClasses.Sample('V+jets',18,
    #        VJetsPathS
    #        lumi+sel_MET,
    #        'vjets',
    #        samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('VV',ROOT.kAzure+2,
            dibosonPathS,
            lumi+sel_MET,
            'diboson',
            samDict=sampleDict, readTrees=doReadTrees),
    ]


samples_5FS = [
    plotClasses.Sample('t#bar{t}+b#bar{b} (5FS)',ROOT.kRed+3,
            ttbarPathS,
            lumi+'*((GenEvt_I_TTPlusBB==1)||(GenEvt_I_TTPlusBB==2)||(GenEvt_I_TTPlusBB==3))'+sel_MET+sel_StrangeMuWeights,
            'ttbb_5FS',
            samDict=sampleDict, readTrees=doReadTrees, plot = False), 
    ]

samples = [
#      signal samples
    plotClasses.Sample('t#bar{t}+H',ROOT.kBlue+1,
            ttHpath,
            lumi+sel_MET,
            'ttH',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),     

    # ttbar 5FS default background samples
    plotClasses.Sample('t#bar{t}+lf',ROOT.kRed-7,
            ttbarPathS,
            lumi+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttlf',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,
            ttbarPathS,
            lumi+'*(GenEvt_I_TTPlusCC==1)'+sel_MET+sel_StrangeMuWeights,
            'ttcc',
            samDict=sampleDict, readTrees=doReadTrees),
    ]


# samples += samples_tH
samples += samples_ttbb_4FS
# samples += samples_minor_backgrounds
samples += samples_5FS
#samples += samples_ttbar_hf_spilt
# samples += samples_ttH_decay



processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = [p for p in processes if not p == "ttbb_5FS"]


plottingsamples = [
    plotClasses.Sample("t#bar{t}+V", ROOT.kCyan, "", "",
        "ttV", addsamples = ["ttbarZ","ttbarW"],
        samDict = sampleDict, readTrees = doReadTrees),

    plotClasses.Sample("V+jets", 18, "", "",
        "vjets", addsamples = ["wjets", "zjets"],
        samDict = sampleDict, readTrees = doReadTrees)

#    plotClasses.Sample("misc.", 18, "", "",
#        "misc", addsamples ["ttbarZ", "ttbarW", "wjets", "zjets", "diboson"],
#        samDict = sampleDict, readTrees = doReadTrees)
     ]

# sort subset of processes in plots. descending order
sortedProcesses = ["ttlf", "ttcc", "ttbb", "ttbb_5FS", "ttbb_4FS"]
