import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(filedir+'/../../util')

 
import plotClasses

sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)*(N_Jets>=4 && N_BTagsM>=2)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0 && (N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1)))*(N_Jets>=4 && N_BTagsM>=2)" # and vice versa...
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
                   #"_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   #"_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   #"_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   #"_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
####                    "_CMS_ttHbb_TopPtUp","_CMS_ttHbb_TopPtDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarOtherUp","_CMS_ttHbb_Q2scale_ttbarOtherDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlusBUp","_CMS_ttHbb_Q2scale_ttbarPlusBDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlus2BUp","_CMS_ttHbb_Q2scale_ttbarPlus2BDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlusBBbarUp","_CMS_ttHbb_Q2scale_ttbarPlusBBbarDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlusCCbarUp","_CMS_ttHbb_Q2scale_ttbarPlusCCbarDown",
###                    "_CMS_ttHbb_NNPDFUp","_CMS_ttHbb_NNPDFDown",
                  #"_CMS_effTrigger_eUp","_CMS_effTrigger_eDown",  
                   #"_CMS_effTrigger_mUp","_CMS_effTrigger_mDown",  
###                     "_CMS_ttHbb_ljets_TrigUp","_CMS_ttHbb_ljets_TrigDown",
                   #"_CMS_eff_eUp","_CMS_eff_eDown", 
                   #"_CMS_eff_mUp","_CMS_eff_mDown",
                   #"_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",
		  ##"_CMS_ttHbb_eff_leptonUp","_CMS_ttHbb_eff_leptonDown",
                   ##"_CMS_res_jUp","_CMS_res_jDown"
                    ##"_CMS_scale_jUp","_CMS_scale_jDown",
]

