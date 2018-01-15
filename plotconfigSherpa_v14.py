import sys
import os
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *

sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)*(N_Jets>=4 && N_BTagsM>=2)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0 && (N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1)))*(N_Jets>=4 && N_BTagsM>=2)" # and vice versa...
#sel_MET="*(Evt_Pt_MET>20.)"
sel_MET="*(Evt_Pt_MET>20.)"

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
weightSystNames=[
                    "",
                   "_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   "_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   "_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   "_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
###                    "_CMS_ttHbb_TopPtUp","_CMS_ttHbb_TopPtDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarOtherUp","_CMS_ttHbb_Q2scale_ttbarOtherDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlusBUp","_CMS_ttHbb_Q2scale_ttbarPlusBDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlus2BUp","_CMS_ttHbb_Q2scale_ttbarPlus2BDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlusBBbarUp","_CMS_ttHbb_Q2scale_ttbarPlusBBbarDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlusCCbarUp","_CMS_ttHbb_Q2scale_ttbarPlusCCbarDown",
##                    "_CMS_ttHbb_NNPDFUp","_CMS_ttHbb_NNPDFDown",
                  "_CMS_effTrigger_eUp","_CMS_effTrigger_eDown",  
                   "_CMS_effTrigger_mUp","_CMS_effTrigger_mDown",  
##                     "_CMS_ttHbb_ljets_TrigUp","_CMS_ttHbb_ljets_TrigDown",
                   "_CMS_eff_eUp","_CMS_eff_eDown", 
                   "_CMS_eff_mUp","_CMS_eff_mDown",
                   "_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",
		  ##"_CMS_ttHbb_eff_leptonUp","_CMS_ttHbb_eff_leptonDown",
                   ##"_CMS_res_jUp","_CMS_res_jDown"
                    ##"_CMS_scale_jUp","_CMS_scale_jDown",
]

systsAllSamples=[
                    "",
                   "_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   "_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   "_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   "_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
                  "_CMS_effTrigger_eUp","_CMS_effTrigger_eDown",  
                   "_CMS_effTrigger_mUp","_CMS_effTrigger_mDown",  
                    #"_CMS_ttHbb_ljets_TrigUp","_CMS_ttHbb_ljets_TrigDown",
                    "_CMS_eff_eUp","_CMS_eff_eDown", 
                   "_CMS_eff_mUp","_CMS_eff_mDown",  
                   "_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",

                   #"_CMS_ttHbb_eff_leptonUp","_CMS_ttHbb_eff_leptonDown",
                   ##"_CMS_res_jUp","_CMS_res_jDown",
                    ##"_CMS_scale_jUp","_CMS_scale_jDown",
 #"_CMS_scale_jUp","_CMS_scale_jDown",
    #"_CMS_res_jUp","_CMS_res_jDown",
    #"_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
    #"_CMS_scaleAbsoluteScale_jUp","_CMS_scaleAbsoluteScale_jDown",
    ##"_CMS_scaleAbsoluteFlavMap_jUp","_CMS_scaleAbsoluteFlavMap_jDown",
    #"_CMS_scaleAbsoluteMPFBias_jUp","_CMS_scaleAbsoluteMPFBias_jDown",
    #"_CMS_scaleFragmentation_jUp","_CMS_scaleFragmentation_jDown",
    #"_CMS_scaleSinglePionECAL_jUp","_CMS_scaleSinglePionECAL_jDown",
    #"_CMS_scaleSinglePionHCAL_jUp","_CMS_scaleSinglePionHCAL_jDown",
    #"_CMS_scaleFlavorQCD_jUp","_CMS_scaleFlavorQCD_jDown",
    #"_CMS_scaleTimePtEta_jUp","_CMS_scaleTimePtEta_jDown",
    #"_CMS_scaleRelativeJEREC1_jUp","_CMS_scaleRelativeJEREC1_jDown",
    #"_CMS_scaleRelativeJEREC2_jUp","_CMS_scaleRelativeJEREC2_jDown",
    #"_CMS_scaleRelativeJERHF_jUp","_CMS_scaleRelativeJERHF_jDown",
    #"_CMS_scaleRelativePtBB_jUp","_CMS_scaleRelativePtBB_jDown",
    #"_CMS_scaleRelativePtEC1_jUp","_CMS_scaleRelativePtEC1_jDown",
    #"_CMS_scaleRelativePtEC2_jUp","_CMS_scaleRelativePtEC2_jDown",
    #"_CMS_scaleRelativePtHF_jUp","_CMS_scaleRelativePtHF_jDown",
    #"_CMS_scaleRelativeBal_jUp","_CMS_scaleRelativeBal_jDown",
    #"_CMS_scaleRelativeFSR_jUp","_CMS_scaleRelativeFSR_jDown",
    #"_CMS_scaleRelativeStatFSR_jUp","_CMS_scaleRelativeStatFSR_jDown",
    #"_CMS_scaleRelativeStatEC_jUp","_CMS_scaleRelativeStatEC_jDown",
    #"_CMS_scaleRelativeStatHF_jUp","_CMS_scaleRelativeStatHF_jDown",
    #"_CMS_scalePileUpDataMC_jUp","_CMS_scalePileUpDataMC_jDown",
    #"_CMS_scalePileUpPtRef_jUp","_CMS_scalePileUpPtRef_jDown",
    #"_CMS_scalePileUpPtBB_jUp","_CMS_scalePileUpPtBB_jDown",
    #"_CMS_scalePileUpPtEC1_jUp","_CMS_scalePileUpPtEC1_jDown",
    #"_CMS_scalePileUpPtEC2_jUp","_CMS_scalePileUpPtEC2_jDown",
    #"_CMS_scalePileUpPtHF_jUp","_CMS_scalePileUpPtHF_jDown",
    #"_CMS_scalePileUpMuZero_jUp","_CMS_scalePileUpMuZero_jDown",
    #"_CMS_scalePileUpEnvelope_jUp","_CMS_scalePileUpEnvelope_jDown",
    #"_CMS_scaleSubTotalPileUp_jUp","_CMS_scaleSubTotalPileUp_jDown",
    #"_CMS_scaleSubTotalRelative_jUp","_CMS_scaleSubTotalRelative_jDown",
    #"_CMS_scaleSubTotalPt_jUp","_CMS_scaleSubTotalPt_jDown",
    #"_CMS_scaleSubTotalScale_jUp","_CMS_scaleSubTotalScale_jDown",
    #"_CMS_scaleSubTotalAbsolute_jUp","_CMS_scaleSubTotalAbsolute_jDown",
    #"_CMS_scaleSubTotalMC_jUp","_CMS_scaleSubTotalMC_jDown",
    #"_CMS_scaleTotal_jUp","_CMS_scaleTotal_jDown",
    #"_CMS_scaleTotalNoFlavor_jUp","_CMS_scaleTotalNoFlavor_jDown",
    #"_CMS_scaleTotalNoTime_jUp","_CMS_scaleTotalNoTime_jDown",
    #"_CMS_scaleTotalNoFlavorNoTime_jUp","_CMS_scaleTotalNoFlavorNoTime_jDown",
    #"_CMS_scaleFlavorZJet_jUp","_CMS_scaleFlavorZJet_jDown",
    #"_CMS_scaleFlavorPhotonJet_jUp","_CMS_scaleFlavorPhotonJet_jDown",
    #"_CMS_scaleFlavorPureGluon_jUp","_CMS_scaleFlavorPureGluon_jDown",
    #"_CMS_scaleFlavorPureQuark_jUp","_CMS_scaleFlavorPureQuark_jDown",
    #"_CMS_scaleFlavorPureCharm_jUp","_CMS_scaleFlavorPureCharm_jDown",
    #"_CMS_scaleFlavorPureBottom_jUp","_CMS_scaleFlavorPureBottom_jDown",
    #"_CMS_scaleTimeRunBCD_jUp","_CMS_scaleTimeRunBCD_jDown",
    #"_CMS_scaleTimeRunEF_jUp","_CMS_scaleTimeRunEF_jDown",
    #"_CMS_scaleTimeRunG_jUp","_CMS_scaleTimeRunG_jDown",
    #"_CMS_scaleTimeRunH_jUp","_CMS_scaleTimeRunH_jDown",

]

