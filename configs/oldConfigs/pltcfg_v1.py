import sys
import os
import ROOT
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses

sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1 && (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1))*(N_Jets>=4 && N_BTagsM>=3)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0 && N_TightMuons==1 && (Triggered_HLT_IsoMu27_vX==1))*(N_Jets>=4 && N_BTagsM>=3)*(Muon_Pt[0]>29.)" # and vice versa...
sel_MET="*(Evt_Pt_MET>20.)"
#sel_MET="*1.0"
sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'

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

# names of the systematics (proper names needed e.g. for combination)
# TODO Add CSV SFs and uncertainties
weightSystNames=[
                    "",
                   "_CMS_btag_lf_2017Up","_CMS_btag_lf_2017Down","_CMS_btag_hf_2017Up","_CMS_btag_hf_2017Down",
                   "_CMS_btag_hfstats1_2017Up","_CMS_btag_hfstats1_2017Down","_CMS_btag_lfstats1_2017Up","_CMS_btag_lfstats1_2017Down",
                   "_CMS_btag_hfstats2_2017Up","_CMS_btag_hfstats2_2017Down","_CMS_btag_lfstats2_2017Up","_CMS_btag_lfstats2_2017Down",
                   "_CMS_btag_cferr1_2017Up","_CMS_btag_cferr1_2017Down","_CMS_btag_cferr2_2017Up","_CMS_btag_cferr2_2017Down",
                  "_CMS_effTrigger_e_2017Up","_CMS_effTrigger_e_2017Down",  
                   "_CMS_effTrigger_m_2017Up","_CMS_effTrigger_m_2017Down",  
                   "_CMS_eff_e_2017Up","_CMS_eff_e_2017Down", 
                   "_CMS_eff_m_2017Up","_CMS_eff_m_2017Down",
                   "_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",
]

systsAllSamples=[
                    "",
                   "_CMS_btag_lf_2017Up","_CMS_btag_lf_2017Down","_CMS_btag_hf_2017Up","_CMS_btag_hf_2017Down",
                   "_CMS_btag_hfstats1_2017Up","_CMS_btag_hfstats1_2017Down","_CMS_btag_lfstats1_2017Up","_CMS_btag_lfstats1_2017Down",
                   "_CMS_btag_hfstats2_2017Up","_CMS_btag_hfstats2_2017Down","_CMS_btag_lfstats2_2017Up","_CMS_btag_lfstats2_2017Down",
                   "_CMS_btag_cferr1_2017Up","_CMS_btag_cferr1_2017Down","_CMS_btag_cferr2_2017Up","_CMS_btag_cferr2_2017Down",
                  "_CMS_effTrigger_e_2017Up","_CMS_effTrigger_e_2017Down",  
                   "_CMS_effTrigger_m_2017Up","_CMS_effTrigger_m_2017Down",  
                    "_CMS_eff_e_2017Up","_CMS_eff_e_2017Down", 
                   "_CMS_eff_m_2017Up","_CMS_eff_m_2017Down",  
                   "_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",

]

systs_tt_all= [
]

systs_tt_lf=[]
systs_tt_b=[]
systs_tt_2b=[]
systs_tt_bb=[]
systs_tt_cc=[]



mcWeightAll='41.53'
mcWeight='41.53*2.0'

# TODO Add Trigger SFs
mcTriggerWeight='((1.0) * (internalEleTriggerWeight*(N_LooseMuons==0 && N_TightElectrons==1)* (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1) +internalMuTriggerWeight*(N_LooseElectrons==0 && N_TightMuons==1)*(Muon_Pt[0]>29.) *(Triggered_HLT_IsoMu27_vX==1)))*(N_Jets>=4 && N_BTagsM>=3)'
#mcTriggerWeight='(1.0)'
#mcTriggerWeight='((1.0) * (1*(N_LooseMuons==0 && N_TightElectrons==1)* (1) +1*(N_LooseElectrons==0 && N_TightMuons==1) *(1)))*(N_Jets>=4 && N_BTagsM>=3)'

#TODO Check that SFs and uncertainties are correct
sfs="1.0"
sfs="internalEleIDWeight*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeight"
#sfs="internalEleIDWeight*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeight*internalMuHIPWeight"
#sfs="1.0"

usualWeights="(1*Weight_pu69p2*Weight_GEN_nom)"+"*"+sfs
#usualWeights="(1*(Weight_GEN_nom))"+"*"+sfs

