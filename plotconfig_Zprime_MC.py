import sys
import os
from scriptgenerator import *
from plotutils import *
from plot_cuts_ZPrime_MC import *

weigthsystnamesbasic=[
                    "",
                    "_no_nominal",
                    "_no_systup",
                    "_no_systdown",
]
systweightsbasic=[
                    "nom:=1",
                    "no_nominal:=1.0",
                    "no_systup:=1.0",
                    "no_systdown:=1.0",
  
]
    
    
weightsystnamesMadgraphbantiZprimeM=[
                    #"",
                    "_ABMadgraphbantiZprimeM_nominal",
                    "_ABMadgraphbantiZprimeM_systup",
                    "_ABMadgraphbantiZprimeM_systdown",
] 

systweightsMadgraphbantiZprimeM=[
                    #"nom:=1",
                    #"ABMadgraphbantiZprimeM_nominal:=2",
                    "ABMadgraphbantiZprimeM_nominal:=QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M",
                    ##"ABMadgraphbantiZprimeM_nominal:=2*(DoWeights==1)+(DoWeights==0)*1.0",
                    "ABMadgraphbantiZprimeM_systup:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systup)",
                    "ABMadgraphbantiZprimeM_systdown:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systdown)",
]


weightsystnamesPythia8bantiZprimeM=[
                    "_ABPythiabantiZprimeM_nominal",
                    "_ABPythiabantiZprimeM_systup",
                    "_ABPythiabantiZprimeM_systdown",
] 

systweightsPythia8bantiZprimeM=[
                    "ABPythiabantiZprimeM_nominal:=QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M",
                    "ABPythiabantiZprimeM_systup:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systup)",
                    "ABPythiabantiZprimeM_systdown:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systdown)",
]
 
weightsystnamesGeneratorDiffMadgraphbantiZprimeM=[
                    "_ABMadgraphbantiZprimeMGeneratorDiff_systup",
                    "_ABMadgraphbantiZprimeMGeneratorDiff_systdown",
]

systweightsGeneartorDiffMadgraphbantiZprimeM=[
                    "ABMadgraphbantiZprimeMGeneratorDiff_systup:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))",
                    "ABMadgraphbantiZprimeMGeneratorDiff_systdown:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))",
]
 
weightsystnamesGeneratorDiffPythia8bantiZprimeM=[
                    "_ABPythiabantiZprimeMGeneratorDiff_systup",
                    "_ABPythiabantiZprimeMGeneratorDiff_systdown",
]

systweightsGeneartorDiffPythia8bantiZprimeM=[
                    "ABPythiabantiZprimeMGeneratorDiff_systup:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))",
                    "ABPythiabantiZprimeMGeneratorDiff_systdown:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))",
]
    
 
weightsystnamesMadgraphtantiTopPt=[
                    "_ABMadgraphtantiTopPt_nominal",
                    "_ABMadgraphtantiTopPt_systup",
                    "_ABMadgraphtantiTopPt_systdown",
] 

systweightsMadgraphtantiTopPt=[
                    "ABMadgraphtantiTopPt_nominal:=QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt",
                    "ABMadgraphtantiTopPt_systup:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt+QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systup)",
                    "ABMadgraphtantiTopPt_systdown:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systdown)",
]


weightsystnamesPythia8tantiTopPt=[
                    "_ABPythiatantiTopPt_nominal",
                    "_ABPythiatantiTopPt_systup",
                    "_ABPythiatantiTopPt_systdown",
] 

systweightsPythia8tantiTopPt=[
                    "ABPythiatantiTopPt_nominal:=QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt",
                    "ABPythiatantiTopPt_systup:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt + QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systup)",
                    "ABPythiatantiTopPt_systdown:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt - QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systdown)",
]

weightsystnamesGeneratorDiffMadgraphtantiTopPt=[
                    "_ABMadgraphtantiTopPtGeneratorDiff_systup",
                    "_ABMadgraphtantiTopPtGeneratorDiff_systdown",
]

systweightsGeneartorDiffMadgraphtantiTopPt=[
                    "ABMadgraphtantiTopPtGeneratorDiff_systup:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt + abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))",
                    "ABMadgraphtantiTopPtGeneratorDiff_systdown:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt - abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))",
]
 
weightsystnamesGeneratorDiffPythia8tantiTopPt=[
                    "_ABPythiatantiTopPtGeneratorDiff_systup",
                    "_ABPythiatantiTopPtGeneratorDiff_systdown",
]

systweightsGeneartorDiffPythia8tantiTopPt=[
                    "ABPythiatantiTopPtGeneratorDiff_systup:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt+ abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))",
                    "ABPythiatantiTopPtGeneratorDiff_systdown:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt- abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))",
]




#########################################################################
  
    
weightsystnamesMadgraphbantiZprimeMWithtopbtag=[
                    "_ABMadgraphbantiZprimeMWithtopbtag_nominal",
                    "_ABMadgraphbantiZprimeMWithtopbtag_systup",
                    "_ABMadgraphbantiZprimeMWithtopbtag_systdown",
] 
systweightsMadgraphbantiZprimeMWithtopbtag=[
                    #"ABMadgraphbantiZprimeMWithtopbtag_nominal:=2",
                    "ABMadgraphbantiZprimeMWithtopbtag_nominal:=QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M",
                    ##"ABMadgraphbantiZprimeMWithtopbtag_nominal:=2*(DoWeights==1)+(DoWeights==0)*1.0",
                    "ABMadgraphbantiZprimeMWithtopbtag_systup:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systup)",
                    "ABMadgraphbantiZprimeMWithtopbtag_systdown:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systdown)",
]