systsAllSamples=[
                    "",
                   #"_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   #"_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   #"_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   #"_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
                  #"_CMS_effTrigger_eUp","_CMS_effTrigger_eDown",  
                   #"_CMS_effTrigger_mUp","_CMS_effTrigger_mDown",  
                    ##"_CMS_ttHbb_ljets_TrigUp","_CMS_ttHbb_ljets_TrigDown",
                    #"_CMS_eff_eUp","_CMS_eff_eDown", 
                   #"_CMS_eff_mUp","_CMS_eff_mDown",  
                   #"_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",

                   ##"_CMS_ttHbb_eff_leptonUp","_CMS_ttHbb_eff_leptonDown",
                   ###"_CMS_res_jUp","_CMS_res_jDown",
                    ###"_CMS_scale_jUp","_CMS_scale_jDown",
 #"_CMS_scale_jUp","_CMS_scale_jDown",
    #"_CMS_res_jUp","_CMS_res_jDown",
    ##"_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
    ##"_CMS_scaleAbsoluteScale_jUp","_CMS_scaleAbsoluteScale_jDown",
    ###"_CMS_scaleAbsoluteFlavMap_jUp","_CMS_scaleAbsoluteFlavMap_jDown",
    ##"_CMS_scaleAbsoluteMPFBias_jUp","_CMS_scaleAbsoluteMPFBias_jDown",
    ##"_CMS_scaleFragmentation_jUp","_CMS_scaleFragmentation_jDown",
    ##"_CMS_scaleSinglePionECAL_jUp","_CMS_scaleSinglePionECAL_jDown",
    ##"_CMS_scaleSinglePionHCAL_jUp","_CMS_scaleSinglePionHCAL_jDown",
    ##"_CMS_scaleFlavorQCD_jUp","_CMS_scaleFlavorQCD_jDown",
    ##"_CMS_scaleTimePtEta_jUp","_CMS_scaleTimePtEta_jDown",
    ##"_CMS_scaleRelativeJEREC1_jUp","_CMS_scaleRelativeJEREC1_jDown",
    ##"_CMS_scaleRelativeJEREC2_jUp","_CMS_scaleRelativeJEREC2_jDown",
    ##"_CMS_scaleRelativeJERHF_jUp","_CMS_scaleRelativeJERHF_jDown",
    ##"_CMS_scaleRelativePtBB_jUp","_CMS_scaleRelativePtBB_jDown",
    ##"_CMS_scaleRelativePtEC1_jUp","_CMS_scaleRelativePtEC1_jDown",
    ##"_CMS_scaleRelativePtEC2_jUp","_CMS_scaleRelativePtEC2_jDown",
    ##"_CMS_scaleRelativePtHF_jUp","_CMS_scaleRelativePtHF_jDown",
    ##"_CMS_scaleRelativeBal_jUp","_CMS_scaleRelativeBal_jDown",
    ##"_CMS_scaleRelativeFSR_jUp","_CMS_scaleRelativeFSR_jDown",
    ##"_CMS_scaleRelativeStatFSR_jUp","_CMS_scaleRelativeStatFSR_jDown",
    ##"_CMS_scaleRelativeStatEC_jUp","_CMS_scaleRelativeStatEC_jDown",
    ##"_CMS_scaleRelativeStatHF_jUp","_CMS_scaleRelativeStatHF_jDown",
    ##"_CMS_scalePileUpDataMC_jUp","_CMS_scalePileUpDataMC_jDown",
    ##"_CMS_scalePileUpPtRef_jUp","_CMS_scalePileUpPtRef_jDown",
    ##"_CMS_scalePileUpPtBB_jUp","_CMS_scalePileUpPtBB_jDown",
    ##"_CMS_scalePileUpPtEC1_jUp","_CMS_scalePileUpPtEC1_jDown",
    ##"_CMS_scalePileUpPtEC2_jUp","_CMS_scalePileUpPtEC2_jDown",
    ##"_CMS_scalePileUpPtHF_jUp","_CMS_scalePileUpPtHF_jDown",
    ##"_CMS_scalePileUpMuZero_jUp","_CMS_scalePileUpMuZero_jDown",
    ##"_CMS_scalePileUpEnvelope_jUp","_CMS_scalePileUpEnvelope_jDown",
    ##"_CMS_scaleSubTotalPileUp_jUp","_CMS_scaleSubTotalPileUp_jDown",
    ##"_CMS_scaleSubTotalRelative_jUp","_CMS_scaleSubTotalRelative_jDown",
    ##"_CMS_scaleSubTotalPt_jUp","_CMS_scaleSubTotalPt_jDown",
    ##"_CMS_scaleSubTotalScale_jUp","_CMS_scaleSubTotalScale_jDown",
    ##"_CMS_scaleSubTotalAbsolute_jUp","_CMS_scaleSubTotalAbsolute_jDown",
    ##"_CMS_scaleSubTotalMC_jUp","_CMS_scaleSubTotalMC_jDown",
    ##"_CMS_scaleTotal_jUp","_CMS_scaleTotal_jDown",
    ##"_CMS_scaleTotalNoFlavor_jUp","_CMS_scaleTotalNoFlavor_jDown",
    ##"_CMS_scaleTotalNoTime_jUp","_CMS_scaleTotalNoTime_jDown",
    ##"_CMS_scaleTotalNoFlavorNoTime_jUp","_CMS_scaleTotalNoFlavorNoTime_jDown",
    ##"_CMS_scaleFlavorZJet_jUp","_CMS_scaleFlavorZJet_jDown",
    ##"_CMS_scaleFlavorPhotonJet_jUp","_CMS_scaleFlavorPhotonJet_jDown",
    ##"_CMS_scaleFlavorPureGluon_jUp","_CMS_scaleFlavorPureGluon_jDown",
    ##"_CMS_scaleFlavorPureQuark_jUp","_CMS_scaleFlavorPureQuark_jDown",
    ##"_CMS_scaleFlavorPureCharm_jUp","_CMS_scaleFlavorPureCharm_jDown",
    ##"_CMS_scaleFlavorPureBottom_jUp","_CMS_scaleFlavorPureBottom_jDown",
    ##"_CMS_scaleTimeRunBCD_jUp","_CMS_scaleTimeRunBCD_jDown",
    ##"_CMS_scaleTimeRunEF_jUp","_CMS_scaleTimeRunEF_jDown",
    ##"_CMS_scaleTimeRunG_jUp","_CMS_scaleTimeRunG_jDown",
    #"_CMS_scaleTimeRunH_jUp","_CMS_scaleTimeRunH_jDown",

]

