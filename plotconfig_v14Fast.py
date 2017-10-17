import sys
import os
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *

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
                   "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                   "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                   "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                   "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
###                    "_CMS_ttH_TopPtUp","_CMS_ttH_TopPtDown",
                    ##"_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
##                    "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown",
                  "_CMS_ttH_ljets_Trig_elUp","_CMS_ttH_ljets_Trig_elDown",  
                   "_CMS_ttH_ljets_Trig_muUp","_CMS_ttH_ljets_Trig_muDown",  
##                     "_CMS_ttH_ljets_TrigUp","_CMS_ttH_ljets_TrigDown",
                   "_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown", 
                   "_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",
                   "_CMS_ttH_PUUp","_CMS_ttH_PUDown",
		  ##"_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",
                   ##"_CMS_res_jUp","_CMS_res_jDown"
                    ##"_CMS_scale_jUp","_CMS_scale_jDown",
]

systsAllSamples=[
                    "",
                   "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                   "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                   "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                   "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
                  "_CMS_ttH_ljets_Trig_elUp","_CMS_ttH_ljets_Trig_elDown",  
                   "_CMS_ttH_ljets_Trig_muUp","_CMS_ttH_ljets_Trig_muDown",  
                    #"_CMS_ttH_ljets_TrigUp","_CMS_ttH_ljets_TrigDown",
                    "_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown", 
                   "_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",  
                   "_CMS_ttH_PUUp","_CMS_ttH_PUDown",

                   #"_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",
                   ##"_CMS_res_jUp","_CMS_res_jDown",
                    ##"_CMS_scale_jUp","_CMS_scale_jDown",
 "_CMS_scale_jUp","_CMS_scale_jDown",
    "_CMS_res_jUp","_CMS_res_jDown",
    #"_CMS_scale_AbsoluteStat_jUp","_CMS_scale_AbsoluteStat_jDown",
    #"_CMS_scale_AbsoluteScale_jUp","_CMS_scale_AbsoluteScale_jDown",
    ##"_CMS_scale_AbsoluteFlavMap_jUp","_CMS_scale_AbsoluteFlavMap_jDown",
    #"_CMS_scale_AbsoluteMPFBias_jUp","_CMS_scale_AbsoluteMPFBias_jDown",
    #"_CMS_scale_Fragmentation_jUp","_CMS_scale_Fragmentation_jDown",
    #"_CMS_scale_SinglePionECAL_jUp","_CMS_scale_SinglePionECAL_jDown",
    #"_CMS_scale_SinglePionHCAL_jUp","_CMS_scale_SinglePionHCAL_jDown",
    #"_CMS_scale_FlavorQCD_jUp","_CMS_scale_FlavorQCD_jDown",
    #"_CMS_scale_TimePtEta_jUp","_CMS_scale_TimePtEta_jDown",
    #"_CMS_scale_RelativeJEREC1_jUp","_CMS_scale_RelativeJEREC1_jDown",
    #"_CMS_scale_RelativeJEREC2_jUp","_CMS_scale_RelativeJEREC2_jDown",
    #"_CMS_scale_RelativeJERHF_jUp","_CMS_scale_RelativeJERHF_jDown",
    #"_CMS_scale_RelativePtBB_jUp","_CMS_scale_RelativePtBB_jDown",
    #"_CMS_scale_RelativePtEC1_jUp","_CMS_scale_RelativePtEC1_jDown",
    #"_CMS_scale_RelativePtEC2_jUp","_CMS_scale_RelativePtEC2_jDown",
    #"_CMS_scale_RelativePtHF_jUp","_CMS_scale_RelativePtHF_jDown",
    #"_CMS_scale_RelativeBal_jUp","_CMS_scale_RelativeBal_jDown",
    #"_CMS_scale_RelativeFSR_jUp","_CMS_scale_RelativeFSR_jDown",
    #"_CMS_scale_RelativeStatFSR_jUp","_CMS_scale_RelativeStatFSR_jDown",
    #"_CMS_scale_RelativeStatEC_jUp","_CMS_scale_RelativeStatEC_jDown",
    #"_CMS_scale_RelativeStatHF_jUp","_CMS_scale_RelativeStatHF_jDown",
    #"_CMS_scale_PileUpDataMC_jUp","_CMS_scale_PileUpDataMC_jDown",
    #"_CMS_scale_PileUpPtRef_jUp","_CMS_scale_PileUpPtRef_jDown",
    #"_CMS_scale_PileUpPtBB_jUp","_CMS_scale_PileUpPtBB_jDown",
    #"_CMS_scale_PileUpPtEC1_jUp","_CMS_scale_PileUpPtEC1_jDown",
    #"_CMS_scale_PileUpPtEC2_jUp","_CMS_scale_PileUpPtEC2_jDown",
    #"_CMS_scale_PileUpPtHF_jUp","_CMS_scale_PileUpPtHF_jDown",
    #"_CMS_scale_PileUpMuZero_jUp","_CMS_scale_PileUpMuZero_jDown",
    #"_CMS_scale_PileUpEnvelope_jUp","_CMS_scale_PileUpEnvelope_jDown",
    #"_CMS_scale_SubTotalPileUp_jUp","_CMS_scale_SubTotalPileUp_jDown",
    #"_CMS_scale_SubTotalRelative_jUp","_CMS_scale_SubTotalRelative_jDown",
    #"_CMS_scale_SubTotalPt_jUp","_CMS_scale_SubTotalPt_jDown",
    #"_CMS_scale_SubTotalScale_jUp","_CMS_scale_SubTotalScale_jDown",
    #"_CMS_scale_SubTotalAbsolute_jUp","_CMS_scale_SubTotalAbsolute_jDown",
    #"_CMS_scale_SubTotalMC_jUp","_CMS_scale_SubTotalMC_jDown",
    #"_CMS_scale_Total_jUp","_CMS_scale_Total_jDown",
    #"_CMS_scale_TotalNoFlavor_jUp","_CMS_scale_TotalNoFlavor_jDown",
    #"_CMS_scale_TotalNoTime_jUp","_CMS_scale_TotalNoTime_jDown",
    #"_CMS_scale_TotalNoFlavorNoTime_jUp","_CMS_scale_TotalNoFlavorNoTime_jDown",
    #"_CMS_scale_FlavorZJet_jUp","_CMS_scale_FlavorZJet_jDown",
    #"_CMS_scale_FlavorPhotonJet_jUp","_CMS_scale_FlavorPhotonJet_jDown",
    #"_CMS_scale_FlavorPureGluon_jUp","_CMS_scale_FlavorPureGluon_jDown",
    #"_CMS_scale_FlavorPureQuark_jUp","_CMS_scale_FlavorPureQuark_jDown",
    #"_CMS_scale_FlavorPureCharm_jUp","_CMS_scale_FlavorPureCharm_jDown",
    #"_CMS_scale_FlavorPureBottom_jUp","_CMS_scale_FlavorPureBottom_jDown",
    #"_CMS_scale_TimeRunBCD_jUp","_CMS_scale_TimeRunBCD_jDown",
    #"_CMS_scale_TimeRunEF_jUp","_CMS_scale_TimeRunEF_jDown",
    #"_CMS_scale_TimeRunG_jUp","_CMS_scale_TimeRunG_jDown",
    #"_CMS_scale_TimeRunH_jUp","_CMS_scale_TimeRunH_jDown",

]

