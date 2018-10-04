#############
# plot general control distributions
##############

from plotconfig_Zprime_MC_Lena import *
from plot_additional_Zprime_MC_Lena import *
from plot_cuts_ZPrime_MC_Lena import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy



ABCDeventhandling='oncefirst'
#ABCDeventhandling='reweight'

name='Zprime_MC_ABCD'+radi+'_'+ABCDeventhandling+'_'+WPs
#SampleNames=['ttbar' , 'QCD_HT', 'QCD_Pt' ]
#SignalSampleNames=['Zprime1500900',  'Zprime20001200',  'Zprime25001200']

plots=[




    #All elements
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_top_MSD" ,"tau_{32}(t) VS m_{SD}(t)",20,0,1,60,0,300),"Tops_ABCD"+radi+"_MSD","Tops_ABCD"+radi+"_t32",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_W_tau21" ,"tau_{32}(t) VS tau_{21}(W)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Ws_ABCD"+radi+"_t21",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_t_MSD,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_W_MSD" ,"tau_{32}(t) VS m_{SD}(W)",20,0,1,60,0,300),"Tops_ABCD"+radi+"_t32","Ws_ABCD"+radi+"_MSD",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_tau21 + " && " + plotselection_t_MSD,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_t_MSD,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_TprimeM" ,"tau_{32}(t) VS m(T')",20,0,1,50,0,2500),"Tops_ABCD"+radi+"_t32","Tprimes_ABCD"+radi+"_M",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_t_MSD,"1 btag"),
    
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_MSD_vs_W_tau21" ,"m_{SD}(t) VS tau_{21}(W)",60,0,300,20,0,1),"Tops_ABCD"+radi+"_MSD","Ws_ABCD"+radi+"_t21",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_tau32,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_MSD_vs_W_MSD" ,"m_{SD}(t) VS m_{SD}(t)(W)",60,0,300,60,0,300),"Tops_ABCD"+radi+"_MSD","Ws_ABCD"+radi+"_MSD",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_tau21 + " && " + plotselection_tau32,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(t) VS CSV_v2(b)",60,0,300,20,0,1),"Tops_ABCD"+radi+"_MSD","Bottoms_ABCD"+radi+"_CSV",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_tau32,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_MSD_vs_TprimeM" ,"m_{SD}(t) VS m(T')",60,0,300,50,0,2500),"Tops_ABCD"+radi+"_MSD","Tprimes_ABCD"+radi+"_M",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_tau32,"1 btag"),
    
    
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_MSD_vs_W_tau21" ,"m_{SD}(W) VS tau_{21}(W)",60,0,300,20,0,1),"Ws_ABCD"+radi+"_MSD","Ws_ABCD"+radi+"_t21",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_tau32 + " && " + plotselection_t_MSD,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",60,0,300,20,0,1),"Ws_ABCD"+radi+"_MSD","Bottoms_ABCD"+radi+"_CSV",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_tau32 + " && " + plotselection_W_tau21 + " && " + plotselection_t_MSD,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_MSD_vs_TprimeM" ,"m_{SD}(W) VS m(T')",60,0,300,50,0,2500),"Ws_ABCD"+radi+"_MSD","Tprimes_ABCD"+radi+"_M",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_B_CSV + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_tau32,"1 btag"),
    
    
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_tau21_vs_Bottom_CSV_v2" ,"tau_{21}(W) VS CSV_v2(b)",20,0,1,20,0,1),"Ws_ABCD"+radi+"_t21","Bottoms_ABCD"+radi+"_CSV",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_W_MSD + " && " + plotselection_tau32 + " && " + plotselection_t_MSD,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_tau21_vs_Bottom_CSV_v2_WMSD_anti" ,"tau_{21}(W) VS CSV_v2(b)",20,0,1,20,0,1),"Ws_ABCD"+radi+"_t21","Bottoms_ABCD"+radi+"_CSV",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_W_MSD_anti + " && " + plotselection_tau32 + " && " + plotselection_t_MSD,"1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_tau21_vs_TprimeM" ,"tau_{21}(W) VS m(T')",20,0,1,50,0,2500),"Ws_ABCD"+radi+"_t21","Tprimes_ABCD"+radi+"_M",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_B_CSV + " && " + plotselection_t_MSD + " && " + plotselection_W_MSD + " && " + plotselection_tau32,"1 btag"),

    TwoDimPlot(ROOT.TH2F("ABCD_Bottom_CSV_v2_vs_TprimeM" ,"CSV_v2(b) VS m(T')",20,0,1,50,0,2500),"Bottoms_ABCD"+radi+"_CSV","Tprimes_ABCD"+radi+"_M",plotselection1 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_tau32,"1 btag"),
    

    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Topsubjet_CSV_v2" ,"tau_{32}(t) VS CSV_v2(t-sub)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Tops_ABCD"+radi+"_maxsubjetCSVv2",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_Topsubjet_CSV_v_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_maxsubjetCSVv2","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_maxsubjetCSVv2>0 && Bottoms_ABCD"+radi+"_CSV>0" + " && " + plotselection_TprimeMass,"1 btag"),


    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_ZprimeM" ,"tau_{32}(t) VS m(Z')",20,0,1,50,0,5000),"Tops_ABCD"+radi+"_t32","Zprimes_ABCD"+radi+"_M",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Zprimes_ABCD"+radi+"_M>0" + " && " + plotselection_TprimeMass + " && " +,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_Bottom_CSV_v2_vs_ZprimeM" ,"CSV_v2(b) VS m(Z')",20,0,1,50,0,5000),"Bottoms_ABCD"+radi+"_CSV","Zprimes_ABCD"+radi+"_M",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>0" + " && " + plotselection_TprimeMass + " && " +,"1 btag"),    
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_tau21_vs_ZprimeM" ,"tau_{21}(W) VS m(Z')",20,0,1,50,0,5000),"Ws_ABCD"+radi+"_t21","Zprimes_ABCD"+radi+"_M",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Ws_ABCD"+radi+"_t21>0 && Zprimes_ABCD"+radi+"_M>0" + " && " + plotselection_TprimeMass + " && " +,"1 btag"),
    
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_TprimeM" ,"tau_{32}(t) VS m(Z')",20,0,1,50,0,2500),"Tops_ABCD"+radi+"_t32","Tprimes_ABCD"+radi+"_M",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Zprimes_ABCD"+radi+"_M>0" + " && " +,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_Bottom_CSV_v2_vs_TprimeM" ,"CSV_v2(b) VS m(Z')",20,0,1,50,0,2500),"Bottoms_ABCD"+radi+"_CSV","Tprimes_ABCD"+radi+"_M",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>0" + " && " +,"1 btag"),    
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_tau21_vs_TprimeM" ,"tau_{21}(W) VS m(Z')",20,0,1,50,0,2500),"Ws_ABCD"+radi+"_t21","Tprimes_ABCD"+radi+"_M",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Ws_ABCD"+radi+"_t21>0 && Zprimes_ABCD"+radi+"_M>0" + " && " +,"1 btag"),    
    

    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime01000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>0 && Zprimes_ABCD"+radi+"_M<1000" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime10001250" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>1000 && Zprimes_ABCD"+radi+"_M<1250" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime12501500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>1250 && Zprimes_ABCD"+radi+"_M<1500" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime15001750" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>1500 && Zprimes_ABCD"+radi+"_M<1750" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime17502000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>1750 && Zprimes_ABCD"+radi+"_M<2000" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime20002250" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>2000 && Zprimes_ABCD"+radi+"_M<2250" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime22502500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>2250 && Zprimes_ABCD"+radi+"_M<2500" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime25003000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>2500 && Zprimes_ABCD"+radi+"_M<3000" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime30003500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>3000 && Zprimes_ABCD"+radi+"_M<3500" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime35004000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>3500 && Zprimes_ABCD"+radi+"_M<4000" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime40004500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>4000 && Zprimes_ABCD"+radi+"_M<4500" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime45005000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>4500 && Zprimes_ABCD"+radi+"_M<5000" + " && " + plotselection_TprimeMass,"1 btag"),
    
    #All elements
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_top_MSD" ,"tau_{32}(t) VS m_{SD}(t)",20,0,1,60,0,300),"Tops_ABCD"+radi+"_MSD","Tops_ABCD"+radi+"_t32",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"2 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_W_tau21" ,"tau_{32}(t) VS tau_{21}(W)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Ws_ABCD"+radi+"_t21",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_t_MSD,"2 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_W_MSD" ,"tau_{32}(t) VS m_{SD}(W)",20,0,1,60,0,300),"Tops_ABCD"+radi+"_t32","Ws_ABCD"+radi+"_MSD",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_tau21 + " && " + plotselection_t_MSD,"2 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_t_MSD,"2 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_TprimeM" ,"tau_{32}(t) VS m(T')",20,0,1,50,0,2500),"Tops_ABCD"+radi+"_t32","Tprimes_ABCD"+radi+"_M",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_t_MSD,"2 btag"),
    
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_MSD_vs_W_tau21" ,"m_{SD}(t) VS tau_{21}(W)",60,0,300,20,0,1),"Tops_ABCD"+radi+"_MSD","Ws_ABCD"+radi+"_t21",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_tau32,"2 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_MSD_vs_W_MSD" ,"m_{SD}(t) VS m_{SD}(t)(W)",60,0,300,30,0,300),"Tops_ABCD"+radi+"_MSD","Ws_ABCD"+radi+"_MSD",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_tau21 + " && " + plotselection_tau32,"2 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(t) VS CSV_v2(b)",60,0,300,20,0,1),"Tops_ABCD"+radi+"_MSD","Bottoms_ABCD"+radi+"_CSV",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_tau32,"2 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_MSD_vs_TprimeM" ,"m_{SD}(t) VS m(T')",60,0,300,50,0,2500),"Tops_ABCD"+radi+"_MSD","Tprimes_ABCD"+radi+"_M",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_tau32,"2 btag"),
    
    
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_W_MSD_vs_W_tau21" ,"m_{SD}(W) VS tau_{21}(W)",60,0,300,20,0,1),"Ws_ABCD"+radi+"_MSD","Ws_ABCD"+radi+"_t21",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_tau32 + " && " + plotselection_t_MSD,"2 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_W_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",60,0,300,20,0,1),"Ws_ABCD"+radi+"_MSD","Bottoms_ABCD"+radi+"_CSV",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_tau32 + " && " + plotselection_W_tau21 + " && " + plotselection_t_MSD,"2 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_W_MSD_vs_TprimeM" ,"m_{SD}(W) VS m(T')",60,0,300,50,0,2500),"Ws_ABCD"+radi+"_MSD","Tprimes_ABCD"+radi+"_M",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_B_CSV + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_tau32,"2 btag"),
    
    
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_W_tau21_vs_Bottom_CSV_v2" ,"tau_{21}(W) VS CSV_v2(b)",20,0,1,20,0,1),"Ws_ABCD"+radi+"_t21","Bottoms_ABCD"+radi+"_CSV",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_W_MSD + " && " + plotselection_tau32 + " && " + plotselection_t_MSD,"2 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_W_tau21_vs_Bottom_CSV_v2_anti" ,"tau_{21}(W) VS CSV_v2(b)",20,0,1,20,0,1),"Ws_ABCD"+radi+"_t21","Bottoms_ABCD"+radi+"_CSV",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_W_MSD_anti + " && " + plotselection_tau32 + " && " + plotselection_t_MSD,"2 btag"),
    
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_W_tau21_vs_TprimeM" ,"tau_{21}(W) VS m(Z')",20,0,1,50,0,2500),"Ws_ABCD"+radi+"_t21","Tprimes_ABCD"+radi+"_M",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_B_CSV + " && " + plotselection_t_MSD + " && " + plotselection_W_MSD + " && " + plotselection_tau32,"2 btag"),

    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_Bottom_CSV_v2_vs_TprimeM" ,"CSV_v2(b) VS m(T')",20,0,1,50,0,2500),"Ws_ABCD"+radi+"_MSD","Tprimes_ABCD"+radi+"_M",plotselection1 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_tau32,"2 btag"),
    

    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime01000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>0 && Zprimes_ABCD"+radi+"_M<1000" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime10001250" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>1000 && Zprimes_ABCD"+radi+"_M<1250" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime12501500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>1250 && Zprimes_ABCD"+radi+"_M<1500" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime15001750" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>1500 && Zprimes_ABCD"+radi+"_M<1750" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime17502000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>1750 && Zprimes_ABCD"+radi+"_M<2000" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime20002250" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>2000 && Zprimes_ABCD"+radi+"_M<2250" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime22502500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>2250 && Zprimes_ABCD"+radi+"_M<2500" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime25003000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>2500 && Zprimes_ABCD"+radi+"_M<3000" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime30003500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>3000 && Zprimes_ABCD"+radi+"_M<3500" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime35004000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>3500 && Zprimes_ABCD"+radi+"_M<4000" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime40004500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>4000 && Zprimes_ABCD"+radi+"_M<4500" + " && " + plotselection_TprimeMass,"1 btag"),
    #TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime45005000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD"+radi+"_t32","Bottoms_ABCD"+radi+"_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD"+radi+"_t32>0 && Bottoms_ABCD"+radi+"_CSV>0 && Zprimes_ABCD"+radi+"_M>4500 && Zprimes_ABCD"+radi+"_M<5000" + " && " + plotselection_TprimeMass,"1 btag"),



    ## Plots for ZPrime_M - with right plotselection - All Elements
    ## W_ MSD is used as thrid variable
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD , "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + "&&" +plotselection_sideband ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD + "&&" +plotselection_sideband ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD + "&&" +plotselection_sideband ,"1 btag"),


    #Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti + "&&" +plotselection_sideband ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti + "&&" +plotselection_sideband ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti + "&&" +plotselection_sideband ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti + "&&" +plotselection_sideband ,"1 btag"),




    # Plots for W tau21 as third variable ---- beta



    ## Plots for ZPrime_M - with right plotselection - All Elements
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M_beta" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M_beta" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M_beta" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M_beta" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),


    #Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M_beta" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M_beta" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M_beta" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M_beta" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),



    #Test if one-sided cut on W_MSD changes Normalization

    #Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M_one_sided" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_one_sided, "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M_one_sided" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_one_sided  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M_one_sided" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_one_sided  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M_one_sided" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_one_sided  ,"1 btag"),


    #Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M_one_sided" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_one_sided_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M_one_sided" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_one_sided_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M_one_sided" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_one_sided_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M_one_sided" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_one_sided_anti  ,"1 btag"),




    #doing only first element
    #beta (tau21)
    
##ABCD1 t-tau32 bottomCSV    
    ## no topsubbtag
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatB_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatC_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatD_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatE_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatF_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatG_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatH_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,
    
    ## with topsubbtag
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,
    
    ##inclusive
    #Plot(ROOT.TH1F("ABCD_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatA_withtopbtag) || ABCD_CatID==ABCD_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatB_withtopbtag) || ABCD_CatID==ABCD_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatC_withtopbtag) || ABCD_CatID==ABCD_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatD_withtopbtag) || ABCD_CatID==ABCD_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatE_withtopbtag) || ABCD_CatID==ABCD_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatF_withtopbtag) || ABCD_CatID==ABCD_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatG_withtopbtag) || ABCD_CatID==ABCD_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatH_withtopbtag) || ABCD_CatID==ABCD_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,




##ABCD2 topMSD bottomCSV
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD2_CatID==ABCD2_CatA_withtopbtag) || ABCD2_CatID==ABCD2_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD2_CatID==ABCD2_CatB_withtopbtag) || ABCD2_CatID==ABCD2_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD2_CatID==ABCD2_CatC_withtopbtag) || ABCD2_CatID==ABCD2_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD2_CatID==ABCD2_CatD_withtopbtag) || ABCD2_CatID==ABCD2_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD2_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD2_CatID==ABCD2_CatE_withtopbtag) || ABCD2_CatID==ABCD2_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD2_CatID==ABCD2_CatF_withtopbtag) || ABCD2_CatID==ABCD2_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD2_CatID==ABCD2_CatG_withtopbtag) || ABCD2_CatID==ABCD2_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD2_CatID==ABCD2_CatH_withtopbtag) || ABCD2_CatID==ABCD2_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,


