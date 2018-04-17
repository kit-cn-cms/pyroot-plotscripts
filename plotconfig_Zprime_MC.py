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
          
murmufs=[#muR20muF20,muR05muF05,muR20muF10,muR05muF10,muR10muF20,muR10muF05
[0.943018825183,1.06342163233,0.999902678539,1.00011266322,0.943106166118,1.06331345473],    #1500
[0.929516248064,1.08024932978,0.999949012411,1.00005880273,0.929561359871,1.08020214758],    #2000
[0.918381534597,1.09442296069,0.999970237242,1.00003393267,0.918407254497,1.09440158723],    #2500  
]

systweightnamesMCSFs=[
                    #"CSV_nominal:=(1)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systUp:=(1*(1+1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systDown:=(1*(1-1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "nom:=1.0",
                    
                    "" + ABCDversion + "_nominal:=(MCSF_Weight_" + ABCDversion + ")*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    
                    
                    "" + ABCDversion + "_MCSF_CSVLFUp:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFDown:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFUp:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFDown:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVHFStats2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVLFStats2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr1Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr1Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr2Up:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr2Down:=(MCSF_Weight_" + ABCDversion + "*" + ABCDversion + "_WeightCSVCErr2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_toptagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_toptagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_topmisstagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_topmisstagweightnominal*" + ABCDversion + "_topmisstagweightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_topmisstagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_topmisstagweightnominal*" + ABCDversion + "_topmisstagweightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                                        
                    "" + ABCDversion + "_MCSF_WtagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_weightnominal*" + ABCDversion + "_Wtag_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_WtagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_weightnominal*" + ABCDversion + "_Wtag_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",     
                    #"" + ABCDversion + "_MCSF_Wtag_tag_t21anti_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_tag_t21anti_weightnominal*" + ABCDversion + "_Wtag_tag_t21anti_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_tag_t21anti_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_tag_t21anti_weightnominal*" + ABCDversion + "_Wtag_tag_t21anti_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21_weightnominal*" + ABCDversion + "_Wtag_mistag_t21_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21_weightnominal*" + ABCDversion + "_Wtag_mistag_t21_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21anti_Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21anti_weightnominal*" + ABCDversion + "_Wtag_mistag_t21anti_weightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"" + ABCDversion + "_MCSF_Wtag_mistag_t21anti_Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtag_mistag_t21anti_weightnominal*" + ABCDversion + "_Wtag_mistag_t21anti_weightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",  
 
                    
                    "" + ABCDversion + "_MCSF_PUUp:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_PUDown:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    "" + ABCDversion + "_MCSF_PDFUp:=(MCSF_Weight_" + ABCDversion + "/PDF_RMSMean*PDF_RMSUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_PDFDown:=(MCSF_Weight_" + ABCDversion + "/PDF_RMSMean*PDF_RMSDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                                        
                    "" + ABCDversion + "_MCSF_LumiUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.025))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_LumiDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.025))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    "" + ABCDversion + "_MCSF_TriggerUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.016))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_TriggerDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.016))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "" + ABCDversion + "_MCSF_renfac_envUp:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_renfac_envDown:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_ttbarXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_ttbarXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*MCSF_Weight_" + ABCDversion + "+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    
                    "" + ABCDversion + "_MCSF_renfacUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF2p0"+"*("+str(1.29465480107)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)+(murmuf1500==1)/"+str(murmufs[0][0])+"+(murmuf2000==1)/"+str(murmufs[1][0])+"+(murmuf2500==1)/"+str(murmufs[2][0])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_renfacDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF0p5"+"*("+str(0.755423761535)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)+(murmuf1500==1)/"+str(murmufs[0][1])+"+(murmuf2000==1)/"+str(murmufs[1][1])+"+(murmuf2500==1)/"+str(murmufs[2][1])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_renUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR2p0_muF1p0"+"*("+str(1.12267866063)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)+(murmuf1500==1)/"+str(murmufs[0][2])+"+(murmuf2000==1)/"+str(murmufs[1][2])+"+(murmuf2500==1)/"+str(murmufs[2][2])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_renDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR0p5_muF1p0"+"*("+str(0.814903279727)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)+(murmuf1500==1)/"+str(murmufs[0][3])+"+(murmuf2000==1)/"+str(murmufs[1][3])+"+(murmuf2500==1)/"+str(murmufs[2][3])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_facUp:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF2p0"+"*("+str(1.07529312329)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)+(murmuf1500==1)/"+str(murmufs[0][4])+"+(murmuf2000==1)/"+str(murmufs[1][4])+"+(murmuf2500==1)/"+str(murmufs[2][4])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_facDown:=(MCSF_Weight_" + ABCDversion + "*Weight_scale_variation_muR1p0_muF0p5"+"*("+str(0.926990626083)+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0)+(murmuf1500==1)/"+str(murmufs[0][5])+"+(murmuf2000==1)/"+str(murmufs[1][5])+"+(murmuf2500==1)/"+str(murmufs[2][5])+"))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 

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
#path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_old/"

