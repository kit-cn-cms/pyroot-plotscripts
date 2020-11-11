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
path  = "/nfs/dust/cms/group/ttx-kit/ntuples_ttZ/2017"

ttbarPathS = path+'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+';'+ \
             path+'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'+";"+\
             path+'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx/*nominal*.root'

VJetsPathS = path+'/DYJets*/*nominal*.root'+';'+ \
             path+'/WJets*/*nominal*.root'

ttWPath  = path+'/TTW*/*nominal*.root'

ttZqqPath = path+'/TTZToQQ*/*nominal*.root'
ttZllPath = path+'/TTZToLLNuNu*/*nominal*.root'

ttZPath  =  path+'/TTZToQQ*/*nominal*.root'+';'+ \
            path+'/TTZToLLNuNu*/*nominal*.root'

dibosonPathS = path+'/WW_*/*nominal*.root'+';'+ \
               path+'/WZ_*/*nominal*.root'+';'+ \
               path+'/ZZ_*/*nominal*.root'

stpath = path+'/ST_*/*nominal*.root'


ttHbbPath    = path+'/ttHTobb*/*nominal*.root'
ttHnonbbPath = path+'/ttHToNonbb*/*nominal*.root'

ttHpath = path+'/ttHTobb*/*nominal*.root'+';'+ \
          path+'/ttHToNonbb*/*nominal*.root'

friendTrees = {
    "weight": "/nfs/dust/cms/group/ttx-kit/ntuples_ttZ/friendTrees/weights/2017"
    #"ctag": "/nfs/dust/cms/user/vdlinden/legacyTTZ/ntuples/friendTrees/2017/ctagging"
    #"dnnZ": "/nfs/dust/cms/user/larmbrus/combined_ttZ_ttH/ntuples/2017/new_ntuples/reconstructed_Z_v1",
    #"dnnH": "/nfs/dust/cms/user/larmbrus/combined_ttZ_ttH/ntuples/2017/new_ntuples/reconstructed_Higgs_v1",
    #"matchZ": "/nfs/dust/cms/user/larmbrus/combined_ttZ_ttH/ntuples/2017/new_ntuples/matchZ_v1",
    #"matchH": "/nfs/dust/cms/user/larmbrus/combined_ttZ_ttH/ntuples/2017/new_ntuples/matchHiggs_v1",
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
defaultWeight = sel_jettag+"*Weight_GEN_nom"
defaultWeight+= "*weight_ft_pileup"
defaultWeight+= "*weight_ft_btagSF*weight_ft_sfPatch"
defaultWeight+= "*(weight_ft_elSF*weight_ft_elTrigSF*"+sel_singleel
defaultWeight+= "+weight_ft_muSF*weight_ft_muTrigSF*"+sel_singlemu+")"

# dictionary of expressions to replace in systematics csv
weightReplacements = {
    # default weight
    "DEFAULTWEIGHT":    defaultWeight,
    # do weights for data
    "DOWEIGHTS":        "(DoWeights==1)+(DoWeights==0)*1.0",
    }

# Lumi weight
lumi = '41.5'

# correct vjets cross sections
kfactor_zjets = "*1.23"
kfactor_wjets = "*1.21"
kfactor_vjets = "*1.22"

# correct ttbb cross-sections
ttbb_FH_scale = "(17.3731/16.2728)"
ttbb_SL_scale = "(15.7438/15.7286)"
ttbb_DL_scale = "(3.5531/3.8024)"
ttbb_4FS_scale = "*((N_GenTopLep==0)*"+ttbb_FH_scale+"+(N_GenTopLep==1)*"+ttbb_SL_scale+"+(N_GenTopLep==2)*"+ttbb_DL_scale+")"

# nominal weight
nominalweight="NomWeight:=("+defaultWeight+")*(DoWeights==1)+(DoWeights==0)*1.0"

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
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = True),

    plotClasses.Sample('t#bar{t}+Z',ROOT.kMagenta+1,
            ttZPath,
            lumi+sel_MET+evenSel,
            'ttZ',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal", plot = True),
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
            path+"/TTbb*/*nominal*.root",
            lumi+evenSel+'*(GenEvt_I_TTPlusCC==0)*(GenEvt_I_TTPlusBB>=1)'+ttbb_4FS_scale+sel_MET+sel_StrangeMuWeights,
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
            VJetsPathS,
            lumi+kfactor_vjets+sel_MET,
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