weightsystnamesPythia8bantiZprimeMWithtopbtag=[
                    "_ABPythiabantiZprimeMWithtopbtag_nominal",
                    "_ABPythiabantiZprimeMWithtopbtag_systup",
                    "_ABPythiabantiZprimeMWithtopbtag_systdown",
] 
systweightsPythia8bantiZprimeMWithtopbtag=[
                    "ABPythiabantiZprimeMWithtopbtag_nominal:=QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M",
                    "ABPythiabantiZprimeMWithtopbtag_systup:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systup)",
                    "ABPythiabantiZprimeMWithtopbtag_systdown:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systdown)",
]
 
weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag=[
                    "_ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systup",
                    "_ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systdown",
]

systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag=[
                    "ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systup:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))",
                    "ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systdown:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))",
]
 
weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag=[
                    "_ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systup",
                    "_ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systdown",
]

systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag=[
                    "ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systup:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))",
                    "ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systdown:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))",
]
    
 
weightsystnamesMadgraphtantiTopPtWithtopbtag=[
                    "_ABMadgraphtantiTopPtWithtopbtag_nominal",
                    "_ABMadgraphtantiTopPtWithtopbtag_systup",
                    "_ABMadgraphtantiTopPtWithtopbtag_systdown",
] 

systweightsMadgraphtantiTopPtWithtopbtag=[
                    "ABMadgraphtantiTopPtWithtopbtag_nominal:=QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt",
                    "ABMadgraphtantiTopPtWithtopbtag_systup:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt+QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systup)",
                    "ABMadgraphtantiTopPtWithtopbtag_systdown:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systdown)",
]


weightsystnamesPythia8tantiTopPtWithtopbtag=[
                    "_ABPythiatantiTopPtWithtopbtag_nominal",
                    "_ABPythiatantiTopPtWithtopbtag_systup",
                    "_ABPythiatantiTopPtWithtopbtag_systdown",
] 

systweightsPythia8tantiTopPtWithtopbtag=[
                    "ABPythiatantiTopPtWithtopbtag_nominal:=QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt",
                    "ABPythiatantiTopPtWithtopbtag_systup:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt + QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systup)",
                    "ABPythiatantiTopPtWithtopbtag_systdown:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt - QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systdown)",
]

weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag=[
                    "_ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systup",
                    "_ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systdown",
]

systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag=[
                    "ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systup:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt + abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))",
                    "ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systdown:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt - abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))",
]
 
weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag=[
                    "_ABPythiatantiTopPtWithtopbtagGeneratorDiff_systup",
                    "_ABPythiatantiTopPtWithtopbtagGeneratorDiff_systdown",
]

systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag=[
                    "ABPythiatantiTopPtWithtopbtagGeneratorDiff_systup:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt+ abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))",
                    "ABPythiatantiTopPtWithtopbtagGeneratorDiff_systdown:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt- abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))",
]

