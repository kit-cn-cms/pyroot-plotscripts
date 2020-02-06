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
path  = "/nfs/dust/cms/user/vdlinden/legacyTTH/ntuples/sfDerivation_new/2016/"


path_4FS_ttbb_SL  = path+"/TTbb_4f*SemiLeptonic*/*nominal*.root"
path_4FS_ttbb_DL  = path+"/TTbb_4f*2l2nu*/*nominal*.root"
#path_4FS_ttbb_FH  = path+"/TTbb_4f*Hadronic*/*nominal*.root"

path_5FS_ttbar_SL = path+"/TTToSemiLeptonic*/*nominal*.root"
path_5FS_ttbar_DL = path+"/TTTo2L2Nu*/*nominal*.root"
path_5FS_ttbar_FH = path+"/TTToHadronic*/*nominal*.root"

path_ttH_bb       = path+"/ttHTobb*/*nominal*.root"
path_ttH_nonbb    = path+"/ttHToNonbb*/*nominal*.root"


weightReplacements = {
    # default weight
    "FINALWEIGHTNJET":  "Weight_GEN_nom*internalCSVweight*sf__NJet__btag_NOMINAL",
    "FINALWEIGHTJETPT": "Weight_GEN_nom*internalCSVweight*sf__JetPt_vs_NJet__btag_NOMINAL",
    "FINALWEIGHTNPV":   "Weight_GEN_nom*internalCSVweight*sf__NPV_vs_NJet__btag_NOMINAL",
    "CSVSFWEIGHT":      "Weight_GEN_nom*internalCSVweight",
    "ORIGINALWEIGHT":   "Weight_GEN_nom",
    }


# Lumi weight
lumi = '59.7'
sel_ttb =  "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==1)"
sel_tt2b = "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==2)"
sel_ttbb = "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==3)"
sel_tthf = "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB>=1)"
sel_ttcc = "(GenEvt_I_TTPlusCC==1)"
sel_ttlf = "(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)"

# nominal weight
nominalweight="NomWeight:=(Weight_GEN_nom)"


sampleDict.doPrintout()
doReadTrees=True

# data samples
samplesDataControlPlots=[
]


