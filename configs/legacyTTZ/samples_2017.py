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
path  = "/nfs/dust/cms/user/vdlinden/legacyTTZ/ntuples/2017"

ttbarPathS = path+'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
             path+'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+";"+\
             path+'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx/*nominal*.root'
             #'TTbb_Powheg_Openloops_new_pmx' needs to be added?

VJetsPathS = path+'/DYJets*/*nominal*.root'+';'+ \
             path+'/WJets*/*nominal*.root'

ttWPath  = path+'/TTW*/*nominal*.root'

ttZqqPath = path+'/TTZToQQ*/*nominal*.root'
ttZllPath = path+'/TTZToLLNuNu*/*nominal*.root'

ttZPath  = path+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path+'/TTZToQQ*/*nominal*.root'

dibosonPathS = path+'/WW_*/*nominal*.root'+';'+ \
               path+'/WZ_*/*nominal*.root'+';'+ \
               path+'/ZZ_*/*nominal*.root'

stpath = path+'/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_new_pmx/*nominal*.root'+';'+ \
         path+'/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8*/*nominal*.root'+';'+ \
         path+'/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx*/*nominal*.root'+';'+ \
         path+'/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8*/*nominal*.root'+';'+ \
         path+'/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_new_pmx*/*nominal*.root'


ttHbbPath    = path+'/ttHTobb*/*nominal*.root'
ttHnonbbPath = path+'/ttHToNonbb*/*nominal*.root'

ttHpath = path+'/ttHTobb*/*nominal*.root'+';'+ \
          path+'/ttHToNonbb*/*nominal*.root'

friendTrees = {
    "ctag": "/nfs/dust/cms/user/vdlinden/legacyTTZ/ntuples/friendTrees/2017/ctagging"
    #"dnnZ": "/nfs/dust/cms/user/vdlinden/legacyTTZ/ntuples/friendTrees/reconstruction/reco_Z_boson/",
    #"dnnH": "/nfs/dust/cms/user/vdlinden/legacyTTZ/ntuples/friendTrees/reconstruction/reco_H_boson/",
    #"matchZ": "/nfs/dust/cms/user/vdlinden/legacyTTZ/ntuples/friendTrees/matched_Z_bosons/",
    #"matchH": "/nfs/dust/cms/user/vdlinden/legacyTTZ/ntuples/friendTrees/matched_H_bosons/",
    }

# SELECTIONS

# need to veto muon events in electron dataset to avoid double counting and vice versa
sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1)"# && (Triggered_HLT_Ele32_WPTight_Gsf_2017SeedsX==1 && Triggered_HLT_Ele32_WPTight_Gsf_L1DoubleEG_vX==1))"
# sel_singlemu="(N_LooseElectrons==0 && N_TightMuons==1 && (Triggered_HLT_IsoMu27_vX==1))"
# sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1)"
sel_singlemu="(N_LooseElectrons==0 && N_TightMuons==1)"
# jet tag base selection #and selection on Pt added
sel_jettag = "(N_Jets>=4 && N_BTagsM>=3)"#&&(Jet_Pt>=50)"

# MET base selection
sel_MET="*(Evt_MET_Pt>20.)"
#sel_MET="*1.0"

# select events without huge MuR/MuF weights
sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'
sel_StrangeMuWeights="*(1.0)"

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
defaultWeight = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2*Weight_btagSF*sf__HT_vs_NJet__btag_NOMINAL"

# pile up weights
pileupWeightUp   = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2Up*Weight_btagSF*sf__HT_vs_NJet__btag_NOMINAL"
pileupWeightDown = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2Down*Weight_btagSF*sf__HT_vs_NJet__btag_NOMINAL"

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


matchableZ =    "((dnnZ_ft_RecoZ_dRGen_Z_genB1_recoB1<=0.4)*" + \
                "(dnnZ_ft_RecoZ_dRGen_Z_genB2_recoB2<=0.4))+" + \
                "((dnnZ_ft_RecoZ_dRGen_Z_genB2_recoB1<=0.4)*" + \
                "(dnnZ_ft_RecoZ_dRGen_Z_genB1_recoB2<=0.4))"

matchableH =    "((dnnH_ft_RecoHiggs_dRGen_Higgs_genB1_recoB1<=0.4)*" + \
                "(dnnH_ft_RecoHiggs_dRGen_Higgs_genB2_recoB2<=0.4))+" + \
                "((dnnH_ft_RecoHiggs_dRGen_Higgs_genB2_recoB1<=0.4)*" + \
                "(dnnH_ft_RecoHiggs_dRGen_Higgs_genB1_recoB2<=0.4))"

nonZbb = "(GenEvt_I_TTZ==0)"
Zbb    = "(GenEvt_I_TTZ==1)"


samples = []

combined_sig_samples = [
    # signal samples     
    plotClasses.Sample('t#bar{t}+H',ROOT.kRed+1,
            ttHpath,
            lumi+sel_MET+evenSel,
            'ttH',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = False),

    plotClasses.Sample('t#bar{t}+Z',ROOT.kMagenta+1,
            ttZPath,
            lumi+sel_MET+evenSel,
            'ttZ',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = False),
    ]