systsTtbar= [
  #"_CMS_ttHbb_FSRUp","_CMS_ttHbb_FSRDown",
  #"_CMS_ttHbb_ISRUp","_CMS_ttHbb_ISRDown",
  #"_CMS_ttHbb_HDAMPUp","_CMS_ttHbb_HDAMPDown",
  #"_CMS_ttHbb_UEUp","_CMS_ttHbb_UEDown",
  "_CMS_ttHbb_scaleMuFUp",
  "_CMS_ttHbb_scaleMuFDown",
  "_CMS_ttHbb_scaleMuRUp",
  "_CMS_ttHbb_scaleMuRDown",  
  "_CMS_ttHbb_PDFUp",
  "_CMS_ttHbb_PDFDown",
  
  
]

systs_tt_lf=[]
systs_tt_b=[]
systs_tt_2b=[]
systs_tt_bb=[]
systs_tt_cc=[]



mcWeightAll='35.91823'
mcWeight='35.91823*2.0'


mcTriggerWeight='((1.0)*(internalEleTriggerWeight*internalMuTriggerWeight)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))))'
#mcTriggerWeight='((1.0)*(Weight_ElectronSFTrigger*Weight_MuonSFTrigger)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))) )'
#mcTriggerWeight='((1.0)*(1.0)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))))'

#sfs="Weight_ElectronSFID*Weight_MuonSFID*Weight_MuonSFIso*Weight_ElectronSFGFS*Weight_MuonSFHIP"
sfs="internalEleIDWeight*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeight*internalMuHIPWeight"

usualWeights="(1*Weight_pu69p2*((Weight>0)-(Weight<0)))"+"*"+sfs

evenSel="*(Evt_Odd==0)"


#ttbarMCWeight='*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))'
#ttbarMCWeight='*0.0084896859/Weight_XS'

# generator rate normalization weights
#mu_down_sf=1.1402
#mu_up_sf=0.8727
mu_down_sf=1.0
mu_up_sf=1.0
pdf_05_sf=0.950964383883
pdf_67_sf=1.04093344845

systWeights=[
                    "NomWeight:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
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
                   
                   #"dummyWeight_CMS_ttH_PUUp:="+"(1*Weight_pu69p2Up*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",

		   #"dummyWeight_CMS_ttH_PUDown:="+"(1*Weight_pu69p2Down*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",

		   "dummyWeight_CMS_ttH_ljets_Trig_elUp:="+usualWeights+"*"+"((1.0)*(internalEleTriggerWeightUp*internalMuTriggerWeight)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))) )"+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
		    
		    "dummyWeight_CMS_ttH_ljets_Trig_elDown:="+usualWeights+"*"+"((1.0)*(internalEleTriggerWeightDown*internalMuTriggerWeight)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))) )"+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
		    
		    "dummyWeight_CMS_ttH_ljets_Trig_muUp:="+usualWeights+"*"+"((1.0)*(internalEleTriggerWeight*internalMuTriggerWeightUp)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))) )"+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
		    
		    "dummyWeight_CMS_ttH_ljets_Trig_muDown:="+usualWeights+"*"+"((1.0)*(internalEleTriggerWeight*internalMuTriggerWeightDown)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))) )"+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
		    "dummyWeight_CMS_ttH_eff_elUp:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))*internalEleIDWeightUp*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeightUp*internalMuHIPWeight*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
		    "dummyWeight_CMS_ttH_eff_elDown:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))"+"*internalEleIDWeightDown*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeightDown*internalMuHIPWeight*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
		     "dummyWeight_CMS_ttH_eff_muUp:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))"+"*internalEleIDWeight*internalMuIDWeightUp*internalMuIsoWeightUp*internalEleGFSWeight*internalMuHIPWeightUp*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
		    "dummyWeight_CMS_ttH_eff_muDown:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))"+"*internalEleIDWeight*internalMuIDWeightDown*internalMuIsoWeightDown*internalEleGFSWeight*internalMuHIPWeightDown*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
		    
		    "dummyWeightPileUpUp:="+"(1*Weight_pu69p2Up*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
		    "dummyWeightPileUpDown:="+"(1*Weight_pu69p2Down*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",
		    
		    #"dummyWeightQCDScaleFactor_=
]



Q2SystWeights= [

                "dummyWeight_CMS_ttH_scaleMuRDown:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_0p5_muF_1p0*Weight_scale_variation_muR_0p5_muF_1p0)*(DoWeights==1)+(DoWeights==0)*1.0)",
                "dummyWeight_CMS_ttH_scaleMuRUp:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_2p0_muF_1p0*Weight_scale_variation_muR_2p0_muF_1p0)*(DoWeights==1)+(DoWeights==0)*1.0)",
                "dummyWeight_CMS_ttH_scaleMuFDown:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_1p0_muF_0p5*Weight_scale_variation_muR_1p0_muF_0p5)*(DoWeights==1)+(DoWeights==0)*1.0)",
                "dummyWeight_CMS_ttH_scaleMuFUp:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_1p0_muF_2p0*Weight_scale_variation_muR_1p0_muF_2p0)*(DoWeights==1)+(DoWeights==0)*1.0)",
                "dummyWeight_CMS_ttH_scaleMEDown:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_0p5_muF_0p5*Weight_scale_variation_muR_0p5_muF_0p5)*(DoWeights==1)+(DoWeights==0)*1.0)",
                "dummyWeight_CMS_ttH_scaleMEUp:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_2p0_muF_2p0*Weight_scale_variation_muR_2p0_muF_2p0)*(DoWeights==1)+(DoWeights==0)*1.0)",
                "dummyWeight_CMS_ttH_Q2_muR_Up_muF_Down:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_2p0_muF_0p5*Weight_scale_variation_muR_2p0_muF_0p5)*(DoWeights==1)+(DoWeights==0)*1.0)",        
                "dummyWeight_CMS_ttH_Q2_muR_Down_muF_Up:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_0p5_muF_2p0*Weight_scale_variation_muR_0p5_muF_2p0)*(DoWeights==1)+(DoWeights==0)*1.0)",
]

Q2SystNames= [

                "_CMS_ttHbb_scaleMuRDown",
                "_CMS_ttHbb_scaleMuRUp",
                "_CMS_ttHbb_scaleMuFDown",
                "_CMS_ttHbb_scaleMuFUp",
                "_CMS_ttHbb_scaleMEDown",
                "_CMS_ttHbb_scaleMEUp",
                "_CMS_ttHbb_scaleMuRupMuFdown",
                "_CMS_ttHbb_scaleMuRdownMuFup",
]

PDFSystWeights= [

                "dummyWeight_CMS_ttH_PDFUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalPDFweightUp*(DoWeights==1)+(DoWeights==0)*1.0)",
                "dummyWeight_CMS_ttH_PDFDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalPDFweightDown*(DoWeights==1)+(DoWeights==0)*1.0)"
                
]

PDFSystNames= [

                "_CMS_ttHbb_PDFUp",
                "_CMS_ttHbb_PDFDown",

]

systs_tt_all=["_CMS_ttHbb_FSRUp","_CMS_ttHbb_FSRDown","_CMS_ttHbb_ISRUp","_CMS_ttHbb_ISRDown","_CMS_ttHbb_HDAMPUp","_CMS_ttHbb_HDAMPDown","_CMS_ttHbb_UEUp","_CMS_ttHbb_UEDown"]
systs_tt_all_weights=[
                    "dummyWeight_CMS_ttH_FSRUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightup)*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_FSRDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightdown)*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISRUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightup)*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISRDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightdown)*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdampUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightup)*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdampDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightdown)*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ueUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightup)*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ueDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightdown)*(DoWeights==1)+(DoWeights==0)*1.0"
                    ]



systs_tt_lf=["_CMS_ttHbb_FSR_ttbarOtherUp","_CMS_ttHbb_FSR_ttbarOtherDown","_CMS_ttHbb_ISR_ttbarOtherUp","_CMS_ttHbb_ISR_ttbarOtherDown","_CMS_ttHbb_HDAMP_ttbarOtherUp","_CMS_ttHbb_HDAMP_ttbarOtherDown","_CMS_ttHbb_UE_ttbarOtherUp","_CMS_ttHbb_UE_ttbarOtherDown"]
systs_tt_lf_weights=[
                    "dummyWeight_CMS_ttH_FSR_ttbarOtherUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightup*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_FSR_ttbarOtherDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightdown*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISR_ttbarOtherUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightup*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISR_ttbarOtherDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightdown*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdamp_ttbarOtherUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightup*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdamp_ttbarOtherDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightdown*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ue_ttbarOtherUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightup*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ue_ttbarOtherDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightdown*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))*(DoWeights==1)+(DoWeights==0)*1.0"
                    ]