if topWP=='loose' and WWP=='loose' and bottomWP=='medium':


    weightsystnamesABCD=[
                    #"",
                    "_ABCD_nominal",
                    
                    "_ABCD_inclusive_ZprimeM_systup",
                    "_ABCD_inclusive_ZprimeM_systdown",
                    "_ABCD_notopbtag_ZprimeM_systup",
                    "_ABCD_notopbtag_ZprimeM_systdown",
                    "_ABCD_withtopbtag_ZprimeM_systup",
                    "_ABCD_withtopbtag_ZprimeM_systdown",
                    "_ABCD_inclusive_TprimeM_systup",
                    "_ABCD_inclusive_TprimeM_systdown",
                    "_ABCD_notopbtag_TprimeM_systup",
                    "_ABCD_notopbtag_TprimeM_systdown",
                    "_ABCD_withtopbtag_TprimeM_systup",
                    "_ABCD_withtopbtag_TprimeM_systdown",
                    
                    #"_ABCDcorrE_inclusive_ZprimeM_systup",
                    #"_ABCDcorrE_inclusive_ZprimeM_systdown",
                    #"_ABCDcorrE_notopbtag_ZprimeM_systup",
                    #"_ABCDcorrE_notopbtag_ZprimeM_systdown",
                    #"_ABCDcorrE_withtopbtag_ZprimeM_systup",
                    #"_ABCDcorrE_withtopbtag_ZprimeM_systdown",
                    #"_ABCDcorrE_inclusive_TprimeM_systup",
                    #"_ABCDcorrE_inclusive_TprimeM_systdown",
                    #"_ABCDcorrE_notopbtag_TprimeM_systup",
                    #"_ABCDcorrE_notopbtag_TprimeM_systdown",
                    #"_ABCDcorrE_withtopbtag_TprimeM_systup",
                    #"_ABCDcorrE_withtopbtag_TprimeM_systdown",
                    
                    "_ABCD2_inclusive_ZprimeM_systup",
                    "_ABCD2_inclusive_ZprimeM_systdown",
                    "_ABCD2_notopbtag_ZprimeM_systup",
                    "_ABCD2_notopbtag_ZprimeM_systdown",
                    "_ABCD2_withtopbtag_ZprimeM_systup",
                    "_ABCD2_withtopbtag_ZprimeM_systdown",
                    "_ABCD2_inclusive_TprimeM_systup",
                    "_ABCD2_inclusive_TprimeM_systdown",
                    "_ABCD2_notopbtag_TprimeM_systup",
                    "_ABCD2_notopbtag_TprimeM_systdown",
                    "_ABCD2_withtopbtag_TprimeM_systup",
                    "_ABCD2_withtopbtag_TprimeM_systdown",

                    #"_ABCD2corrE_inclusive_ZprimeM_systup",
                    #"_ABCD2corrE_inclusive_ZprimeM_systdown",
                    #"_ABCD2corrE_notopbtag_ZprimeM_systup",
                    #"_ABCD2corrE_notopbtag_ZprimeM_systdown",
                    #"_ABCD2corrE_withtopbtag_ZprimeM_systup",
                    #"_ABCD2corrE_withtopbtag_ZprimeM_systdown",
                    #"_ABCD2corrE_inclusive_TprimeM_systup",
                    #"_ABCD2corrE_inclusive_TprimeM_systdown",
                    #"_ABCD2corrE_notopbtag_TprimeM_systup",
                    #"_ABCD2corrE_notopbtag_TprimeM_systdown",
                    #"_ABCD2corrE_withtopbtag_TprimeM_systup",
                    #"_ABCD2corrE_withtopbtag_TprimeM_systdown",      


]
else:
    weightsystnamesABCD=[
                    #"",
                    "_ABCD_nominal",
                    
                    "_ABCD_inclusive_ZprimeM_systup",
                    "_ABCD_inclusive_ZprimeM_systdown",
                    "_ABCD_notopbtag_ZprimeM_systup",
                    "_ABCD_notopbtag_ZprimeM_systdown",
                    "_ABCD_withtopbtag_ZprimeM_systup",
                    "_ABCD_withtopbtag_ZprimeM_systdown",
                    "_ABCD_inclusive_TprimeM_systup",
                    "_ABCD_inclusive_TprimeM_systdown",
                    "_ABCD_notopbtag_TprimeM_systup",
                    "_ABCD_notopbtag_TprimeM_systdown",
                    "_ABCD_withtopbtag_TprimeM_systup",
                    "_ABCD_withtopbtag_TprimeM_systdown",
                    
                    #"_ABCDcorrE_inclusive_ZprimeM_systup",
                    #"_ABCDcorrE_inclusive_ZprimeM_systdown",
                    #"_ABCDcorrE_notopbtag_ZprimeM_systup",
                    #"_ABCDcorrE_notopbtag_ZprimeM_systdown",
                    #"_ABCDcorrE_withtopbtag_ZprimeM_systup",
                    #"_ABCDcorrE_withtopbtag_ZprimeM_systdown",
                    #"_ABCDcorrE_inclusive_TprimeM_systup",
                    #"_ABCDcorrE_inclusive_TprimeM_systdown",
                    #"_ABCDcorrE_notopbtag_TprimeM_systup",
                    #"_ABCDcorrE_notopbtag_TprimeM_systdown",
                    #"_ABCDcorrE_withtopbtag_TprimeM_systup",
                    #"_ABCDcorrE_withtopbtag_TprimeM_systdown",
                    
                    "_ABCD2_inclusive_ZprimeM_systup",
                    "_ABCD2_inclusive_ZprimeM_systdown",
                    "_ABCD2_notopbtag_ZprimeM_systup",
                    "_ABCD2_notopbtag_ZprimeM_systdown",
                    "_ABCD2_withtopbtag_ZprimeM_systup",
                    "_ABCD2_withtopbtag_ZprimeM_systdown",
                    "_ABCD2_inclusive_TprimeM_systup",
                    "_ABCD2_inclusive_TprimeM_systdown",
                    "_ABCD2_notopbtag_TprimeM_systup",
                    "_ABCD2_notopbtag_TprimeM_systdown",
                    "_ABCD2_withtopbtag_TprimeM_systup",
                    "_ABCD2_withtopbtag_TprimeM_systdown",

                    #"_ABCD2corrE_inclusive_ZprimeM_systup",
                    #"_ABCD2corrE_inclusive_ZprimeM_systdown",
                    #"_ABCD2corrE_notopbtag_ZprimeM_systup",
                    #"_ABCD2corrE_notopbtag_ZprimeM_systdown",
                    #"_ABCD2corrE_withtopbtag_ZprimeM_systup",
                    #"_ABCD2corrE_withtopbtag_ZprimeM_systdown",
                    #"_ABCD2corrE_inclusive_TprimeM_systup",
                    #"_ABCD2corrE_inclusive_TprimeM_systdown",
                    #"_ABCD2corrE_notopbtag_TprimeM_systup",
                    #"_ABCD2corrE_notopbtag_TprimeM_systdown",
                    #"_ABCD2corrE_withtopbtag_TprimeM_systup",
                    #"_ABCD2corrE_withtopbtag_TprimeM_systdown",      


]    
    
    
    
