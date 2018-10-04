
import sys
import os
from scriptgenerator import *
from plotutils import *
from plot_cuts_ZPrime_MC import *

    
#weightsystnamesMadgraphbantiZprimeM=[
                    ##"",
                    #"_ABMadgraphbantiZprimeM_nominal",
                    #"_ABMadgraphbantiZprimeM_systUp",
                    #"_ABMadgraphbantiZprimeM_systDown",
#] 

#systweightsMadgraphbantiZprimeM=[
                    ##"nom:=1",
                    ##"ABMadgraphbantiZprimeM_nominal:=2",
                    #"ABMadgraphbantiZprimeM_nominal:=QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    ###"ABMadgraphbantiZprimeM_nominal:=2*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"ABMadgraphbantiZprimeM_systUp:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABMadgraphbantiZprimeM_systDown:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]


#weightsystnamesPythia8bantiZprimeM=[
                    #"_ABPythiabantiZprimeM_nominal",
                    #"_ABPythiabantiZprimeM_systUp",
                    #"_ABPythiabantiZprimeM_systDown",
#] 

#systweightsPythia8bantiZprimeM=[
                    #"ABPythiabantiZprimeM_nominal:=QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiabantiZprimeM_systUp:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiabantiZprimeM_systDown:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]
 
#weightsystnamesGeneratorDiffMadgraphbantiZprimeM=[
                    #"_ABMadgraphbantiZprimeMGeneratorDiff_systUp",
                    #"_ABMadgraphbantiZprimeMGeneratorDiff_systDown",
#]

#systweightsGeneartorDiffMadgraphbantiZprimeM=[
                    #"ABMadgraphbantiZprimeMGeneratorDiff_systUp:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABMadgraphbantiZprimeMGeneratorDiff_systDown:=(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]
 
#weightsystnamesGeneratorDiffPythia8bantiZprimeM=[
                    #"_ABPythiabantiZprimeMGeneratorDiff_systUp",
                    #"_ABPythiabantiZprimeMGeneratorDiff_systDown",
#]

#systweightsGeneartorDiffPythia8bantiZprimeM=[
                    #"ABPythiabantiZprimeMGeneratorDiff_systUp:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiabantiZprimeMGeneratorDiff_systDown:=(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]
    
 
#weightsystnamesMadgraphtantiTopPt=[
                    #"_ABMadgraphtantiTopPt_nominal",
                    #"_ABMadgraphtantiTopPt_systUp",
                    #"_ABMadgraphtantiTopPt_systDown",
#] 

#systweightsMadgraphtantiTopPt=[
                    #"ABMadgraphtantiTopPt_nominal:=QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABMadgraphtantiTopPt_systUp:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt+QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABMadgraphtantiTopPt_systDown:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]


#weightsystnamesPythia8tantiTopPt=[
                    #"_ABPythiatantiTopPt_nominal",
                    #"_ABPythiatantiTopPt_systUp",
                    #"_ABPythiatantiTopPt_systDown",
#] 

#systweightsPythia8tantiTopPt=[
                    #"ABPythiatantiTopPt_nominal:=QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiatantiTopPt_systUp:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt + QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiatantiTopPt_systDown:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt - QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]

#weightsystnamesGeneratorDiffMadgraphtantiTopPt=[
                    #"_ABMadgraphtantiTopPtGeneratorDiff_systUp",
                    #"_ABMadgraphtantiTopPtGeneratorDiff_systDown",
#]

#systweightsGeneartorDiffMadgraphtantiTopPt=[
                    #"ABMadgraphtantiTopPtGeneratorDiff_systUp:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt + abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABMadgraphtantiTopPtGeneratorDiff_systDown:=(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt - abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]
 
#weightsystnamesGeneratorDiffPythia8tantiTopPt=[
                    #"_ABPythiatantiTopPtGeneratorDiff_systUp",
                    #"_ABPythiatantiTopPtGeneratorDiff_systDown",
#]

#systweightsGeneartorDiffPythia8tantiTopPt=[
                    #"ABPythiatantiTopPtGeneratorDiff_systUp:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt+ abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiatantiTopPtGeneratorDiff_systDown:=(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt- abs( QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]




##########################################################################
  
    
#weightsystnamesMadgraphbantiZprimeMWithtopbtag=[
                    #"_ABMadgraphbantiZprimeMWithtopbtag_nominal",
                    #"_ABMadgraphbantiZprimeMWithtopbtag_systUp",
                    #"_ABMadgraphbantiZprimeMWithtopbtag_systDown",