systs_tt_b=["_CMS_ttHbb_FSR_ttbarPlusBUp","_CMS_ttHbb_FSR_ttbarPlusBDown","_CMS_ttHbb_ISR_ttbarPlusBUp","_CMS_ttHbb_ISR_ttbarPlusBDown","_CMS_ttHbb_HDAMP_ttbarPlusBUp","_CMS_ttHbb_HDAMP_ttbarPlusBDown","_CMS_ttHbb_UE_ttbarPlusBUp","_CMS_ttHbb_UE_ttbarPlusBDown"]
systs_tt_b_weights=[
                    "dummyWeight_CMS_ttH_FSR_ttbarPlusBUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightup*(GenEvt_I_TTPlusBB==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_FSR_ttbarPlusBDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightdown*(GenEvt_I_TTPlusBB==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISR_ttbarPlusBUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightup*(GenEvt_I_TTPlusBB==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISR_ttbarPlusBDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightdown*(GenEvt_I_TTPlusBB==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdamp_ttbarPlusBUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightup*(GenEvt_I_TTPlusBB==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdamp_ttbarPlusBDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightdown*(GenEvt_I_TTPlusBB==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ue_ttbarPlusBUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightup*(GenEvt_I_TTPlusBB==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ue_ttbarPlusBDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightdown*(GenEvt_I_TTPlusBB==1))*(DoWeights==1)+(DoWeights==0)*1.0"
                    ]
systs_tt_2b=["_CMS_ttHbb_FSR_ttbarPlus2BUp","_CMS_ttHbb_FSR_ttbarPlus2BDown","_CMS_ttHbb_ISR_ttbarPlus2BUp","_CMS_ttHbb_ISR_ttbarPlus2BDown","_CMS_ttHbb_HDAMP_ttbarPlus2BUp","_CMS_ttHbb_HDAMP_ttbarPlus2BDown","_CMS_ttHbb_UE_ttbarPlus2BUp","_CMS_ttHbb_UE_ttbarPlus2BDown"]
systs_tt_2b_weights=[
                    "dummyWeight_CMS_ttH_FSR_ttbarPlus2BUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightup*(GenEvt_I_TTPlusBB==2))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_FSR_ttbarPlus2BDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightdown*(GenEvt_I_TTPlusBB==2))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISR_ttbarPlus2BUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightup*(GenEvt_I_TTPlusBB==2))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISR_ttbarPlus2BDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightdown*(GenEvt_I_TTPlusBB==2))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdamp_ttbarPlus2BUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightup*(GenEvt_I_TTPlusBB==2))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdamp_ttbarPlus2BDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightdown*(GenEvt_I_TTPlusBB==2))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ue_ttbarPlus2BUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightup*(GenEvt_I_TTPlusBB==2))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ue_ttbarPlus2BDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightdown*(GenEvt_I_TTPlusBB==2))*(DoWeights==1)+(DoWeights==0)*1.0"
                ]
systs_tt_bb=["_CMS_ttHbb_FSR_ttbarPlusBBbarUp","_CMS_ttHbb_FSR_ttbarPlusBBbarDown","_CMS_ttHbb_ISR_ttbarPlusBBbarUp","_CMS_ttHbb_ISR_ttbarPlusBBbarDown","_CMS_ttHbb_HDAMP_ttbarPlusBBbarUp","_CMS_ttHbb_HDAMP_ttbarPlusBBbarDown","_CMS_ttHbb_UE_ttbarPlusBBbarUp","_CMS_ttHbb_UE_ttbarPlusBBbarDown"]
systs_tt_bb_weights=[
                    "dummyWeight_CMS_ttH_FSR_ttbarPlusBBbarUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightup*(GenEvt_I_TTPlusBB==3))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_FSR_ttbarPlusBBbarDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightdown*(GenEvt_I_TTPlusBB==3))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISR_ttbarPlusBBbarUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightup*(GenEvt_I_TTPlusBB==3))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISR_ttbarPlusBBbarDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightdown*(GenEvt_I_TTPlusBB==3))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdamp_ttbarPlusBBbarUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightup*(GenEvt_I_TTPlusBB==3))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdamp_ttbarPlusBBbarDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightdown*(GenEvt_I_TTPlusBB==3))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ue_ttbarPlusBBbarUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightup*(GenEvt_I_TTPlusBB==3))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ue_ttbarPlusBBbarDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightdown*(GenEvt_I_TTPlusBB==3))*(DoWeights==1)+(DoWeights==0)*1.0"
                ]
systs_tt_cc=["_CMS_ttHbb_FSR_ttbarPlusCCbarUp","_CMS_ttHbb_FSR_ttbarPlusCCbarDown","_CMS_ttHbb_ISR_ttbarPlusCCbarUp","_CMS_ttHbb_ISR_ttbarPlusCCbarDown","_CMS_ttHbb_HDAMP_ttbarPlusCCbarUp","_CMS_ttHbb_HDAMP_ttbarPlusCCbarDown","_CMS_ttHbb_UE_ttbarPlusCCbarUp","_CMS_ttHbb_UE_ttbarPlusCCbarDown"]
systs_tt_cc_weights=[
                    "dummyWeight_CMS_ttH_FSR_ttbarPlusCCbarUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightup*(GenEvt_I_TTPlusCC==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_FSR_ttbarPlusCCbarDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalFSRweightdown*(GenEvt_I_TTPlusCC==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISR_ttbarPlusCCbarUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightup*(GenEvt_I_TTPlusCC==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ISR_ttbarPlusCCbarDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalISRweightdown*(GenEvt_I_TTPlusCC==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdamp_ttbarPlusCCbarUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightup*(GenEvt_I_TTPlusCC==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_hdamp_ttbarPlusCCbarDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalHDAMPweightdown*(GenEvt_I_TTPlusCC==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ue_ttbarPlusCCbarUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightup*(GenEvt_I_TTPlusCC==1))*(DoWeights==1)+(DoWeights==0)*1.0",
                    "dummyWeight_CMS_ttH_ue_ttbarPlusCCbarDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalUEweightdown*(GenEvt_I_TTPlusCC==1))*(DoWeights==1)+(DoWeights==0)*1.0"
                    ]

systWeights+=Q2SystWeights+PDFSystWeights+systs_tt_all_weights+systs_tt_lf_weights+systs_tt_b_weights+systs_tt_2b_weights+systs_tt_bb_weights+systs_tt_cc_weights
weightSystNames+=Q2SystNames+PDFSystNames+systs_tt_all+systs_tt_lf+systs_tt_b+systs_tt_2b+systs_tt_bb+systs_tt_cc


assert len(systWeights)==len(weightSystNames)