if topWP=='loose' and WWP=='loose' and bottomWP=='medium':
    
      systweightsABCD=[
                    #"nom:=1",
                    
                    
#########medium working points                    
                    
                    "ABCD_nominal:= 1",
 

###########loose working points
                    "ABCD_inclusive_ZprimeM_systup:= pow(1+0.024348,1.0/1.0)",
                    "ABCD_inclusive_ZprimeM_systdown:= pow(1-0.024348,1.0/1.0)",
                    "ABCD_notopbtag_ZprimeM_systup:= pow(1+0.018073,1.0/1.0)",
                    "ABCD_notopbtag_ZprimeM_systdown:= pow(1-0.018073,1.0/1.0)",
                    "ABCD_withtopbtag_ZprimeM_systup:= pow(1+0.144325,1.0/1.0)",
                    "ABCD_withtopbtag_ZprimeM_systdown:= pow(1-0.144325,1.0/1.0)",
                    "ABCD_inclusive_TprimeM_systup:= pow(1+0.027596,1.0/1.0)",
                    "ABCD_inclusive_TprimeM_systdown:= pow(1-0.027596,1.0/1.0)",
                    "ABCD_notopbtag_TprimeM_systup:= pow(1+0.021271,1.0/1.0)",
                    "ABCD_notopbtag_TprimeM_systdown:= pow(1-0.021271,1.0/1.0)",
                    "ABCD_withtopbtag_TprimeM_systup:= pow(1+0.259112,1.0/1.0)",
                    "ABCD_withtopbtag_TprimeM_systdown:= pow(1-0.259112,1.0/1.0)",

                    #"ABCDcorrE_inclusive_ZprimeM_systup:= pow(1+0.015,1.0/1.0)",
                    #"ABCDcorrE_inclusive_ZprimeM_systdown:= pow(1-0.015,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_ZprimeM_systup:= pow(1+0.02,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_ZprimeM_systdown:= pow(1-0.02,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_ZprimeM_systup:= pow(1+0.3,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_ZprimeM_systdown:= pow(1-0.3,1.0/1.0)",
                    #"ABCDcorrE_inclusive_TprimeM_systup:= pow(1+0.005,1.0/1.0)",
                    #"ABCDcorrE_inclusive_TprimeM_systdown:= pow(1-0.005,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_TprimeM_systup:= pow(1+0.02,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_TprimeM_systdown:= pow(1-0.02,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_TprimeM_systup:= pow(1+0.6,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_TprimeM_systdown:= pow(1-0.6,1.0/1.0)",
                    
                    "ABCD2_inclusive_ZprimeM_systup:= pow(1+0.01874,1.0/1.0)",
                    "ABCD2_inclusive_ZprimeM_systdown:= pow(1-0.01874,1.0/1.0)",
                    "ABCD2_notopbtag_ZprimeM_systup:= pow(1+0.01194,1.0/1.0)",
                    "ABCD2_notopbtag_ZprimeM_systdown:= pow(1-0.01194,1.0/1.0)",
                    "ABCD2_withtopbtag_ZprimeM_systup:= pow(1+0.063702,1.0/1.0)",
                    "ABCD2_withtopbtag_ZprimeM_systdown:= pow(1-0.063702,1.0/1.0)",
                    "ABCD2_inclusive_TprimeM_systup:= pow(1+0.01731,1.0/1.0)",
                    "ABCD2_inclusive_TprimeM_systdown:= pow(1-0.01731,1.0/1.0)",
                    "ABCD2_notopbtag_TprimeM_systup:= pow(1+0.01194,1.0/1.0)",
                    "ABCD2_notopbtag_TprimeM_systdown:= pow(1-0.01194,1.0/1.0)",
                    "ABCD2_withtopbtag_TprimeM_systup:= pow(1+0.082416,1.0/1.0)",
                    "ABCD2_withtopbtag_TprimeM_systdown:= pow(1-0.082416,1.0/1.0)",
                                        
                    #"ABCD2corrE_inclusive_ZprimeM_systup:= pow(1+0.015,1.0/1.0)",
                    #"ABCD2corrE_inclusive_ZprimeM_systdown:= pow(1-0.015,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_ZprimeM_systup:= pow(1+0.025,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_ZprimeM_systdown:= pow(1-0.025,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_ZprimeM_systup:= pow(1+0.02,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_ZprimeM_systdown:= pow(1-0.02,1.0/1.0)",
                    #"ABCD2corrE_inclusive_TprimeM_systup:= pow(1+0.01,1.0/1.0)",
                    #"ABCD2corrE_inclusive_TprimeM_systdown:= pow(1-0.01,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_TprimeM_systup:= pow(1+0.025,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_TprimeM_systdown:= pow(1-0.025,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_TprimeM_systup:= pow(1+0.005,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_TprimeM_systdown:= pow(1-0.005,1.0/1.0)",
                                        
################otherstuff
                    #"ABCD_inclusive_ZprimeM_systup:= 1+0.06*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCD_inclusive_ZprimeM_systdown:= 1-0.06*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",  
                    #"ABCD_notopbtag_ZprimeM_systup:= 1+0.08*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD_notopbtag_ZprimeM_systdown:= 1-0.08*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD_withtopbtag_ZprimeM_systup:= 1+0.35*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCD_withtopbtag_ZprimeM_systdown:= 1-0.35*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCD_inclusive_TprimeM_systup:= 1+0.06*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCD_inclusive_TprimeM_systdown:= 1-0.06*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")", 
                    #"ABCD_notopbtag_TprimeM_systup:= 1+0.08*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD_notopbtag_TprimeM_systdown:= 1-0.08*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD_withtopbtag_TprimeM_systup:= 1+0.6*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCD_withtopbtag_TprimeM_systdown:= 1-0.6*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",

                    #"ABCDcorrE_inclusive_ZprimeM_systup:= 1+0.005*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCDcorrE_inclusive_ZprimeM_systdown:= 1-0.005*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCDcorrE_notopbtag_ZprimeM_systup:= 1+0.005*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCDcorrE_notopbtag_ZprimeM_systdown:= 1-0.005*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCDcorrE_withtopbtag_ZprimeM_systup:= 1+0.6*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCDcorrE_withtopbtag_ZprimeM_systdown:= 1-0.6*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCDcorrE_inclusive_TprimeM_systup:= 1+0.005*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCDcorrE_inclusive_TprimeM_systdown:= 1-0.005*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCDcorrE_notopbtag_TprimeM_systup:=1+0.02*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCDcorrE_notopbtag_TprimeM_systdown:=1-0.02*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCDcorrE_withtopbtag_TprimeM_systup:=1+0.8*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCDcorrE_withtopbtag_TprimeM_systdown:=1-0.8*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",  

                    #"ABCD2_inclusive_ZprimeM_systup:=1+0.06*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCD2_inclusive_ZprimeM_systdown:=1-0.06*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",  
                    #"ABCD2_notopbtag_ZprimeM_systup:=1+0.10*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD2_notopbtag_ZprimeM_systdown:=1-0.10*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD2_withtopbtag_ZprimeM_systup:=1+0.02*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCD2_withtopbtag_ZprimeM_systdown:=1-0.02*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCD2_inclusive_TprimeM_systup:=1+0.06*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCD2_inclusive_TprimeM_systdown:=1-0.06*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")", 
                    #"ABCD2_notopbtag_TprimeM_systup:=1+0.12*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD2_notopbtag_TprimeM_systdown:=1-0.12*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD2_withtopbtag_TprimeM_systup:=1+0.01*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCD2_withtopbtag_TprimeM_systdown:=1-0.01*("+plotselection_tau32_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",

                    #"ABCD2corrE_inclusive_ZprimeM_systup:=1+0.08*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCD2corrE_inclusive_ZprimeM_systdown:=1-0.08*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCD2corrE_notopbtag_ZprimeM_systup:=1+0.05*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD2corrE_notopbtag_ZprimeM_systdown:=1-0.05*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD2corrE_withtopbtag_ZprimeM_systup:=1+0.05*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCD2corrE_withtopbtag_ZprimeM_systdown:=1-0.05*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCD2corrE_inclusive_TprimeM_systup:=1+0.08*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCD2corrE_inclusive_TprimeM_systdown:=1-0.08*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+")",
                    #"ABCD2corrE_notopbtag_TprimeM_systup:=1+0.05*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD2corrE_notopbtag_TprimeM_systdown:=1-0.05*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2_anti+")",
                    #"ABCD2corrE_withtopbtag_TprimeM_systup:=1+0.02*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",
                    #"ABCD2corrE_withtopbtag_TprimeM_systdown:=1-0.02*("+plotselection_t_MSD_anti+"&&"+plotselection_B_CSV+"&&"+plotselection_W_tau21+"&&"+plotselection_topsubjetCSVv2+")",  
    ]

