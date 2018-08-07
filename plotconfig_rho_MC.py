import sys
import os
from scriptgenerator import *
from plotutils import *
from plot_cuts_ZPrime_MC import *

    

if WWP=='medium':
  weightsystnamesABCD=[
                    "_" + ABCDversion + "_ABCD_rateUp",
                    "_" + ABCDversion + "_ABCD_rateDown",
                    "_" + ABCDversion + "_ABCD_shapeUp",
                    "_" + ABCDversion + "_ABCD_shapeDown",
                ]

    
if WWP=='medium':
    systweightsABCD=[
                    
                    "" + ABCDversion + "_ABCD_rateUp:=ABCD_rate_systUp*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "" + ABCDversion + "_ABCD_rateDown:=ABCD_rate_systDown*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "" + ABCDversion + "_ABCD_shapeUp:=ABCD_shape_systUp*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "" + ABCDversion + "_ABCD_shapeDown:=ABCD_shape_systDown*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
            
    ]
                    #"nom:=1",r

        
        
else:
    print "Wrong WPs"
    raw_input()

weigthsystnamesMCSFs=[
                    #"_CSV_nominal",
                    #"_CSV_MCSF_systUp",
                    #"_CSV_MCSF_systDown",
                    #"_CSV_nominal",
                    
                    "",
                    
                    "_" + ABCDversion + "_nominal",
                    
                    "_" + ABCDversion + "_MCSF_CSVLFUp",
                    "_" + ABCDversion + "_MCSF_CSVLFDown",
                    "_" + ABCDversion + "_MCSF_CSVHFUp",
                    "_" + ABCDversion + "_MCSF_CSVHFDown",
                    "_" + ABCDversion + "_MCSF_CSVHFStats1Up",
                    "_" + ABCDversion + "_MCSF_CSVHFStats1Down",
                    "_" + ABCDversion + "_MCSF_CSVLFStats1Up",
                    "_" + ABCDversion + "_MCSF_CSVLFStats1Down",
                    "_" + ABCDversion + "_MCSF_CSVHFStats2Up",
                    "_" + ABCDversion + "_MCSF_CSVHFStats2Down",
                    "_" + ABCDversion + "_MCSF_CSVLFStats2Up",
                    "_" + ABCDversion + "_MCSF_CSVLFStats2Down",
                    "_" + ABCDversion + "_MCSF_CSVCErr1Up",
                    "_" + ABCDversion + "_MCSF_CSVCErr1Down",
                    "_" + ABCDversion + "_MCSF_CSVCErr2Up",
                    "_" + ABCDversion + "_MCSF_CSVCErr2Down",
                    "_" + ABCDversion + "_MCSF_toptagUp",
                    "_" + ABCDversion + "_MCSF_toptagDown",
                    "_" + ABCDversion + "_MCSF_topmisstagUp",
                    "_" + ABCDversion + "_MCSF_topmisstagDown",
                    "_" + ABCDversion + "_MCSF_WtagUp",
                    "_" + ABCDversion + "_MCSF_WtagDown",
                    #"_" + ABCDversion + "_MCSF_Wtag_tag_t21antiUp",
                    #"_" + ABCDversion + "_MCSF_Wtag_tag_t21antiDown",
                    #"_" + ABCDversion + "_MCSF_Wtag_mistag_t21Up",
                    #"_" + ABCDversion + "_MCSF_Wtag_mistag_t21Down",
                    #"_" + ABCDversion + "_MCSF_Wtag_mistag_t21antiUp",
                    #"_" + ABCDversion + "_MCSF_Wtag_mistag_t21antiDown",

                    "_" + ABCDversion + "_MCSF_PUUp",
                    "_" + ABCDversion + "_MCSF_PUDown",
                    "_" + ABCDversion + "_MCSF_PDFUp",
                    "_" + ABCDversion + "_MCSF_PDFDown",  
                    "_" + ABCDversion + "_MCSF_LumiUp",
                    "_" + ABCDversion + "_MCSF_LumiDown",
                    "_" + ABCDversion + "_MCSF_TriggerUp",
                    "_" + ABCDversion + "_MCSF_TriggerDown",
                    #"_" + ABCDversion + "_MCSF_renfac_envUp",
                    #"_" + ABCDversion + "_MCSF_renfac_envDown",
                    "_" + ABCDversion + "_ttbarXSUp",
                    "_" + ABCDversion + "_ttbarXSDown",
                    "_" + ABCDversion + "_ST_tWXSUp",
                    "_" + ABCDversion + "_ST_tWXSDown",  
                    "_" + ABCDversion + "_ST_tchanXSUp",
                    "_" + ABCDversion + "_ST_tchanXSDown",
                    "_" + ABCDversion + "_ST_schanXSUp",
                    "_" + ABCDversion + "_ST_schanXSDown",                      
                    
                    
                    "_" + ABCDversion + "_MCSF_powheg_renfac_envUp",
                    "_" + ABCDversion + "_MCSF_powheg_renfac_envDown",
                    "_" + ABCDversion + "_MCSF_powheg_renfacUp",
                    "_" + ABCDversion + "_MCSF_powheg_renfacDown",
                    "_" + ABCDversion + "_MCSF_powheg_renUp",
                    "_" + ABCDversion + "_MCSF_powheg_renDown",
                    "_" + ABCDversion + "_MCSF_powheg_facUp",
                    "_" + ABCDversion + "_MCSF_powheg_facDown",

                    
                    "_" + ABCDversion + "_MCSF_amc_renfac_envUp",
                    "_" + ABCDversion + "_MCSF_amc_renfac_envDown",
                    "_" + ABCDversion + "_MCSF_amc_renfacUp",
                    "_" + ABCDversion + "_MCSF_amc_renfacDown",
                    "_" + ABCDversion + "_MCSF_amc_renUp",
                    "_" + ABCDversion + "_MCSF_amc_renDown",
                    "_" + ABCDversion + "_MCSF_amc_facUp",
                    "_" + ABCDversion + "_MCSF_amc_facDown",
                    
                    "_" + ABCDversion + "_MCSF_JetMassScaleUp",
                    "_" + ABCDversion + "_MCSF_JetMassScaleDown",
                    "_" + ABCDversion + "_MCSF_JetMassResUp",
                    "_" + ABCDversion + "_MCSF_JetMassResDown",
                    
                    

    ]
          