systsTtbar= [
  #"_CMS_ttHbb_FSRUp","_CMS_ttHbb_FSRDown",
  #"_CMS_ttHbb_ISRUp","_CMS_ttHbb_ISRDown",
  #"_CMS_ttHbb_HDAMPUp","_CMS_ttHbb_HDAMPDown",
  #"_CMS_ttHbb_UEUp","_CMS_ttHbb_UEDown",
  #"_CMS_ttHbb_scaleMuFUp",
  #"_CMS_ttHbb_scaleMuFDown",
  #"_CMS_ttHbb_scaleMuRUp",
  #"_CMS_ttHbb_scaleMuRDown",  
  #"_CMS_ttHbb_PDFUp",
  #"_CMS_ttHbb_PDFDown",
  
  
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
                   #"dummyWeight_CSVLFup:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFUp*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFdown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFDown*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFup:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFUp*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFdown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFDown*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFStats1up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats1Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFStats1down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats1Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFStats1up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats1Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFStats1down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats1Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFStats2up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats2Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVHFStats2down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVHFStats2Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFStats2up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats2Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVLFStats2down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVLFStats2Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr1up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr1Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr1down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr1Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr2up:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr2Up*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   #"dummyWeight_CSVCErr2down:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight_CSVCErr2Down*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
                   
                   ##"dummyWeight_CMS_ttH_PUUp:="+"(1*Weight_pu69p2Up*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",

		   ##"dummyWeight_CMS_ttH_PUDown:="+"(1*Weight_pu69p2Down*((Weight>0)-(Weight<0)))"+"*"+sfs+"*"+mcTriggerWeight+"*internalCSVweight*(DoWeights==1)+(DoWeights==0)*1.0",

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
		    
		    #"dummyWeightQCDScaleFactor_=
]



Q2SystWeights= [

                #"dummyWeight_CMS_ttH_scaleMuRDown:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_0p5_muF_1p0*Weight_scale_variation_muR_0p5_muF_1p0)*(DoWeights==1)+(DoWeights==0)*1.0)",
                #"dummyWeight_CMS_ttH_scaleMuRUp:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_2p0_muF_1p0*Weight_scale_variation_muR_2p0_muF_1p0)*(DoWeights==1)+(DoWeights==0)*1.0)",
                #"dummyWeight_CMS_ttH_scaleMuFDown:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_1p0_muF_0p5*Weight_scale_variation_muR_1p0_muF_0p5)*(DoWeights==1)+(DoWeights==0)*1.0)",
                #"dummyWeight_CMS_ttH_scaleMuFUp:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_1p0_muF_2p0*Weight_scale_variation_muR_1p0_muF_2p0)*(DoWeights==1)+(DoWeights==0)*1.0)",
                #"dummyWeight_CMS_ttH_scaleMEDown:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_0p5_muF_0p5*Weight_scale_variation_muR_0p5_muF_0p5)*(DoWeights==1)+(DoWeights==0)*1.0)",
                #"dummyWeight_CMS_ttH_scaleMEUp:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_2p0_muF_2p0*Weight_scale_variation_muR_2p0_muF_2p0)*(DoWeights==1)+(DoWeights==0)*1.0)",
                #"dummyWeight_CMS_ttH_Q2_muR_Up_muF_Down:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_2p0_muF_0p5*Weight_scale_variation_muR_2p0_muF_0p5)*(DoWeights==1)+(DoWeights==0)*1.0)",        
                #"dummyWeight_CMS_ttH_Q2_muR_Down_muF_Up:=(("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalNormFactor_Weight_scale_variation_muR_0p5_muF_2p0*Weight_scale_variation_muR_0p5_muF_2p0)*(DoWeights==1)+(DoWeights==0)*1.0)",
]

Q2SystNames= [

                #"_CMS_ttHbb_scaleMuRDown",
                #"_CMS_ttHbb_scaleMuRUp",
                #"_CMS_ttHbb_scaleMuFDown",
                #"_CMS_ttHbb_scaleMuFUp",
                #"_CMS_ttHbb_scaleMEDown",
                #"_CMS_ttHbb_scaleMEUp",
                #"_CMS_ttHbb_scaleMuRupMuFdown",
                #"_CMS_ttHbb_scaleMuRdownMuFup",
]

PDFSystWeights= [

                #"dummyWeight_CMS_ttH_PDFUp:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalPDFweightUp*(DoWeights==1)+(DoWeights==0)*1.0)",
                #"dummyWeight_CMS_ttH_PDFDown:=("+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*internalPDFweightDown*(DoWeights==1)+(DoWeights==0)*1.0)"
                
]

