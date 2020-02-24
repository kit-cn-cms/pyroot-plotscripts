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
path  = "/nfs/dust/cms/user/vdlinden/legacyTTH/ntuples/nobtags/2016/"


path_4FS_ttbb_SL  = path+"/TTbb_4f*SemiLeptonic*/*nominal*.root"
path_4FS_ttbb_DL  = path+"/TTbb_4f*2l2nu*/*nominal*.root"
path_4FS_ttbb_FH  = path+"/TTbb_4f*Hadronic*/*nominal*.root"

path_5FS_ttbar_SL = path+"/TTToSemiLeptonic*/*nominal*.root"
path_5FS_ttbar_DL = path+"/TTTo2L2Nu*/*nominal*.root"
path_5FS_ttbar_FH = path+"/TTToHadronic*/*nominal*.root"

path_ttH_bb       = path+"/ttHTobb*/*nominal*.root"
path_ttH_nonbb    = path+"/ttHToNonbb*/*nominal*.root"

path_ttZ_qq       = path+"/TTZToQQ*/*nominal*.root"
path_ttZ_ll       = path+"/TTZToLL*/*nominal*.root"

# SELECTIONS
# need to veto muon events in electron dataset to avoid double counting and vice versa
sel_singleel="((N_LooseMuons==0 && N_TightElectrons==1))"
sel_singlemu="(N_LooseElectrons==0 && N_TightMuons==1)"
# jet tag base selection

sel_jettag = "(N_Jets>=4)*(Evt_MET_Pt>20.)"

# ======= # 
# WEIGHTS #
# ======= #
defaultWeight = sel_jettag+"*Weight_GEN_nom*Weight_pu69p2"

# lepton scale factors
electronSFs = "((N_TightElectrons==1)&&(Electron_IdentificationSF[0]>0.)&&(Electron_ReconstructionSF[0]>0.))*Electron_IdentificationSF[0]*Electron_ReconstructionSF[0]"
muonSFs     = "((N_TightMuons==1)&&(Muon_IdentificationSF[0]>0.)&&(Muon_IsolationSF[0]>0.))*Muon_IdentificationSF[0]*Muon_IsolationSF[0]"
electronTrigger = "("+sel_singleel+"&&(internalEleTriggerWeight>0.))*internalEleTriggerWeight"
muonTrigger = "("+sel_singlemu+"&&(Weight_MuonTriggerSF>0.))*Weight_MuonTriggerSF"

defaultWeight += "*"+"("+electronSFs+"+"+muonSFs+")"+"*"+"("+electronTrigger+"+"+muonTrigger+")"
# dictionary of expressions to replace in systematics csv

weightReplacements = {
    # default weight
    "FINALWEIGHTNJET":  defaultWeight+"*internalCSVweight*sf__NJet__btag_NOMINAL",
    "FINALWEIGHTHT":    defaultWeight+"*internalCSVweight*sf__HT_vs_NJet__btag_NOMINAL",
    "DEFAULTWEIGHT":    defaultWeight+"*internalCSVweight",
    }


# Lumi weight
lumi = '59.7'
sel_ttb  = "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==1)"
sel_tt2b = "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==2)"
sel_ttbb = "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==3)"
sel_tthf = "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB>=1)"
sel_ttcc = "(GenEvt_I_TTPlusCC==1)"
sel_ttlf = "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)"

# nominal weight
nominalweight="NomWeight:=("+defaultWeight+")"

sampleDict=plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees=True

# data samples
samplesDataControlPlots=[
]


samples  = [
     plotClasses.Sample('t#bar{t}+H',ROOT.kBlue+1,
            path_ttH_bb+";"+path_ttH_nonbb,
            lumi,
            'ttH',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),     

     plotClasses.Sample('t#bar{t}+b#bar{b} (4FS)',ROOT.kRed+3,
             path_4FS_ttbb_SL+";"+path_4FS_ttbb_DL+";"+path_4FS_ttbb_FH,
             lumi+"*"+sel_tthf,
             'ttbb',
             samDict=sampleDict, readTrees=doReadTrees),

     plotClasses.Sample('t#bar{t}+b#bar{b} (5FS)',ROOT.kRed+3,
             path_5FS_ttbar_SL+";"+path_5FS_ttbar_DL+";"+path_5FS_ttbar_FH,
             lumi+"*"+sel_tthf,
             'ttbb_5FS',
             samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+lf',ROOT.kRed-7,
            path_5FS_ttbar_SL+";"+path_5FS_ttbar_DL+";"+path_5FS_ttbar_FH,
            lumi+"*"+sel_ttlf,
            'ttlf',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,
            path_5FS_ttbar_SL+";"+path_5FS_ttbar_DL+";"+path_5FS_ttbar_FH,
            lumi+"*"+sel_ttcc,
            'ttcc',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+Z',ROOT.kOrange+7,
            path_ttZ_qq+";"+path_ttZ_ll,
            lumi,
            'ttZ',
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
sortedProcesses = []