murmufGstars=[#muR20muF20,muR05muF05,muR20muF10,muR05muF10,muR10muF20,muR10muF05
[0.902298845069,1.07357151428,0.793411397192,1.12920371887,0.844779183017,1.06331345473],    #1500
[0.913541564396,1.07114310217,0.788859891827,1.11569334394,0.847201881135,1.06331345473],    #1750
[0.923842764153,1.06855988154,0.785227925426,1.10349024658,0.849681375230,1.08020214758],    #2000
[0.933137438387,1.06592639902,0.781691305888,1.09273276844,0.851738871894,1.08020214758],    #2250
[0.941522478977,1.06328174834,0.777840522115,1.08333081305,0.853184006575,1.09440158723],    #2500  
[0.949449385820,1.06058432115,0.774780218314,1.07448235922,0.854855062329,1.09440158723],    #2750  
[0.956902394754,1.05792270536,0.770967744269,1.06648128262,0.855854021111,1.09440158723],    #3000  
[0.970622717239,1.05270948818,0.764547328234,1.05195774915,0.857959613747,1.09440158723],    #3500  
[0.982975177373,1.04780254477,0.758514448366,1.03929120896,0.859612665386,1.09440158723],    #4000  
]

murmufs=[#muR20muF20,muR05muF05,muR20muF10,muR05muF10,muR10muF20,muR10muF05
[0.943018825183,1.06342163233,0.999902678539,1.00011266322,0.943106166118,1.06331345473],    #1500
[0.929516248064,1.08024932978,0.999949012411,1.00005880273,0.929561359871,1.08020214758],    #2000
[0.918381534597,1.09442296069,0.999970237242,1.00003393267,0.918407254497,1.09440158723],    #2500  
]

PDFs=[
[1.0,1.0,1.0], #1500
[1.0,1.0,1.0], #2000
[1.0,1.0,1.0], #2500
]


PDFsGstar=[
[], #1500
[], #2000
[], #2500
]