##ABCD3 bottomCSV W_MSD
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD3_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD3_CatID==ABCD3_CatA_withtopbtag) || ABCD3_CatID==ABCD3_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD3_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD3_CatID==ABCD3_CatB_withtopbtag) || ABCD3_CatID==ABCD3_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD3_CatID==ABCD3_CatC_withtopbtag) || ABCD3_CatID==ABCD3_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD3_CatID==ABCD3_CatD_withtopbtag) || ABCD3_CatID==ABCD3_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD3_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD3_CatID==ABCD3_CatE_withtopbtag) || ABCD3_CatID==ABCD3_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD3_CatID==ABCD3_CatF_withtopbtag) || ABCD3_CatID==ABCD3_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD3_CatID==ABCD3_CatG_withtopbtag) || ABCD3_CatID==ABCD3_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD3_CatID==ABCD3_CatH_withtopbtag) || ABCD3_CatID==ABCD3_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,


##ABCD4 TprimeMass bottomCSV
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD4_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD4_CatID==ABCD4_CatA_withtopbtag) || ABCD4_CatID==ABCD4_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD4_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD4_CatID==ABCD4_CatB_withtopbtag) || ABCD4_CatID==ABCD4_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD4_CatID==ABCD4_CatC_withtopbtag) || ABCD4_CatID==ABCD4_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD4_CatID==ABCD4_CatD_withtopbtag) || ABCD4_CatID==ABCD4_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD4_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD4_CatID==ABCD4_CatE_withtopbtag) || ABCD4_CatID==ABCD4_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD4_CatID==ABCD4_CatF_withtopbtag) || ABCD4_CatID==ABCD4_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD4_CatID==ABCD4_CatG_withtopbtag) || ABCD4_CatID==ABCD4_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_TprimeMass  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD4_CatID==ABCD4_CatH_withtopbtag) || ABCD4_CatID==ABCD4_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,


