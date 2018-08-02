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
                    "_" + ABCDversion + "_MCSF_renfac_envUp",
                    "_" + ABCDversion + "_MCSF_renfac_envDown",
                    "_" + ABCDversion + "_ttbarXSUp",
                    "_" + ABCDversion + "_ttbarXSDown",
                    
                    "_" + ABCDversion + "_MCSF_renfacUp",
                    "_" + ABCDversion + "_MCSF_renfacDown",
                    "_" + ABCDversion + "_MCSF_renUp",
                    "_" + ABCDversion + "_MCSF_renDown",
                    "_" + ABCDversion + "_MCSF_facUp",
                    "_" + ABCDversion + "_MCSF_facDown",

    ]
        
murmufttbar=[
1.14398309396,0.880338673747,1.11578278373,0.897477695732,1.01990637208,0.975146721204
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

systweightnamesMCSFs=[
                    #"CSV_nominal:=(1)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systUp:=(1*(1+1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systDown:=(1*(1-1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "nom:=1.0",
                    
                    "" + ABCDversion + "_nominal:=(MCSF_Weight_" + ABCDversion + ")*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    
                    
                    
                    "" + ABCDversion + "_MCSF_CSVLFUp:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVLFDown:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVHFUp:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVHFDown:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVHFStats1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVHFStats1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVLFStats1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVLFStats1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVHFStats2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVHFStats2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVLFStats2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVLFStats2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVCErr1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVCErr1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVCErr2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_CSVCErr2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_toptagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_toptagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_topmisstagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_topmisstagweightnominal*" + ABCDversion + "_topmisstagweightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_topmisstagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_topmisstagweightnominal*" + ABCDversion + "_topmisstagweightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                                        
                    "" + ABCDversion + "_MCSF_WtagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_weightnominal*" + ABCDversion + "_Wtag_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_WtagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_weightnominal*" + ABCDversion + "_Wtag_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",     
                    #"" + ABCDversion + "_MCSF_Wtag_tag_t21anti_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_tag_t21anti_weightnominal*" + ABCDversion + "_Wtag_tag_t21anti_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_tag_t21anti_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_tag_t21anti_weightnominal*" + ABCDversion + "_Wtag_tag_t21anti_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21_weightnominal*" + ABCDversion + "_Wtag_mistag_t21_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21_weightnominal*" + ABCDversion + "_Wtag_mistag_t21_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21anti_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21anti_weightnominal*" + ABCDversion + "_Wtag_mistag_t21anti_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21anti_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21anti_weightnominal*" + ABCDversion + "_Wtag_mistag_t21anti_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
 
                    
                    "" + ABCDversion + "_MCSF_PUUp:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_PUDown:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered", 
                    "" + ABCDversion + "_MCSF_PDFUp:=(MCSF_Weight_" + ABCDversion + "/PDF_RMSMean*PDF_RMSUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_PDFDown:=(MCSF_Weight_" + ABCDversion + "/PDF_RMSMean*PDF_RMSDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                                        
                    "" + ABCDversion + "_MCSF_LumiUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.025))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_LumiDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.025))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered", 
                    "" + ABCDversion + "_MCSF_TriggerUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.016))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_TriggerDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.016))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered", 
                    
                    "" + ABCDversion + "_MCSF_renfac_envUp:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_renfac_envDown:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_ttbarXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_ttbarXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",
                    
                    
                    #"" + ABCDversion + "_MCSF_renfacUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF2p0"+"*("+str(murmufttbar[0])+"*(DoMCDataWeights_ttbaronly==1)+1.0*((DoMCDataWeights_ST_tW==1)+(DoMCDataWeights_ST_t==1)+(DoMCDataWeights_ST_s==1))*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][0])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][0])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][0])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][0])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][0])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][0])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][0])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][0])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][0])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_renfacDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF0p5"+"*("+str(murmufttbar[1])+"*(DoMCDataWeights_ttbaronly==1)+1.0*((DoMCDataWeights_ST_tW==1)+(DoMCDataWeights_ST_t==1)+(DoMCDataWeights_ST_s==1))*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][1])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][1])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][1])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][1])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][1])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][1])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_renUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF1p0"+"*("+str(murmufttbar[2])+"*(DoMCDataWeights_ttbaronly==1)+1.0*((DoMCDataWeights_ST_tW==1)+(DoMCDataWeights_ST_t==1)+(DoMCDataWeights_ST_s==1))*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][2])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][2])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][2])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][2])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][2])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][2])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][2])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][2])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][2])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_renDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF1p0"+"*("+str(murmufttbar[3])+"*(DoMCDataWeights_ttbaronly==1)+1.0*((DoMCDataWeights_ST_tW==1)+(DoMCDataWeights_ST_t==1)+(DoMCDataWeights_ST_s==1))*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][3])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][3])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][3])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][3])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][3])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][3])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][3])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][3])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][3])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_facUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF2p0"+"*("+str(murmufttbar[4])+"*(DoMCDataWeights_ttbaronly==1)+1.0*((DoMCDataWeights_ST_tW==1)+(DoMCDataWeights_ST_t==1)+(DoMCDataWeights_ST_s==1))*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][4])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][4])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][4])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][4])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][4])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][4])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][4])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][4])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][4])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_facDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF0p5"+"*("+str(murmufttbar[5])+"*(DoMCDataWeights_ttbaronly==1)+1.0*((DoMCDataWeights_ST_tW==1)+(DoMCDataWeights_ST_t==1)+(DoMCDataWeights_ST_s==1))*(DoMCDataWeights_ttbaronly==0)+(murmufGstar1500==1)/"+str(murmufGstars[0][5])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][5])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][5])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][5])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][5])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][5])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][5])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][5])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][5])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered", 
                    
                    "" + ABCDversion + "_MCSF_renfacUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF2p0"+"*("+str(murmufttbar[0])+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_renfacDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF0p5"+"*("+str(murmufttbar[1])+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_renUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF1p0"+"*("+str(murmufttbar[2])+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_renDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF1p0"+"*("+str(murmufttbar[3])+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_facUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF2p0"+"*("+str(murmufttbar[4])+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_MCSF_facDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF0p5"+"*("+str(murmufttbar[5])+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*triggered",                     

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
    BR_name="BR05_025_025"

if BR_name is "BR05_025_025":
    BR=[0.5,0.25,0.25]



sfs="Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"
usualweights="(1*Weight_PU*((Weight>0)-(Weight<0)))*Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"


# samples
# input path 
path_80x_MC="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"
path_80x_DATA="/nfs/dust/cms/user/skudella/processed_DATA/flat_trees/"


#DATA_MC_rate_scalefactor_QCD='0.506626268137'
#DATA_MC_rate_scalefactor_QCD='0.681942750822'
DATA_MC_rate_scalefactor_QCD='0.761444753045'


BackgroundSamples=[
                    Sample('Top background',ROOT.kBlue-4,path_80x_MC+'BKG_TTbar/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',allweightsystnames) ,
                    #Sample('Top background',ROOT.kBlue-4,path_80x_MC+'BKG_TTbar/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',allweightsystnames) ,
                    Sample('single top (tW-channel)',ROOT.kBlue+2,path_80x_MC+'BKG_ST/*ST*tW*nominal*.root',mcweight,'ST_tW',allweightsystnames) ,
                    Sample('single top (t-channel)',ROOT.kBlue-9,path_80x_MC+'BKG_ST/*ST*t-channel*nominal*.root',mcweight,'ST_t',allweightsystnames) ,
                    Sample('single top (s-channel)',ROOT.kBlue-7,path_80x_MC+'BKG_ST/*ST*s-channel*nominal*.root',mcweight,'ST_s',allweightsystnames) ,
                    #Sample('QCD from MC',ROOT.kOrange-3,path_80x_MC+'BKG_QCD/*QCD_H*nominal*Tree*.root',mcweight,'QCDMadgraph',allweightsystnames),
]


DataSamples=[
                    Sample('data',ROOT.kBlack,path_80x_DATA+'*nominal*.root','1.0','DATA_2016'),
]




#samplenames=[]
#for i in samples:
    #samplenames.append(i.nick)
#SignalSampleNames=[]
#for i in SignalSamples:
    #SignalSampleNames.append(i.nick)
BackgroundSampleNames=[]
for i in BackgroundSamples:
    BackgroundSampleNames.append(i.nick)
DataSampleNames=[]
for i in DataSamples:
    DataSampleNames.append(i.nick)
  
samples=BackgroundSamples+DataSamples

samplenames=BackgroundSampleNames+DataSampleNames




systsamples=[]
for sample,samplename in zip(samples,samplenames):
 if (( 'QCDMadgraph' not in samplename ) and ( 'QCDPythia8' not in samplename ) and ( 'BKG' not in samplename ) and ( 'DATA' not in samplename ) ):   
  for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    thisnewsel=sample.selection
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
    #DataSampleNames.append(sample.nick+sysname)
    print 'with JEC ', sample.path

 else:
  for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    thisnewsel=sample.selection
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path,thisnewsel,sample.nick+sysname))
    #DataSampleNames.append(sample.nick+sysname)  
    print 'no JEC ', sample.path


