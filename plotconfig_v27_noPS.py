import sys
import os
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *

sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1 && (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1))*(N_Jets>=4 && N_BTagsM>=2)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0 && N_TightMuons==1 && (Triggered_HLT_IsoMu27_vX==1))*(N_Jets>=4 && N_BTagsM>=2)*(Muon_Pt[0]>29.)" # and vice versa...
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
                   "_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   "_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   "_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   "_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
                  #"_CMS_effTrigger_eUp","_CMS_effTrigger_eDown",  
                   #"_CMS_effTrigger_mUp","_CMS_effTrigger_mDown",  
                   #"_CMS_eff_eUp","_CMS_eff_eDown", 
                   #"_CMS_eff_mUp","_CMS_eff_mDown",
                   "_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",
]

systsAllSamples=[
                    "",
                   "_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   "_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   "_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   "_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
                  #"_CMS_effTrigger_eUp","_CMS_effTrigger_eDown",  
                   #"_CMS_effTrigger_mUp","_CMS_effTrigger_mDown",  
                    #"_CMS_eff_eUp","_CMS_eff_eDown", 
                   #"_CMS_eff_mUp","_CMS_eff_mDown",  
                   "_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",

    #"_CMS_scale_jUp","_CMS_scale_jDown",
    "_CMS_res_jUp","_CMS_res_jDown",
    "_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
    "_CMS_scaleAbsoluteScale_jUp","_CMS_scaleAbsoluteScale_jDown",
    ##"_CMS_scaleAbsoluteFlavMap_jUp","_CMS_scaleAbsoluteFlavMap_jDown",
    "_CMS_scaleAbsoluteMPFBias_jUp","_CMS_scaleAbsoluteMPFBias_jDown",
    "_CMS_scaleFragmentation_jUp","_CMS_scaleFragmentation_jDown",
    "_CMS_scaleSinglePionECAL_jUp","_CMS_scaleSinglePionECAL_jDown",
    "_CMS_scaleSinglePionHCAL_jUp","_CMS_scaleSinglePionHCAL_jDown",
    "_CMS_scaleFlavorQCD_jUp","_CMS_scaleFlavorQCD_jDown",
    "_CMS_scaleTimePtEta_jUp","_CMS_scaleTimePtEta_jDown",
    "_CMS_scaleRelativeJEREC1_jUp","_CMS_scaleRelativeJEREC1_jDown",
    "_CMS_scaleRelativeJEREC2_jUp","_CMS_scaleRelativeJEREC2_jDown",
    "_CMS_scaleRelativeJERHF_jUp","_CMS_scaleRelativeJERHF_jDown",
    "_CMS_scaleRelativePtBB_jUp","_CMS_scaleRelativePtBB_jDown",
    "_CMS_scaleRelativePtEC1_jUp","_CMS_scaleRelativePtEC1_jDown",
    "_CMS_scaleRelativePtEC2_jUp","_CMS_scaleRelativePtEC2_jDown",
    "_CMS_scaleRelativePtHF_jUp","_CMS_scaleRelativePtHF_jDown",
    "_CMS_scaleRelativeBal_jUp","_CMS_scaleRelativeBal_jDown",
    "_CMS_scaleRelativeFSR_jUp","_CMS_scaleRelativeFSR_jDown",
    "_CMS_scaleRelativeStatFSR_jUp","_CMS_scaleRelativeStatFSR_jDown",
    "_CMS_scaleRelativeStatEC_jUp","_CMS_scaleRelativeStatEC_jDown",
    "_CMS_scaleRelativeStatHF_jUp","_CMS_scaleRelativeStatHF_jDown",
    "_CMS_scalePileUpDataMC_jUp","_CMS_scalePileUpDataMC_jDown",
    "_CMS_scalePileUpPtRef_jUp","_CMS_scalePileUpPtRef_jDown",
    "_CMS_scalePileUpPtBB_jUp","_CMS_scalePileUpPtBB_jDown",
    "_CMS_scalePileUpPtEC1_jUp","_CMS_scalePileUpPtEC1_jDown",
    "_CMS_scalePileUpPtEC2_jUp","_CMS_scalePileUpPtEC2_jDown",
    "_CMS_scalePileUpPtHF_jUp","_CMS_scalePileUpPtHF_jDown",
]