otherSystNames=[
                    #"_CMS_scale_jUp",
                    #"_CMS_scale_jDown",
                   #"_CMS_res_jUp",
                   #"_CMS_res_jDown"
                    ##"_CMS_ttHbb_PSscaleUp",
                    ##"_CMS_ttHbb_PSscaleDown"
    #"_CMS_scale_jUp","_CMS_scale_jDown",
    #"_CMS_res_jUp","_CMS_res_jDown",
    #"_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
    #"_CMS_scaleAbsoluteScale_jUp","_CMS_scaleAbsoluteScale_jDown",
    ##"_CMS_scaleAbsoluteFlavMap_jUp","_CMS_scaleAbsoluteFlavMap_jDown",
    #"_CMS_scaleAbsoluteMPFBias_jUp","_CMS_scaleAbsoluteMPFBias_jDown",
    #"_CMS_scaleFragmentation_jUp","_CMS_scaleFragmentation_jDown",
    #"_CMS_scaleSinglePionECAL_jUp","_CMS_scaleSinglePionECAL_jDown",
    #"_CMS_scaleSinglePionHCAL_jUp","_CMS_scaleSinglePionHCAL_jDown",
    #"_CMS_scaleFlavorQCD_jUp","_CMS_scaleFlavorQCD_jDown",
    #"_CMS_scaleTimePtEta_jUp","_CMS_scaleTimePtEta_jDown",
    #"_CMS_scaleRelativeJEREC1_jUp","_CMS_scaleRelativeJEREC1_jDown",
    #"_CMS_scaleRelativeJEREC2_jUp","_CMS_scaleRelativeJEREC2_jDown",
    #"_CMS_scaleRelativeJERHF_jUp","_CMS_scaleRelativeJERHF_jDown",
    #"_CMS_scaleRelativePtBB_jUp","_CMS_scaleRelativePtBB_jDown",
    #"_CMS_scaleRelativePtEC1_jUp","_CMS_scaleRelativePtEC1_jDown",
    #"_CMS_scaleRelativePtEC2_jUp","_CMS_scaleRelativePtEC2_jDown",
    #"_CMS_scaleRelativePtHF_jUp","_CMS_scaleRelativePtHF_jDown",
    #"_CMS_scaleRelativeBal_jUp","_CMS_scaleRelativeBal_jDown",
    #"_CMS_scaleRelativeFSR_jUp","_CMS_scaleRelativeFSR_jDown",
    #"_CMS_scaleRelativeStatFSR_jUp","_CMS_scaleRelativeStatFSR_jDown",
    #"_CMS_scaleRelativeStatEC_jUp","_CMS_scaleRelativeStatEC_jDown",
    #"_CMS_scaleRelativeStatHF_jUp","_CMS_scaleRelativeStatHF_jDown",
    #"_CMS_scalePileUpDataMC_jUp","_CMS_scalePileUpDataMC_jDown",
    #"_CMS_scalePileUpPtRef_jUp","_CMS_scalePileUpPtRef_jDown",
    #"_CMS_scalePileUpPtBB_jUp","_CMS_scalePileUpPtBB_jDown",
    #"_CMS_scalePileUpPtEC1_jUp","_CMS_scalePileUpPtEC1_jDown",
    #"_CMS_scalePileUpPtEC2_jUp","_CMS_scalePileUpPtEC2_jDown",
    #"_CMS_scalePileUpPtHF_jUp","_CMS_scalePileUpPtHF_jDown",
    #"_CMS_scalePileUpMuZero_jUp","_CMS_scalePileUpMuZero_jDown",
    #"_CMS_scalePileUpEnvelope_jUp","_CMS_scalePileUpEnvelope_jDown",
    #"_CMS_scaleSubTotalPileUp_jUp","_CMS_scaleSubTotalPileUp_jDown",
    #"_CMS_scaleSubTotalRelative_jUp","_CMS_scaleSubTotalRelative_jDown",
    #"_CMS_scaleSubTotalPt_jUp","_CMS_scaleSubTotalPt_jDown",
    #"_CMS_scaleSubTotalScale_jUp","_CMS_scaleSubTotalScale_jDown",
    #"_CMS_scaleSubTotalAbsolute_jUp","_CMS_scaleSubTotalAbsolute_jDown",
    #"_CMS_scaleSubTotalMC_jUp","_CMS_scaleSubTotalMC_jDown",
    #"_CMS_scaleTotal_jUp","_CMS_scaleTotal_jDown",
    #"_CMS_scaleTotalNoFlavor_jUp","_CMS_scaleTotalNoFlavor_jDown",
    #"_CMS_scaleTotalNoTime_jUp","_CMS_scaleTotalNoTime_jDown",
    #"_CMS_scaleTotalNoFlavorNoTime_jUp","_CMS_scaleTotalNoFlavorNoTime_jDown",
    #"_CMS_scaleFlavorZJet_jUp","_CMS_scaleFlavorZJet_jDown",
    #"_CMS_scaleFlavorPhotonJet_jUp","_CMS_scaleFlavorPhotonJet_jDown",
    #"_CMS_scaleFlavorPureGluon_jUp","_CMS_scaleFlavorPureGluon_jDown",
    #"_CMS_scaleFlavorPureQuark_jUp","_CMS_scaleFlavorPureQuark_jDown",
    #"_CMS_scaleFlavorPureCharm_jUp","_CMS_scaleFlavorPureCharm_jDown",
    #"_CMS_scaleFlavorPureBottom_jUp","_CMS_scaleFlavorPureBottom_jDown",
    #"_CMS_scaleTimeRunBCD_jUp","_CMS_scaleTimeRunBCD_jDown",
    #"_CMS_scaleTimeRunEF_jUp","_CMS_scaleTimeRunEF_jDown",
    #"_CMS_scaleTimeRunG_jUp","_CMS_scaleTimeRunG_jDown",
    #"_CMS_scaleTimeRunH_jUp","_CMS_scaleTimeRunH_jDown",
    
]

otherSystFileNames=[
      #"JESup","JESdown",
      #"JERup","JERdown",
    #"JESAbsoluteStatup","JESAbsoluteStatdown",
    #"JESAbsoluteScaleup","JESAbsoluteScaledown",
    ##"JESAbsoluteFlavMapup","JESAbsoluteFlavMapdown",
    #"JESAbsoluteMPFBiasup","JESAbsoluteMPFBiasdown",
    #"JESFragmentationup","JESFragmentationdown",
    #"JESSinglePionECALup","JESSinglePionECALdown",
    #"JESSinglePionHCALup","JESSinglePionHCALdown",
    #"JESFlavorQCDup","JESFlavorQCDdown",
    #"JESTimePtEtaup","JESTimePtEtadown",
    #"JESRelativeJEREC1up","JESRelativeJEREC1down",
    #"JESRelativeJEREC2up","JESRelativeJEREC2down",
    #"JESRelativeJERHFup","JESRelativeJERHFdown",
    #"JESRelativePtBBup","JESRelativePtBBdown",
    #"JESRelativePtEC1up","JESRelativePtEC1down",
    #"JESRelativePtEC2up","JESRelativePtEC2down",
    #"JESRelativePtHFup","JESRelativePtHFdown",
    #"JESRelativeBalup","JESRelativeBaldown",
    #"JESRelativeFSRup","JESRelativeFSRdown",
    #"JESRelativeStatFSRup","JESRelativeStatFSRdown",
    #"JESRelativeStatECup","JESRelativeStatECdown",
    #"JESRelativeStatHFup","JESRelativeStatHFdown",
    #"JESPileUpDataMCup","JESPileUpDataMCdown",
    #"JESPileUpPtRefup","JESPileUpPtRefdown",
    #"JESPileUpPtBBup","JESPileUpPtBBdown",
    #"JESPileUpPtEC1up","JESPileUpPtEC1down",
    #"JESPileUpPtEC2up","JESPileUpPtEC2down",
    #"JESPileUpPtHFup","JESPileUpPtHFdown",
    #"JESPileUpMuZeroUp","JESPileUpMuZeroDown",
    #"JESPileUpEnvelopeUp","JESPileUpEnvelopeDown",
    #"JESSubTotalPileUpUp","JESSubTotalPileUpDown",
    #"JESSubTotalRelativeUp","JESSubTotalRelativeDown",
    #"JESSubTotalPtUp","JESSubTotalPtDown",
    #"JESSubTotalScaleUp","JESSubTotalScaleDown",
    #"JESSubTotalAbsoluteUp","JESSubTotalAbsoluteDown",
    #"JESSubTotalMCUp","JESSubTotalMCDown",
    #"JESTotalUp","JESTotalDown",
    #"JESTotalNoFlavorUp","JESTotalNoFlavorDown",
    #"JESTotalNoTimeUp","JESTotalNoTimeDown",
    #"JESTotalNoFlavorNoTimeUp","JESTotalNoFlavorNoTimeDown",
    #"JESFlavorZJetUp","JESFlavorZJetDown",
    #"JESFlavorPhotonJetUp","JESFlavorPhotonJetDown",
    #"JESFlavorPureGluonUp","JESFlavorPureGluonDown",
    #"JESFlavorPureQuarkUp","JESFlavorPureQuarkDown",
    #"JESFlavorPureCharmUp","JESFlavorPureCharmDown",
    #"JESFlavorPureBottomUp","JESFlavorPureBottomDown",
    #"JESTimeRunBCDUp","JESTimeRunBCDDown",
    #"JESTimeRunEFUp","JESTimeRunEFDown",
    #"JESTimeRunGUp","JESTimeRunGDown",
    #"JESTimeRunHUp","JESTimeRunHDown",

]

