import sys
import os
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *

sel_singleel="(N_LooseMuons==0 && N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)*(N_Jets>=4 && N_BTagsM>=2)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0 && (N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1)))*(N_Jets>=4 && N_BTagsM>=2)" # and vice versa...

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
 #"_CMS_scale_JESUp","_CMS_scale_JESDown",
    "_CMS_res_JERUp","_CMS_res_JERDown",
    "_CMS_scale_JESAbsoluteStatUp","_CMS_scale_JESAbsoluteStatDown",
    "_CMS_scale_JESAbsoluteScaleUp","_CMS_scale_JESAbsoluteScaleDown",
    #"_CMS_scale_JESAbsoluteFlavMapUp","_CMS_scale_JESAbsoluteFlavMapDown",
    "_CMS_scale_JESAbsoluteMPFBiasUp","_CMS_scale_JESAbsoluteMPFBiasDown",
    "_CMS_scale_JESFragmentationUp","_CMS_scale_JESFragmentationDown",
    "_CMS_scale_JESSinglePionECALUp","_CMS_scale_JESSinglePionECALDown",
    "_CMS_scale_JESSinglePionHCALUp","_CMS_scale_JESSinglePionHCALDown",
    "_CMS_scale_JESFlavorQCDUp","_CMS_scale_JESFlavorQCDDown",
    "_CMS_scale_JESTimePtEtaUp","_CMS_scale_JESTimePtEtaDown",
    "_CMS_scale_JESRelativeJEREC1Up","_CMS_scale_JESRelativeJEREC1Down",
    "_CMS_scale_JESRelativeJEREC2Up","_CMS_scale_JESRelativeJEREC2Down",
    "_CMS_scale_JESRelativeJERHFUp","_CMS_scale_JESRelativeJERHFDown",
    "_CMS_scale_JESRelativePtBBUp","_CMS_scale_JESRelativePtBBDown",
    "_CMS_scale_JESRelativePtEC1Up","_CMS_scale_JESRelativePtEC1Down",
    "_CMS_scale_JESRelativePtEC2Up","_CMS_scale_JESRelativePtEC2Down",
    "_CMS_scale_JESRelativePtHFUp","_CMS_scale_JESRelativePtHFDown",
    "_CMS_scale_JESRelativeBalUp","_CMS_scale_JESRelativeBalDown",
    "_CMS_scale_JESRelativeFSRUp","_CMS_scale_JESRelativeFSRDown",
    "_CMS_scale_JESRelativeStatFSRUp","_CMS_scale_JESRelativeStatFSRDown",
    "_CMS_scale_JESRelativeStatECUp","_CMS_scale_JESRelativeStatECDown",
    "_CMS_scale_JESRelativeStatHFUp","_CMS_scale_JESRelativeStatHFDown",
    "_CMS_scale_JESPileUpDataMCUp","_CMS_scale_JESPileUpDataMCDown",
    "_CMS_scale_JESPileUpPtRefUp","_CMS_scale_JESPileUpPtRefDown",
    "_CMS_scale_JESPileUpPtBBUp","_CMS_scale_JESPileUpPtBBDown",
    "_CMS_scale_JESPileUpPtEC1Up","_CMS_scale_JESPileUpPtEC1Down",
    "_CMS_scale_JESPileUpPtEC2Up","_CMS_scale_JESPileUpPtEC2Down",
    "_CMS_scale_JESPileUpPtHFUp","_CMS_scale_JESPileUpPtHFDown",
    #"_CMS_scale_JESPileUpMuZeroUp","_CMS_scale_JESPileUpMuZeroDown",
    #"_CMS_scale_JESPileUpEnvelopeUp","_CMS_scale_JESPileUpEnvelopeDown",
    #"_CMS_scale_JESSubTotalPileUpUp","_CMS_scale_JESSubTotalPileUpDown",
    #"_CMS_scale_JESSubTotalRelativeUp","_CMS_scale_JESSubTotalRelativeDown",
    #"_CMS_scale_JESSubTotalPtUp","_CMS_scale_JESSubTotalPtDown",
    #"_CMS_scale_JESSubTotalScaleUp","_CMS_scale_JESSubTotalScaleDown",
    #"_CMS_scale_JESSubTotalAbsoluteUp","_CMS_scale_JESSubTotalAbsoluteDown",
    #"_CMS_scale_JESSubTotalMCUp","_CMS_scale_JESSubTotalMCDown",
    #"_CMS_scale_JESTotalUp","_CMS_scale_JESTotalDown",
    #"_CMS_scale_JESTotalNoFlavorUp","_CMS_scale_JESTotalNoFlavorDown",
    #"_CMS_scale_JESTotalNoTimeUp","_CMS_scale_JESTotalNoTimeDown",
    #"_CMS_scale_JESTotalNoFlavorNoTimeUp","_CMS_scale_JESTotalNoFlavorNoTimeDown",
    #"_CMS_scale_JESFlavorZJetUp","_CMS_scale_JESFlavorZJetDown",
    #"_CMS_scale_JESFlavorPhotonJetUp","_CMS_scale_JESFlavorPhotonJetDown",
    #"_CMS_scale_JESFlavorPureGluonUp","_CMS_scale_JESFlavorPureGluonDown",
    #"_CMS_scale_JESFlavorPureQuarkUp","_CMS_scale_JESFlavorPureQuarkDown",
    #"_CMS_scale_JESFlavorPureCharmUp","_CMS_scale_JESFlavorPureCharmDown",
    #"_CMS_scale_JESFlavorPureBottomUp","_CMS_scale_JESFlavorPureBottomDown",
    #"_CMS_scale_JESTimeRunBCDUp","_CMS_scale_JESTimeRunBCDDown",
    #"_CMS_scale_JESTimeRunEFUp","_CMS_scale_JESTimeRunEFDown",
    #"_CMS_scale_JESTimeRunGUp","_CMS_scale_JESTimeRunGDown",
    #"_CMS_scale_JESTimeRunHUp","_CMS_scale_JESTimeRunHDown",

]

