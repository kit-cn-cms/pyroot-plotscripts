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
#path  = "/nfs/dust/cms/user/thsu/ntuples/"
path = "/nfs/dust/cms/user/thsu/ntuples/"

ttbarPathS = path+'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'
             #'TTbb_Powheg_Openloops_new_pmx' needs to be added?

ttZPath  = path+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path+'/TTZToQQ*/*nominal*.root'

ttHpath = path+'/ttHTobb*/*nominal*.root'+';'+ \
          path+'/ttHToNonbb*/*nominal*.root'

ttbbpath = path+"/TTbb_Powheg_Openloops_new_pmx/*nominal*.root"

friendTrees = {
    "dnnZ": "/nfs/dust/cms/user/thsu/karim/workdir/DNNSet/A",
    "dnnH": "/nfs/dust/cms/user/thsu/karim/workdir/Higgs_multi_Dnn",
    }

# ttZpath =  path+'/TTZToQQ*/*nominal*.root'+';'+ \
        #     path+'/TTZToLLNuNu_M-10*/*nominal*.root'+';'

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
sel_StrangeMuWeights="*(1.0)"

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
    #plotClasses.Sample('SingleMu',ROOT.kBlack,
    #        path+'/SingleMuon*/*nominal*.root',
    #        sel_singlemu+sel_MET+"*"+sel_jettag,
    #        'SingleMu', samDict=sampleDict, readTrees=doReadTrees),

    #plotClasses.Sample('SingleEl',ROOT.kBlack,
    #        path+'/SingleElectron*/*nominal*.root',
    #        sel_singleel+sel_MET+"*"+sel_jettag,
    #        'SingleEl', samDict=sampleDict, readTrees=doReadTrees)
]

samples=[
    # signal samples     
    plotClasses.Sample('t#bar{t}+H',ROOT.kRed+1,
            ttHpath,
            lumi+sel_MET+evenSel,
            'ttH',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+Z',ROOT.kOrange+7,
            ttZPath,
            lumi+sel_MET+evenSel,
            'ttZ',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

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
            ttbbpath,
            lumi+TTbbweight+evenSel+'*(GenEvt_I_TTPlusCC==0)*((GenEvt_I_TTPlusBB==1)||(GenEvt_I_TTPlusBB==2)||(GenEvt_I_TTPlusBB==3))'+sel_MET+sel_StrangeMuWeights,
            'ttbb',
            samDict=sampleDict, readTrees=doReadTrees),

    ]

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = processes


plottingsamples = [
    ]

# sort subset of processes in plots. descending order
sortedProcesses = ["ttZ", "ttH", "ttlf", "ttcc", "ttbb"]

