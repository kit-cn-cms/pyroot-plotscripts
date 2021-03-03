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
base     = "/nfs/dust/cms/group/ttx-kit/ntuples_ttZ/{year}"

ttbar18  = base.format(year="2018")+'/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
           base.format(year="2018")+'/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'+";"+\
           base.format(year="2018")+'/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/*nominal*.root'

ttbar17  = base.format(year="2017")+'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
           base.format(year="2017")+'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+";"+\
           base.format(year="2017")+'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx/*nominal*.root'

ttbar16  = base.format(year="2016")+'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
           base.format(year="2016")+'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+";"+\
           base.format(year="2016")+'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'

ttbb     = base+"/TTbb*/*nominal*.root"

vjets    = base+'/DYJets*/*nominal*.root'+';'+ \
           base+'/WJets*/*nominal*.root'

ttW      = base+'/TTW*/*nominal*.root'

ttZqq    = base+'/TTZToQQ*/*nominal*.root'
ttZll    = base+'/TTZToLLNuNu*/*nominal*.root'
ttZ      = ttZqq+";"+ttZll

diboson  = base+'/WW_*/*nominal*.root'+';'+ \
           base+'/WZ_*/*nominal*.root'+';'+ \
           base+'/ZZ_*/*nominal*.root'

singlet  = base+'/ST_*/*nominal*.root'

ttHbb    = base+'/ttHTobb*/*nominal*.root'
ttHnonbb = base+'/ttHToNonbb*/*nominal*.root'
ttH      = ttHbb+";"+ttHnonbb