PSSystNames=[
  #"_CMS_ttHbbFROMTREES_FSRUp","_CMS_ttHbbFROMTREES_FSRDown",
  #"_CMS_ttHbbFROMTREES_ISRUp","_CMS_ttHbbFROMTREES_ISRDown",
  #"_CMS_ttHbbFROMTREES_HDAMPUp","_CMS_ttHbbFROMTREES_HDAMPDown",
  #"_CMS_ttHbbFROMTREES_UEUp","_CMS_ttHbbFROMTREES_UEDown",
]
PSSystFileNames=[
  #"fsr_up","fsr_down",
  #"isr_up","isr_down",
  #"hdamp_up","hdamp_down",
  #"ue_up","ue_down",
]

QCDSystNames=[
  "_CMS_ttHbb_QCDScaleFactorUp","_CMS_ttHbb_QCDScaleFactorDown",
  ]
QCDSystReplacementStrings=[
  "internalQCDweightup","internalQCDweightdown",
  ]



errorSystNamesNoPS=[
                    "",
                   "_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   "_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   "_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   "_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
##                    "_CMS_ttHbb_TopPtUp","_CMS_ttHbb_TopPtDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarOtherUp","_CMS_ttHbb_Q2scale_ttbarOtherDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlusBUp","_CMS_ttHbb_Q2scale_ttbarPlusBDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlus2BUp","_CMS_ttHbb_Q2scale_ttbarPlus2BDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlusBBbarUp","_CMS_ttHbb_Q2scale_ttbarPlusBBbarDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlusCCbarUp","_CMS_ttHbb_Q2scale_ttbarPlusCCbarDown",
##                    "_CMS_ttHbb_NNPDFUp","_CMS_ttHbb_NNPDFDown",
                   "_CMS_effTrigger_eUp","_CMS_effTrigger_eDown",  
                   "_CMS_effTrigger_mUp","_CMS_effTrigger_mDown",  
###                     "_CMS_ttHbb_ljets_TrigUp","_CMS_ttHbb_ljets_TrigDown",
                    "_CMS_eff_eUp","_CMS_eff_eDown", 
                   "_CMS_eff_mUp","_CMS_eff_mDown",  
                    "_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",

                   ##"_CMS_ttHbb_eff_leptonUp","_CMS_ttHbb_eff_leptonDown",
                   ##"_CMS_res_jUp","_CMS_res_jDown",
                    ##"_CMS_scale_jUp","_CMS_scale_jDown",
                    ##"_CMS_ttHbb_PSscaleUp","_CMS_ttHbb_PSscaleDown",

    #"_CMS_scale_jUp","_CMS_scale_jDown",
    #"_CMS_res_jUp","_CMS_res_jDown",
    #"_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
    #"_CMS_scaleAbsoluteScale_jUp","_CMS_scaleAbsoluteScale_jDown",
    ##"_CMS_scaleAbsoluteFlavMap_jUp","_CMS_scaleAbsoluteFlavMap_jDown",
    #"_CMS_scaleAbsoluteMPFBias_jUp","_CMS_scaleAbsoluteMPFBias_jDown",
    #"_CMS_scaleFragmentation_jUp","_CMS_scaleFragmentation_jDown",
    #"_CMS_scaleSinglePionECAL_jUp","_CMS_scaleSinglePionECAL_jDown",
    #"_CMS_scaleSinglePionHCAL_jUp","_CMS_scaleSinglePionHCAL_jDown",
    #"_CMS_scaleFlavorQCD_jUp","_CMS_scaleFlavorQCD_jDown",
    #"_CMS_scaleTimePtEta_jUp","_CMS_scaleTimePtEta_jDown",
    #"_CMS_scaleRelativeJEREC1_jUp","_CMS_scaleRelativeJEREC1_jDown",
    #"_CMS_scaleRelativeJEREC2_jUp","_CMS_scaleRelativeJEREC2_jDown",
    #"_CMS_scaleRelativeJERHF_jUp","_CMS_scaleRelativeJERHF_jDown",
    #"_CMS_scaleRelativePtBB_jUp","_CMS_scaleRelativePtBB_jDown",
    #"_CMS_scaleRelativePtEC1_jUp","_CMS_scaleRelativePtEC1_jDown",
    #"_CMS_scaleRelativePtEC2_jUp","_CMS_scaleRelativePtEC2_jDown",
    #"_CMS_scaleRelativePtHF_jUp","_CMS_scaleRelativePtHF_jDown",
    #"_CMS_scaleRelativeBal_jUp","_CMS_scaleRelativeBal_jDown",
    #"_CMS_scaleRelativeFSR_jUp","_CMS_scaleRelativeFSR_jDown",
    #"_CMS_scaleRelativeStatFSR_jUp","_CMS_scaleRelativeStatFSR_jDown",
    #"_CMS_scaleRelativeStatEC_jUp","_CMS_scaleRelativeStatEC_jDown",
    #"_CMS_scaleRelativeStatHF_jUp","_CMS_scaleRelativeStatHF_jDown",
    #"_CMS_scalePileUpDataMC_jUp","_CMS_scalePileUpDataMC_jDown",
    #"_CMS_scalePileUpPtRef_jUp","_CMS_scalePileUpPtRef_jDown",
    #"_CMS_scalePileUpPtBB_jUp","_CMS_scalePileUpPtBB_jDown",
    #"_CMS_scalePileUpPtEC1_jUp","_CMS_scalePileUpPtEC1_jDown",
    #"_CMS_scalePileUpPtEC2_jUp","_CMS_scalePileUpPtEC2_jDown",
    #"_CMS_scalePileUpPtHF_jUp","_CMS_scalePileUpPtHF_jDown",
    #"_CMS_scalePileUpMuZero_jUp","_CMS_scalePileUpMuZero_jDown",
    #"_CMS_scalePileUpEnvelope_jUp","_CMS_scalePileUpEnvelope_jDown",
    #"_CMS_scaleSubTotalPileUp_jUp","_CMS_scaleSubTotalPileUp_jDown",
    #"_CMS_scaleSubTotalRelative_jUp","_CMS_scaleSubTotalRelative_jDown",
    #"_CMS_scaleSubTotalPt_jUp","_CMS_scaleSubTotalPt_jDown",
    #"_CMS_scaleSubTotalScale_jUp","_CMS_scaleSubTotalScale_jDown",
    #"_CMS_scaleSubTotalAbsolute_jUp","_CMS_scaleSubTotalAbsolute_jDown",
    #"_CMS_scaleSubTotalMC_jUp","_CMS_scaleSubTotalMC_jDown",
    #"_CMS_scaleTotal_jUp","_CMS_scaleTotal_jDown",
    #"_CMS_scaleTotalNoFlavor_jUp","_CMS_scaleTotalNoFlavor_jDown",
    #"_CMS_scaleTotalNoTime_jUp","_CMS_scaleTotalNoTime_jDown",
    #"_CMS_scaleTotalNoFlavorNoTime_jUp","_CMS_scaleTotalNoFlavorNoTime_jDown",
    #"_CMS_scaleFlavorZJet_jUp","_CMS_scaleFlavorZJet_jDown",
    #"_CMS_scaleFlavorPhotonJet_jUp","_CMS_scaleFlavorPhotonJet_jDown",
    #"_CMS_scaleFlavorPureGluon_jUp","_CMS_scaleFlavorPureGluon_jDown",
    #"_CMS_scaleFlavorPureQuark_jUp","_CMS_scaleFlavorPureQuark_jDown",
    #"_CMS_scaleFlavorPureCharm_jUp","_CMS_scaleFlavorPureCharm_jDown",
    #"_CMS_scaleFlavorPureBottom_jUp","_CMS_scaleFlavorPureBottom_jDown",
    #"_CMS_scaleTimeRunBCD_jUp","_CMS_scaleTimeRunBCD_jDown",
    #"_CMS_scaleTimeRunEF_jUp","_CMS_scaleTimeRunEF_jDown",
    #"_CMS_scaleTimeRunG_jUp","_CMS_scaleTimeRunG_jDown",
    #"_CMS_scaleTimeRunH_jUp","_CMS_scaleTimeRunH_jDown",

  "_CMS_ttHbb_QCDScaleFactorUp","_CMS_ttHbb_QCDScaleFactorDown",
  "_CMS_ttHbb_scaleMuFUp",
  "_CMS_ttHbb_scaleMuFDown",
  "_CMS_ttHbb_scaleMuRUp",
  "_CMS_ttHbb_scaleMuRDown",  
  "_CMS_ttHbb_PDFUp",
  "_CMS_ttHbb_PDFDown",
]+systs_tt_all


