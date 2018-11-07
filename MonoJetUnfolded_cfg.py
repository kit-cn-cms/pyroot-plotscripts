import sys
import os
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *

ExSystNames = ["",
    "_CMS_btag_lfUp", "_CMS_btag_lfDown", "_CMS_btag_hfUp", "_CMS_btag_hfDown",
    "_CMS_btag_hfstats1Up", "_CMS_btag_hfstats1Down", "_CMS_btag_lfstats1Up", "_CMS_btag_lfstats1Down",
    "_CMS_btag_hfstats2Up", "_CMS_btag_hfstats2Down", "_CMS_btag_lfstats2Up", "_CMS_btag_lfstats2Down",
    "_CMS_btag_cferr1Up", "_CMS_btag_cferr1Down", "_CMS_btag_cferr2Up", "_CMS_btag_cferr2Down",
    "_Weight_PUUp", "_Weight_PUDown",
    "_CMS_scale_jUp", "_CMS_scale_jDown",
    "_CMS_res_jUp", "_CMS_res_jDown"
]

EWTheorySystNames = ["",
    "_amc_scale_variation_muRUp", "_amc_scale_variation_muRDown",
    "_amc_scale_variation_muFUp", "_amc_scale_variation_muFDown",
]

madgraphTheorySystNames = ["",
    "_madgraph_scale_variation_muRUp", "_madgraph_scale_variation_muRDown",
    "_madgraph_scale_variation_muFUp", "_mpdgraph_scale_variation_muFDown",
]

powhegTheorySystNames = ["",
    "_powheg_scale_variation_muRUp", "_powheg_scale_variation_muRDown",
    "_powheg_scale_variation_muFUp", "_powheg_scale_variation_muFDown",
]

PDFSystNames = [
    "_Weight_PDFUp", "_Weight_PDFDown",
]

BosonSystNames = [
    "_BosonWeight_QCD1Up", "_BosonWeight_QCD1Down",
    "_BosonWeight_QCD2Up", "_BosonWeight_QCD2Down",
    "_BosonWeight_QCD3Up", "_BosonWeight_QCD3Down",
    "_BosonWeight_EW1Up", "_BosonWeight_EW1Down",
    "_BosonWeight_AlphaUp","_BosonWeight_AlphaDown",
]

ZvvBosonSystNames=[
    "_ZvvBosonWeight_EW2", "_ZvvBosonWeight_EW2Down",
    "_ZvvBosonWeight_EW3", "_ZvvBosonWeight_EW3Down",
    "_ZvvBosonWeight_MixedUp", "_ZvvBosonWeight_MixedDown",
]

WlnuBosonSystNames=[
    "_WlnuBosonWeight_EW2Up", "_WlnBosonWeight_EW2Down",
    "_WlnBosonWeight_EW3", "_WlnBosonWeight_EW3Down",
    "_WlnBosonWeight_MixedUp", "_WlnBosonWeight_MixedDown",
]

ZllBosonSystNames=[
    "_ZllBosonWeight_EW2Up", "_ZllBosonWeight_EW2Down",
    "_ZllBosonWeight_EW3", "_ZllBosonWeight_EW3Down",
    "_ZllBosonWeight_MixedUp", "_ZllBosonWeight_MixedDown",
]


unfoldedExtraSystNames = [
    "_DataStatUp", "_DataStatDown",
    # "_fakeStatUp", "_fakeStatDown",
    # "_fakeScaleUp", "_fakeScaleDown",
    # "_MCStatUp", "_MCStatDown"
]


MCSystnames = EWTheorySystNames + BosonSystNames
unfoldedSystNames =  ExSystNames + unfoldedExtraSystNames 
allSystnames=MCSystnames+ExSystNames

path_ntuples = "/nfs/dust/cms/user/mwassmer/DarkMatter/ntuples"
# path_ntuples = "/nfs/dust/cms/user/swieland/Darkmatter/ntuples"

sampleDict = SampleDictionary()
sampleDict.doPrintout()

sel_MET = "*(Triggered_HLT_PFMET170_X==1||Triggered_HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_X==1||Triggered_HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_X==1||Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_X==1||Triggered_HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_X==1)"

dummySys=[""]
dummypath=path_ntuples
dummyweight="1."

samples_unfolded = [
    Sample('unfolded', ROOT.kBlack, dummypath+"unfolded", dummyweight, 'unfolded', dummySys, samDict=sampleDict),
]

samples_data = [
    Sample('data',ROOT.kBlack, dummypath+"data",dummyweight,'data',[""],samDict=sampleDict),
]

samples_dataUnfolded = [
    Sample('unfolded data',ROOT.kBlack, dummypath+"data",dummyweight,'data',[""],samDict=sampleDict),
]

samples_background = [
    Sample('Z(#nu#nu)+jets', ROOT.kBlue, dummypath, dummyweight, 'z_nunu_jets', EWTheorySystNames + PDFSystNames + BosonSystNames + ZvvBosonSystNames, samDict=sampleDict),
    Sample('W(l#nu)+jets', ROOT.kGreen, dummypath, dummyweight, 'w_lnu_jets', EWTheorySystNames + PDFSystNames + BosonSystNames + WlnuBosonSystNames, samDict=sampleDict),
    Sample('Diboson', ROOT.kViolet, dummypath, dummyweight, 'diboson', dummySys, samDict=sampleDict),
    Sample('Single Top', ROOT.kViolet-1, dummypath, dummyweight, 'singletop', madgraphTheorySystNames, samDict=sampleDict),
    Sample('t#bar{t}', ROOT.kViolet-2, dummypath, dummyweight, 'ttbar', madgraphTheorySystNames + PDFSystNames , samDict=sampleDict),
    Sample('Z(ll)+jets', ROOT.kViolet-7, dummypath, dummyweight, 'z_ll_jets', EWTheorySystNames + PDFSystNames  + BosonSystNames + ZvvBosonSystNames, samDict=sampleDict),
    Sample('QCD', ROOT.kViolet+3, dummypath, dummyweight, 'qcd', powhegTheorySystNames, samDict=sampleDict),
    Sample('#gamma +jets', ROOT.kViolet+7, dummypath, dummyweight, 'gamma_jets', powhegTheorySystNames, samDict=sampleDict)
]


samples_signal = [
    Sample('Signal', ROOT.kRed,dummypath, dummySys, 'signal', dummySys, samDict=sampleDict),
]

samples_signalUnfolded = [
    Sample('Signal', ROOT.kRed,dummypath, dummySys, 'Axial_MonoJ_NLO_Mphi-1000_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph', dummySys, samDict=sampleDict),
    # Sample('Signal', ROOT.kRed,dummypath, dummySys, 'Axial_MonoJ_NLO_Mphi-1750_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph', dummySys, samDict=sampleDict),
]