#DATA_MC_rate_scalefactor_QCD='0.506626268137'
#DATA_MC_rate_scalefactor_QCD='0.681942750822'
DATA_MC_rate_scalefactor_QCD='0.761444753045'

if not doBR:
    
    SignalSamples=[
                    Sample('Z->tWb, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->Wb',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/99.03*8.6','SigZprime15001200_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1200, T\'->Wb',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/86.28*0.27','SigZprime20001200_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->Wb',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/37.6*0.33','SigZprime25001200_tWb',allweightsystnames), 
                    
                    Sample('Z->tWb, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->Wb',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/95.06*0.80','SigZprime1500700_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->Wb',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/138.07*1.5','SigZprime1500900_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->Wb',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/55.83*0.21','SigZprime2000900_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->Wb',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/83.47*0.90','SigZprime20001500_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->Wb',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/53.9*0.29','SigZprime25001500_tWb',allweightsystnames),

                    Sample('Z->ttZ, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->tZ',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToZT*1500*1200*nominal*Tree.root',mcweight+'/285.1*3.1','SigZprime15001200_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1200, T\'->tZ',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1200*LH*nominal*Tree.root',mcweight+'/205.6*0.29','SigZprime20001200_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->tZ',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1200*nominal*Tree.root',mcweight+'/83.5*0.18','SigZprime25001200_ttZ',allweightsystnames), 
                    
                    Sample('Z->ttZ, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->tZ',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToZT*1500*700*nominal*Tree.root',mcweight+'/186.7*3.1','SigZprime1500700_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->tZ',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToZT*1500*900*nominal*Tree.root',mcweight+'/320.4*2.4','SigZprime1500900_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->tZ',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToZT*2000*900*nominal*Tree.root',mcweight+'/114.7*0.40','SigZprime2000900_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->tZ',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1500*nominal*Tree.root',mcweight+'/214.1*0.33','SigZprime20001500_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->tZ',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1500*nominal*Tree.root',mcweight+'/124.2*0.13','SigZprime25001500_ttZ',allweightsystnames),

                    Sample('Z->ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->tH',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToHT*1500*1200*nominal*Tree.root',mcweight+'/1.731*11.0','SigZprime15001200_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1200, T\'->tH',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1200*LH*nominal*Tree.root',mcweight+'/1.251*0.54','SigZprime20001200_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->tH',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1200*nominal*Tree.root',mcweight+'/0.511*0.26','SigZprime25001200_ttH',allweightsystnames), 
                    
                    Sample('Z->ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->tH',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToHT*1500*700*nominal*Tree.root',mcweight+'/3.62*3.5','SigZprime1500700_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->tH',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToHT*1500*900*nominal*Tree.root',mcweight+'/3.571*2.6','SigZprime1500900_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->tH',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToHT*2000*900*nominal*Tree.root',mcweight+'/1.305*0.56','SigZprime2000900_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->tH',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1500*nominal*Tree.root',mcweight+'/0.8246*0.59','SigZprime20001500_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->tH',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1500*nominal*Tree.root',mcweight+'/0.4775*0.22','SigZprime25001500_ttH',allweightsystnames),
    ]
else:
    SignalSamples=[


                    Sample('Z->tWb, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->Wb',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/99.03','SigZprime15001200_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1200, T\'->Wb',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/86.28','SigZprime20001200_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->Wb',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/37.6','SigZprime25001200_tWb',allweightsystnames), 
                    
                    Sample('Z->tWb, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->Wb',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/95.06','SigZprime1500700_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->Wb',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/138.07','SigZprime1500900_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->Wb',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/55.83','SigZprime2000900_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->Wb',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/83.47','SigZprime20001500_tWb',allweightsystnames),
                    Sample('Z->tWb, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->Wb',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/53.9','SigZprime25001500_tWb',allweightsystnames),

                    Sample('Z->ttZ, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->tZ',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToZT*1500*1200*nominal*Tree.root',mcweight+'/285.1','SigZprime15001200_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1200, T\'->tZ',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1200*LH*nominal*Tree.root',mcweight+'/205.6','SigZprime20001200_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->tZ',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1200*nominal*Tree.root',mcweight+'/83.5','SigZprime25001200_ttZ',allweightsystnames), 
                    
                    Sample('Z->ttZ, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->tZ',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToZT*1500*700*nominal*Tree.root',mcweight+'/186.7','SigZprime1500700_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->tZ',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToZT*1500*900*nominal*Tree.root',mcweight+'/320.4','SigZprime1500900_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->tZ',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToZT*2000*900*nominal*Tree.root',mcweight+'/114.7','SigZprime2000900_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->tZ',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1500*nominal*Tree.root',mcweight+'/214.1','SigZprime20001500_ttZ',allweightsystnames),
                    Sample('Z->ttZ, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->tZ',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1500*nominal*Tree.root',mcweight+'/124.2','SigZprime25001500_ttZ',allweightsystnames),

                    Sample('Z->ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->tH',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToHT*1500*1200*nominal*Tree.root',mcweight+'/1.731','SigZprime15001200_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1200, T\'->tH',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1200*LH*nominal*Tree.root',mcweight+'/1.251','SigZprime20001200_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->tH',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1200*nominal*Tree.root',mcweight+'/0.511','SigZprime25001200_ttH',allweightsystnames), 
                    
                    Sample('Z->ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->tH',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToHT*1500*700*nominal*Tree.root',mcweight+'/3.62','SigZprime1500700_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->tH',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToHT*1500*900*nominal*Tree.root',mcweight+'/3.571','SigZprime1500900_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->tH',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToHT*2000*900*nominal*Tree.root',mcweight+'/1.305','SigZprime2000900_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->tH',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1500*nominal*Tree.root',mcweight+'/0.8246','SigZprime20001500_ttH',allweightsystnames),
                    Sample('Z->ttH, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->tH',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1500*nominal*Tree.root',mcweight+'/0.4775','SigZprime25001500_ttH',allweightsystnames),





                    Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=1200, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/10000000','SigZprime15001200_'+BR_name+'',allweightsystnames),
                    Sample('Signal',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/10000000','SigZprime20001200_'+BR_name+'',allweightsystnames),
                    Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1200, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kRed,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/10000000','SigZprime25001200_'+BR_name+'',allweightsystnames), 
                    
                    Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/10000000','SigZprime1500700_'+BR_name+'',allweightsystnames),
                    Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=900, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/10000000','SigZprime1500900_'+BR_name+'',allweightsystnames),
                    Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=900, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/10000000','SigZprime2000900_'+BR_name+'',allweightsystnames),
                    Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=2000, m(T\'_{Nar,LH})=1500, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/10000000','SigZprime20001500_'+BR_name+'',allweightsystnames),
                    Sample('Z->tWb/ttZ/ttH, m(Z\'_{Nar})=2500, m(T\'_{Nar,LH})=1500, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/10000000','SigZprime25001500_'+BR_name+'',allweightsystnames),


    ]
    
    
if not doBR:
    BackgroundSamples=[

                    Sample('Top background',ROOT.kBlue,path_80x+'BKG_TTbar/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',allweightsystnames), 
                    Sample('single top (tW-channel)',ROOT.kBlue+2,path_80x+'BKG_ST/*ST*tW*nominal*.root',mcweight,'ST_tW',allweightsystnames),
                    Sample('single top (t-channel)',ROOT.kBlue-9,path_80x+'BKG_ST/*ST*t-channel*nominal*.root',mcweight,'ST_t',allweightsystnames),
                    Sample('single top (s-channel)',ROOT.kBlue-7,path_80x+'BKG_ST/*ST*s-channel*nominal*.root',mcweight,'ST_s',allweightsystnames),
                    Sample('QCDMadgraph',ROOT.kOrange-3,path_80x+'BKG_QCD/*QCD_H*nominal*.root',mcweight +'*'+DATA_MC_rate_scalefactor_QCD,'QCDMadgraph',allweightsystnames),
                    
                    Sample('Signal Contamination (8.6pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200, T\'->Wb',ROOT.kMagenta-3,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/99.03*8.6','SC_Zprime15001200_tWb_8_6pb',allweightsystnames),  
                    Sample('Signal Contamination (0.3pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200, T\'->Wb',ROOT.kCyan-3,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/86.28*0.3','SC_Zprime20001200_tWb_0_3pb',allweightsystnames),  
                    Sample('Signal Contamination (0.3pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200, T\'->Wb',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/37.6*0.3','SC_Zprime25001200_tWb_0_3pb',allweightsystnames),  
                    
                    Sample('Signal Contamination (0.8pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700, T\'->Wb',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/95.06*0.80','SC_Zprime1500700_tWb_0_8pb',allweightsystnames),  
                    Sample('Signal Contamination (1.5pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900, T\'->Wb',ROOT.kMagenta-8,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/138.07*1.5','SC_Zprime1500900_tWb_1_5pb',allweightsystnames),  
                    Sample('Signal Contamination (0.21pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900, T\'->Wb',ROOT.kCyan+1,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/55.83*0.21','SC_Zprime2000900_tWb_0_21pb',allweightsystnames),  
                    Sample('Signal Contamination (0.9pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500, T\'->Wb',ROOT.kCyan-7,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/83.47*0.90','SC_Zprime20001500_tWb_0_9pb',allweightsystnames),  
                    Sample('Signal Contamination (0.29pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500, T\'->Wb',ROOT.kRed-2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/53.9*0.29','SC_Zprime25001500_tWb_0_29pb',allweightsystnames),  
                    
                    Sample('Signal Contamination (3.1pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200, T\'->tZ',ROOT.kMagenta-3,path_80x+'Signal_Zprime/Zprime*ToZT*1500*1200*nominal*Tree.root',mcweight+'/285.1*3.1','SC_Zprime15001200_ttZ_3_1pb',allweightsystnames),  
                    Sample('Signal Contamination (0.29pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200, T\'->tZ',ROOT.kCyan-3,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1200*LH*nominal*Tree.root',mcweight+'/205.6*0.29','SC_Zprime20001200_ttZ_0_29pb',allweightsystnames),  
                    Sample('Signal Contamination (0.18pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200, T\'->tZ',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1200*nominal*Tree.root',mcweight+'/83.5*0.18','SC_Zprime25001200_ttZ_0_18pb',allweightsystnames),  
                    
                    Sample('Signal Contamination (3.1pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700, T\'->tZ',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Zprime*ToZT*1500*700*nominal*Tree.root',mcweight+'/186.7*3.1','SC_Zprime1500700_ttZ_3_1pb',allweightsystnames),  
                    Sample('Signal Contamination (2.4pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900, T\'->tZ',ROOT.kMagenta-8,path_80x+'Signal_Zprime/Zprime*ToZT*1500*900*nominal*Tree.root',mcweight+'/320.4*2.4','SC_Zprime1500900_ttZ_2_45pb',allweightsystnames),  
                    Sample('Signal Contamination (0.40pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900, T\'->tZ',ROOT.kCyan+1,path_80x+'Signal_Zprime/Zprime*ToZT*2000*900*nominal*Tree.root',mcweight+'/114.7*0.40','SC_Zprime2000900_ttZ_0_40pb',allweightsystnames),  
                    Sample('Signal Contamination (0.33pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500, T\'->tZ',ROOT.kCyan-7,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1500*nominal*Tree.root',mcweight+'/214.1*0.33','SC_Zprime20001500_ttZ_0_33pb',allweightsystnames),  
                    Sample('Signal Contamination (0.29pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500, T\'->tZ',ROOT.kRed-2,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1500*nominal*Tree.root',mcweight+'/124.2*0.13','SC_Zprime25001500_ttZ_0_29pb',allweightsystnames),  
                    
                    Sample('Signal Contamination (11.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200, T\'->tH',ROOT.kMagenta-3,path_80x+'Signal_Zprime/Zprime*ToHT*1500*1200*nominal*Tree.root',mcweight+'/1.731*11.0','SC_Zprime15001200_ttH_11_0pb',allweightsystnames),  
                    Sample('Signal Contamination (0.54pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200, T\'->tH',ROOT.kCyan-3,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1200*LH*nominal*Tree.root',mcweight+'/1.251*0.54','SC_Zprime20001200_ttH_0_54pb',allweightsystnames),  
                    Sample('Signal Contamination (0.26pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200, T\'->tH',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1200*nominal*Tree.root',mcweight+'/0.511*0.26','SC_Zprime25001200_ttH_0_26pb',allweightsystnames),  
                    
                    Sample('Signal Contamination (3.5pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700, T\'->tH',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Zprime*ToHT*1500*700*nominal*Tree.root',mcweight+'/3.62*3.5','SC_Zprime1500700_ttH_3_58pb',allweightsystnames),  
                    Sample('Signal Contamination (2.6pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900, T\'->tH',ROOT.kMagenta-8,path_80x+'Signal_Zprime/Zprime*ToHT*1500*900*nominal*Tree.root',mcweight+'/3.571*2.6','SC_Zprime1500900_ttH_2_6pb',allweightsystnames),  
                    Sample('Signal Contamination (0.56pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900, T\'->tH',ROOT.kCyan+1,path_80x+'Signal_Zprime/Zprime*ToHT*2000*900*nominal*Tree.root',mcweight+'/1.305*0.56','SC_Zprime2000900_ttH_0_56pb',allweightsystnames),  
                    Sample('Signal Contamination (0.59pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500, T\'->tH',ROOT.kCyan-7,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1500*nominal*Tree.root',mcweight+'/0.8246*0.59','SC_Zprime20001500_ttH_0_59pb',allweightsystnames),  
                    Sample('Signal Contamination (0.22pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500, T\'->tH',ROOT.kRed-2,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1500*nominal*Tree.root',mcweight+'/0.4775*0.22','SC_Zprime25001500_ttH_0_22pb',allweightsystnames), 
                  
                    Sample('Signal Contamination none',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/10000000','SC_none',allweightsystnames),  
                    #Sample('QCDPythia8',ROOT.kGreen+2,path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root',mcweight,'QCDPythia8',allweightsystnames),                    
    ]
    
else:
    BackgroundSamples=[

                    Sample('Top background',ROOT.kBlue,path_80x+'BKG_TTbar/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',allweightsystnames), 
                    Sample('single top (tW-channel)',ROOT.kBlue+2,path_80x+'BKG_ST/*ST*tW*nominal*.root',mcweight,'ST_tW',allweightsystnames),
                    Sample('single top (t-channel)',ROOT.kBlue-9,path_80x+'BKG_ST/*ST*t-channel*nominal*.root',mcweight,'ST_t',allweightsystnames),
                    Sample('single top (s-channel)',ROOT.kBlue-7,path_80x+'BKG_ST/*ST*s-channel*nominal*.root',mcweight,'ST_s',allweightsystnames),
                    Sample('QCD from ABCD',ROOT.kOrange-3,path_80x+'BKG_QCD/*QCD_H*nominal*Tree*.root',mcweight,'QCDMadgraph',allweightsystnames),
                        

                    Sample('Signal Contamination',ROOT.kMagenta-3,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/99.03','SC_Zprime15001200_tWb_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan-3,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/86.28','SC_Zprime20001200_tWb_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/37.6','SC_Zprime25001200_tWb_1_0pb',allweightsystnames),  
                    
                    Sample('Signal Contamination',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/95.06','SC_Zprime1500700_tWb_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kMagenta-8,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/138.07','SC_Zprime1500900_tWb_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan+1,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/55.83','SC_Zprime2000900_tWb_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan-7,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/83.47','SC_Zprime20001500_tWb_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kRed-2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/53.9','SC_Zprime25001500_tWb_1_0pb',allweightsystnames),  
                    
                    Sample('Signal Contamination',ROOT.kMagenta-3,path_80x+'Signal_Zprime/Zprime*ToZT*1500*1200*nominal*Tree.root',mcweight+'/285.1','SC_Zprime15001200_ttZ_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan-3,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1200*LH*nominal*Tree.root',mcweight+'/205.6','SC_Zprime20001200_ttZ_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1200*nominal*Tree.root',mcweight+'/83.5','SC_Zprime25001200_ttZ_1_0pb',allweightsystnames),  
                    
                    Sample('Signal Contamination',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Zprime*ToZT*1500*700*nominal*Tree.root',mcweight+'/186.7','SC_Zprime1500700_ttZ_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kMagenta-8,path_80x+'Signal_Zprime/Zprime*ToZT*1500*900*nominal*Tree.root',mcweight+'/320.4','SC_Zprime1500900_ttZ_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan+1,path_80x+'Signal_Zprime/Zprime*ToZT*2000*900*nominal*Tree.root',mcweight+'/114.7','SC_Zprime2000900_ttZ_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan-7,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1500*nominal*Tree.root',mcweight+'/214.1','SC_Zprime20001500_ttZ_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kRed-2,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1500*nominal*Tree.root',mcweight+'/124.2','SC_Zprime25001500_ttZ_1_0pb',allweightsystnames),  
                    
                    Sample('Signal Contamination',ROOT.kMagenta-3,path_80x+'Signal_Zprime/Zprime*ToHT*1500*1200*nominal*Tree.root',mcweight+'/1.731','SC_Zprime15001200_ttH_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan-3,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1200*LH*nominal*Tree.root',mcweight+'/1.251','SC_Zprime20001200_ttH_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1200*nominal*Tree.root',mcweight+'/0.511','SC_Zprime25001200_ttH_1_0pb',allweightsystnames),  
                    
                    Sample('Signal Contamination',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Zprime*ToHT*1500*700*nominal*Tree.root',mcweight+'/3.62','SC_Zprime1500700_ttH_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kMagenta-8,path_80x+'Signal_Zprime/Zprime*ToHT*1500*900*nominal*Tree.root',mcweight+'/3.571','SC_Zprime1500900_ttH_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan+1,path_80x+'Signal_Zprime/Zprime*ToHT*2000*900*nominal*Tree.root',mcweight+'/1.305','SC_Zprime2000900_ttH_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan-7,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1500*nominal*Tree.root',mcweight+'/0.8246','SC_Zprime20001500_ttH_1_0pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kRed-2,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1500*nominal*Tree.root',mcweight+'/0.4775','SC_Zprime25001500_ttH_1_0pb',allweightsystnames),  



                    Sample('Signal Contamination',ROOT.kMagenta-3,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/10000000','SC_Zprime15001200_'+BR_name+'_1pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan-3,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/10000000','SC_Zprime20001200_'+BR_name+'_1pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/10000000','SC_Zprime25001200_'+BR_name+'_1pb',allweightsystnames),  
                    
                    Sample('Signal Contamination',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/10000000','SC_Zprime1500700_'+BR_name+'_1pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kMagenta-8,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/10000000','SC_Zprime1500900_'+BR_name+'_1pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan+1,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/10000000','SC_Zprime2000900_'+BR_name+'_1pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kCyan-7,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/10000000','SC_Zprime20001500_'+BR_name+'_1pb',allweightsystnames),  
                    Sample('Signal Contamination',ROOT.kRed-2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/10000000','SC_Zprime25001500_'+BR_name+'_1pb',allweightsystnames),
                    
                  
                    Sample('Signal Contamination',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/10000000','SC_none',allweightsystnames),  
                    #Sample('QCDPythia8',ROOT.kGreen+2,path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root',mcweight,'QCDPythia8',allweightsystnames),

    ]

if not doBR:
    
    DataSamples=[
                    Sample('Data = Background with (8.6pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/99.03*8.6','DATA_Zprime15001200_tWb_8_6pb',allweightsystnames),     
                    Sample('Data = Background with (0.3pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/86.28*0.3','DATA_Zprime20001200_tWb_0_3pb',allweightsystnames),     
                    Sample('Data = Background with (0.3pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/37.6*0.3','DATA_Zprime25001200_tWb_0_3pb',allweightsystnames),    
                    
                    Sample('Data = Background with (0.8pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/95.06*0.80','DATA_Zprime1500700_tWb_0_8pb',allweightsystnames),  
                    Sample('Data = Background with (1.5pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/138.07*1.5','DATA_Zprime1500900_tWb_1_5pb',allweightsystnames),  
                    Sample('Data = Background with (0.21pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/55.83*0.21','DATA_Zprime2000900_tWb_0_21pb',allweightsystnames),  
                    Sample('Data = Background with (0.9pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/83.47*0.90','DATA_Zprime20001500_tWb_0_9pb',allweightsystnames),  
                    Sample('Data = Background with (0.29pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/53.9*0.29','DATA_Zprime25001500_tWb_0_29pb',allweightsystnames),  
                    
                    Sample('Data = Background with (3.pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*1500*1200*nominal*Tree.root',mcweight+'/285.1*3.1','DATA_Zprime15001200_ttZ_3_pb',allweightsystnames),     
                    Sample('Data = Background with (0.29pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1200*LH*nominal*Tree.root',mcweight+'/205.6*0.29','DATA_Zprime20001200_ttZ_0_29pb',allweightsystnames),     
                    Sample('Data = Background with (0.18pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1200*nominal*Tree.root',mcweight+'/83.5*0.18','DATA_Zprime25001200_ttZ_0_18pb',allweightsystnames),    
                    
                    Sample('Data = Background with (3.1pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*1500*700*nominal*Tree.root',mcweight+'/186.7*3.1','DATA_Zprime1500700_ttZ_3_1pb',allweightsystnames),  
                    Sample('Data = Background with (2.4pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*1500*900*nominal*Tree.root',mcweight+'/320.4*2.4','DATA_Zprime1500900_ttZ_2_4pb',allweightsystnames),  
                    Sample('Data = Background with (0.40pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*2000*900*nominal*Tree.root',mcweight+'/114.7*0.40','DATA_Zprime2000900_ttZ_0_401pb',allweightsystnames),  
                    Sample('Data = Background with (0.33pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1500*nominal*Tree.root',mcweight+'/214.1*0.33','DATA_Zprime20001500_ttZ_0_33pb',allweightsystnames),  
                    Sample('Data = Background with (0.13pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1500*nominal*Tree.root',mcweight+'/124.2*0.13','DATA_Zprime25001500_ttZ_0_13pb',allweightsystnames),  
                    
                    Sample('Data = Background with (11.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*1500*1200*nominal*Tree.root',mcweight+'/1.731*11.0','DATA_Zprime15001200_ttH_11_0pb',allweightsystnames),     
                    Sample('Data = Background with (0.54pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1200*LH*nominal*Tree.root',mcweight+'/1.251*0.54','DATA_Zprime20001200_ttH_0_54pb',allweightsystnames),     
                    Sample('Data = Background with (0.26pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1200*nominal*Tree.root',mcweight+'/0.511*0.26','DATA_Zprime25001200_ttH_0_26pb',allweightsystnames),    
                    
                    Sample('Data = Background with (3.5pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*1500*700*nominal*Tree.root',mcweight+'/3.62*3.5','DATA_Zprime1500700_ttH_3_5pb',allweightsystnames),  
                    Sample('Data = Background with (2.6pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*1500*900*nominal*Tree.root',mcweight+'/3.571*2.6','DATA_Zprime1500900_ttH_2_6pb',allweightsystnames),  
                    Sample('Data = Background with (0.56pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*2000*900*nominal*Tree.root',mcweight+'/1.305*0.56','DATA_Zprime2000900_ttH_0_56pb',allweightsystnames),  
                    Sample('Data = Background with (0.59pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1500*nominal*Tree.root',mcweight+'/0.8246*0.59','DATA_Zprime20001500_ttH_0_59pb',allweightsystnames),  
                    Sample('Data = Background with (0.22pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1500*nominal*Tree.root',mcweight+'/0.4775*0.22','DATA_Zprime25001500_ttH_0_22pb',allweightsystnames),
                    
                    Sample('Data = Background with no signal',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/100000.0','DATA_noSignal',allweightsystnames) ,     
    ]
else:
    DataSamples=[
                
         
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/99.03','DATA_Zprime15001200_tWb_1_0pb',allweightsystnames),     
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/86.28','DATA_Zprime20001200_tWb_1_0pb',allweightsystnames),     
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/37.6','DATA_Zprime25001200_tWb_1_0pb',allweightsystnames),    
                    
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/95.06','DATA_Zprime1500700_tWb_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/138.07','DATA_Zprime1500900_tWb_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/55.83','DATA_Zprime2000900_tWb_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/83.47','DATA_Zprime20001500_tWb_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500, T\'->Wb',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/53.9','DATA_Zprime25001500_tWb_1_0pb',allweightsystnames),  
                    
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*1500*1200*nominal*Tree.root',mcweight+'/285.1','DATA_Zprime15001200_ttZ_1_0pb',allweightsystnames),     
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1200*LH*nominal*Tree.root',mcweight+'/205.6','DATA_Zprime20001200_ttZ_1_0pb',allweightsystnames),     
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1200*nominal*Tree.root',mcweight+'/83.5','DATA_Zprime25001200_ttZ_1_0pb',allweightsystnames),    
                    
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*1500*700*nominal*Tree.root',mcweight+'/186.7','DATA_Zprime1500700_ttZ_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*1500*900*nominal*Tree.root',mcweight+'/320.4','DATA_Zprime1500900_ttZ_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*2000*900*nominal*Tree.root',mcweight+'/114.7','DATA_Zprime2000900_ttZ_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*2000*1500*nominal*Tree.root',mcweight+'/214.1','DATA_Zprime20001500_ttZ_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500, T\'->tZ',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToZT*2500*1500*nominal*Tree.root',mcweight+'/124.2','DATA_Zprime25001500_ttZ_1_0pb',allweightsystnames),  
                    
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*1500*1200*nominal*Tree.root',mcweight+'/1.731','DATA_Zprime15001200_ttH_1_0pb',allweightsystnames),     
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1200*LH*nominal*Tree.root',mcweight+'/1.251','DATA_Zprime20001200_ttH_1_0pb',allweightsystnames),     
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1200*nominal*Tree.root',mcweight+'/0.511','DATA_Zprime25001200_ttH_1_0pb',allweightsystnames),    
                    
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*1500*700*nominal*Tree.root',mcweight+'/3.62','DATA_Zprime1500700_ttH_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*1500*900*nominal*Tree.root',mcweight+'/3.571','DATA_Zprime1500900_ttH_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*2000*900*nominal*Tree.root',mcweight+'/1.305','DATA_Zprime2000900_ttH_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*2000*1500*nominal*Tree.root',mcweight+'/0.8246','DATA_Zprime20001500_ttH_1_0pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500, T\'->tH',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToHT*2500*1500*nominal*Tree.root',mcweight+'/0.4775','DATA_Zprime25001500_ttH_1_0pb',allweightsystnames),  
                  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*1200*nominal*Tree.root',mcweight+'/10000000','DATA_Zprime15001200_'+BR_name+'_1pb',allweightsystnames),     
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1200*LH*nominal*Tree.root',mcweight+'/10000000','DATA_Zprime20001200_'+BR_name+'_1pb',allweightsystnames),     
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/10000000','DATA_Zprime25001200_'+BR_name+'_1pb',allweightsystnames),    
                    
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/10000000','DATA_Zprime1500700_'+BR_name+'_1pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*1500*900*nominal*Tree.root',mcweight+'/10000000','DATA_Zprime1500900_'+BR_name+'_1pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*900*nominal*Tree.root',mcweight+'/10000000','DATA_Zprime2000900_'+BR_name+'_1pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2000*1500*nominal*Tree.root',mcweight+'/10000000','DATA_Zprime20001500_'+BR_name+'_1pb',allweightsystnames),  
                    Sample('Data = Background with (1.0pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500, T\'->bW/tZ/tH, BR=0.5,0.25,0.25',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1500*nominal*Tree.root',mcweight+'/10000000','DATA_Zprime25001500_'+BR_name+'_1pb',allweightsystnames),  
                    
                    Sample('Data = Background with no signal',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/100000.0','DATA_noSignal',allweightsystnames) ,     
                  
                   
                    #Sample('Data = Background with (1pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kBlack,path_80x+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight+'/86.28*0.3','BKG_Zprime20001200_1pb') ,     
                    #Sample('Data = Background with (1pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kBlack,path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight+'/138.07*0.3','BKG_Zprime1500900_1pb') ,     

    ]



expectedSignals=[8.6,0.27,0.33,0.8,1.5,0.21,0.9,0.29]+[3.1,0.29,0.18,3.1,2.4,0.4,0.33,0.13]+[11,0.54,0.26,3.5,2.6,0.56,0.59,0.22]+[8.6,0.27,0.33,0.8,1.5,0.21,0.9,0.29]


#samplenames=[]
#for i in samples:
    #samplenames.append(i.nick)
SignalSampleNames=[]
for i in SignalSamples:
    SignalSampleNames.append(i.nick)
BackgroundSampleNames=[]
for i in BackgroundSamples:
    BackgroundSampleNames.append(i.nick)
DataSampleNames=[]
for i in DataSamples:
    DataSampleNames.append(i.nick)
  
samples=SignalSamples+BackgroundSamples+DataSamples

samplenames=SignalSampleNames+BackgroundSampleNames+DataSampleNames




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


