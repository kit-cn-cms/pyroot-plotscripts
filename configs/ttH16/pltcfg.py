import sys
import os
import ROOT
import pandas
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses

# samples
# input path 
path_mwassmer  = "/nfs/dust/cms/user/mwassmer/ttH_2019/ntuples_2018"

ttbarPathS = path_mwassmer+'/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
             path_mwassmer+'/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+\
             path_mwassmer+'/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'

VJetsPathS = path_mwassmer+'/DYJets*/*nominal*.root'+';'+ \
             path_mwassmer+'/WJets*/*nominal*.root'

ttVPathS = path_mwassmer+'/TTW*/*nominal*.root'+';'+ \
           path_mwassmer+'/TTZToLLNuNu*/*nominal*.root'+';'+ \
           path_mwassmer+'/TTZToQQ*/*nominal*.root'

dibosonPathS = path_mwassmer+'/WW_*/*nominal*.root'+';'+ path_mwassmer+'/ZZ_*/*nominal*.root'

stpath = path_mwassmer+'/ST_*/*nominal*.root'

ttHpath = path_mwassmer+'/ttHTobb_M125*/*nominal*.root'+';'+ \
          path_mwassmer+'/ttHToNonbb_M125*/*nominal*.root'

# SELECTIONS

# need to veto muon events in electron dataset to avoid double counting and vice versa
sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1 && (Triggered_HLT_Ele32_WPTight_Gsf_vX==1))*(N_Jets>=4 && N_BTagsM>=3)"
sel_singlemu="(N_LooseElectrons==0 && N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1))*(N_Jets>=4 && N_BTagsM>=3)"
sel_MET="*(Evt_Pt_MET>20.)"

#sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'
sel_StrangeMuWeights = '*1.'

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

# weights
usualWeight = "1.*(N_Jets>=4 && N_BTagsM>=3)*Weight_GEN_nom"

puWeight = "Weight_pu69p2"

csvWeight = "Weight_CSV"

# lepton scalefactors
leptonscalefactors = "(((N_TightElectrons==1) && (Electron_IdentificationSF[0]>0.) && (Electron_ReconstructionSF[0]>0.))*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0] + ((N_TightMuons==1) && (Muon_IdentificationSF[0]>0.) && (Muon_IsolationSF[0]>0.))*Muon_IdentificationSF[0]*Muon_IsolationSF[0])"

electronscalefactorsup = "(((N_TightElectrons==1) && (Electron_IdentificationSFUp[0]>0.) && (Electron_ReconstructionSFUp[0]>0.))*Electron_IdentificationSFUp[0]*Electron_ReconstructionSFUp[0] + ((N_TightMuons==1) && (Muon_IdentificationSF[0]>0.) && (Muon_IsolationSF[0]>0.))*Muon_IdentificationSF[0]*Muon_IsolationSF[0])"

electronscalefactorsdown = "(((N_TightElectrons==1) && (Electron_IdentificationSFDown[0]>0.) && (Electron_ReconstructionSFDown[0]>0.))*Electron_IdentificationSFDown[0]*Electron_ReconstructionSFDown[0] + ((N_TightMuons==1) && (Muon_IdentificationSF[0]>0.) && (Muon_IsolationSF[0]>0.))*Muon_IdentificationSF[0]*Muon_IsolationSF[0])"

muonscalefactorsup = "(((N_TightElectrons==1) && (Electron_IdentificationSF[0]>0.) && (Electron_ReconstructionSF[0]>0.))*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0] + ((N_TightMuons==1) && (Muon_IdentificationSFUp[0]>0.) && (Muon_IsolationSFUp[0]>0.))*Muon_IdentificationSFUp[0]*Muon_IsolationSFUp[0])"

muonscalefactorsdown = "(((N_TightElectrons==1) && (Electron_IdentificationSF[0]>0.) && (Electron_ReconstructionSF[0]>0.))*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0] + ((N_TightMuons==1) && (Muon_IdentificationSFDown[0]>0.) && (Muon_IsolationSFDown[0]>0.))*Muon_IdentificationSFDown[0]*Muon_IsolationSFDown[0])"

triggerscalefactors = "(((N_TightElectrons==1) && (N_LooseMuons==0) && (Triggered_HLT_Ele32_WPTight_Gsf_vX==1))*1. + ((N_TightMuons==1) && (N_LooseElectrons==0) && (Triggered_HLT_IsoMu24_vX==1) && (Weight_MuonTriggerSF>0.))*Weight_MuonTriggerSF)"