if topWP=='medium' and WWP=='medium' and bottomWP=='medium':
    systweightsABCD=[
                    #"nom:=1",
                    
                    
########medium working points                    
                    
                    "ABCD_nominal:= 1",
                    "ABCD_inclusive_ZprimeM_systup:= pow(1+0.106943,1.0/1.0)",
                    "ABCD_inclusive_ZprimeM_systdown:= pow(1-0.106943,1.0/1.0)",
                    "ABCD_notopbtag_ZprimeM_systup:= pow(1+0.136033,1.0/1.0)",
                    "ABCD_notopbtag_ZprimeM_systdown:= pow(1-0.136033,1.0/1.0)",
                    "ABCD_withtopbtag_ZprimeM_systup:= pow(1+0.692666,1.0/1.0)",
                    "ABCD_withtopbtag_ZprimeM_systdown:= pow(1-0.692666,1.0/1.0)",
                    "ABCD_inclusive_TprimeM_systup:= pow(1+0.146241,1.0/1.0)",
                    "ABCD_inclusive_TprimeM_systdown:= pow(1-0.146241,1.0/1.0)",
                    "ABCD_notopbtag_TprimeM_systup:= pow(1+0.0987,1.0/1.0)",
                    "ABCD_notopbtag_TprimeM_systdown:= pow(1-0.0987,1.0/1.0)",
                    "ABCD_withtopbtag_TprimeM_systup:= pow(1+0.602912,1.0/1.0)",
                    "ABCD_withtopbtag_TprimeM_systdown:= pow(1-0.602912,1.0/1.0)",

                    #"ABCDcorrE_inclusive_ZprimeM_systup:= pow(1+0.06,1.0/1.0)",
                    #"ABCDcorrE_inclusive_ZprimeM_systdown:= pow(1-0.06,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_ZprimeM_systup:= pow(1+0.06,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_ZprimeM_systdown:= pow(1-0.06,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_ZprimeM_systup:= pow(1+0.5,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_ZprimeM_systdown:= pow(1-0.5,1.0/1.0)",
                    #"ABCDcorrE_inclusive_TprimeM_systup:= pow(1+0.07,1.0/1.0)",
                    #"ABCDcorrE_inclusive_TprimeM_systdown:= pow(1-0.07,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_TprimeM_systup:= pow(1+0.06,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_TprimeM_systdown:= pow(1-0.06,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_TprimeM_systup:= pow(1+0.67,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_TprimeM_systdown:= pow(1-0.67,1.0/1.0)",
                    
                    "ABCD2_inclusive_ZprimeM_systup:= pow(1+0.021092,1.0/1.0)",
                    "ABCD2_inclusive_ZprimeM_systdown:= pow(1-0.021092,1.0/1.0)",
                    "ABCD2_notopbtag_ZprimeM_systup:= pow(1+0.030895,1.0/1.0)",
                    "ABCD2_notopbtag_ZprimeM_systdown:= pow(1-0.030895,1.0/1.0)",
                    "ABCD2_withtopbtag_ZprimeM_systup:= pow(1+0.095578,1.0/1.0)",
                    "ABCD2_withtopbtag_ZprimeM_systdown:= pow(1-0.095578,1.0/1.0)",
                    "ABCD2_inclusive_TprimeM_systup:= pow(1+0.01965,1.0/1.0)",
                    "ABCD2_inclusive_TprimeM_systdown:= pow(1-0.01965,1.0/1.0)",
                    "ABCD2_notopbtag_TprimeM_systup:= pow(1+0.019774,1.0/1.0)",
                    "ABCD2_notopbtag_TprimeM_systdown:= pow(1-0.019774,1.0/1.0)",
                    "ABCD2_withtopbtag_TprimeM_systup:= pow(1+0.132762,1.0/1.0)",
                    "ABCD2_withtopbtag_TprimeM_systdown:= pow(1-0.132762,1.0/1.0)",
                                        
                    #"ABCD2corrE_inclusive_ZprimeM_systup:= pow(1+0.05,1.0/1.0)",
                    #"ABCD2corrE_inclusive_ZprimeM_systdown:= pow(1-0.05,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_ZprimeM_systup:= pow(1+0.05,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_ZprimeM_systdown:= pow(1-0.05,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_ZprimeM_systup:= pow(1+0.03,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_ZprimeM_systdown:= pow(1-0.03,1.0/1.0)",
                    #"ABCD2corrE_inclusive_TprimeM_systup:= pow(1+0.03,1.0/1.0)",
                    #"ABCD2corrE_inclusive_TprimeM_systdown:= pow(1-0.03,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_TprimeM_systup:= pow(1+0.05,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_TprimeM_systdown:= pow(1-0.05,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_TprimeM_systup:= pow(1+0.05,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_TprimeM_systdown:= pow(1-0.05,1.0/1.0)",
                    

    ]