#] 
#systweightsMadgraphbantiZprimeMWithtopbtag=[
                    ##"ABMadgraphbantiZprimeMWithtopbtag_nominal:=2",
                    #"ABMadgraphbantiZprimeMWithtopbtag_nominal:=QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    ###"ABMadgraphbantiZprimeMWithtopbtag_nominal:=2*(DoWeights==1)+(DoWeights==0)*1.0",
                    #"ABMadgraphbantiZprimeMWithtopbtag_systUp:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABMadgraphbantiZprimeMWithtopbtag_systDown:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]


#weightsystnamesPythia8bantiZprimeMWithtopbtag=[
                    #"_ABPythiabantiZprimeMWithtopbtag_nominal",
                    #"_ABPythiabantiZprimeMWithtopbtag_systUp",
                    #"_ABPythiabantiZprimeMWithtopbtag_systDown",
#] 
#systweightsPythia8bantiZprimeMWithtopbtag=[
                    #"ABPythiabantiZprimeMWithtopbtag_nominal:=QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiabantiZprimeMWithtopbtag_systUp:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiabantiZprimeMWithtopbtag_systDown:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]
 
#weightsystnamesGeneratorDiffMadgraphbantiZprimeMWithtopbtag=[
                    #"_ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systUp",
                    #"_ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systDown",
#]

#systweightsGeneartorDiffMadgraphbantiZprimeMWithtopbtag=[
                    #"ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systUp:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABMadgraphbantiZprimeMWithtopbtagGeneratorDiff_systDown:=(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]
 
#weightsystnamesGeneratorDiffPythia8bantiZprimeMWithtopbtag=[
                    #"_ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systUp",
                    #"_ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systDown",
#]

#systweightsGeneartorDiffPythia8bantiZprimeMWithtopbtag=[
                    #"ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systUp:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M+ abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiabantiZprimeMWithtopbtagGeneratorDiff_systDown:=(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M- abs( QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M-QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]
    
 
#weightsystnamesMadgraphtantiTopPtWithtopbtag=[
                    #"_ABMadgraphtantiTopPtWithtopbtag_nominal",
                    #"_ABMadgraphtantiTopPtWithtopbtag_systUp",
                    #"_ABMadgraphtantiTopPtWithtopbtag_systDown",
#] 

#systweightsMadgraphtantiTopPtWithtopbtag=[
                    #"ABMadgraphtantiTopPtWithtopbtag_nominal:=QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABMadgraphtantiTopPtWithtopbtag_systUp:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt+QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABMadgraphtantiTopPtWithtopbtag_systDown:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]


#weightsystnamesPythia8tantiTopPtWithtopbtag=[
                    #"_ABPythiatantiTopPtWithtopbtag_nominal",
                    #"_ABPythiatantiTopPtWithtopbtag_systUp",
                    #"_ABPythiatantiTopPtWithtopbtag_systDown",
#] 

#systweightsPythia8tantiTopPtWithtopbtag=[
                    #"ABPythiatantiTopPtWithtopbtag_nominal:=QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiatantiTopPtWithtopbtag_systUp:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt + QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systUp)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiatantiTopPtWithtopbtag_systDown:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt - QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt_systDown)*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]

#weightsystnamesGeneratorDiffMadgraphtantiTopPtWithtopbtag=[
                    #"_ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systUp",
                    #"_ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systDown",
#]

#systweightsGeneartorDiffMadgraphtantiTopPtWithtopbtag=[
                    #"ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systUp:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt + abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABMadgraphtantiTopPtWithtopbtagGeneratorDiff_systDown:=(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt - abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]
 
#weightsystnamesGeneratorDiffPythia8tantiTopPtWithtopbtag=[
                    #"_ABPythiatantiTopPtWithtopbtagGeneratorDiff_systUp",
                    #"_ABPythiatantiTopPtWithtopbtagGeneratorDiff_systDown",
#]

#systweightsGeneartorDiffPythia8tantiTopPtWithtopbtag=[
                    #"ABPythiatantiTopPtWithtopbtagGeneratorDiff_systUp:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt+ abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
                    #"ABPythiatantiTopPtWithtopbtagGeneratorDiff_systDown:=(QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt- abs( QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt-QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt))*(DoABCDsyst==1)+1*(DoABCDsyst==0)",