muontrigscalefactorsup = "(((N_TightElectrons==1) && (N_LooseMuons==0) && (Triggered_HLT_Ele32_WPTight_Gsf_vX==1))*1. + ((N_TightMuons==1) && (N_LooseElectrons==0) && (Triggered_HLT_IsoMu24_vX==1) && (Weight_MuonTriggerSF_Up>0.))*Weight_MuonTriggerSF_Up)"

muontrigscalefactorsdown = "(((N_TightElectrons==1) && (N_LooseMuons==0) && (Triggered_HLT_Ele32_WPTight_Gsf_vX==1))*1. + ((N_TightMuons==1) && (N_LooseElectrons==0) && (Triggered_HLT_IsoMu24_vX==1) && (Weight_MuonTriggerSF_Down>0.))*Weight_MuonTriggerSF_Down)"

doWeightsFlag = "(DoWeights==1)+(DoWeights==0)*1.0"

# dictionary of expressions to replace in systematics csv
weightReplacements = {
    "USUALWEIGHT":              usualWeight,
    "LEPTONSCALEFACTORS":       leptonscalefactors,
    "ELECTRONSCALEFACTORSUP":   electronscalefactorsup,
    "ELECTRONSCALEFACTORSDOWN": electronscalefactorsdown,
    "MUONSCALEFACTORSUP":       muonscalefactorsup,
    "MUONSCALEFACTORSDOWN":     muonscalefactorsdown,
    "TRIGGERSCALEFACTORS":      triggerscalefactors,
    "DOWEIGHTS":                doWeightsFlag,
    "CSVWEIGHT":                csvWeight,
    "PUWEIGHT":                 puWeight,
    "MUONTRIGSCALEFACTORSUP":   muontrigscalefactorsup,
    "MUONTRIGSCALEFACTORSDOWN": muontrigscalefactorsdown
    }

# names of the systematics (proper names needed e.g. for combination)
# Lumi weight
mcWeight = "59.7"
evenSel  = "*(Evt_Odd==0)*2.0"

nominalweight="NomWeight:="+usualWeight+"*"+puWeight+"*"+triggerscalefactors+"*"+leptonscalefactors+"*"+csvWeight+"*"+doWeightsFlag


# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
sampleDict=plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees=True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
   plotClasses.Sample('SingleMu',ROOT.kBlack,
           path_mwassmer+'/SingleMuon*/*nominal*.root',
           sel_singlemu+sel_MET,
           'SingleMu', samDict=sampleDict, readTrees=doReadTrees),

   plotClasses.Sample('SingleEl',ROOT.kBlack,
           path_mwassmer+'/EGamma*/*nominal*.root',
           sel_singleel+sel_MET,
           'SingleEl', samDict=sampleDict, readTrees=doReadTrees)
]

print "samples"