systweightnamesMCSFs=[
                    #"CSV_nominal:=(1)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systUp:=(1*(1+1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systDown:=(1*(1-1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "nom:=1.0",
                    
                    "" + ABCDversion + "_nominal:=(MCSF_Weight_" + ABCDversion + "*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    
                    
                    "" + ABCDversion + "_MCSF_CSVLFUp:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFUp*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFDown:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFDown*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFUp:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFUp*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFDown:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFDown*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats1Up*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats1Down*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats1Up*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats1Down*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats2Up*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats2Down*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats2Up*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats2Down*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr1Up*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr1Down*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr2Up*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr2Down*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    "" + ABCDversion + "_MCSF_toptagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightUp*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_toptagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightDown*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_topmisstagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_topmisstagweightnominal*" + ABCDversion + "_topmisstagweightUp*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_topmisstagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_topmisstagweightnominal*" + ABCDversion + "_topmisstagweightDown*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                                        
                    "" + ABCDversion + "_MCSF_WtagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_weightnominal*" + ABCDversion + "_Wtag_weightUp*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_WtagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_weightnominal*" + ABCDversion + "_Wtag_weightDown*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",     
                    #"" + ABCDversion + "_MCSF_Wtag_tag_t21anti_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_tag_t21anti_weightnominal*" + ABCDversion + "_Wtag_tag_t21anti_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_tag_t21anti_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_tag_t21anti_weightnominal*" + ABCDversion + "_Wtag_tag_t21anti_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21_weightnominal*" + ABCDversion + "_Wtag_mistag_t21_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21_weightnominal*" + ABCDversion + "_Wtag_mistag_t21_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21anti_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21anti_weightnominal*" + ABCDversion + "_Wtag_mistag_t21anti_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21anti_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21anti_weightnominal*" + ABCDversion + "_Wtag_mistag_t21anti_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
 
                    
                    "" + ABCDversion + "_MCSF_PUUp:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Up*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_PUDown:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Down*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "" + ABCDversion + "_MCSF_PDFUp:=(MCSF_Weight_" + ABCDversion + "/Weight_LHA_NNPDF30_nlo_as_0118_nominal*Weight_LHA_NNPDF30_nlo_as_0118_up*((murmuf1500==1)/"+str(PDFs[0][2])+"+(murmuf2000==1)/"+str(PDFs[1][2])+"+(murmuf2500==1)/"+str(PDFs[2][2])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_PDFDown:=(MCSF_Weight_" + ABCDversion + "/Weight_LHA_NNPDF30_nlo_as_0118_nominal*Weight_LHA_NNPDF30_nlo_as_0118_down*((murmuf1500==1)/"+str(PDFs[0][0])+"+(murmuf2000==1)/"+str(PDFs[1][0])+"+(murmuf2500==1)/"+str(PDFs[2][0])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                                        
                    "" + ABCDversion + "_MCSF_LumiUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.025)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_LumiDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.025)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    "" + ABCDversion + "_MCSF_TriggerUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.016)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_TriggerDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.016)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 

                    "" + ABCDversion + "_ttbarXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.05)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_ttbarXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.05)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    
                    "" + ABCDversion + "_ST_tWXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.053)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights_ST_tW==1)+(DoWeights*DoMCDataWeights_ST_tW==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_ST_tWXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.053)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights_ST_tW==1)+(DoWeights*DoMCDataWeights_ST_tW==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",   
                    "" + ABCDversion + "_ST_tchanXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.042)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights_ST_t==1)+(DoWeights*DoMCDataWeights_ST_t==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_ST_tchanXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.036)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights_ST_t==1)+(DoWeights*DoMCDataWeights_ST_t==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",                    
                    "" + ABCDversion + "_ST_schanXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.037)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights_ST_s==1)+(DoWeights*DoMCDataWeights_ST_s==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_ST_schanXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.047)*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights_ST_s==1)+(DoWeights*DoMCDataWeights_ST_s==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",                         
                    
                    #"" + ABCDversion + "_MCSF_renfacUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF2p0"+"*("+str(1.29465480107)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ST_tW==1+DoMCDataWeights_ST_t==1+DoMCDataWeights_ST_s)*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][0])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][0])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][0])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][0])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][0])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][0])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][0])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][0])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][0])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_renfacDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF0p5"+"*("+str(0.755423761535)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ST_tW==1+DoMCDataWeights_ST_t==1+DoMCDataWeights_ST_s)*(DoMCDataWeights_ttbaronly==0)(murmufGstar1500==1)/"+str(murmufGstars[0][1])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][1])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][1])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][1])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][1])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][1])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_renUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF1p0"+"*("+str(1.12267866063)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ST_tW==1+DoMCDataWeights_ST_t==1+DoMCDataWeights_ST_s)*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][2])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][2])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][2])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][2])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][2])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][2])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][2])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][2])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][2])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_renDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF1p0"+"*("+str(0.814903279727)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ST_tW==1+DoMCDataWeights_ST_t==1+DoMCDataWeights_ST_s)*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][3])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][3])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][3])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][3])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][3])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][3])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][3])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][3])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][3])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_facUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF2p0"+"*("+str(1.07529312329)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ST_tW==1+DoMCDataWeights_ST_t==1+DoMCDataWeights_ST_s)*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][4])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][4])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][4])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][4])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][4])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][4])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][4])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][4])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][4])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_facDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF0p5"+"*("+str(0.926990626083)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ST_tW==1+DoMCDataWeights_ST_t==1+DoMCDataWeights_ST_s)*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][5])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][5])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][5])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][5])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][5])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][5])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][5])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][5])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][5])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "" + ABCDversion + "_MCSF_powheg_renfac_envUp:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeUp*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_renfac_envDown:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeDown*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_renfacUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF2p0"+"*((murmuf1500==1)/"+str(murmufs[0][0])+"+(murmuf2000==1)/"+str(murmufs[1][0])+"+(murmuf2500==1)/"+str(murmufs[2][0])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_renfacDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF0p5"+"*((murmuf1500==1)/"+str(murmufs[0][1])+"+(murmuf2000==1)/"+str(murmufs[1][1])+"+(murmuf2500==1)/"+str(murmufs[2][1])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_renUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF1p0"+"*((murmuf1500==1)/"+str(murmufs[0][2])+"+(murmuf2000==1)/"+str(murmufs[1][2])+"+(murmuf2500==1)/"+str(murmufs[2][2])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_renDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF1p0"+"*((murmuf1500==1)/"+str(murmufs[0][3])+"+(murmuf2000==1)/"+str(murmufs[1][3])+"+(murmuf2500==1)/"+str(murmufs[2][3])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_facUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF2p0"+"*((murmuf1500==1)/"+str(murmufs[0][4])+"+(murmuf2000==1)/"+str(murmufs[1][4])+"+(murmuf2500==1)/"+str(murmufs[2][4])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_facDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF0p5"+"*((murmuf1500==1)/"+str(murmufs[0][5])+"+(murmuf2000==1)/"+str(murmufs[1][5])+"+(murmuf2500==1)/"+str(murmufs[2][5])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "" + ABCDversion + "_MCSF_amc_renfac_envUp:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeUp*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_renfac_envDown:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeDown*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_renfacUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF2p0"+"*((murmuf1500==1)/"+str(murmufs[0][0])+"+(murmuf2000==1)/"+str(murmufs[1][0])+"+(murmuf2500==1)/"+str(murmufs[2][0])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_renfacDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF0p5"+"*((murmuf1500==1)/"+str(murmufs[0][1])+"+(murmuf2000==1)/"+str(murmufs[1][1])+"+(murmuf2500==1)/"+str(murmufs[2][1])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_renUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF1p0"+"*((murmuf1500==1)/"+str(murmufs[0][2])+"+(murmuf2000==1)/"+str(murmufs[1][2])+"+(murmuf2500==1)/"+str(murmufs[2][2])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_renDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF1p0"+"*((murmuf1500==1)/"+str(murmufs[0][3])+"+(murmuf2000==1)/"+str(murmufs[1][3])+"+(murmuf2500==1)/"+str(murmufs[2][3])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_facUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF2p0"+"*((murmuf1500==1)/"+str(murmufs[0][4])+"+(murmuf2000==1)/"+str(murmufs[1][4])+"+(murmuf2500==1)/"+str(murmufs[2][4])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_facDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF0p5"+"*((murmuf1500==1)/"+str(murmufs[0][5])+"+(murmuf2000==1)/"+str(murmufs[1][5])+"+(murmuf2500==1)/"+str(murmufs[2][5])+")*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                                        
                    "" + ABCDversion + "_MCSF_JetMassScaleUp:=(MCSF_Weight_" + ABCDversion + "_JetMassScaleUp"+"*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    "" + ABCDversion + "_MCSF_JetMassScaleDown:=(MCSF_Weight_" + ABCDversion + "_JetMassScaleDown"+"*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    "" + ABCDversion + "_MCSF_JetMassResUp:=(MCSF_Weight_" + ABCDversion + "_JetMassResUp"+"*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    "" + ABCDversion + "_MCSF_JetMassResDown:=(MCSF_Weight_" + ABCDversion + "_JetMassResDown"+"*((murmuf1500==1)/"+str(PDFs[0][1])+"+(murmuf2000==1)/"+str(PDFs[1][1])+"+(murmuf2500==1)/"+str(PDFs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 

    ]
    

assert len(weigthsystnamesMCSFs)==len(systweightnamesMCSFs)


otherSystNames=[
    "_JERUp","_JERDown",
    "_JESUp","_JESDown",



]

otherSystFileNames=[
    "JERup","JERdown",
    "JESup","JESdown",
]

JECsystnames=[
    "_" + ABCDversion + "_nominal_JERUp","_" + ABCDversion + "_nominal_JERDown",
    "_" + ABCDversion + "_nominal_JESUp","_" + ABCDversion + "_nominal_JESDown",

]

assert len(otherSystNames)==len(JECsystnames)

#allweightsystnames=weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM+weightsystnamesPythia8bantiZprimeM+weightsystnamesMadgraphtantiTopPt+weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffMadgraphbantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM+weightsystnamesGeneratorDiffMadgraphtantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt+weightsystnamesMadgraphbantiZprimeMWithtopbtag+weightsystnamesPythia8bantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag+weightsystnamesMadgraphtantiTopPtWithtopbtag+weightsystnamesPythia8tantiTopPtWithtopbtag+weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag+weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag+weightsystnamesABCD+weigthsystnamesMCSFs
##allweightsystnames=weightsystnamesABCD

#allsystweights=systweightsbasic+systweightsMadgraphbantiZprimeM+systweightsPythia8bantiZprimeM+systweightsMadgraphtantiTopPt+systweightsPythia8tantiTopPt+systweightsGeneartorDiffMadgraphbantiZprimeM+systweightsGeneartorDiffPythia8bantiZprimeM+systweightsGeneartorDiffMadgraphtantiTopPt+systweightsGeneartorDiffPythia8tantiTopPt+systweightsMadgraphbantiZprimeMWithtopbtag+systweightsPythia8bantiZprimeMWithtopbtag+systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag+systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag+systweightsMadgraphtantiTopPtWithtopbtag+systweightsPythia8tantiTopPtWithtopbtag+systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag+systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag+systweightsABCD+systweightnamesMCSFs
##allsystweights=systweightsABCD

#ABweightsystnames=weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM+weightsystnamesPythia8bantiZprimeM+weightsystnamesMadgraphtantiTopPt+weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffMadgraphbantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM+weightsystnamesGeneratorDiffMadgraphtantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt+weightsystnamesMadgraphbantiZprimeMWithtopbtag+weightsystnamesPythia8bantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag+weightsystnamesMadgraphtantiTopPtWithtopbtag+weightsystnamesPythia8tantiTopPtWithtopbtag+weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag+weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag+weigthsystnamesMCSFs

#ABsystweights=systweightsbasic+systweightsMadgraphbantiZprimeM+systweightsPythia8bantiZprimeM+systweightsMadgraphtantiTopPt+systweightsPythia8tantiTopPt+systweightsGeneartorDiffMadgraphbantiZprimeM+systweightsGeneartorDiffPythia8bantiZprimeM+systweightsGeneartorDiffMadgraphtantiTopPt+systweightsGeneartorDiffPythia8tantiTopPt+systweightsMadgraphbantiZprimeMWithtopbtag+systweightsPythia8bantiZprimeMWithtopbtag+systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag+systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag+systweightsMadgraphtantiTopPtWithtopbtag+systweightsPythia8tantiTopPtWithtopbtag+systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag+systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag+systweightnamesMCSFs
     
#allweightsystnames=weigthsystnamesMCSFs+weightsystnamesABCD+JECsystnames
allweightsystnames=weigthsystnamesMCSFs+weightsystnamesABCD

allsystweights=systweightnamesMCSFs+systweightsABCD

# names of the systematics (proper names needed e.g. for combination)
mcweight='35.9'

ttbarXS_MCgen='730.0'
ttbarXS_NLO='831.76' 
rateunc_ttbarXS_Up=math.sqrt(19.77*19.77 + 35.06*35.06)
rateunc_ttbarXS_Down=math.sqrt(29.20*29.20 + 35.06*35.06)

doBR=True

if doBR:
    BR_name="BR00_50_50"

if BR_name is "BR05_025_025":
    BR=[0.5,0.25,0.25]
if BR_name is "BR00_50_50":
    BR=[0.0,0.5,0.5]



sfs="Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"
usualweights="(1*Weight_PU*((Weight>0)-(Weight<0)))*Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"


# samples
# input path 
path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"
path="/pnfs/desy.de/cms/tier2/store/user/skudella/*/MC_limits_*/*/*/*"

#path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_old/"

#DATA_MC_rate_scalefactor_QCD='0.506626268137'
#DATA_MC_rate_scalefactor_QCD='0.681942750822'
DATA_MC_rate_scalefactor_QCD='0.761444753045'


SignalSamples=[

                    #Sample('Z->tWb, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->Wb',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/95.06*232956.0/232893.0','SigRho1500700_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->Wb',ROOT.kMagenta-7,'/pnfs/desy.de/cms/tier2/store/user/skudella/ZprimeToTprimeT_TprimeToWB_Zp1500Nar_Tp1000Nar_LH_TuneCUETP8M2T4_13TeV-madgraph-pythia8_V2/MC_limits_ZprimeToTprimeT_TprimeToWB_Zp1500Nar_Tp1000Nar_LH/180725_094945/0000/ZprimeToTprimeT_TprimeToWB_Zp1500Nar_Tp1000Nar_LH_nominal_Tree_2.root',mcweight+'/95.06*232956.0/232893.0','SigRho1500700_tWb',allweightsystnames),
                    #Sample('Z->tWb, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->Wb',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/138.07*233247.0/233185.0','SigRho1500900_tWb',allweightsystnames),
                    #Sample('Z->tWb, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->Wb',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/99.03*232087.0/197288.0','SigRho15001200_tWb',allweightsystnames),
                    #Sample('Z->tWb, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->Wb',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/55.83*229339.0/230269.0','SigRho2000900_tWb',allweightsystnames),
                    #Sample('Z->tWb, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1200, T\'->Wb',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/86.28*197385.0/197288.0','SigRho20001200_tWb',allweightsystnames),
                    #Sample('Z->tWb, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->Wb',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/83.47*229497.0/229372.0','SigRho20001500_tWb',allweightsystnames),
                    #Sample('Z->tWb, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->Wb',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/37.6*226697.0/223936.0','SigRho25001200_tWb',allweightsystnames), 
                    #Sample('Z->tWb, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->Wb',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/53.9*227926.0/225306.0','SigRho25001500_tWb',allweightsystnames),

                    
                    #Sample('Z->ttZ, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->tZ',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToZT*1500*700*nominal*Tree.root',mcweight+'/186.7*197390.0/197390.0','SigRho1500700_ttZ',allweightsystnames),
                    #Sample('Z->ttZ, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->tZ',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToZT*1500*900*nominal*Tree.root',mcweight+'/320.4*205947.0/205919.0','SigRho1500900_ttZ',allweightsystnames),
                    #Sample('Z->ttZ, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->tZ',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToZT*1500*1200*nominal*Tree.root',mcweight+'/285.1*201839.0/201808.0','SigRho15001200_ttZ',allweightsystnames),
                    #Sample('Z->ttZ, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->tZ',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToZT*2000*900*nominal*Tree.root',mcweight+'/114.7*206508.0/206453.0','SigRho2000900_ttZ',allweightsystnames),
                    #Sample('Z->ttZ, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1200, T\'->tZ',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1200*LH*nominal*Tree.root',mcweight+'/205.6*205497.0/205436.0','SigRho20001200_ttZ',allweightsystnames),
                    #Sample('Z->ttZ, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->tZ',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1500*nominal*Tree.root',mcweight+'/214.1*203441.0/203382.0','SigRho20001500_ttZ',allweightsystnames),
                    #Sample('Z->ttZ, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->tZ',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1200*nominal*Tree.root',mcweight+'/83.5*206568.0/206497.0','SigRho25001200_ttZ',allweightsystnames), 
                    #Sample('Z->ttZ, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->tZ',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1500*nominal*Tree.root',mcweight+'/124.2*206117.0/206035.0','SigRho25001500_ttZ',allweightsystnames),

                    
                    #Sample('Z->ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->tH',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToHT*1500*700*nominal*Tree.root',mcweight+'/3.62*207419.0/207388.0','SigRho1500700_ttH',allweightsystnames),
                    #Sample('Z->ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->tH',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToHT*1500*900*nominal*Tree.root',mcweight+'/3.571*205787.0/205759.0','SigRho1500900_ttH',allweightsystnames),
                    #Sample('Z->ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->tH',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToHT*1500*1200*nominal*Tree.root',mcweight+'/1.731*203617.0/203575.0','SigRho15001200_ttH',allweightsystnames),
                    #Sample('Z->ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->tH',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToHT*2000*900*nominal*Tree.root',mcweight+'/1.305*204023.0/207827.0','SigRho2000900_ttH',allweightsystnames),
                    #Sample('Z->ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1200, T\'->tH',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1200*LH*nominal*Tree.root',mcweight+'/1.251*196615.0/206563.0','SigRho20001200_ttH',allweightsystnames),
                    #Sample('Z->ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->tH',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1500*nominal*Tree.root',mcweight+'/0.8246*209543.0/196143.0','SigRho20001500_ttH',allweightsystnames),
                    #Sample('Z->ttH, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->tH',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1200*nominal*Tree.root',mcweight+'/0.511*207688.0/207581.0','SigRho25001200_ttH',allweightsystnames), 
                    #Sample('Z->ttH, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->tH',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1500*nominal*Tree.root',mcweight+'/0.4775*207043.0/206938.0','SigRho25001500_ttH',allweightsystnames),
                    





                    
                    #Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/10000000','SigRho1500700_'+BR_name+'',allweightsystnames),
                    #Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/10000000','SigRho1500900_'+BR_name+'',allweightsystnames),
                    #Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/10000000','SigRho15001200_'+BR_name+'',allweightsystnames),
                    #Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/10000000','SigRho2000900_'+BR_name+'',allweightsystnames),
                    #Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1200, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/10000000','SigRho20001200_'+BR_name+'',allweightsystnames),
                    #Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/10000000','SigRho20001500_'+BR_name+'',allweightsystnames),
                    #Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/10000000','SigRho25001200_'+BR_name+'',allweightsystnames), 
                    #Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/10000000','SigRho25001500_'+BR_name+'',allweightsystnames),





]
    
    



#expectedSignals=[8.6,0.27,0.33,0.8,1.5,0.21,0.9,0.29]+[3.1,0.29,0.18,3.1,2.4,0.4,0.33,0.13]+[11,0.54,0.26,3.5,2.6,0.56,0.59,0.22]+[8.6,0.27,0.33,0.8,1.5,0.21,0.9,0.29]


#samplenames=[]
#for i in samples:
    #samplenames.append(i.nick)
SignalSampleNames=[]
for i in SignalSamples:
    SignalSampleNames.append(i.nick)
#BackgroundSampleNames=[]
#for i in BackgroundSamples:
    #BackgroundSampleNames.append(i.nick)
#DataSampleNames=[]
#for i in DataSamples:
    #DataSampleNames.append(i.nick)
  
samples=SignalSamples

samplenames=SignalSampleNames




systsamples=[]
for sample,samplename in zip(samples,samplenames):
 if (( 'QCDMadgraph' not in samplename ) and ( 'QCDPythia8' not in samplename ) and ( 'BKG' not in samplename ) and ( 'DATA' not in samplename ) ):   
  for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    thisnewsel=sample.selection
    print sample.nick
    print sample.name
    print sample.path.replace("nominal",sysfilename)
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
    #DataSampleNames.append(sample.nick+sysname)
    print 'with JEC ', sample.path

 else:
  for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    thisnewsel=sample.selection
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path,thisnewsel,sample.nick+sysname))
    #DataSampleNames.append(sample.nick+sysname)  
    print 'no JEC ', sample.path


