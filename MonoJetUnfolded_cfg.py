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

commonTheorySystNames = ["",
    "_Weight_scale_variation_muRUp", "_Weight_scale_variation_muRDown",
    "_Weight_scale_variation_muFUp", "_Weight_scale_variation_muFDown",
    ]

otherSystNames = [
    "_CMS_scale_jUp", "_CMS_scale_jDown",
    "_CMS_res_jUp", "_CMS_res_jDown"
]

WBosonSystNames = [
    "_WbosonWeight_QCD1Up", "_WbosonWeight_QCD1Down",
    "_WbosonWeight_QCD2Up", "_WbosonWeight_QCD2Down",
    "_WbosonWeight_QCD3Up", "_WbosonWeight_QCD3Down",
    "_WbosonWeight_EW1Up", "_WbosonWeight_EW1Down",
    "_WbosonWeight_EW2Up", "_WbosonWeight_EW2Down",
    "_WbosonWeight_EW3Up", "_WbosonWeight_EW3Down",
    "_WbosonWeight_MixedUp", "_WbosonWeight_MixedDown",
    "_WbosonWeight_AlphaUp","_WbosonWeight_AlphaDown",

]

ZBosonSystNames = [
    "_ZbosonWeight_QCD1Up", "_ZbosonWeight_QCD1Down",
    "_ZbosonWeight_QCD2Up", "_ZbosonWeight_QCD2Down",
    "_ZbosonWeight_QCD3Up", "_ZbosonWeight_QCD3Down",
    "_ZbosonWeight_EW1Up",  "_ZbosonWeight_EW1Down",
    "_ZbosonWeight_EW2Up",  "_ZbosonWeight_EW2Down",
    "_ZbosonWeight_EW3Up",  "_ZbosonWeight_EW3Down",
    "_ZbosonWeight_MixedUp","_ZbosonWeight_MixedDown",
    "_ZbosonWeight_AlphaUp","_ZbosonWeight_AlphaDown",
]

unfoldedExtraSystNames = [
    "_DataStatUp", "_DataStatDown",
    "_fakeStatUp", "_fakeStatDown",
    "_fakeScaleUp", "_fakeScaleDown",
    "_MCStatUp", "_MCStatDown"
]


BosonSystNames = ZBosonSystNames+WBosonSystNames

MCSystnames = commonTheorySystNames + BosonSystNames
unfoldedSystNames =  ExSystNames + unfoldedExtraSystNames +MCSystnames 

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

samples_background = [
    Sample('Z(#nu#nu)+jets', ROOT.kBlue, dummypath, dummyweight, 'z_nunu_jets', commonTheorySystNames + ZBosonSystNames, samDict=sampleDict),
    Sample('W(l#nu)+jets', ROOT.kGreen, dummypath, dummyweight, 'w_lnu_jets', commonTheorySystNames + WBosonSystNames, samDict=sampleDict),
    Sample('Diboson', ROOT.kViolet, dummypath, dummyweight, 'diboson', dummySys, samDict=sampleDict),
    Sample('Single Top', ROOT.kViolet-1, dummypath, dummyweight, 'singletop', dummySys, samDict=sampleDict),
    Sample('t#bar{t}', ROOT.kViolet-2, dummypath, dummyweight, 'ttbar', dummySys, samDict=sampleDict),
    Sample('Z(ll)+jets', ROOT.kViolet-7, dummypath, dummyweight, 'z_ll_jets', dummySys, samDict=sampleDict),
    Sample('QCD', ROOT.kViolet+3, dummypath, dummyweight, 'qcd', dummySys, samDict=sampleDict),
    Sample('#gamma +jets', ROOT.kViolet+7, dummypath, dummyweight, 'gamma_jets', dummySys, samDict=sampleDict)
]


samples_signal = [
    Sample('signal', ROOT.kRed,dummypath, dummySys, 'signal', dummySys, samDict=sampleDict),
]