#print "limit samples"
samples=[

    plotClasses.Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,
            path_mwassmer+'/ttHTobb_M125*/*nominal*.root',
            '1.0*'+mcWeight+evenSel+sel_MET,
            'ttH_hbb',
            samDict=sampleDict, readTrees=doReadTrees,typ="signal"),
  
    plotClasses.Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,
            path_mwassmer+'/ttHToNonbb_M125*/*nominal*.root',
            '1.0*'+mcWeight+evenSel+hccSel+sel_MET,
            'ttH_hcc',
            samDict=sampleDict, readTrees=doReadTrees,typ="signal"),
  
    plotClasses.Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,
            path_mwassmer+'/ttHToNonbb_M125*/*nominal*.root',
            '1.0*'+mcWeight+evenSel+httSel+sel_MET,
            'ttH_htt',
            samDict=sampleDict, readTrees=doReadTrees,typ="signal"),
  
    plotClasses.Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,
            path_mwassmer+'/ttHToNonbb_M125*/*nominal*.root',
            '1.0*'+mcWeight+evenSel+hggSel+sel_MET,'ttH_hgg',
            samDict=sampleDict, readTrees=doReadTrees,typ="signal"), 
 
    plotClasses.Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,
            path_mwassmer+'/ttHToNonbb_M125*/*nominal*.root',
            '1.0*'+mcWeight+evenSel+hglugluSel+sel_MET, 
            'ttH_hgluglu',
            samDict=sampleDict, readTrees=doReadTrees,typ="signal"), 
 
    plotClasses.Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,
            path_mwassmer+'/ttHToNonbb_M125*/*nominal*.root',
            '1.0*'+mcWeight+evenSel+hwwSel+sel_MET,'ttH_hww',
            samDict=sampleDict, readTrees=doReadTrees,typ="signal"),
  
    plotClasses.Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,
            path_mwassmer+'/ttHToNonbb_M125*/*nominal*.root',
            '1.0*'+mcWeight+evenSel+hzzSel+sel_MET,
            'ttH_hzz',
            samDict=sampleDict, readTrees=doReadTrees,typ="signal"),
  
    plotClasses.Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,
            path_mwassmer+'/ttHToNonbb_M125*/*nominal*.root',
            '1.0*'+mcWeight+evenSel+hzgSel+sel_MET, 
            'ttH_hzg',
            samDict=sampleDict, readTrees=doReadTrees,typ="signal"),
    
    # background samples

    plotClasses.Sample('t#bar{t}+lf',ROOT.kRed-7,
            ttbarPathS,
            mcWeight+evenSel+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttbarOther',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,
            ttbarPathS,
            mcWeight+evenSel+'*(GenEvt_I_TTPlusCC==1)'+sel_MET+sel_StrangeMuWeights,
            'ttbarPlusCCbar',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+b',ROOT.kRed-2,
            ttbarPathS,
            mcWeight+evenSel+'*(GenEvt_I_TTPlusBB==1)'+sel_MET+sel_StrangeMuWeights,
            'ttbarPlusB',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+2b',ROOT.kRed+2,
            ttbarPathS,
            mcWeight+evenSel+'*(GenEvt_I_TTPlusBB==2)'+sel_MET+sel_StrangeMuWeights,
            'ttbarPlus2B',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,
            ttbarPathS,
            mcWeight+evenSel+'*(GenEvt_I_TTPlusBB==3)'+sel_MET+sel_StrangeMuWeights,
            'ttbarPlusBBbar',
            samDict=sampleDict, readTrees=doReadTrees), 

    # minor samples
    
    plotClasses.Sample('Single Top',ROOT.kMagenta,
            stpath,
            mcWeight+sel_MET,
            'singlet',
            samDict=sampleDict, readTrees=doReadTrees),
 
    plotClasses.Sample('Z+jets',ROOT.kGreen-3,
            path_mwassmer+'/DYJets*/*nominal*.root',
            mcWeight+sel_MET,
            'zjets',
            samDict=sampleDict, readTrees=doReadTrees),
 
    plotClasses.Sample('W+jets',ROOT.kGreen-7,
            path_mwassmer+'/WJets*/*nominal*.root',
            mcWeight+sel_MET,
            'wjets',
            samDict=sampleDict, readTrees=doReadTrees), 

    plotClasses.Sample('t#bar{t}+W',ROOT.kBlue-10,
            path_mwassmer+'/TTW*/*nominal*.root',  
            mcWeight+sel_MET,
            'ttbarW',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+Z',ROOT.kBlue-6,
            path_mwassmer+'/TTZToLLNuNu*/*nominal*.root'+';'+ path_mwassmer+'/TTZToQQ*/*nominal*.root',
            mcWeight+sel_MET,
            'ttbarZ',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('Diboson',ROOT.kAzure+2,
           dibosonPathS,
           mcWeight+sel_MET,
           'diboson',
           samDict=sampleDict, readTrees=doReadTrees), 
]

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = processes



#define summerized samples that are used later in the plotting step instead of the single processes
plottingsamples=[
    
    plotClasses.Sample('t#bar{t}H',ROOT.kBlue+1,
            path_mwassmer+'/ttH*/*nominal*.root',
            mcWeight+sel_MET,
            'ttH', 
            addsamples=['ttH_hbb','ttH_hcc','ttH_htt','ttH_hgg','ttH_hgluglu','ttH_hww','ttH_hzz','ttH_hzg'],
            samDict=sampleDict, readTrees=doReadTrees,typ="signal"), 

    plotClasses.Sample('V+jets',ROOT.kGreen-3,
            VJetsPathS,
            mcWeight+sel_MET,
            'Vjets', addsamples=['wjets','zjets'],
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample(
            't#bar{t}+V',ROOT.kBlue-10,
            ttVPathS,
            mcWeight+sel_MET,
            'ttV',  addsamples=['ttbarW','ttbarZ'],
            samDict=sampleDict, readTrees=doReadTrees),
]

# sort subset of processes in plots. descending order
sortedProcesses = []

