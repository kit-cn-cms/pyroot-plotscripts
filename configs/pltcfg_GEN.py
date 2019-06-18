import sys
import os
import ROOT
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses

sel_singleel="*1.0" # need to veto muon events in electron dataset to avoid double counting
sel_singlemu="*1.0" # and vice versa...
#sel_MET="*(Evt_Pt_MET>20.)"
sel_MET="*1.0"
#sel_StrangeMuWeights='*(abs(Weight_scale_variation_muR_0p5_muF_0p5)<=100 && abs(Weight_scale_variation_muR_0p5_muF_1p0)<=100 && abs(Weight_scale_variation_muR_0p5_muF_2p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_1p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_1p0_muF_2p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_0p5)<=100 && abs(Weight_scale_variation_muR_2p0_muF_1p0)<=100 && abs(Weight_scale_variation_muR_2p0_muF_2p0)<=100)'
sel_StrangeMuWeights='*1.0'


# names of the systematics (proper names needed e.g. for combination)
# TODO Add CSV SFs and uncertainties
weightSystNames=[
                    "",
]

systsAllSamples=[
                    "",
]

systs_tt_all= [
]

systs_tt_lf=[]
systs_tt_b=[]
systs_tt_2b=[]
systs_tt_bb=[]
systs_tt_cc=[]



mcWeightAll='1.0'
mcWeight='1.0'

# TODO Add Trigger SFs
#mcTriggerWeight='((1.0) * (internalEleTriggerWeight*(N_LooseMuons==0 && N_TightElectrons==1)* (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1) +internalMuTriggerWeight*(N_LooseElectrons==0 && N_TightMuons==1)*(Muon_Pt[0]>29.) *(Triggered_HLT_IsoMu27_vX==1)))*(N_Jets>=4 && N_BTagsM>=3)'
mcTriggerWeight='(1.0)'
#mcTriggerWeight='((1.0) * (1*(N_LooseMuons==0 && N_TightElectrons==1)* (1) +1*(N_LooseElectrons==0 && N_TightMuons==1) *(1)))*(N_Jets>=4 && N_BTagsM>=3)'

#TODO Check that SFs and uncertainties are correct
sfs="1.0"
#sfs="internalEleIDWeight*internalMuIDWeight*internalMuIsoWeight*internalEleGFSWeight*internalMuHIPWeight"

usualWeights="(1*Weight_GEN_nom)"+"*"+sfs
#usualWeights="(1*(Weight_GEN_nom))"+"*"+sfs

evenSel="*1.0"


#ttbarMCWeight='*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))'
#ttbarMCWeight='*0.0084896859/Weight_XS'

systWeights=[
                    "NomWeight:="+usualWeights+"*"+mcTriggerWeight+"*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
]


assert len(weightSystNames)==len(systWeights)


systs_tt_and_ttH=[
                    # ~ "_CMS_ttHbb_PDF_2017Up","_CMS_ttHbb_PDF_2017Down",
                    # ~ "_CMS_ttHbb_scaleMuRUp","_CMS_ttHbb_scaleMuRDown",
                    # ~ "_CMS_ttHbb_scaleMuFUp","_CMS_ttHbb_scaleMuFDown",
                    #"_CMS_ttHbb_ISRUp","_CMS_ttHbb_ISRDown",
                    #"_CMS_ttHbb_FSRUp","_CMS_ttHbb_FSRDown",
                    ]