errorSystNamesNoQCD=[
                    "",
                   "_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   "_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   "_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   "_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
##                    "_CMS_ttHbb_TopPtUp","_CMS_ttHbb_TopPtDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarOtherUp","_CMS_ttHbb_Q2scale_ttbarOtherDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlusBUp","_CMS_ttHbb_Q2scale_ttbarPlusBDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlus2BUp","_CMS_ttHbb_Q2scale_ttbarPlus2BDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlusBBbarUp","_CMS_ttHbb_Q2scale_ttbarPlusBBbarDown",
                    ##"_CMS_ttHbb_Q2scale_ttbarPlusCCbarUp","_CMS_ttHbb_Q2scale_ttbarPlusCCbarDown",
##                    "_CMS_ttHbb_NNPDFUp","_CMS_ttHbb_NNPDFDown",
                   "_CMS_effTrigger_eUp","_CMS_effTrigger_eDown",  
                   "_CMS_effTrigger_mUp","_CMS_effTrigger_mDown",  
###                     "_CMS_ttHbb_ljets_TrigUp","_CMS_ttHbb_ljets_TrigDown",
                    "_CMS_eff_eUp","_CMS_eff_eDown", 
                   "_CMS_eff_mUp","_CMS_eff_mDown",  
                    "_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",

                   ##"_CMS_ttHbb_eff_leptonUp","_CMS_ttHbb_eff_leptonDown",
                   ##"_CMS_res_jUp","_CMS_res_jDown",
                    ##"_CMS_scale_jUp","_CMS_scale_jDown",
                    ##"_CMS_ttHbb_PSscaleUp","_CMS_ttHbb_PSscaleDown",

    #"_CMS_scale_jUp","_CMS_scale_jDown",
    #"_CMS_res_jUp","_CMS_res_jDown",
    #"_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
    #"_CMS_scaleAbsoluteScale_jUp","_CMS_scaleAbsoluteScale_jDown",
    ##"_CMS_scaleAbsoluteFlavMap_jUp","_CMS_scaleAbsoluteFlavMap_jDown",
    #"_CMS_scaleAbsoluteMPFBias_jUp","_CMS_scaleAbsoluteMPFBias_jDown",
    #"_CMS_scaleFragmentation_jUp","_CMS_scaleFragmentation_jDown",
    #"_CMS_scaleSinglePionECAL_jUp","_CMS_scaleSinglePionECAL_jDown",
    #"_CMS_scaleSinglePionHCAL_jUp","_CMS_scaleSinglePionHCAL_jDown",
    #"_CMS_scaleFlavorQCD_jUp","_CMS_scaleFlavorQCD_jDown",
    #"_CMS_scaleTimePtEta_jUp","_CMS_scaleTimePtEta_jDown",
    #"_CMS_scaleRelativeJEREC1_jUp","_CMS_scaleRelativeJEREC1_jDown",
    #"_CMS_scaleRelativeJEREC2_jUp","_CMS_scaleRelativeJEREC2_jDown",
    #"_CMS_scaleRelativeJERHF_jUp","_CMS_scaleRelativeJERHF_jDown",
    #"_CMS_scaleRelativePtBB_jUp","_CMS_scaleRelativePtBB_jDown",
    #"_CMS_scaleRelativePtEC1_jUp","_CMS_scaleRelativePtEC1_jDown",
    #"_CMS_scaleRelativePtEC2_jUp","_CMS_scaleRelativePtEC2_jDown",
    #"_CMS_scaleRelativePtHF_jUp","_CMS_scaleRelativePtHF_jDown",
    #"_CMS_scaleRelativeBal_jUp","_CMS_scaleRelativeBal_jDown",
    #"_CMS_scaleRelativeFSR_jUp","_CMS_scaleRelativeFSR_jDown",
    #"_CMS_scaleRelativeStatFSR_jUp","_CMS_scaleRelativeStatFSR_jDown",
    #"_CMS_scaleRelativeStatEC_jUp","_CMS_scaleRelativeStatEC_jDown",
    #"_CMS_scaleRelativeStatHF_jUp","_CMS_scaleRelativeStatHF_jDown",
    #"_CMS_scalePileUpDataMC_jUp","_CMS_scalePileUpDataMC_jDown",
    #"_CMS_scalePileUpPtRef_jUp","_CMS_scalePileUpPtRef_jDown",
    #"_CMS_scalePileUpPtBB_jUp","_CMS_scalePileUpPtBB_jDown",
    #"_CMS_scalePileUpPtEC1_jUp","_CMS_scalePileUpPtEC1_jDown",
    #"_CMS_scalePileUpPtEC2_jUp","_CMS_scalePileUpPtEC2_jDown",
    #"_CMS_scalePileUpPtHF_jUp","_CMS_scalePileUpPtHF_jDown",
    ##"_CMS_scalePileUpMuZero_jUp","_CMS_scalePileUpMuZero_jDown",
    #"_CMS_scalePileUpEnvelope_jUp","_CMS_scalePileUpEnvelope_jDown",
    #"_CMS_scaleSubTotalPileUp_jUp","_CMS_scaleSubTotalPileUp_jDown",
    #"_CMS_scaleSubTotalRelative_jUp","_CMS_scaleSubTotalRelative_jDown",
    #"_CMS_scaleSubTotalPt_jUp","_CMS_scaleSubTotalPt_jDown",
    #"_CMS_scaleSubTotalScale_jUp","_CMS_scaleSubTotalScale_jDown",
    #"_CMS_scaleSubTotalAbsolute_jUp","_CMS_scaleSubTotalAbsolute_jDown",
    #"_CMS_scaleSubTotalMC_jUp","_CMS_scaleSubTotalMC_jDown",
    #"_CMS_scaleTotal_jUp","_CMS_scaleTotal_jDown",
    #"_CMS_scaleTotalNoFlavor_jUp","_CMS_scaleTotalNoFlavor_jDown",
    #"_CMS_scaleTotalNoTime_jUp","_CMS_scaleTotalNoTime_jDown",
    #"_CMS_scaleTotalNoFlavorNoTime_jUp","_CMS_scaleTotalNoFlavorNoTime_jDown",
    #"_CMS_scaleFlavorZJet_jUp","_CMS_scaleFlavorZJet_jDown",
    #"_CMS_scaleFlavorPhotonJet_jUp","_CMS_scaleFlavorPhotonJet_jDown",
    #"_CMS_scaleFlavorPureGluon_jUp","_CMS_scaleFlavorPureGluon_jDown",
    #"_CMS_scaleFlavorPureQuark_jUp","_CMS_scaleFlavorPureQuark_jDown",
    #"_CMS_scaleFlavorPureCharm_jUp","_CMS_scaleFlavorPureCharm_jDown",
    #"_CMS_scaleFlavorPureBottom_jUp","_CMS_scaleFlavorPureBottom_jDown",
    #"_CMS_scaleTimeRunBCD_jUp","_CMS_scaleTimeRunBCD_jDown",
    #"_CMS_scaleTimeRunEF_jUp","_CMS_scaleTimeRunEF_jDown",
    #"_CMS_scaleTimeRunG_jUp","_CMS_scaleTimeRunG_jDown",
    #"_CMS_scaleTimeRunH_jUp","_CMS_scaleTimeRunH_jDown",
  "","",
  "_CMS_ttHbb_scaleMuFUp",
  "_CMS_ttHbb_scaleMuFDown",
  "_CMS_ttHbb_scaleMuRUp",
  "_CMS_ttHbb_scaleMuRDown",  
  "_CMS_ttHbb_PDFUp",
  "_CMS_ttHbb_PDFDown",
]+systs_tt_all



#assert len(errorSystNames)==len(weightSystNames+otherSystNames+PSSystNames+QCDSystNames)

