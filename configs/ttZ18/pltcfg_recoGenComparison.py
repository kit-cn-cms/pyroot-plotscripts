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
path_vdlinden       = "/nfs/dust/cms/user/vdlinden/ttZAnalysis/ntuples/"
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

# lepton scale factors
electronSFs             = "("+sel_singleel+"&&(Electron_IdentificationSF[0]>0.)&&(Electron_ReconstructionSF[0]>0.))*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0]"
muonSFs                 = "("+sel_singlemu+"&&(Muon_IdentificationSF[0]>0.)&&(Muon_IsolationSF[0]>0.))*Muon_IdentificationSF[0]*Muon_IsolationSF[0]"

# trigger scale factors
electronTrigger         = "("+sel_singleel+"&&(Weight_ElectronTriggerSF>0.))*Weight_ElectronTriggerSF"
muonTrigger             = "("+sel_singlemu+"&&(Weight_MuonTriggerSF>0.))*Weight_MuonTriggerSF"

# dictionary of expressions to replace in systematics csv
weightReplacements = {
    }

# Lumi weight
lumi = '59.7'

# nominal weight
nominalweight = "NomWeight:=("+defaultWeight+"*"+"("+electronSFs+"+"+muonSFs+")"+"*"+"("+electronTrigger+"+"+muonTrigger+")"+")*(DoWeights==1)+(DoWeights==0)*1.0"

sampleDict  = plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees = True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots = [
    ]

samples = [

    # signal samples     

    plotClasses.Sample('t#bar{t}+Z',ROOT.kOrange+7,
            path_vdlinden+'/TTZToBB*/*nominal*.root',
            lumi+sel_StrangeMuWeights,
            'ttZbb',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),

    ]

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = processes

plottingsamples = [
    ]


# sort subset of processes in plots. descending order
sortedProcesses = ["ttlf", "ttcc", "ttbb", "singlet", "misc", "ttH", "ttZ"]