evenSel="*(Evt_Odd==0)"


#ttbarMCWeight='*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))'
#ttbarMCWeight='*0.0084896859/Weight_XS'

systWeights=[
                    "NomWeight:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFup:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFUp*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFdown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFDown*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFup:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFUp*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFdown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFDown*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFStats1up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats1Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFStats1down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats1Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFStats1up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats1Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFStats1down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats1Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFStats2up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats2Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVHFStats2down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats2Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFStats2up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats2Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVLFStats2down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats2Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVCErr1up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr1Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVCErr1down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr1Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVCErr2up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr2Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   "dummyWeight_CSVCErr2down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr2Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   
                   "dummyWeight_CMS_ttH_PUUp:="+"(1*Weight_pu69p2Up*Weight_GEN_nom*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",

                   "dummyWeight_CMS_ttH_PUDown:="+"(1*Weight_pu69p2Down*Weight_GEN_nom*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",

                   "dummyWeight_CMS_ttH_ljets_Trig_elUp:="+usualWeights+"*"+'((1.0) * (internalEleTriggerWeightUp*(N_LooseMuons==0 && N_TightElectrons==1)* (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1) +internalMuTriggerWeight*(N_LooseElectrons==0 && N_TightMuons==1)*(Muon_Pt[0]>29.) *(Triggered_HLT_IsoMu27_vX==1)))*(N_Jets>=4 && N_BTagsM>=3)'+"*internalCSVweight*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ljets_Trig_elDown:="+usualWeights+"*"+'((1.0) * (internalEleTriggerWeightDown*(N_LooseMuons==0 && N_TightElectrons==1)* (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1) +internalMuTriggerWeight*(N_LooseElectrons==0 && N_TightMuons==1)*(Muon_Pt[0]>29.) *(Triggered_HLT_IsoMu27_vX==1)))*(N_Jets>=4 && N_BTagsM>=3)'+"*internalCSVweight*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ljets_Trig_muUp:="+usualWeights+"*"+'((1.0) * (internalEleTriggerWeight*(N_LooseMuons==0 && N_TightElectrons==1)* (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1) +internalMuTriggerWeightUp*(N_LooseElectrons==0 && N_TightMuons==1)*(Muon_Pt[0]>29.) *(Triggered_HLT_IsoMu27_vX==1)))*(N_Jets>=4 && N_BTagsM>=3)'+"*internalCSVweight*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ljets_Trig_muDown:="+usualWeights+"*"+'((1.0) * (internalEleTriggerWeight*(N_LooseMuons==0 && N_TightElectrons==1)* (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1) +internalMuTriggerWeightDown*(N_LooseElectrons==0 && N_TightMuons==1)*(Muon_Pt[0]>29.) *(Triggered_HLT_IsoMu27_vX==1)))*(N_Jets>=4 && N_BTagsM>=3)'+"*internalCSVweight*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_eff_elUp:="+"(1*Weight_pu69p2*Weight_GEN_nom)"+"*"+"internalEleIDWeightUp*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeightUp"+"*"+mcTriggerWeight+"*internalCSVweight*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_eff_elDown:="+"(1*Weight_pu69p2*Weight_GEN_nom)"+"*"+"internalEleIDWeightDown*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeightDown"+"*"+mcTriggerWeight+"*internalCSVweight*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                     "dummyWeight_CMS_ttH_eff_muUp:="+"(1*Weight_pu69p2*Weight_GEN_nom)"+"*"+"internalEleIDWeight*internalMuIDWeightUp*internalMuIsoWeightUp*internalEleGFSWeight"+"*"+mcTriggerWeight+"*internalCSVweight*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_eff_muDown:="+"(1*Weight_pu69p2*Weight_GEN_nom)"+"*"+"internalEleIDWeight*internalMuIDWeightDown*internalMuIsoWeightDown*internalEleGFSWeight"+"*"+mcTriggerWeight+"*internalCSVweight*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeightPileUpUp:="+"(1*Weight_pu69p2Up*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeightPileUpDown:="+"(1*Weight_pu69p2Down*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeightPileUpUp:="+"(1*Weight_pu69p2Up*(Weight_GEN_nom))"+"*"+sfs+"*"+mcTriggerWeight+"*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeightPileUpDown:="+"(1*Weight_pu69p2Down*(Weight_GEN_nom))"+"*"+sfs+"*"+mcTriggerWeight+"*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeightQCDScaleFactor_=
]


assert len(weightSystNames)==len(systWeights)


systs_tt_and_ttH=[
  ]

systs_tt_and_ttH_weights=[
                    
                    ]

systs_ttH=[
  ]

systs_ttH_weights=[
                    ]


systs_tt_all=[
  ]

systs_tt_all_weights=[
                    ]



systs_tt_lf=[
  ]
systs_tt_lf_weights=[
                    ]

systs_tt_b=[
  ]
systs_tt_b_weights=[
                    ]

systs_tt_2b=[
  ]
systs_tt_2b_weights=[
                ]

systs_tt_bb=[
  ]
systs_tt_bb_weights=[
                ]

systs_tt_cc=[
  ]
systs_tt_cc_weights=[
                    ]

systWeights+=systs_tt_all_weights+systs_tt_lf_weights+systs_tt_b_weights+systs_tt_2b_weights+systs_tt_bb_weights+systs_tt_cc_weights+systs_tt_and_ttH_weights+systs_ttH_weights
weightSystNames+=systs_tt_all+systs_tt_lf+systs_tt_b+systs_tt_2b+systs_tt_bb+systs_tt_cc+systs_tt_and_ttH+systs_ttH
print systWeights
print weightSystNames

assert len(systWeights)==len(weightSystNames)

otherSystNames=[
]

otherSystFileNames=[
]

for i,j in zip(otherSystNames,otherSystFileNames):
    print i, j
assert len(otherSystNames)==len(otherSystFileNames)




#assert len(errorSystNames)==len(weightSystNames+otherSystNames+PSSystNames+QCDSystNames)

# samples
# input path 
path_karim_new="/nfs/dust/cms/user/kelmorab/ttH_2018/ntuples_v5"
path_mwassmer="/nfs/dust/cms/user/kelmorab/ttH_2018/ntuples_v5"
ttbarPathS=path_karim_new+'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_v2/*nominal*.root'+';'+path_karim_new+'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx/*nominal*.root'+';'+path_karim_new+'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'
VJetsPathS=path_karim_new+'/DYJets*/*nominal*.root'+';'+path_karim_new+'/WJets*/*nominal*.root'
ttVPathS=path_karim_new+'/TTW*/*nominal*.root'+';'+path_karim_new+'/TTZ*/*nominal*.root'
dibosonPathS=path_karim_new+'/WW_*/*nominal*.root'+';'+path_karim_new+'/WZ_*/*nominal*.root'+';'+path_karim_new+'/ZZ_*/*nominal*.root'
stpath=path_karim_new+'/ST_*/*nominal*.root'
ttHpath=path_karim_new+'/ttHTo*/*nominal*.root'


hdamp_ue_systnames_tt_all = [
]
hdamp_ue_filenames_tt_all = [
]


hdamp_ue_systnames_tt_lf = [
]
hdamp_ue_filenames_tt_lf = [
]

hdamp_ue_systnames_tt_bb = [
]
hdamp_ue_filenames_tt_bb = [
]

hdamp_ue_systnames_tt_2b = [
]
hdamp_ue_filenames_tt_2b = [
]

hdamp_ue_systnames_tt_b = [
]
hdamp_ue_filenames_tt_b = [
]

hdamp_ue_systnames_tt_cc = [
]
hdamp_ue_filenames_tt_cc = [
]




errorSystNames=[
                    "",

]+systs_tt_lf+systs_tt_cc+systs_tt_b+systs_tt_2b+systs_tt_bb+hdamp_ue_systnames_tt_lf+hdamp_ue_systnames_tt_cc+hdamp_ue_systnames_tt_b+hdamp_ue_systnames_tt_2b+hdamp_ue_systnames_tt_bb

otherSystNames+=hdamp_ue_systnames_tt_lf+hdamp_ue_systnames_tt_cc+hdamp_ue_systnames_tt_b+hdamp_ue_systnames_tt_2b+hdamp_ue_systnames_tt_bb

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
sampleDict=plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees=True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
                    plotClasses.Sample('SingleMu',ROOT.kBlack,path_karim_new+'/SingleMuon*/*nominal*.root',sel_singlemu+sel_MET,'SingleMu',samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('SingleEl',ROOT.kBlack,path_karim_new+'/SingleElectron*/*nominal*.root',sel_singleel+sel_MET,'SingleEl',samDict=sampleDict, readTrees=doReadTrees)
]


print "controlsamples"
samplesControlPlots=[
                    plotClasses.Sample('t#bar{t}H',ROOT.kBlue+1,path_mwassmer+'/ttH*/*nominal*.root',mcWeightAll+sel_MET,'ttH',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,     
                    
                    plotClasses.Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,'ttbarOther',systsAllSamples+systs_tt_all+systs_tt_lf+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_lf,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusCC==1)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusCCbar',systsAllSamples+systs_tt_all+systs_tt_cc+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_cc,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==1)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusB',systsAllSamples+systs_tt_all+systs_tt_b+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_b,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==2)'+sel_MET+sel_StrangeMuWeights,'ttbarPlus2B',systsAllSamples+systs_tt_all+systs_tt_2b+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_2b,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==3)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusBBbar',systsAllSamples+systs_tt_all+systs_tt_bb+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_bb,samDict=sampleDict, readTrees=doReadTrees), 
                    
                    plotClasses.Sample('Single Top',ROOT.kMagenta,stpath,mcWeightAll+sel_MET,'singlet',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    plotClasses.Sample('V+jets',ROOT.kGreen-3,VJetsPathS,mcWeightAll+sel_MET,'Vjets',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    plotClasses.Sample('t#bar{t}+V',ROOT.kBlue-10,ttVPathS,mcWeightAll+sel_MET,'ttV',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees),         
                    plotClasses.Sample('Diboson',ROOT.kAzure+2,dibosonPathS,mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    #plotClasses.Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict, readTrees=doReadTrees),  
]

#print "limit samples"
samplesLimits=[
                    plotClasses.Sample('t#bar{t}H',ROOT.kBlue+1,path_mwassmer+'/ttH*/*nominal*.root',mcWeight+evenSel+sel_MET,'ttH',systsAllSamples+systs_ttH+systs_tt_and_ttH  ,samDict=sampleDict, readTrees=doReadTrees) ,     
                    plotClasses.Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_mwassmer+'/ttHTobb*/*nominal*.root','1.0*'+mcWeight+evenSel+sel_MET,'ttH_hbb',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    plotClasses.Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hccSel+sel_MET,'ttH_hcc',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    plotClasses.Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+httSel+sel_MET,'ttH_htt',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    plotClasses.Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hggSel+sel_MET,'ttH_hgg',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    plotClasses.Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hglugluSel+sel_MET,'ttH_hgluglu',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    plotClasses.Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hwwSel+sel_MET,'ttH_hww',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    plotClasses.Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hzzSel+sel_MET,'ttH_hzz',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    plotClasses.Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hzgSel+sel_MET,'ttH_hzg',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,
                    
                    plotClasses.Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,'ttbarOther',systsAllSamples+systs_tt_all+systs_tt_lf+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_lf,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusCC==1)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusCCbar',systsAllSamples+systs_tt_all+systs_tt_cc+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_cc,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==1)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusB',systsAllSamples+systs_tt_all+systs_tt_b+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_b,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==2)'+sel_MET+sel_StrangeMuWeights,'ttbarPlus2B',systsAllSamples+systs_tt_all+systs_tt_2b+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_2b,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==3)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusBBbar',systsAllSamples+systs_tt_all+systs_tt_bb+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_bb,samDict=sampleDict, readTrees=doReadTrees), 
                    
                    plotClasses.Sample('Single Top',ROOT.kMagenta,stpath,mcWeightAll+sel_MET,'singlet',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    plotClasses.Sample('Z+jets',ROOT.kGreen-3,path_karim_new+'/DYJets*/*nominal*.root',mcWeightAll+sel_MET,'zjets',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    plotClasses.Sample('W+jets',ROOT.kGreen-7,path_karim_new+'/WJets*/*nominal*.root',mcWeightAll+sel_MET,'wjets',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    plotClasses.Sample('t#bar{t}+W',ROOT.kBlue-10,path_karim_new+'/TTW*/*nominal*.root',mcWeightAll+sel_MET,'ttbarW',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('t#bar{t}+Z',ROOT.kBlue-6,path_karim_new+'/TTZ*/*nominal*.root',mcWeightAll+sel_MET,'ttbarZ',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('Diboson',ROOT.kAzure+2,dibosonPathS,mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    #plotClasses.Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict, readTrees=doReadTrees),  
]