systsTtbar= [
  #"_CMS_ttH_FSRUp","_CMS_ttH_FSRDown",
  #"_CMS_ttH_ISRUp","_CMS_ttH_ISRDown",
  #"_CMS_ttH_hdampUp","_CMS_ttH_hdampDown",
  #"_CMS_ttH_ueUp","_CMS_ttH_ueDown",
]

#systs_tt_lf=["_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown"]
#systs_tt_b=["_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown"]
#systs_tt_2b=[ "_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown"]
#systs_tt_bb=[ "_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown"]
#systs_tt_cc=[ "_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown"]

systs_tt_lf=[]
systs_tt_b=[]
systs_tt_2b=[]
systs_tt_bb=[]
systs_tt_cc=[]


errorSystNames=[
                    "",
                   "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                   "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                   "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                   "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
##                    "_CMS_ttH_TopPtUp","_CMS_ttH_TopPtDown",
                    ##"_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
##                    "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown",
                   "_CMS_ttH_ljets_Trig_elUp","_CMS_ttH_ljets_Trig_elDown",  
                   "_CMS_ttH_ljets_Trig_muUp","_CMS_ttH_ljets_Trig_muDown",  
###                     "_CMS_ttH_ljets_TrigUp","_CMS_ttH_ljets_TrigDown",
                    "_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown", 
                   "_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",  
                    "_CMS_ttH_PUUp","_CMS_ttH_PUDown",

                   ##"_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",
                   ##"_CMS_res_jUp","_CMS_res_jDown",
                    ##"_CMS_scale_jUp","_CMS_scale_jDown",
                    ##"_CMS_ttH_PSscaleUp","_CMS_ttH_PSscaleDown",
  "_CMS_scale_jUp","_CMS_scale_jDown",
    "_CMS_res_jUp","_CMS_res_jDown",
    #"_CMS_scale_AbsoluteStat_jUp","_CMS_scale_AbsoluteStat_jDown",
    #"_CMS_scale_AbsoluteScale_jUp","_CMS_scale_AbsoluteScale_jDown",
    ##"_CMS_scale_AbsoluteFlavMap_jUp","_CMS_scale_AbsoluteFlavMap_jDown",
    #"_CMS_scale_AbsoluteMPFBias_jUp","_CMS_scale_AbsoluteMPFBias_jDown",
    #"_CMS_scale_Fragmentation_jUp","_CMS_scale_Fragmentation_jDown",
    #"_CMS_scale_SinglePionECAL_jUp","_CMS_scale_SinglePionECAL_jDown",
    #"_CMS_scale_SinglePionHCAL_jUp","_CMS_scale_SinglePionHCAL_jDown",
    #"_CMS_scale_FlavorQCD_jUp","_CMS_scale_FlavorQCD_jDown",
    #"_CMS_scale_TimePtEta_jUp","_CMS_scale_TimePtEta_jDown",
    #"_CMS_scale_RelativeJEREC1_jUp","_CMS_scale_RelativeJEREC1_jDown",
    #"_CMS_scale_RelativeJEREC2_jUp","_CMS_scale_RelativeJEREC2_jDown",
    #"_CMS_scale_RelativeJERHF_jUp","_CMS_scale_RelativeJERHF_jDown",
    #"_CMS_scale_RelativePtBB_jUp","_CMS_scale_RelativePtBB_jDown",
    #"_CMS_scale_RelativePtEC1_jUp","_CMS_scale_RelativePtEC1_jDown",
    #"_CMS_scale_RelativePtEC2_jUp","_CMS_scale_RelativePtEC2_jDown",
    #"_CMS_scale_RelativePtHF_jUp","_CMS_scale_RelativePtHF_jDown",
    #"_CMS_scale_RelativeBal_jUp","_CMS_scale_RelativeBal_jDown",
    #"_CMS_scale_RelativeFSR_jUp","_CMS_scale_RelativeFSR_jDown",
    #"_CMS_scale_RelativeStatFSR_jUp","_CMS_scale_RelativeStatFSR_jDown",
    #"_CMS_scale_RelativeStatEC_jUp","_CMS_scale_RelativeStatEC_jDown",
    #"_CMS_scale_RelativeStatHF_jUp","_CMS_scale_RelativeStatHF_jDown",
    #"_CMS_scale_PileUpDataMC_jUp","_CMS_scale_PileUpDataMC_jDown",
    #"_CMS_scale_PileUpPtRef_jUp","_CMS_scale_PileUpPtRef_jDown",
    #"_CMS_scale_PileUpPtBB_jUp","_CMS_scale_PileUpPtBB_jDown",
    #"_CMS_scale_PileUpPtEC1_jUp","_CMS_scale_PileUpPtEC1_jDown",
    #"_CMS_scale_PileUpPtEC2_jUp","_CMS_scale_PileUpPtEC2_jDown",
    #"_CMS_scale_PileUpPtHF_jUp","_CMS_scale_PileUpPtHF_jDown",
    #"_CMS_scale_PileUpMuZero_jUp","_CMS_scale_PileUpMuZero_jDown",
    #"_CMS_scale_PileUpEnvelope_jUp","_CMS_scale_PileUpEnvelope_jDown",
    #"_CMS_scale_SubTotalPileUp_jUp","_CMS_scale_SubTotalPileUp_jDown",
    #"_CMS_scale_SubTotalRelative_jUp","_CMS_scale_SubTotalRelative_jDown",
    #"_CMS_scale_SubTotalPt_jUp","_CMS_scale_SubTotalPt_jDown",
    #"_CMS_scale_SubTotalScale_jUp","_CMS_scale_SubTotalScale_jDown",
    #"_CMS_scale_SubTotalAbsolute_jUp","_CMS_scale_SubTotalAbsolute_jDown",
    #"_CMS_scale_SubTotalMC_jUp","_CMS_scale_SubTotalMC_jDown",
    #"_CMS_scale_Total_jUp","_CMS_scale_Total_jDown",
    #"_CMS_scale_TotalNoFlavor_jUp","_CMS_scale_TotalNoFlavor_jDown",
    #"_CMS_scale_TotalNoTime_jUp","_CMS_scale_TotalNoTime_jDown",
    #"_CMS_scale_TotalNoFlavorNoTime_jUp","_CMS_scale_TotalNoFlavorNoTime_jDown",
    #"_CMS_scale_FlavorZJet_jUp","_CMS_scale_FlavorZJet_jDown",
    #"_CMS_scale_FlavorPhotonJet_jUp","_CMS_scale_FlavorPhotonJet_jDown",
    #"_CMS_scale_FlavorPureGluon_jUp","_CMS_scale_FlavorPureGluon_jDown",
    #"_CMS_scale_FlavorPureQuark_jUp","_CMS_scale_FlavorPureQuark_jDown",
    #"_CMS_scale_FlavorPureCharm_jUp","_CMS_scale_FlavorPureCharm_jDown",
    #"_CMS_scale_FlavorPureBottom_jUp","_CMS_scale_FlavorPureBottom_jDown",
    #"_CMS_scale_TimeRunBCD_jUp","_CMS_scale_TimeRunBCD_jDown",
    #"_CMS_scale_TimeRunEF_jUp","_CMS_scale_TimeRunEF_jDown",
    #"_CMS_scale_TimeRunG_jUp","_CMS_scale_TimeRunG_jDown",
    #"_CMS_scale_TimeRunH_jUp","_CMS_scale_TimeRunH_jDown",
      #"_CMS_ttH_FSRUp","_CMS_ttH_FSRDown",
  #"_CMS_ttH_ISRUp","_CMS_ttH_ISRDown",
  #"_CMS_ttH_hdampUp","_CMS_ttH_hdampDown",
  #"_CMS_ttH_ueUp","_CMS_ttH_ueDown",
]