systsTtbar= [
  "_CMS_PS_fsrUp","_CMS_PS_fsrDown",
  "_CMS_PS_isrUp","_CMS_PS_isrDown",
  "_CMS_PS_hdampUp","_CMS_PS_hdampDown",
  "_CMS_ueUp","_CMS_ueDown",
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

    #"_CMS_scale_JESUp","_CMS_scale_JESDown",
    "_CMS_res_JERUp","_CMS_res_JERDown",
    "_CMS_scale_JESAbsoluteStatUp","_CMS_scale_JESAbsoluteStatDown",
    "_CMS_scale_JESAbsoluteScaleUp","_CMS_scale_JESAbsoluteScaleDown",
    #"_CMS_scale_JESAbsoluteFlavMapUp","_CMS_scale_JESAbsoluteFlavMapDown",
    "_CMS_scale_JESAbsoluteMPFBiasUp","_CMS_scale_JESAbsoluteMPFBiasDown",
    "_CMS_scale_JESFragmentationUp","_CMS_scale_JESFragmentationDown",
    "_CMS_scale_JESSinglePionECALUp","_CMS_scale_JESSinglePionECALDown",
    "_CMS_scale_JESSinglePionHCALUp","_CMS_scale_JESSinglePionHCALDown",
    "_CMS_scale_JESFlavorQCDUp","_CMS_scale_JESFlavorQCDDown",
    "_CMS_scale_JESTimePtEtaUp","_CMS_scale_JESTimePtEtaDown",
    "_CMS_scale_JESRelativeJEREC1Up","_CMS_scale_JESRelativeJEREC1Down",
    "_CMS_scale_JESRelativeJEREC2Up","_CMS_scale_JESRelativeJEREC2Down",
    "_CMS_scale_JESRelativeJERHFUp","_CMS_scale_JESRelativeJERHFDown",
    "_CMS_scale_JESRelativePtBBUp","_CMS_scale_JESRelativePtBBDown",
    "_CMS_scale_JESRelativePtEC1Up","_CMS_scale_JESRelativePtEC1Down",
    "_CMS_scale_JESRelativePtEC2Up","_CMS_scale_JESRelativePtEC2Down",
    "_CMS_scale_JESRelativePtHFUp","_CMS_scale_JESRelativePtHFDown",
    "_CMS_scale_JESRelativeBalUp","_CMS_scale_JESRelativeBalDown",
    "_CMS_scale_JESRelativeFSRUp","_CMS_scale_JESRelativeFSRDown",
    "_CMS_scale_JESRelativeStatFSRUp","_CMS_scale_JESRelativeStatFSRDown",
    "_CMS_scale_JESRelativeStatECUp","_CMS_scale_JESRelativeStatECDown",
    "_CMS_scale_JESRelativeStatHFUp","_CMS_scale_JESRelativeStatHFDown",
    "_CMS_scale_JESPileUpDataMCUp","_CMS_scale_JESPileUpDataMCDown",
    "_CMS_scale_JESPileUpPtRefUp","_CMS_scale_JESPileUpPtRefDown",
    "_CMS_scale_JESPileUpPtBBUp","_CMS_scale_JESPileUpPtBBDown",
    "_CMS_scale_JESPileUpPtEC1Up","_CMS_scale_JESPileUpPtEC1Down",
    "_CMS_scale_JESPileUpPtEC2Up","_CMS_scale_JESPileUpPtEC2Down",
    "_CMS_scale_JESPileUpPtHFUp","_CMS_scale_JESPileUpPtHFDown",
    #"_CMS_scale_JESPileUpMuZeroUp","_CMS_scale_JESPileUpMuZeroDown",
    #"_CMS_scale_JESPileUpEnvelopeUp","_CMS_scale_JESPileUpEnvelopeDown",
    #"_CMS_scale_JESSubTotalPileUpUp","_CMS_scale_JESSubTotalPileUpDown",
    #"_CMS_scale_JESSubTotalRelativeUp","_CMS_scale_JESSubTotalRelativeDown",
    #"_CMS_scale_JESSubTotalPtUp","_CMS_scale_JESSubTotalPtDown",
    #"_CMS_scale_JESSubTotalScaleUp","_CMS_scale_JESSubTotalScaleDown",
    #"_CMS_scale_JESSubTotalAbsoluteUp","_CMS_scale_JESSubTotalAbsoluteDown",
    #"_CMS_scale_JESSubTotalMCUp","_CMS_scale_JESSubTotalMCDown",
    #"_CMS_scale_JESTotalUp","_CMS_scale_JESTotalDown",
    #"_CMS_scale_JESTotalNoFlavorUp","_CMS_scale_JESTotalNoFlavorDown",
    #"_CMS_scale_JESTotalNoTimeUp","_CMS_scale_JESTotalNoTimeDown",
    #"_CMS_scale_JESTotalNoFlavorNoTimeUp","_CMS_scale_JESTotalNoFlavorNoTimeDown",
    #"_CMS_scale_JESFlavorZJetUp","_CMS_scale_JESFlavorZJetDown",
    #"_CMS_scale_JESFlavorPhotonJetUp","_CMS_scale_JESFlavorPhotonJetDown",
    #"_CMS_scale_JESFlavorPureGluonUp","_CMS_scale_JESFlavorPureGluonDown",
    #"_CMS_scale_JESFlavorPureQuarkUp","_CMS_scale_JESFlavorPureQuarkDown",
    #"_CMS_scale_JESFlavorPureCharmUp","_CMS_scale_JESFlavorPureCharmDown",
    #"_CMS_scale_JESFlavorPureBottomUp","_CMS_scale_JESFlavorPureBottomDown",
    #"_CMS_scale_JESTimeRunBCDUp","_CMS_scale_JESTimeRunBCDDown",
    #"_CMS_scale_JESTimeRunEFUp","_CMS_scale_JESTimeRunEFDown",
    #"_CMS_scale_JESTimeRunGUp","_CMS_scale_JESTimeRunGDown",
    #"_CMS_scale_JESTimeRunHUp","_CMS_scale_JESTimeRunHDown",
      "_CMS_PS_fsrUp","_CMS_PS_fsrDown",
  "_CMS_PS_isrUp","_CMS_PS_isrDown",
  "_CMS_PS_hdampUp","_CMS_PS_hdampDown",
  "_CMS_ueUp","_CMS_ueDown",
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

    #"_CMS_scale_JESUp","_CMS_scale_JESDown",
    "_CMS_res_JERUp","_CMS_res_JERDown",
    "_CMS_scale_JESAbsoluteStatUp","_CMS_scale_JESAbsoluteStatDown",
    "_CMS_scale_JESAbsoluteScaleUp","_CMS_scale_JESAbsoluteScaleDown",
    #"_CMS_scale_JESAbsoluteFlavMapUp","_CMS_scale_JESAbsoluteFlavMapDown",
    "_CMS_scale_JESAbsoluteMPFBiasUp","_CMS_scale_JESAbsoluteMPFBiasDown",
    "_CMS_scale_JESFragmentationUp","_CMS_scale_JESFragmentationDown",
    "_CMS_scale_JESSinglePionECALUp","_CMS_scale_JESSinglePionECALDown",
    "_CMS_scale_JESSinglePionHCALUp","_CMS_scale_JESSinglePionHCALDown",
    "_CMS_scale_JESFlavorQCDUp","_CMS_scale_JESFlavorQCDDown",
    "_CMS_scale_JESTimePtEtaUp","_CMS_scale_JESTimePtEtaDown",
    "_CMS_scale_JESRelativeJEREC1Up","_CMS_scale_JESRelativeJEREC1Down",
    "_CMS_scale_JESRelativeJEREC2Up","_CMS_scale_JESRelativeJEREC2Down",
    "_CMS_scale_JESRelativeJERHFUp","_CMS_scale_JESRelativeJERHFDown",
    "_CMS_scale_JESRelativePtBBUp","_CMS_scale_JESRelativePtBBDown",
    "_CMS_scale_JESRelativePtEC1Up","_CMS_scale_JESRelativePtEC1Down",
    "_CMS_scale_JESRelativePtEC2Up","_CMS_scale_JESRelativePtEC2Down",
    "_CMS_scale_JESRelativePtHFUp","_CMS_scale_JESRelativePtHFDown",
    "_CMS_scale_JESRelativeBalUp","_CMS_scale_JESRelativeBalDown",
    "_CMS_scale_JESRelativeFSRUp","_CMS_scale_JESRelativeFSRDown",
    "_CMS_scale_JESRelativeStatFSRUp","_CMS_scale_JESRelativeStatFSRDown",
    "_CMS_scale_JESRelativeStatECUp","_CMS_scale_JESRelativeStatECDown",
    "_CMS_scale_JESRelativeStatHFUp","_CMS_scale_JESRelativeStatHFDown",
    "_CMS_scale_JESPileUpDataMCUp","_CMS_scale_JESPileUpDataMCDown",
    "_CMS_scale_JESPileUpPtRefUp","_CMS_scale_JESPileUpPtRefDown",
    "_CMS_scale_JESPileUpPtBBUp","_CMS_scale_JESPileUpPtBBDown",
    "_CMS_scale_JESPileUpPtEC1Up","_CMS_scale_JESPileUpPtEC1Down",
    "_CMS_scale_JESPileUpPtEC2Up","_CMS_scale_JESPileUpPtEC2Down",
    "_CMS_scale_JESPileUpPtHFUp","_CMS_scale_JESPileUpPtHFDown",
    #"_CMS_scale_JESPileUpMuZeroUp","_CMS_scale_JESPileUpMuZeroDown",
    #"_CMS_scale_JESPileUpEnvelopeUp","_CMS_scale_JESPileUpEnvelopeDown",
    #"_CMS_scale_JESSubTotalPileUpUp","_CMS_scale_JESSubTotalPileUpDown",
    #"_CMS_scale_JESSubTotalRelativeUp","_CMS_scale_JESSubTotalRelativeDown",
    #"_CMS_scale_JESSubTotalPtUp","_CMS_scale_JESSubTotalPtDown",
    #"_CMS_scale_JESSubTotalScaleUp","_CMS_scale_JESSubTotalScaleDown",
    #"_CMS_scale_JESSubTotalAbsoluteUp","_CMS_scale_JESSubTotalAbsoluteDown",
    #"_CMS_scale_JESSubTotalMCUp","_CMS_scale_JESSubTotalMCDown",
    #"_CMS_scale_JESTotalUp","_CMS_scale_JESTotalDown",
    #"_CMS_scale_JESTotalNoFlavorUp","_CMS_scale_JESTotalNoFlavorDown",
    #"_CMS_scale_JESTotalNoTimeUp","_CMS_scale_JESTotalNoTimeDown",
    #"_CMS_scale_JESTotalNoFlavorNoTimeUp","_CMS_scale_JESTotalNoFlavorNoTimeDown",
    #"_CMS_scale_JESFlavorZJetUp","_CMS_scale_JESFlavorZJetDown",
    #"_CMS_scale_JESFlavorPhotonJetUp","_CMS_scale_JESFlavorPhotonJetDown",
    #"_CMS_scale_JESFlavorPureGluonUp","_CMS_scale_JESFlavorPureGluonDown",
    #"_CMS_scale_JESFlavorPureQuarkUp","_CMS_scale_JESFlavorPureQuarkDown",
    #"_CMS_scale_JESFlavorPureCharmUp","_CMS_scale_JESFlavorPureCharmDown",
    #"_CMS_scale_JESFlavorPureBottomUp","_CMS_scale_JESFlavorPureBottomDown",
    #"_CMS_scale_JESTimeRunBCDUp","_CMS_scale_JESTimeRunBCDDown",
    #"_CMS_scale_JESTimeRunEFUp","_CMS_scale_JESTimeRunEFDown",
    #"_CMS_scale_JESTimeRunGUp","_CMS_scale_JESTimeRunGDown",
    #"_CMS_scale_JESTimeRunHUp","_CMS_scale_JESTimeRunHDown",
      "","",
  "","",
  "","",
  "","",
]