#ABCD5 W tau21 bottomCSV
    #no topbtag
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD5_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD5_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD5_CatID==ABCD5_CatA_withtopbtag) || ABCD5_CatID==ABCD5_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD5_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD5_CatID==ABCD5_CatB_withtopbtag) || ABCD5_CatID==ABCD5_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD5_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD5_CatID==ABCD5_CatC_withtopbtag) || ABCD5_CatID==ABCD5_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD5_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD5_CatID==ABCD5_CatD_withtopbtag) || ABCD5_CatID==ABCD5_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD5_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD5_CatID==ABCD5_CatE_withtopbtag) || ABCD5_CatID==ABCD5_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD5_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD5_CatID==ABCD5_CatF_withtopbtag) || ABCD5_CatID==ABCD5_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD5_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD5_CatID==ABCD5_CatG_withtopbtag) || ABCD5_CatID==ABCD5_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD5_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD5_CatID==ABCD5_CatH_withtopbtag) || ABCD5_CatID==ABCD5_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,


##ABCD6 W tau21 topMSD
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD6_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD6_CatID==ABCD6_CatA_withtopbtag) || ABCD6_CatID==ABCD6_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD6_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD6_CatID==ABCD6_CatB_withtopbtag) || ABCD6_CatID==ABCD6_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD6_CatID==ABCD6_CatC_withtopbtag) || ABCD6_CatID==ABCD6_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD6_CatID==ABCD6_CatD_withtopbtag) || ABCD6_CatID==ABCD6_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD6_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD6_CatID==ABCD6_CatE_withtopbtag) || ABCD6_CatID==ABCD6_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD6_CatID==ABCD6_CatF_withtopbtag) || ABCD6_CatID==ABCD6_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD6_CatID==ABCD6_CatG_withtopbtag) || ABCD6_CatID==ABCD6_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD6_CatID==ABCD6_CatH_withtopbtag) || ABCD6_CatID==ABCD6_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,


##ABCD7 WMSD topMSD
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD, "1 btag"),
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD, "2 btag"),
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD7_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD7_CatID==ABCD7_CatA_withtopbtag) || ABCD7_CatID==ABCD7_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD, "1 btag"),
    #Plot(ROOT.TH1F("ABCD7_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD7_CatID==ABCD7_CatB_withtopbtag) || ABCD7_CatID==ABCD7_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD7_CatID==ABCD7_CatC_withtopbtag) || ABCD7_CatID==ABCD7_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD7_CatID==ABCD7_CatD_withtopbtag) || ABCD7_CatID==ABCD7_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD7_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD7_CatID==ABCD7_CatE_withtopbtag) || ABCD7_CatID==ABCD7_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD7_CatID==ABCD7_CatF_withtopbtag) || ABCD7_CatID==ABCD7_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD7_CatID==ABCD7_CatG_withtopbtag) || ABCD7_CatID==ABCD7_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD7_CatID==ABCD7_CatH_withtopbtag) || ABCD7_CatID==ABCD7_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"1 btag") ,




##ABCD8 W tau21 bottomCSV  tmsd as third
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD8_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD8_CatID==ABCD8_CatA_withtopbtag) || ABCD8_CatID==ABCD8_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD8_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD8_CatID==ABCD8_CatB_withtopbtag) || ABCD8_CatID==ABCD8_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD8_CatID==ABCD8_CatC_withtopbtag) || ABCD8_CatID==ABCD8_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD8_CatID==ABCD8_CatD_withtopbtag) || ABCD8_CatID==ABCD8_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD8_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD8_CatID==ABCD8_CatE_withtopbtag) || ABCD8_CatID==ABCD8_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD8_CatID==ABCD8_CatF_withtopbtag) || ABCD8_CatID==ABCD8_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD8_CatID==ABCD8_CatG_withtopbtag) || ABCD8_CatID==ABCD8_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD8_CatID==ABCD8_CatH_withtopbtag) || ABCD8_CatID==ABCD8_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,



##ABCD9 W tau21 bottomCSV  tau32 as third
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD9_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD9_CatID==ABCD9_CatA_withtopbtag) || ABCD9_CatID==ABCD9_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD9_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD9_CatID==ABCD9_CatB_withtopbtag) || ABCD9_CatID==ABCD9_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD9_CatID==ABCD9_CatC_withtopbtag) || ABCD9_CatID==ABCD9_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD9_CatID==ABCD9_CatD_withtopbtag) || ABCD9_CatID==ABCD9_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD9_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD9_CatID==ABCD9_CatE_withtopbtag) || ABCD9_CatID==ABCD9_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD9_CatID==ABCD9_CatF_withtopbtag) || ABCD9_CatID==ABCD9_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD9_CatID==ABCD9_CatG_withtopbtag) || ABCD9_CatID==ABCD9_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_tau32_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD9_CatID==ABCD9_CatH_withtopbtag) || ABCD9_CatID==ABCD9_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,



##ABCD10 W tau21 bottomCSV  TprimeM as third
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD10_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD10_CatID==ABCD10_CatA_withtopbtag) || ABCD10_CatID==ABCD10_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD10_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD10_CatID==ABCD10_CatB_withtopbtag) || ABCD10_CatID==ABCD10_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD10_CatID==ABCD10_CatC_withtopbtag) || ABCD10_CatID==ABCD10_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD10_CatID==ABCD10_CatD_withtopbtag) || ABCD10_CatID==ABCD10_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD10_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD10_CatID==ABCD10_CatE_withtopbtag) || ABCD10_CatID==ABCD10_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD10_CatID==ABCD10_CatF_withtopbtag) || ABCD10_CatID==ABCD10_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD10_CatID==ABCD10_CatG_withtopbtag) || ABCD10_CatID==ABCD10_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_TprimeMass_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD10_CatID==ABCD10_CatH_withtopbtag) || ABCD10_CatID==ABCD10_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,










    Plot(ROOT.TH1F("Notopbtag_Tprime_M" ,"m_{SD}(t-notoptag) in GeV" ,60,0,300),"Tprimes_ABCD"+radi+"_M",    plotselection2 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_t_MSD, "1 btag"),
    Plot(ROOT.TH1F("Withtopbtag_Tprime_M" ,"m_{SD}(t-notoptag) in GeV" ,60,0,300),"Tprimes_ABCD"+radi+"_M",    plotselection2 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_t_MSD, "1 btag"),