errorSystNamesNoPS=[
                    "",
                   "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
                   "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
                   "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
                   "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
##                    "_CMS_ttH_TopPtUp","_CMS_ttH_TopPtDown",
                    ##"_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarOtherDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlusBDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlus2BDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusBBbarDown",
                    ##"_CMS_ttH_Q2scale_ttbarPlusCCbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
##                    "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown",
                   "_CMS_ttH_ljets_Trig_elUp","_CMS_ttH_ljets_Trig_elDown",  
                   "_CMS_ttH_ljets_Trig_muUp","_CMS_ttH_ljets_Trig_muDown",  
###                     "_CMS_ttH_ljets_TrigUp","_CMS_ttH_ljets_TrigDown",
                    "_CMS_ttH_eff_elUp","_CMS_ttH_eff_elDown", 
                   "_CMS_ttH_eff_muUp","_CMS_ttH_eff_muDown",  
                    "_CMS_ttH_PUUp","_CMS_ttH_PUDown",

                   ##"_CMS_ttH_eff_leptonUp","_CMS_ttH_eff_leptonDown",
                   ##"_CMS_res_jUp","_CMS_res_jDown",
                    ##"_CMS_scale_jUp","_CMS_scale_jDown",
                    ##"_CMS_ttH_PSscaleUp","_CMS_ttH_PSscaleDown",

    "_CMS_scale_jUp","_CMS_scale_jDown",
    "_CMS_res_jUp","_CMS_res_jDown",
    #"_CMS_scale_AbsoluteStat_jUp","_CMS_scale_AbsoluteStat_jDown",
    #"_CMS_scale_AbsoluteScale_jUp","_CMS_scale_AbsoluteScale_jDown",
    ##"_CMS_scale_AbsoluteFlavMap_jUp","_CMS_scale_AbsoluteFlavMap_jDown",
    #"_CMS_scale_AbsoluteMPFBias_jUp","_CMS_scale_AbsoluteMPFBias_jDown",
    #"_CMS_scale_Fragmentation_jUp","_CMS_scale_Fragmentation_jDown",
    #"_CMS_scale_SinglePionECAL_jUp","_CMS_scale_SinglePionECAL_jDown",
    #"_CMS_scale_SinglePionHCAL_jUp","_CMS_scale_SinglePionHCAL_jDown",
    #"_CMS_scale_FlavorQCD_jUp","_CMS_scale_FlavorQCD_jDown",
    #"_CMS_scale_TimePtEta_jUp","_CMS_scale_TimePtEta_jDown",
    #"_CMS_scale_RelativeJEREC1_jUp","_CMS_scale_RelativeJEREC1_jDown",
    #"_CMS_scale_RelativeJEREC2_jUp","_CMS_scale_RelativeJEREC2_jDown",
    #"_CMS_scale_RelativeJERHF_jUp","_CMS_scale_RelativeJERHF_jDown",
    #"_CMS_scale_RelativePtBB_jUp","_CMS_scale_RelativePtBB_jDown",
    #"_CMS_scale_RelativePtEC1_jUp","_CMS_scale_RelativePtEC1_jDown",
    #"_CMS_scale_RelativePtEC2_jUp","_CMS_scale_RelativePtEC2_jDown",
    #"_CMS_scale_RelativePtHF_jUp","_CMS_scale_RelativePtHF_jDown",
    #"_CMS_scale_RelativeBal_jUp","_CMS_scale_RelativeBal_jDown",
    #"_CMS_scale_RelativeFSR_jUp","_CMS_scale_RelativeFSR_jDown",
    #"_CMS_scale_RelativeStatFSR_jUp","_CMS_scale_RelativeStatFSR_jDown",
    #"_CMS_scale_RelativeStatEC_jUp","_CMS_scale_RelativeStatEC_jDown",
    #"_CMS_scale_RelativeStatHF_jUp","_CMS_scale_RelativeStatHF_jDown",
    #"_CMS_scale_PileUpDataMC_jUp","_CMS_scale_PileUpDataMC_jDown",
    #"_CMS_scale_PileUpPtRef_jUp","_CMS_scale_PileUpPtRef_jDown",
    #"_CMS_scale_PileUpPtBB_jUp","_CMS_scale_PileUpPtBB_jDown",
    #"_CMS_scale_PileUpPtEC1_jUp","_CMS_scale_PileUpPtEC1_jDown",
    #"_CMS_scale_PileUpPtEC2_jUp","_CMS_scale_PileUpPtEC2_jDown",
    #"_CMS_scale_PileUpPtHF_jUp","_CMS_scale_PileUpPtHF_jDown",
    ##"_CMS_scale_PileUpMuZero_jUp","_CMS_scale_PileUpMuZero_jDown",
    ##"_CMS_scale_PileUpEnvelope_jUp","_CMS_scale_PileUpEnvelope_jDown",
    ##"_CMS_scale_SubTotalPileUp_jUp","_CMS_scale_SubTotalPileUp_jDown",
    ##"_CMS_scale_SubTotalRelative_jUp","_CMS_scale_SubTotalRelative_jDown",
    ##"_CMS_scale_SubTotalPt_jUp","_CMS_scale_SubTotalPt_jDown",
    ##"_CMS_scale_SubTotalScale_jUp","_CMS_scale_SubTotalScale_jDown",
    ##"_CMS_scale_SubTotalAbsolute_jUp","_CMS_scale_SubTotalAbsolute_jDown",
    ##"_CMS_scale_SubTotalMC_jUp","_CMS_scale_SubTotalMC_jDown",
    ##"_CMS_scale_Total_jUp","_CMS_scale_Total_jDown",
    ##"_CMS_scale_TotalNoFlavor_jUp","_CMS_scale_TotalNoFlavor_jDown",
    ##"_CMS_scale_TotalNoTime_jUp","_CMS_scale_TotalNoTime_jDown",
    ##"_CMS_scale_TotalNoFlavorNoTime_jUp","_CMS_scale_TotalNoFlavorNoTime_jDown",
    ##"_CMS_scale_FlavorZJet_jUp","_CMS_scale_FlavorZJet_jDown",
    ##"_CMS_scale_FlavorPhotonJet_jUp","_CMS_scale_FlavorPhotonJet_jDown",
    ##"_CMS_scale_FlavorPureGluon_jUp","_CMS_scale_FlavorPureGluon_jDown",
    ##"_CMS_scale_FlavorPureQuark_jUp","_CMS_scale_FlavorPureQuark_jDown",
    ##"_CMS_scale_FlavorPureCharm_jUp","_CMS_scale_FlavorPureCharm_jDown",
    ##"_CMS_scale_FlavorPureBottom_jUp","_CMS_scale_FlavorPureBottom_jDown",
    ##"_CMS_scale_TimeRunBCD_jUp","_CMS_scale_TimeRunBCD_jDown",
    ##"_CMS_scale_TimeRunEF_jUp","_CMS_scale_TimeRunEF_jDown",
    ##"_CMS_scale_TimeRunG_jUp","_CMS_scale_TimeRunG_jDown",
    ##"_CMS_scale_TimeRunH_jUp","_CMS_scale_TimeRunH_jDown",
      #"","",
  #"","",
  #"","",
  #"","",
]

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
]