split_sig_samples = [
    # ttH classes
    plotClasses.Sample('t#bar{t}+H (correct H)',ROOT.kRed+1,
            ttHbbPath,
            lumi+sel_MET+evenSel+"*(matchH_ft_RecoHiggs_matchable>0.)*("+matchableH+")",
            'ttH_correctH',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+H (false H)',ROOT.kViolet+1,
            ttHbbPath,
            lumi+sel_MET+evenSel+"*(matchH_ft_RecoHiggs_matchable>0.)*("+matchableH+"==0)",
            'ttH_falseH',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+H (no H)',ROOT.kYellow-7,
            ttHbbPath,
            lumi+sel_MET+evenSel+"*(matchH_ft_RecoHiggs_matchable<=0.)",
            'ttH_noH',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+H (H to non bb)',ROOT.kGreen-10,
            ttHnonbbPath,
            lumi+sel_MET+evenSel+"*(matchH_ft_RecoHiggs_matchable<=0.)",
            'ttH_nonHbb',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),



    # ttZ classes
    plotClasses.Sample('t#bar{t}+Z (correct Z)',ROOT.kMagenta+1,
            ttZqqPath,
            lumi+sel_MET+evenSel+"*(matchZ_ft_RecoZ_matchable>0.)*("+matchableZ+")",
            'ttZ_correctZ',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+Z (false Z)',ROOT.kOrange+7,
            ttZqqPath,
            lumi+sel_MET+evenSel+"*(matchZ_ft_RecoZ_matchable>0.)*("+matchableZ+"==0)",
            'ttZ_falseZ',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+Z (no Z)',ROOT.kSpring-6,
            ttZqqPath,
            lumi+sel_MET+evenSel+"*(matchZ_ft_RecoZ_matchable<=0.)*"+Zbb,
            'ttZ_noZ',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+Z (Z to qq)',ROOT.kAzure+8,
            ttZqqPath,
            lumi+sel_MET+evenSel+"*(matchZ_ft_RecoZ_matchable<=0.)*"+nonZbb,
            'ttZ_Zqq',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+Z (Z to ll)',ROOT.kBlue-4,
            ttZllPath,
            lumi+sel_MET+evenSel+"*(matchZ_ft_RecoZ_matchable<=0.)*"+nonZbb,
            'ttZ_Zll',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    ]


major_backgrounds = [
    # ttbar classes
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

    plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kAzure+3,
            path+"/TTbb_Powheg_Openloops_new_pmx/*nominal*.root",
            lumi+evenSel+'*(GenEvt_I_TTPlusCC==0)*((GenEvt_I_TTPlusBB==1)||(GenEvt_I_TTPlusBB==2)||(GenEvt_I_TTPlusBB==3))'+sel_MET+sel_StrangeMuWeights,
            'ttbb',
            samDict=sampleDict, readTrees=doReadTrees),

    ]

minor_backgrounds = [

    plotClasses.Sample('t',ROOT.kRed-2,
            stpath,
            lumi+sel_MET,
            'singlet',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('V+jets',18,
            path+'/DYJets*/*nominal*.root',
            lumi+sel_MET,
            'vjets',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+W',ROOT.kBlue-10,
            path+'/TTW*/*nominal*.root',
            lumi+sel_MET,
            'ttW',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('VV',ROOT.kAzure+2,
            dibosonPathS,
            lumi+sel_MET,
            'diboson',
            samDict=sampleDict, readTrees=doReadTrees),
    

    ]

samples += combined_sig_samples
#samples += split_sig_samples
samples += major_backgrounds
samples += minor_backgrounds

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = [p for p in processes if not ("ttZ_" in p or "ttH_" in p)]


plottingsamples = [
    plotClasses.Sample("misc.", 18, "", "",
        "misc", addsamples = ["vjets", "diboson", "ttW"],
        samDict = sampleDict, readTrees = doReadTrees),
        
    #plotClasses.Sample("t#bar{t}", 18, "", "",
    #    "ttbar", addsamples = ["ttlf", "ttcc", "ttbb"],
    #    samDict = sampleDict, readTrees = doReadTrees),

    #plotClasses.Sample("t#bar{t}+Z (Zbb in acc.)", ROOT.kMagenta+1, "", "",
    #    "ttZ_ZbbiA", addsamples = ["ttZ_correctZ", "ttZ_falseZ"],
    #    samDict = sampleDict, readTrees = doReadTrees, typ = "signal"),

    #plotClasses.Sample("t#bar{t}+Z (no Zbb)", ROOT.kSpring-6, "", "",
    #    "ttZ_noZbb", addsamples = ["ttZ_noZ", "ttZ_Zqq", "ttZ_Zll"],
    #    samDict = sampleDict, readTrees = doReadTrees, typ = "signal"),

    #plotClasses.Sample("t#bar{t}+H (Hbb in acc.)", ROOT.kRed+1, "", "",
    #    "ttH_HbbiA", addsamples = ["ttH_correctH", "ttH_falseH"],
    #    samDict = sampleDict, readTrees = doReadTrees, typ = "signal"),

    #plotClasses.Sample("t#bar{t}+H (no Hbb)", ROOT.kYellow-7, "", "",
    #    "ttH_noHbb", addsamples = ["ttH_noH", "ttH_nonHbb"],
    #    samDict = sampleDict, readTrees = doReadTrees, typ = "signal"),
    ]

# sort subset of processes in plots. descending order
sortedProcesses = ["ttZ", "ttH", "ttZ_ZbbiA", "ttH_HbbiA", "ttlf", "ttcc", "ttbb", "singlet", "misc", "ttH_noHbb", "ttZ_noZbb"]