#]

if topWP=='loose' and WWP=='loose' and bottomWP=='medium':

  if ABCDversion is 'ABCD3':            
    weightsystnamesABCD=[
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
    weightsystnamesABCD=[
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
    
elif topWP=='loose' and WWP=='medium' and bottomWP=='medium':
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
    
    
if topWP=='loose' and WWP=='loose' and bottomWP=='medium':

    systweightsABCD=[
                    
                    "" + ABCDversion + "_ABCD_rateUp:=ABCD_rate_systUp*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "" + ABCDversion + "_ABCD_rateDown:=ABCD_rate_systDown*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "" + ABCDversion + "_ABCD_shapeUp:=ABCD_shape_systUp*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "" + ABCDversion + "_ABCD_shapeDown:=ABCD_shape_systDown*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
            
    ]
    if ABCDversion is 'ABCD3': 
        systweightsABCD=systweightsABCD+[
                    "ABCD3_inclusive_ZprimeM_systUp:= pow(1+0.019232,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_inclusive_ZprimeM_systDown:= pow(1-0.019232,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_notopbtag_ZprimeM_systUp:= pow(1+0.015085,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_notopbtag_ZprimeM_systDown:= pow(1-0.015085,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_withtopbtag_ZprimeM_systUp:= pow(1+0.13,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_withtopbtag_ZprimeM_systDown:= pow(1-0.13,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_inclusive_TprimeM_systUp:= pow(1+0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_inclusive_TprimeM_systDown:= pow(1-0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_notopbtag_TprimeM_systUp:= pow(1+0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_notopbtag_TprimeM_systDown:= pow(1-0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_withtopbtag_TprimeM_systUp:= pow(1+0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_withtopbtag_TprimeM_systDown:= pow(1-0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",          
          
        ]
    elif ABCDversion is 'ABCD5': 
        systweightsABCD=systweightsABCD+[ 
                    "ABCD5_inclusive_ZprimeM_systUp:= pow(1+0.03681,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_inclusive_ZprimeM_systDown:= pow(1-0.03681,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_notopbtag_ZprimeM_systUp:= pow(1+0.03671,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_notopbtag_ZprimeM_systDown:= pow(1-0.03671,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_withtopbtag_ZprimeM_systUp:= pow(1+0.033691,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_withtopbtag_ZprimeM_systDown:= pow(1-0.033691,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_inclusive_TprimeM_systUp:= pow(1+0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_inclusive_TprimeM_systDown:= pow(1-0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_notopbtag_TprimeM_systUp:= pow(1+0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_notopbtag_TprimeM_systDown:= pow(1-0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_withtopbtag_TprimeM_systUp:= pow(1+0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_withtopbtag_TprimeM_systDown:= pow(1-0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",       
        ]

    
elif topWP=='loose' and WWP=='medium' and bottomWP=='medium':
    systweightsABCD=[
                    
                    "" + ABCDversion + "_ABCD_rateUp:=ABCD_rate_systUp*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "" + ABCDversion + "_ABCD_rateDown:=ABCD_rate_systDown*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "" + ABCDversion + "_ABCD_shapeUp:=ABCD_shape_systUp*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "" + ABCDversion + "_ABCD_shapeDown:=ABCD_shape_systDown*(DoABCDsyst==1)+MCSF_Weight_" + ABCDversion +"*(DoMCDataWeights==1)*(DoABCDsyst==0)",
            
    ]
                    #"nom:=1",
                    
    if ABCDversion is 'ABCD3': 
        systweightsABCD=systweightsABCD+[
                    "ABCD3_inclusive_ZprimeM_systUp:= pow(1+0.019232,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_inclusive_ZprimeM_systDown:= pow(1-0.019232,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_notopbtag_ZprimeM_systUp:= pow(1+0.01299,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_notopbtag_ZprimeM_systDown:= pow(1-0.01299,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_withtopbtag_ZprimeM_systUp:= pow(1+0.075,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD3_withtopbtag_ZprimeM_systDown:= pow(1-0.075,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_inclusive_TprimeM_systUp:= pow(1+0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_inclusive_TprimeM_systDown:= pow(1-0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_notopbtag_TprimeM_systUp:= pow(1+0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_notopbtag_TprimeM_systDown:= pow(1-0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_withtopbtag_TprimeM_systUp:= pow(1+0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD3_withtopbtag_TprimeM_systDown:= pow(1-0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD3*(DoMCDataWeights==1)*(DoABCDsyst==0)",          
          
        ]
    elif ABCDversion is 'ABCD5': 
      if (not WZwindow) and fullWMSD:  
        systweightsABCD=systweightsABCD+[ 
                    "ABCD5_inclusive_ZprimeM_systUp:= pow(1+0.03681,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_inclusive_ZprimeM_systDown:= pow(1-0.03681,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_notopbtag_ZprimeM_systUp:= pow(1+0.03894,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_notopbtag_ZprimeM_systDown:= pow(1-0.03894,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_withtopbtag_ZprimeM_systUp:= pow(1+0.15223,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_withtopbtag_ZprimeM_systDown:= pow(1-0.15223,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_inclusive_TprimeM_systUp:= pow(1+0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_inclusive_TprimeM_systDown:= pow(1-0.01731,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_notopbtag_TprimeM_systUp:= pow(1+0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_notopbtag_TprimeM_systDown:= pow(1-0.01194,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_withtopbtag_TprimeM_systUp:= pow(1+0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    #"ABCD5_withtopbtag_TprimeM_systDown:= pow(1-0.082416,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",        
                    ]
      if WZwindow and fullWMSD:
        systweightsABCD=systweightsABCD+[ 
                    "ABCD5_inclusive_ZprimeM_systUp:= pow(1+0.03681,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_inclusive_ZprimeM_systDown:= pow(1-0.03681,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_notopbtag_ZprimeM_systUp:= pow(1+0.06,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_notopbtag_ZprimeM_systDown:= pow(1-0.06,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_withtopbtag_ZprimeM_systUp:= pow(1+0.09,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    "ABCD5_withtopbtag_ZprimeM_systDown:= pow(1-0.09,1.0/1.0)*(DoABCDsyst==1)+MCSF_Weight_ABCD5*(DoMCDataWeights==1)*(DoABCDsyst==0)",
                    ]
    else:
        print "Wrong WPs"
        raw_input()
else:
    print "Wrong WPs"
    raw_input()

weigthsystnamesMCSFs=[

                    "",
                    
                    #"_" + ABCDversion + "_nominal",
                    
                    #"_" + ABCDversion + "_MCSF_CSVLFUp",
                    #"_" + ABCDversion + "_MCSF_CSVLFDown",
                    #"_" + ABCDversion + "_MCSF_CSVHFUp",
                    #"_" + ABCDversion + "_MCSF_CSVHFDown",
                    #"_" + ABCDversion + "_MCSF_CSVHFStats1Up",
                    #"_" + ABCDversion + "_MCSF_CSVHFStats1Down",
                    #"_" + ABCDversion + "_MCSF_CSVLFStats1Up",
                    #"_" + ABCDversion + "_MCSF_CSVLFStats1Down",
                    #"_" + ABCDversion + "_MCSF_CSVHFStats2Up",
                    #"_" + ABCDversion + "_MCSF_CSVHFStats2Down",
                    #"_" + ABCDversion + "_MCSF_CSVLFStats2Up",
                    #"_" + ABCDversion + "_MCSF_CSVLFStats2Down",
                    #"_" + ABCDversion + "_MCSF_CSVCErr1Up",
                    #"_" + ABCDversion + "_MCSF_CSVCErr1Down",
                    #"_" + ABCDversion + "_MCSF_CSVCErr2Up",
                    #"_" + ABCDversion + "_MCSF_CSVCErr2Down",
                    #"_" + ABCDversion + "_MCSF_toptagUp",
                    #"_" + ABCDversion + "_MCSF_toptagDown",
                    #"_" + ABCDversion + "_MCSF_WtagUp",
                    #"_" + ABCDversion + "_MCSF_WtagDown",
                    #"_" + ABCDversion + "_MCSF_PUUp",
                    #"_" + ABCDversion + "_MCSF_PUDown",
                    #"_" + ABCDversion + "_MCSF_PDFUp",
                    #"_" + ABCDversion + "_MCSF_PDFDown",  
                    #"_" + ABCDversion + "_MCSF_LumiUp",
                    #"_" + ABCDversion + "_MCSF_LumiDown",
                    #"_" + ABCDversion + "_MCSF_TriggerUp",
                    #"_" + ABCDversion + "_MCSF_TriggerDown",
                    #"_" + ABCDversion + "_MCSF_renfac_envUp",
                    #"_" + ABCDversion + "_MCSF_renfac_envDown",
                    #"_" + ABCDversion + "_ttbarXSUp",
                    #"_" + ABCDversion + "_ttbarXSDown",
                    
                    #"_" + ABCDversion + "_MCSF_renfacUp",
                    #"_" + ABCDversion + "_MCSF_renfacDown",
                    #"_" + ABCDversion + "_MCSF_renUp",
                    #"_" + ABCDversion + "_MCSF_renDown",
                    #"_" + ABCDversion + "_MCSF_facUp",
                    #"_" + ABCDversion + "_MCSF_facDown",
                    
                    
                    #"_All_nominal",
                    
                    #"_All_MCSF_CSVLFUp",
                    #"_All_MCSF_CSVLFDown",
                    #"_All_MCSF_CSVHFUp",
                    #"_All_MCSF_CSVHFDown",
                    #"_All_MCSF_CSVHFStats1Up",
                    #"_All_MCSF_CSVHFStats1Down",
                    #"_All_MCSF_CSVLFStats1Up",
                    #"_All_MCSF_CSVLFStats1Down",
                    #"_All_MCSF_CSVHFStats2Up",
                    #"_All_MCSF_CSVHFStats2Down",
                    #"_All_MCSF_CSVLFStats2Up",
                    #"_All_MCSF_CSVLFStats2Down",
                    #"_All_MCSF_CSVCErr1Up",
                    #"_All_MCSF_CSVCErr1Down",
                    #"_All_MCSF_CSVCErr2Up",
                    #"_All_MCSF_CSVCErr2Down",                    
                    #"_All_MCSF_PUUp",
                    #"_All_MCSF_PUDown",
                    #"_All_MCSF_PDFUp",
                    #"_All_MCSF_PDFDown",  
                    #"_All_MCSF_LumiUp",
                    #"_All_MCSF_LumiDown",
                    #"_All_MCSF_TriggerUp",
                    #"_All_MCSF_TriggerDown",
                    #"_All_MCSF_renfac_envUp",
                    #"_All_MCSF_renfac_envDown",
                    #"_All_ttbarXSUp",
                    #"_All_ttbarXSDown",
                    
                    #"_Nobtagging_nominal",
                    #"_Nobtagging_MCSF_PUUp",
                    #"_Nobtagging_MCSF_PUDown",
                    #"_Nobtagging_MCSF_PDFUp",
                    #"_Nobtagging_MCSF_PDFDown",  
                    #"_Nobtagging_MCSF_LumiUp",
                    #"_Nobtagging_MCSF_LumiDown",
                    #"_Nobtagging_MCSF_TriggerUp",
                    #"_Nobtagging_MCSF_TriggerDown",
                    #"_Nobtagging_MCSF_renfac_envUp",
                    #"_Nobtagging_MCSF_renfac_envDown",
                    #"_Nobtagging_ttbarXSUp",
                    #"_Nobtagging_ttbarXSDown",                    
]
          

    

systweightnamesMCSFs=[

                    
                    "nom:=1.0",
                    
                    #"" + ABCDversion + "_nominal:=(MCSF_Weight_" + ABCDversion + ")*(DoWeights==1)+(DoWeights==0)*triggered",
                    
                    
                    
                    #"" + ABCDversion + "_MCSF_CSVLFUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFUp)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVLFDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFDown)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVHFUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFUp)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVHFDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFDown)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVHFStats1Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFStats1Up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVHFStats1Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFStats1Down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVLFStats1Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFStats1Up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVLFStats1Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFStats1Down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVHFStats2Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFStats2Up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVHFStats2Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVHFStats2Down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVLFStats2Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFStats2Up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVLFStats2Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVLFStats2Down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVCErr1Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVCErr1Up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVCErr1Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVCErr1Down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVCErr2Up:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVCErr2Up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_CSVCErr2Down:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_WeightCSVnominal*" + ABCDversion + "_WeightCSVCErr2Down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_toptagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightUp)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_toptagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_toptagweightnominal*" + ABCDversion + "_toptagweightDown)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_WtagUp:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtagweightnominal*" + ABCDversion + "_WtagweightUp)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_WtagDown:=(MCSF_Weight_" + ABCDversion + "/" + ABCDversion + "_Wtagweightnominal*" + ABCDversion + "_WtagweightDown)*(DoWeights==1)+(DoWeights==0)*triggered",      
                    
                    #"" + ABCDversion + "_MCSF_PUUp:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_PUDown:=(MCSF_Weight_" + ABCDversion + "/Weight_pu69p2*Weight_pu69p2Down)*(DoWeights==1)+(DoWeights==0)*triggered", 
                    #"" + ABCDversion + "_MCSF_PDFUp:=(MCSF_Weight_" + ABCDversion + "/PDF_RMSMean*PDF_RMSUp)*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*triggered",
                    #"" + ABCDversion + "_MCSF_PDFDown:=(MCSF_Weight_" + ABCDversion + "/PDF_RMSMean*PDF_RMSDown)*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*triggered",
                    #"" + ABCDversion + "_MCSF_LumiUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.025))*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_LumiDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.025))*(DoWeights==1)+(DoWeights==0)*triggered", 
                    #"" + ABCDversion + "_MCSF_TriggerUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.016))*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_TriggerDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.016))*(DoWeights==1)+(DoWeights==0)*triggered", 
                    
                    #"" + ABCDversion + "_MCSF_renfac_envUp:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeUp)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_renfac_envDown:=(MCSF_Weight_" + ABCDversion + "*MCSF_RenFac_envelopeDown)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_ttbarXSUp:=(MCSF_Weight_" + ABCDversion + "*(1.0+0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*triggered",
                    #"" + ABCDversion + "_ttbarXSDown:=(MCSF_Weight_" + ABCDversion + "*(1.0-0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*triggered",
                 
                 
                    #"" + ABCDversion + "_MCSF_renfacUp:=(Weight_scale_variation_muR2p0_muF2p0)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_renfacDown:=(Weight_scale_variation_muR0p5_muF0p5)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_renUp:=(Weight_scale_variation_muR2p0_muF1p0)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_renDown:=(Weight_scale_variation_muR0p5_muF1p0)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_facUp:=(Weight_scale_variation_muR1p0_muF2p0)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"" + ABCDversion + "_MCSF_facDown:=(Weight_scale_variation_muR1p0_muF0p5)*(DoWeights==1)+(DoWeights==0)*triggered", 
                    
                    
                    
                    #"All_nominal:=(MCSF_Weight_All)*(DoWeights==1)+(DoWeights==0)*triggered",
                    
                    #"All_MCSF_CSVLFUp:=(MCSF_Weight_All/Weight_CSV*Weight_CSVLFup)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVLFDown:=(MCSF_Weight_All/Weight_CSV*Weight_CSVLFdown)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVHFUp:=(MCSF_Weight_All/Weight_CSV*Weight_CSVHFup)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVHFDown:=(MCSF_Weight_All/Weight_CSV*Weight_CSVHFdown)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVHFStats1Up:=(MCSF_Weight_All/Weight_CSV*Weight_CSVHFStats1up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVHFStats1Down:=(MCSF_Weight_All/Weight_CSV*Weight_CSVHFStats1down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVLFStats1Up:=(MCSF_Weight_All/Weight_CSV*Weight_CSVLFStats1up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVLFStats1Down:=(MCSF_Weight_All/Weight_CSV*Weight_CSVLFStats1down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVHFStats2Up:=(MCSF_Weight_All/Weight_CSV*Weight_CSVHFStats2up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVHFStats2Down:=(MCSF_Weight_All/Weight_CSV*Weight_CSVHFStats2down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVLFStats2Up:=(MCSF_Weight_All/Weight_CSV*Weight_CSVLFStats2up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVLFStats2Down:=(MCSF_Weight_All/Weight_CSV*Weight_CSVLFStats2down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVCErr1Up:=(MCSF_Weight_All/Weight_CSV*Weight_CSVCErr1up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVCErr1Down:=(MCSF_Weight_All/Weight_CSV*Weight_CSVCErr1down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVCErr2Up:=(MCSF_Weight_All/Weight_CSV*Weight_CSVCErr2up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_CSVCErr2Down:=(MCSF_Weight_All/Weight_CSV*Weight_CSVCErr2down)*(DoWeights==1)+(DoWeights==0)*triggered",
                    
                    #"All_MCSF_PUUp:=(MCSF_Weight_All/Weight_pu69p2*Weight_pu69p2Up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_PUDown:=(MCSF_Weight_All/Weight_pu69p2*Weight_pu69p2Down)*(DoWeights==1)+(DoWeights==0)*triggered", 
                    #"All_MCSF_PDFUp:=(MCSF_Weight_All/PDF_RMSMean*PDF_RMSUp)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_PDFDown:=(MCSF_Weight_All/PDF_RMSMean*PDF_RMSDown)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_LumiUp:=(MCSF_Weight_All*(1.0+0.025))*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_LumiDown:=(MCSF_Weight_All*(1.0-0.025))*(DoWeights==1)+(DoWeights==0)*triggered", 
                    #"All_MCSF_TriggerUp:=(MCSF_Weight_All*(1.0+0.03))*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_TriggerDown:=(MCSF_Weight_All*(1.0-0.03))*(DoWeights==1)+(DoWeights==0)*triggered", 
                    
                    #"All_MCSF_renfac_envUp:=(MCSF_Weight_All*MCSF_RenFac_envelopeUp)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_MCSF_renfac_envDown:=(MCSF_Weight_All*MCSF_RenFac_envelopeDown)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"All_ttbarXSUp:=(MCSF_Weight_All*(1.0+0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*triggered",
                    #"All_ttbarXSDown:=(MCSF_Weight_All*(1.0-0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*triggered",
                                    
                    
                    #"Nobtagging_nominal:=(MCSF_Weight_Nobtagging)*(DoWeights==1)+(DoWeights==0)*triggered",
                    
                    #"Nobtagging_MCSF_PUUp:=(Nobtagging_nominal/Weight_pu69p2*Weight_pu69p2Up)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"Nobtagging_MCSF_PUDown:=(Nobtagging_nominal/Weight_pu69p2*Weight_pu69p2Down)*(DoWeights==1)+(DoWeights==0)*triggered", 
                    #"Nobtagging_MCSF_PDFUp:=(Nobtagging_nominal/PDF_RMSMean*PDF_RMSUp)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"Nobtagging_MCSF_PDFDown:=(Nobtagging_nominal/PDF_RMSMean*PDF_RMSDown)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"Nobtagging_MCSF_LumiUp:=(Nobtagging_nominal*(1.0+0.025))*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"Nobtagging_MCSF_LumiDown:=(Nobtagging_nominal*(1.0-0.025))*(DoWeights==1)+(DoWeights==0)*triggered", 
                    #"Nobtagging_MCSF_TriggerUp:=(Nobtagging_nominal*(1.0+0.03))*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"Nobtagging_MCSF_TriggerDown:=(Nobtagging_nominal*(1.0-0.03))*(DoWeights==1)+(DoWeights==0)*triggered", 

                    #"Nobtagging_MCSF_renfac_envUp:=(Nobtagging_nominal*MCSF_RenFac_envelopeUp)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"Nobtagging_MCSF_renfac_envDown:=(Nobtagging_nominal*MCSF_RenFac_envelopeDown)*(DoWeights==1)+(DoWeights==0)*triggered",
                    #"Nobtagging_ttbarXSUp:=(Nobtagging_nominal*(1.0+0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*triggered",
                    #"Nobtagging_ttbarXSDown:=(Nobtagging_nominal*(1.0-0.05))*(DoWeights*DoMCDataWeights_ttbaronly==1)+(DoWeights*DoMCDataWeights_ttbaronly==0)*triggered",
                                    
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

assert len(otherSystNames)==len(otherSystFileNames)

     
allweightsystnames=weigthsystnamesMCSFs+weightsystnamesABCD+JECsystnames

allsystweights=systweightnamesMCSFs+systweightsABCD

# names of the systematics (proper names needed e.g. for combination)
mcweight='35.9'

ttbarXS_MCgen='730.0'
ttbarXS_NLO='831.76' 
rateunc_ttbarXS_Up=math.sqrt(19.77*19.77 + 35.06*35.06)
rateunc_ttbarXS_Down=math.sqrt(29.20*29.20 + 35.06*35.06)

sfs="Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"
usualweights="(1*Weight_PU*((Weight>0)-(Weight<0)))*Weight_ElectronSFID*Weight_ElectronSFTrigger*Weight_ElectronSFIso*Weight_MuonSFID*Weight_MuonSFTrigger*Weight_MuonSFIso"


# samples
# input paths
path_80x_MC="/nfs/dust/cms/user/skudella/processed_MC/flat_trees_new/"
path_80x_DATA="/nfs/dust/cms/user/skudella/processed_DATA/flat_trees/"

path_new="/pnfs/desy.de/cms/tier2/store/user/skudella/"
path="/pnfs/desy.de/cms/tier2/store/user/skudella/*/MC_limits_*/*/*/*"


SignalSamples=[
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=700',ROOT.kMagenta,path_80x_MC+'Signal_Zprime/Zprime_1500_700_nominal_Tree.root',mcweight,'Zprime1500700') ,
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=900',ROOT.kMagenta+2,path_80x_MC+'Signal_Zprime/Zprime_1500_900_nominal_Tree.root',mcweight,'Zprime1500900'),
                    #Sample('Z->tWb, m(Zp_{Nar})=1500, m(Tp_{Nar,LH})=1200',ROOT.kMagenta-9,path_80x_MC+'Signal_Zprime/Zprime_1500_1200_nominal_Tree.root',mcweight,'Zprime15001200'),
                    #Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1200',ROOT.kCyan,path_80x_MC+'Signal_Zprime/Zprime_2000_1200_LH_nominal_Tree.root',mcweight,'Zprime20001200'),
                    #Sample('Z->tWb, m(Zp_{Nar})=2000, m(Tp_{Nar,LH})=1500',ROOT.kCyan+3,path_80x_MC+'Signal_Zprime/Zprime_2000_1500_nominal_Tree.root',mcweight,'Zprime20001500'),
                    #Sample('Signal',ROOT.kRed,path_80x_MC+'Signal_Zprime/Zprime*nominal*Tree.root',mcweight+'/35.9' ,'Zprimeall',allweightsystnames),
                    #Sample('Signal (1pb)',ROOT.kRed,path_80x_MC+'Signal_Zprime/Zprime*ToWB*2500*1200*nominal*Tree.root',mcweight+'/37.6' ,'Zprimeall',allweightsystnames),
                    #Sample("Sig. m_{Z'}=1.5 TeV, m_{T}=0.7 TeV",ROOT.kMagenta,path_80x_MC+'Signal_Zprime/Zprime*ToWB*1500*700*nominal*Tree.root',mcweight+'/95.06*0.80','Zprimeall',allweightsystnames) ,
                    
                    Sample('Sig. m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700',ROOT.kMagenta-7,path+'Zprime*ToWB*Mzp-1500Nar*700Nar*nominal*Tree*.root',mcweight+'/95.06*232956.0/232893.0','Zprimeall',allweightsystnames),
                    #Sample('Sig. m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700',ROOT.kMagenta-7,path+'Zprime*ToZT*Mzp-1500Nar*700Nar*nominal*Tree*.root',mcweight+'/186.7*197390.0/197390.0','Zprimeall',allweightsystnames),
                    #Sample('Sig. m(Z\'_{Nar})=1500, m(T\'_{Nar,LH})=700',ROOT.kMagenta-7,path+'Zprime*ToHT*Mzp-1500Nar*700Nar*nominal*Tree*.root',mcweight+'/3.62*207419.0/207388.0','Zprimeall',allweightsystnames),


]

BackgroundSamples=[
                    #Sample('t#bar{t}',ROOT.kBlue-4,path_80x_MC+'BKG_TTbar/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',allweightsystnames) ,
                    Sample('Top background',ROOT.kBlue-4,path_new+'TT_*/MC_limits*/*/*/*nominal*.root',mcweight+'/'+ttbarXS_MCgen+'*'+ttbarXS_NLO,'ttbar',allweightsystnames) ,
                    Sample('single top (tW-channel)',ROOT.kBlue+2,path_new+'ST_tW*/MC_limits*/*/*/*nominal*.root',mcweight,'ST_tW',allweightsystnames) ,
                    Sample('single top (t-channel)',ROOT.kBlue-9,path_new+'ST_t-*/MC_limits*/*/*/*nominal*.root',mcweight,'ST_t',allweightsystnames) ,
                    Sample('single top (s-channel)',ROOT.kBlue-7,path_new+'ST_s*/MC_limits*/*/*/*nominal*.root',mcweight,'ST_s',allweightsystnames) ,
                    Sample('QCD background from MC',ROOT.kOrange-3,path_80x_MC+'BKG_QCD/*QCD_H*nominal*Tree*.root',mcweight,'QCDMadgraph',allweightsystnames),
]


DataSamples=[
                    Sample('data',ROOT.kBlack,path_80x_DATA+'*nominal*.root','1.0','DATA_2016'),
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




systsamples=[]
for sample,samplename in zip(samples,samplenames):
 #if (( 'QCDPythia8' not in samplename ) and ( 'BKG' not in samplename ) and ( 'DATA_2016' not in samplename ) ):   
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