PDFSystNames= [

                #"_CMS_ttHbb_PDFUp",
                #"_CMS_ttHbb_PDFDown",

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


#systWeights+=Q2SystWeights+PDFSystWeights+systs_tt_all_weights
#weightSystNames+=Q2SystNames+PDFSystNames+systs_tt_all


assert len(systWeights)==len(weightSystNames)

otherSystNames=[
                    #"_CMS_scale_jUp",
                    #"_CMS_scale_jDown",
                   #"_CMS_res_jUp",
                   #"_CMS_res_jDown"
                    ##"_CMS_ttHbb_PSscaleUp",
                    ###"_CMS_ttHbb_PSscaleDown"
    #"_CMS_scale_jUp","_CMS_scale_jDown",
    #"_CMS_res_jUp","_CMS_res_jDown",
    ##"_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
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
  #"_CMS_ttHbb_QCDScaleFactorUp","_CMS_ttHbb_QCDScaleFactorDown",
  ]
QCDSystReplacementStrings=[
  #"internalQCDweightup","internalQCDweightdown",
  ]



errorSystNamesNoPS=[
                    "",
                   #"_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   #"_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   #"_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   #"_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
###                    "_CMS_ttHbb_TopPtUp","_CMS_ttHbb_TopPtDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarOtherUp","_CMS_ttHbb_Q2scale_ttbarOtherDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlusBUp","_CMS_ttHbb_Q2scale_ttbarPlusBDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlus2BUp","_CMS_ttHbb_Q2scale_ttbarPlus2BDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlusBBbarUp","_CMS_ttHbb_Q2scale_ttbarPlusBBbarDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlusCCbarUp","_CMS_ttHbb_Q2scale_ttbarPlusCCbarDown",
###                    "_CMS_ttHbb_NNPDFUp","_CMS_ttHbb_NNPDFDown",
                   #"_CMS_effTrigger_eUp","_CMS_effTrigger_eDown",  
                   #"_CMS_effTrigger_mUp","_CMS_effTrigger_mDown",  
####                     "_CMS_ttHbb_ljets_TrigUp","_CMS_ttHbb_ljets_TrigDown",
                    #"_CMS_eff_eUp","_CMS_eff_eDown", 
                   #"_CMS_eff_mUp","_CMS_eff_mDown",  
                    #"_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",

                   ###"_CMS_ttHbb_eff_leptonUp","_CMS_ttHbb_eff_leptonDown",
                   ###"_CMS_res_jUp","_CMS_res_jDown",
                    ###"_CMS_scale_jUp","_CMS_scale_jDown",
                    ###"_CMS_ttHbb_PSscaleUp","_CMS_ttHbb_PSscaleDown",

    #"_CMS_scale_jUp","_CMS_scale_jDown",
    #"_CMS_res_jUp","_CMS_res_jDown",
    ##"_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
    ##"_CMS_scaleAbsoluteScale_jUp","_CMS_scaleAbsoluteScale_jDown",
    ###"_CMS_scaleAbsoluteFlavMap_jUp","_CMS_scaleAbsoluteFlavMap_jDown",
    ##"_CMS_scaleAbsoluteMPFBias_jUp","_CMS_scaleAbsoluteMPFBias_jDown",
    ##"_CMS_scaleFragmentation_jUp","_CMS_scaleFragmentation_jDown",
    ##"_CMS_scaleSinglePionECAL_jUp","_CMS_scaleSinglePionECAL_jDown",
    ##"_CMS_scaleSinglePionHCAL_jUp","_CMS_scaleSinglePionHCAL_jDown",
    ##"_CMS_scaleFlavorQCD_jUp","_CMS_scaleFlavorQCD_jDown",
    ##"_CMS_scaleTimePtEta_jUp","_CMS_scaleTimePtEta_jDown",
    ##"_CMS_scaleRelativeJEREC1_jUp","_CMS_scaleRelativeJEREC1_jDown",
    ##"_CMS_scaleRelativeJEREC2_jUp","_CMS_scaleRelativeJEREC2_jDown",
    ##"_CMS_scaleRelativeJERHF_jUp","_CMS_scaleRelativeJERHF_jDown",
    ##"_CMS_scaleRelativePtBB_jUp","_CMS_scaleRelativePtBB_jDown",
    ##"_CMS_scaleRelativePtEC1_jUp","_CMS_scaleRelativePtEC1_jDown",
    ##"_CMS_scaleRelativePtEC2_jUp","_CMS_scaleRelativePtEC2_jDown",
    ##"_CMS_scaleRelativePtHF_jUp","_CMS_scaleRelativePtHF_jDown",
    ##"_CMS_scaleRelativeBal_jUp","_CMS_scaleRelativeBal_jDown",
    ##"_CMS_scaleRelativeFSR_jUp","_CMS_scaleRelativeFSR_jDown",
    ##"_CMS_scaleRelativeStatFSR_jUp","_CMS_scaleRelativeStatFSR_jDown",
    ##"_CMS_scaleRelativeStatEC_jUp","_CMS_scaleRelativeStatEC_jDown",
    ##"_CMS_scaleRelativeStatHF_jUp","_CMS_scaleRelativeStatHF_jDown",
    ##"_CMS_scalePileUpDataMC_jUp","_CMS_scalePileUpDataMC_jDown",
    ##"_CMS_scalePileUpPtRef_jUp","_CMS_scalePileUpPtRef_jDown",
    ##"_CMS_scalePileUpPtBB_jUp","_CMS_scalePileUpPtBB_jDown",
    ##"_CMS_scalePileUpPtEC1_jUp","_CMS_scalePileUpPtEC1_jDown",
    ##"_CMS_scalePileUpPtEC2_jUp","_CMS_scalePileUpPtEC2_jDown",
    ##"_CMS_scalePileUpPtHF_jUp","_CMS_scalePileUpPtHF_jDown",
    ##"_CMS_scalePileUpMuZero_jUp","_CMS_scalePileUpMuZero_jDown",
    ##"_CMS_scalePileUpEnvelope_jUp","_CMS_scalePileUpEnvelope_jDown",
    ##"_CMS_scaleSubTotalPileUp_jUp","_CMS_scaleSubTotalPileUp_jDown",
    ##"_CMS_scaleSubTotalRelative_jUp","_CMS_scaleSubTotalRelative_jDown",
    ##"_CMS_scaleSubTotalPt_jUp","_CMS_scaleSubTotalPt_jDown",
    ##"_CMS_scaleSubTotalScale_jUp","_CMS_scaleSubTotalScale_jDown",
    ##"_CMS_scaleSubTotalAbsolute_jUp","_CMS_scaleSubTotalAbsolute_jDown",
    ##"_CMS_scaleSubTotalMC_jUp","_CMS_scaleSubTotalMC_jDown",
    ##"_CMS_scaleTotal_jUp","_CMS_scaleTotal_jDown",
    ##"_CMS_scaleTotalNoFlavor_jUp","_CMS_scaleTotalNoFlavor_jDown",
    ##"_CMS_scaleTotalNoTime_jUp","_CMS_scaleTotalNoTime_jDown",
    ##"_CMS_scaleTotalNoFlavorNoTime_jUp","_CMS_scaleTotalNoFlavorNoTime_jDown",
    ##"_CMS_scaleFlavorZJet_jUp","_CMS_scaleFlavorZJet_jDown",
    ##"_CMS_scaleFlavorPhotonJet_jUp","_CMS_scaleFlavorPhotonJet_jDown",
    ##"_CMS_scaleFlavorPureGluon_jUp","_CMS_scaleFlavorPureGluon_jDown",
    ##"_CMS_scaleFlavorPureQuark_jUp","_CMS_scaleFlavorPureQuark_jDown",
    ##"_CMS_scaleFlavorPureCharm_jUp","_CMS_scaleFlavorPureCharm_jDown",
    ##"_CMS_scaleFlavorPureBottom_jUp","_CMS_scaleFlavorPureBottom_jDown",
    ##"_CMS_scaleTimeRunBCD_jUp","_CMS_scaleTimeRunBCD_jDown",
    ##"_CMS_scaleTimeRunEF_jUp","_CMS_scaleTimeRunEF_jDown",
    ##"_CMS_scaleTimeRunG_jUp","_CMS_scaleTimeRunG_jDown",
    ##"_CMS_scaleTimeRunH_jUp","_CMS_scaleTimeRunH_jDown",

  ##"_CMS_ttHbb_QCDScaleFactorUp","_CMS_ttHbb_QCDScaleFactorDown",
  #"_CMS_ttHbb_scaleMuFUp",
  #"_CMS_ttHbb_scaleMuFDown",
  #"_CMS_ttHbb_scaleMuRUp",
  #"_CMS_ttHbb_scaleMuRDown",  
  #"_CMS_ttHbb_PDFUp",
  #"_CMS_ttHbb_PDFDown",
]


errorSystNamesNoQCD=[
                    "",
                   #"_CMS_btag_lfUp","_CMS_btag_lfDown","_CMS_btag_hfUp","_CMS_btag_hfDown",
                   #"_CMS_btag_hfstats1Up","_CMS_btag_hfstats1Down","_CMS_btag_lfstats1Up","_CMS_btag_lfstats1Down",
                   #"_CMS_btag_hfstats2Up","_CMS_btag_hfstats2Down","_CMS_btag_lfstats2Up","_CMS_btag_lfstats2Down",
                   #"_CMS_btag_cferr1Up","_CMS_btag_cferr1Down","_CMS_btag_cferr2Up","_CMS_btag_cferr2Down",
###                    "_CMS_ttHbb_TopPtUp","_CMS_ttHbb_TopPtDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarOtherUp","_CMS_ttHbb_Q2scale_ttbarOtherDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlusBUp","_CMS_ttHbb_Q2scale_ttbarPlusBDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlus2BUp","_CMS_ttHbb_Q2scale_ttbarPlus2BDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlusBBbarUp","_CMS_ttHbb_Q2scale_ttbarPlusBBbarDown",
                    ###"_CMS_ttHbb_Q2scale_ttbarPlusCCbarUp","_CMS_ttHbb_Q2scale_ttbarPlusCCbarDown",
###                    "_CMS_ttHbb_NNPDFUp","_CMS_ttHbb_NNPDFDown",
                   #"_CMS_effTrigger_eUp","_CMS_effTrigger_eDown",  
                   #"_CMS_effTrigger_mUp","_CMS_effTrigger_mDown",  
####                     "_CMS_ttHbb_ljets_TrigUp","_CMS_ttHbb_ljets_TrigDown",
                    #"_CMS_eff_eUp","_CMS_eff_eDown", 
                   #"_CMS_eff_mUp","_CMS_eff_mDown",  
                    #"_CMS_ttHbb_PUUp","_CMS_ttHbb_PUDown",

                   ###"_CMS_ttHbb_eff_leptonUp","_CMS_ttHbb_eff_leptonDown",
                   ###"_CMS_res_jUp","_CMS_res_jDown",
                    ###"_CMS_scale_jUp","_CMS_scale_jDown",
                    ###"_CMS_ttHbb_PSscaleUp","_CMS_ttHbb_PSscaleDown",

    #"_CMS_scale_jUp","_CMS_scale_jDown",
    #"_CMS_res_jUp","_CMS_res_jDown",
    ##"_CMS_scaleAbsoluteStat_jUp","_CMS_scaleAbsoluteStat_jDown",
    ##"_CMS_scaleAbsoluteScale_jUp","_CMS_scaleAbsoluteScale_jDown",
    ###"_CMS_scaleAbsoluteFlavMap_jUp","_CMS_scaleAbsoluteFlavMap_jDown",
    ##"_CMS_scaleAbsoluteMPFBias_jUp","_CMS_scaleAbsoluteMPFBias_jDown",
    ##"_CMS_scaleFragmentation_jUp","_CMS_scaleFragmentation_jDown",
    ##"_CMS_scaleSinglePionECAL_jUp","_CMS_scaleSinglePionECAL_jDown",
    ##"_CMS_scaleSinglePionHCAL_jUp","_CMS_scaleSinglePionHCAL_jDown",
    ##"_CMS_scaleFlavorQCD_jUp","_CMS_scaleFlavorQCD_jDown",
    ##"_CMS_scaleTimePtEta_jUp","_CMS_scaleTimePtEta_jDown",
    ##"_CMS_scaleRelativeJEREC1_jUp","_CMS_scaleRelativeJEREC1_jDown",
    ##"_CMS_scaleRelativeJEREC2_jUp","_CMS_scaleRelativeJEREC2_jDown",
    ##"_CMS_scaleRelativeJERHF_jUp","_CMS_scaleRelativeJERHF_jDown",
    ##"_CMS_scaleRelativePtBB_jUp","_CMS_scaleRelativePtBB_jDown",
    ##"_CMS_scaleRelativePtEC1_jUp","_CMS_scaleRelativePtEC1_jDown",
    ##"_CMS_scaleRelativePtEC2_jUp","_CMS_scaleRelativePtEC2_jDown",
    ##"_CMS_scaleRelativePtHF_jUp","_CMS_scaleRelativePtHF_jDown",
    ##"_CMS_scaleRelativeBal_jUp","_CMS_scaleRelativeBal_jDown",
    ##"_CMS_scaleRelativeFSR_jUp","_CMS_scaleRelativeFSR_jDown",
    ##"_CMS_scaleRelativeStatFSR_jUp","_CMS_scaleRelativeStatFSR_jDown",
    ##"_CMS_scaleRelativeStatEC_jUp","_CMS_scaleRelativeStatEC_jDown",
    ##"_CMS_scaleRelativeStatHF_jUp","_CMS_scaleRelativeStatHF_jDown",
    ##"_CMS_scalePileUpDataMC_jUp","_CMS_scalePileUpDataMC_jDown",
    ##"_CMS_scalePileUpPtRef_jUp","_CMS_scalePileUpPtRef_jDown",
    ##"_CMS_scalePileUpPtBB_jUp","_CMS_scalePileUpPtBB_jDown",
    ##"_CMS_scalePileUpPtEC1_jUp","_CMS_scalePileUpPtEC1_jDown",
    ##"_CMS_scalePileUpPtEC2_jUp","_CMS_scalePileUpPtEC2_jDown",
    ##"_CMS_scalePileUpPtHF_jUp","_CMS_scalePileUpPtHF_jDown",
    ##"_CMS_scalePileUpMuZero_jUp","_CMS_scalePileUpMuZero_jDown",
    ##"_CMS_scalePileUpEnvelope_jUp","_CMS_scalePileUpEnvelope_jDown",
    ##"_CMS_scaleSubTotalPileUp_jUp","_CMS_scaleSubTotalPileUp_jDown",
    ##"_CMS_scaleSubTotalRelative_jUp","_CMS_scaleSubTotalRelative_jDown",
    ##"_CMS_scaleSubTotalPt_jUp","_CMS_scaleSubTotalPt_jDown",
    ##"_CMS_scaleSubTotalScale_jUp","_CMS_scaleSubTotalScale_jDown",
    ##"_CMS_scaleSubTotalAbsolute_jUp","_CMS_scaleSubTotalAbsolute_jDown",
    ##"_CMS_scaleSubTotalMC_jUp","_CMS_scaleSubTotalMC_jDown",
    ##"_CMS_scaleTotal_jUp","_CMS_scaleTotal_jDown",
    ##"_CMS_scaleTotalNoFlavor_jUp","_CMS_scaleTotalNoFlavor_jDown",
    ##"_CMS_scaleTotalNoTime_jUp","_CMS_scaleTotalNoTime_jDown",
    ##"_CMS_scaleTotalNoFlavorNoTime_jUp","_CMS_scaleTotalNoFlavorNoTime_jDown",
    ##"_CMS_scaleFlavorZJet_jUp","_CMS_scaleFlavorZJet_jDown",
    ##"_CMS_scaleFlavorPhotonJet_jUp","_CMS_scaleFlavorPhotonJet_jDown",
    ##"_CMS_scaleFlavorPureGluon_jUp","_CMS_scaleFlavorPureGluon_jDown",
    ##"_CMS_scaleFlavorPureQuark_jUp","_CMS_scaleFlavorPureQuark_jDown",
    ##"_CMS_scaleFlavorPureCharm_jUp","_CMS_scaleFlavorPureCharm_jDown",
    ##"_CMS_scaleFlavorPureBottom_jUp","_CMS_scaleFlavorPureBottom_jDown",
    ##"_CMS_scaleTimeRunBCD_jUp","_CMS_scaleTimeRunBCD_jDown",
    ##"_CMS_scaleTimeRunEF_jUp","_CMS_scaleTimeRunEF_jDown",
    ##"_CMS_scaleTimeRunG_jUp","_CMS_scaleTimeRunG_jDown",
    ##"_CMS_scaleTimeRunH_jUp","_CMS_scaleTimeRunH_jDown",
  ##"","",
  #"_CMS_ttHbb_scaleMuFUp",
  #"_CMS_ttHbb_scaleMuFDown",
  #"_CMS_ttHbb_scaleMuRUp",
  #"_CMS_ttHbb_scaleMuRDown",  
  #"_CMS_ttHbb_PDFUp",
  #"_CMS_ttHbb_PDFDown",
]



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
sampleDict=plotClasses.SampleDictionary()
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


print "controlsamples"
samplesControlPlots=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_karim+'/ttH*/*nominal*.root',mcWeightAll+sel_MET,'ttH',systsAllSamples,samDict=sampleDict) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight,'ttbar',systsAllSamples) ,     
                    Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict),
                    Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict),  
                    #Sample('Single Top',ROOT.kMagenta,path_karim+'/st*/*nominal*.root',mcWeightAll+sel_MET,'SingleTop',systsAllSamples,samDict=sampleDict) , 
                    #Sample('V+jets',ROOT.kGreen-3,path_karim+'/*ets*/*nominal*.root',mcWeightAll+sel_MET,'Vjets',systsAllSamples,samDict=sampleDict) , 
                    #Sample('t#bar{t}+V',ROOT.kBlue-10,path_karim+'/tt?_*/*nominal*.root',mcWeightAll+sel_MET,'ttV',systsAllSamples,samDict=sampleDict),         
                    #Sample('Diboson',ROOT.kAzure+2,path_karim+'/??_pythia_*/*nominal*.root',mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict) , 
                    #Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict),  
]

