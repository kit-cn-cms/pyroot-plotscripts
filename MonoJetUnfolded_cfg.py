import sys
import os
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *

weightSystNames = ["",
                   "_CMS_btag_lfUp", "_CMS_btag_lfDown", "_CMS_btag_hfUp", "_CMS_btag_hfDown",
                   "_CMS_btag_hfstats1Up", "_CMS_btag_hfstats1Down", "_CMS_btag_lfstats1Up", "_CMS_btag_lfstats1Down",
                   "_CMS_btag_hfstats2Up", "_CMS_btag_hfstats2Down", "_CMS_btag_lfstats2Up", "_CMS_btag_lfstats2Down",
                   "_CMS_btag_cferr1Up", "_CMS_btag_cferr1Down", "_CMS_btag_cferr2Up", "_CMS_btag_cferr2Down",
                   "_Weight_PUUp", "_WeightPUDown",
                   "_Weight_scale_variation_muRUp", "_Weight_scale_variation_muRDown", "_Weight_scale_variation_muFUp", "_Weight_scale_variation_muFDown",
                   ]

common_weight = "1.0*Weight_GEN_nom*Weight_CSV*Weight_pu69p2"

systWeights = ["NomWeight:="+common_weight+"*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVLFup:="+common_weight +
               "*Weight_CSVLFup*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVLFdown:="+common_weight +
               "*Weight_CSVLFdown*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVHFup:="+common_weight +
               "*Weight_CSVHFup*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVHFdown:="+common_weight +
               "*Weight_CSVHFdown*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVHFStats1up:="+common_weight +
               "*Weight_CSVHFStats1up*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVHFStats1down:="+common_weight +
               "*Weight_CSVHFStats1down*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVLFStats1up:="+common_weight +
               "*Weight_CSVLFStats1up*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVLFStats1down:="+common_weight +
               "*Weight_CSVLFStats1down*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVHFStats2up:="+common_weight +
               "*Weight_CSVHFStats2up*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVHFStats2down:="+common_weight +
               "*Weight_CSVHFStats2down*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVLFStats2up:="+common_weight +
               "*Weight_CSVLFStats2up*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVLFStats2down:="+common_weight +
               "*Weight_CSVLFStats2down*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVCErr1up:="+common_weight +
               "*Weight_CSVCErr1up*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVCErr1down:="+common_weight +
               "*Weight_CSVCErr1down*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVCErr2up:="+common_weight +
               "*Weight_CSVCErr2up*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_CSVCErr2down:="+common_weight +
               "*Weight_CSVCErr2down*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_PUup:="+common_weight +
               "*Weight_pu69p2Up/Weight_pu69p2*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_PUdown:="+common_weight +
               "*Weight_pu69p2Down/Weight_pu69p2*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_scale_variation_muRup:="+common_weight +
               "*fabs(Weight_scale_variation_muR_2p0_muF_1p0)*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_scale_variation_muRdown:="+common_weight +
               "*fabs(Weight_scale_variation_muR_0p5_muF_1p0)*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_scale_variation_muFup:="+common_weight +
               "*fabs(Weight_scale_variation_muR_1p0_muF_2p0)*(DoWeights==1)+(DoWeights==0)*1.0",
               "dummyWeight_scale_variation_muFdown:="+common_weight +
               "*fabs(Weight_scale_variation_muR_1p0_muF_0p5)*(DoWeights==1)+(DoWeights==0)*1.0",
               ]
otherSystNames = [
    "_CMS_scale_jUp", "_CMS_scale_jDown",
    "_CMS_res_jUp", "_CMS_res_jDown"
]
otherSystFileNames = [
    "JESup", "JESdown",
    "JERup", "JERdown"
]

MCWeight = '35.91823'

path_ntuples = "/nfs/dust/cms/user/mwassmer/DarkMatter/ntuples"
# path_ntuples = "/nfs/dust/cms/user/swieland/Darkmatter/ntuples"

sampleDict = SampleDictionary()
sampleDict.doPrintout()

sel_MET = "*(Triggered_HLT_PFMET170_X==1||Triggered_HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_X==1||Triggered_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_X==1||Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_X==1||Triggered_HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_X==1)"

samples_unfolded = [
    Sample('unfolded', ROOT.kBlack, path_ntuples+'/MET_Run2016*/*nominal*.root',
           "1."+sel_MET, 'unfolded', [""], samDict=sampleDict),
]

samples_background = [
    Sample('Z(#nu#nu)+jets', ROOT.kBlue, path_ntuples+'/DYJetsToNuNu_PtZ-*/*nominal*.root', "1.*3*0.971" +
           "*"+MCWeight+sel_MET, 'z_nunu_jets', weightSystNames+otherSystNames, samDict=sampleDict),
    Sample('W(l#nu)+jets', ROOT.kGreen, path_ntuples+'/WJetsToLNu_Pt-*/*nominal*.root', "1.*" +
           MCWeight+sel_MET, 'w_lnu_jets', weightSystNames+otherSystNames, samDict=sampleDict),
    Sample('Diboson', ROOT.kViolet, path_ntuples+'/??_TuneCUETP8M1_13TeV-pythia8/*nominal*.root',
           "1."+"*"+MCWeight+sel_MET, 'diboson', weightSystNames[:-4]+otherSystNames, samDict=sampleDict),
    Sample('Single Top', ROOT.kViolet-1, path_ntuples+'/ST*/*nominal*.root', "1."+"*" +
           MCWeight+sel_MET, 'singletop', weightSystNames[:-4]+otherSystNames, samDict=sampleDict),
    Sample('t#bar{t}', ROOT.kViolet-2, path_ntuples+'/TT_Tune*/*nominal*.root', "1."+"*" +
           MCWeight+sel_MET, 'ttbar', weightSystNames[:-4]+otherSystNames, samDict=sampleDict),
    Sample('Z(ll)+jets', ROOT.kViolet-7, path_ntuples+'/DYJetsToLL*/*nominal*.root', "1."+"*" +
           MCWeight+sel_MET, 'z_ll_jets', weightSystNames[:-4]+otherSystNames, samDict=sampleDict),
    Sample('QCD', ROOT.kViolet+3, path_ntuples+'/QCD*/*nominal*.root', "1."+"*" +
           MCWeight+sel_MET, 'qcd', weightSystNames[:-4]+otherSystNames, samDict=sampleDict),
    Sample('#gamma +jets', ROOT.kViolet+7, path_ntuples+'/GJets*/*nominal*.root', "1."+"*" +
           MCWeight+sel_MET, 'gamma_jets', weightSystNames[:-4]+otherSystNames, samDict=sampleDict)
]

samples_signal = [
    Sample('signal', ROOT.kRed, path_ntuples+'/DMV_NNPDF30_Axial_Mphi-1000_Mchi-300_gSM-0p25_gDM-1p0_v2_13TeV-powheg/*nominal*.root',
           "1."+"*"+MCWeight+sel_MET, 'signal', weightSystNames[:-4], samDict=sampleDict),
]
