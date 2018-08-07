import sys
import os
from scriptgenerator import *
from plotutils import *
from plot_cuts_ZPrime_MC import *

    
weightsystnamesMadgraphbantiZprimeM=[
                    #"",
                    "_ABMadgraphbantiZprimeM_nominal",
                    "_ABMadgraphbantiZprimeM_systUp",
                    "_ABMadgraphbantiZprimeM_systDown",
] 

systweightsMadgraphbantiZprimeM=[
                    #"nom:=1",
                    #"ABMadgraphbantiZprimeM_nominal:=2",
                    "ABMadgraphbantiZprimeM_nominal:=QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    ##"ABMadgraphbantiZprimeM_nominal:=2*(DoWeights==1)+(DoWeights==0)*1.0",
                    "ABMadgraphbantiZprimeM_systUp:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABMadgraphbantiZprimeM_systDown:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]


weightsystnamesPythia8bantiZprimeM=[
                    "_ABPythiabantiZprimeM_nominal",
                    "_ABPythiabantiZprimeM_systUp",
                    "_ABPythiabantiZprimeM_systDown",
] 

systweightsPythia8bantiZprimeM=[
                    "ABPythiabantiZprimeM_nominal:=QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiabantiZprimeM_systUp:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiabantiZprimeM_systDown:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]
 
weightsystnamesGeneratorDiffMadgraphbantiZprimeM=[
                    "_ABMadgraphbantiZprimeMGeneratorDiff_systUp",
                    "_ABMadgraphbantiZprimeMGeneratorDiff_systDown",
]

systweightsGeneartorDiffMadgraphbantiZprimeM=[
                    "ABMadgraphbantiZprimeMGeneratorDiff_systUp:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABMadgraphbantiZprimeMGeneratorDiff_systDown:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]
 
weightsystnamesGeneratorDiffPythia8bantiZprimeM=[
                    "_ABPythiabantiZprimeMGeneratorDiff_systUp",
                    "_ABPythiabantiZprimeMGeneratorDiff_systDown",
]

systweightsGeneartorDiffPythia8bantiZprimeM=[
                    "ABPythiabantiZprimeMGeneratorDiff_systUp:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiabantiZprimeMGeneratorDiff_systDown:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]
    
 
weightsystnamesMadgraphtantiTopPt=[
                    "_ABMadgraphtantiTopPt_nominal",
                    "_ABMadgraphtantiTopPt_systUp",
                    "_ABMadgraphtantiTopPt_systDown",
] 

systweightsMadgraphtantiTopPt=[
                    "ABMadgraphtantiTopPt_nominal:=QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABMadgraphtantiTopPt_systUp:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt+QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABMadgraphtantiTopPt_systDown:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]


weightsystnamesPythia8tantiTopPt=[
                    "_ABPythiatantiTopPt_nominal",
                    "_ABPythiatantiTopPt_systUp",
                    "_ABPythiatantiTopPt_systDown",
] 

systweightsPythia8tantiTopPt=[
                    "ABPythiatantiTopPt_nominal:=QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiatantiTopPt_systUp:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt + QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiatantiTopPt_systDown:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt - QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]

weightsystnamesGeneratorDiffMadgraphtantiTopPt=[
                    "_ABMadgraphtantiTopPtGeneratorDiff_systUp",
                    "_ABMadgraphtantiTopPtGeneratorDiff_systDown",
]

systweightsGeneartorDiffMadgraphtantiTopPt=[
                    "ABMadgraphtantiTopPtGeneratorDiff_systUp:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt + abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABMadgraphtantiTopPtGeneratorDiff_systDown:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt - abs( QCDPythia8_SF_SB_top_ati_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]
 
weightsystnamesGeneratorDiffPythia8tantiTopPt=[
                    "_ABPythiatantiTopPtGeneratorDiff_systUp",
                    "_ABPythiatantiTopPtGeneratorDiff_systDown",
]

systweightsGeneartorDiffPythia8tantiTopPt=[
                    "ABPythiatantiTopPtGeneratorDiff_systUp:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt+ abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiatantiTopPtGeneratorDiff_systDown:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt- abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]




#########################################################################
  
    
weightsystnamesMadgraphbantiZprimeMWithtopbtag=[
                    "_ABMadgraphbantiZprimeMWithtopbtag_nominal",
                    "_ABMadgraphbantiZprimeMWithtopbtag_systUp",
                    "_ABMadgraphbantiZprimeMWithtopbtag_systDown",
] 
systweightsMadgraphbantiZprimeMWithtopbtag=[
                    #"ABMadgraphbantiZprimeMWithtopbtag_nominal:=2",
                    "ABMadgraphbantiZprimeMWithtopbtag_nominal:=QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    ##"ABMadgraphbantiZprimeMWithtopbtag_nominal:=2*(DoWeights==1)+(DoWeights==0)*1.0",
                    "ABMadgraphbantiZprimeMWithtopbtag_systUp:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABMadgraphbantiZprimeMWithtopbtag_systDown:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]


weightsystnamesPythia8bantiZprimeMWithtopbtag=[
                    "_ABPythiabantiZprimeMWithtopbtag_nominal",
                    "_ABPythiabantiZprimeMWithtopbtag_systUp",
                    "_ABPythiabantiZprimeMWithtopbtag_systDown",
] 
systweightsPythia8bantiZprimeMWithtopbtag=[
                    "ABPythiabantiZprimeMWithtopbtag_nominal:=QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiabantiZprimeMWithtopbtag_systUp:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiabantiZprimeMWithtopbtag_systDown:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]
 
weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag=[
                    "_ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systUp",
                    "_ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systDown",
]

systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag=[
                    "ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systUp:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systDown:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]
 
weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag=[
                    "_ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systUp",
                    "_ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systDown",
]

systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag=[
                    "ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systUp:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systDown:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]
    
 
weightsystnamesMadgraphtantiTopPtWithtopbtag=[
                    "_ABMadgraphtantiTopPtWithtopbtag_nominal",
                    "_ABMadgraphtantiTopPtWithtopbtag_systUp",
                    "_ABMadgraphtantiTopPtWithtopbtag_systDown",
] 

systweightsMadgraphtantiTopPtWithtopbtag=[
                    "ABMadgraphtantiTopPtWithtopbtag_nominal:=QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABMadgraphtantiTopPtWithtopbtag_systUp:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt+QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABMadgraphtantiTopPtWithtopbtag_systDown:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]


weightsystnamesPythia8tantiTopPtWithtopbtag=[
                    "_ABPythiatantiTopPtWithtopbtag_nominal",
                    "_ABPythiatantiTopPtWithtopbtag_systUp",
                    "_ABPythiatantiTopPtWithtopbtag_systDown",
] 

systweightsPythia8tantiTopPtWithtopbtag=[
                    "ABPythiatantiTopPtWithtopbtag_nominal:=QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiatantiTopPtWithtopbtag_systUp:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt + QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiatantiTopPtWithtopbtag_systDown:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt - QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]

weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag=[
                    "_ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systUp",
                    "_ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systDown",
]

systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag=[
                    "ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systUp:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt + abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systDown:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt - abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]
 
weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag=[
                    "_ABPythiatantiTopPtWithtopbtagGeneratorDiff_systUp",
                    "_ABPythiatantiTopPtWithtopbtagGeneratorDiff_systDown",
]

systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag=[
                    "ABPythiatantiTopPtWithtopbtagGeneratorDiff_systUp:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt+ abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    "ABPythiatantiTopPtWithtopbtagGeneratorDiff_systDown:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt- abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
]

if WWP=='medium':
  weightsystnamesABCD=[
                    "_" + ABCDversion + "_ABCD_rateUp",
                    "_" + ABCDversion + "_ABCD_rateDown",
                    "_" + ABCDversion + "_ABCD_shapeUp",
                    "_" + ABCDversion + "_ABCD_shapeDown",
                ]
  if ABCDversion is 'ABCD3':            
    weightsystnamesABCD=weightsystnamesABCD+[
                    "_ABCD3_inclusive_ZprimeM_systUp",
                    "_ABCD3_inclusive_ZprimeM_systDown",
                    "_ABCD3_notopbtag_ZprimeM_systUp",
                    "_ABCD3_notopbtag_ZprimeM_systDown",
                    "_ABCD3_withtopbtag_ZprimeM_systUp",
                    "_ABCD3_withtopbtag_ZprimeM_systDown",
                    #"_ABCD3_inclusive_TprimeM_systUp",
                    #"_ABCD3_inclusive_TprimeM_systDown",
                    #"_ABCD3_notopbtag_TprimeM_systUp",
                    #"_ABCD3_notopbtag_TprimeM_systDown",
                    #"_ABCD3_withtopbtag_TprimeM_systUp",
                    #"_ABCD3_withtopbtag_TprimeM_systDown",  
                    ]
  elif ABCDversion is 'ABCD5':            
    weightsystnamesABCD=weightsystnamesABCD+[
                    "_ABCD5_inclusive_ZprimeM_systUp",
                    "_ABCD5_inclusive_ZprimeM_systDown",
                    "_ABCD5_notopbtag_ZprimeM_systUp",
                    "_ABCD5_notopbtag_ZprimeM_systDown",
                    "_ABCD5_withtopbtag_ZprimeM_systUp",
                    "_ABCD5_withtopbtag_ZprimeM_systDown",
                    #"_ABCD5_inclusive_TprimeM_systUp",
                    #"_ABCD5_inclusive_TprimeM_systDown",
                    #"_ABCD5_notopbtag_TprimeM_systUp",
                    #"_ABCD5_notopbtag_TprimeM_systDown",
                    #"_ABCD5_withtopbtag_TprimeM_systUp",
                    #"_ABCD5_withtopbtag_TprimeM_systDown", 

                    ]
  #else: 
    #print "Wrong WPs"
    
#else:
  #print "Wrong WPs"
  #raw_input()
  #break
    
    
#if topWP=='loose' and WWP=='loose' and bottomWP=='medium':

    #systweightsABCD=[
                    
                    #"" + ABCDversion + "_ABCD_rateUp:=ABCD_rate_systUp*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"" + ABCDversion + "_ABCD_rateDown:=ABCD_rate_systDown*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"" + ABCDversion + "_ABCD_shapeUp:=ABCD_shape_systUp*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"" + ABCDversion + "_ABCD_shapeDown:=ABCD_shape_systDown*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
            
    #]
    #if ABCDversion is 'ABCD3': 
        #systweightsABCD=systweightsABCD+[
                    #"ABCD3_inclusive_ZprimeM_systUp:= pow(1+0.019232,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_inclusive_ZprimeM_systDown:= pow(1-0.019232,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_notopbtag_ZprimeM_systUp:= pow(1+0.015085,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_notopbtag_ZprimeM_systDown:= pow(1-0.015085,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_withtopbtag_ZprimeM_systUp:= pow(1+0.13,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_withtopbtag_ZprimeM_systDown:= pow(1-0.13,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD3_inclusive_TprimeM_systUp:= pow(1+0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD3_inclusive_TprimeM_systDown:= pow(1-0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD3_notopbtag_TprimeM_systUp:= pow(1+0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD3_notopbtag_TprimeM_systDown:= pow(1-0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD3_withtopbtag_TprimeM_systUp:= pow(1+0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD3_withtopbtag_TprimeM_systDown:= pow(1-0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",          
          
        #]
    #elif ABCDversion is 'ABCD5': 
        #systweightsABCD=systweightsABCD+[ 
                    #"ABCD5_inclusive_ZprimeM_systUp:= pow(1+0.03681,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_inclusive_ZprimeM_systDown:= pow(1-0.03681,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_notopbtag_ZprimeM_systUp:= pow(1+0.03671,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_notopbtag_ZprimeM_systDown:= pow(1-0.03671,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_withtopbtag_ZprimeM_systUp:= pow(1+0.033691,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_withtopbtag_ZprimeM_systDown:= pow(1-0.033691,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD5_inclusive_TprimeM_systUp:= pow(1+0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD5_inclusive_TprimeM_systDown:= pow(1-0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD5_notopbtag_TprimeM_systUp:= pow(1+0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD5_notopbtag_TprimeM_systDown:= pow(1-0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD5_withtopbtag_TprimeM_systUp:= pow(1+0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ##"ABCD5_withtopbtag_TprimeM_systDown:= pow(1-0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",       
        #]

    
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

    ]
          
murmufGstars=[#muR20muF20,muR05muF05,muR20muF10,muR05muF10,muR10muF20,muR10muF05
[0.902298845069,1.07357151428,0.793411397192,1.12920371887,1.06331345473,0.844779183017],    #1500
[0.913541564396,1.07114310217,0.788859891827,1.11569334394,0.847201881135,0.847201881135],    #1750
[0.923842764153,1.06855988154,0.785227925426,1.10349024658,0.849681375230,0.84968137523],    #2000
[0.933137438387,1.06592639902,0.781691305888,1.09273276844,0.851738871894,0.851738871894],    #2250
[0.941522478977,1.06328174834,0.777840522115,1.08333081305,0.853184006575,0.853184006575],    #2500  
[0.949449385820,1.06058432115,0.774780218314,1.07448235922,0.854855062329,0.854855062329],    #2750  
[0.956902394754,1.05792270536,0.770967744269,1.06648128262,0.855854021111,0.855854021111],    #3000  
[0.970622717239,1.05270948818,0.764547328234,1.05195774915,0.857959613747,0.857959613747],    #3500  
[0.982975177373,1.04780254477,0.758514448366,1.03929120896,0.859612665386,0.859612665386],    #4000  
]
PDFsGstar=[
[1.0,1.0,1.0], #1500
[1.0,1.0,1.0], #1750
[1.0,1.0,1.0], #2000
[1.0,1.0,1.0], #2250
[1.0,1.0,1.0], #2500
[1.0,1.0,1.0], #2750
[1.0,1.0,1.0], #3000
[1.0,1.0,1.0], #3500
[1.0,1.0,1.0], #4000



]
systweightnamesMCSFs=[
                    #"CSV_nominal:=(1)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systUp:=(1*(1+1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systDown:=(1*(1-1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "nom:=1.0",
                    
                    "" + ABCDversion + "_nominal:=(MCSF_Weight_" + ABCDversion + "*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    
                    
                    "" + ABCDversion + "_MCSF_CSVLFUp:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFUp*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFDown:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFDown*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFUp:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFUp*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFDown:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFDown*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats1Up*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats1Down*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats1Up*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats1Down*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats2Up*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats2Down*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats2Up*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats2Down*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr1Up*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr1Down*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr2Up*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr2Down*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_toptagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightUp*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_toptagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightDown*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_topmisstagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_topmisstagweightnominal*" + ABCDversion + "_topmisstagweightUp*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_topmisstagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_topmisstagweightnominal*" + ABCDversion + "_topmisstagweightDown*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                                        
                    "" + ABCDversion + "_MCSF_WtagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_weightnominal*" + ABCDversion + "_Wtag_weightUp*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_WtagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_weightnominal*" + ABCDversion + "_Wtag_weightDown*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",     
                    #"" + ABCDversion + "_MCSF_Wtag_tag_t21anti_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_tag_t21anti_weightnominal*" + ABCDversion + "_Wtag_tag_t21anti_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_tag_t21anti_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_tag_t21anti_weightnominal*" + ABCDversion + "_Wtag_tag_t21anti_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21_weightnominal*" + ABCDversion + "_Wtag_mistag_t21_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21_weightnominal*" + ABCDversion + "_Wtag_mistag_t21_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21anti_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21anti_weightnominal*" + ABCDversion + "_Wtag_mistag_t21anti_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21anti_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21anti_weightnominal*" + ABCDversion + "_Wtag_mistag_t21anti_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
 
                    
                    "" + ABCDversion + "_MCSF_PUUp:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Up*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_PUDown:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Down*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "" + ABCDversion + "_MCSF_PDFUp:=(MCSF_Weight_" + ABCDversion + "/Weight_LHA_NNPDF30_nlo_as_0118_nominal*Weight_LHA_NNPDF30_nlo_as_0118_up*((murmufGstar1500==1)/"+str(PDFsGstar[0][2])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][2])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][2])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][2])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][2])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][2])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][2])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][2])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][2])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_PDFDown:=(MCSF_Weight_" + ABCDversion + "/Weight_LHA_NNPDF30_nlo_as_0118_nominal*Weight_LHA_NNPDF30_nlo_as_0118_down*((murmufGstar1500==1)/"+str(PDFsGstar[0][0])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][0])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][0])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][0])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][0])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][0])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][0])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][0])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][0])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                                        
                    "" + ABCDversion + "_MCSF_LumiUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.025)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_LumiDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.025)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    "" + ABCDversion + "_MCSF_TriggerUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.016)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_TriggerDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.016)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "" + ABCDversion + "_ttbarXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.05)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_ttbarXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.05)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_ST_tWXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.053)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights_ST_tW==1)+(DoWeights*DoMCDataWeights_ST_tW==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_ST_tWXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.053)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights_ST_tW==1)+(DoWeights*DoMCDataWeights_ST_tW==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",   
                    "" + ABCDversion + "_ST_tchanXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.042)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights_ST_t==1)+(DoWeights*DoMCDataWeights_ST_t==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_ST_tchanXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.036)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights_ST_t==1)+(DoWeights*DoMCDataWeights_ST_t==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",                    
                    "" + ABCDversion + "_ST_schanXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.037)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights_ST_s==1)+(DoWeights*DoMCDataWeights_ST_s==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",
                    "" + ABCDversion + "_ST_schanXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.047)*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights_ST_s==1)+(DoWeights*DoMCDataWeights_ST_s==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*triggered",                         
                    
                    
                    

                    "" + ABCDversion + "_MCSF_powheg_renfac_envUp:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeUp*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_renfac_envDown:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeDown*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    "" + ABCDversion + "_MCSF_powheg_renfacUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF2p0"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][0])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][0])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][0])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][0])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][0])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][0])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][0])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][0])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][0])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_renfacDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF0p5"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][1])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][1])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][1])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][1])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][1])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][1])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][1])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_renUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF1p0"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][2])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][2])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][2])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][2])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][2])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][2])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][2])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][2])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][2])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_renDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF1p0"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][3])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][3])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][3])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][3])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][3])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][3])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][3])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][3])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][3])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_facUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF2p0"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][4])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][4])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][4])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][4])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][4])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][4])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][4])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][4])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][4])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_powheg_facDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF0p5"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][5])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][5])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][5])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][5])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][5])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][5])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][5])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][5])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][5])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 



                    "" + ABCDversion + "_MCSF_amc_renfac_envUp:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeUp*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_renfac_envDown:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeDown*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    "" + ABCDversion + "_MCSF_amc_renfacUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF2p0"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][0])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][0])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][0])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][0])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][0])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][0])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][0])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][0])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][0])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_renfacDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF0p5"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][1])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][1])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][1])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][1])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][1])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][1])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][1])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_renUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF1p0"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][2])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][2])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][2])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][2])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][2])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][2])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][2])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][2])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][2])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_renDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF1p0"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][3])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][3])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][3])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][3])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][3])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][3])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][3])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][3])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][3])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_facUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF2p0"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][4])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][4])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][4])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][4])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][4])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][4])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][4])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][4])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][4])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_amc_facDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF0p5"+"*((murmufGstar1500==1)/"+str(murmufGstars[0][5])+"+(murmufGstar1750==1)/"+str(murmufGstars[1][5])+"+(murmufGstar2000==1)/"+str(murmufGstars[2][5])+"+(murmufGstar2250==1)/"+str(murmufGstars[3][5])+"+(murmufGstar2500==1)/"+str(murmufGstars[4][5])+"+(murmufGstar2750==1)/"+str(murmufGstars[5][5])+"+(murmufGstar3000==1)/"+str(murmufGstars[6][5])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][5])+"+(murmufGstar4000==1)/"+str(murmufGstars[8][5])+")*((murmufGstar1500==1)/"+str(PDFsGstar[0][1])+"+(murmufGstar1750==1)/"+str(PDFsGstar[1][1])+"+(murmufGstar2000==1)/"+str(PDFsGstar[2][1])+"+(murmufGstar2250==1)/"+str(PDFsGstar[3][1])+"+(murmufGstar2500==1)/"+str(PDFsGstar[4][1])+"+(murmufGstar2750==1)/"+str(PDFsGstar[5][1])+"+(murmufGstar3000==1)/"+str(PDFsGstar[6][1])+"+(murmufGstar3500==1)/"+str(murmufGstars[7][1])+"+(murmufGstar4000==1)/"+str(PDFsGstar[8][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 


    ]
    

    #systweightnamesMCSFs=[
                    #"ABCD2_nominal:=(MCSF_Weight_ABCD2)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    #"ABCD2_MCSF_CSVLFUp:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVLFUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVLFDown:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVLFDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVHFUp:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVHFUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVHFDown:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVHFDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVHFStats1Up:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVHFStats1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVHFStats1Down:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVHFStats1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVLFStats1Up:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVLFStats1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVLFStats1Down:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVLFStats1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVHFStats2Up:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVHFStats2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVHFStats2Down:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVHFStats2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVLFStats2Up:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVLFStats2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVLFStats2Down:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVLFStats2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVCErr1Up:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVCErr1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVCErr1Down:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVCErr1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVCErr2Up:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVCErr2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_CSVCErr2Down:=(MCSF_Weight_ABCD2/ABCD2_WeightCSVnominal*ABCD2_WeightCSVCErr2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_toptagUp:=(MCSF_Weight_ABCD2/ABCD2_toptagweightnominal*ABCD2_toptagweightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_toptagDown:=(MCSF_Weight_ABCD2/ABCD2_toptagweightnominal*ABCD2_toptagweightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_WtagUp:=(MCSF_Weight_ABCD2/ABCD2_Wtagweightnominal*ABCD2_WtagweightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_WtagDown:=(MCSF_Weight_ABCD2/ABCD2_Wtagweightnominal*ABCD2_WtagweightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    #"ABCD2_MCSF_PUUp:=(MCSF_Weight_ABCD2/Weight_pu69p2*Weight_pu69p2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_PUDown:=(MCSF_Weight_ABCD2/Weight_pu69p2*Weight_pu69p2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    #"ABCD2_MCSF_PDFUp:=(MCSF_Weight_ABCD2/PDF_RMSMean*PDF_RMSUp)*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0",
                    #"ABCD2_MCSF_PDFDown:=(MCSF_Weight_ABCD2/PDF_RMSMean*PDF_RMSDown)*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0",
                    #"ABCD2_MCSF_LumiUp:=(MCSF_Weight_ABCD2*(1.0+0.025))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_LumiDown:=(MCSF_Weight_ABCD2*(1.0-0.025))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",                  

                    #"ABCD2_MCSF_renfac_envUp:=(MCSF_Weight_ABCD2*MCSF_RenFac_envelopeUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_renfac_envDown:=(MCSF_Weight_ABCD2*MCSF_RenFac_envelopeDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_ttbarXSUp:=(MCSF_Weight_ABCD2*(1.0+0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0",
                    #"ABCD2_ttbarXSDown:=(MCSF_Weight_ABCD2*(1.0-0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0",
              
              
                    #"ABCD2_MCSF_renfacUp:=(Weight_scale_variation_muR2p0_muF2p0)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_renfacDown:=(Weight_scale_variation_muR0p5_muF0p5)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_renUp:=(Weight_scale_variation_muR2p0_muF1p0)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_renDown:=(Weight_scale_variation_muR0p5_muF1p0)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_facUp:=(Weight_scale_variation_muR1p0_muF2p0)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"ABCD2_MCSF_facDown:=(Weight_scale_variation_muR1p0_muF0p5)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",            
                    
                    
    #]

#for i in range(0,100):


    ##weigthsystnamesMCSFs.append("_MCSF_PDF"+str(i)+"Up")
    ##weigthsystnamesMCSFs.append("_MCSF_PDF"+str(i)+"Down")
    ##systweightnamesMCSFs.append("MCSF_PDF"+str(i)+"Up:=(Weight_nnpdf30_lo_as_0130_0 + abs(Weight_nnpdf30_lo_as_0130_0 - Weight_nnpdf30_lo_as_0130_0"+str(i)+"))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0")
    ##systweightnamesMCSFs.append("MCSF_PDF"+str(i)+"Down:=(Weight_nnpdf30_lo_as_0130_0 - abs(Weight_nnpdf30_lo_as_0130_0 - Weight_nnpdf30_lo_as_0130_0"+str(i)+"))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0")
    #weigthsystnamesMCSFs.append("_MCSF_PDF"+str(i))
    #systweightnamesMCSFs.append("MCSF_PDF"+str(i)+":=(Weight_nnpdf30_lo_as_0130_"+str(i)+")*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0")
    #print 'weigthsystnamesMCSFs= ',len(weigthsystnamesMCSFs), '  systweightnamesMCSFs=',len(systweightnamesMCSFs)
    

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
path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"
path="/pnfs/desy.de/cms/tier2/store/user/skudella/*/MC_limits_*/*/*/*"
path_new="/pnfs/desy.de/cms/tier2/store/user/skudella/*/MC_limits_*/1805*/*/*"

#path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_old/"

#DATA_MC_rate_scalefactor_QCD='0.506626268137'
#DATA_MC_rate_scalefactor_QCD='0.681942750822'
DATA_MC_rate_scalefactor_QCD='0.761444753045'

sampleDict=SampleDictionary()

SignalSamples=[


                    Sample('G->tWb, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToWB*Zp1500Nar*800Nar*nominal*Tree*.root',mcweight+'/45.51*248432.0/248385.0','SigGstar1500800_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToWB*Zp1500Nar*1000Nar*nominal*Tree*.root',mcweight+'/28.52*245491.0/245442.0','SigGstar15001000_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToWB*Zp1500Nar*1300Nar*nominal*Tree*.root',mcweight+'/3.888*248434.0/248344.0','SigGstar15001300_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb, m(Gp_{Nar})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToWB*Zp1750*Nar*1300Nar*nominal*Tree*.root',mcweight+'/8.951*245928.0/245838.0','SigGstar17501300_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToWB*Zp2000Nar*1000Nar*LH*nominal*Tree*.root',mcweight+'/11.6*238860.0/238765.0','SigGstar20001000_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToWB*Zp2000Nar*1300Nar*LH*nominal*Tree*.root',mcweight+'/7.248*246954.0/246846.0','SigGstar20001300_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToWB*Zp2000Nar*1500Nar*nominal*Tree*.root',mcweight+'/4.33*247216.0/247089.0','SigGstar20001500_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToWB*Zp2250*Nar*1300Nar*nominal*Tree*.root',mcweight+'/4.879*246910.0/246794.0','SigGstar22501300_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToWB*Zp2250*Nar*1500Nar*nominal*Tree*.root',mcweight+'/3.528*250000.0/249859.0','SigGstar22501500_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1300',ROOT.kCyan,path+'Zprime*ToWB*Zp2500Nar*1300Nar*nominal*Tree*.root',mcweight+'/2.982*238023.0/237882.0' ,'SigGstar25001300_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToWB*Zp2500Nar*1500Nar*nominal*Tree*.root',mcweight+'/2.440*243695.0/243539.0' ,'SigGstar25001500_tWb'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToWB*Zp2500Nar*1800Nar*nominal*Tree*.root',mcweight+'/1.467*233654.0/233478.0' ,'SigGstar25001800_tWb'+'Nar',allweightsystnames,samDict=sampleDict),                 
                 
                    Sample('G->tWb, m(Gp_{Nar})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToWB*Zp2750*Nar*1500Nar*nominal*Tree*.root',mcweight+'/1.583*238854.0/238665.0','SigGstar27501500_tWb'+'Nar',allweightsystnames,samDict=sampleDict),

                    Sample('G->tWb, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToWB*Zp3000Nar*1500Nar*nominal*Tree*.root',mcweight+'/1.002*246860.0/246643.0' ,'SigGstar30001500_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToWB*Zp3000Nar*1800Nar*nominal*Tree*.root',mcweight+'/0.7563*239740.0/239509.0' ,'SigGstar30001800_tWb'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToWB*Zp3000Nar*2100Nar*nominal*Tree*.root',mcweight+'/0.509*245156.0/247404.0' ,'SigGstar30002100_tWb'+'Nar',allweightsystnames,samDict=sampleDict), 

                    Sample('G->tWb, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToWB*Zp3500Nar*1800Nar*nominal*Tree*.root',mcweight+'/0.3202*249585.0/249320.0' ,'SigGstar35001800_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToWB*Zp3500Nar*2100Nar*nominal*Tree*.root',mcweight+'/0.2502*246897.0/246607.0' ,'SigGstar35002100_tWb'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToWB*Zp3500Nar*2500Nar*nominal*Tree*.root',mcweight+'/0.1562*248230.0/247903.0' ,'SigGstar35002500_tWb'+'Nar',allweightsystnames,samDict=sampleDict), 

                    Sample('G->tWb, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToWB*Zp4000Nar*2100Nar*nominal*Tree*.root',mcweight+'/0.1027*236624.0/236290.0' ,'SigGstar40002100_tWb'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToWB*Zp4000Nar*2500Nar*nominal*Tree*.root',mcweight+'/0.07946*244460.0/244109.0' ,'SigGstar40002500_tWb'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path+'Zprime*ToWB*Zp4000Nar*3000Nar*nominal*Tree*.root',mcweight+'/0.04446*245912.0/245509.0' ,'SigGstar40003000_tWb'+'Nar',allweightsystnames,samDict=sampleDict), 
                    
         


                    Sample('G->ttZ, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToZT*Zp1500Nar*800Nar*nominal*Tree*.root',mcweight+'/19.73*246845.0/246811.0','SigGstar1500800_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToZT*Zp1500Nar*1000Nar*nominal*Tree*.root',mcweight+'/12.93*246364.0/246315.0','SigGstar15001000_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToZT*Zp1500Nar*1300Nar*nominal*Tree*.root',mcweight+'/1.831*247816.0/247768.0','SigGstar15001300_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttZ, m(Gp_{Nar})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToZT*Zp1750*Nar*1300Nar*nominal*Tree*.root',mcweight+'/4.247*237937.0/237886.0','SigGstar17501300_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttZ, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToZT*Zp2000Nar*1000Nar*LH*nominal*Tree*.root',mcweight+'/5.302*250000.0/249939.0','SigGstar20001000_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToZT*Zp2000Nar*1300Nar*LH*nominal*Tree*.root',mcweight+'/3.444*246960.0/246895.0','SigGstar20001300_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToZT*Zp2000Nar*1500Nar*nominal*Tree*.root',mcweight+'/2.079*246832.0/246762.0','SigGstar20001500_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttZ, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToZT*Zp2250*Nar*1300Nar*nominal*Tree*.root',mcweight+'/2.307*245960.0/245891.0','SigGstar22501300_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToZT*Zp2250*Nar*1500Nar*nominal*Tree*.root',mcweight+'/2.315*242410.0/241701.0','SigGstar22501500_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttZ, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1300',ROOT.kCyan,path+'Zprime*ToZT*Zp2500Nar*1300Nar*nominal*Tree*.root',mcweight+'/1.456*246856.0/246769.0' ,'SigGstar25001300_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToZT*Zp2500Nar*1500Nar*nominal*Tree*.root',mcweight+'/1.17*233280.0/246461.0' ,'SigGstar25001500_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttZ, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToZT*Zp2500Nar*1800Nar*nominal*Tree*.root',mcweight+'/0.7136*246728.0/233176.0' ,'SigGstar25001800_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),                 
                 
                    Sample('G->ttZ, m(Gp_{Nar})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToZT*Zp2750*Nar*1500Nar*nominal*Tree*.root',mcweight+'/0.7609*246356.0/246240.0','SigGstar27501500_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),

                    Sample('G->ttZ, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToZT*Zp3000Nar*1500Nar*nominal*Tree*.root',mcweight+'/0.4788*233500.0/233369.0' ,'SigGstar30001500_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToZT*Zp3000Nar*1800Nar*nominal*Tree*.root',mcweight+'/0.3673*243392.0/243236.0' ,'SigGstar30001800_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttZ, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToZT*Zp3000Nar*2100Nar*nominal*Tree*.root',mcweight+'/0.2483*249704.0/249540.0' ,'SigGstar30002100_ttZ'+'Nar',allweightsystnames,samDict=sampleDict), 

                    Sample('G->ttZ, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToZT*Zp3500Nar*1800Nar*nominal*Tree*.root',mcweight+'/0.1560*249670.0/249457.0' ,'SigGstar35001800_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToZT*Zp3500Nar*2100Nar*nominal*Tree*.root',mcweight+'/0.1223*250000.0/249794.0' ,'SigGstar35002100_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttZ, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToZT*Zp3500Nar*2500Nar*nominal*Tree*.root',mcweight+'/0.07688*248038.0/247811.0' ,'SigGstar35002500_ttZ'+'Nar',allweightsystnames,samDict=sampleDict), 

                    Sample('G->ttZ, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToZT*Zp4000Nar*2100Nar*nominal*Tree*.root',mcweight+'/0.05284*248308.0/248009.0' ,'SigGstar40002100_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToZT*Zp4000Nar*2500Nar*nominal*Tree*.root',mcweight+'/0.03903*244709.0/244437.0' ,'SigGstar40002500_ttZ'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttZ, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path_new+'Zprime*ToZT*Zp4000Nar*3000Nar*nominal*Tree*.root',mcweight+'/0.02199*235310.0/(235028.0-4276)' ,'SigGstar40003000_ttZ'+'Nar',allweightsystnames,samDict=sampleDict), 
                    
                    
                    
                    
         



                    Sample('G->ttH, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToHT*Zp1500Nar*800Nar*nominal*Tree*.root',mcweight+'/21.56*232625.0/232591.0','SigGstar1500800_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToHT*Zp1500Nar*1000Nar*nominal*Tree*.root',mcweight+'/13.83*245160.0/245118.0','SigGstar15001000_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToHT*Zp1500Nar*1300Nar*nominal*Tree*.root',mcweight+'/1.902*246056.0/246013.0','SigGstar15001300_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttH, m(Gp_{Nar})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToHT*Zp1750*Nar*1300Nar*nominal*Tree*.root',mcweight+'/4.429*246290.0/246236.0','SigGstar17501300_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToHT*Zp2000Nar*1000Nar*LH*nominal*Tree*.root',mcweight+'/5.647*246855.0/246771.0','SigGstar20001000_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToHT*Zp2000Nar*1300Nar*LH*nominal*Tree*.root',mcweight+'/3.573*0.54*238270.0/238233.0','SigGstar20001300_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    #Sample('G->ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToHT*Zp2000Nar*1000Nar*LH*nominal*Tree*.root',mcweight+'/100000*238270.0/238233.0','SigGstar20001300_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToHT*Zp2000Nar*1500Nar*nominal*Tree*.root',mcweight+'/2.131*245363.0/245272.0','SigGstar20001500_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttH, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToHT*Zp2250*Nar*1300Nar*nominal*Tree*.root',mcweight+'/2.399*244627.0/244512.0','SigGstar22501300_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToHT*Zp2250*Nar*1500Nar*nominal*Tree*.root',mcweight+'/1.744*248588.0/248488.0','SigGstar22501500_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1300',ROOT.kCyan,path+'Zprime*ToHT*Zp2500Nar*1300Nar*nominal*Tree*.root',mcweight+'/1.507*249066.0/248933.0' ,'SigGstar25001300_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    #Sample('G->ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToHT*Zp2500Nar*1500Nar*nominal*Tree*.root',mcweight+'/1.204*10.0*240770.0/240623.0' ,'SigGstar25001500_ttH'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToHT*Zp2500Nar*1500Nar*nominal*Tree*.root',mcweight+'/1.204*240770.0/240623.0' ,'SigGstar25001500_ttH'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    ##Sample('G->ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToHT*Zp2500Nar*1800Nar*nominal*Tree*.root',mcweight+'/0.7276*10.0*249424.0/249273.0' ,'SigGstar25001800_ttH'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToHT*Zp2500Nar*1800Nar*nominal*Tree*.root',mcweight+'/0.7276*249424.0/249273.0' ,'SigGstar25001800_ttH'+'Nar',allweightsystnames,samDict=sampleDict),                 
                 
                    Sample('G->ttH, m(Gp_{Nar})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToHT*Zp2750*Nar*1500Nar*nominal*Tree*.root',mcweight+'/0.7825*237106.0/236924.0','SigGstar27501500_ttH'+'Nar',allweightsystnames,samDict=sampleDict),

                    Sample('G->ttH, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToHT*Zp3000Nar*1500Nar*nominal*Tree*.root',mcweight+'/0.4936*239810.0/239612.0' ,'SigGstar30001500_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToHT*Zp3000Nar*1800Nar*nominal*Tree*.root',mcweight+'/0.3752*246755.0/246561.0' ,'SigGstar30001800_ttH'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttH, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToHT*Zp3000Nar*2100Nar*nominal*Tree*.root',mcweight+'/0.2511*245890.0/245662.0' ,'SigGstar30002100_ttH'+'Nar',allweightsystnames,samDict=sampleDict), 

                    Sample('G->ttH, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToHT*Zp3500Nar*1800Nar*nominal*Tree*.root',mcweight+'/0.1579*237616.0/237313.0' ,'SigGstar35001800_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToHT*Zp3500Nar*2100Nar*nominal*Tree*.root',mcweight+'/0.1245*243421.0/243137.0' ,'SigGstar35002100_ttH'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttH, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToHT*Zp3500Nar*2500Nar*nominal*Tree*.root',mcweight+'/0.07811*241612.0/241288.0' ,'SigGstar35002500_ttH'+'Nar',allweightsystnames,samDict=sampleDict), 

                    Sample('G->ttH, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToHT*Zp4000Nar*2100Nar*nominal*Tree*.root',mcweight+'/0.05331*243202.0/242850.0' ,'SigGstar40002100_ttH'+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToHT*Zp4000Nar*2500Nar*nominal*Tree*.root',mcweight+'/0.03950*245831.0/245447.0' ,'SigGstar40002500_ttH'+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttH, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path+'Zprime*ToHT*Zp4000Nar*3000Nar*nominal*Tree*.root',mcweight+'/0.02133*237112.0/236663.0' ,'SigGstar40003000_ttH'+'Nar',allweightsystnames,samDict=sampleDict), 


                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToHT*Zp1500Nar*800Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar1500800_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToHT*Zp1500Nar*1000Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar15001000_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToHT*Zp1500Nar*1300Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar15001300_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToHT*Zp1750*Nar*1300Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar17501300_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToHT*Zp2000Nar*1000Nar*LH*nominal*Tree*.root',mcweight+'/10000000','SigGstar20001000_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    #Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToHT*Zp2000Nar*1300Nar*LH*nominal*Tree*.root',mcweight+'/10000000','SigGstar20001300_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToHT*Zp2000Nar*1000Nar*LH*nominal*Tree*.root',mcweight+'/10000000','SigGstar20001300_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToHT*Zp2000Nar*1500Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar20001500_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToHT*Zp2250*Nar*1300Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar22501300_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToHT*Zp2250*Nar*1500Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar22501500_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1300',ROOT.kCyan,path+'Zprime*ToHT*Zp2500Nar*1300Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar25001300_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToHT*Zp2500Nar*1500Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar25001500_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToHT*Zp2500Nar*1800Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar25001800_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),                 
                 
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToHT*Zp2750*Nar*1500Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar27501500_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),

                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToHT*Zp3000Nar*1500Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar30001500_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToHT*Zp3000Nar*1800Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar30001800_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToHT*Zp3000Nar*2100Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar30002100_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict), 

                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToHT*Zp3500Nar*1800Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar35001800_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToHT*Zp3500Nar*2100Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar35002100_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToHT*Zp3500Nar*2500Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar35002500_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict), 

                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToHT*Zp4000Nar*2100Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar40002100_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToHT*Zp4000Nar*2500Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar40002500_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Nar})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path+'Zprime*ToHT*Zp4000Nar*3000Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar40003000_'+BR_name+'Nar',allweightsystnames,samDict=sampleDict), 






                    Sample('G->tWb, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToWB*Zp1500Wid*800Nar*nominal*Tree*.root',mcweight+'/1.086*238560.0/238513.0','SigGstar1500800_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToWB*Zp1500Wid*1000Nar*nominal*Tree*.root',mcweight+'/0.6229*250000.0/249933.0','SigGstar15001000_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToWB*Zp1500Wid*1300Nar*nominal*Tree*.root',mcweight+'/0.1636*241750.0/241634.0','SigGstar15001300_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb, m(Gp_{Wid})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToWB*Zp1750*Wid*1300Nar*nominal*Tree*.root',mcweight+'/8.976*248587.0/248483.0','SigGstar17501300_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToWB*Zp2000Wid*1000Nar*LH*nominal*Tree*.root',mcweight+'/0.2904*242040.0/241944.0','SigGstar20001000_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToWB*Zp2000Wid*1300Nar*LH*nominal*Tree*.root',mcweight+'/0.1578*244752.0/244665.0','SigGstar20001300_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToWB*Zp2000Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.09067*239410.0/239288.0','SigGstar20001500_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb, m(Gp_{Wid})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToWB*Zp2250*Wid*1300Nar*nominal*Tree*.root',mcweight+'/4.88*250000.0/249875.0','SigGstar22501300_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Wid})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToWB*Zp2250*Wid*1500Nar*nominal*Tree*.root',mcweight+'/3.53*248826.0/248692.0','SigGstar22501500_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1300',ROOT.kCyan,path+'Zprime*ToWB*Zp2500Wid*1300Nar*nominal*Tree*.root',mcweight+'/0.07731*241928.0/241791.0' ,'SigGstar25001300_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToWB*Zp2500Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.05573*242220.0/242041.0' ,'SigGstar25001500_tWb'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToWB*Zp2500Wid*1800Nar*nominal*Tree*.root',mcweight+'/0.02993*238798.0/238626.0' ,'SigGstar25001800_tWb'+'Wid',allweightsystnames,samDict=sampleDict),                 
                 
                    Sample('G->tWb, m(Gp_{Wid})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToWB*Zp2750*Wid*1500Nar*nominal*Tree*.root',mcweight+'/1.578*240816.0/240627.0','SigGstar27501500_tWb'+'Wid',allweightsystnames,samDict=sampleDict),

                    Sample('G->tWb, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToWB*Zp3000Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.0269*239740.0/243487.0' ,'SigGstar30001500_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToWB*Zp3000Wid*1800Nar*nominal*Tree*.root',mcweight+'/0.01747*243695.0/244943.0' ,'SigGstar30001800_tWb'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToWB*Zp3000Wid*2100Nar*nominal*Tree*.root',mcweight+'/0.01026*246773.0/246517.0' ,'SigGstar30002100_tWb'+'Wid',allweightsystnames,samDict=sampleDict), 

                    Sample('G->tWb, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToWB*Zp3500Wid*1800Nar*nominal*Tree*.root',mcweight+'/0.008886*248407.0/248192.0' ,'SigGstar35001800_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToWB*Zp3500Wid*2100Nar*nominal*Tree*.root',mcweight+'/0.005958*233387.0/233100.0' ,'SigGstar35002100_tWb'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToWB*Zp3500Wid*2500Nar*nominal*Tree*.root',mcweight+'/0.003081*246359.0/245996.0' ,'SigGstar35002500_tWb'+'Wid',allweightsystnames,samDict=sampleDict), 

                    Sample('G->tWb, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToWB*Zp4000Wid*2100Nar*nominal*Tree*.root',mcweight+'/0.003129*243504.0/243191.0' ,'SigGstar40002100_tWb'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToWB*Zp4000Wid*2500Nar*nominal*Tree*.root',mcweight+'/0.001862*244442.0/244090.0' ,'SigGstar40002500_tWb'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path+'Zprime*ToWB*Zp4000Wid*3000Nar*nominal*Tree*.root',mcweight+'/0.000828*245370.0/244936.0' ,'SigGstar40003000_tWb'+'Wid',allweightsystnames,samDict=sampleDict), 
                    


                    Sample('G->ttZ, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToZT*Zp1500Wid*800Nar*nominal*Tree*.root',mcweight+'/0.4715*238270.0/238233.0','SigGstar1500800_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToZT*Zp1500Wid*1000Nar*nominal*Tree*.root',mcweight+'/0.2864*240766.0/240719.0','SigGstar15001000_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToZT*Zp1500Wid*1300Nar*nominal*Tree*.root',mcweight+'/0.07689*243724.0/243674.0','SigGstar15001300_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttZ, m(Gp_{Wid})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToZT*Zp1750*Wid*1300Nar*nominal*Tree*.root',mcweight+'/4.256*243673.0/243622.0','SigGstar17501300_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttZ, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToZT*Zp2000Wid*1000Nar*LH*nominal*Tree*.root',mcweight+'/0.1327*244605.0/244548.0','SigGstar20001000_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToZT*Zp2000Wid*1300Nar*LH*nominal*Tree*.root',mcweight+'/0.07492*249519.0/249460.0','SigGstar20001300_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToZT*Zp2000Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.04334*248972.0/248906.0','SigGstar20001500_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttZ, m(Gp_{Wid})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToZT*Zp2250*Wid*1300Nar*nominal*Tree*.root',mcweight+'/1.695*241775.0/242349.0','SigGstar22501300_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Wid})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToZT*Zp2250*Wid*1500Nar*nominal*Tree*.root',mcweight+'/1.696*245420.0/245339.0','SigGstar22501500_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttZ, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1300',ROOT.kCyan,path_new+'Zprime*ToZT*Zp2500Wid*1300Nar*nominal*Tree*.root',mcweight+'/0.03652*246560.0/206176.0' ,'SigGstar25001300_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToZT*Zp2500Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.02684*247744.0/246618.0' ,'SigGstar25001500_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttZ, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToZT*Zp2500Wid*1800Nar*nominal*Tree*.root',mcweight+'/0.01451*237291.0/237167.0' ,'SigGstar25001800_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),                 
                 
                    Sample('G->ttZ, m(Gp_{Wid})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToZT*Zp2750*Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.7649*246915.0/246791.0','SigGstar27501500_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),

                    Sample('G->ttZ, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToZT*Zp3000Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.01294*242300.0/242159.0' ,'SigGstar30001500_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToZT*Zp3000Wid*1800Nar*nominal*Tree*.root',mcweight+'/0.008574*244247.0/244093.0' ,'SigGstar30001800_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttZ, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToZT*Zp3000Wid*2100Nar*nominal*Tree*.root',mcweight+'/0.005022*249530.0/249360.0' ,'SigGstar30002100_ttZ'+'Wid',allweightsystnames,samDict=sampleDict), 

                    Sample('G->ttZ, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToZT*Zp3500Wid*1800Nar*nominal*Tree*.root',mcweight+'/0.004276*244113.0/211904.0' ,'SigGstar35001800_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToZT*Zp3500Wid*2100Nar*nominal*Tree*.root',mcweight+'/0.002908*247192.0/246952.0' ,'SigGstar35002100_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttZ, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToZT*Zp3500Wid*2500Nar*nominal*Tree*.root',mcweight+'/0.001521*238575.0/238357.0' ,'SigGstar35002500_ttZ'+'Wid',allweightsystnames,samDict=sampleDict), 

                    Sample('G->ttZ, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToZT*Zp4000Wid*2100Nar*nominal*Tree*.root',mcweight+'/0.001533*248377.0/248138.0' ,'SigGstar40002100_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttZ, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToZT*Zp4000Wid*2500Nar*nominal*Tree*.root',mcweight+'/0.000917*240860.0/240555.0' ,'SigGstar40002500_ttZ'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttZ, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path+'Zprime*ToZT*Zp4000Wid*3000Nar*nominal*Tree*.root',mcweight+'/0.000412*250000.0/249675.0' ,'SigGstar40003000_ttZ'+'Wid',allweightsystnames,samDict=sampleDict), 
                    
         

         



                    Sample('G->ttH, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToHT*Zp1500Wid*800Nar*nominal*Tree*.root',mcweight+'/0.5185*249184.0/249140.0','SigGstar1500800_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToHT*Zp1500Wid*1000Nar*nominal*Tree*.root',mcweight+'/0.3022*246616.0/246563.0','SigGstar15001000_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToHT*Zp1500Wid*1300Nar*nominal*Tree*.root',mcweight+'/0.0808*246040.0/245960.0','SigGstar15001300_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttH, m(Gp_{Wid})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToHT*Zp1750*Wid*1300Nar*nominal*Tree*.root',mcweight+'/4.426*247675.0/247607.0','SigGstar17501300_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttH, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToHT*Zp2000Wid*1000Nar*LH*nominal*Tree*.root',mcweight+'/0.1411*246638.0/246565.0','SigGstar20001000_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToHT*Zp2000Wid*1300Nar*LH*nominal*Tree*.root',mcweight+'/0.07749*238983.0/238893.0','SigGstar20001300_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToHT*Zp2000Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.04481*236319.0/236219.0','SigGstar20001500_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttH, m(Gp_{Wid})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToHT*Zp2250*Wid*1300Nar*nominal*Tree*.root',mcweight+'/2.403*244596.0/244496.0','SigGstar22501300_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Wid})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToHT*Zp2250*Wid*1500Nar*nominal*Tree*.root',mcweight+'/1.737*241442.0/241317.0','SigGstar22501500_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->ttH, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1300',ROOT.kCyan,path+'Zprime*ToHT*Zp2500Wid*1300Nar*nominal*Tree*.root',mcweight+'/0.03803*244568.0/244434.0' ,'SigGstar25001300_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path_new+'Zprime*ToHT*Zp2500Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.02759*247764.0/247606.0' ,'SigGstar25001500_ttH'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttH, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path_new+'Zprime*ToHT*Zp2500Wid*1800Nar*nominal*Tree*.root',mcweight+'/0.01474*241165.0/240998.0' ,'SigGstar25001800_ttH'+'Wid',allweightsystnames,samDict=sampleDict),                 
                 
                    Sample('G->ttH, m(Gp_{Wid})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToHT*Zp2750*Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.7817*240036.0/239881.0','SigGstar27501500_ttH'+'Wid',allweightsystnames,samDict=sampleDict),

                    Sample('G->ttH, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToHT*Zp3000Wid*1500Nar*nominal*Tree*.root',mcweight+'/0.0133*247378.0/247199.0' ,'SigGstar30001500_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToHT*Zp3000Wid*1800Nar*nominal*Tree*.root',mcweight+'/0.008698*248954.0/248724.0' ,'SigGstar30001800_ttH'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttH, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToHT*Zp3000Wid*2100Nar*nominal*Tree*.root',mcweight+'/0.005084*240460.0/240218.0' ,'SigGstar30002100_ttH'+'Wid',allweightsystnames,samDict=sampleDict), 

                    Sample('G->ttH, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToHT*Zp3500Wid*1800Nar*nominal*Tree*.root',mcweight+'/0.004407*247972.0/247700.0' ,'SigGstar35001800_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToHT*Zp3500Wid*2100Nar*nominal*Tree*.root',mcweight+'/0.002958*243392.0/243104.0' ,'SigGstar35002100_ttH'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttH, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToHT*Zp3500Wid*2500Nar*nominal*Tree*.root',mcweight+'/0.001534*248143.0/247789.0' ,'SigGstar35002500_ttH'+'Wid',allweightsystnames,samDict=sampleDict), 

                    Sample('G->ttH, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToHT*Zp4000Wid*2100Nar*nominal*Tree*.root',mcweight+'/0.001555*232832.0/232509.0' ,'SigGstar40002100_ttH'+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->ttH, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToHT*Zp4000Wid*2500Nar*nominal*Tree*.root',mcweight+'/0.000927*245970.0/245588.0' ,'SigGstar40002500_ttH'+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->ttH, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path+'Zprime*ToHT*Zp4000Wid*3000Nar*nominal*Tree*.root',mcweight+'/0.000414*249642.0/249137.0' ,'SigGstar40003000_ttH'+'Wid',allweightsystnames,samDict=sampleDict), 


                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=800',ROOT.kMagenta,path+'Zprime*ToHT*Zp1500Wid*800Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar1500800_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=1000',ROOT.kMagenta+2,path+'Zprime*ToHT*Zp1500Wid*1000Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar15001000_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=1500, m(Tp_{Nar,LH})=1300',ROOT.kMagenta-7,path+'Zprime*ToHT*Zp1500Wid*1300Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar15001300_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=1750, m(Tp_{Nar,LH})=1300',ROOT.kYellow-3,path+'Zprime*ToHT*Zp1750*Wid*1300Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar17501300_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1000',ROOT.kOrange-5,path+'Zprime*ToHT*Zp2000Wid*1000Nar*LH*nominal*Tree*.root',mcweight+'/10000000','SigGstar20001000_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1300',ROOT.kOrange-9,path+'Zprime*ToHT*Zp2000Wid*1300Nar*LH*nominal*Tree*.root',mcweight+'/10000000','SigGstar20001300_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=2000, m(Tp_{Nar,LH})=1500',ROOT.kOrange+3,path+'Zprime*ToHT*Zp2000Wid*1500Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar20001500_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=2250, m(Tp_{Nar,LH})=1300',ROOT.kSpring,path+'Zprime*ToHT*Zp2250*Wid*1300Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar22501300_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=2250, m(Tp_{Nar,LH})=1500',ROOT.kSpring+2,path+'Zprime*ToHT*Zp2250*Wid*1500Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar22501500_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1300',ROOT.kCyan,path+'Zprime*ToHT*Zp2500Wid*1300Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar25001300_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1500',ROOT.kCyan-3,path+'Zprime*ToHT*Zp2500Wid*1500Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar25001500_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=2500, m(Tp_{Nar,LH})=1800',ROOT.kCyan-7,path+'Zprime*ToHT*Zp2500Wid*1800Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar25001800_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),                 
                 
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=2750, m(Tp_{Nar,LH})=1500',ROOT.kPink,path+'Zprime*ToHT*Zp2750*Wid*1500Nar*nominal*Tree*.root',mcweight+'/10000000','SigGstar27501500_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),

                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=1500',ROOT.kRed+2,path+'Zprime*ToHT*Zp3000Wid*1500Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar30001500_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=1800',ROOT.kRed-7,path+'Zprime*ToHT*Zp3000Wid*1800Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar30001800_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=3000, m(Tp_{Nar,LH})=2100',ROOT.kRed-3,path+'Zprime*ToHT*Zp3000Wid*2100Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar30002100_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict), 

                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=1800',ROOT.kGreen,path+'Zprime*ToHT*Zp3500Wid*1800Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar35001800_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=2100',ROOT.kGreen+2,path+'Zprime*ToHT*Zp3500Wid*2100Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar35002100_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=3500, m(Tp_{Nar,LH})=2500',ROOT.kGreen-7,path+'Zprime*ToHT*Zp3500Wid*2500Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar35002500_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict), 

                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=2100',ROOT.kBlue-3,path+'Zprime*ToHT*Zp4000Wid*2100Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar40002100_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=2500',ROOT.kBlue-5,path+'Zprime*ToHT*Zp4000Wid*2500Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar40002500_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict),                 
                    Sample('G->tWb/ttZ/ttH, m(Gp_{Wid})=4000, m(Tp_{Nar,LH})=3000',ROOT.kBlue-9,path+'Zprime*ToHT*Zp4000Wid*3000Nar*nominal*Tree*.root',mcweight+'/10000000' ,'SigGstar40003000_'+BR_name+'Wid',allweightsystnames,samDict=sampleDict), 




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
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname,samDict=sampleDict))
    #DataSampleNames.append(sample.nick+sysname)
    print 'with JEC ', sample.path

 else:
  for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    thisnewsel=sample.selection
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path,thisnewsel,sample.nick+sysname,samDict=sampleDict))
    #DataSampleNames.append(sample.nick+sysname)  
    print 'no JEC ', sample.path


