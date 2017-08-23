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
                    "ABMadgraphtantiTopPtGeneratorDiff_systDown:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt - abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
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

if topWP=='loose' and WWP=='loose' and bottomWP=='medium':

  if ABCDversion is 'ABCD1':
    weightsystnamesABCD=[
                    #"",
                    #"_ABCD1_nominal",
                    
                    "_ABCD1_inclusive_ZprimeM_systUp",
                    "_ABCD1_inclusive_ZprimeM_systDown",
                    "_ABCD1_notopbtag_ZprimeM_systUp",
                    "_ABCD1_notopbtag_ZprimeM_systDown",
                    "_ABCD1_withtopbtag_ZprimeM_systUp",
                    "_ABCD1_withtopbtag_ZprimeM_systDown",
                    "_ABCD1_inclusive_TprimeM_systUp",
                    "_ABCD1_inclusive_TprimeM_systDown",
                    "_ABCD1_notopbtag_TprimeM_systUp",
                    "_ABCD1_notopbtag_TprimeM_systDown",
                    "_ABCD1_withtopbtag_TprimeM_systUp",
                    "_ABCD1_withtopbtag_TprimeM_systDown",
    ]                    
  elif ABCDversion is 'ABCD2':            
    weightsystnamesABCD=[
                    "_ABCD2_inclusive_ZprimeM_systUp",
                    "_ABCD2_inclusive_ZprimeM_systDown",
                    "_ABCD2_notopbtag_ZprimeM_systUp",
                    "_ABCD2_notopbtag_ZprimeM_systDown",
                    "_ABCD2_withtopbtag_ZprimeM_systUp",
                    "_ABCD2_withtopbtag_ZprimeM_systDown",
                    "_ABCD2_inclusive_TprimeM_systUp",
                    "_ABCD2_inclusive_TprimeM_systDown",
                    "_ABCD2_notopbtag_TprimeM_systUp",
                    "_ABCD2_notopbtag_TprimeM_systDown",
                    "_ABCD2_withtopbtag_TprimeM_systUp",
                    "_ABCD2_withtopbtag_TprimeM_systDown",
    ]     
  elif ABCDversion is 'ABCD3':            
    weightsystnamesABCD=[
                    "_ABCD3_inclusive_ZprimeM_systUp",
                    "_ABCD3_inclusive_ZprimeM_systDown",
                    "_ABCD3_notopbtag_ZprimeM_systUp",
                    "_ABCD3_notopbtag_ZprimeM_systDown",
                    "_ABCD3_withtopbtag_ZprimeM_systUp",
                    "_ABCD3_withtopbtag_ZprimeM_systDown",
                    "_ABCD3_inclusive_TprimeM_systUp",
                    "_ABCD3_inclusive_TprimeM_systDown",
                    "_ABCD3_notopbtag_TprimeM_systUp",
                    "_ABCD3_notopbtag_TprimeM_systDown",
                    "_ABCD3_withtopbtag_TprimeM_systUp",
                    "_ABCD3_withtopbtag_TprimeM_systDown",  
    ]
  elif ABCDversion is 'ABCD5':            
    weightsystnamesABCD=[
                    "_ABCD5_inclusive_ZprimeM_systUp",
                    "_ABCD5_inclusive_ZprimeM_systDown",
                    "_ABCD5_notopbtag_ZprimeM_systUp",
                    "_ABCD5_notopbtag_ZprimeM_systDown",
                    "_ABCD5_withtopbtag_ZprimeM_systUp",
                    "_ABCD5_withtopbtag_ZprimeM_systDown",
                    "_ABCD5_inclusive_TprimeM_systUp",
                    "_ABCD5_inclusive_TprimeM_systDown",
                    "_ABCD5_notopbtag_TprimeM_systUp",
                    "_ABCD5_notopbtag_TprimeM_systDown",
                    "_ABCD5_withtopbtag_TprimeM_systUp",
                    "_ABCD5_withtopbtag_TprimeM_systDown", 

    ]
    

    
    
    