# samples
# input path 
#path_Matthias="/nfs/dust/cms/user/matsch/ntuples/Spring17/v3"
path_additionalSamples="/nfs/dust/cms/user/kelmorab/trees_Spring17_v5_additional"
#path_data="/nfs/dust/cms/user/mwassmer/ntuples/data_json"
path_michael="/nfs/dust/cms/user/mwassmer/ntuples/august17"
path_qcd_samples = "/nfs/dust/cms/user/mwassmer/ntuples/QCD_Estimation_alternative"
path_karim="/nfs/dust/cms/user/kelmorab/trees_Spring17_v5"
ttbarPathS=path_karim+'/ttbar_incl/*nominal*.root'+';'+path_karim+'/ttbar_excl_SL/*nominal*.root'+';'+path_michael+'/ttbar_excl_DL_0/*nominal*.root'
iso_inverted_paths=path_qcd_samples+'/Single*/*nominal*.root'+';'+path_qcd_samples+'/ttbar_excl_SL_0/*nominal*.root'+';'+path_qcd_samples+'/ttbar_excl_DL_0/*nominal*.root'+';'+path_qcd_samples+'/WJets-HT-*/*nominal*.root'+';'+path_qcd_samples+'/Zjets*/*nominal*.root'+';'+path_qcd_samples+'/??_0/*nominal*.root'+';'+path_qcd_samples+'/ttHbb*/*nominal*.root'+';'+path_qcd_samples+'/ttHnonbb*/*nominal*.root'+';'+path_qcd_samples+'/tt?_*/*nominal*.root'+';'+path_qcd_samples+'/st*/*nominal*.root'



# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
sampleDict=SampleDictionary()
sampleDict.doPrintout()

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
                    Sample('SingleMu',ROOT.kBlack,path_karim+'/SingleMuon*/*nominal*.root',sel_singlemu+sel_MET,'SingleMu',samDict=sampleDict),
                    Sample('SingleEl',ROOT.kBlack,path_karim+'/SingleElectron*/*nominal*.root',sel_singleel+sel_MET,'SingleEl',samDict=sampleDict)
]

## DANGERZONE 
# Recheck these numbers !!!
# Use incl and SL samples together
# SL sample has nominally 152720952  events
# After skims but before ntupling at least 4 SL files are missing with events 235523/58319342 = 0.004038506 -> 0.995961494
# incl sample has 77229341 events
# branching for Single lepton = 43.8 (pdg) -> nSL = 77229341*0.438 + 152720952*0.995961494
# the total number of SL events in both samples is 185930638.8770223 . This also included the fact that 3 MiniAOD files are missing
# the ttbar DL sample has a total of 79092400 events
# branching dfraction is 10.5% 
# ttbarDL + BF*ttbar_incl = 79092400 + 0.105*77229341 = 87201480.805
# Now Calculate new XS weights to mix the samples together
# incl ttbar XS = 831.76
# SL ttbar XS = 831.76*0.438 = 364.31088
# => weight had  831.76*1000/77229341 = 0.01077
# => weight DL 831.76*0.105*1000/87201480.805 = 0.001001529
# => weight SL = 364.31088*1000/185930638.8770223 = 0.00195939

ttbarMCWeight='*((0.001958064*(N_GenTopHad==1 && N_GenTopLep==1)+0.001001529*(N_GenTopLep==2 && N_GenTopHad==0)+0.01077*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)'


# Now for the ttbb sherpa sample:
# the weighted number of events here is 20.924893208852154 with >=4j >=2t und ttbb definition without the GenValue
# the weighted number of events here is 3675937.4093933105 with >=4j >=2t und ttbb definition with the GenValue
# the number in powheg = 10897.337975859642 for 35.918 fb
# to get the same yield we have to multiply the ttbb sherpa weights with 10897.337975859642/35.918/20.924893208852154 = 14.499232841620643
# and 
# 10897.337975859642/35.918/3675937.4093933105 = 8.253538214386172e-05
specialSherpaWeight='*14.49923'
specialSherpaWeightWithGenValue='*0.000082535*abs(Weight_GenValue)'
ttbarSherpaPath=path_additionalSamples+"/ttbb_sherpa_ol/*nominal*root"

#DANGERZONE
# need also to correct for the pos/neg fraction of ttH
# ttHbb:
# nGen=3845992
# xs=0.2953
# weight_noposneg = xs*1000/nGen = 7.67812309542e-05
# Having negative and positive events changes the weight calculation to
# weight_posneg = (xs*1000/nGen = 7.67812309542e-05)/((pos-neg)/total)
# But we only have the ratio of r=neg/pos at this moment
# => corrFactor=1.0/((pos-r*pos)/total)
# and with total=pos+neg = pos+r*pos 
# follows corrFactor =1.0/( (1+r)/(1-r) )
# => weight_new=corrFactor*weight_old
# With a r=neg/pos=0.010039594265217715
corrFactor_posneg_ttHbb = "*((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5)*1.02028 + 1.0*(!(abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5)))"

# and for ttHnonbb
corrFactor_posneg_ttHnonbb ="*((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5)*1.0 + 1.02166*(!(abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5)))"

