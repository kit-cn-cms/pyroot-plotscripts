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
path_vdlinden       = "/nfs/dust/cms/user/vdlinden/legacyTTH/ntuples/legacy_2018_ttZ_v4"
path_vdlinden_data  = "/nfs/dust/cms/user/vdlinden/legacyTTH/ntuples/legacy_2018_ttZ_v2"

ttbarPathS          = path_vdlinden+'/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
                      path_vdlinden+'/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+\
                      path_vdlinden+'/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'

dibosonPathS        = path_vdlinden+'/WW_*/*nominal*.root'+';'+ \
                      path_vdlinden+'/WZ_*/*nominal*.root'+';'+ \
                      path_vdlinden+'/ZZ_*/*nominal*.root'

stpath              = path_vdlinden+'/ST_*/*nominal*.root'

ttHpath             = path_vdlinden+'/ttHTobb_M125*/*nominal*.root'+';'+ \
	                  path_vdlinden+'/ttHToNonbb_M125*/*nominal*.root'

# SELECTIONS

# need to veto muon events in electron dataset to avoid double counting and vice versa
sel_singleel    = "(N_LooseMuons==0 && N_TightElectrons==1)" # && (Triggered_HLT_Ele32_WPTight_Gsf_vX==1 || Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1)"
sel_singlemu    = "(N_LooseElectrons==0 && N_TightMuons==1)" # && (Triggered_HLT_IsoMu24_vX==1))"

# jet tag base selection
sel_base        = "(N_Jets>=4 && N_BTagsM>=3)*(Evt_MET_Pt>20.)"

# select events without huge MuR/MuF weights
sel_StrangeMuWeights = "*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)"



# ======= # 
# WEIGHTS #
# ======= #
defaultWeight           = sel_base+"*Weight_GEN_nom*Weight_pu69p2*Weight_CSV"

# pile up weights
pileupWeightUp          = sel_base+"*Weight_GEN_nom*Weight_pu69p2Up*Weight_CSV"
pileupWeightDown        = sel_base+"*Weight_GEN_nom*Weight_pu69p2Down*Weight_CSV"

# lepton scale factors
electronSFs             = "("+sel_singleel+"&&(Electron_IdentificationSF[0]>0.)&&(Electron_ReconstructionSF[0]>0.))*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0]"
muonSFs                 = "("+sel_singlemu+"&&(Muon_IdentificationSF[0]>0.)&&(Muon_IsolationSF[0]>0.))*Muon_IdentificationSF[0]*Muon_IsolationSF[0]"

electronSFs_up          = "("+sel_singleel+"&&(Electron_IdentificationSFUp[0]>0.)&&(Electron_ReconstructionSFUp[0]>0.))*Electron_IdentificationSFUp[0]*Electron_ReconstructionSFUp[0]"
electronSFs_down        = "("+sel_singleel+"&&(Electron_IdentificationSFDown[0]>0.)&&(Electron_ReconstructionSFDown[0]>0.))*Electron_IdentificationSFDown[0]*Electron_ReconstructionSFDown[0]"
muonSFs_up              = "("+sel_singlemu+"&&(Muon_IdentificationSFUp[0]>0.)&&(Muon_IsolationSFUp[0]>0.))*Muon_IdentificationSFUp[0]*Muon_IsolationSFUp[0]"
muonSFs_down            = "("+sel_singleme+"&&(Muon_IdentificationSFDown[0]>0.)&&(Muon_IsolationSFDown[0]>0.))*Muon_IdentificationSFDown[0]*Muon_IsolationSFDown[0]"

# trigger scale factors
electronTrigger         = "("+sel_singleel+"&&(Weight_EleTriggerSF>0.))*Weight_EleTriggerSF"
muonTrigger             = "("+sel_singlemu+"&&(Weight_MuonTriggerSF>0.))*Weight_MuonTriggerSF"

electronTrigger_up      = "("+sel_singleel+"&&(Weight_EleTriggerSF_Up>0.))*Weight_EleTriggerSF_Up"
electronTrigger_down    = "("+sel_singleel+"&&(Weight_EleTriggerSF_Down>0.))*Weight_EleTriggerSF_Down"
muonTrigger_up          = "("+sel_singlemu+"&&(Weight_MuonTriggerSF_Up>0.))*Weight_MuonTriggerSF_Up"
muonTrigger_down        = "("+sel_singlemu+"&&(Weight_MuonTriggerSF_Down>0.))*Weight_MuonTriggerSF_Down"


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

    # muR/muF variations
    "SCALEMURUP":       "Weight_scale_variation_muR_2p0_muF_1p0*internalNormFactor_Weight_scale_variation_muR_2p0_muF_1p0",
    "SCALEMURDOWN":     "Weight_scale_variation_muR_0p5_muF_1p0*internalNormFactor_Weight_scale_variation_muR_0p5_muF_1p0",
    "SCALEMUFUP":       "Weight_scale_variation_muR_1p0_muF_2p0*internalNormFactor_Weight_scale_variation_muR_1p0_muF_2p0",
    "SCALEMUFDOWN":     "Weight_scale_variation_muR_1p0_muF_0p5*internalNormFactor_Weight_scale_variation_muR_1p0_muF_0p5",

    # do weights for data
    "DOWEIGHTS":        "(DoWeights==1)+(DoWeights==0)*1.0",

    }