#print "limit samples"
samplesLimits=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_karim+'/ttH*/*nominal*.root',mcWeight+evenSel+sel_MET,'ttH',systsAllSamples,samDict=sampleDict) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight+evenSel,'ttbar',samDict=sampleDict) ,     
                    Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_karim+'/ttHbb/*nominal*.root','1.0*'+mcWeight+evenSel+sel_MET,'ttH_hbb',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hccSel+sel_MET,'ttH_hcc',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+httSel+sel_MET,'ttH_htt',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hggSel+sel_MET,'ttH_hgg',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hglugluSel+sel_MET,'ttH_hgluglu',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hwwSel+sel_MET,'ttH_hww',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hzzSel+sel_MET,'ttH_hzz',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hzgSel+sel_MET,'ttH_hzg',systsAllSamples,samDict=sampleDict) ,
                    
                    Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET,'ttbarOther',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict),
                    #Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==1)'+sel_MET,'ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict),
                    #Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==1)'+sel_MET,'ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict),
                    #Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==2)'+sel_MET,'ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict),
                    #Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==3)'+sel_MET,'ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict), 
                    #Sample('Single Top',ROOT.kMagenta,path_karim+'/st*/*nominal*.root',mcWeightAll+sel_MET,'singlet',systsAllSamples,samDict=sampleDict) , 
                    #Sample('Z+jets',ROOT.kGreen-3,path_karim+'/Zjets*/*nominal*.root',mcWeightAll+sel_MET,'zjets',systsAllSamples,samDict=sampleDict) , 
                    #Sample('W+jets',ROOT.kGreen-7,path_karim+'/Wjets*/*nominal*.root',mcWeightAll+sel_MET,'wjets',systsAllSamples,samDict=sampleDict) , 
                    #Sample('t#bar{t}+W',ROOT.kBlue-10,path_karim+'/ttW_*/*nominal*.root',mcWeightAll+sel_MET,'ttbarW',systsAllSamples,samDict=sampleDict),
                    #Sample('t#bar{t}+Z',ROOT.kBlue-6,path_karim+'/ttZ_*/*nominal*.root',mcWeightAll+sel_MET,'ttbarZ',systsAllSamples,samDict=sampleDict),
                    #Sample('Diboson',ROOT.kAzure+2,path_karim+'/??_pythia_*/*nominal*.root',mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict) , 
                    #Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict),  
]