assert len(systWeights)==len(weightSystNames)

otherSystNames=[
                    #"_CMS_scale_jUp",
                    #"_CMS_scale_jDown",
                   #"_CMS_res_jUp",
                   #"_CMS_res_jDown"
                    ##"_CMS_ttH_PSscaleUp",
                    ##"_CMS_ttH_PSscaleDown"
    "_CMS_scale_jUp","_CMS_scale_jDown",
    "_CMS_res_jUp","_CMS_res_jDown",
    #"_CMS_scale_AbsoluteStat_jUp","_CMS_scale_AbsoluteStat_jDown",
    #"_CMS_scale_AbsoluteScale_jUp","_CMS_scale_AbsoluteScale_jDown",
    ##"_CMS_scale_AbsoluteFlavMap_jUp","_CMS_scale_AbsoluteFlavMap_jDown",
    #"_CMS_scale_AbsoluteMPFBias_jUp","_CMS_scale_AbsoluteMPFBias_jDown",
    #"_CMS_scale_Fragmentation_jUp","_CMS_scale_Fragmentation_jDown",
    #"_CMS_scale_SinglePionECAL_jUp","_CMS_scale_SinglePionECAL_jDown",
    #"_CMS_scale_SinglePionHCAL_jUp","_CMS_scale_SinglePionHCAL_jDown",
    #"_CMS_scale_FlavorQCD_jUp","_CMS_scale_FlavorQCD_jDown",
    #"_CMS_scale_TimePtEta_jUp","_CMS_scale_TimePtEta_jDown",
    #"_CMS_scale_RelativeJEREC1_jUp","_CMS_scale_RelativeJEREC1_jDown",
    #"_CMS_scale_RelativeJEREC2_jUp","_CMS_scale_RelativeJEREC2_jDown",
    #"_CMS_scale_RelativeJERHF_jUp","_CMS_scale_RelativeJERHF_jDown",
    #"_CMS_scale_RelativePtBB_jUp","_CMS_scale_RelativePtBB_jDown",
    #"_CMS_scale_RelativePtEC1_jUp","_CMS_scale_RelativePtEC1_jDown",
    #"_CMS_scale_RelativePtEC2_jUp","_CMS_scale_RelativePtEC2_jDown",
    #"_CMS_scale_RelativePtHF_jUp","_CMS_scale_RelativePtHF_jDown",
    #"_CMS_scale_RelativeBal_jUp","_CMS_scale_RelativeBal_jDown",
    #"_CMS_scale_RelativeFSR_jUp","_CMS_scale_RelativeFSR_jDown",
    #"_CMS_scale_RelativeStatFSR_jUp","_CMS_scale_RelativeStatFSR_jDown",
    #"_CMS_scale_RelativeStatEC_jUp","_CMS_scale_RelativeStatEC_jDown",
    #"_CMS_scale_RelativeStatHF_jUp","_CMS_scale_RelativeStatHF_jDown",
    #"_CMS_scale_PileUpDataMC_jUp","_CMS_scale_PileUpDataMC_jDown",
    #"_CMS_scale_PileUpPtRef_jUp","_CMS_scale_PileUpPtRef_jDown",
    #"_CMS_scale_PileUpPtBB_jUp","_CMS_scale_PileUpPtBB_jDown",
    #"_CMS_scale_PileUpPtEC1_jUp","_CMS_scale_PileUpPtEC1_jDown",
    #"_CMS_scale_PileUpPtEC2_jUp","_CMS_scale_PileUpPtEC2_jDown",
    #"_CMS_scale_PileUpPtHF_jUp","_CMS_scale_PileUpPtHF_jDown",
    ##"_CMS_scale_PileUpMuZero_jUp","_CMS_scale_PileUpMuZero_jDown",
    ##"_CMS_scale_PileUpEnvelope_jUp","_CMS_scale_PileUpEnvelope_jDown",
    ##"_CMS_scale_SubTotalPileUp_jUp","_CMS_scale_SubTotalPileUp_jDown",
    ##"_CMS_scale_SubTotalRelative_jUp","_CMS_scale_SubTotalRelative_jDown",
    ##"_CMS_scale_SubTotalPt_jUp","_CMS_scale_SubTotalPt_jDown",
    ##"_CMS_scale_SubTotalScale_jUp","_CMS_scale_SubTotalScale_jDown",
    ##"_CMS_scale_SubTotalAbsolute_jUp","_CMS_scale_SubTotalAbsolute_jDown",
    ##"_CMS_scale_SubTotalMC_jUp","_CMS_scale_SubTotalMC_jDown",
    ##"_CMS_scale_Total_jUp","_CMS_scale_Total_jDown",
    ##"_CMS_scale_TotalNoFlavor_jUp","_CMS_scale_TotalNoFlavor_jDown",
    ##"_CMS_scale_TotalNoTime_jUp","_CMS_scale_TotalNoTime_jDown",
    ##"_CMS_scale_TotalNoFlavorNoTime_jUp","_CMS_scale_TotalNoFlavorNoTime_jDown",
    ##"_CMS_scale_FlavorZJet_jUp","_CMS_scale_FlavorZJet_jDown",
    ##"_CMS_scale_FlavorPhotonJet_jUp","_CMS_scale_FlavorPhotonJet_jDown",
    ##"_CMS_scale_FlavorPureGluon_jUp","_CMS_scale_FlavorPureGluon_jDown",
    ##"_CMS_scale_FlavorPureQuark_jUp","_CMS_scale_FlavorPureQuark_jDown",
    ##"_CMS_scale_FlavorPureCharm_jUp","_CMS_scale_FlavorPureCharm_jDown",
    ##"_CMS_scale_FlavorPureBottom_jUp","_CMS_scale_FlavorPureBottom_jDown",
    ##"_CMS_scale_TimeRunBCD_jUp","_CMS_scale_TimeRunBCD_jDown",
    ##"_CMS_scale_TimeRunEF_jUp","_CMS_scale_TimeRunEF_jDown",
    ##"_CMS_scale_TimeRunG_jUp","_CMS_scale_TimeRunG_jDown",
    ##"_CMS_scale_TimeRunH_jUp","_CMS_scale_TimeRunH_jDown",
]