mcWeightAll='35.922'
mcWeight='35.922*2.0'


mcTriggerWeight='((1.0)*(internalEleTriggerWeight*internalMuTriggerWeight)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))))'
#mcTriggerWeight='((1.0)*(Weight_ElectronSFTrigger*Weight_MuonSFTrigger)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))) )'
#mcTriggerWeight='((1.0)*(1.0)*((N_TightElectrons==1 && Triggered_HLT_Ele27_eta2p1_WPTight_Gsf_vX==1)||(N_TightMuons==1 && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))))'

#sfs="Weight_ElectronSFID*Weight_MuonSFID*Weight_MuonSFIso*Weight_ElectronSFGFS*Weight_MuonSFHIP"
sfs="internalEleIDWeight*internalMuIDWeight*internalEleIsoWeight*internalMuIsoWeight*internalEleGFSWeight*internalMuHIPWeight"

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
		    "dummyWeight_CMS_ttH_eff_elUp:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))*internalEleIDWeightUp*internalMuIDWeight*internalEleIsoWeightUp*internalMuIsoWeight*internalEleGFSWeightUp*internalMuHIPWeight*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
		    "dummyWeight_CMS_ttH_eff_elDown:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))"+"*internalEleIDWeightDown*internalMuIDWeight*internalEleIsoWeightDown*internalMuIsoWeight*internalEleGFSWeightDown*internalMuHIPWeight*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
		     "dummyWeight_CMS_ttH_eff_muUp:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))"+"*internalEleIDWeight*internalMuIDWeightUp*internalEleIsoWeight*internalMuIsoWeightUp*internalEleGFSWeight*internalMuHIPWeightUp*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
		    "dummyWeight_CMS_ttH_eff_muDown:=(1*Weight_pu69p2*((Weight>0)-(Weight<0))"+"*internalEleIDWeight*internalMuIDWeightDown*internalEleIsoWeight*internalMuIsoWeightDown*internalEleGFSWeight*internalMuHIPWeightDown*"+mcTriggerWeight+"*internalCSVweight)*(DoWeights==1)+(DoWeights==0)*1.0",
		    
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
    #"_CMS_scale_JESUp","_CMS_scale_JESDown",
     "_CMS_res_JERUp","_CMS_res_JERDown",
    "_CMS_scale_JESAbsoluteStatUp","_CMS_scale_JESAbsoluteStatDown",
    "_CMS_scale_JESAbsoluteScaleUp","_CMS_scale_JESAbsoluteScaleDown",
    #"_CMS_scale_JESAbsoluteFlavMapUp","_CMS_scale_JESAbsoluteFlavMapDown",
    "_CMS_scale_JESAbsoluteMPFBiasUp","_CMS_scale_JESAbsoluteMPFBiasDown",
    "_CMS_scale_JESFragmentationUp","_CMS_scale_JESFragmentationDown",
    "_CMS_scale_JESSinglePionECALUp","_CMS_scale_JESSinglePionECALDown",
    "_CMS_scale_JESSinglePionHCALUp","_CMS_scale_JESSinglePionHCALDown",
    "_CMS_scale_JESFlavorQCDUp","_CMS_scale_JESFlavorQCDDown",
    "_CMS_scale_JESTimePtEtaUp","_CMS_scale_JESTimePtEtaDown",
    "_CMS_scale_JESRelativeJEREC1Up","_CMS_scale_JESRelativeJEREC1Down",
    "_CMS_scale_JESRelativeJEREC2Up","_CMS_scale_JESRelativeJEREC2Down",
    "_CMS_scale_JESRelativeJERHFUp","_CMS_scale_JESRelativeJERHFDown",
    "_CMS_scale_JESRelativePtBBUp","_CMS_scale_JESRelativePtBBDown",
    "_CMS_scale_JESRelativePtEC1Up","_CMS_scale_JESRelativePtEC1Down",
    "_CMS_scale_JESRelativePtEC2Up","_CMS_scale_JESRelativePtEC2Down",
    "_CMS_scale_JESRelativePtHFUp","_CMS_scale_JESRelativePtHFDown",
    "_CMS_scale_JESRelativeBalUp","_CMS_scale_JESRelativeBalDown",
    "_CMS_scale_JESRelativeFSRUp","_CMS_scale_JESRelativeFSRDown",
    "_CMS_scale_JESRelativeStatFSRUp","_CMS_scale_JESRelativeStatFSRDown",
    "_CMS_scale_JESRelativeStatECUp","_CMS_scale_JESRelativeStatECDown",
    "_CMS_scale_JESRelativeStatHFUp","_CMS_scale_JESRelativeStatHFDown",
    "_CMS_scale_JESPileUpDataMCUp","_CMS_scale_JESPileUpDataMCDown",
    "_CMS_scale_JESPileUpPtRefUp","_CMS_scale_JESPileUpPtRefDown",
    "_CMS_scale_JESPileUpPtBBUp","_CMS_scale_JESPileUpPtBBDown",
    "_CMS_scale_JESPileUpPtEC1Up","_CMS_scale_JESPileUpPtEC1Down",
    "_CMS_scale_JESPileUpPtEC2Up","_CMS_scale_JESPileUpPtEC2Down",
    "_CMS_scale_JESPileUpPtHFUp","_CMS_scale_JESPileUpPtHFDown",
    #"_CMS_scale_JESPileUpMuZeroUp","_CMS_scale_JESPileUpMuZeroDown",
    #"_CMS_scale_JESPileUpEnvelopeUp","_CMS_scale_JESPileUpEnvelopeDown",
    #"_CMS_scale_JESSubTotalPileUpUp","_CMS_scale_JESSubTotalPileUpDown",
    #"_CMS_scale_JESSubTotalRelativeUp","_CMS_scale_JESSubTotalRelativeDown",
    #"_CMS_scale_JESSubTotalPtUp","_CMS_scale_JESSubTotalPtDown",
    #"_CMS_scale_JESSubTotalScaleUp","_CMS_scale_JESSubTotalScaleDown",
    #"_CMS_scale_JESSubTotalAbsoluteUp","_CMS_scale_JESSubTotalAbsoluteDown",
    #"_CMS_scale_JESSubTotalMCUp","_CMS_scale_JESSubTotalMCDown",
    #"_CMS_scale_JESTotalUp","_CMS_scale_JESTotalDown",
    #"_CMS_scale_JESTotalNoFlavorUp","_CMS_scale_JESTotalNoFlavorDown",
    #"_CMS_scale_JESTotalNoTimeUp","_CMS_scale_JESTotalNoTimeDown",
    #"_CMS_scale_JESTotalNoFlavorNoTimeUp","_CMS_scale_JESTotalNoFlavorNoTimeDown",
    #"_CMS_scale_JESFlavorZJetUp","_CMS_scale_JESFlavorZJetDown",
    #"_CMS_scale_JESFlavorPhotonJetUp","_CMS_scale_JESFlavorPhotonJetDown",
    #"_CMS_scale_JESFlavorPureGluonUp","_CMS_scale_JESFlavorPureGluonDown",
    #"_CMS_scale_JESFlavorPureQuarkUp","_CMS_scale_JESFlavorPureQuarkDown",
    #"_CMS_scale_JESFlavorPureCharmUp","_CMS_scale_JESFlavorPureCharmDown",
    #"_CMS_scale_JESFlavorPureBottomUp","_CMS_scale_JESFlavorPureBottomDown",
    #"_CMS_scale_JESTimeRunBCDUp","_CMS_scale_JESTimeRunBCDDown",
    #"_CMS_scale_JESTimeRunEFUp","_CMS_scale_JESTimeRunEFDown",
    #"_CMS_scale_JESTimeRunGUp","_CMS_scale_JESTimeRunGDown",
    #"_CMS_scale_JESTimeRunHUp","_CMS_scale_JESTimeRunHDown",

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
  "_CMS_PS_fsrUp","_CMS_PS_fsrDown",
  "_CMS_PS_isrUp","_CMS_PS_isrDown",
  "_CMS_PS_hdampUp","_CMS_PS_hdampDown",
  "_CMS_ueUp","_CMS_ueDown",
]
PSSystFileNames=[
  "fsr_up","fsr_down",
  "isr_up","isr_down",
  "hdamp_up","hdamp_down",
  "ue_up","ue_down",
]
path_additionalSamples="/nfs/dust/cms/user/mwassmer/ntuples/additional_samples"
  