if topWP=='medium' and WWP=='loose' and bottomWP=='medium':
    systweightsABCD=[
                    #"nom:=1",
                    
                    
########medium working points                    
                    
                    "ABCD_nominal:= 1",
                    "ABCD_inclusive_ZprimeM_systup:= pow(1+0.106943,1.0/1.0)",
                    "ABCD_inclusive_ZprimeM_systdown:= pow(1-0.106943,1.0/1.0)",
                    "ABCD_notopbtag_ZprimeM_systup:= pow(1+0.136033,1.0/1.0)",
                    "ABCD_notopbtag_ZprimeM_systdown:= pow(1-0.136033,1.0/1.0)",
                    "ABCD_withtopbtag_ZprimeM_systup:= pow(1+0.692666,1.0/1.0)",
                    "ABCD_withtopbtag_ZprimeM_systdown:= pow(1-0.692666,1.0/1.0)",
                    "ABCD_inclusive_TprimeM_systup:= pow(1+0.146241,1.0/1.0)",
                    "ABCD_inclusive_TprimeM_systdown:= pow(1-0.146241,1.0/1.0)",
                    "ABCD_notopbtag_TprimeM_systup:= pow(1+0.0987,1.0/1.0)",
                    "ABCD_notopbtag_TprimeM_systdown:= pow(1-0.0987,1.0/1.0)",
                    "ABCD_withtopbtag_TprimeM_systup:= pow(1+0.602912,1.0/1.0)",
                    "ABCD_withtopbtag_TprimeM_systdown:= pow(1-0.602912,1.0/1.0)",

                    #"ABCDcorrE_inclusive_ZprimeM_systup:= pow(1+0.06,1.0/1.0)",
                    #"ABCDcorrE_inclusive_ZprimeM_systdown:= pow(1-0.06,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_ZprimeM_systup:= pow(1+0.06,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_ZprimeM_systdown:= pow(1-0.06,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_ZprimeM_systup:= pow(1+0.5,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_ZprimeM_systdown:= pow(1-0.5,1.0/1.0)",
                    #"ABCDcorrE_inclusive_TprimeM_systup:= pow(1+0.07,1.0/1.0)",
                    #"ABCDcorrE_inclusive_TprimeM_systdown:= pow(1-0.07,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_TprimeM_systup:= pow(1+0.06,1.0/1.0)",
                    #"ABCDcorrE_notopbtag_TprimeM_systdown:= pow(1-0.06,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_TprimeM_systup:= pow(1+0.67,1.0/1.0)",
                    #"ABCDcorrE_withtopbtag_TprimeM_systdown:= pow(1-0.67,1.0/1.0)",
                    
                    "ABCD2_inclusive_ZprimeM_systup:= pow(1+0.05428,1.0/1.0)",
                    "ABCD2_inclusive_ZprimeM_systdown:= pow(1-0.05428,1.0/1.0)",
                    "ABCD2_notopbtag_ZprimeM_systup:= pow(1+0.056178,1.0/1.0)",
                    "ABCD2_notopbtag_ZprimeM_systdown:= pow(1-0.056178,1.0/1.0)",
                    "ABCD2_withtopbtag_ZprimeM_systup:= pow(1+0.185563,1.0/1.0)",
                    "ABCD2_withtopbtag_ZprimeM_systdown:= pow(1-0.185563,1.0/1.0)",
                    "ABCD2_inclusive_TprimeM_systup:= pow(1+0.042944,1.0/1.0)",
                    "ABCD2_inclusive_TprimeM_systdown:= pow(1-0.042944,1.0/1.0)",
                    "ABCD2_notopbtag_TprimeM_systup:= pow(1+0.046409,1.0/1.0)",
                    "ABCD2_notopbtag_TprimeM_systdown:= pow(1-0.046409,1.0/1.0)",
                    "ABCD2_withtopbtag_TprimeM_systup:= pow(1+0.183169,1.0/1.0)",
                    "ABCD2_withtopbtag_TprimeM_systdown:= pow(1-0.183169,1.0/1.0)",
                                        
                    #"ABCD2corrE_inclusive_ZprimeM_systup:= pow(1+0.05,1.0/1.0)",
                    #"ABCD2corrE_inclusive_ZprimeM_systdown:= pow(1-0.05,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_ZprimeM_systup:= pow(1+0.05,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_ZprimeM_systdown:= pow(1-0.05,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_ZprimeM_systup:= pow(1+0.03,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_ZprimeM_systdown:= pow(1-0.03,1.0/1.0)",
                    #"ABCD2corrE_inclusive_TprimeM_systup:= pow(1+0.03,1.0/1.0)",
                    #"ABCD2corrE_inclusive_TprimeM_systdown:= pow(1-0.03,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_TprimeM_systup:= pow(1+0.05,1.0/1.0)",
                    #"ABCD2corrE_notopbtag_TprimeM_systdown:= pow(1-0.05,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_TprimeM_systup:= pow(1+0.05,1.0/1.0)",
                    #"ABCD2corrE_withtopbtag_TprimeM_systdown:= pow(1-0.05,1.0/1.0)",
                    

    ]