samples  = [
     plotClasses.Sample('t#bar{t}+H(bb)',ROOT.kBlue+1,
            path_ttH_bb,
            lumi,
            'ttH_bb',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),     

     plotClasses.Sample('t#bar{t}+H(nonbb)',ROOT.kBlue+1,
            path_ttH_nonbb,
            lumi,
            'ttH_nonbb',
            samDict=sampleDict, readTrees=doReadTrees, typ = "signal"),     



     plotClasses.Sample('t#bar{t}+b#bar{b} (4FS,SL)',ROOT.kRed+3,
             path_4FS_ttbb_SL,
             lumi+"*"+sel_tthf,
             'ttbb_SL',
             samDict=sampleDict, readTrees=doReadTrees),

     plotClasses.Sample('t#bar{t}+b#bar{b} (4FS,DL)',ROOT.kRed+3,
             path_4FS_ttbb_DL,
             lumi+"*"+sel_tthf,
             'ttbb_DL',
             samDict=sampleDict, readTrees=doReadTrees),

     #plotClasses.Sample('t#bar{t}+b#bar{b} (4FS,FH)',ROOT.kRed+3,
     #        path_4FS_ttbb_FH,
     #        lumi+"*"+sel_tthf,
     #        'ttbb_FH',
     #        samDict=sampleDict, readTrees=doReadTrees),


     plotClasses.Sample('t#bar{t}+b#bar{b} (5FS,SL)',ROOT.kRed+3,
             path_5FS_ttbar_SL,
             lumi+"*"+sel_tthf,
             'ttbb_5FS_SL',
             samDict=sampleDict, readTrees=doReadTrees),

     plotClasses.Sample('t#bar{t}+b#bar{b} (5FS,DL)',ROOT.kRed+3,
             path_5FS_ttbar_DL,
             lumi+"*"+sel_tthf,
             'ttbb_5FS_DL',
             samDict=sampleDict, readTrees=doReadTrees),

     #plotClasses.Sample('t#bar{t}+b#bar{b} (5FS,FH)',ROOT.kRed+3,
     #        path_5FS_ttbar_FH,
     #        lumi+"*"+sel_tthf,
     #        'ttbb_5FS_FH',
     #        samDict=sampleDict, readTrees=doReadTrees),



     #plotClasses.Sample('t#bar{t}+b (4FS,SL)',ROOT.kRed+3,
     #        path_4FS_ttbb_SL,
     #        lumi+"*"+sel_ttb,
     #        'ttb_4FS_SL',
     #        samDict=sampleDict, readTrees=doReadTrees),

     #plotClasses.Sample('t#bar{t}+b (4FS,DL)',ROOT.kRed+3,
      #       path_4FS_ttbb_DL,
      #       lumi+"*"+sel_ttb,
      #       'ttb_4FS_DL',
      #       samDict=sampleDict, readTrees=doReadTrees),

     #plotClasses.Sample('t#bar{t}+b (4FS,FH)',ROOT.kRed+3,
     #        path_4FS_ttbb_FH,
     #        lumi+"*"+sel_ttb,
     #        'ttb_4FS_FH',
     #        samDict=sampleDict, readTrees=doReadTrees),



     #plotClasses.Sample('t#bar{t}+2b (4FS,SL)',ROOT.kRed+3,
     #        path_4FS_ttbb_SL,
     #        lumi+"*"+sel_tt2b,
     #        'tt2b_4FS_SL',
     #        samDict=sampleDict, readTrees=doReadTrees),

     #plotClasses.Sample('t#bar{t}+2b (4FS,DL)',ROOT.kRed+3,
     #        path_4FS_ttbb_DL,
     #        lumi+"*"+sel_tt2b,
     #        'tt2b_4FS_DL',
     #        samDict=sampleDict, readTrees=doReadTrees),

     #plotClasses.Sample('t#bar{t}+2b (4FS,FH)',ROOT.kRed+3,
     #        path_4FS_ttbb_FH,
     #        lumi+"*"+sel_tt2b,
     #        'tt2b_4FS_FH',
     #        samDict=sampleDict, readTrees=doReadTrees),


     #plotClasses.Sample('t#bar{t}+b#bar{b} (5FS)',ROOT.kRed+3,
     #        path_5FS_ttbar,
     #        lumi+"*"+sel_ttbb,
     #        'ttbb_5FS',
     #        samDict=sampleDict, readTrees=doReadTrees), 

     #plotClasses.Sample('t#bar{t}+b (5FS)',ROOT.kRed-2,
     #        path_5FS_ttbar,
     #        lumi+"*"+sel_ttb,
     #        'ttb_5FS',
     #        samDict=sampleDict, readTrees=doReadTrees),

     #plotClasses.Sample('t#bar{t}+2b (5FS)',ROOT.kRed+2,
     #        path_5FS_ttbar,
     #        lumi+"*"+sel_tt2b,
     #        'tt2b_5FS',
     #        samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+lf (SL)',ROOT.kRed-7,
            path_5FS_ttbar_SL,
            lumi+"*"+sel_ttlf,
            'ttlf_SL',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+lf (DL)',ROOT.kRed-7,
            path_5FS_ttbar_DL,
            lumi+"*"+sel_ttlf,
            'ttlf_DL',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+lf (FH)',ROOT.kRed-7,
            path_5FS_ttbar_FH,
            lumi+"*"+sel_ttlf,
            'ttlf_FH',
            samDict=sampleDict, readTrees=doReadTrees),



    plotClasses.Sample('t#bar{t}+c#bar{c} (SL)',ROOT.kRed+1,
            path_5FS_ttbar_SL,
            lumi+"*"+sel_ttcc,
            'ttcc_SL',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c} (DL)',ROOT.kRed+1,
            path_5FS_ttbar_DL,
            lumi+"*"+sel_ttcc,
            'ttcc_DL',
            samDict=sampleDict, readTrees=doReadTrees),

    plotClasses.Sample('t#bar{t}+c#bar{c} (FH)',ROOT.kRed+1,
            path_5FS_ttbar_FH,
            lumi+"*"+sel_ttcc,
            'ttcc_FH',
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