assert len(errorSystNames)==len(weightSystNames+otherSystNames+PSSystNames)

# samples
# input path 
#path_Matthias="/nfs/dust/cms/user/matsch/ntuples/Spring17/v3"
path_data="/nfs/dust/cms/user/mwassmer/ntuples/data_new"
path_minorBackgrounds="/nfs/dust/cms/user/mwassmer/ntuples/minor_backgrounds"
path_karim="/nfs/dust/cms/user/kelmorab/trees_Spring17_v4/"



# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
sampleDict=SampleDictionary()
sampleDict.doPrintout()

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
                    Sample('SingleMu',ROOT.kBlack,path_data+'/SingleMuon*/*nominal*.root',sel_singlemu,'SingleMu',samDict=sampleDict),
                    Sample('SingleEl',ROOT.kBlack,path_data+'/SingleElectron*/*nominal*.root',sel_singleel,'SingleEl',samDict=sampleDict)
]

## DANGERZONE 
# Recheck these numbers !!!
# Use incl and SL samples together
# SL sample has nominally 152720952  events
#After skims but before ntupling at least 4 SL files are missing with events 235523/58319342 = 0.004038506 -> 0.995961494
# incl sample has 77229341 events
# branching for Single lepton = 43.8 (pdg) -> nSL = 77229341*0.438 + 152720952*0.995961494
# the total number of SL events in both samples is 185930638.8770223 . This also included the fact that 3 MiniAOD files are missing
# Now Calculate new XS weights to mix the samples together
# incl ttbar XS = 831.76
# SL ttbar XS = 831.76*0.438 = 364.31088
# => weight had and DL = 831.76*1000/77229341 = 0.01077
# => weight SL = 364.31088*1000/185930638.8770223 = 0.00195939