weigthsystnamesMCSFs=[
                    #"_CSV_MCSF_nominal",
                    #"_CSV_MCSF_systup",
                    #"_CSV_MCSF_systdown",
                    #"_CSV_MCSF_nominal",
                    "_MCSF_nominal",
                    
                    "_MCSF_CSVLFUp",
                    "_MCSF_CSVLFDown",
                    "_MCSF_CSVHFUp",
                    "_MCSF_CSVHFDown",
                    "_MCSF_CSVHFStats1Up",
                    "_MCSF_CSVHFStats1Down",
                    "_MCSF_CSVLFStats1Up",
                    "_MCSF_CSVLFStats1Down",
                    "_MCSF_CSVHFStats2Up",
                    "_MCSF_CSVHFStats2Down",
                    "_MCSF_CSVLFStats2Up",
                    "_MCSF_CSVLFStats2Down",
                    "_MCSF_CSVCErr1Up",
                    "_MCSF_CSVCErr1Down",
                    "_MCSF_CSVCErr2Up",
                    "_MCSF_CSVCErr2Down",

                    "_MCSF_PUUp",
                    "_MCSF_PUDown",

                    "_MCSF_JESup",
                    "_MCSF_JESdown",
                    "_MCSF_JERup",
                    "_MCSF_JERdown",
                   
                    
                    "_t21_MCSF_nominal",
                    "_t21_MCSF_systup",
                    "_t21_MCSF_systdown", 
                    "_t32_MCSF_notopbtag_nominal",
                    "_t32_MCSF_notopbtag_systup",
                    "_t32_MCSF_notopbtag_systdown", 
                    "_t32_MCSF_withtopbtag_nominal",
                    "_t32_MCSF_withtopbtag_systup",
                    "_t32_MCSF_withtopbtag_systdown", 
                    
]

systweightnamesMCSFs=[
                    #"CSV_MCSF_nominal:=(1)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systup:=(1*(1+1.15))*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systdown:=(1*(1-1.15))*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0", 
                    
                    "MCSF_nominal:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    
                    "MCSF_CSVLFUp:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVLFDown:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVHFUp:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVHFDown:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVHFStats1Up:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVHFStats1Down:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVLFStats1Up:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVLFStats1Down:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVHFStats2Up:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVHFStats2Down:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVLFStats2Up:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVLFStats2Down:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVCErr1Up:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVCErr1Down:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVCErr2Up:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_CSVCErr2Down:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",

                    "MCSF_PUUp:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_PUDown:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",

                    "MCSF_JESup:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_JESdown:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_JERup:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "MCSF_JERdown:=(1.0)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",                    
                    
                    
                    "t21_MCSF_nominal:=(1.10)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "t21_MCSF_systup:=(1.10*(1+0.12))*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "t21_MCSF_systdown:=(1.10*(1-0.12))*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "t32_MCSF_notopbtag_nominal:=(1.06)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "t32_MCSF_notopbtag_systup:=(1.06*(1+0.08))*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "t32_MCSF_notopbtag_systdown:=(1.06*(1-0.04))*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "t32_MCSF_withtopbtag_nominal:=(1.05)*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "t32_MCSF_withtopbtag_systup:=(1.05*(1+0.11))*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    "t32_MCSF_withtopbtag_systdown:=(1.05*(1-0.05))*(DoMCDataWeights==1)+(DoMCDataWeights==0)*1.0",
                    
]


#allweightsystnames=weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM+weightsystnamesPythia8bantiZprimeM+weightsystnamesMadgraphtantiTopPt+weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffMadgraphbantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM+weightsystnamesGeneratorDiffMadgraphtantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt+weightsystnamesMadgraphbantiZprimeMWithtopbtag+weightsystnamesPythia8bantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag+weightsystnamesMadgraphtantiTopPtWithtopbtag+weightsystnamesPythia8tantiTopPtWithtopbtag+weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag+weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag+weightsystnamesABCD+weigthsystnamesMCSFs
##allweightsystnames=weightsystnamesABCD

#allsystweights=systweightsbasic+systweightsMadgraphbantiZprimeM+systweightsPythia8bantiZprimeM+systweightsMadgraphtantiTopPt+systweightsPythia8tantiTopPt+systweightsGeneartorDiffMadgraphbantiZprimeM+systweightsGeneartorDiffPythia8bantiZprimeM+systweightsGeneartorDiffMadgraphtantiTopPt+systweightsGeneartorDiffPythia8tantiTopPt+systweightsMadgraphbantiZprimeMWithtopbtag+systweightsPythia8bantiZprimeMWithtopbtag+systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag+systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag+systweightsMadgraphtantiTopPtWithtopbtag+systweightsPythia8tantiTopPtWithtopbtag+systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag+systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag+systweightsABCD+systweightnamesMCSFs
##allsystweights=systweightsABCD

#ABweightsystnames=weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM+weightsystnamesPythia8bantiZprimeM+weightsystnamesMadgraphtantiTopPt+weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffMadgraphbantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM+weightsystnamesGeneratorDiffMadgraphtantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt+weightsystnamesMadgraphbantiZprimeMWithtopbtag+weightsystnamesPythia8bantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag+weightsystnamesMadgraphtantiTopPtWithtopbtag+weightsystnamesPythia8tantiTopPtWithtopbtag+weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag+weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag+weigthsystnamesMCSFs

#ABsystweights=systweightsbasic+systweightsMadgraphbantiZprimeM+systweightsPythia8bantiZprimeM+systweightsMadgraphtantiTopPt+systweightsPythia8tantiTopPt+systweightsGeneartorDiffMadgraphbantiZprimeM+systweightsGeneartorDiffPythia8bantiZprimeM+systweightsGeneartorDiffMadgraphtantiTopPt+systweightsGeneartorDiffPythia8tantiTopPt+systweightsMadgraphbantiZprimeMWithtopbtag+systweightsPythia8bantiZprimeMWithtopbtag+systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag+systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag+systweightsMadgraphtantiTopPtWithtopbtag+systweightsPythia8tantiTopPtWithtopbtag+systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag+systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag+systweightnamesMCSFs
     
allweightsystnames=weigthsystnamesbasic+weightsystnamesABCD

allsystweights=systweightsbasic+systweightsABCD

# names of the systematics (proper names needed e.g. for combination)
mcweight='37.8'