otherSystFileNames=[
      "JESup","JESdown",
      "JERup","JERdown",
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
    ##"JESPileUpMuZeroUp","JESPileUpMuZeroDown",
    ##"JESPileUpEnvelopeUp","JESPileUpEnvelopeDown",
    ##"JESSubTotalPileUpUp","JESSubTotalPileUpDown",
    ##"JESSubTotalRelativeUp","JESSubTotalRelativeDown",
    ##"JESSubTotalPtUp","JESSubTotalPtDown",
    ##"JESSubTotalScaleUp","JESSubTotalScaleDown",
    ##"JESSubTotalAbsoluteUp","JESSubTotalAbsoluteDown",
    ##"JESSubTotalMCUp","JESSubTotalMCDown",
    ##"JESTotalUp","JESTotalDown",
    ##"JESTotalNoFlavorUp","JESTotalNoFlavorDown",
    ##"JESTotalNoTimeUp","JESTotalNoTimeDown",
    ##"JESTotalNoFlavorNoTimeUp","JESTotalNoFlavorNoTimeDown",
    ##"JESFlavorZJetUp","JESFlavorZJetDown",
    ##"JESFlavorPhotonJetUp","JESFlavorPhotonJetDown",
    ##"JESFlavorPureGluonUp","JESFlavorPureGluonDown",
    ##"JESFlavorPureQuarkUp","JESFlavorPureQuarkDown",
    ##"JESFlavorPureCharmUp","JESFlavorPureCharmDown",
    ##"JESFlavorPureBottomUp","JESFlavorPureBottomDown",
    ##"JESTimeRunBCDUp","JESTimeRunBCDDown",
    ##"JESTimeRunEFUp","JESTimeRunEFDown",
    ##"JESTimeRunGUp","JESTimeRunGDown",
    ##"JESTimeRunHUp","JESTimeRunHDown",

]