# Lumi weight
lumi = '59.7'

# nominal weight
nominalweight = "NomWeight:=("+defaultWeight+"*"+"("+electronSFs+"+"+muonSFs+")"+"*"+"("+electronTrigger+"+"+muonTrigger+")"+")*(DoWeights==1)+(DoWeights==0)*1.0"

# even selection for train samples
evenSel = "*(Evt_Odd==0)*2.0"

sampleDict  = plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees = True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots = [
    #plotClasses.Sample('SingleMu',ROOT.kBlack,
    #        path_vdlinden+'/SingleMuon*/*nominal*.root',
    #        sel_singlemu+"*"+sel_base,
    #        'SingleMu', samDict=sampleDict, readTrees=doReadTrees),

    #plotClasses.Sample('SingleEl',ROOT.kBlack,
    #        path_vdlinden+'/EGamma*/*nominal*.root',
    #        sel_singleel+"*"+sel_base,
    #        'SingleEl', samDict=sampleDict, readTrees=doReadTrees)
    ]

samples = [

    # signal samples     

    plotClasses.Sample('t#bar{t}+Z (Z # rightarrow b#bar{b})',ROOT.kOrange+7,
            path_vdlinden+'/TTZToBB*/*nominal*.root',
            lumi+evenSel+sel_StrangeMuWeights,
            'ttZbb',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+Z (Z #rightarrow q#bar{q})',ROOT.kOrange+7,
            path_vdlinden+'/TTZToQQ*/*nominal*.root',
            lumi+"*(GenEvt_I_TTZ==0)"+sel_StrangeMuWeights,
            'ttZqq',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    plotClasses.Sample('t#bar{t}+Z, (Z #rightarrow ll/#nu#nu)', ROOT.kOrange+7,
            path_vdlinden+'/TTZToLLNuNu_M-10*/*nominal*.root',
            lumi+sel_StrangeMuWeights,
            'ttZll',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),
    
    # background samples

    plotClasses.Sample('t#bar{t}+lf',ROOT.kAzure-9,
            ttbarPathS,
            lumi+evenSel+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_StrangeMuWeights,
            'ttlf',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kAzure+8,
            ttbarPathS,
            lumi+evenSel+'*(GenEvt_I_TTPlusCC==1)'+sel_StrangeMuWeights,
            'ttcc',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kAzure+3,
            ttbarPathS,
            lumi+evenSel+"*1.312"+'*(GenEvt_I_TTPlusBB>=1)'+sel_StrangeMuWeights,
            'ttbb',
            samDict=sampleDict, readTrees=doReadTrees),

    # minor samples
    
    plotClasses.Sample('Single Top',ROOT.kRed-2,
            stpath,
            lumi,
            'singlet',
            samDict=sampleDict, readTrees=doReadTrees),
 
    plotClasses.Sample('Z+jets',ROOT.kGreen-3,
            path_vdlinden+'/DYJets*/*nominal*.root',
            lumi,
            'zjets',
            samDict=sampleDict, readTrees=doReadTrees),
 
    plotClasses.Sample('W+jets',ROOT.kGreen-7,
            path_vdlinden+'/WJets*/*nominal*.root',
            lumi,
            'wjets',
            samDict=sampleDict, readTrees=doReadTrees), 

    plotClasses.Sample('t#bar{t}+W',ROOT.kBlue-10,
            path_vdlinden+'/TTW*/*nominal*.root',
            lumi,
            'ttW',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('Diboson',ROOT.kAzure+2,
            dibosonPathS,
            lumi,
            'diboson',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+H',ROOT.kRed+1,
            ttHpath,
            lumi+evenSel+sel_StrangeMuWeights,
            'ttH',
            samDict=sampleDict, readTrees=doReadTrees),

    ]

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = processes

plottingsamples = [
    plotClasses.Sample("t#bar{t}+Z", ROOT.kOrange+7,
        "", "", "ttZ", addsamples = ["ttZbb", "ttZqq", "ttZll"],
        samDict = sampleDict, readTrees = doReadTrees, typ = "signal"),

    plotClasses.Sample("misc.", ROOT.kGray,
        "", "", "misc", addsamples = ["wjets", "zjets", "diboson", "ttW"],
        samDict = sampleDict, readTrees = doReadTrees)
    ]


# sort subset of processes in plots. descending order
sortedProcesses = ["ttlf", "ttcc", "ttbb", "singlet", "misc", "ttH", "ttZ"]