ttbarMCWeight='*((0.001958064*(N_GenTopHad==1 && N_GenTopLep==1)+0.01077*(N_GenTopLep==2 && N_GenTopHad==0)+0.01077*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)'

ttbarPathS=path_karim+'/ttbar_incl/*nominal*.root'+';'+path_karim+'/ttbar_excl_SL/*nominal*.root'

print "controlsamples"
samplesControlPlots=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_karim+'/ttH*/*nominal*.root',mcWeightAll,'ttH',systsAllSamples,samDict=sampleDict) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight,'ttbar',systsAllSamples) ,     
                    Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeightAll+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeightAll+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict),
                    Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeightAll+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeightAll+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeightAll+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict),  
                    Sample('Single Top',ROOT.kMagenta,path_karim+'/st*/*nominal*.root',mcWeightAll,'SingleTop',systsAllSamples,samDict=sampleDict) , 
                    Sample('V+jets',ROOT.kGreen-3,path_minorBackgrounds+'/*ets*/*nominal*.root',mcWeightAll,'Vjets',systsAllSamples,samDict=sampleDict) , 
                    Sample('t#bar{t}+V',ROOT.kBlue-10,path_karim+'/tt?_*/*nominal*.root',mcWeightAll,'ttV',systsAllSamples,samDict=sampleDict),         
                    Sample('Diboson',ROOT.kAzure+2,path_minorBackgrounds+'/??_pythia_*/*nominal*.root',mcWeightAll,'Diboson',systsAllSamples,samDict=sampleDict) , 