PSSystNames=[
  #"_CMS_ttH_FSRUp","_CMS_ttH_FSRDown",
  #"_CMS_ttH_ISRUp","_CMS_ttH_ISRDown",
  #"_CMS_ttH_hdampUp","_CMS_ttH_hdampDown",
  #"_CMS_ttH_ueUp","_CMS_ttH_ueDown",
]
PSSystFileNames=[
  #"fsr_up","fsr_down",
  #"isr_up","isr_down",
  #"hdamp_up","hdamp_down",
  #"ue_up","ue_down",
]
  

assert len(errorSystNames)==len(weightSystNames+otherSystNames+PSSystNames)

# samples
# input path 
#path_Matthias="/nfs/dust/cms/user/matsch/ntuples/Spring17/v3"
path_additionalSamples="/nfs/dust/cms/user/kelmorab/trees_Spring17_v5_additional"
#path_data="/nfs/dust/cms/user/mwassmer/ntuples/data_json"
path_michael="/nfs/dust/cms/user/mwassmer/ntuples/august17"
path_qcd_samples = "/nfs/dust/cms/user/mwassmer/ntuples/QCD_Estimation_alternative"
#path_karim="/nfs/dust/cms/user/kelmorab/trees_Spring17_v5"
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


print "controlsamples"
samplesControlPlots=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_karim+'/ttH*/*nominal*.root',mcWeightAll+sel_MET,'ttH',systsAllSamples,samDict=sampleDict) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight,'ttbar',systsAllSamples) ,     
                    Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict),
                    Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict),  
                    Sample('Single Top',ROOT.kMagenta,path_karim+'/st*/*nominal*.root',mcWeightAll+sel_MET,'SingleTop',systsAllSamples,samDict=sampleDict) , 
                    Sample('V+jets',ROOT.kGreen-3,path_karim+'/*ets*/*nominal*.root',mcWeightAll+sel_MET,'Vjets',systsAllSamples,samDict=sampleDict) , 
                    Sample('t#bar{t}+V',ROOT.kBlue-10,path_karim+'/tt?_*/*nominal*.root',mcWeightAll+sel_MET,'ttV',systsAllSamples,samDict=sampleDict),         
                    Sample('Diboson',ROOT.kAzure+2,path_karim+'/??_pythia_*/*nominal*.root',mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict) , 
#Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',weightSystNames)  
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
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==1)'+sel_MET,'ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict),
                    Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==1)'+sel_MET,'ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==2)'+sel_MET,'ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==3)'+sel_MET,'ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict), 
                    Sample('Single Top',ROOT.kMagenta,path_karim+'/st*/*nominal*.root',mcWeightAll+sel_MET,'singlet',systsAllSamples,samDict=sampleDict) , 
                    Sample('Z+jets',ROOT.kGreen-3,path_karim+'/Zjets*/*nominal*.root',mcWeightAll+sel_MET,'zjets',systsAllSamples,samDict=sampleDict) , 
                    Sample('W+jets',ROOT.kGreen-7,path_karim+'/Wjets*/*nominal*.root',mcWeightAll+sel_MET,'wjets',systsAllSamples,samDict=sampleDict) , 
                    Sample('t#bar{t}+W',ROOT.kBlue-10,path_karim+'/ttW_*/*nominal*.root',mcWeightAll+sel_MET,'ttbarW',systsAllSamples,samDict=sampleDict),
                    Sample('t#bar{t}+Z',ROOT.kBlue-6,path_karim+'/ttZ_*/*nominal*.root',mcWeightAll+sel_MET,'ttbarZ',systsAllSamples,samDict=sampleDict),
                    Sample('Diboson',ROOT.kAzure+2,path_karim+'/??_pythia_*/*nominal*.root',mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict) , 
#Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',weightSystNames)  
]

#print "shape samples"
#samplesShapes=[
                    #Sample('t#bar{t}H',ROOT.kBlue+1,path_Matthias+'/ttH*/*nominal*.root',mcWeight+evenSel,'ttH',systsAllSamples,samDict=sampleDict) ,     