#MSD manual sepaTest


    Plot(ROOT.TH1F("Notopbtag_Top_MSD" ,"m_{SD}(t-jet) in GeV, 1 b-tag" ,60,0,300),"Tops_ABCD"+radi+"_MSD",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    Plot(ROOT.TH1F("Withtopbtag_Top_MSD" ,"m_{SD}(t-jet) in GeV, 2 b-tag",60,0,300),"Tops_ABCD"+radi+"_MSD",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    Plot(ROOT.TH1F("Notopbtag_W_MSD" ,"m_{SD}(W-jet) in GeV, 1 b-tag" ,60,0,300),"Ws_ABCD"+radi+"_MSD",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    Plot(ROOT.TH1F("Withtopbtag_W_MSD" ,"m_{SD}(W-jet) in GeV, 2 b-tag" ,60,0,300),"Ws_ABCD"+radi+"_MSD",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
 
    Plot(ROOT.TH1F("Notopbtag_Bottom_CSV" ,"CSV_v2(b-jet), 1 b-tag" ,50,0,1),"Bottoms_ABCD"+radi+"_CSV",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_t_MSD + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    Plot(ROOT.TH1F("Withtopbtag_Bottom_CSV" ,"CSV_v2(b-jet), 2 b-tag",50,0,1),"Bottoms_ABCD"+radi+"_CSV",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_t_MSD + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"), 
 
    Plot(ROOT.TH1F("Notopbtag_Top_t32" ,"#tau_{32}(t-jet), 1 b-tag" ,20,0,1),"Tops_ABCD"+radi+"_t32",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    Plot(ROOT.TH1F("Withtopbtag_Top_t32" ,"#tau_{32}(t-jet), 2 b-tag",20,0,1),"Tops_ABCD"+radi+"_t32",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    Plot(ROOT.TH1F("Notopbtag_W_t21" ,"#tau_{21}(W-jet), 1 b-tag" ,20,0,1),"Ws_ABCD"+radi+"_t21",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_tau32 + " && " + plotselection_TprimeMass, "1 btag"),
    Plot(ROOT.TH1F("Withtopbtag_W_t21" ,"#tau_{21}(W-jet), 2 b-tag" ,20,0,1),"Ws_ABCD"+radi+"_t21",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_tau32 + " && " + plotselection_TprimeMass, "1 btag"),


    Plot(ROOT.TH1F("Notopbtag_EvtHT" ,"Evt_HT_Jets, 1 b-tag" ,80,1000,5000),"Evt_HT_Jets",  plotselection2 + " && " + plotselection1+ " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),
    Plot(ROOT.TH1F("Notopbtag_N_JetsAK8" ,"N_JetsAK8, 1 b-tag" ,10,0,10),"N_packedPatJetsAK8PFCHSSoftDrop",  plotselection2 + " && " + plotselection1+ " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),
    Plot(ROOT.TH1F("Notopbtag_N_JetsAK4" ,"N_JetsAK4, 1 b-tag" ,10,0,10),"N_Jets",  plotselection2 + " && " + plotselection1+ " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),
    
    Plot(ROOT.TH1F("Withtopbtag_EvtHT" ,"Evt_HT_Jets, 2 b-tag" ,80,1000,5000),"Evt_HT_Jets",  plotselection2 + " && " + plotselection1+ " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"2 btag"),
    Plot(ROOT.TH1F("Withtopbtag_N_JetsAK8" ,"N_JetsAK8, 2 b-tag" ,10,0,10),"N_packedPatJetsAK8PFCHSSoftDrop",  plotselection2 + " && " + plotselection1+ " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"2 btag"),
    Plot(ROOT.TH1F("Withtopbtag_N_JetsAK4" ,"N_JetsAK4, 2 b-tag" ,10,0,10),"N_Jets",  plotselection2 + " && " + plotselection1+ " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"2 btag"),

    TwoDimPlot(ROOT.TH2F("Notopbtag_Zprime_M_vs_EvtHT" ,"m(Z') VS Evt_HT_Jets",80,1000,5000,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "Evt_HT_Jets", " (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300)" + " && " + "Evt_HT_Jets>1000  && N_Jets<9 && N_packedPatJetsAK8PFCHSSoftDrop<9 && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400"+ " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),
    TwoDimPlot(ROOT.TH2F("Withtopbtag_Zprime_M_vs_EvtHT" ,"m(Z') VS Evt_HT_Jets",80,1000,5000,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "Evt_HT_Jets", " (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300)" + " && " + "Evt_HT_Jets>1000  && N_Jets<9 && N_packedPatJetsAK8PFCHSSoftDrop<9 && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400"+ " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),
    TwoDimPlot(ROOT.TH2F("Notopbtag_Zprime_M_vs_N_JetsAK8" ,"m(Z') VS N_JetsAK8",80,1000,5000,10,0,10),"Zprimes_ABCD"+radi+"_M", "N_packedPatJetsAK8PFCHSSoftDrop", " (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300)" + " && " + "Evt_HT_Jets>1000  && N_Jets<9 && N_packedPatJetsAK8PFCHSSoftDrop<9 && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400"+ " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),
    TwoDimPlot(ROOT.TH2F("Withtopbtag_Zprime_M_vs_N_JetsAK8" ,"m(Z') VS N_JetsAK8",80,1000,5000,10,0,10),"Zprimes_ABCD"+radi+"_M", "N_packedPatJetsAK8PFCHSSoftDrop", " (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300)" + " && " + "Evt_HT_Jets>1000  && N_Jets<9 && N_packedPatJetsAK8PFCHSSoftDrop<9 && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400"+ " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),
    TwoDimPlot(ROOT.TH2F("Notopbtag_Zprime_M_vs_N_JetsAK4" ,"m(Z') VS N_JetsAK4",80,1000,5000,10,0,10),"Zprimes_ABCD"+radi+"_M", "N_Jets", " (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300)" + " && " + "Evt_HT_Jets>1000  && N_Jets<9 && N_packedPatJetsAK8PFCHSSoftDrop<9 && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400"+ " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),
    TwoDimPlot(ROOT.TH2F("Withtopbtag_Zprime_M_vs_N_JetsAK4" ,"m(Z') VS N_JetsAK4",80,1000,5000,10,0,10),"Zprimes_ABCD"+radi+"_M", "N_Jets", " (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300)" + " && " + "Evt_HT_Jets>1000  && N_Jets<9 && N_packedPatJetsAK8PFCHSSoftDrop<9 && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400"+ " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),

    TwoDimPlot(ROOT.TH2F("Notopbtag_Zprime_M_vs_sqrts" ,"m(Z') VS Evt_HT_Jets",80,1000,5000,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "Evt_sqrts", " (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300)" + " && " + "Evt_HT_Jets>1000 && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400"+ " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),
    TwoDimPlot(ROOT.TH2F("Withtopbtag_Zprime_M_vs_sqrts" ,"m(Z') VS Evt_HT_Jets",80,1000,5000,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "Evt_sqrts", " (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300)" + " && " + "Evt_HT_Jets>1000 && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400"+ " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + plotselection_B_CSV + " && " + plotselection_W_MSD + " && " + plotselection_W_tau21,"1 btag"),

    Plot(ROOT.TH1F("nth_bjet_firsttagged_wtb" ,"p_{T} order of first b-tagged jet" ,11,-0.5,10.5),"first_tagged_bottom_jets",   "first_tagged_bottom_jets>0 && (ABCD5_CatID==ABCD5_CatA_withtopbtag || ABCD5_CatID==ABCD5_CatB_withtopbtag || ABCD5_CatID==ABCD5_CatC_withtopbtag || ABCD5_CatID==ABCD5_CatD_withtopbtag)", "2 btag"),
    Plot(ROOT.TH1F("nth_bjet_firsttagged_ntb" ,"p_{T} order of first b-tagged jet" ,11,-0.5,10.5),"first_tagged_bottom_jets",   "first_tagged_bottom_jets>0 && (ABCD5_CatID==ABCD5_CatA_notopbtag || ABCD5_CatID==ABCD5_CatB_notopbtag || ABCD5_CatID==ABCD5_CatC_notopbtag || ABCD5_CatID==ABCD5_CatD_notopbtag)", "1 btag"),

    Plot(ROOT.TH1F("nth_Wjet_firsttagged_wtb" ,"p_{T} order of first W-tagged jet" ,11,-0.5,10.5),"first_tagged_W_jets",   "first_tagged_W_jets>0 && (ABCD5_CatID==ABCD5_CatA_withtopbtag || ABCD5_CatID==ABCD5_CatB_withtopbtag || ABCD5_CatID==ABCD5_CatC_withtopbtag || ABCD5_CatID==ABCD5_CatD_withtopbtag)", "2 btag"),
    Plot(ROOT.TH1F("nth_Wjet_firsttagged_ntb" ,"p_{T} order of first W-tagged jet" ,11,-0.5,10.5),"first_tagged_W_jets",   "first_tagged_W_jets>0 && (ABCD5_CatID==ABCD5_CatA_notopbtag || ABCD5_CatID==ABCD5_CatB_notopbtag || ABCD5_CatID==ABCD5_CatC_notopbtag || ABCD5_CatID==ABCD5_CatD_notopbtag)", "1 btag"),

    Plot(ROOT.TH1F("ZprimeminusEvtHT_wtb" ,"(m(Z')-H_{T})/m(Z')" ,26,-0.3,1),"ZprimeminusEvtHT_wtb",   "ZprimeminusEvtHT_wtb>(-20000.0)", "2 btag"),
    Plot(ROOT.TH1F("ZprimeminusEvtHT_ntb" ,"(m(Z')-H_{T})/m(Z')" ,26,-0.3,1),"ZprimeminusEvtHT_ntb",   "ZprimeminusEvtHT_ntb>(-20000.0)", "1 btag"),

    Plot(ROOT.TH1F("mTquark" ,"m(T) in GeV" ,40,0,2000),"Tprimes_ABCD"+radi+"_M",   plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>1000 " + "  &&  " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, ""),

    #Plot(ROOT.TH1F("ZprimeminusSqrtS_wtb" ,"(m(Z')-#sqrt{AK4-jets})/m(Z'), CatA" ,40,-1,1),"ZprimeminusSqrtS_wtb",   "ZprimeminusSqrtS_wtb>(-20000.0)", "2 btag"),
    #Plot(ROOT.TH1F("ZprimeminusSqrtS_ntb" ,"(m(Z')-#sqrt{AK4-jets})/m(Z'), CatA" ,40,-1,1),"ZprimeminusSqrtS_ntb",   "ZprimeminusSqrtS_ntb>(-20000.0)", "1 btag"),



#Correlation of Variables to Mass of Z_Prime
TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_Zprime_M" ,"#tau_{32}(t) VS m(Z')",20,0,1,30,0,300),"Tops_ABCD"+radi+"_t32", "Zprimes_ABCD"+radi+"_M",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Zprimes_ABCD"+radi+"_M>0 && Tops_ABCD"+radi+"_t32>0","1 btag"),
TwoDimPlot(ROOT.TH2F("ABCD_W_tau21_vs_Zprime_M" ,"#tau_{21}(W) VS m(Z')",20,0,1,30,0,300),"Ws_ABCD"+radi+"_t21", "Zprimes_ABCD"+radi+"_M",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Zprimes_ABCD"+radi+"_M>0 && Ws_ABCD"+radi+"_t21>0","1 btag"),
TwoDimPlot(ROOT.TH2F("ABCD_bottom_csv_v2_vs_Zprime_M" ,"CSV_v2(b) VS m(Z')",20,0,1,30,0,300),"Bottoms_ABCD"+radi+"_CSV", "Zprimes_ABCD"+radi+"_M",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Zprimes_ABCD"+radi+"_M>0 && Tops_ABCD"+radi+"_t32>0","1 btag"),




]
for l in range(1,11):
    haeeee=str(l)
    plots=plots+[
        Plot(ROOT.TH1F("bottom_jet_tagged_numbers_wtb_" +haeeee ,"# of b-tags for jet i, 2 b-tag" ,11,0,11),"bottom_jet_tagged_numbers" + haeeee,   "bottom_jet_tagged_numbers" + haeeee+">0 && (ABCD5_CatID==ABCD5_CatA_withtopbtag || ABCD5_CatID==ABCD5_CatB_withtopbtag || ABCD5_CatID==ABCD5_CatC_withtopbtag || ABCD5_CatID==ABCD5_CatD_withtopbtag)", "2 btag"),
        Plot(ROOT.TH1F("bottom_jet_cand_numbers_wtb_"+haeeee ,"# of b-jet candidates, 2 b-tag" ,11,0,11),"bottom_jet_cand_numbers"+haeeee,   "bottom_jet_cand_numbers"+haeeee+">0 && (ABCD5_CatID==ABCD5_CatA_withtopbtag || ABCD5_CatID==ABCD5_CatB_withtopbtag || ABCD5_CatID==ABCD5_CatC_withtopbtag ||     ABCD5_CatID==ABCD5_CatD_withtopbtag)", "2 btag"),
        Plot(ROOT.TH1F("bottom_jet_tagged_numbers_ntb_"+haeeee ,"# of b-tags for jet i, 1 b-tag" ,11,0,11),"bottom_jet_tagged_numbers"+haeeee,   "bottom_jet_tagged_numbers"+haeeee+">0 && (ABCD5_CatID==ABCD5_CatA_notopbtag || ABCD5_CatID==ABCD5_CatB_notopbtag || ABCD5_CatID==ABCD5_CatC_notopbtag || ABCD5_CatID==ABCD5_CatD_notopbtag)", "1 btag"),
        Plot(ROOT.TH1F("bottom_jet_cand_numbers_ntb_"+haeeee ,"# of b-jet candidates, 1 b-tagi" ,11,0,11),"bottom_jet_cand_numbers"+haeeee,   "bottom_jet_cand_numbers"+haeeee+">0 && (ABCD5_CatID==ABCD5_CatA_notopbtag || ABCD5_CatID==ABCD5_CatB_notopbtag || ABCD5_CatID==ABCD5_CatC_notopbtag || ABCD5_CatID==ABCD5_CatD_notopbtag)", "1 btag"),
        
        Plot(ROOT.TH1F("W_jet_tagged_numbers_wtb_" +haeeee ,"# of W-tags for jet i, 2 b-tag" ,11,0,11),"W_jet_tagged_numbers" + haeeee,   "W_jet_tagged_numbers" + haeeee+">0 && (ABCD5_CatID==ABCD5_CatA_withtopbtag || ABCD5_CatID==ABCD5_CatB_withtopbtag || ABCD5_CatID==ABCD5_CatC_withtopbtag || ABCD5_CatID==ABCD5_CatD_withtopbtag)", "2 btag"),
        Plot(ROOT.TH1F("W_jet_cand_numbers_wtb_"+haeeee ,"# of W-jet candidates, 2 b-tag" ,11,0,11),"W_jet_cand_numbers"+haeeee,   "W_jet_cand_numbers"+haeeee+">0 && (ABCD5_CatID==ABCD5_CatA_withtopbtag || ABCD5_CatID==ABCD5_CatB_withtopbtag || ABCD5_CatID==ABCD5_CatC_withtopbtag ||     ABCD5_CatID==ABCD5_CatD_withtopbtag)", "2 btag"),
        Plot(ROOT.TH1F("W_jet_tagged_numbers_ntb_"+haeeee ,"# of W-tags for jet i, 2 b-tag" ,11,0,11),"W_jet_tagged_numbers"+haeeee,   "W_jet_tagged_numbers"+haeeee+">0 && (ABCD5_CatID==ABCD5_CatA_notopbtag || ABCD5_CatID==ABCD5_CatB_notopbtag || ABCD5_CatID==ABCD5_CatC_notopbtag || ABCD5_CatID==ABCD5_CatD_notopbtag)", "1 btag"),
        Plot(ROOT.TH1F("W_jet_cand_numbers_ntb_"+haeeee ,"# of W-jet candidates, 1 b-tag" ,11,0,11),"W_jet_cand_numbers"+haeeee,   "W_jet_cand_numbers"+haeeee+">0 && (ABCD5_CatID==ABCD5_CatA_notopbtag || ABCD5_CatID==ABCD5_CatB_notopbtag || ABCD5_CatID==ABCD5_CatC_notopbtag || ABCD5_CatID==ABCD5_CatD_notopbtag)", "1 btag"),
    ]




CatAList=["ABCD_notopbtag_CatA_Zprime_M" , "ABCD_notopbtag_CatA_Zprime_M_beta", "ABCD_notopbtag_CatA_Zprime_M_beta_first", "ABCD_notopbtag_CatA_Zprime_M_first"]

plotnames=[]
for i in plots:
    plotnames.append(i.name)


OnlyFirstList=len(plots)*[False]
#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
OnlyFirstList[plotnames.index("ABCD5_notopbtag_CatA_Zprime_M_beta_first"):plotnames.index('Withtopbtag_Zprime_M_vs_sqrts') +1 ] = len(OnlyFirstList[plotnames.index("ABCD5_notopbtag_CatA_Zprime_M_beta_first"):plotnames.index('Withtopbtag_Zprime_M_vs_sqrts') + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'

#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
assert len(OnlyFirstList)==len(plots)
#raw_input()




print name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,4000000,plots,samples)
outputpath=plotParallel(name,1500000,plots,SignalSamples+BackgroundSamples, [''], ['1'] , [''], ['1'],additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)
#outputpath=plotParallel(name,2000000,plots,SignalSamples, [''], ['1'] , [''], ['1'],additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+CombinedSamples, [''], ['1'] , [''], ['1'], [],  OnlyFirstList)
#outputpathBackground=plotParallel(name,4000000,plots,BackgroundSamples)
#outputpathData=plotParallel(name,4000000,plots,DataSamples)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#print outputpath, SignalSamples, plots
listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples ,plots,1, [""], True )
#print "hell yeah", listOfHistoListsSignal

#listOfHistoListsBackground=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples,plots,1) #needed? Same as  ABCD?
listOfHistoListsABCD=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples ,plots,1,[""], True )

print listOfHistoListsABCD
#raw_input()
addLOLTtoLOLT([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]],[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ST_tW')]])
addLOLTtoLOLT([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]],[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ST_t')]])
addLOLTtoLOLT([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]],[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ST_s')]])

print listOfHistoListsABCD

#raw_input()
listOfHistoListsABCDnew=transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])
listOfHistoListsABCD=listOfHistoListsABCDnew
BackgroundSamples=[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]
BackgroundSampleNames=[BackgroundSampleNames[BackgroundSampleNames.index('ttbar')]]+[BackgroundSampleNames[BackgroundSampleNames.index('QCD_HT')]]
                                                                                    
print listOfHistoListsABCD
#raw_input()



#print "hell yeah 1312", listOfHistoListsABCD

# listOfHistoListsSignalAndBackground=createHistoLists_fromSuperHistoFile(outputpath,CombinedSamples,plots,1, [""], True )

#listOfHistoListsSignalAndBackground1500900=CloneListOfHistoLists(listOfHistoListsABCD+listOfHistoListsSignal)
#listOfHistoListsSignalAndBackground20001200=CloneListOfHistoLists(listOfHistoListsABCD+listOfHistoListsSignal)
#listOfHistoListsSignalAndBackground25001200=CloneListOfHistoLists(listOfHistoListsABCD+listOfHistoListsSignal)


#listOfHistoListsSignalAndBackground=[listOfHistoListsSignalAndBackground1500900, listOfHistoListsSignalAndBackground20001200, listOfHistoListsSignalAndBackground25001200]


#for lol in listOfHistoListsSignalAndBackground:
    #print lol[0][0], "Sind die pointer anders fuer die verschiedenen listOfHistoLists?"

labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)



#print [transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]
#print listOfHistoListsSignal
print SignalSampleNames

#writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime15001200')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001200')]])[plotnames.index('Notopbtag_Tprime_M'):plotnames.index('Withtopbtag_W_t21')+1],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[SignalSamples[SignalSampleNames.index('Zprime15001200')]]+[SignalSamples[SignalSampleNames.index('Zprime20001200')]]+[SignalSamples[SignalSampleNames.index('Zprime25001200')]], '','MSDs'+radi,True)

#writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first'):plotnames.index('ABCD7_inclusive_CatH_Zprime_M_beta_first')+1],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]], '','single_regions_QCD'+radi,True)


#writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001200')]])[plotnames.index('Notopbtag_Tprime_M'):plotnames.index('Withtopbtag_W_t21')+1],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[SignalSamples[SignalSampleNames.index('Zprime25001200')]], '','MSDs'+radi,False)

print BackgroundSampleNames
print listOfHistoListsSignal
#print transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime15001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime15001200_ttH')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001200_ttH')]])[plotnames.index('Notopbtag_EvtHT'):plotnames.index('ZprimeminusEvtHT_ntb')+1]

#writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime15001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime15001200_ttH')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001200_ttH')]])[plotnames.index('Notopbtag_EvtHT'):plotnames.index('ZprimeminusEvtHT_ntb')+1],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[SignalSamples[SignalSampleNames.index('Zprime15001200_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime20001200_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime25001200_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime15001200_ttH')]]+[SignalSamples[SignalSampleNames.index('Zprime25001200_ttH')]], '','additionalcuts'+name,True,False,False,"")
print transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('Notopbtag_EvtHT'):plotnames.index('mTquark')+1]
print [BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[SignalSamples[SignalSampleNames.index('ZprimeAll')]]


writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001500_tWb')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]])[plotnames.index('Notopbtag_Top_MSD'):plotnames.index('Withtopbtag_N_JetsAK4')+1],[SignalSamples[SignalSampleNames.index('Zprime1500700_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime20001200_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime25001500_tWb')]]+[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]],"","distros",True,False,False,"",False,False,False)

writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime15001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001500_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001500_tWb')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]])[plotnames.index('Notopbtag_Top_MSD'):plotnames.index('Withtopbtag_N_JetsAK4')+1],[SignalSamples[SignalSampleNames.index('Zprime15001200_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime20001500_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime25001500_tWb')]]+[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]],"","distros",True,False,False,"",False,False,False)



writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001500_tWb')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]])[plotnames.index('Notopbtag_EvtHT'):plotnames.index('ZprimeminusEvtHT_ntb')+1],[SignalSamples[SignalSampleNames.index('Zprime1500700_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime20001200_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime25001500_tWb')]]+[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]],"","additionalcuts_final",True,False,False,"",False,False,False)

writeListOfHistoLists([transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001500_tWb')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]])[plotnames.index('mTquark')]],[SignalSamples[SignalSampleNames.index('Zprime1500700_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime20001200_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime25001500_tWb')]]+[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]],"","additionalcuts_final",True,False,False,"",False,False,False)


#writeListOfHistoLists( transposeLOL([lolABCDT[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('ABCD_notopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_Bottom_CSV_v2_vs_TprimeM")+1], [BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]] , plotnames[plotnames.index('ABCD_notopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_Bottom_CSV_v2_vs_TprimeM")+1], 'ABCD_2D'+name , True, False, False, "colz", False, False, False, True)


#writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('Notopbtag_Tprime_M'):plotnames.index('Withtopbtag_W_t21')+1],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]], 'label','MSDs'+radi,True)
#print SignalSampleNames
#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500900'):SignalSampleNames.index('Zprime25001200')+1])[plotnames.index('Notopbtag_Tprime_M'):plotnames.index('Withtopbtag_W_t21')+1],SignalSamples[SignalSampleNames.index('Zprime1500900'):SignalSampleNames.index('Zprime25001200')+1], 'label','MSDs'+radi,True)
#writeListOfHistoLists([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first')]],BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], 'label','MSDs_QCD ')
#print listOfHistoListsABCD
print plotnames
#raw_input()

                   
                   

for l in range(2,11):
  for histo,histo1 in zip(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("bottom_jet_tagged_numbers_wtb_" +str(l) )],transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("bottom_jet_tagged_numbers_wtb_1")]):
       print "added ", histo, " to ", histo1, " with ",histo.Integral(), " to ", histo1.Integral()
       
       histo1.Add(histo,1.0)
  for histo,histo1 in zip(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("bottom_jet_cand_numbers_wtb_" +str(l))],transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("bottom_jet_cand_numbers_wtb_1")]):
       print "added ", histo, " to ", histo1, " with ",histo.Integral(), " to ", histo1.Integral()
       
       histo1.Add(histo,1.0)
       #print "added ", histo, " to ", histo1
  for histo,histo1 in zip(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("bottom_jet_tagged_numbers_ntb_" +str(l))],transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("bottom_jet_tagged_numbers_ntb_1")]):
       print "added ", histo, " to ", histo1, " with ",histo.Integral(), " to ", histo1.Integral()
       histo1.Add(histo,1.0)
       #print "added ", histo, " to ", histo1
  for histo,histo1 in zip(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("bottom_jet_cand_numbers_ntb_" +str(l))],transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("bottom_jet_cand_numbers_ntb_1")]):
       print "added ", histo, " to ", histo1, " with ",histo.Integral(), " to ", histo1.Integral()
       histo1.Add(histo,1.0)  
       #print "added ", histo, " to ", histo1

  for histo,histo1 in zip(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("W_jet_tagged_numbers_wtb_" +str(l) )],transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("W_jet_tagged_numbers_wtb_1")]):
       print "added ", histo, " to ", histo1, " with ",histo.Integral(), " to ", histo1.Integral()
       
       histo1.Add(histo,1.0)
  for histo,histo1 in zip(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("W_jet_cand_numbers_wtb_" +str(l))],transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("W_jet_cand_numbers_wtb_1")]):
       print "added ", histo, " to ", histo1, " with ",histo.Integral(), " to ", histo1.Integral()
       
       histo1.Add(histo,1.0)
       #print "added ", histo, " to ", histo1
  for histo,histo1 in zip(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("W_jet_tagged_numbers_ntb_" +str(l))],transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("W_jet_tagged_numbers_ntb_1")]):
       print "added ", histo, " to ", histo1, " with ",histo.Integral(), " to ", histo1.Integral()
       histo1.Add(histo,1.0)
       #print "added ", histo, " to ", histo1
  for histo,histo1 in zip(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("W_jet_cand_numbers_ntb_" +str(l))],transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index("W_jet_cand_numbers_ntb_1")]):
       print "added ", histo, " to ", histo1, " with ",histo.Integral(), " to ", histo1.Integral()
       histo1.Add(histo,1.0)  

writeListOfHistoLists([transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('bottom_jet_tagged_numbers_wtb_1')]]+[transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('bottom_jet_tagged_numbers_ntb_1')]],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[SignalSamples[SignalSampleNames.index('ZprimeAll')]] ,"","tags_"+name,True,False,False,'histoE')
writeListOfHistoLists([transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('W_jet_tagged_numbers_wtb_1')]]+[transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('W_jet_tagged_numbers_ntb_1')]],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[SignalSamples[SignalSampleNames.index('ZprimeAll')]] ,"","tags_"+name,True,False,False,'histoE')

writeListOfHistoLists([transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('bottom_jet_cand_numbers_wtb_1')]]+[transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('bottom_jet_cand_numbers_ntb_1')]],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[SignalSamples[SignalSampleNames.index('ZprimeAll')]] ,"","tags_"+name,True,False,False,'histoE')
writeListOfHistoLists([transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('W_jet_cand_numbers_wtb_1')]]+[transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('W_jet_cand_numbers_ntb_1')]],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[SignalSamples[SignalSampleNames.index('ZprimeAll')]] ,"","tags_"+name,True,False,False,'histoE')


writeListOfHistoLists([transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001500_tWb')]])[plotnames.index('nth_bjet_firsttagged_wtb')]]+[transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001500_tWb')]])[plotnames.index('nth_bjet_firsttagged_ntb')]],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[SignalSamples[SignalSampleNames.index('Zprime1500700_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime20001200_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime25001500_tWb')]] ,"","tags_"+name,True,False,True,'histoE')

writeListOfHistoLists([transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001500_tWb')]])[plotnames.index('nth_Wjet_firsttagged_wtb')]]+[transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200_tWb')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001500_tWb')]])[plotnames.index('nth_Wjet_firsttagged_ntb')]],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[SignalSamples[SignalSampleNames.index('Zprime1500700_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime20001200_tWb')]]+[SignalSamples[SignalSampleNames.index('Zprime25001500_tWb')]] ,"","tags_"+name,True,False,True,'histoE')


#writeListOfHistoLists([transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb'):SignalSampleNames.index('Zprime25001500_tWb')])[plotnames.index('nth_Wjet_firsttagged_wtb')]]+[transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700_tWb'):SignalSampleNames.index('Zprime25001500_tWb')])[plotnames.index('nth_Wjet_firsttagged_ntb')]],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+SignalSamples[SignalSampleNames.index('Zprime1500700_tWb'):SignalSampleNames.index('Zprime25001500_tWb')] ,"","tags_"+name,True,False,True,'histoE')

#print "btag"

#print transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('bottom_jet_tagged_numbers_ntb_1')][0][2]
#print transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('bottom_jet_cand_numbers_ntb_1')][0][2]
#print "--------------"
#print transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('bottom_jet_tagged_numbers_ntb_1')][0][2]/transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('bottom_jet_cand_numbers_ntb_1')][0][2]
#print transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('bottom_jet_tagged_numbers_ntb_1')][0][2]
#print transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('bottom_jet_cand_numbers_ntb_1')][0][2]
#print "-----------------------"
#print transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('bottom_jet_tagged_numbers_ntb_1')][0][2]/transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('bottom_jet_cand_numbers_ntb_1')][0][2]
#print "Wtag"
#print transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('W_jet_tagged_numbers_ntb_1')][0][2]
#print transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('W_jet_cand_numbers_ntb_1')][0][2]
#print "--------------"
#print transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('W_jet_tagged_numbers_ntb_1')][0][2]/transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('W_jet_cand_numbers_ntb_1')][0][2]
#print transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('W_jet_tagged_numbers_ntb_1')][0][2]
#print transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('W_jet_cand_numbers_ntb_1')][0][2]
#print "-----------------------"
#print transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('W_jet_tagged_numbers_ntb_1')][0][2]/transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]])[plotnames.index('W_jet_cand_numbers_ntb_1')][0][2]

#raw_input()



numeratorindexlist=[plotnames.index('bottom_jet_tagged_numbers_wtb_1'),plotnames.index('bottom_jet_tagged_numbers_ntb_1'),plotnames.index('W_jet_tagged_numbers_wtb_1'),plotnames.index('W_jet_tagged_numbers_ntb_1')]
denumeratorindexlist=[plotnames.index('bottom_jet_cand_numbers_wtb_1'),plotnames.index('bottom_jet_cand_numbers_ntb_1'),plotnames.index('W_jet_cand_numbers_wtb_1'),plotnames.index('W_jet_cand_numbers_ntb_1')]

propLOL=efficiencies(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('ZprimeAll')]]),[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[SignalSamples[SignalSampleNames.index('ZprimeAll')]],numeratorindexlist,denumeratorindexlist ,name)
print propLOL