#                    Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcWeight,'QCD') , 
]

#print "limit samples"
samplesLimits=[
                    Sample('t#bar{t}H',ROOT.kBlue+1,path_karim+'/ttH*/*nominal*.root',mcWeight+evenSel,'ttH',systsAllSamples,samDict=sampleDict) ,     
#                    Sample('t#bar{t}',ROOT.kRed+1,path_80x+'/ttbar/*nominal*.root',mcWeight+evenSel,'ttbar',samDict=sampleDict) ,     
                    Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_karim+'/ttHbb/*nominal*.root','1.0*'+mcWeight+evenSel,'ttH_hbb',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hccSel,'ttH_hcc',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+httSel,'ttH_htt',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hggSel,'ttH_hgg',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hglugluSel,'ttH_hgluglu',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hwwSel,'ttH_hww',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hzzSel,'ttH_hzz',systsAllSamples,samDict=sampleDict) ,  
                    Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_karim+'/ttHnonbb/*nominal*.root','1.0*'+mcWeight+evenSel+hzgSel,'ttH_hzg',systsAllSamples,samDict=sampleDict) ,
                    
                    Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systsAllSamples+systsTtbar+systs_tt_lf,samDict=sampleDict),
                    Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systsAllSamples+systsTtbar+systs_tt_cc,samDict=sampleDict),
                    Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systsAllSamples+systsTtbar+systs_tt_b,samDict=sampleDict),
                    Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systsAllSamples+systsTtbar+systs_tt_2b,samDict=sampleDict),
                    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeight+evenSel+ttbarMCWeight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systsAllSamples+systsTtbar+systs_tt_bb,samDict=sampleDict), 
                    Sample('Single Top',ROOT.kMagenta,path_karim+'/st*/*nominal*.root',mcWeightAll,'singlet',systsAllSamples,samDict=sampleDict) , 
                    Sample('Z+jets',ROOT.kGreen-3,path_minorBackgrounds+'/Zjets*/*nominal*.root',mcWeightAll,'zjets',systsAllSamples,samDict=sampleDict) , 
                    Sample('W+jets',ROOT.kGreen-7,path_minorBackgrounds+'/Wjets*/*nominal*.root',mcWeightAll,'wjets',systsAllSamples,samDict=sampleDict) , 
                    Sample('t#bar{t}+W',ROOT.kBlue-10,path_karim+'/ttW_*/*nominal*.root',mcWeightAll,'ttbarW',systsAllSamples,samDict=sampleDict),
                    Sample('t#bar{t}+Z',ROOT.kBlue-6,path_karim+'/ttZ_*/*nominal*.root',mcWeightAll,'ttbarZ',systsAllSamples,samDict=sampleDict),
                    Sample('Diboson',ROOT.kAzure+2,path_minorBackgrounds+'/??_pythia_*/*nominal*.root',mcWeightAll,'Diboson',systsAllSamples,samDict=sampleDict) , 
##                    Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcWeightAll,'QCD',samDict=sampleDict) , 
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