friendTrees = {
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

sel_StrangeMuWeights="*(1.0)"

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
lumi18 = '59.7'
lumi17 = '41.5'
lumi16 = '35.9'

# correct vjets cross sections
kfactor_zjets = "*1.23"
kfactor_wjets = "*1.21"
kfactor_vjets = "*1.22"

# correct ttbb cross-sections
ttbb_FH_scale18  = "(17.3853/16.2728)"
ttbb_SL_scale18  = "(15.7322/15.7286)"
ttbb_DL_scale18  = "(3.5378/3.8024)"
ttbb_4FS_scale18 = "*((N_GenTopLep==0)*"+ttbb_FH_scale18+"+(N_GenTopLep==1)*"+ttbb_SL_scale18+"+(N_GenTopLep==2)*"+ttbb_DL_scale18+")"

ttbb_FH_scale17  = "(17.3731/16.2728)"
ttbb_SL_scale17  = "(15.7438/15.7286)"
ttbb_DL_scale17  = "(3.5531/3.8024)"
ttbb_4FS_scale17 = "*((N_GenTopLep==0)*"+ttbb_FH_scale17+"+(N_GenTopLep==1)*"+ttbb_SL_scale17+"+(N_GenTopLep==2)*"+ttbb_DL_scale17+")"

ttbb_FH_scale16  = "(17.3107/16.2728)"
ttbb_SL_scale16  = "(15.7315/15.7286)"
ttbb_DL_scale16  = "(3.5378/3.8024)"
ttbb_4FS_scale16 = "*((N_GenTopLep==0)*"+ttbb_FH_scale16+"+(N_GenTopLep==1)*"+ttbb_SL_scale16+"+(N_GenTopLep==2)*"+ttbb_DL_scale16+")"

# nominal weight
nominalweight="NomWeight:=("+defaultWeight+"*"+"("+electronSFs+"+"+muonSFs+")"+"*"+"("+electronTrigger+"+"+muonTrigger+")"+")*(DoWeights==1)+(DoWeights==0)*1.0"

# even selection for sample splitting
evenSel="*(Evt_Odd==0)*2.0"

sampleDict=plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees=True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
    plotClasses.Sample('SingleMu18',ROOT.kBlack,
            base.format(year="2018")+'/SingleMuon*/*nominal*.root',
            sel_singlemu+sel_MET+"*"+sel_jettag,
            'SingleMu18', samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('SingleMu17',ROOT.kBlack,
            base.format(year="2017")+'/SingleMuon*/*nominal*.root',
            sel_singlemu+sel_MET+"*"+sel_jettag,
            'SingleMu17', samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('SingleMu16',ROOT.kBlack,
            base.format(year="2016")+'/SingleMuon*/*nominal*.root',
            sel_singlemu+sel_MET+"*"+sel_jettag,
            'SingleMu16', samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('SingleEl18',ROOT.kBlack,
            base.format(year="2018")+'/EGamma*/*nominal*.root',
            sel_singleel+sel_MET+"*"+sel_jettag,
            'SingleEl18', samDict=sampleDict, readTrees=doReadTrees)

    plotClasses.Sample('SingleEl17',ROOT.kBlack,
            base.format(year="2017")+'/SingleEl*/*nominal*.root',
            sel_singleel+sel_MET+"*"+sel_jettag,
            'SingleEl17', samDict=sampleDict, readTrees=doReadTrees)

    plotClasses.Sample('SingleEl16',ROOT.kBlack,
            base.format(year="2016")+'/SingleEl*/*nominal*.root',
            sel_singleel+sel_MET+"*"+sel_jettag,
            'SingleEl16', samDict=sampleDict, readTrees=doReadTrees)
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
    plotClasses.Sample('t#bar{t}+H (18)',ROOT.kRed+1,
            ttH.format(year="2018"),
            lumi18+sel_MET+evenSel,
            'ttH18',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = True),

    plotClasses.Sample('t#bar{t}+H (17)',ROOT.kRed+1,
            ttH.format(year="2017"),
            lumi17+sel_MET+evenSel,
            'ttH17',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = True),

    plotClasses.Sample('t#bar{t}+H (16)',ROOT.kRed+1,
            ttH.format(year="2016"),
            lumi16+sel_MET+evenSel,
            'ttH16',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = True),

    plotClasses.Sample('t#bar{t}+Z (18)',ROOT.kMagenta+1,
            ttZ.format(year="2018"),
            lumi18+sel_MET+evenSel,
            'ttZ18',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = True),

    plotClasses.Sample('t#bar{t}+Z (17)',ROOT.kMagenta+1,
            ttZ.format(year="2017"),
            lumi17+sel_MET+evenSel,
            'ttZ17',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = True),

    plotClasses.Sample('t#bar{t}+Z (16)',ROOT.kMagenta+1,
            ttZ.format(year="2016"),
            lumi16+sel_MET+evenSel,
            'ttZ16',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = True),
    ]

major_backgrounds = [
    # ttbar classes
    plotClasses.Sample('t#bar{t}+lf (18)',ROOT.kAzure-9,
            ttbar18,
            lumi18+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttlf18',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+lf (17)',ROOT.kAzure-9,
            ttbar17,
            lumi17+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttlf17',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+lf (16)',ROOT.kAzure-9,
            ttbar16,
            lumi16+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttlf16',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c} (18)',ROOT.kAzure+8,
            ttbar18,
            lumi18+'*(GenEvt_I_TTPlusCC==1&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttcc18',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c} (17)',ROOT.kAzure+8,
            ttbar17,
            lumi17+'*(GenEvt_I_TTPlusCC==1&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttcc17',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c} (16)',ROOT.kAzure+8,
            ttbar16,
            lumi16+'*(GenEvt_I_TTPlusCC==1&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,
            'ttcc16',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+b#bar{b} (18)',ROOT.kAzure+3,
            ttbb.format(year="2018"),
            lumi18+evenSel+'*(GenEvt_I_TTPlusCC==0)*(GenEvt_I_TTPlusBB>=1)'+ttbb_4FS_scale18+sel_MET+sel_StrangeMuWeights,
            'ttbb18',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+b#bar{b} (17)',ROOT.kAzure+3,
            ttbb.format(year="2017"),
            lumi17+evenSel+'*(GenEvt_I_TTPlusCC==0)*(GenEvt_I_TTPlusBB>=1)'+ttbb_4FS_scale17+sel_MET+sel_StrangeMuWeights,
            'ttbb17',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+b#bar{b} (16)',ROOT.kAzure+3,
            ttbb.format(year="2016"),
            lumi16+evenSel+'*(GenEvt_I_TTPlusCC==0)*(GenEvt_I_TTPlusBB>=1)'+ttbb_4FS_scale16+sel_MET+sel_StrangeMuWeights,
            'ttbb16',
            samDict=sampleDict, readTrees=doReadTrees),

    ]

minor_backgrounds = [

    plotClasses.Sample('t (18)',ROOT.kRed-2,
            singlet.format(year="2018"),
            lumi18+sel_MET,
            'singlet18',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t (17)',ROOT.kRed-2,
            singlet.format(year="2017"),
            lumi17+sel_MET,
            'singlet17',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t (16)',ROOT.kRed-2,
            singlet.format(year="2016"),
            lumi16+sel_MET,
            'singlet16',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('v+jets (18)',18,
            vjets.format(year="2018"),
            lumi18+kfactor_vjets+sel_MET,
            'vjets18',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('v+jets (17)',18,
            vjets.format(year="2017"),
            lumi17+kfactor_vjets+sel_MET,
            'vjets17',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('v+jets (16)',18,
            vjets.format(year="2016"),
            lumi16+kfactor_vjets+sel_MET,
            'vjets16',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+W (18)',ROOT.kBlue-10,
            ttW.format(year="2018"),
            lumi18+sel_MET,
            'ttW18',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+W (17)',ROOT.kBlue-10,
            ttW.format(year="2017"),
            lumi17+sel_MET,
            'ttW17',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+W (16)',ROOT.kBlue-10,
            ttW.format(year="2016"),
            lumi16+sel_MET,
            'ttW16',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('VV (18)',ROOT.kAzure+2,
            diboson.format(year="2018"),
            lumi18+sel_MET,
            'diboson18',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('VV (17)',ROOT.kAzure+2,
            diboson.format(year="2017"),
            lumi17+sel_MET,
            'diboson17',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('VV (16)',ROOT.kAzure+2,
            diboson.format(year="2016"),
            lumi16+sel_MET,
            'diboson16',
            samDict=sampleDict, readTrees=doReadTrees),
    

    ]

samples += combined_sig_samples
samples += major_backgrounds
samples += minor_backgrounds

processes = []
for sample in samples:
    processes.append(sample.nick)
list_of_processes   = processes
datacard_processes  = [p for p in processes if not ("ttZ_" in p or "ttH_" in p)]


plottingsamples = [
    plotClasses.Sample("t#bar{t}+H", ROOT.kRed+1, "", "",
        "ttH", addsamples = ["ttH18", "ttH17", "ttH16"],
        samDict = sampleDict, readTrees = doReadTrees),
        
    plotClasses.Sample("t#bar{t}+Z", ROOT.kMagenta+1, "", "",
        "ttZ", addsamples = ["ttZ18", "ttZ17", "ttZ16"],
        samDict = sampleDict, readTrees = doReadTrees),
        
    plotClasses.Sample("t#bar{t}+jj", ROOT.kAzure-9, "", "",
        "ttlf", addsamples = ["ttlf18", "ttlf17", "ttlf16"],
        samDict = sampleDict, readTrees = doReadTrees),
        
    plotClasses.Sample("t#bar{t}+C", ROOT.kAzure+8, "", "",
        "ttcc", addsamples = ["ttcc18", "ttcc17", "ttcc16"],
        samDict = sampleDict, readTrees = doReadTrees),
        
    plotClasses.Sample("t#bar{t}+B", ROOT.kAzure+3, "", "",
        "ttbb", addsamples = ["ttbb18", "ttbb17", "ttbb16"],
        samDict = sampleDict, readTrees = doReadTrees),
        
    plotClasses.Sample("t", ROOT.kRed-2, "", "",
        "singlet", addsamples = ["singlet18", "singlet17", "singlet16"],
        samDict = sampleDict, readTrees = doReadTrees),

    plotClasses.Sample("misc.", 18, "", "",
        "misc", addsamples = ["vjets18", "vjets17", "vjets16", "diboson18", "diboson17", "diboson16", "ttW18", "ttW17", "ttW16"],
        samDict = sampleDict, readTrees = doReadTrees),
    ]

# sort subset of processes in plots. descending order
sortedProcesses = ["ttZ", "ttH", "ttlf", "ttcc", "ttbb", "singlet", "misc"]