#raw_input()
writeListOfHistoLists(transposeLOL(transposeLOL(propLOL)),[SignalSamples[SignalSampleNames.index('ZprimeAll')]]+[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]], "","tag_prop_"+name,True,False,False,'histoE')

#writeListOfHistoLists([transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('bottom_jet_tagged_numbers_wtb_1')]]+[transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('bottom_jet_tagged_numbers_ntb_1')]],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]], '','single_regions_QCD'+name,False,False,False,'histoE')
  

listOfHistoListsSignal_rebinned=rebintovarbinsLOL(listOfHistoListsSignal,False,False,False,False)
listOfHistoListsSignal=listOfHistoListsSignal_rebinned
chekcNbins(listOfHistoListsSignal)

lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD,False,False,False,False)
listOfHistoListsABCD=lolABCD_rebinned
chekcNbins(listOfHistoListsABCD)


  
#lolBackgroundT=transposeLOL(listOfHistoListsBackground)
lolABCDT=transposeLOL(listOfHistoListsABCD)
#lolDataT=transposeLOL(listOfHistoListsData)

#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)
#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)


#lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD,False,False,False,True)

#chekcNbins(lolABCD_rebinned)

writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('ABCD5_notopbtag_CatA_Zprime_M_beta_first'):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first')+1],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]], '','single_regions_QCD'+name,False,False,False,'histoE')