systs_tt_all= [
]

systs_tt_lf=[]
systs_tt_b=[]
systs_tt_2b=[]
systs_tt_bb=[]
systs_tt_cc=[]



mcWeightAll='41.298'
mcWeight='41.298*2.0'

# TODO Add Trigger SFs
mcTriggerWeight='((1.0) * (internalEleTriggerWeight*(N_LooseMuons==0 && N_TightElectrons==1)* (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1) +internalMuTriggerWeight*(N_LooseElectrons==0 && N_TightMuons==1)*(Muon_Pt[0]>29.) *(Triggered_HLT_IsoMu27_vX==1)))*(N_Jets>=4 && N_BTagsM>=2)'
#mcTriggerWeight='(1.0)'
#mcTriggerWeight='((1.0) * (1*(N_LooseMuons==0 && N_TightElectrons==1)* (1) +1*(N_LooseElectrons==0 && N_TightMuons==1) *(1)))*(N_Jets>=4 && N_BTagsM>=2)'

#TODO Check that SFs and uncertainties are correct
sfs="1.0"
sfs="internalEleIDWeight*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeight"
#sfs="internalEleIDWeight*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeight*internalMuHIPWeight"
#sfs="1.0"

usualWeights="(1*Weight_pu69p2*Weight_GEN_nom*((Weight>0)-(Weight<0)))"+"*"+sfs
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

                   #"dummyWeight_CMS_ttH_ljets_Trig_elUp:="+usualWeights+"*"+"((1.0)*(internalEleTriggerWeightUp*internalMuTriggerWeight)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))) )"+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ljets_Trig_elDown:="+usualWeights+"*"+"((1.0)*(internalEleTriggerWeightDown*internalMuTriggerWeight)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))) )"+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ljets_Trig_muUp:="+usualWeights+"*"+"((1.0)*(internalEleTriggerWeight*internalMuTriggerWeightUp)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))) )"+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ljets_Trig_muDown:="+usualWeights+"*"+"((1.0)*(internalEleTriggerWeight*internalMuTriggerWeightDown)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))) )"+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_eff_elUp:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))*internalEleIDWeightUp*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeightUp*internalMuHIPWeight*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_eff_elDown:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))"+"*internalEleIDWeightDown*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeightDown*internalMuHIPWeight*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                     #"dummyWeight_CMS_ttH_eff_muUp:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))"+"*internalEleIDWeight*internalMuIDWeightUp*internalMuIsoWeightUp*internalEleGFSWeight*internalMuHIPWeightUp*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_eff_muDown:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))"+"*internalEleIDWeight*internalMuIDWeightDown*internalMuIsoWeightDown*internalEleGFSWeight*internalMuHIPWeightDown*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeightPileUpUp:="+"(1*Weight_pu69p2Up*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeightPileUpDown:="+"(1*Weight_pu69p2Down*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeightPileUpUp:="+"(1*Weight_pu69p2Up*(Weight_GEN_nom))"+"*"+sfs+"*"+mcTriggerWeight+"*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeightPileUpDown:="+"(1*Weight_pu69p2Down*(Weight_GEN_nom))"+"*"+sfs+"*"+mcTriggerWeight+"*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeightQCDScaleFactor_=
]


assert len(weightSystNames)==len(systWeights)

systs_tt_all=[
  #"_CMS_ttHbb_ttbar_NNPDFUp","_CMS_ttHbb_ttbar_NNPDFDown",
  "_CMS_ttHbb_ttbar_scaleMuRUp","_CMS_ttHbb_ttbar_scaleMuRDown",
  "_CMS_ttHbb_ttbar_scaleMuFUp","_CMS_ttHbb_ttbar_scaleMuFDown",
  #"_CMS_ttHbb_ttbar_ISRUp","_CMS_ttHbb_ttbar_ISRDown",
  #"_CMS_ttHbb_ttbar_FSRUp","_CMS_ttHbb_ttbar_FSRDown",
  
  
  ]