if topWP=='loose' and WWP=='loose' and bottomWP=='medium':
    
                    #"nom:=1",
                    
    if ABCDversion is 'ABCD1': 
        systweightsABCD=[
                    "ABCD1_inclusive_ZprimeM_systUp:= (pow(1+0.024348,1.0/1.0))*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_inclusive_ZprimeM_systDown:= pow(1-0.024348,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_notopbtag_ZprimeM_systUp:= pow(1+0.018073,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_notopbtag_ZprimeM_systDown:= pow(1-0.018073,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_withtopbtag_ZprimeM_systUp:= pow(1+0.144325,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_withtopbtag_ZprimeM_systDown:= pow(1-0.144325,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_inclusive_TprimeM_systUp:= pow(1+0.027596,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_inclusive_TprimeM_systDown:= pow(1-0.027596,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_notopbtag_TprimeM_systUp:= pow(1+0.021271,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_notopbtag_TprimeM_systDown:= pow(1-0.021271,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_withtopbtag_TprimeM_systUp:= pow(1+0.259112,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD1_withtopbtag_TprimeM_systDown:= pow(1-0.259112,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD1*(DoMCDataWeights==1)*(DoABCDsyst==0)",
        ]
    elif ABCDversion is 'ABCD2': 
        systweightsABCD=[
                    "ABCD2_inclusive_ZprimeM_systUp:= pow(1+0.01874,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_inclusive_ZprimeM_systDown:= pow(1-0.01874,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_notopbtag_ZprimeM_systUp:= pow(1+0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_notopbtag_ZprimeM_systDown:= pow(1-0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_withtopbtag_ZprimeM_systUp:= pow(1+0.063702,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_withtopbtag_ZprimeM_systDown:= pow(1-0.063702,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_inclusive_TprimeM_systUp:= pow(1+0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_inclusive_TprimeM_systDown:= pow(1-0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_notopbtag_TprimeM_systUp:= pow(1+0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_notopbtag_TprimeM_systDown:= pow(1-0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_withtopbtag_TprimeM_systUp:= pow(1+0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD2_withtopbtag_TprimeM_systDown:= pow(1-0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD2*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                     
        ]
    elif ABCDversion is 'ABCD3': 
        systweightsABCD=[
                    "ABCD3_inclusive_ZprimeM_systUp:= pow(1+0.019232,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_inclusive_ZprimeM_systDown:= pow(1-0.019232,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_notopbtag_ZprimeM_systUp:= pow(1+0.01551,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_notopbtag_ZprimeM_systDown:= pow(1-0.01551,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_withtopbtag_ZprimeM_systUp:= pow(1+0.066,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_withtopbtag_ZprimeM_systDown:= pow(1-0.066,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_inclusive_TprimeM_systUp:= pow(1+0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_inclusive_TprimeM_systDown:= pow(1-0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_notopbtag_TprimeM_systUp:= pow(1+0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_notopbtag_TprimeM_systDown:= pow(1-0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_withtopbtag_TprimeM_systUp:= pow(1+0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_withtopbtag_TprimeM_systDown:= pow(1-0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",          
          
        ]
    elif ABCDversion is 'ABCD5': 
        systweightsABCD=[ 
                    "ABCD5_inclusive_ZprimeM_systUp:= pow(1+0.03681,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_inclusive_ZprimeM_systDown:= pow(1-0.03681,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_notopbtag_ZprimeM_systUp:= pow(1+0.03509,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_notopbtag_ZprimeM_systDown:= pow(1-0.03509,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_withtopbtag_ZprimeM_systUp:= pow(1+0.021591,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_withtopbtag_ZprimeM_systDown:= pow(1-0.021591,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_inclusive_TprimeM_systUp:= pow(1+0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_inclusive_TprimeM_systDown:= pow(1-0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_notopbtag_TprimeM_systUp:= pow(1+0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_notopbtag_TprimeM_systDown:= pow(1-0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_withtopbtag_TprimeM_systUp:= pow(1+0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_withtopbtag_TprimeM_systDown:= pow(1-0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",        ]



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
                    "_" + ABCDversion + "_MCSF_WtagUp",
                    "_" + ABCDversion + "_MCSF_WtagDown",
                    "_" + ABCDversion + "_MCSF_PUUp",
                    "_" + ABCDversion + "_MCSF_PUDown",
                    "_" + ABCDversion + "_MCSF_PDFUp",
                    "_" + ABCDversion + "_MCSF_PDFDown",  
                    "_" + ABCDversion + "_MCSF_LumiUp",
                    "_" + ABCDversion + "_MCSF_LumiDown",
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
          
    #weigthsystnamesMCSFs=[
                    #"_ABCD2_nominal",
                    
                    #"_ABCD2_MCSF_CSVLFUp",
                    #"_ABCD2_MCSF_CSVLFDown",
                    #"_ABCD2_MCSF_CSVHFUp",
                    #"_ABCD2_MCSF_CSVHFDown",
                    #"_ABCD2_MCSF_CSVHFStats1Up",
                    #"_ABCD2_MCSF_CSVHFStats1Down",
                    #"_ABCD2_MCSF_CSVLFStats1Up",
                    #"_ABCD2_MCSF_CSVLFStats1Down",
                    #"_ABCD2_MCSF_CSVHFStats2Up",
                    #"_ABCD2_MCSF_CSVHFStats2Down",
                    #"_ABCD2_MCSF_CSVLFStats2Up",
                    #"_ABCD2_MCSF_CSVLFStats2Down",
                    #"_ABCD2_MCSF_CSVCErr1Up",
                    #"_ABCD2_MCSF_CSVCErr1Down",
                    #"_ABCD2_MCSF_CSVCErr2Up",
                    #"_ABCD2_MCSF_CSVCErr2Down",
                    #"_ABCD2_MCSF_toptagUp",
                    #"_ABCD2_MCSF_toptagDown",
                    #"_ABCD2_MCSF_WtagUp",
                    #"_ABCD2_MCSF_WtagDown",
                    #"_ABCD2_MCSF_PUUp",
                    #"_ABCD2_MCSF_PUDown",
                    #"_ABCD2_MCSF_PDFUp",
                    #"_ABCD2_MCSF_PDFDown",  
                    #"_ABCD2_MCSF_LumiUp",
                    #"_ABCD2_MCSF_LumiDown",
                    #"_ABCD2_MCSF_renfac_envUp",
                    #"_ABCD2_MCSF_renfac_envDown",
                    #"_ABCD2_ttbarXSUp",
                    #"_ABCD2_ttbarXSDown",
                    
                    #"_ABCD2_MCSF_renfacUp",
                    #"_ABCD2_MCSF_renfacDown",
                    #"_ABCD2_MCSF_renUp",
                    #"_ABCD2_MCSF_renDown",
                    #"_ABCD2_MCSF_facUp",
                    #"_ABCD2_MCSF_facDown",
                    
                    
    #]
    
    

    systweightnamesMCSFs=[
                    #"CSV_nominal:=(1)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systUp:=(1*(1+1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    #"CSV_MCSF_systDown:=(1*(1-1.15))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
                    "nom:=1.0",
                    
                    "" + ABCDversion + "_nominal:=(MCSF_Weight_" + ABCDversion + ")*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    
                    "" + ABCDversion + "_MCSF_CSVLFUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats1Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFStats1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats1Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFStats1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats1Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFStats1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats1Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFStats1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats2Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFStats2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVHFStats2Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFStats2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats2Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFStats2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVLFStats2Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFStats2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr1Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVCErr1Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr1Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVCErr1Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr2Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVCErr2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_CSVCErr2Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVCErr2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_toptagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_toptagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_WtagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtagweightnominal*" + ABCDversion + "_WtagweightUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_WtagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtagweightnominal*" + ABCDversion + "_WtagweightDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",      
                    
                    "" + ABCDversion + "_MCSF_PUUp:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Up)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_PUDown:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Down)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    "" + ABCDversion + "_MCSF_PDFUp:=(MCSF_Weight_" + ABCDversion + "/PDF_RMSMean*PDF_RMSUp)*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0",
                    "" + ABCDversion + "_MCSF_PDFDown:=(MCSF_Weight_" + ABCDversion + "/PDF_RMSMean*PDF_RMSDown)*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0",
                    "" + ABCDversion + "_MCSF_LumiUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.025))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_LumiDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.025))*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 

                    "" + ABCDversion + "_MCSF_renfac_envUp:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeUp)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_renfac_envDown:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeDown)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_ttbarXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0",
                    "" + ABCDversion + "_ttbarXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*1.0",
                 
                 
                    "" + ABCDversion + "_MCSF_renfacUp:=(Weight_scale_variation_muR2p0_muF2p0)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_renfacDown:=(Weight_scale_variation_muR0p5_muF0p5)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_renUp:=(Weight_scale_variation_muR2p0_muF1p0)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_renDown:=(Weight_scale_variation_muR0p5_muF1p0)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_facUp:=(Weight_scale_variation_muR1p0_muF2p0)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0",
                    "" + ABCDversion + "_MCSF_facDown:=(Weight_scale_variation_muR1p0_muF0p5)*(DoWeights*DoMCDataWeights==1)+(DoWeights*DoMCDataWeights==0)*1.0", 
                    
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

assert len(otherSystNames)==len(otherSystFileNames)

#allweightsystnames=weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM+weightsystnamesPythia8bantiZprimeM+weightsystnamesMadgraphtantiTopPt+weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffMadgraphbantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM+weightsystnamesGeneratorDiffMadgraphtantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt+weightsystnamesMadgraphbantiZprimeMWithtopbtag+weightsystnamesPythia8bantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag+weightsystnamesMadgraphtantiTopPtWithtopbtag+weightsystnamesPythia8tantiTopPtWithtopbtag+weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag+weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag+weightsystnamesABCD+weigthsystnamesMCSFs
##allweightsystnames=weightsystnamesABCD

#allsystweights=systweightsbasic+systweightsMadgraphbantiZprimeM+systweightsPythia8bantiZprimeM+systweightsMadgraphtantiTopPt+systweightsPythia8tantiTopPt+systweightsGeneartorDiffMadgraphbantiZprimeM+systweightsGeneartorDiffPythia8bantiZprimeM+systweightsGeneartorDiffMadgraphtantiTopPt+systweightsGeneartorDiffPythia8tantiTopPt+systweightsMadgraphbantiZprimeMWithtopbtag+systweightsPythia8bantiZprimeMWithtopbtag+systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag+systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag+systweightsMadgraphtantiTopPtWithtopbtag+systweightsPythia8tantiTopPtWithtopbtag+systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag+systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag+systweightsABCD+systweightnamesMCSFs
##allsystweights=systweightsABCD

#ABweightsystnames=weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM+weightsystnamesPythia8bantiZprimeM+weightsystnamesMadgraphtantiTopPt+weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffMadgraphbantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM+weightsystnamesGeneratorDiffMadgraphtantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt+weightsystnamesMadgraphbantiZprimeMWithtopbtag+weightsystnamesPythia8bantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag+weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag+weightsystnamesMadgraphtantiTopPtWithtopbtag+weightsystnamesPythia8tantiTopPtWithtopbtag+weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag+weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag+weigthsystnamesMCSFs

#ABsystweights=systweightsbasic+systweightsMadgraphbantiZprimeM+systweightsPythia8bantiZprimeM+systweightsMadgraphtantiTopPt+systweightsPythia8tantiTopPt+systweightsGeneartorDiffMadgraphbantiZprimeM+systweightsGeneartorDiffPythia8bantiZprimeM+systweightsGeneartorDiffMadgraphtantiTopPt+systweightsGeneartorDiffPythia8tantiTopPt+systweightsMadgraphbantiZprimeMWithtopbtag+systweightsPythia8bantiZprimeMWithtopbtag+systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag+systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag+systweightsMadgraphtantiTopPtWithtopbtag+systweightsPythia8tantiTopPtWithtopbtag+systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag+systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag+systweightnamesMCSFs
     
allweightsystnames=weigthsystnamesMCSFs+weightsystnamesABCD

allsystweights=systweightnamesMCSFs+systweightsABCD

# names of the systematics (proper names needed e.g. for combination)
mcweight='37.8'

ttbarXS=831.76 
rateunc_ttbarXS_Up=math.sqrt(19.77*19.77 + 35.06*35.06)
rateunc_ttbarXS_Down=math.sqrt(29.20*29.20 + 35.06*35.06)


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
                    ##Sample('V+jets',ROOT.kGreen-3,path_80x+'/??ets*/*nominal*.root',mcweightAll,'Vjets',systs_all_samples) , s
                    ##Sample('t#bar{t}+V',ROOT.kBlue-10,path_80x+'/tt?_*/*nominal*.root',mcweightAll,'ttV',systs_all_samples),         
                    ##Sample('Diboson',ROOT.kAzure+2,path_80x+'/??/*nominal*.root',mcweightAll,'Diboson',systs_all_samples) , 
                    ##Sample('QCD',ROOT.kYellow ,path_80x+'/QCD*/*nominal*root',mcweight,'QCD') , 
                    #Sample('MC_BKG_DATA',ROOT.kAzure,path_80x+'BKG*/*nominal*.root',mcweight,'MC_BKG_DATA') ,     
                    ##Sample('C_BKG_DATA',ROOT.kAzure,path_80x+'QCD*/*nominal*.root',mcweight,'MC_BKG_DATA') ,     

#]



SignalSamples=[
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight+'/138.07*0.3','Zprime1500900',allweightsystnames),
                    Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Zprime_1500_1200_nominal_Tree.root',mcweight+'/99.03*8.6','SigZprime15001200',allweightsystnames),
                    Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path_80x+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight+'/86.28*0.27','SigZprime20001200',allweightsystnames),
                    Sample('Z->tWb, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/37.6*0.33','SigZprime25001200',allweightsystnames), 
                    
                    Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta-7,path_80x+'Signal_Zprime/Zprime_1500_700_nominal_Tree.root',mcweight+'/95.06*0.80','SigZprime1500700',allweightsystnames),
                    Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta,path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight+'/138.07*1.5','SigZprime1500900',allweightsystnames),
                    Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900',ROOT.kCyan+3,path_80x+'Signal_Zprime/Zprime_2000_900_nominal_Tree.root',mcweight+'/55.83*0.21','SigZprime2000900',allweightsystnames),
                    Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kCyan-6,path_80x+'Signal_Zprime/Zprime_2000_1500_nominal_Tree.root',mcweight+'/83.47*0.90','SigZprime20001500',allweightsystnames),
                    Sample('Z->tWb, m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kRed-7,path_80x+'Signal_Zprime/Zprime_2500_1500_nominal_Tree.root',mcweight+'/53.9*0.29','SigZprime25001500',allweightsystnames),

                    Sample('Gstar->tWb, m(Gstar_{Nar})=1500, m(Tp_{Nar})=800',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_1500_800_nominal_Tree.root',mcweight+'/1.447','SigGstar1500800Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=1500, m(Tp_{Nar})=1000',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_1500_1000_nominal_Tree.root',mcweight+'/1.447','SigGstar15001000Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=1500, m(Tp_{Nar})=1300',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_1500_1300_nominal_Tree.root',mcweight+'/1.447','SigGstar15001300Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=2000, m(Tp_{Nar})=1000',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_2000_1000_nominal_Tree.root',mcweight+'/1.447','SigGstar20001000Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=2000, m(Tp_{Nar})=1300',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_2000_1300_nominal_Tree.root',mcweight+'/1.447','SigGstar20001300Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=2000, m(Tp_{Nar})=1500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_2000_1500_nominal_Tree.root',mcweight+'/1.447','SigGstar20001500Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=2500, m(Tp_{Nar})=1300',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_2500_1300_nominal_Tree.root',mcweight+'/1.447','SigGstar25001300Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=2500, m(Tp_{Nar})=1500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_2500_1500_nominal_Tree.root',mcweight+'/1.447','SigGstar25001500Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=2500, m(Tp_{Nar})=1800',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_2500_1800_nominal_Tree.root',mcweight+'/1.447','SigGstar25001800Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=3000, m(Tp_{Nar})=1500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_3000_1500_nominal_Tree.root',mcweight+'/1.447','SigGstar30001500Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=3000, m(Tp_{Nar})=1800',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_3000_1800_nominal_Tree.root',mcweight+'/1.447','SigGstar30001800Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=3000, m(Tp_{Nar})=2100',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_3000_2100_nominal_Tree.root',mcweight+'/1.447','SigGstar30002100Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=3500, m(Tp_{Nar})=1800',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_3500_1800_nominal_Tree.root',mcweight+'/1.447','SigGstar35001800Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=3500, m(Tp_{Nar})=2100',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_3500_2100_nominal_Tree.root',mcweight+'/1.447','SigGstar35002100Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=3500, m(Tp_{Nar})=2500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_3500_2500_nominal_Tree.root',mcweight+'/1.447','SigGstar35002500Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=4000, m(Tp_{Nar})=2100',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_4000_2100_nominal_Tree.root',mcweight+'/1.447','SigGstar40002100Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=4000, m(Tp_{Nar})=2500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_4000_2500_nominal_Tree.root',mcweight+'/1.447','SigGstar40002500Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=4000, m(Tp_{Nar})=3000',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_4000_3000_nominal_Tree.root',mcweight+'/1.447','SigGstar40003000Nar',allweightsystnames),


                    Sample('Gstar->tWb, m(Gstar_{Wid})=1500, m(Tp_{Nar})=800',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_1500_800_nominal_Tree.root',mcweight+'/1.447','SigGstar1500800Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=1500, m(Tp_{Nar})=1000',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_1500_1000_nominal_Tree.root',mcweight+'/1.447','SigGstar15001000Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=1500, m(Tp_{Nar})=1300',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_1500_1300_nominal_Tree.root',mcweight+'/1.447','SigGstar15001300Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=2000, m(Tp_{Nar})=1000',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_2000_1000_nominal_Tree.root',mcweight+'/1.447','SigGstar20001000Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=2000, m(Tp_{Nar})=1300',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_2000_1300_nominal_Tree.root',mcweight+'/1.447','SigGstar20001300Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=2000, m(Tp_{Nar})=1500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_2000_1500_nominal_Tree.root',mcweight+'/1.447','SigGstar20001500Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=2500, m(Tp_{Nar})=1300',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_2500_1300_nominal_Tree.root',mcweight+'/1.447','SigGstar25001300Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=2500, m(Tp_{Nar})=1500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_2500_1500_nominal_Tree.root',mcweight+'/1.447','SigGstar25001500Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=2500, m(Tp_{Nar})=1800',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_2500_1800_nominal_Tree.root',mcweight+'/1.447','SigGstar25001800Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=3000, m(Tp_{Nar})=1500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_3000_1500_nominal_Tree.root',mcweight+'/1.447','SigGstar30001500Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=3000, m(Tp_{Nar})=1800',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_3000_1800_nominal_Tree.root',mcweight+'/1.447','SigGstar30001800Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=3000, m(Tp_{Nar})=2100',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_3000_2100_nominal_Tree.root',mcweight+'/1.447','SigGstar30002100Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=3500, m(Tp_{Nar})=1800',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_3500_1800_nominal_Tree.root',mcweight+'/1.447','SigGstar35001800Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=3500, m(Tp_{Nar})=2100',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_3500_2100_nominal_Tree.root',mcweight+'/1.447','SigGstar35002100Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=3500, m(Tp_{Nar})=2500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_3500_2500_nominal_Tree.root',mcweight+'/1.447','SigGstar35002500Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=4000, m(Tp_{Nar})=2100',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_4000_2100_nominal_Tree.root',mcweight+'/1.447','SigGstar40002100Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=4000, m(Tp_{Nar})=2500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_4000_2500_nominal_Tree.root',mcweight+'/1.447','SigGstar40002500Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=4000, m(Tp_{Nar})=3000',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_4000_3000_nominal_Tree.root',mcweight+'/1.447','SigGstar40003000Wid',allweightsystnames),
                    
                    Sample('Gstar->tWb, m(Gstar_{Nar})=1750, m(Tp_{Nar})=1300',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_1750_1300_nominal_Tree.root',mcweight+'/1.447','SigGstar17501300Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=2250, m(Tp_{Nar})=1300',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_2250_1300_nominal_Tree.root',mcweight+'/1.447','SigGstar22501300Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=2250, m(Tp_{Nar})=1500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_2250_1500_nominal_Tree.root',mcweight+'/1.447','SigGstar22501500Nar',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Nar})=2750, m(Tp_{Nar})=1500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Nar_2750_1500_nominal_Tree.root',mcweight+'/1.447','SigGstar27501500Nar',allweightsystnames),
                    
                    Sample('Gstar->tWb, m(Gstar_{Wid})=1750, m(Tp_{Nar})=1300',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_1750_1300_nominal_Tree.root',mcweight+'/1.447','SigGstar17501300Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=2250, m(Tp_{Nar})=1300',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_2250_1300_nominal_Tree.root',mcweight+'/1.447','SigGstar22501300Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=2250, m(Tp_{Nar})=1500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_2250_1500_nominal_Tree.root',mcweight+'/1.447','SigGstar22501500Wid',allweightsystnames),
                    Sample('Gstar->tWb, m(Gstar_{Wid})=2750, m(Tp_{Nar})=1500',ROOT.kMagenta+2,path_80x+'Signal_Zprime/Gstar_Wid_2750_1500_nominal_Tree.root',mcweight+'/1.447','SigGstar27501500Wid',allweightsystnames),

]

BackgroundSamples=[
                    Sample('t#bar{t} + jets',ROOT.kBlue,path_80x+'BKG_TTbar/*nominal*.root',mcweight,'ttbar',allweightsystnames), 
                    Sample('QCDMadgraph',ROOT.kOrange-3,path_80x+'BKG_QCD/MC_QCD_H*nominal*.root',mcweight,'QCDMadgraph',allweightsystnames),
                    
                    Sample('Signal Contamination (8.6pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta-3,path_80x+'Signal_Zprime/Zprime_1500_1200_nominal_Tree.root',mcweight+'/99.03*8.6','SC_Zprime15001200_8_6pb',allweightsystnames),  
                    Sample('Signal Contamination (0.3pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan-3,path_80x+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight+'/86.28*0.3','SC_Zprime20001200_0_3pb',allweightsystnames),  
                    Sample('Signal Contamination (0.3pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/37.6*0.3','SC_Zprime25001200_0_3pb',allweightsystnames),  
                    
                    Sample('Signal Contamination (0.8pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Zprime_1500_700_nominal_Tree.root',mcweight+'/95.06*0.80','SC_Zprime1500700_0_8pb',allweightsystnames),  
                    Sample('Signal Contamination (1.5pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta-8,path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight+'/138.07*1.5','SC_Zprime1500900_1_5pb',allweightsystnames),  
                    Sample('Signal Contamination (0.21pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900',ROOT.kCyan+1,path_80x+'Signal_Zprime/Zprime_2000_900_nominal_Tree.root',mcweight+'/55.83*0.21','SC_Zprime2000900_0_21pb',allweightsystnames),  
                    Sample('Signal Contamination (0.9pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kCyan-7,path_80x+'Signal_Zprime/Zprime_2000_1500_nominal_Tree.root',mcweight+'/83.47*0.90','SC_Zprime20001500_0_9pb',allweightsystnames),  
                    Sample('Signal Contamination (0.29pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kRed-2,path_80x+'Signal_Zprime/Zprime_2500_1500_nominal_Tree.root',mcweight+'/53.9*0.29','SC_Zprime25001500_0_29pb',allweightsystnames),  
                    
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=1500, m(Tp_{Nar})=800',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_1500_800_nominal_Tree.root',mcweight+'/1.447','SC_Gstar1500800Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=1500, m(Tp_{Nar})=1000',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_1500_1000_nominal_Tree.root',mcweight+'/1.447','SC_Gstar15001000Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=1500, m(Tp_{Nar})=1300',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_1500_1300_nominal_Tree.root',mcweight+'/1.447','SC_Gstar15001300Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=2000, m(Tp_{Nar})=1000',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_2000_1000_nominal_Tree.root',mcweight+'/1.447','SC_Gstar20001000Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=2000, m(Tp_{Nar})=1300',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_2000_1300_nominal_Tree.root',mcweight+'/1.447','SC_Gstar20001300Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=2000, m(Tp_{Nar})=1500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_2000_1500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar20001500Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=2500, m(Tp_{Nar})=1300',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_2500_1300_nominal_Tree.root',mcweight+'/1.447','SC_Gstar25001300Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=2500, m(Tp_{Nar})=1500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_2500_1500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar25001500Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=2500, m(Tp_{Nar})=1800',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_2500_1800_nominal_Tree.root',mcweight+'/1.447','SC_Gstar25001800Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=3000, m(Tp_{Nar})=1500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_3000_1500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar30001500Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=3000, m(Tp_{Nar})=1800',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_3000_1800_nominal_Tree.root',mcweight+'/1.447','SC_Gstar30001800Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=3000, m(Tp_{Nar})=2100',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_3000_2100_nominal_Tree.root',mcweight+'/1.447','SC_Gstar30002100Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=3500, m(Tp_{Nar})=1800',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_3500_1800_nominal_Tree.root',mcweight+'/1.447','SC_Gstar35001800Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=3500, m(Tp_{Nar})=2100',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_3500_2100_nominal_Tree.root',mcweight+'/1.447','SC_Gstar35002100Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=3500, m(Tp_{Nar})=2500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_3500_2500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar35002500Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=4000, m(Tp_{Nar})=2100',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_4000_2100_nominal_Tree.root',mcweight+'/1.447','SC_Gstar40002100Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=4000, m(Tp_{Nar})=2500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_4000_2500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar40002500Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=4000, m(Tp_{Nar})=3000',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_4000_3000_nominal_Tree.root',mcweight+'/1.447','SC_Gstar40003000Nar_1_4pb',allweightsystnames),


                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=1500, m(Tp_{Nar})=800',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_1500_800_nominal_Tree.root',mcweight+'/1.447','SC_Gstar1500800Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=1500, m(Tp_{Nar})=1000',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_1500_1000_nominal_Tree.root',mcweight+'/1.447','SC_Gstar15001000Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=1500, m(Tp_{Nar})=1300',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_1500_1300_nominal_Tree.root',mcweight+'/1.447','SC_Gstar15001300Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=2000, m(Tp_{Nar})=1000',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_2000_1000_nominal_Tree.root',mcweight+'/1.447','SC_Gstar20001000Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=2000, m(Tp_{Nar})=1300',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_2000_1300_nominal_Tree.root',mcweight+'/1.447','SC_Gstar20001300Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=2000, m(Tp_{Nar})=1500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_2000_1500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar20001500Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=2500, m(Tp_{Nar})=1300',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_2500_1300_nominal_Tree.root',mcweight+'/1.447','SC_Gstar25001300Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=2500, m(Tp_{Nar})=1500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_2500_1500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar25001500Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=2500, m(Tp_{Nar})=1800',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_2500_1800_nominal_Tree.root',mcweight+'/1.447','SC_Gstar25001800Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=3000, m(Tp_{Nar})=1500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_3000_1500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar30001500Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=3000, m(Tp_{Nar})=1800',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_3000_1800_nominal_Tree.root',mcweight+'/1.447','SC_Gstar30001800Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=3000, m(Tp_{Nar})=2100',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_3000_2100_nominal_Tree.root',mcweight+'/1.447','SC_Gstar30002100Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=3500, m(Tp_{Nar})=1800',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_3500_1800_nominal_Tree.root',mcweight+'/1.447','SC_Gstar35001800Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=3500, m(Tp_{Nar})=2100',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_3500_2100_nominal_Tree.root',mcweight+'/1.447','SC_Gstar35002100Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=3500, m(Tp_{Nar})=2500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_3500_2500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar35002500Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=4000, m(Tp_{Nar})=2100',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_4000_2100_nominal_Tree.root',mcweight+'/1.447','SC_Gstar40002100Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=4000, m(Tp_{Nar})=2500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_4000_2500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar40002500Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=4000, m(Tp_{Nar})=3000',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_4000_3000_nominal_Tree.root',mcweight+'/1.447','SC_Gstar40003000Wid_1_4pb',allweightsystnames),
                    
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=1750, m(Tp_{Nar})=1300',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_1750_1300_nominal_Tree.root',mcweight+'/1.447','SC_Gstar17501300Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=2250, m(Tp_{Nar})=1300',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_2250_1300_nominal_Tree.root',mcweight+'/1.447','SC_Gstar22501300Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=2250, m(Tp_{Nar})=1500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_2250_1500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar22501500Nar_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Nar})=2750, m(Tp_{Nar})=1500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Nar_2750_1500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar27501500Nar_1_4pb',allweightsystnames),
                    
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=1750, m(Tp_{Nar})=1300',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_1750_1300_nominal_Tree.root',mcweight+'/1.447','SC_Gstar17501300Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=2250, m(Tp_{Nar})=1300',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_2250_1300_nominal_Tree.root',mcweight+'/1.447','SC_Gstar22501300Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=2250, m(Tp_{Nar})=1500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_2250_1500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar22501500Wid_1_4pb',allweightsystnames),
                    Sample('Signal Contamination (1.4pb), m(Gstar_{Wid})=2750, m(Tp_{Nar})=1500',ROOT.kMagenta-5,path_80x+'Signal_Zprime/Gstar_Wid_2750_1500_nominal_Tree.root',mcweight+'/1.447','SC_Gstar27501500Wid_1_4pb',allweightsystnames),                    
                    
                    Sample('Signal Contamination none',ROOT.kRed-3,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/100000','SC_none',allweightsystnames),  
                    Sample('QCDPythia8',ROOT.kGreen+2,path_80x+'BKG_QCD/MC_QCD_P*nominal*Tree*.root',mcweight,'QCDPythia8',allweightsystnames),

]


DataSamples=[
                    Sample('Data = Background with (8.6pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_1500_1200_nominal_Tree.root',mcweight+'/99.03*8.6','DATA_Zprime15001200_8_6pb',allweightsystnames),     
                    Sample('Data = Background with (0.3pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight+'/86.28*0.3','DATA_Zprime20001200_0_3pb',allweightsystnames),     
                    Sample('Data = Background with (0.3pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1200',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/37.6*0.3','DATA_Zprime25001200_0_3pb',allweightsystnames),    
                    
                    Sample('Data = Background with (8.6pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_1500_700_nominal_Tree.root',mcweight+'/95.06*0.80','DATA_Zprime1500700_0_8pb',allweightsystnames),  
                    Sample('Data = Background with (1.5pb), m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight+'/138.07*1.5','DATA_Zprime1500900_1_5pb',allweightsystnames),  
                    Sample('Data = Background with (0.21pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=900',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_2000_900_nominal_Tree.root',mcweight+'/55.83*0.21','DATA_Zprime2000900_0_21pb',allweightsystnames),  
                    Sample('Data = Background with (0.9pb), m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_2000_1500_nominal_Tree.root',mcweight+'/83.47*0.90','DATA_Zprime20001500_0_9pb',allweightsystnames),  
                    Sample('Data = Background with (0.29pb), m(Zp_{Nar})=2500, m(Tp_{Nar,LH})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_2500_1500_nominal_Tree.root',mcweight+'/53.9*0.29','DATA_Zprime25001500_0_29pb',allweightsystnames),  
                    

                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=1500, m(Tp_{Nar})=800',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_1500_800_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar1500800Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=1500, m(Tp_{Nar})=1000',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_1500_1000_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar15001000Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=1500, m(Tp_{Nar})=1300',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_1500_1300_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar15001300Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=2000, m(Tp_{Nar})=1000',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_2000_1000_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar20001000Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=2000, m(Tp_{Nar})=1300',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_2000_1300_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar20001300Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=2000, m(Tp_{Nar})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_2000_1500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar20001500Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=2500, m(Tp_{Nar})=1300',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_2500_1300_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar25001300Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=2500, m(Tp_{Nar})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_2500_1500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar25001500Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=2500, m(Tp_{Nar})=1800',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_2500_1800_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar25001800Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=3000, m(Tp_{Nar})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_3000_1500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar30001500Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=3000, m(Tp_{Nar})=1800',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_3000_1800_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar30001800Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=3000, m(Tp_{Nar})=2100',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_3000_2100_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar30002100Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=3500, m(Tp_{Nar})=1800',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_3500_1800_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar35001800Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=3500, m(Tp_{Nar})=2100',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_3500_2100_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar35002100Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=3500, m(Tp_{Nar})=2500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_3500_2500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar35002500Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=4000, m(Tp_{Nar})=2100',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_4000_2100_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar40002100Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=4000, m(Tp_{Nar})=2500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_4000_2500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar40002500Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=4000, m(Tp_{Nar})=3000',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_4000_3000_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar40003000Nar_1_4pb',allweightsystnames),


                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=1500, m(Tp_{Nar})=800',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_1500_800_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar1500800Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=1500, m(Tp_{Nar})=1000',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_1500_1000_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar15001000Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=1500, m(Tp_{Nar})=1300',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_1500_1300_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar15001300Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=2000, m(Tp_{Nar})=1000',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_2000_1000_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar20001000Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=2000, m(Tp_{Nar})=1300',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_2000_1300_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar20001300Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=2000, m(Tp_{Nar})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_2000_1500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar20001500Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=2500, m(Tp_{Nar})=1300',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_2500_1300_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar25001300Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=2500, m(Tp_{Nar})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_2500_1500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar25001500Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=2500, m(Tp_{Nar})=1800',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_2500_1800_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar25001800Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=3000, m(Tp_{Nar})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_3000_1500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar30001500Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=3000, m(Tp_{Nar})=1800',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_3000_1800_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar30001800Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=3000, m(Tp_{Nar})=2100',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_3000_2100_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar30002100Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=3500, m(Tp_{Nar})=1800',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_3500_1800_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar35001800Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=3500, m(Tp_{Nar})=2100',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_3500_2100_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar35002100Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=3500, m(Tp_{Nar})=2500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_3500_2500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar35002500Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=4000, m(Tp_{Nar})=2100',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_4000_2100_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar40002100Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=4000, m(Tp_{Nar})=2500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_4000_2500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar40002500Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=4000, m(Tp_{Nar})=3000',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_4000_3000_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar40003000Wid_1_4pb',allweightsystnames),
                    
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=1750, m(Tp_{Nar})=1300',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_1750_1300_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar17501300Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=2250, m(Tp_{Nar})=1300',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_2250_1300_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar22501300Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=2250, m(Tp_{Nar})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_2250_1500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar22501500Nar_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Nar})=2750, m(Tp_{Nar})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Nar_2750_1500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar27501500Nar_1_4pb',allweightsystnames),
                    
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=1750, m(Tp_{Nar})=1300',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_1750_1300_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar17501300Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=2250, m(Tp_{Nar})=1300',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_2250_1300_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar22501300Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=2250, m(Tp_{Nar})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_2250_1500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar22501500Wid_1_4pb',allweightsystnames),
                    Sample('Data = Background with (1.4pb), m(Gstar_{Wid})=2750, m(Tp_{Nar})=1500',ROOT.kBlack+2,path_80x+'Signal_Zprime/Gstar_Wid_2750_1500_nominal_Tree.root',mcweight+'/1.447','DATA_Gstar27501500Wid_1_4pb',allweightsystnames),
                   
                   
                   
                    Sample('Data = Background with no signal',ROOT.kBlack+2,path_80x+'Signal_Zprime/Zprime_2500_1200_nominal_Tree.root',mcweight+'/100000.0','DATA_noSignal',allweightsystnames) ,     
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
  
samples=SignalSamples+BackgroundSamples+DataSamples

samplenames=SignalSampleNames+BackgroundSampleNames+DataSampleNames


#for sample,samplename in zip(samples,samplenames):
 #if (( 'QCDMadgraph' not in samplename ) and ( 'QCDPythia8' not in samplename )):   
  #for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    #thisnewsel=sample.selection
    #systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))

#for sample,samplename in zip(SignalSamples,SignalSampleNames):
 #if (( 'QCDMadgraph' not in samplename ) and ( 'QCDPythia8' not in samplename )):   
  #for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    #thisnewsel=sample.selection
    #SignalSamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
    #SignalSampleNames.append(sample.nick+sysname)
    #print 'with JEC ', sample.path

 #else:
  #for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    #thisnewsel=sample.selection
    #SignalSamples.append(Sample(sample.name+sysname,sample.color,sample.path,thisnewsel,sample.nick+sysname))
    #SignalSampleNames.append(sample.nick+sysname)     
    #print 'no JEC ', sample.path



#for sample,samplename in zip(BackgroundSamples,BackgroundSampleNames):
 #if (( 'QCDMadgraph' not in samplename ) and ( 'QCDPythia8' not in samplename )):   
  #for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    #thisnewsel=sample.selection
    #BackgroundSamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
    #BackgroundSampleNames.append(sample.nick+sysname)
    #print 'with JEC ', sample.path

 #else:
  #for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    #thisnewsel=sample.selection
    #BackgroundSamples.append(Sample(sample.name+sysname,sample.color,sample.path,thisnewsel,sample.nick+sysname))
    #BackgroundSampleNames.append(sample.nick+sysname)   
    #print 'no JEC ', sample.path



#for sample,samplename in zip(DataSamples,DataSampleNames):
 #if (( 'QCDMadgraph' not in samplename ) and ( 'QCDPythia8' not in samplename ) and ( 'BKG' not in samplename ) and ( 'DATA' not in samplename ) ):   
  #for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    #thisnewsel=sample.selection
    #DataSamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
    #DataSampleNames.append(sample.nick+sysname)
    #print 'with JEC ', sample.path

 #else:
  #for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    #thisnewsel=sample.selection
    #DataSamples.append(Sample(sample.name+sysname,sample.color,sample.path,thisnewsel,sample.nick+sysname))
    #DataSampleNames.append(sample.nick+sysname)  
    #print 'no JEC ', sample.path


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