####ABCDclosure1D_final
#for ABCDversion in ['ABCD','ABCD2','ABCD3','ABCD4','ABCD5','ABCD6','ABCD7','ABCD8','ABCD9','ABCD10']:
for ABCDversion in ['ABCD5']:
	ABCDclosure1D_final(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]),plotnames,[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]],ABCDversion+'_notopbtag_CatA_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatB_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatC_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatD_Zprime_M_beta_first', ABCDversion+'_notopbtag_CatE_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatF_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatG_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_notopbtag')
	#ABCDclosure1D_new(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]),plotnames,samples,ABCDversion+'_notopbtag_CatA_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatB_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatC_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatD_Zprime_M_beta_first', ABCDversion+'_notopbtag_CatE_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatF_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatG_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_notopbtag')
	ABCDclosure1D_final(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]),plotnames,[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]],ABCDversion+'_withtopbtag_CatA_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatB_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatC_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatD_Zprime_M_beta_first', ABCDversion+'_withtopbtag_CatE_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatF_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatG_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_withtopbtag')
	#ABCDclosure1D_new(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]),plotnames,samples,ABCDversion+'_withtopbtag_CatA_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatB_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatC_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatD_Zprime_M_beta_first', ABCDversion+'_withtopbtag_CatE_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatF_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatG_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_withtopbtag')
	#ABCDclosure1D_new(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]),plotnames,samples,ABCDversion+'_inclusive_CatA_Zprime_M_beta_first',ABCDversion+'_inclusive_CatB_Zprime_M_beta_first',ABCDversion+'_inclusive_CatC_Zprime_M_beta_first',ABCDversion+'_inclusive_CatD_Zprime_M_beta_first',ABCDversion+'_inclusive_CatE_Zprime_M_beta_first',ABCDversion+'_inclusive_CatF_Zprime_M_beta_first',ABCDversion+'_inclusive_CatG_Zprime_M_beta_first',ABCDversion+'_inclusive_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_inclusive')