systs_tt_all_weights=[
                    #"dummyWeight_CMS_ttH_ttbar_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbar_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbar_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbar_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbar_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbar_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbar_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ttbar_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbar_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbar_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    ]



systs_tt_lf=[
    #"_CMS_ttHbb_ttbarOther_NNPDFUp","_CMS_ttHbb_ttbarOther_NNPDFDown",
  "_CMS_ttHbb_ttbarOther_scaleMuRUp","_CMS_ttHbb_ttbarOther_scaleMuRDown",
  "_CMS_ttHbb_ttbarOther_scaleMuFUp","_CMS_ttHbb_ttbarOther_scaleMuFDown",
  #"_CMS_ttHbb_ttbarOther_ISRUp","_CMS_ttHbb_ttbarOther_ISRDown",
  #"_CMS_ttHbb_ttbarOther_FSRUp","_CMS_ttHbb_ttbarOther_FSRDown",
  
  ]
systs_tt_lf_weights=[
                    #"dummyWeight_CMS_ttH_ttbarOther_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarOther_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbarOther_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbarOther_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbarOther_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbarOther_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarOther_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ttbarOther_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarOther_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarOther_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    ]
systs_tt_b=[
    #"_CMS_ttHbb_ttbarPlusB_NNPDFUp","_CMS_ttHbb_ttbarPlusB_NNPDFDown",
  "_CMS_ttHbb_ttbarPlusB_scaleMuRUp","_CMS_ttHbb_ttbarPlusB_scaleMuRDown",
  "_CMS_ttHbb_ttbarPlusB_scaleMuFUp","_CMS_ttHbb_ttbarPlusB_scaleMuFDown",
  #"_CMS_ttHbb_ttbarPlusB_ISRUp","_CMS_ttHbb_ttbarPlusB_ISRDown",
  #"_CMS_ttHbb_ttbarPlusB_FSRUp","_CMS_ttHbb_ttbarPlusB_FSRDown",
  ]
systs_tt_b_weights=[
                    #"dummyWeight_CMS_ttH_ttbarPlusB_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusB_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbarPlusB_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbarPlusB_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbarPlusB_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbarPlusB_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarPlusB_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ttbarPlusB_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarPlusB_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusB_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    ]
systs_tt_2b=[
    #"_CMS_ttHbb_ttbarPlus2B_NNPDFUp","_CMS_ttHbb_ttbarPlus2B_NNPDFDown",
  "_CMS_ttHbb_ttbarPlus2B_scaleMuRUp","_CMS_ttHbb_ttbarPlus2B_scaleMuRDown",
  "_CMS_ttHbb_ttbarPlus2B_scaleMuFUp","_CMS_ttHbb_ttbarPlus2B_scaleMuFDown",
  #"_CMS_ttHbb_ttbarPlus2B_ISRUp","_CMS_ttHbb_ttbarPlus2B_ISRDown",
  #"_CMS_ttHbb_ttbarPlus2B_FSRUp","_CMS_ttHbb_ttbarPlus2B_FSRDown",
  ]
systs_tt_2b_weights=[
                    #"dummyWeight_CMS_ttH_ttbarPlus2B_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlus2B_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbarPlus2B_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbarPlus2B_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbarPlus2B_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbarPlus2B_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarPlus2B_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ttbarPlus2B_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarPlus2B_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlus2B_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                ]
systs_tt_bb=[
    #"_CMS_ttHbb_ttbarPlusBBbar_NNPDFUp","_CMS_ttHbb_ttbarPlusBBbar_NNPDFDown",
  "_CMS_ttHbb_ttbarPlusBBbar_scaleMuRUp","_CMS_ttHbb_ttbarPlusBBbar_scaleMuRDown",
  "_CMS_ttHbb_ttbarPlusBBbar_scaleMuFUp","_CMS_ttHbb_ttbarPlusBBbar_scaleMuFDown",
  #"_CMS_ttHbb_ttbarPlusBBbar_ISRUp","_CMS_ttHbb_ttbarPlusBBbar_ISRDown",
  #"_CMS_ttHbb_ttbarPlusBBbar_FSRUp","_CMS_ttHbb_ttbarPlusBBbar_FSRDown",
  ]
systs_tt_bb_weights=[
                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbarPlusBBbar_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbarPlusBBbar_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbarPlusBBbar_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbarPlusBBbar_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ttbarPlusBBbar_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                ]
systs_tt_cc=[
    #"_CMS_ttHbb_ttbarPlusCCbar_NNPDFUp","_CMS_ttHbb_ttbarPlusCCbar_NNPDFDown",
  "_CMS_ttHbb_ttbarPlusCCbar_scaleMuRUp","_CMS_ttHbb_ttbarPlusCCbar_scaleMuRDown",
  "_CMS_ttHbb_ttbarPlusCCbar_scaleMuFUp","_CMS_ttHbb_ttbarPlusCCbar_scaleMuFDown",
  #"_CMS_ttHbb_ttbarPlusCCbar_ISRUp","_CMS_ttHbb_ttbarPlusCCbar_ISRDown",
  #"_CMS_ttHbb_ttbarPlusCCbar_FSRUp","_CMS_ttHbb_ttbarPlusCCbar_FSRDown",
  ]
systs_tt_cc_weights=[
                    #"dummyWeight_CMS_ttH_ttbarPlusCCbar_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusCCbar_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbarPlusCCbar_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbarPlusCCbar_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    "dummyWeight_CMS_ttH_ttbarPlusCCbar_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ttbarPlusCCbar_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarPlusCCbar_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ttbarPlusCCbar_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarPlusCCbar_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusCCbar_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    ]

systWeights+=systs_tt_all_weights+systs_tt_lf_weights+systs_tt_b_weights+systs_tt_2b_weights+systs_tt_bb_weights+systs_tt_cc_weights
weightSystNames+=systs_tt_all+systs_tt_lf+systs_tt_b+systs_tt_2b+systs_tt_bb+systs_tt_cc
print systWeights
print weightSystNames

assert len(systWeights)==len(weightSystNames)

otherSystNames=[
                    #"_CMS_scale_jUp",
                    #"_CMS_scale_jDown",
                   "_CMS_res_jUp",
                   "_CMS_res_jDown",
    "_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
    "_CMS_scaleAbsoluteScale_jUp","_CMS_scaleAbsoluteScale_jDown",
    #"_CMS_scaleAbsoluteFlavMap_jUp","_CMS_scaleAbsoluteFlavMap_jDown",
    "_CMS_scaleAbsoluteMPFBias_jUp","_CMS_scaleAbsoluteMPFBias_jDown",
    "_CMS_scaleFragmentation_jUp","_CMS_scaleFragmentation_jDown",
    "_CMS_scaleSinglePionECAL_jUp","_CMS_scaleSinglePionECAL_jDown",
    "_CMS_scaleSinglePionHCAL_jUp","_CMS_scaleSinglePionHCAL_jDown",
    "_CMS_scaleFlavorQCD_jUp","_CMS_scaleFlavorQCD_jDown",
    "_CMS_scaleTimePtEta_jUp","_CMS_scaleTimePtEta_jDown",
    "_CMS_scaleRelativeJEREC1_jUp","_CMS_scaleRelativeJEREC1_jDown",
    "_CMS_scaleRelativeJEREC2_jUp","_CMS_scaleRelativeJEREC2_jDown",
    "_CMS_scaleRelativeJERHF_jUp","_CMS_scaleRelativeJERHF_jDown",
    "_CMS_scaleRelativePtBB_jUp","_CMS_scaleRelativePtBB_jDown",
    "_CMS_scaleRelativePtEC1_jUp","_CMS_scaleRelativePtEC1_jDown",
    "_CMS_scaleRelativePtEC2_jUp","_CMS_scaleRelativePtEC2_jDown",
    "_CMS_scaleRelativePtHF_jUp","_CMS_scaleRelativePtHF_jDown",
    "_CMS_scaleRelativeBal_jUp","_CMS_scaleRelativeBal_jDown",
    "_CMS_scaleRelativeFSR_jUp","_CMS_scaleRelativeFSR_jDown",
    "_CMS_scaleRelativeStatFSR_jUp","_CMS_scaleRelativeStatFSR_jDown",
    "_CMS_scaleRelativeStatEC_jUp","_CMS_scaleRelativeStatEC_jDown",
    "_CMS_scaleRelativeStatHF_jUp","_CMS_scaleRelativeStatHF_jDown",
    "_CMS_scalePileUpDataMC_jUp","_CMS_scalePileUpDataMC_jDown",
    "_CMS_scalePileUpPtRef_jUp","_CMS_scalePileUpPtRef_jDown",
    "_CMS_scalePileUpPtBB_jUp","_CMS_scalePileUpPtBB_jDown",
    "_CMS_scalePileUpPtEC1_jUp","_CMS_scalePileUpPtEC1_jDown",
    "_CMS_scalePileUpPtEC2_jUp","_CMS_scalePileUpPtEC2_jDown",
    "_CMS_scalePileUpPtHF_jUp","_CMS_scalePileUpPtHF_jDown",
]

otherSystFileNames=[
      #"JESup","JESdown",
      "JERup","JERdown",
    "JESAbsoluteStatup","JESAbsoluteStatdown",
    "JESAbsoluteScaleup","JESAbsoluteScaledown",
    #"JESAbsoluteFlavMapup","JESAbsoluteFlavMapdown",
    "JESAbsoluteMPFBiasup","JESAbsoluteMPFBiasdown",
    "JESFragmentationup","JESFragmentationdown",
    "JESSinglePionECALup","JESSinglePionECALdown",
    "JESSinglePionHCALup","JESSinglePionHCALdown",
    "JESFlavorQCDup","JESFlavorQCDdown",
    "JESTimePtEtaup","JESTimePtEtadown",
    "JESRelativeJEREC1up","JESRelativeJEREC1down",
    "JESRelativeJEREC2up","JESRelativeJEREC2down",
    "JESRelativeJERHFup","JESRelativeJERHFdown",
    "JESRelativePtBBup","JESRelativePtBBdown",
    "JESRelativePtEC1up","JESRelativePtEC1down",
    "JESRelativePtEC2up","JESRelativePtEC2down",
    "JESRelativePtHFup","JESRelativePtHFdown",
    "JESRelativeBalup","JESRelativeBaldown",
    "JESRelativeFSRup","JESRelativeFSRdown",
    "JESRelativeStatFSRup","JESRelativeStatFSRdown",
    "JESRelativeStatECup","JESRelativeStatECdown",
    "JESRelativeStatHFup","JESRelativeStatHFdown",
    "JESPileUpDataMCup","JESPileUpDataMCdown",
    "JESPileUpPtRefup","JESPileUpPtRefdown",
    "JESPileUpPtBBup","JESPileUpPtBBdown",
    "JESPileUpPtEC1up","JESPileUpPtEC1down",
    "JESPileUpPtEC2up","JESPileUpPtEC2down",
    "JESPileUpPtHFup","JESPileUpPtHFdown",
]

for i,j in zip(otherSystNames,otherSystFileNames):
    print i, j
assert len(otherSystNames)==len(otherSystFileNames)


errorSystNames=[
                    "",
                   "_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   "_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   "_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   "_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
                   "_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",

    #"_CMS_scale_jUp","_CMS_scale_jDown",
    #"_CMS_res_jUp","_CMS_res_jDown",
    
        "_CMS_res_jUp","_CMS_res_jDown",
    "_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
    "_CMS_scaleAbsoluteScale_jUp","_CMS_scaleAbsoluteScale_jDown",
    ##"_CMS_scaleAbsoluteFlavMap_jUp","_CMS_scaleAbsoluteFlavMap_jDown",
    "_CMS_scaleAbsoluteMPFBias_jUp","_CMS_scaleAbsoluteMPFBias_jDown",
    "_CMS_scaleFragmentation_jUp","_CMS_scaleFragmentation_jDown",
    "_CMS_scaleSinglePionECAL_jUp","_CMS_scaleSinglePionECAL_jDown",
    "_CMS_scaleSinglePionHCAL_jUp","_CMS_scaleSinglePionHCAL_jDown",
    "_CMS_scaleFlavorQCD_jUp","_CMS_scaleFlavorQCD_jDown",
    "_CMS_scaleTimePtEta_jUp","_CMS_scaleTimePtEta_jDown",
    "_CMS_scaleRelativeJEREC1_jUp","_CMS_scaleRelativeJEREC1_jDown",
    "_CMS_scaleRelativeJEREC2_jUp","_CMS_scaleRelativeJEREC2_jDown",
    "_CMS_scaleRelativeJERHF_jUp","_CMS_scaleRelativeJERHF_jDown",
    "_CMS_scaleRelativePtBB_jUp","_CMS_scaleRelativePtBB_jDown",
    "_CMS_scaleRelativePtEC1_jUp","_CMS_scaleRelativePtEC1_jDown",
    "_CMS_scaleRelativePtEC2_jUp","_CMS_scaleRelativePtEC2_jDown",
    "_CMS_scaleRelativePtHF_jUp","_CMS_scaleRelativePtHF_jDown",
    "_CMS_scaleRelativeBal_jUp","_CMS_scaleRelativeBal_jDown",
    "_CMS_scaleRelativeFSR_jUp","_CMS_scaleRelativeFSR_jDown",
    "_CMS_scaleRelativeStatFSR_jUp","_CMS_scaleRelativeStatFSR_jDown",
    "_CMS_scaleRelativeStatEC_jUp","_CMS_scaleRelativeStatEC_jDown",
    "_CMS_scaleRelativeStatHF_jUp","_CMS_scaleRelativeStatHF_jDown",
    "_CMS_scalePileUpDataMC_jUp","_CMS_scalePileUpDataMC_jDown",
    "_CMS_scalePileUpPtRef_jUp","_CMS_scalePileUpPtRef_jDown",
    "_CMS_scalePileUpPtBB_jUp","_CMS_scalePileUpPtBB_jDown",
    "_CMS_scalePileUpPtEC1_jUp","_CMS_scalePileUpPtEC1_jDown",
    "_CMS_scalePileUpPtEC2_jUp","_CMS_scalePileUpPtEC2_jDown",
    "_CMS_scalePileUpPtHF_jUp","_CMS_scalePileUpPtHF_jDown",

]+systs_tt_all



#assert len(errorSystNames)==len(weightSystNames+otherSystNames+PSSystNames+QCDSystNames)

# samples
# input path 
path_karim="/nfs/dust/cms/user/kelmorab/ttH_2018/ntuples_v2"
path_matsch="/nfs/dust/cms/user/kelmorab/ttH_2018/ntuples_v3"
path_pkeicher="/nfs/dust/cms/user/pkeicher/ttH_2018/naf_jobs_for_Karim/ntuples"
path_mwassmer="/nfs/dust/cms/user/mwassmer/ttH_2018/ntuples"
ttbarPathS=path_karim+'/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_new_pmx/*nominal*.root'+';'+path_mwassmer+'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx/*nominal*.root'+';'+path_karim+'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*nominal*.root'
VJetsPathS=path_karim+'/DYJets*/*nominal*.root'+';'+path_mwassmer+'/WJets*/*nominal*.root'
ttVPathS=path_pkeicher+'/TTW*/*nominal*.root'+';'+path_pkeicher+'/TTZ*/*nominal*.root'
dibosonPathS=path_mwassmer+'/WW_*/*nominal*.root'+';'+path_mwassmer+'/WZ_*/*nominal*.root'+';'+path_mwassmer+'/ZZ_*/*nominal*.root'
stpath=path_pkeicher+'/ST_*/*nominal*.root'
ttHpath=path_mwassmer+'/ttHTo*/*nominal*.root'


# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
sampleDict=SampleDictionary()
sampleDict.doPrintout()

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
                    Sample('SingleMu',ROOT.kBlack,path_karim+'/SingleMuon*/*nominal*.root',sel_singlemu+sel_MET,'SingleMu',samDict=sampleDict),
                    Sample('SingleEl',ROOT.kBlack,path_karim+'/SingleElectron*/*nominal*.root',sel_singleel+sel_MET,'SingleEl',samDict=sampleDict)
]


print "controlsamples"
samplesControlPlots=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_mwassmer+'/ttH*/*nominal*.root',mcWeightAll+sel_MET,'ttH',systsAllSamples,samDict=sampleDict) ,     
                    Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeightAll+sel_MET+sel_StrangeMuWeights+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systsAllSamples+systs_tt_all+systs_tt_lf,samDict=sampleDict),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeightAll+sel_MET+sel_StrangeMuWeights+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systsAllSamples+systs_tt_all+systs_tt_cc,samDict=sampleDict),
                    Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeightAll+sel_MET+sel_StrangeMuWeights+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systsAllSamples+systs_tt_all+systs_tt_b,samDict=sampleDict),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeightAll+sel_MET+sel_StrangeMuWeights+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systsAllSamples+systs_tt_all+systs_tt_2b,samDict=sampleDict),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeightAll+sel_MET+sel_StrangeMuWeights+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systsAllSamples+systs_tt_all+systs_tt_bb,samDict=sampleDict),  
                    Sample('Single Top',ROOT.kMagenta,stpath,mcWeightAll+sel_MET,'SingleTop',systsAllSamples,samDict=sampleDict) , 
                    Sample('V+jets',ROOT.kGreen-3,VJetsPathS,mcWeightAll+sel_MET,'Vjets',systsAllSamples,samDict=sampleDict) , 
                    Sample('t#bar{t}+V',ROOT.kBlue-10,ttVPathS,mcWeightAll+sel_MET,'ttV',systsAllSamples,samDict=sampleDict),         
                    Sample('Diboson',ROOT.kAzure+2,dibosonPathS,mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict) , 
                    #Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict),  
]