# correction factors to take even/odd splitting into account 
evenWeight_ttH = "*((N_Jets>=6&&N_BTagsM==2)*1.00259034198 + (N_Jets==4&&N_BTagsM==3)*0.993218447691 + (N_Jets==5&&N_BTagsM==3)*1.00531861013 + (N_Jets>=6&&N_BTagsM==3)*0.99788182971 + (N_Jets==4&&N_BTagsM>=4)*0.995369893223 + (N_Jets==5&&N_BTagsM>=4)*0.996719815245 + (N_Jets>=6&&N_BTagsM>=4)*1.00269083017 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttH_hbb = "*((N_Jets>=6&&N_BTagsM==2)*1.00401305677 + (N_Jets==4&&N_BTagsM==3)*0.992461831261 + (N_Jets==5&&N_BTagsM==3)*1.00665379522 + (N_Jets>=6&&N_BTagsM==3)*0.999294824768 + (N_Jets==4&&N_BTagsM>=4)*0.994934728544 + (N_Jets==5&&N_BTagsM>=4)*0.995972029483 + (N_Jets>=6&&N_BTagsM>=4)*1.00386335248 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttH_hcc = "*((N_Jets>=6&&N_BTagsM==2)*1.02933684902 + (N_Jets==4&&N_BTagsM==3)*0.969233705254 + (N_Jets==5&&N_BTagsM==3)*1.07442421713 + (N_Jets>=6&&N_BTagsM==3)*0.939579319546 + (N_Jets==4&&N_BTagsM>=4)*1.44559873446 + (N_Jets==5&&N_BTagsM>=4)*0.93259195499 + (N_Jets>=6&&N_BTagsM>=4)*0.988910117375 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttH_hww = "*((N_Jets>=6&&N_BTagsM==2)*1.0072749693 + (N_Jets==4&&N_BTagsM==3)*1.01913462971 + (N_Jets==5&&N_BTagsM==3)*1.00246353815 + (N_Jets>=6&&N_BTagsM==3)*0.995483524925 + (N_Jets==4&&N_BTagsM>=4)*1.13175517892 + (N_Jets==5&&N_BTagsM>=4)*1.05318209121 + (N_Jets>=6&&N_BTagsM>=4)*0.976690141824 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttH_hzz = "*((N_Jets>=6&&N_BTagsM==2)*0.96154443077 + (N_Jets==4&&N_BTagsM==3)*0.979948488426 + (N_Jets==5&&N_BTagsM==3)*0.918107925149 + (N_Jets>=6&&N_BTagsM==3)*1.00294817123 + (N_Jets==4&&N_BTagsM>=4)*1.18893936333 + (N_Jets==5&&N_BTagsM>=4)*0.971677675169 + (N_Jets>=6&&N_BTagsM>=4)*1.11350611091 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttH_htt = "*((N_Jets>=6&&N_BTagsM==2)*0.98931520386 + (N_Jets==4&&N_BTagsM==3)*1.04376582688 + (N_Jets==5&&N_BTagsM==3)*0.967505946821 + (N_Jets>=6&&N_BTagsM==3)*0.982411625155 + (N_Jets==4&&N_BTagsM>=4)*0.692924564086 + (N_Jets==5&&N_BTagsM>=4)*1.18728634504 + (N_Jets>=6&&N_BTagsM>=4)*0.84891962106 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttH_hgg = "*((N_Jets>=6&&N_BTagsM==2)*0.977549831446 + (N_Jets==4&&N_BTagsM==3)*1.38639077739 + (N_Jets==5&&N_BTagsM==3)*1.17250328444 + (N_Jets>=6&&N_BTagsM==3)*1.90302173909 + (N_Jets>=6&&N_BTagsM>=4)*0.501357836064 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttH_hgluglu = "*((N_Jets>=6&&N_BTagsM==2)*0.995675201646 + (N_Jets==4&&N_BTagsM==3)*0.932422744087 + (N_Jets==5&&N_BTagsM==3)*0.984314909964 + (N_Jets>=6&&N_BTagsM==3)*0.999811574701 + (N_Jets==4&&N_BTagsM>=4)*0.759757163734 + (N_Jets==5&&N_BTagsM>=4)*1.0767902998 + (N_Jets>=6&&N_BTagsM>=4)*1.06001906365 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttH_hzg = "*((N_Jets>=6&&N_BTagsM==2)*0.955776288592 + (N_Jets==4&&N_BTagsM==3)*1.28839073053 + (N_Jets==5&&N_BTagsM==3)*1.15772752057 + (N_Jets>=6&&N_BTagsM==3)*0.911383632984 + (N_Jets==4&&N_BTagsM>=4)*0.767450585102 + (N_Jets>=6&&N_BTagsM>=4)*0.914383605909 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttbarOther = "*((N_Jets>=6&&N_BTagsM==2)*1.00034485799 + (N_Jets==4&&N_BTagsM==3)*0.999721880196 + (N_Jets==5&&N_BTagsM==3)*1.00245164082 + (N_Jets>=6&&N_BTagsM==3)*0.992863302453 + (N_Jets==4&&N_BTagsM>=4)*0.980003485631 + (N_Jets==5&&N_BTagsM>=4)*1.02109352629 + (N_Jets>=6&&N_BTagsM>=4)*0.980264790403 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttbarPlusB = "*((N_Jets>=6&&N_BTagsM==2)*0.998657571164 + (N_Jets==4&&N_BTagsM==3)*1.00234957317 + (N_Jets==5&&N_BTagsM==3)*1.01189419133 + (N_Jets>=6&&N_BTagsM==3)*0.990403631007 + (N_Jets==4&&N_BTagsM>=4)*1.03391421004 + (N_Jets==5&&N_BTagsM>=4)*0.988297188392 + (N_Jets>=6&&N_BTagsM>=4)*1.02629639163 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttbarPlus2B = "*((N_Jets>=6&&N_BTagsM==2)*1.0011011967 + (N_Jets==4&&N_BTagsM==3)*0.998672303154 + (N_Jets==5&&N_BTagsM==3)*1.00005381083 + (N_Jets>=6&&N_BTagsM==3)*1.00790722387 + (N_Jets==4&&N_BTagsM>=4)*1.05014046552 + (N_Jets==5&&N_BTagsM>=4)*1.00503439176 + (N_Jets>=6&&N_BTagsM>=4)*1.02482458405 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttbarPlusBBbar = "*((N_Jets>=6&&N_BTagsM==2)*0.997740414419 + (N_Jets==4&&N_BTagsM==3)*0.996447054425 + (N_Jets==5&&N_BTagsM==3)*0.999155544707 + (N_Jets>=6&&N_BTagsM==3)*0.998067271837 + (N_Jets==4&&N_BTagsM>=4)*1.01253849135 + (N_Jets==5&&N_BTagsM>=4)*0.991172816531 + (N_Jets>=6&&N_BTagsM>=4)*1.00226402447 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"
evenWeight_ttbarPlusCCbar = "*((N_Jets>=6&&N_BTagsM==2)*1.00111281833 + (N_Jets==4&&N_BTagsM==3)*1.00212184704 + (N_Jets==5&&N_BTagsM==3)*0.999470938958 + (N_Jets>=6&&N_BTagsM==3)*1.00454308971 + (N_Jets==4&&N_BTagsM>=4)*1.01824667 + (N_Jets==5&&N_BTagsM>=4)*1.02429204075 + (N_Jets>=6&&N_BTagsM>=4)*0.992977729595 + 1.0*(N_Jets==4 && N_BTagsM==2) + 1.0*(N_Jets==5 && N_BTagsM==2))"







print "controlsamples"
samplesControlPlots=[
                    #Sample('t#bar{t}H',ROOT.kBlue+1,path_karim+'/ttH*/*nominal*.root',mcWeightAll+sel_MET+corrFactor_posneg_ttHbb+corrFactor_posneg_ttHnonbb,'ttH',systsAllSamples,samDict=sampleDict) ,     
##                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight,'ttbar',systsAllSamples) ,     
                    #Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict),
                    #Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict),
                    #Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict),
                    #Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict),
                    #Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict),  
                    #Sample('Single Top',ROOT.kMagenta,path_karim+'/st*/*nominal*.root',mcWeightAll+sel_MET,'SingleTop',systsAllSamples,samDict=sampleDict) , 
                    #Sample('V+jets',ROOT.kGreen-3,path_karim+'/*ets*/*nominal*.root',mcWeightAll+sel_MET,'Vjets',systsAllSamples,samDict=sampleDict) , 
                    #Sample('t#bar{t}+V',ROOT.kBlue-10,path_karim+'/tt?_*/*nominal*.root',mcWeightAll+sel_MET,'ttV',systsAllSamples,samDict=sampleDict),         
                    #Sample('Diboson',ROOT.kAzure+2,path_karim+'/??_pythia_*/*nominal*.root',mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict) , 
                    #Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict),  
]

#print "limit samples"
samplesLimits=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_karim+'/ttH*/*nominal*.root',mcWeight+evenSel+sel_MET+corrFactor_posneg_ttHbb+corrFactor_posneg_ttHnonbb+evenWeight_ttH,'ttH',systsAllSamples,samDict=sampleDict) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight+evenSel,'ttbar',samDict=sampleDict) ,     
                    Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_karim+'/ttHbb/*nominal*.root','1.0*'+mcWeight+evenSel+sel_MET+corrFactor_posneg_ttHbb+evenWeight_ttH_hbb,'ttH_hbb',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeightAll+hccSel+sel_MET+corrFactor_posneg_ttHnonbb,'ttH_hcc',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeightAll+httSel+sel_MET+corrFactor_posneg_ttHnonbb,'ttH_htt',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeightAll+hggSel+sel_MET+corrFactor_posneg_ttHnonbb,'ttH_hgg',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeightAll+hglugluSel+sel_MET+corrFactor_posneg_ttHnonbb,'ttH_hgluglu',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeightAll+hwwSel+sel_MET+corrFactor_posneg_ttHnonbb,'ttH_hww',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeightAll+hzzSel+sel_MET+corrFactor_posneg_ttHnonbb,'ttH_hzz',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeightAll+hzgSel+sel_MET+corrFactor_posneg_ttHnonbb,'ttH_hzg',systsAllSamples,samDict=sampleDict) ,
                    
                    #Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+evenWeight_ttbarOther,'ttbarOther',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict),
                    #Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==1)'+sel_MET+evenWeight_ttbarPlusCCbar,'ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict),
                    #Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==1)'+sel_MET+evenWeight_ttbarPlusB,'ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict),
                    #Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==2)'+sel_MET+evenWeight_ttbarPlus2B,'ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarSherpaPath,mcWeightAll+specialSherpaWeightWithGenValue+'*(GenEvt_I_TTPlusBB==3)'+sel_MET,'ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict), 
                    #Sample('Single Top',ROOT.kMagenta,path_karim+'/st*/*nominal*.root',mcWeightAll+sel_MET,'singlet',systsAllSamples,samDict=sampleDict) , 
                    #Sample('Z+jets',ROOT.kGreen-3,path_karim+'/Zjets*/*nominal*.root',mcWeightAll+sel_MET,'zjets',systsAllSamples,samDict=sampleDict) , 
                    #Sample('W+jets',ROOT.kGreen-7,path_karim+'/Wjets*/*nominal*.root',mcWeightAll+sel_MET,'wjets',systsAllSamples,samDict=sampleDict) , 
                    #Sample('t#bar{t}+W',ROOT.kBlue-10,path_karim+'/ttW_*/*nominal*.root',mcWeightAll+sel_MET,'ttbarW',systsAllSamples,samDict=sampleDict),
                    #Sample('t#bar{t}+Z',ROOT.kBlue-6,path_karim+'/ttZ_*/*nominal*.root',mcWeightAll+sel_MET,'ttbarZ',systsAllSamples,samDict=sampleDict),
                    #Sample('Diboson',ROOT.kAzure+2,path_karim+'/??_pythia_*/*nominal*.root',mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict) , 
                    #Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict),  
]