#for l in transposeLOL(listOfHistoListsSignal):
    #for hsig,hqcd in zip(l,transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]):
            #hsig.Add(hqcd,1.0)

#for ABCDversion in ['ABCD5']:
    #for signalname in SignalSampleNames:
	#ABCDclosure1D_new(transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index(signalname)]]),plotnames,SignalSamples,ABCDversion+'_notopbtag_CatA_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatB_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatC_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatD_Zprime_M_beta_first', ABCDversion+'_notopbtag_CatE_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatF_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatG_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_notopbtag')
	#ABCDclosure1D_new(transposeLOL([transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index(signalname)]]),plotnames,SignalSamples,ABCDversion+'_withtopbtag_CatA_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatB_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatC_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatD_Zprime_M_beta_first', ABCDversion+'_withtopbtag_CatE_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatF_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatG_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_withtopbtag')
	##ABCDclosure1D_new(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]),plotnames,samples,ABCDversion+'_inclusive_CatA_Zprime_M_beta_first',ABCDversion+'_inclusive_CatB_Zprime_M_beta_first',ABCDversion+'_inclusive_CatC_Zprime_M_beta_first',ABCDversion+'_inclusive_CatD_Zprime_M_beta_first',ABCDversion+'_inclusive_CatE_Zprime_M_beta_first',ABCDversion+'_inclusive_CatF_Zprime_M_beta_first',ABCDversion+'_inclusive_CatG_Zprime_M_beta_first',ABCDversion+'_inclusive_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_inclusive')





#for ABCDversion in ['ABCD3','ABCD5']:
	#ABCDclosure1D_oneside(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]),plotnames,samples,ABCDversion+'_notopbtag_CatA_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatB_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatC_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatD_Zprime_M_beta_first', ABCDversion+'_notopbtag_CatE_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatF_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatG_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_notopbtag')


#################################################################################################################
##Here Starts: Plots And Calculating



##Stack Plot, Background and Signal, Z_Prime_M
##writeLOLSeveralOnTop(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1])[:plotnames.index("Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M")+1],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1],transposeLOL(lolSignalT),SignalSamples,-0.2,'Zprime',False ,'histoE','samehistoE')
##print "plot_Zprime_MC_Lena Len(listOfHistoListsABCD):"+str( len(listOfHistoListsABCD) )


##writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_bottom_csv_v2_vs_Zprime_M")+1], BackgroundSamples , plotnames[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_bottom_csv_v2_vs_Zprime_M")+1], 'ABCD_2D_Zprime' , True, False, False, "colz", False, False, False, True)


#writeListOfHistoLists( transposeLOL([lolABCDT[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('ABCD_notopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_Bottom_CSV_v2_vs_TprimeM")+1], [BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]] , plotnames[plotnames.index('ABCD_notopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_Bottom_CSV_v2_vs_TprimeM")+1], 'ABCD_2D'+name , True, False, False, "colz", False, False, False, True)

##writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_notopbtag_CatA_Zprime_M" ) : plotnames.index( "ABCD_notopbtag_CatH_Zprime_M_first" ) +1] , "Integrallist_before_multiplication.tex" , SampleNames )
##writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_beta" ) : plotnames.index( "ABCD_notopbtag_CatH_Zprime_M_beta" ) +1] , "Integrallist_before_multiplication_beta.tex" , SampleNames )


##Compare BackgroundAndSignal in SignalSample (mistaged Signal infuences Background prediction )
#compareEntriesInBackgroundAndSignalRegion( transposeLOL(listOfHistoListsSignal), "ComparisonIntegralsinSignalSample.txt" )