#print "limit samples"
samplesLimits=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_mwassmer+'/ttH*/*nominal*.root',mcWeight+evenSel+sel_MET,'ttH',systsAllSamples,samDict=sampleDict) ,     
                    Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_mwassmer+'/ttHTobb*/*nominal*.root','1.0*'+mcWeight+evenSel+sel_MET,'ttH_hbb',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hccSel+sel_MET,'ttH_hcc',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+httSel+sel_MET,'ttH_htt',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hggSel+sel_MET,'ttH_hgg',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hglugluSel+sel_MET,'ttH_hgluglu',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hwwSel+sel_MET,'ttH_hww',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hzzSel+sel_MET,'ttH_hzz',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hzgSel+sel_MET,'ttH_hzg',systsAllSamples,samDict=sampleDict) ,
                    
                    Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,'ttbarOther',systsAllSamples+systs_tt_all+systs_tt_lf,samDict=sampleDict),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusCC==1)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusCCbar',systsAllSamples+systs_tt_all+systs_tt_cc,samDict=sampleDict),
                    Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==1)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusB',systsAllSamples+systs_tt_all+systs_tt_b,samDict=sampleDict),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==2)'+sel_MET+sel_StrangeMuWeights,'ttbarPlus2B',systsAllSamples+systs_tt_all+systs_tt_2b,samDict=sampleDict),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==3)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusBBbar',systsAllSamples+systs_tt_all+systs_tt_bb,samDict=sampleDict), 
                    Sample('Single Top',ROOT.kMagenta,stpath,mcWeightAll+sel_MET,'singlet',systsAllSamples,samDict=sampleDict) , 
                    Sample('Z+jets',ROOT.kGreen-3,path_karim+'/DYJets*/*nominal*.root',mcWeightAll+sel_MET,'zjets',systsAllSamples,samDict=sampleDict) , 
                    Sample('W+jets',ROOT.kGreen-7,path_mwassmer+'/WJets*/*nominal*.root',mcWeightAll+sel_MET,'wjets',systsAllSamples,samDict=sampleDict) , 
                    Sample('t#bar{t}+W',ROOT.kBlue-10,path_pkeicher+'/TTW*/*nominal*.root',mcWeightAll+sel_MET,'ttbarW',systsAllSamples,samDict=sampleDict),
                    Sample('t#bar{t}+Z',ROOT.kBlue-6,path_pkeicher+'/TTZ*/*nominal*.root',mcWeightAll+sel_MET,'ttbarZ',systsAllSamples,samDict=sampleDict),
                    Sample('Diboson',ROOT.kAzure+2,dibosonPathS,mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict) , 
                    #Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict),  
]