systs_tt_and_ttH_weights=[
                        # ~ "dummyWeight_CMS_ttH_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttH_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                        # ~ "dummyWeight_CMS_ttH_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttH_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                        # ~ "dummyWeight_CMS_ttH_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttH_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                        #"dummyWeight_CMS_ttH_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                        #"dummyWeight_CMS_ttH_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        #"dummyWeight_CMS_ttH_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                        ]

systs_ttH=[
  #"_CMS_ttHbb_ttH_PDFUp","_CMS_ttHbb_ttH_PDFDown",
  #"_CMS_ttHbb_ttH_scaleMuRUp","_CMS_ttHbb_ttH_scaleMuRDown",
  #"_CMS_ttHbb_ttH_scaleMuFUp","_CMS_ttHbb_ttH_scaleMuFDown",
  #"_CMS_ttHbb_ttH_ISR_2017Up","_CMS_ttHbb_ttH_ISR_2017Down",
  #"_CMS_ttHbb_ttH_FSR_2017Up","_CMS_ttHbb_ttH_FSR_2017Down",
  ]
systs_ttH_weights=[
  ]


systs_tt_all=[
                #"_CMS_ttHbb_PDF_ttbarUp","_CMS_ttHbb_PDF_ttbarDown",
                #"_CMS_ttHbb_scaleMuR_ttbarUp","_CMS_ttHbb_scaleMuR_ttbarDown",
                #"_CMS_ttHbb_scaleMuF_ttbarUp","_CMS_ttHbb_scaleMuF_ttbarDown",
                #"_CMS_ttHbb_ISR_ttbarUp","_CMS_ttHbb_ISR_ttbarDown",
                #"_CMS_ttHbb_FSR_ttbarUp","_CMS_ttHbb_FSR_ttbarDown",
                ]
systs_tt_all_weights=[
                    #"dummyWeight_CMS_ttH_ttbar_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*internalNormFactor_weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbar_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*internalNormFactor_weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    #"dummyWeight_CMS_ttH_ttbar_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*internalNormFactor_weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbar_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*internalNormFactor_weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    #"dummyWeight_CMS_ttH_ttbar_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*internalNormFactor_weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbar_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*internalNormFactor_weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    #"dummyWeight_CMS_ttH_ttbar_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ttbar_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    #"dummyWeight_CMS_ttH_ttbar_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbar_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    ]



systs_tt_lf=[
            #"_CMS_ttHbb_PDF_ttbarOtherUp","_CMS_ttHbb_PDF_ttbarOtherDown",
            #"_CMS_ttHbb_scaleMuR_ttbarOtherUp","_CMS_ttHbb_scaleMuR_ttbarOtherDown",
            #"_CMS_ttHbb_scaleMuF_ttbarOtherUp","_CMS_ttHbb_scaleMuF_ttbarOtherDown",
            # ~ "_CMS_ttHbb_ISR_ttbarOther_2017Up","_CMS_ttHbb_ISR_ttbarOther_2017Down",
            # ~ "_CMS_ttHbb_FSR_ttbarOther_2017Up","_CMS_ttHbb_FSR_ttbarOther_2017Down",
            ]
systs_tt_lf_weights=[
                    #"dummyWeight_CMS_ttH_ttbarOther_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*internalNormFactor_weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarOther_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*internalNormFactor_weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarOther_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*internalNormFactor_weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarOther_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*internalNormFactor_weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarOther_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*internalNormFactor_weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarOther_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*internalNormFactor_weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    # ~ "dummyWeight_CMS_ttH_ttbarOther_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ttbarOther_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    # ~ "dummyWeight_CMS_ttH_ttbarOther_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    # ~ "dummyWeight_CMS_ttH_ttbarOther_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    ]

systs_tt_b=[
            #"_CMS_ttHbb_PDF_ttbarPlusBUp","_CMS_ttHbb_PDF_ttbarPlusBDown",
            #"_CMS_ttHbb_scaleMuR_ttbarPlusBUp","_CMS_ttHbb_scaleMuR_ttbarPlusBDown",
            #"_CMS_ttHbb_scaleMuF_ttbarPlusBUp","_CMS_ttHbb_scaleMuF_ttbarPlusBDown",
            # ~ "_CMS_ttHbb_ISR_ttbarPlusB_2017Up","_CMS_ttHbb_ISR_ttbarPlusB_2017Down",
            # ~ "_CMS_ttHbb_FSR_ttbarPlusB_2017Up","_CMS_ttHbb_FSR_ttbarPlusB_2017Down",
            ]
systs_tt_b_weights=[
                    #"dummyWeight_CMS_ttH_ttbarPlusB_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*internalNormFactor_weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusB_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*internalNormFactor_weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    #"dummyWeight_CMS_ttH_ttbarPlusB_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*internalNormFactor_weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusB_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*internalNormFactor_weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    #"dummyWeight_CMS_ttH_ttbarPlusB_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*internalNormFactor_weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusB_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*internalNormFactor_weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    # ~ "dummyWeight_CMS_ttH_ttbarPlusB_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ttbarPlusB_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    # ~ "dummyWeight_CMS_ttH_ttbarPlusB_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    # ~ "dummyWeight_CMS_ttH_ttbarPlusB_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    ]

systs_tt_2b=[
            #"_CMS_ttHbb_PDF_ttbarPlus2BUp","_CMS_ttHbb_PDF_ttbarPlus2BDown",
            #"_CMS_ttHbb_scaleMuR_ttbarPlus2BUp","_CMS_ttHbb_scaleMuR_ttbarPlus2BDown",
            #"_CMS_ttHbb_scaleMuF_ttbarPlus2BUp","_CMS_ttHbb_scaleMuF_ttbarPlus2BDown",
            # ~ "_CMS_ttHbb_ISR_ttbarPlus2B_2017Up","_CMS_ttHbb_ISR_ttbarPlus2B_2017Down",
            # ~ "_CMS_ttHbb_FSR_ttbarPlus2B_2017Up","_CMS_ttHbb_FSR_ttbarPlus2B_2017Down",
            ]
systs_tt_2b_weights=[
                    #"dummyWeight_CMS_ttH_ttbarPlus2B_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*internalNormFactor_weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlus2B_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*internalNormFactor_weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    #"dummyWeight_CMS_ttH_ttbarPlus2B_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*internalNormFactor_weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlus2B_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*internalNormFactor_weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    #"dummyWeight_CMS_ttH_ttbarPlus2B_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*internalNormFactor_weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlus2B_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*internalNormFactor_weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    # ~ "dummyWeight_CMS_ttH_ttbarPlus2B_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                    "dummyWeight_CMS_ttH_ttbarPlus2B_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    # ~ "dummyWeight_CMS_ttH_ttbarPlus2B_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    # ~ "dummyWeight_CMS_ttH_ttbarPlus2B_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    ]

systs_tt_bb=[
            #"_CMS_ttHbb_PDF_ttbarPlusBBbarUp","_CMS_ttHbb_PDF_ttbarPlusBBbarDown",
            #"_CMS_ttHbb_scaleMuR_ttbarPlusBBbarUp","_CMS_ttHbb_scaleMuR_ttbarPlusBBbarDown",
            #"_CMS_ttHbb_scaleMuF_ttbarPlusBBbarUp","_CMS_ttHbb_scaleMuF_ttbarPlusBBbarDown",
            # ~ "_CMS_ttHbb_ISR_ttbarPlusBBbar_2017Up","_CMS_ttHbb_ISR_ttbarPlusBBbar_2017Down",
            # ~ "_CMS_ttHbb_FSR_ttbarPlusBBbar_2017Up","_CMS_ttHbb_FSR_ttbarPlusBBbar_2017Down",
            ]
systs_tt_bb_weights=[
                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*internalNormFactor_weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*internalNormFactor_weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*internalNormFactor_weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*internalNormFactor_weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*internalNormFactor_weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusBBbar_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*internalNormFactor_weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    # ~ "dummyWeight_CMS_ttH_ttbarPlusBBbar_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                "dummyWeight_CMS_ttH_ttbarPlusBBbar_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",

                    # ~ "dummyWeight_CMS_ttH_ttbarPlusBBbar_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    # ~ "dummyWeight_CMS_ttH_ttbarPlusBBbar_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    ]

systs_tt_cc=[
            #"_CMS_ttHbb_PDF_ttbarPlusCCbarUp","_CMS_ttHbb_PDF_ttbarPlusCCbarDown",
            #"_CMS_ttHbb_scaleMuR_ttbarPlusCCbarUp","_CMS_ttHbb_scaleMuR_ttbarPlusCCbarDown",
            #"_CMS_ttHbb_scaleMuF_ttbarPlusCCbarUp","_CMS_ttHbb_scaleMuF_ttbarPlusCCbarDown",
            # ~ "_CMS_ttHbb_ISR_ttbarPlusCCbar_2017Up","_CMS_ttHbb_ISR_ttbarPlusCCbar_2017Down",
            # ~ "_CMS_ttHbb_FSR_ttbarPlusCCbar_2017Up","_CMS_ttHbb_FSR_ttbarPlusCCbar_2017Down",
            ]
systs_tt_cc_weights=[                                           #"dummyWeight_CMS_ttH_ttbarPlusCCbar_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_up*internalNormFactor_weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusCCbar_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_LHA_306000_down*internalNormFactor_weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarPlusCCbar_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_2p0_muF_1p0*internalNormFactor_weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusCCbar_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_0p5_muF_1p0*internalNormFactor_weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    #"dummyWeight_CMS_ttH_ttbarPlusCCbar_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_2p0*internalNormFactor_weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"dummyWeight_CMS_ttH_ttbarPlusCCbar_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*internalCSVweight*Weight_scale_variation_muR_1p0_muF_0p5*internalNormFactor_weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    # ~ "dummyWeight_CMS_ttH_ttbarPlusCCbar_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",                 "dummyWeight_CMS_ttH_ttbarPlusCCbar_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    
                    # ~ "dummyWeight_CMS_ttH_ttbarPlusCCbar_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    # ~ "dummyWeight_CMS_ttH_ttbarPlusCCbar_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                    ]



systs_ttbb_incl=[
                "_CMS_ttbb_incl_ISRUp","_CMS_ttbb_incl_ISRDown",
                "_CMS_ttbb_incl_FSRUp","_CMS_ttbb_incl_FSRDown",
                
                # ~ "_CMS_ttbb_incl_PDF_Up","_CMS_ttbb_incl_PDF_Down",
                # ~ "_CMS_ttbb_incl_scaleMuRUp","_CMS_ttbb_incl_scaleMuRDown",
                # ~ "_CMS_ttbb_incl_scaleMuFUp","_CMS_ttbb_incl_scaleMuFDown",
                ]
systs_ttbb_incl_weights=[
                        "dummyWeight_CMS_ttbb_incl_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        "dummyWeight_CMS_ttbb_incl_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        
                        "dummyWeight_CMS_ttbb_incl_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        "dummyWeight_CMS_ttbb_incl_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        
                        # ~ "dummyWeight_CMS_ttbb_incl_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_incl_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            
                        # ~ "dummyWeight_CMS_ttbb_incl_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_incl_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            
                        # ~ "dummyWeight_CMS_ttbb_incl_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_incl_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        ]




systs_ttbb_PowHel=[
                "_CMS_ttbb_PowHel_ISRUp","_CMS_ttbb_PowHel_ISRDown",
                "_CMS_ttbb_PowHel_FSRUp","_CMS_ttbb_PowHel_FSRDown",
                
                # ~ "_CMS_ttbb_PowHel_PDF_Up","_CMS_ttbb_PowHel_PDF_Down",
                # ~ "_CMS_ttbb_PowHel_scaleMuRUp","_CMS_ttbb_PowHel_scaleMuRDown",
                # ~ "_CMS_ttbb_PowHel_scaleMuFUp","_CMS_ttbb_PowHel_scaleMuFDown",
                # ~ "_CMS_ttbb_PowHel_scalesUp","_CMS_ttbb_PowHel_scalesDown",
                ]
systs_ttbb_PowHel_weights=[
                        "dummyWeight_CMS_ttbb_PowHel_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        "dummyWeight_CMS_ttbb_PowHel_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        
                        "dummyWeight_CMS_ttbb_PowHel_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        "dummyWeight_CMS_ttbb_PowHel_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        
                        # ~ "dummyWeight_CMS_ttbb_PowHel_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_LHA_NNPDF30_nlo_nf_5_pdfas_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_PowHel_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_LHA_NNPDF30_nlo_nf_5_pdfas_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            
                        # ~ "dummyWeight_CMS_ttbb_PowHel_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_PowHel_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            
                        # ~ "dummyWeight_CMS_ttbb_PowHel_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_PowHel_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_PowHel_scalesUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_2p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_PowHel_scalesDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_0p5_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        ]

systs_ttbb_PowOL=[
                "_CMS_ttbb_PowOL_ISRUp","_CMS_ttbb_PowOL_ISRDown",
                "_CMS_ttbb_PowOL_FSRUp","_CMS_ttbb_PowOL_FSRDown",
                
                # ~ "_CMS_ttbb_PowOL_PDF_Up","_CMS_ttbb_PowOL_PDF_Down",
                # ~ "_CMS_ttbb_PowOL_scaleMuRUp","_CMS_ttbb_PowOL_scaleMuRDown",
                # ~ "_CMS_ttbb_PowOL_scaleMuFUp","_CMS_ttbb_PowOL_scaleMuFDown",
                ]
systs_ttbb_PowOL_weights=[
                        "dummyWeight_CMS_ttbb_PowOL_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        "dummyWeight_CMS_ttbb_PowOL_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        
                        "dummyWeight_CMS_ttbb_PowOL_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        "dummyWeight_CMS_ttbb_PowOL_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        
                        # ~ "dummyWeight_CMS_ttbb_PowOL_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_PowOL_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            
                        # ~ "dummyWeight_CMS_ttbb_PowOL_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_PowOL_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            
                        # ~ "dummyWeight_CMS_ttbb_PowOL_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        # ~ "dummyWeight_CMS_ttbb_PowOL_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                        ]

systs_ttbb_aMCatNLO=[
                    # ~ "_CMS_ttbb_aMCatNLO_ISRUp","_CMS_ttbb_aMCatNLO_ISRDown",
                    # ~ "_CMS_ttbb_aMCatNLO_FSRUp","_CMS_ttbb_aMCatNLO_FSRDown",
                    
                    # ~ "_CMS_ttbb_aMCatNLO_PDF_Up","_CMS_ttbb_aMCatNLO_PDF_Down",
                    # ~ "_CMS_ttbb_aMCatNLO_scaleMuRUp","_CMS_ttbb_aMCatNLO_scaleMuRDown",
                    # ~ "_CMS_ttbb_aMCatNLO_scaleMuFUp","_CMS_ttbb_aMCatNLO_scaleMuFDown",
                    ]
systs_ttbb_aMCatNLO_weights=[
                            # ~ "dummyWeight_CMS_ttbb_aMCatNLO_ISRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_6*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            # ~ "dummyWeight_CMS_ttbb_aMCatNLO_ISRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_8*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            
                            # ~ "dummyWeight_CMS_ttbb_aMCatNLO_FSRUp:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_7*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            # ~ "dummyWeight_CMS_ttbb_aMCatNLO_FSRDown:="+usualWeights+"*"+mcTriggerWeight+"*GenWeight_9*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            
                            # ~ "dummyWeight_CMS_ttbb_aMCatNLO_NNPDFUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_LHA_306000_up*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            # ~ "dummyWeight_CMS_ttbb_aMCatNLO_NNPDFDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_LHA_306000_down*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                                
                            # ~ "dummyWeight_CMS_ttbb_aMCatNLO_scaleMuRUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_2p0_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            # ~ "dummyWeight_CMS_ttbb_aMCatNLO_scaleMuRDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_0p5_muF_1p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                                
                            # ~ "dummyWeight_CMS_ttbb_aMCatNLO_scaleMuFUp:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_1p0_muF_2p0*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            # ~ "dummyWeight_CMS_ttbb_aMCatNLO_scaleMuFDown:="+usualWeights+"*"+mcTriggerWeight+"*Weight_scale_variation_muR_1p0_muF_0p5*1.0*(DoWeights==1)+(DoWeights==0)*1.0",
                            ]

systWeights+=systs_tt_all_weights+systs_tt_lf_weights+systs_tt_b_weights+systs_tt_2b_weights+systs_tt_bb_weights+systs_tt_cc_weights+systs_tt_and_ttH_weights+systs_ttH_weights+systs_ttbb_PowHel_weights+systs_ttbb_PowOL_weights+systs_ttbb_aMCatNLO_weights+systs_ttbb_incl_weights
weightSystNames+=systs_tt_all+systs_tt_lf+systs_tt_b+systs_tt_2b+systs_tt_bb+systs_tt_cc+systs_tt_and_ttH+systs_ttH+systs_ttbb_PowHel+systs_ttbb_PowOL+systs_ttbb_aMCatNLO+systs_ttbb_incl
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
path_ttbbdata="/nfs/dust/cms/user/mhorzela/ttbb_data/ntuples_gen/"
ttbarPathS=path_ttbbdata+'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_new_pmx/*nominal*.root'
ttbbPathPowOL=path_ttbbdata+'TTbb_Powheg_Openloops/*nominal*.root'
ttbbPathPowHel=path_ttbbdata+'TTbb_Powheg_Helac/*nominal*.root'
ttbbPathaMCatNLO=path_ttbbdata+'ttbb_4FS_ckm_NNPDF31_TuneCP5_amcatnlo_madspin_pythia_new_pmx/*nominal*.root'
# VJetsPathS=path_karim_new+'/DYJets*/*nominal*.root'+';'+path_karim_new+'/WJets*/*nominal*.root'
# ttVPathS=path_karim_new+'/TTW*/*nominal*.root'+';'+path_karim_new+'/TTZ*/*nominal*.root'
# dibosonPathS=path_karim_new+'/WW_*/*nominal*.root'+';'+path_karim_new+'/WZ_*/*nominal*.root'+';'+path_karim_new+'/ZZ_*/*nominal*.root'
# stpath=path_karim_new+'/ST_*/*nominal*.root'
# ttHpath=path_karim_new+'/ttHTo*/*nominal*.root'


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

]+systs_tt_lf+systs_tt_cc+systs_tt_b+systs_tt_2b+systs_tt_bb+systs_ttbb_PowHel+systs_ttbb_PowOL+systs_ttbb_aMCatNLO+systs_ttbb_incl+hdamp_ue_systnames_tt_lf+hdamp_ue_systnames_tt_cc+hdamp_ue_systnames_tt_b+hdamp_ue_systnames_tt_2b+hdamp_ue_systnames_tt_bb

otherSystNames+=hdamp_ue_systnames_tt_lf+hdamp_ue_systnames_tt_cc+hdamp_ue_systnames_tt_b+hdamp_ue_systnames_tt_2b+hdamp_ue_systnames_tt_bb

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
sampleDict=plotClasses.SampleDictionary()
sampleDict.doPrintout()
doReadTrees=True

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samplesDataControlPlots=[
]


print "controlsamples"
samplesControlPlots=[
                    plotClasses.Sample('Powheg t#bar{t}+b-jets ',ROOT.kBlack,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB>0)'+sel_MET+sel_StrangeMuWeights,'tt-inclusive',systsAllSamples+systs_tt_all+systs_tt_bb+systs_ttbb_incl+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_bb,samDict=sampleDict, readTrees=doReadTrees),
                    
                    plotClasses.Sample('Powheg+OpenLoops t#bar{t}+b-jets',ROOT.kRed,ttbbPathPowOL,mcWeightAll+'*(GenEvt_I_TTPlusBB>0)'+sel_MET+sel_StrangeMuWeights,'ttbb-PowOL',systsAllSamples+systs_ttbb_PowOL+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_bb,samDict=sampleDict, readTrees=doReadTrees),
                    plotClasses.Sample('Powheg+Helac t#bar{t}+b-jets',ROOT.kSpring-1,ttbbPathPowHel,mcWeightAll+'*(GenEvt_I_TTPlusBB>0)'+sel_MET+sel_StrangeMuWeights,'ttbb-PowHel',systsAllSamples+systs_ttbb_PowHel+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_bb,samDict=sampleDict, readTrees=doReadTrees),
                    # ~ plotClasses.Sample('aMC@NLO t#bar{t}+b-jets',ROOT.kAzure,ttbbPathaMCatNLO,mcWeightAll+'*(GenEvt_I_TTPlusBB>0)'+sel_MET+sel_StrangeMuWeights,'ttbb-aMC',systsAllSamples+systs_ttbb_aMCatNLO+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_bb,samDict=sampleDict, readTrees=doReadTrees),
                    
                    
                    # plotClasses.Sample('t#bar{t}H',ROOT.kBlue+1,path_mwassmer+'/ttH*/*nominal*.root',mcWeightAll+sel_MET,'ttH',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees),
                    # plotClasses.Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,'ttbarOther',systsAllSamples+systs_tt_all+systs_tt_lf+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_lf,samDict=sampleDict, readTrees=doReadTrees),
                    # plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusCC==1)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusCCbar',systsAllSamples+systs_tt_all+systs_tt_cc+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_cc,samDict=sampleDict, readTrees=doReadTrees),
                    #plotClasses.Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==1)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusB',systsAllSamples+systs_tt_all+systs_tt_b+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_b,samDict=sampleDict, readTrees=doReadTrees),
                    #plotClasses.Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==2)'+sel_MET+sel_StrangeMuWeights,'ttbarPlus2B',systsAllSamples+systs_tt_all+systs_tt_2b+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_2b,samDict=sampleDict, readTrees=doReadTrees),
                    #plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==3)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusBBbar',systsAllSamples+systs_tt_all+systs_tt_bb+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_bb,samDict=sampleDict, readTrees=doReadTrees), 
                    

                    
                    # plotClasses.Sample('Single Top',ROOT.kMagenta,stpath,mcWeightAll+sel_MET,'singlet',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    # plotClasses.Sample('V+jets',ROOT.kGreen-3,VJetsPathS,mcWeightAll+sel_MET,'Vjets',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    # plotClasses.Sample('t#bar{t}+V',ROOT.kBlue-10,ttVPathS,mcWeightAll+sel_MET,'ttV',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees),         
                    # plotClasses.Sample('Diboson',ROOT.kAzure+2,dibosonPathS,mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    #plotClasses.Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict, readTrees=doReadTrees),  
]

#print "limit samples"
samplesLimits=[
                    # plotClasses.Sample('t#bar{t}H',ROOT.kBlue+1,path_mwassmer+'/ttH*/*nominal*.root',mcWeight+evenSel+sel_MET,'ttH',systsAllSamples+systs_ttH+systs_tt_and_ttH  ,samDict=sampleDict, readTrees=doReadTrees) ,     
                    # plotClasses.Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path_mwassmer+'/ttHTobb*/*nominal*.root','1.0*'+mcWeight+evenSel+sel_MET,'ttH_hbb',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    # plotClasses.Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hccSel+sel_MET,'ttH_hcc',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    # plotClasses.Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+httSel+sel_MET,'ttH_htt',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    # plotClasses.Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hggSel+sel_MET,'ttH_hgg',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    # plotClasses.Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hglugluSel+sel_MET,'ttH_hgluglu',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    # plotClasses.Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hwwSel+sel_MET,'ttH_hww',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    # plotClasses.Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hzzSel+sel_MET,'ttH_hzz',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,  
                    # plotClasses.Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path_mwassmer+'/ttHToNonbb*/*nominal*.root','1.0*'+mcWeight+evenSel+hzgSel+sel_MET,'ttH_hzg',systsAllSamples+systs_ttH+systs_tt_and_ttH,samDict=sampleDict, readTrees=doReadTrees) ,
                    
                    # plotClasses.Sample('t#bar{t}+lf',ROOT.kRed-7,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+sel_MET+sel_StrangeMuWeights,'ttbarOther',systsAllSamples+systs_tt_all+systs_tt_lf+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_lf,samDict=sampleDict, readTrees=doReadTrees),
                    # plotClasses.Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusCC==1)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusCCbar',systsAllSamples+systs_tt_all+systs_tt_cc+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_cc,samDict=sampleDict, readTrees=doReadTrees),
                    # plotClasses.Sample('t#bar{t}+b',ROOT.kRed-2,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==1)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusB',systsAllSamples+systs_tt_all+systs_tt_b+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_b,samDict=sampleDict, readTrees=doReadTrees),
                    # plotClasses.Sample('t#bar{t}+2b',ROOT.kRed+2,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==2)'+sel_MET+sel_StrangeMuWeights,'ttbarPlus2B',systsAllSamples+systs_tt_all+systs_tt_2b+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_2b,samDict=sampleDict, readTrees=doReadTrees),
                    # plotClasses.Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,ttbarPathS,mcWeightAll+'*(GenEvt_I_TTPlusBB==3)'+sel_MET+sel_StrangeMuWeights,'ttbarPlusBBbar',systsAllSamples+systs_tt_all+systs_tt_bb+systs_tt_and_ttH+hdamp_ue_filenames_tt_all+hdamp_ue_filenames_tt_bb,samDict=sampleDict, readTrees=doReadTrees), 
                    
                    # plotClasses.Sample('Single Top',ROOT.kMagenta,stpath,mcWeightAll+sel_MET,'singlet',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    # plotClasses.Sample('Z+jets',ROOT.kGreen-3,path_karim_new+'/DYJets*/*nominal*.root',mcWeightAll+sel_MET,'zjets',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    # plotClasses.Sample('W+jets',ROOT.kGreen-7,path_karim_new+'/WJets*/*nominal*.root',mcWeightAll+sel_MET,'wjets',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    # plotClasses.Sample('t#bar{t}+W',ROOT.kBlue-10,path_karim_new+'/TTW*/*nominal*.root',mcWeightAll+sel_MET,'ttbarW',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees),
                    # plotClasses.Sample('t#bar{t}+Z',ROOT.kBlue-6,path_karim_new+'/TTZ*/*nominal*.root',mcWeightAll+sel_MET,'ttbarZ',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees),
                    # plotClasses.Sample('Diboson',ROOT.kAzure+2,dibosonPathS,mcWeightAll+sel_MET,'diboson',systsAllSamples,samDict=sampleDict, readTrees=doReadTrees) , 
                    #plotClasses.Sample('QCD',ROOT.kYellow,iso_inverted_paths,'1.'+sel_MET+'*internalQCDweight'+'*(((Weight_XS==1.0)*1.0*((electron_data*'+sel_singleel+')+(muon_data*'+sel_singlemu+')))+((Weight_XS!=1.0)*(-1.0)*35.91823))','QCD',[systsAllSamples[0]]+QCDSystNames,samDict=sampleDict, readTrees=doReadTrees),  
]