# Correlationfactor  (with difference to selection with only first element)
writeCorrLOL(listOfHistoListsABCD[plotnames.index('ABCD_notopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_Bottom_CSV_v2_vs_TprimeM")+1] , "Correlationfactors/"+name+"_Correlationfactors"+radi+".txt", plotnames[plotnames.index('ABCD_notopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_Bottom_CSV_v2_vs_TprimeM")+1], ["tt-bar", "QCD_HT"] , True )





#### Correlationfactor  (with difference to selection with only first element)
#writeCorrLOLinTEX( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_withtopbtag_W_tau21_vs_TprimeM")+1], "Correlationfactors.tex", plotnames[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_withtopbtag_W_tau21_vs_TprimeM")+1], ["tt-bar", "QCD_HT", "QCD_Pt", "QCD_comb"] , True )



###################
##Test if shape of CatA=shape of CatB






## # ABCD-Zprime_M Plots Work?
## writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_notopbtag_CatA_Zprime_M'):plotnames.index('ABCD_notopbtag_CatH_Zprime_M_first_beta')+1], BackgroundSamples , plotnames[plotnames.index('ABCD_notopbtag_CatA_Zprime_M'):plotnames.index('ABCD_notopbtag_CatH_Zprime_M_first_beta')+1], 'ABCD_ZPrime_M' , True, False, False, "histoE", False, False, False, True)


##
##
##
##
### Multiply and Divide for ABCD Methode - short verion with funktion ReconstructWithABCD()
#for plotname in CatAList:
    #ReconstructWithABCD(listOfHistoListsABCD, plotname, plotnames)
    #ReconstructWithABCD(listOfHistoListsSignal, plotname, plotnames)

##
##
##
##
##Add Signal and Backgroundhistos
#XC_Factor=1
#weights= [ XC_Factor/138.07, XC_Factor/86.28, XC_Factor/37.6 ]
#for plotnameindex in range(plotnames.index("ABCD_notopbtag_CatA_Zprime_M"), plotnames.index("ABCD_notopbtag_CatH_Zprime_M_first") ):
    #for index, listOfHistoList, weight in zip(range(3),listOfHistoListsSignalAndBackground, weights):
        #addHistos(listOfHistoList, plotnameindex, plotnameindex + len(plotnames), weight , True, index)

##Multiply and Divide for ABCD
#for listOfHistoList in listOfHistoListsSignalAndBackground:
    #for plotname in CatAList:
        #ReconstructWithABCD(listOfHistoList, plotname, plotnames)

##
##
##
##
##
##
##
###Write ListOfIntegralLists
#writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_notopbtag_CatA_Zprime_M" ) : plotnames.index( "ABCD_notopbtag_CatH_Zprime_M_first" ) +1] , "Integrallist_after_multiplication.tex" , SampleNames )
## writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_beta" ) : plotnames.index( "ABCD_notopbtag_CatH_Zprime_M_beta" ) +1] , "Integrallist_after_multiplication_beta.tex" , SampleNames )
##
##
##
##
##

##Create and Write List Of RatioPlots
##Workaround to use writeListOfHistoLists with a Transposed ListOfHistoList (uses trnasposeLOLextendet in plotutils.py)

#WASamples = 50*[ BackgroundSamples[0], BackgroundSamples[1] ]
#WAPlotNames =  [   "ABCD_notopbtag_CatA_Zprime_M"   ,
                 #"ABCD_notopbtag_CatE_Zprime_M"  ,
                 #"ABCD_notopbtag_CatA_Zprime_M_beta" ,
                 #"ABCD_notopbtag_CatE_Zprime_M_beta" ,
                 ## "ABCD_notopbtag_CatA_Zprime_M_one_sided" ,
                 ## "ABCD_notopbtag_CatE_Zprime_M_one_sided",
                 #"ABCD_notopbtag_CatA_Zprime_M_beta_first",
                 #"ABCD_notopbtag_CatE_Zprime_M_beta_first",
                 #"ABCD_notopbtag_CatA_Zprime_M_first",
                 #"ABCD_notopbtag_CatE_Zprime_M_first" ]

#IndexListToTranspose = [ [plotnames.index( "ABCD_notopbtag_CatA_Zprime_M" ) , plotnames.index( "ABCD_notopbtag_CatB_Zprime_M" ) ] ,
    #[ plotnames.index( "ABCD_notopbtag_CatE_Zprime_M" ), plotnames.index( "ABCD_notopbtag_CatF_Zprime_M" ) ],
    #[plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_beta" ), plotnames.index( "ABCD_notopbtag_CatB_Zprime_M_beta" ) ] ,
    #[plotnames.index( "ABCD_notopbtag_CatE_Zprime_M_beta" ), plotnames.index( "ABCD_notopbtag_CatF_Zprime_M_beta" ) ] ,
    ## [plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_one_sided" ), plotnames.index( "ABCD_notopbtag_CatB_Zprime_M_one_sided" ) ],
    ## [plotnames.index( "ABCD_notopbtag_CatE_Zprime_M_one_sided" ), plotnames.index( "ABCD_notopbtag_CatF_Zprime_M_one_sided" ) ],
    #[plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_beta_first") , plotnames.index("ABCD_notopbtag_CatB_Zprime_M_beta_first") ] ,
    #[plotnames.index( "ABCD_notopbtag_CatE_Zprime_M_beta_first") , plotnames.index( "ABCD_notopbtag_CatF_Zprime_M_beta_first")],
    #[plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_first") , plotnames.index("ABCD_notopbtag_CatB_Zprime_M_first") ] ,
    #[plotnames.index( "ABCD_notopbtag_CatE_Zprime_M_first") , plotnames.index( "ABCD_notopbtag_CatF_Zprime_M_first")]]





### For BackgroundSamples
#WASLnames2 =[]
#for string in WAPlotNames:
    #for sample in SampleNames:
        #WASLnames2.append( string + "_" + sample )

#RatioPlotList = transposeLOLextended( listOfHistoListsABCD,  IndexListToTranspose)
#writeListOfHistoLists( RatioPlotList , WASamples ,  WASLnames2 , 'RatioPlotList' , False , False, False, "histoE", False, False, True, False)



####Print all Plots for Z_Prime (Signal)
##WASignalSamplePlotNames2=[]
##for string in WAPlotNames:
    ##for sample in SignalSampleNames:
        ##WASignalSamplePlotNames2.append( string + "_" + sample)

##RatioPlotListSignal = transposeLOLextended( listOfHistoListsSignal, IndexListToTranspose )
##writeListOfHistoLists( RatioPlotListSignal , WASamples , WASignalSamplePlotNames2 , 'RatioPlotListSignal' , False , False, False, "histoE", False, False, True, False)




##RatioPlots for Combined Background and Signal Sample
#WASignalSamplePlotNameListOfLists=[]
#for SignalSampleName in SignalSampleNames:
    #ListToAppend=[]
    #for PlotName in WAPlotNames:
        #for SampleName in SampleNames:
            #ListToAppend.append(SignalSampleName+SampleName+PlotName)
    #WASignalSamplePlotNameListOfLists.append(ListToAppend)

#for WASignalSamplePlotNameList, SignalSampleName, listOfHistoListSignalAndBackground in zip(WASignalSamplePlotNameListOfLists, SignalSampleNames, listOfHistoListsSignalAndBackground):
    #RatioPlotListComb = transposeLOLextended( listOfHistoListSignalAndBackground, IndexListToTranspose )
    #writeListOfHistoLists( RatioPlotListComb , WASamples , WASignalSamplePlotNameList , 'RatioPlotListComb'+SignalSampleName , False , False, False, "histoE", False, False, True, False)




#### RatioPlots and Error Fit Polinomial , A/B - Signal over Background
##for WASignalSamplePlotNameList, SignalSampleName, listOfHistoListSignalAndBackground in zip(WASignalSamplePlotNameListOfLists, SignalSampleNames, listOfHistoListsSignalAndBackground):
    ##RatioPlotListComb = transposeLOLextended( listOfHistoListSignalAndBackground, IndexListToTranspose )
    ##ListOfPureRatioPlots = []
    ##for HistoList in RatioPlotListComb:
        ##HistoList[0].Divide(HistoList[1])
        ##ListOfPureRatioPlots.append( [HistoList[0] ]  )
    ### writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol2_"+SignalSampleName, 1, "pol2", WASignalSamplePlotNameList, True)
    ##writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol0_"+SignalSampleName, 1, "pol0", WASignalSamplePlotNameList, True)
    ### writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol0_"+SignalSampleName, 1, "pol0", WASignalSamplePlotNameList, True)


### Ratio Plot with Errors, A/B - Signal over Background, without Signalcontamination
#ListOfPureRatioPlots=[]
#for histoList in RatioPlotList:
    #histoList[0].Divide(histoList[1])
    #ListOfPureRatioPlots.append( [histoList[0] ])
#writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol0_Background", 1, "pol0", WASLnames2, True)
## writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol2_Background", 1, "pol2", WASLnames2, True)
## writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol0_Background", 1, "pol0", WASLnames2, True)




### Uncomple STACK PLOT


####Modify Signal And Background listOfHistoList (substract from backgroundprediction)
##for index in range( plotnames.index("ABCD_notopbtag_CatA_Zprime_M"),plotnames.index("ABCD_notopbtag_CatH_Zprime_M_first") +1):
    ##if plotnames[index][8] =="B":
        ##listOfHistoListsSignalAndBackground25001200[index][1].Add(listOfHistoListsABCD[index][1], -1)
        ###listOfHistoListsSignalAndBackground25001200[index][1].Multiply(-1)

        ##listOfHistoListsSignalAndBackground25001200[index-1][1].Add(listOfHistoListsABCD[index-1][0])#Add to Signal and QCD-Background in Signal ttbar in Signal Region

####Create a hISTOlIST TO DO stackPlotABCD
##ListOfHistoListsFinalStackPlot = []
##titlelist = []
##for index in range( plotnames.index("ABCD_notopbtag_CatA_Zprime_M"), plotnames.index("ABCD_notopbtag_CatH_Zprime_M_first") +1):
    ##if plotnames[index][8] =="A":
        ##ListToAppend = []
        ##titlelist.append( listOfHistoListsABCD[index][0].GetName()[5:] )
        ##ListToAppend.append(listOfHistoListsSignalAndBackground25001200[index+1][0]) #Signal
        ##ListToAppend.append(listOfHistoListsSignalAndBackground25001200[index+1][1]) #Signalkontamination
        ##ListToAppend.append(listOfHistoListsABCD[index+1][1]) #QCD_HAT in CatB
        ##ListToAppend.append(listOfHistoListsABCD[index][0]) #ttbar in Signal Region
        ##ListOfHistoListsFinalStackPlot.append(ListToAppend)

##colorlist =[ ROOT.kBlack , ROOT.kRed, ROOT.kYellow,ROOT.kBlue]
##stacklist = [False, True, True, True]
##optionlist = ["E", "histoE", "histoE", "histoE"]
##stackPlotABCD(ListOfHistoListsFinalStackPlot, "StackPlotsABCD", colorlist=colorlist, labellist=["ttbar", "QCD-Backgroundestimation", "Signalcontamination", "Signal"], titlelist = titlelist, stacklist = stacklist, optionlist = optionlist)

##print "Plotnames contains:"
##for i in plotnames:
    ##print i
    
    
    
    
#Anmerkungen fuer Simon:
#Das Skript erzeugt die folgenden Dateien:
#
#Integrallist_before_multiplication.tex
#2D Histogramme in Ordner "ABCD_2D"
#Correlationfactors.tex
#Integrallist_after_multiplication.tex
#Rekonstruktion von Kategoie A und E in "RatioPlotList"
#Signalkontamination in "RatioPlotListComb"+SignalSampleName
#Fehlerbaender in "RatioPlotFit_pol0_Background"