##                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight+evenSel,'ttbar',samDict=sampleDict) ,     
                    #Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_Matthias+'/ttHbb/*nominal*.root','1.0*'+mcWeight+evenSel,'ttH_hbb',systsAllSamples,samDict=sampleDict) ,  
                    #Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_Matthias+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hccSel,'ttH_hcc',systsAllSamples,samDict=sampleDict) ,  
                    #Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_Matthias+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+httSel,'ttH_htt',systsAllSamples,samDict=sampleDict) ,  
                    #Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_Matthias+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hggSel,'ttH_hgg',systsAllSamples,samDict=sampleDict) ,  
                    #Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_Matthias+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hglugluSel,'ttH_hgluglu',systsAllSamples,samDict=sampleDict) ,  
                    #Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_Matthias+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hwwSel,'ttH_hww',systsAllSamples,samDict=sampleDict) ,  
                    #Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_Matthias+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hzzSel,'ttH_hzz',systsAllSamples,samDict=sampleDict) ,  
                    #Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_Matthias+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hzgSel,'ttH_hzg',systsAllSamples,samDict=sampleDict) ,
                    
                    #Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict),
                    #Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict),
                    #Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict),
                    #Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict),
                    #Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict), 
                    ##Sample('Single Top',ROOT.kMagenta,path_karim+'/st*/*nominal*.root',mcWeightAll,'singlet',systsAllSamples,samDict=sampleDict) , 
                    ##Sample('Z+jets',ROOT.kGreen-3,path_80x+'/withTrigger_Zjets*/*nominal*.root',mcWeightAll,'zjets',systsAllSamples,samDict=sampleDict) , 
                    ##Sample('W+jets',ROOT.kGreen-7,path_80x+'/WJets*/*nominal*.root',mcWeightAll,'wjets',systsAllSamples,samDict=sampleDict) , 
                    ##Sample('t#bar{t}+W',ROOT.kBlue-10,path_80x+'/ttW_*/*nominal*.root',mcWeightAll,'ttbarW',systsAllSamples),
                    ##Sample('t#bar{t}+Z',ROOT.kBlue-6,path_80x+'/ttZ_*/*nominal*.root',mcWeightAll,'ttbarZ',systsAllSamples),
                    ##Sample('Diboson',ROOT.kAzure+2,path_80x+'/??/*nominal*.root',mcWeightAll,'diboson',systsAllSamples,samDict=sampleDict) , 
###                    Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcWeightAll,'QCD',samDict=sampleDict) , 
#]

#~ mc_samples_iso_inverted=[
                    #~ Sample('t#bar{t}H_iso_inv',ROOT.kBlue+1,path_qcd_samples+'/ttH*/*nominal*.root',mcWeightAll+sel_MET+'*internalQCDweight','ttH_iso_inv',systsAllSamples,samDict=sampleDict) ,     
                    #~ Sample('t#bar{t}+lf_iso_inv',ROOT.kRed-7,path_qcd_samples+'/ttbar_excl_*_0/*nominal*.root',mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)*internalQCDweight','ttbarOther_iso_inv',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict),
                    #~ Sample('t#bar{t}+c#bar{c}_iso_inv',ROOT.kRed+1,path_qcd_samples+'/ttbar_excl_*_0/*nominal*.root',mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==1)*internalQCDweight','ttbarPlusCCbar_iso_inv',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict),
                    #~ Sample('t#bar{t}+b_iso_inv',ROOT.kRed-2,path_qcd_samples+'/ttbar_excl_*_0/*nominal*.root',mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==1)*internalQCDweight','ttbarPlusB_iso_inv',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict),
                    #~ Sample('t#bar{t}+2b_iso_inv',ROOT.kRed+2,path_qcd_samples+'/ttbar_excl_*_0/*nominal*.root',mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==2)*internalQCDweight','ttbarPlus2B_iso_inv',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict),
                    #~ Sample('t#bar{t}+b#bar{b}_iso_inv',ROOT.kRed+3,path_qcd_samples+'/ttbar_excl_*_0/*nominal*.root',mcWeightAll+sel_MET+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==3)*internalQCDweight','ttbarPlusBBbar_iso_inv',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict),  
                    #~ Sample('Single Top_iso_inv',ROOT.kMagenta,path_qcd_samples+'/st*/*nominal*.root',mcWeightAll+sel_MET+'*internalQCDweight','SingleTop_iso_inv',systsAllSamples,samDict=sampleDict) , 
                    #~ Sample('V+jets_iso_inv',ROOT.kGreen-3,path_qcd_samples+'/*ets*/*nominal*.root',mcWeightAll+sel_MET+'*internalQCDweight','Vjets_iso_inv',systsAllSamples,samDict=sampleDict) , 
                    #~ Sample('t#bar{t}+V_iso_inv',ROOT.kBlue-10,path_qcd_samples+'/tt?_*/*nominal*.root',mcWeightAll+sel_MET+'*internalQCDweight','ttV_iso_inv',systsAllSamples,samDict=sampleDict),         
                    #~ Sample('Diboson_iso_inv',ROOT.kAzure+2,path_qcd_samples+'/??_0/*nominal*.root',mcWeightAll+sel_MET+'*internalQCDweight','diboson_iso_inv',systsAllSamples,samDict=sampleDict)                                          
#~ ]

#~ data_samples_iso_inverted=[
					#~ Sample('SingleMu_iso_inv',ROOT.kBlack,path_qcd_samples+'/SingleMuon*/*nominal*.root',sel_singlemu+sel_MET+'*internalQCDweight','SingleMu_iso_inv',samDict=sampleDict),
					#~ Sample('SingleEl_iso_inv',ROOT.kBlack,path_qcd_samples+'/SingleElectron*/*nominal*.root',sel_singleel+sel_MET+'*internalQCDweight','SingleEl_iso_inv',samDict=sampleDict)
#~ ]