sfs="Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"
usualweights="(1*Weight_PU*((Weight>0)-(Weight<0)))*Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"


# samples
# input path 
path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"
#path_80x="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_old/"

# MC samples (name, color, path to files,weight,nickname_without_special_characters,systematics)                       
#samples=[ 
                    ##Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path_80x+'ZPrime/Zprime_1500_700_nominal_Tree.root',mcweight,'Zprime1500700') ,
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight,'Zprime1500900') ,
                    ##Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta-9,path_80x+'ZPrime/Zprime_1500_1200_nominal_Tree.root',mcweight,'Zprime15001200') ,

                    ##Sample('Z->tWb, MZp2000Nar_MTp900Nar_LH',ROOT.kCyan,path_80x+'ZPrime/Zprime_2000_900_nominal_Tree.root',mcweight,'Zprime2000900') ,
                    #Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight,'Zprime20001200') ,
                    ##Sample('Z->tWb, MZp2000Nar_MTp1200Nar_RH',ROOT.kCyan,path_80x+'ZPrime/Zprime_2000_1200_RH_nominal_Tree.root',mcweight,'Zprime20001200RH') ,
                    ##Sample('Z->tWb, MZp2000Wid_MTp1200Nar_LH',ROOT.kCyan+1,path_80x+'ZPrime/Zprime_2000Wid_1200_nominal_Tree.root',mcweight,'Zprime2000W1200') ,
                    ##Sample('Z->tWb, MZp2000nar_MTp1200Wid_LH',ROOT.kCyan+1,path_80x+'ZPrime/Zprime_2000_1200Wid_nominal_Tree.root',mcweight,'Zprime20001200W') ,
                    ##Sample('Z->tWb, MZp2000Nar_MTp1500Nar_LH',ROOT.kCyan+3,path_80x+'ZPrime/Zprime_2000_1500_nominal_Tree.root',mcweight,'Zprime200015000') , 
                    
                    #Sample('Z->tWb, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/37.8','Zprime25001200') ,     
                    ##Sample('Z->tWb, MZp2500Nar_MTp1500Nar_LH',ROOT.kRed+2,path_80x+'ZPrime/Zprime_2500_1500_nominal_Tree.root',mcweight,'Zprime25001500') ,     
                    

                    ##Sample('QCD_comb',ROOT.kYellow,path_80x+'QCD/MC_QCD_*nominal*Tree*.root',mcweight,'QCD_comb') ,     
                    #Sample('QCD_HT',ROOT.kYellow,path_80x+'BKG_QCD/MC_QCD_H*nominal*Tree*.root',mcweight,'QCD_HT') ,     
                    #Sample('QCD_Pt',ROOT.kGreen,path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root',mcweight,'QCD_PT') ,     

                    ##Sample('t#bar{t} + jets',ROOT.kBlue,path_80x+'BKG_TTbar/MC_TTbar_nominal_Tree_1.root',mcweight,'ttbar') ,     
                    #Sample('t#bar{t} + jets',ROOT.kBlue,path_80x+'BKG_TTbar/*nominal*.root',mcweight,'ttbar') ,     
                    ##Sample('Single Top',ROOT.kMagenta,path_80x+'/st*/*nominal*.root',mcweightAll,'SingleTop',systs_all_samples) , 
                    ##Sample('V+jets',ROOT.kGreen-3,path_80x+'/??ets*/*nominal*.root',mcweightAll,'Vjets',systs_all_samples) , 
                    ##Sample('t#bar{t}+V',ROOT.kBlue-10,path_80x+'/tt?_*/*nominal*.root',mcweightAll,'ttV',systs_all_samples),         
                    ##Sample('Diboson',ROOT.kAzure+2,path_80x+'/??/*nominal*.root',mcweightAll,'Diboson',systs_all_samples) , 
                    ##Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcweight,'QCD') , 
                    #Sample('MC_BKG_DATA',ROOT.kAzure,path_80x+'BKG*/*nominal*.root',mcweight,'MC_BKG_DATA') ,     
                    ##Sample('C_BKG_DATA',ROOT.kAzure,path_80x+'QCD*/*nominal*.root',mcweight,'MC_BKG_DATA') ,     

#]



SignalSamples=[
                    Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight+'/138.07*0.3','Zprime1500900',allweightsystnames),
                    Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight+'/86.28*0.3','Zprime20001200',allweightsystnames),
                    Sample('Z->tWb, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/37.6*0.3','Zprime25001200',allweightsystnames) ,     
]

BackgroundSamples=[
                    Sample('QCDMadgraph',ROOT.kOrange-3,path_80x+'BKG_QCD/MC_QCD_H*nominal*.root',mcweight,'QCDMadgraph',allweightsystnames),
                    Sample('t#bar{t} + jets',ROOT.kBlue,path_80x+'BKG_TTbar/*nominal*.root',mcweight,'ttbar',allweightsystnames) , 
                    Sample('Signal Contamination (1pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/37.6*0.3','SC_Zprime25001200_0.3pb',allweightsystnames) ,  
                    Sample('Signal Contamination none',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/100000','SC_none',allweightsystnames) ,  
                    Sample('QCDPythia8',ROOT.kGreen+2,path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root',mcweight,'QCDPythia8',allweightsystnames),

]


DataSamples=[
                    Sample('Data = Background with (1pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/37.6*0.3','BKG_Zprime25001200_0.3pb',allweightsystnames),     
                    Sample('Data = Background with signal',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/100000.0','DATA_BKG',allweightsystnames) ,     
                    #Sample('Data = Background with (1pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kBlack,path_80x+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight+'/86.28*0.3','BKG_Zprime20001200_1pb') ,     
                    #Sample('Data = Background with (1pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kBlack,path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight+'/138.07*0.3','BKG_Zprime1500900_1pb') ,     

]


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
    
 
