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

name='Zprime_MC_Lena_'+ABCDeventhandling+'_'+WPs
SampleNames=['ttbar' , 'QCD_HT', 'QCD_Pt' ]
SignalSampleNames=['Zprime1500900',  'Zprime20001200',  'Zprime25001200']




# definition of categories

# categoriesZprimeTprime=[
#	("(tWb&&N_BTagsM=1)","tWb1",""),#
#	("(tWb&&N_BTagsM=2)","tWb2",""),
#	("(ttH&&N_BTagsM=1)","ttH1",""),
#	("(ttH&&N_BTagsM=2)","ttH2",""),
#	("(ttH&&N_BTagsM=3)","ttH3",""),
#	("(ttH&&N_BTagsM=4)","ttH4",""),
#	("(ttZ)","ttZ",""),
#]




## book plots
#plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
#plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
#plotselection1="Evt_HT>850"
#plotselection2="N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 && Evt_HT>850 "



##Own Plotselections for ABCD-method

#plotselection_tau32 = " Tops_ABCD_t32 < 0.86   "
##plotselection_tau32 = " Tops_ABCD_t32 < 0.67   "
#plotselection_W_MSD =  " (70 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 100) "
#plotselection_B_CSV = "  Bottoms_ABCD_CSV > 0.8  "
#plotselection_W_tau21 = " Ws_ABCD_t21 < 0.6 "
##plotselection_W_tau21 = " Ws_ABCD_t21 < 0.45"
#plotselection_t_MSD = " (105 < Tops_ABCD_MSD && Tops_ABCD_MSD < 210) "
#plotselection_topsubjetCSVv2 = " Tops_ABCD_maxsubjetCSVv2 > 0.8 "




#plotselection_tau32_0 = " Tops_ABCD_t32[0] < 0.86   "
##plotselection_tau32_0 = " Tops_ABCD_t32[0] < 0.67   "
#plotselection_W_MSD_0 =  " (70 < Ws_ABCD_MSD[0]  &&   Ws_ABCD_MSD[0] < 100) "
#plotselection_B_CSV_0 = "  Bottoms_ABCD_CSV[0] > 0.8   "
#plotselection_W_tau21_0 = " Ws_ABCD_t21[0] < 0.6  "
##plotselection_W_tau21_0 = " Ws_ABCD_t21[0] < 0.45  "

#plotselection_tau32_anti=" Tops_ABCD_t32 > 0.86   "
#plotselection_W_MSD_anti =  " (70 > Ws_ABCD_MSD  ||   Ws_ABCD_MSD > 100) "
#plotselection_B_CSV_anti = "  Bottoms_ABCD_CSV < 0.8   "
#plotselection_W_tau21_anti = " Ws_ABCD_t21 > 0.6 "
#plotselection_t_MSD_anti = " (105 > Tops_ABCD_MSD || Tops_ABCD_MSD > 210) "
#plotselection_topsubjetCSVv2_anti = " Tops_ABCD_maxsubjetCSVv2 < 0.8 "

#plotselection_tau32_anti_0 =" Tops_ABCD_t32[0] > 0.86   "
#plotselection_W_MSD_anti_0 =  " (70 > Ws_ABCD_MSD[0]  ||   Ws_ABCD_MSD[0] > 100) "
#plotselection_B_CSV_anti_0 = "  Bottoms_ABCD_CSV[0] < 0.8   "
#plotselection_W_tau21_anti_0 = " Ws_ABCD_t21[0]  > 0.6 "




#plotselection_W_MSD_one_sided =  " (70 < Ws_ABCD_MSD && Ws_ABCD_MSD < 100)"
#plotselection_W_MSD_one_sided_anti =  " (70 > Ws_ABCD_MSD && Ws_ABCD_MSD < 100)"




#plotselection_sideband = "Signal_Topfirst_Zprime_M < 0"
#plotselection_sideband_withtopbtag = "Signal_withtopbtag_Topfirst_Zprime_M < 0"


#plotselection_ABCD_general=  plotselection2 + "&& Zprimes_ABCD_M>0   &&    Ws_ABCD_t21 <  0.6    &&    100 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210  "
#plotselection_ABCD_general_beta =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    70 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 100     &&    100 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210   "
#plotselection_ABCD_general_beta2 =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    70 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 100     &&     Tops_ABCD_t32 < 0.86   "
#plotselection_ABCD_general_0 =  plotselection2 + "&& Zprimes_ABCD_M[0]>0   &&    Ws_ABCD_t21[0] >  0.6    &&    100 < Tops_ABCD_MSD[0]     &&    Tops_ABCD_MSD[0]  < 210   "
#plotselection_ABCD_general_beta_0 =   plotselection2 + "&& Zprimes_ABCD_M[0]>0   &&    70 < Ws_ABCD_MSD[0]  &&   Ws_ABCD_MSD[0] < 100     &&    100 < Tops_ABCD_MSD[0]     &&    Tops_ABCD_MSD[0]  < 210   "

#plotselection_ABCD_general_alt_notopbtag =  plotselection2 + " && Zprimes_ABCD_masscorrnotopbtag_M>0 && 70 < Ws_ABCD_masscorrnotopbtag_MSD && Ws_ABCD_masscorrnotopbtag_MSD < 100 && Tops_ABCD_masscorrnotopbtag_t32<0.86 "
#plotselection_ABCD_general_alt_withtopbtag =  plotselection2 + " && Zprimes_ABCD_masscorrwithtopbtag_M>0 && 70 < Ws_ABCD_masscorrwithtopbtag_MSD && Ws_ABCD_masscorrwithtopbtag_MSD < 100 && Tops_ABCD_masscorrwithtopbtag_t32<0.86 "



#Create Plots

plots=[


    ##Signalregion
    Plot(ROOT.TH1F("Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
    Plot(ROOT.TH1F("Signal_withtopbtag_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Signal_withtopbtag_Topfirst_Zprime_M",plotselection2+"&&Signal_withtopbtag_Topfirst_Zprime_M>0","1 btag"),
    ##One Anti
    #Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-btag",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0","1 anti-btag"),
    #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-Wtag",50,0,5000),"Sideband_W_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 anti-Wtag"),
    #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 anti-ttag"),

    ##Two Anti
    #Plot(ROOT.TH1F("Sideband_top_anti_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag + anti-btag",50,0,5000),"Sideband_top_anti_bottom_anti_Topfirst_Zprime_M",plotselection2		+"&&Sideband_top_anti_bottom_anti_Topfirst_Zprime_M>0","1 anti-ttag + 1 anti-btag"),
    #Plot(ROOT.TH1F("Sideband_W_anti_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-Wtag + anti-btag",50,0,5000),"Sideband_W_anti_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_W_anti_bottom_anti_Topfirst_Zprime_M>0","1 anti-Wtag + 1 anti-btag"),
    #Plot(ROOT.TH1F("Sideband_top_anti_W_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag + anti-Wtag",50,0,5000),"Sideband_top_anti_W_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_W_anti_Topfirst_Zprime_M>0","1 anti-ttag + 1 anti-Wtag"),

    ##Three Anti
    #Plot(ROOT.TH1F("Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag + anti-Wtag + anti-ttag",50,0,5000),"Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M>0","1 anti-ttag + 1 anti-Wtag + 1 anti-ttag"),





    #All elements
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_top_MSD" ,"tau_{32}(t) VS m_{SD}(t)",20,0,1,30,0,300),"Tops_ABCD_MSD","Tops_ABCD_t32",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_MSD>0 && Tops_ABCD_t32>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_W_tau21" ,"tau_{32}(t) VS tau_{21}(W)",20,0,1,20,0,1),"Tops_ABCD_t32","Ws_ABCD_t21",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_W_MSD" ,"tau_{32}(t) VS m_{SD}(W)",20,0,1,30,0,300),"Tops_ABCD_t32","Ws_ABCD_MSD",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Ws_ABCD_MSD>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_MSD_vs_W_tau21" ,"m_{SD}(t) VS tau_{21}(W)",30,0,300,20,0,1),"Tops_ABCD_MSD","Ws_ABCD_t21",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_MSD>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_MSD_vs_W_MSD" ,"m_{SD}(t) VS m_{SD}(t)(W)",30,0,300,30,0,300),"Tops_ABCD_MSD","Ws_ABCD_MSD",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_MSD>0 && Ws_ABCD_MSD>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(t) VS CSV_v2(b)",30,0,300,20,0,1),"Tops_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_MSD>0 && Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_MSD_vs_W_tau21" ,"m_{SD}(W) VS tau_{21}(W)",30,0,300,20,0,1),"Ws_ABCD_MSD","Ws_ABCD_t21",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Ws_ABCD_MSD>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",30,0,300,20,0,1),"Ws_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Ws_ABCD_MSD>0 &&Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_tau21_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",30,0,300,20,0,1),"Ws_ABCD_t21","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Ws_ABCD_t21>0 &&Bottoms_ABCD_CSV>0","1 btag"),

    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Topsubjet_CSV_v2" ,"tau_{32}(t) VS CSV_v2(t-sub)",20,0,1,20,0,1),"Tops_ABCD_t32","Tops_ABCD_maxsubjetCSVv2",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Tops_ABCD_maxsubjetCSVv2>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_Topsubjet_CSV_v_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_maxsubjetCSVv2","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_maxsubjetCSVv2>0 && Bottoms_ABCD_CSV>0","1 btag"),


    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_ZprimeM" ,"tau_{32}(t) VS m(Z')",20,0,1,50,0,5000),"Tops_ABCD_t32","Zprimes_ABCD_M",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Zprimes_ABCD_M>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_Bottom_CSV_v2_vs_ZprimeM" ,"CSV_v2(b) VS m(Z')",20,0,1,50,0,5000),"Bottoms_ABCD_CSV","Zprimes_ABCD_M",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>0","1 btag"),    
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_W_tau21_vs_ZprimeM" ,"tau_{21}(W) VS m(Z')",20,0,1,50,0,5000),"Ws_ABCD_t21","Zprimes_ABCD_M",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Ws_ABCD_t21>0 && Zprimes_ABCD_M>0","1 btag"),

    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime01000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>0 && Zprimes_ABCD_M<1000","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime10001250" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>1000 && Zprimes_ABCD_M<1250","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime12501500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>1250 && Zprimes_ABCD_M<1500","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime15001750" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>1500 && Zprimes_ABCD_M<1750","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime17502000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>1750 && Zprimes_ABCD_M<2000","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime20002250" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>2000 && Zprimes_ABCD_M<2250","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime22502500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>2250 && Zprimes_ABCD_M<2500","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime25003000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>2500 && Zprimes_ABCD_M<3000","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime30003500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>3000 && Zprimes_ABCD_M<3500","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime35004000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>3500 && Zprimes_ABCD_M<4000","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime40004500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>4000 && Zprimes_ABCD_M<4500","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_notopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime45005000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2_anti +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>4500 && Zprimes_ABCD_M<5000","1 btag"),
    
    #All elements
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_top_MSD" ,"tau_{32}(t) VS m_{SD}(t)",20,0,1,30,0,300),"Tops_ABCD_MSD","Tops_ABCD_t32",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_MSD>0 && Tops_ABCD_t32>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_W_tau21" ,"tau_{32}(t) VS tau_{21}(W)",20,0,1,20,0,1),"Tops_ABCD_t32","Ws_ABCD_t21",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_W_MSD" ,"tau_{32}(t) VS m_{SD}(W)",20,0,1,30,0,300),"Tops_ABCD_t32","Ws_ABCD_MSD",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Ws_ABCD_MSD>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_MSD_vs_W_tau21" ,"m_{SD}(t) VS tau_{21}(W)",30,0,300,20,0,1),"Tops_ABCD_MSD","Ws_ABCD_t21",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_MSD>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_MSD_vs_W_MSD" ,"m_{SD}(t) VS m_{SD}(t)(W)",30,0,300,30,0,300),"Tops_ABCD_MSD","Ws_ABCD_MSD",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_MSD>0 && Ws_ABCD_MSD>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(t) VS CSV_v2(b)",30,0,300,20,0,1),"Tops_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_MSD>0 && Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_W_MSD_vs_W_tau21" ,"m_{SD}(W) VS tau_{21}(W)",30,0,300,20,0,1),"Ws_ABCD_MSD","Ws_ABCD_t21",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Ws_ABCD_MSD>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_W_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",30,0,300,20,0,1),"Ws_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Ws_ABCD_MSD>0 &&Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_W_tau21_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",30,0,300,20,0,1),"Ws_ABCD_t21","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Ws_ABCD_t21>0 &&Bottoms_ABCD_CSV>0","1 btag"),

    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Topsubjet_CSV_v2" ,"tau_{32}(t) VS CSV_v2(t-sub)",20,0,1,20,0,1),"Tops_ABCD_t32","Tops_ABCD_maxsubjetCSVv2",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Tops_ABCD_maxsubjetCSVv2>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_Topsubjet_CSV_v_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_maxsubjetCSVv2","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_maxsubjetCSVv2>0 && Bottoms_ABCD_CSV>0","1 btag"),


    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_ZprimeM" ,"tau_{32}(t) VS m(Z')",20,0,1,50,0,5000),"Tops_ABCD_t32","Zprimes_ABCD_M",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Zprimes_ABCD_M>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_Bottom_CSV_v2_vs_ZprimeM" ,"CSV_v2(b) VS m(Z')",20,0,1,50,0,5000),"Bottoms_ABCD_CSV","Zprimes_ABCD_M",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>0","1 btag"),    
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_W_tau21_vs_ZprimeM" ,"tau_{21}(W) VS m(Z')",20,0,1,50,0,5000),"Ws_ABCD_t21","Zprimes_ABCD_M",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Ws_ABCD_t21>0 && Zprimes_ABCD_M>0","1 btag"),

    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime01000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>0 && Zprimes_ABCD_M<1000","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime10001250" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>1000 && Zprimes_ABCD_M<1250","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime12501500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>1250 && Zprimes_ABCD_M<1500","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime15001750" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>1500 && Zprimes_ABCD_M<1750","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime17502000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>1750 && Zprimes_ABCD_M<2000","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime20002250" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>2000 && Zprimes_ABCD_M<2250","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime22502500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>2250 && Zprimes_ABCD_M<2500","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime25003000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>2500 && Zprimes_ABCD_M<3000","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime30003500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>3000 && Zprimes_ABCD_M<3500","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime35004000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>3500 && Zprimes_ABCD_M<4000","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime40004500" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>4000 && Zprimes_ABCD_M<4500","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime45005000" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0 && Zprimes_ABCD_M>4500 && Zprimes_ABCD_M<5000","1 btag"),



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
    # no topsubbtag
    Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatB_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatC_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatD_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatE_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatF_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatG_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatH_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,
    
    # with topsubbtag
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,
    
    #inclusive
    Plot(ROOT.TH1F("ABCD_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatA_withtopbtag) || ABCD_CatID==ABCD_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatB_withtopbtag) || ABCD_CatID==ABCD_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatC_withtopbtag) || ABCD_CatID==ABCD_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatD_withtopbtag) || ABCD_CatID==ABCD_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatE_withtopbtag) || ABCD_CatID==ABCD_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatF_withtopbtag) || ABCD_CatID==ABCD_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatG_withtopbtag) || ABCD_CatID==ABCD_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatH_withtopbtag) || ABCD_CatID==ABCD_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,




    #ABCD2
    #no topbtag
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD_notopbtag2_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    #inclusive
    Plot(ROOT.TH1F("ABCD2_inclusive_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatA_withtopbtag) || ABCD2_CatID==ABCD2_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatB_withtopbtag) || ABCD2_CatID==ABCD2_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatC_withtopbtag) || ABCD2_CatID==ABCD2_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatD_withtopbtag) || ABCD2_CatID==ABCD2_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD2_inclusive_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatE_withtopbtag) || ABCD2_CatID==ABCD2_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatF_withtopbtag) || ABCD2_CatID==ABCD2_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatG_withtopbtag) || ABCD2_CatID==ABCD2_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatH_withtopbtag) || ABCD2_CatID==ABCD2_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

#Tprime
    # no topsubbtag
    Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Tprime_M_beta_first" ,"m(Z') in GeV, CatA " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Tprime_M_beta_first" ,"m(Z') in GeV, CatB " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Tprime_M_beta_first" ,"m(Z') in GeV, CatC " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Tprime_M_beta_first" ,"m(Z') in GeV, CatD " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Tprime_M_beta_first" ,"m(Z') in GeV, CatE " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Tprime_M_beta_first" ,"m(Z') in GeV, CatF " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Tprime_M_beta_first" ,"m(Z') in GeV, CatG " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Tprime_M_beta_first" ,"m(Z') in GeV, CatH " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti ,"1 btag") ,
    
    # with topsubbtag
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatA_Tprime_M_beta_first" ,"m(Z') in GeV, CatA " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatB_Tprime_M_beta_first" ,"m(Z') in GeV, CatB " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatC_Tprime_M_beta_first" ,"m(Z') in GeV, CatC " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatD_Tprime_M_beta_first" ,"m(Z') in GeV, CatD " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD_withtopbtag_CatE_Tprime_M_beta_first" ,"m(Z') in GeV, CatE " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatF_Tprime_M_beta_first" ,"m(Z') in GeV, CatF " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatG_Tprime_M_beta_first" ,"m(Z') in GeV, CatG " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag_CatH_Tprime_M_beta_first" ,"m(Z') in GeV, CatH " ,50,0,2500),"Tprimes_ABCD_M", "ABCD_CatID==ABCD_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    #inclusive
    Plot(ROOT.TH1F("ABCD_inclusive_CatA_Tprime_M_beta_first" ,"m(Z') in GeV, CatA " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD_CatID==ABCD_CatA_withtopbtag) || ABCD_CatID==ABCD_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatB_Tprime_M_beta_first" ,"m(Z') in GeV, CatB " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD_CatID==ABCD_CatB_withtopbtag) || ABCD_CatID==ABCD_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatC_Tprime_M_beta_first" ,"m(Z') in GeV, CatC " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD_CatID==ABCD_CatC_withtopbtag) || ABCD_CatID==ABCD_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatD_Tprime_M_beta_first" ,"m(Z') in GeV, CatD " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD_CatID==ABCD_CatD_withtopbtag) || ABCD_CatID==ABCD_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD_inclusive_CatE_Tprime_M_beta_first" ,"m(Z') in GeV, CatE " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD_CatID==ABCD_CatE_withtopbtag) || ABCD_CatID==ABCD_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatF_Tprime_M_beta_first" ,"m(Z') in GeV, CatF " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD_CatID==ABCD_CatF_withtopbtag) || ABCD_CatID==ABCD_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatG_Tprime_M_beta_first" ,"m(Z') in GeV, CatG " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD_CatID==ABCD_CatG_withtopbtag) || ABCD_CatID==ABCD_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_inclusive_CatH_Tprime_M_beta_first" ,"m(Z') in GeV, CatH " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD_CatID==ABCD_CatH_withtopbtag) || ABCD_CatID==ABCD_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

#ABCD2
    #with topbtag
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatA_Tprime_M_beta_first" ,"m(Z') in GeV, CatA " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatB_Tprime_M_beta_first" ,"m(Z') in GeV, CatB " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatC_Tprime_M_beta_first" ,"m(Z') in GeV, CatC " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatD_Tprime_M_beta_first" ,"m(Z') in GeV, CatD " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD_notopbtag2_CatE_Tprime_M_beta_first" ,"m(Z') in GeV, CatE " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatF_Tprime_M_beta_first" ,"m(Z') in GeV, CatF " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatG_Tprime_M_beta_first" ,"m(Z') in GeV, CatG " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_notopbtag2_CatH_Tprime_M_beta_first" ,"m(Z') in GeV, CatH " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    #no topbtag
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatA_Tprime_M_beta_first" ,"m(Z') in GeV, CatA " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatB_Tprime_M_beta_first" ,"m(Z') in GeV, CatB " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatC_Tprime_M_beta_first" ,"m(Z') in GeV, CatC " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatD_Tprime_M_beta_first" ,"m(Z') in GeV, CatD " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatE_Tprime_M_beta_first" ,"m(Z') in GeV, CatE " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatF_Tprime_M_beta_first" ,"m(Z') in GeV, CatF " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatG_Tprime_M_beta_first" ,"m(Z') in GeV, CatG " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD_withtopbtag2_CatH_Tprime_M_beta_first" ,"m(Z') in GeV, CatH " ,50,0,2500),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    #inclusive
    Plot(ROOT.TH1F("ABCD2_inclusive_CatA_Tprime_M_beta_first" ,"m(Z') in GeV, CatA " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatA_withtopbtag) || ABCD2_CatID==ABCD2_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatB_Tprime_M_beta_first" ,"m(Z') in GeV, CatB " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatB_withtopbtag) || ABCD2_CatID==ABCD2_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatC_Tprime_M_beta_first" ,"m(Z') in GeV, CatC " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatC_withtopbtag) || ABCD2_CatID==ABCD2_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatD_Tprime_M_beta_first" ,"m(Z') in GeV, CatD " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatD_withtopbtag) || ABCD2_CatID==ABCD2_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD2_inclusive_CatE_Tprime_M_beta_first" ,"m(Z') in GeV, CatE " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatE_withtopbtag) || ABCD2_CatID==ABCD2_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatF_Tprime_M_beta_first" ,"m(Z') in GeV, CatF " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatF_withtopbtag) || ABCD2_CatID==ABCD2_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatG_Tprime_M_beta_first" ,"m(Z') in GeV, CatG " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatG_withtopbtag) || ABCD2_CatID==ABCD2_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD2_inclusive_CatH_Tprime_M_beta_first" ,"m(Z') in GeV, CatH " ,50,0,2500),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatH_withtopbtag) || ABCD2_CatID==ABCD2_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,




    #Plot(ROOT.TH1F("ABCD_notopbtagalt_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_masscorrnotopbtag_M",    plotselection_ABCD_general_alt_notopbtag + " && Tops_ABCD_masscorrnotopbtag_maxsubjetCSVv2<0.8 && (105<Tops_ABCD_masscorrnotopbtag_MSD && Tops_ABCD_masscorrnotopbtag_MSD<210) && Bottoms_ABCD_masscorrnotopbtag_CSV>0.8 && Ws_ABCD_masscorrnotopbtag_t21<0.6", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtagalt_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_masscorrnotopbtag_M",    plotselection_ABCD_general_alt_notopbtag + " && Tops_ABCD_masscorrnotopbtag_maxsubjetCSVv2<0.8 && (105>Tops_ABCD_masscorrnotopbtag_MSD || Tops_ABCD_masscorrnotopbtag_MSD>210) && Bottoms_ABCD_masscorrnotopbtag_CSV>0.8 && Ws_ABCD_masscorrnotopbtag_t21<0.6"+ "&&" + "IsnoSignalnotopbtag" ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtagalt_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_masscorrnotopbtag_M",    plotselection_ABCD_general_alt_notopbtag + " && Tops_ABCD_masscorrnotopbtag_maxsubjetCSVv2<0.8 && (105<Tops_ABCD_masscorrnotopbtag_MSD && Tops_ABCD_masscorrnotopbtag_MSD<210) && Bottoms_ABCD_masscorrnotopbtag_CSV<0.8 && Ws_ABCD_masscorrnotopbtag_t21<0.6"+ "&&" + "IsnoSignalnotopbtag" ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtagalt_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_masscorrnotopbtag_M",    plotselection_ABCD_general_alt_notopbtag + " && Tops_ABCD_masscorrnotopbtag_maxsubjetCSVv2<0.8 && (105>Tops_ABCD_masscorrnotopbtag_MSD || Tops_ABCD_masscorrnotopbtag_MSD>210) && Bottoms_ABCD_masscorrnotopbtag_CSV<0.8 && Ws_ABCD_masscorrnotopbtag_t21<0.6"+ "&&" + "IsnoSignalnotopbtag" ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD_notopbtagalt_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_masscorrnotopbtag_M",    plotselection_ABCD_general_alt_notopbtag + " && Tops_ABCD_masscorrnotopbtag_maxsubjetCSVv2<0.8 && (105<Tops_ABCD_masscorrnotopbtag_MSD && Tops_ABCD_masscorrnotopbtag_MSD<210) && Bottoms_ABCD_masscorrnotopbtag_CSV>0.8 && Ws_ABCD_masscorrnotopbtag_t21>0.6" + "&&" + "IsnoSignalnotopbtag" ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtagalt_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_masscorrnotopbtag_M",    plotselection_ABCD_general_alt_notopbtag + " && Tops_ABCD_masscorrnotopbtag_maxsubjetCSVv2<0.8 && (105>Tops_ABCD_masscorrnotopbtag_MSD || Tops_ABCD_masscorrnotopbtag_MSD>210) && Bottoms_ABCD_masscorrnotopbtag_CSV>0.8 && Ws_ABCD_masscorrnotopbtag_t21>0.6" + "&&" + "IsnoSignalnotopbtag" ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtagalt_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_masscorrnotopbtag_M",    plotselection_ABCD_general_alt_notopbtag + " && Tops_ABCD_masscorrnotopbtag_maxsubjetCSVv2<0.8 && (105<Tops_ABCD_masscorrnotopbtag_MSD && Tops_ABCD_masscorrnotopbtag_MSD<210) && Bottoms_ABCD_masscorrnotopbtag_CSV<0.8 && Ws_ABCD_masscorrnotopbtag_t21>0.6" + "&&" + "IsnoSignalnotopbtag" ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtagalt_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_masscorrnotopbtag_M",    plotselection_ABCD_general_alt_notopbtag + " && Tops_ABCD_masscorrnotopbtag_maxsubjetCSVv2<0.8 && (105>Tops_ABCD_masscorrnotopbtag_MSD || Tops_ABCD_masscorrnotopbtag_MSD>210) && Bottoms_ABCD_masscorrnotopbtag_CSV<0.8 && Ws_ABCD_masscorrnotopbtag_t21>0.6" + "&&" + "IsnoSignalnotopbtag" ,"1 btag") ,


    #Plot(ROOT.TH1F("ABCD_withtopbtagalt_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_masscorrwithtopbtag_M",    plotselection_ABCD_general_alt_withtopbtag + " && Tops_ABCD_masscorrwithtopbtag_maxsubjetCSVv2>0.8 && (105<Tops_ABCD_masscorrwithtopbtag_MSD && Tops_ABCD_masscorrwithtopbtag_MSD<210) && Bottoms_ABCD_masscorrwithtopbtag_CSV>0.8 && Ws_ABCD_masscorrwithtopbtag_t21<0.6", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtagalt_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_masscorrwithtopbtag_M",    plotselection_ABCD_general_alt_withtopbtag + " && Tops_ABCD_masscorrwithtopbtag_maxsubjetCSVv2>0.8 && (105>Tops_ABCD_masscorrwithtopbtag_MSD || Tops_ABCD_masscorrwithtopbtag_MSD>210) && Bottoms_ABCD_masscorrwithtopbtag_CSV>0.8 && Ws_ABCD_masscorrwithtopbtag_t21<0.6"+ "&&" + "IsnoSignalwithtopbtag" ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtagalt_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_masscorrwithtopbtag_M",    plotselection_ABCD_general_alt_withtopbtag + " && Tops_ABCD_masscorrwithtopbtag_maxsubjetCSVv2>0.8 && (105<Tops_ABCD_masscorrwithtopbtag_MSD && Tops_ABCD_masscorrwithtopbtag_MSD<210) && Bottoms_ABCD_masscorrwithtopbtag_CSV<0.8 && Ws_ABCD_masscorrwithtopbtag_t21<0.6"+ "&&" + "IsnoSignalwithtopbtag" ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtagalt_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_masscorrwithtopbtag_M",    plotselection_ABCD_general_alt_withtopbtag + " && Tops_ABCD_masscorrwithtopbtag_maxsubjetCSVv2>0.8 && (105>Tops_ABCD_masscorrwithtopbtag_MSD || Tops_ABCD_masscorrwithtopbtag_MSD>210) && Bottoms_ABCD_masscorrwithtopbtag_CSV<0.8 && Ws_ABCD_masscorrwithtopbtag_t21<0.6"+ "&&" + "IsnoSignalwithtopbtag" ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD_withtopbtagalt_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_masscorrwithtopbtag_M",    plotselection_ABCD_general_alt_withtopbtag + " && Tops_ABCD_masscorrwithtopbtag_maxsubjetCSVv2>0.8 && (105<Tops_ABCD_masscorrwithtopbtag_MSD && Tops_ABCD_masscorrwithtopbtag_MSD<210) && Bottoms_ABCD_masscorrwithtopbtag_CSV>0.8 && Ws_ABCD_masscorrwithtopbtag_t21>0.6" + "&&" + "IsnoSignalwithtopbtag" ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtagalt_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_masscorrwithtopbtag_M",    plotselection_ABCD_general_alt_withtopbtag + " && Tops_ABCD_masscorrwithtopbtag_maxsubjetCSVv2>0.8 && (105>Tops_ABCD_masscorrwithtopbtag_MSD || Tops_ABCD_masscorrwithtopbtag_MSD>210) && Bottoms_ABCD_masscorrwithtopbtag_CSV>0.8 && Ws_ABCD_masscorrwithtopbtag_t21>0.6" + "&&" + "IsnoSignalwithtopbtag" ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtagalt_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_masscorrwithtopbtag_M",    plotselection_ABCD_general_alt_withtopbtag + " && Tops_ABCD_masscorrwithtopbtag_maxsubjetCSVv2>0.8 && (105<Tops_ABCD_masscorrwithtopbtag_MSD && Tops_ABCD_masscorrwithtopbtag_MSD<210) && Bottoms_ABCD_masscorrwithtopbtag_CSV<0.8 && Ws_ABCD_masscorrwithtopbtag_t21>0.6" + "&&" + "IsnoSignalwithtopbtag" ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtagalt_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_masscorrwithtopbtag_M",    plotselection_ABCD_general_alt_withtopbtag + " && Tops_ABCD_masscorrwithtopbtag_maxsubjetCSVv2>0.8 && (105>Tops_ABCD_masscorrwithtopbtag_MSD || Tops_ABCD_masscorrwithtopbtag_MSD>210) && Bottoms_ABCD_masscorrwithtopbtag_CSV<0.8 && Ws_ABCD_masscorrwithtopbtag_t21>0.6" + "&&" + "IsnoSignalwithtopbtag" ,"1 btag") ,



    #Plot(ROOT.TH1F("Alt_MSD_test" ,"m(Z') in GeV, CatA " ,60,0,300),"Tops_ABCD_masscorrnotopbtag_MSD",    plotselection2, "1 btag"),
    #Plot(ROOT.TH1F("Norm_MSD_test" ,"m(Z') in GeV, CatA " ,60,0,300),"Tops_ABCD_MSD",    plotselection2, "1 btag"),


    #only first element
    #W_msd as third variable

    #Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  + "&&" + "IsnoSignalnotopbtag","1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),


    #Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),






    #doing only first element
    #beta (tau21)

    #Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",  "bportiondown*("+  plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag") ,
    


    #only first element
    #W_msd as third variable

    #Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  + "&&" + ""IsnoSignalnotopbtag"" +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),


    #doing only first element
    #beta (tau21)

    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatA_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatB_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatC_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatD_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatE_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatF_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatG_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatH_Zprime_M_beta_first_bottomcontribdown" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag") ,


    #only first element
    #W_msd as third variable

    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatA_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatB_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatC_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  + "&&" +plotselection_sideband+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatD_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatE_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatF_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatG_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatH_Zprime_M_first_bottomcontribdown" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    "bportiondown*("+ plotselection_ABCD_general + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",  "bportionnorm*("+  plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag") ,
    
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatA_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatB_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatC_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatD_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatE_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatF_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatG_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatH_Zprime_M_beta_first_bottomcontribnorm" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    "bportionnorm*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag") ,





    #Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",  "bportionup*("+  plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag") ,
    
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatA_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatB_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatC_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatD_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatE_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatF_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatG_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatH_Zprime_M_beta_first_bottomcontribup" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    "bportionup*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag") ,




    #Plot(ROOT.TH1F("ABCD_notopbtag_CatA_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",  "bportionno*("+  plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatB_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatC_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatD_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_notopbtag_CatE_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatF_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatG_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_notopbtag_CatH_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag") ,
    
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatA_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21+")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatB_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatC_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatD_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  +")", "1 btag"),


    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatE_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatF_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatG_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag"),
    #Plot(ROOT.TH1F("ABCD_withtopbtag_CatH_Zprime_M_beta_first_bottomcontribno" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M",    "bportionno*("+ plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2+ " && "  + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  +")", "1 btag") ,







#MSD manual sepaTest
    Plot(ROOT.TH1F("Notopbtag_Top_MSD" ,"m_{SD}(t-notoptag) in GeV" ,60,0,300),"Tops_ABCD_MSD",    plotselection2 + "&& Zprimes_ABCD_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("Withtopbtag_Top_MSD" ,"m_{SD}(t-withtoptag) in GeV",60,0,300),"Tops_ABCD_MSD",    plotselection2 + "&& Zprimes_ABCD_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("Notopbtag_W_MSD" ,"m_{SD}(W-notoptag) in GeV" ,60,0,300),"Ws_ABCD_MSD",    plotselection2 + "&& Zprimes_ABCD_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("Withtopbtag_W_MSD" ,"m_{SD}(W-withtoptag) in GeV" ,60,0,300),"Ws_ABCD_MSD",    plotselection2 + "&& Zprimes_ABCD_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    
    Plot(ROOT.TH1F("Notopbtag_Top_t32" ,"t_{32}(t-notoptag) in GeV" ,20,0,1),"Tops_ABCD_t32",    plotselection2 + "&& Zprimes_ABCD_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("Withtopbtag_Top_t32" ,"t_{32}(t-withtoptag) in GeV",20,0,1),"Tops_ABCD_t32",    plotselection2 + "&& Zprimes_ABCD_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("Notopbtag_W_t21" ,"W_{21}(W-notoptag) in GeV" ,20,0,1),"Ws_ABCD_t21",    plotselection2 + "&& Zprimes_ABCD_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_tau32, "1 btag"),
    Plot(ROOT.TH1F("Withtopbtag_W_t21" ,"W_{21}(W-withtoptag) in GeV" ,20,0,1),"Ws_ABCD_t21",    plotselection2 + "&& Zprimes_ABCD_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_tau32, "1 btag"),

#Correlation of Variables to Mass of Z_Prime
TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_Zprime_M" ,"tau_{32}(t) VS m(Z')",20,0,1,30,0,300),"Tops_ABCD_t32", "Zprimes_ABCD_M",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Zprimes_ABCD_M>0 && Tops_ABCD_t32>0","1 btag"),
TwoDimPlot(ROOT.TH2F("ABCD_W_tau21_vs_Zprime_M" ,"tau_{21}(W) VS m(Z')",20,0,1,30,0,300),"Ws_ABCD_t21", "Zprimes_ABCD_M",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Zprimes_ABCD_M>0 && Ws_ABCD_t21>0","1 btag"),
TwoDimPlot(ROOT.TH2F("ABCD_bottom_csv_v2_vs_Zprime_M" ,"CSV_v2(b) VS m(Z')",20,0,1,30,0,300),"Bottoms_ABCD_CSV", "Zprimes_ABCD_M",plotselection2 + " && " + plotselection_topsubjetCSVv2 +"&&Zprimes_ABCD_M>0 && Tops_ABCD_t32>0","1 btag"),




]





CatAList=["ABCD_notopbtag_CatA_Zprime_M" , "ABCD_notopbtag_CatA_Zprime_M_beta", "ABCD_notopbtag_CatA_Zprime_M_beta_first", "ABCD_notopbtag_CatA_Zprime_M_first"]

plotnames=[]
for i in plots:
    plotnames.append(i.name)


OnlyFirstList=len(plots)*[False]
#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
OnlyFirstList[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first"):plotnames.index('Withtopbtag_W_t21') +1 ] = len(OnlyFirstList[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first"):plotnames.index('Withtopbtag_W_t21') + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'

#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
assert len(OnlyFirstList)==len(plots)
#raw_input()




print name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,4000000,plots,samples)
outputpath=plotParallel(name,2000000,plots,SignalSamples+BackgroundSamples, [''], ['1'] , [''], ['1'],additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+CombinedSamples, [''], ['1'] , [''], ['1'], [],  OnlyFirstList)
#outputpathBackground=plotParallel(name,4000000,plots,BackgroundSamples)
#outputpathData=plotParallel(name,4000000,plots,DataSamples)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)

listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples,plots,1, [""], True )
#listOfHistoListsBackground=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples,plots,1) #needed? Same as  ABCD?
listOfHistoListsABCD=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples ,plots,1,[""], True )
# listOfHistoListsSignalAndBackground=createHistoLists_fromSuperHistoFile(outputpath,CombinedSamples,plots,1, [""], True )

listOfHistoListsSignalAndBackground1500900=CloneListOfHistoLists(listOfHistoListsABCD+listOfHistoListsSignal)
listOfHistoListsSignalAndBackground20001200=CloneListOfHistoLists(listOfHistoListsABCD+listOfHistoListsSignal)
listOfHistoListsSignalAndBackground25001200=CloneListOfHistoLists(listOfHistoListsABCD+listOfHistoListsSignal)


listOfHistoListsSignalAndBackground=[listOfHistoListsSignalAndBackground1500900, listOfHistoListsSignalAndBackground20001200, listOfHistoListsSignalAndBackground25001200]


#for lol in listOfHistoListsSignalAndBackground:
    #print lol[0][0], "Sind die pointer anders fuer die verschiedenen listOfHistoLists?"

labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)



#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('Notopbtag_Top_MSD'):plotnames.index('Withtopbtag_W_t21')+1],BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], 'label','MSDs_QCD',True)
#writeListOfHistoLists([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first')]],BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], 'label','MSDs_QCD ')
print listOfHistoListsABCD
print plotnames
raw_input()


lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD)
listOfHistoListsABCD=lolABCD_rebinned
chekcNbins(listOfHistoListsABCD)


#lolBackgroundT=transposeLOL(listOfHistoListsBackground)
lolABCDT=transposeLOL(listOfHistoListsABCD)
#lolDataT=transposeLOL(listOfHistoListsData)

#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)
#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)


#lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD)

chekcNbins(lolABCD_rebinned)




divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatB_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatC_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatD_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatC_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatE_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatF_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatG_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatH_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatE_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatG_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')


#GetIntegralLOL( transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first"):plotnames.index("ABCD_notopbtag_CatH_Zprime_M_beta_first")+1]) 
##GetIntegralLOL( listOfHistoListsABCD )


#print listOfHistoListsABCD[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first")][BackgroundSampleNames.index('QCD_HT')], '   integral ', listOfHistoListsABCD[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first")][BackgroundSampleNames.index('QCD_HT')].Integral()
#writeListOfHistoLists([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first')]],BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], 'label','fuck',normalize=False,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False,ratio=False,DoProfile=False)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatE_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)



divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatB_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatC_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatD_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatC_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatE_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatF_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatG_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatH_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatE_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatG_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatE_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)


divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatB_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatC_Zprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatD_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatC_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatE_Zprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatF_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatG_Zprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatH_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatE_Zprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatG_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatE_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)






divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatB_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatC_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatD_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatC_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatE_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatF_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatG_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatH_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatE_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatG_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')


ListOfIntegralLists=GetIntegralLOL( transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag2_CatA_Zprime_M_beta_first"):plotnames.index("ABCD_notopbtag2_CatH_Zprime_M_beta_first")+1]) 
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatE_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)



divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatB_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatC_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatD_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatC_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatE_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatF_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatG_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatH_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatE_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatG_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')


ListOfIntegralLists=GetIntegralLOL( transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_withtopbtag2_CatA_Zprime_M_beta_first"):plotnames.index("ABCD_withtopbtag2_CatH_Zprime_M_beta_first")+1]) 
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatA_Zprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatE_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)


divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatA_Zprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatB_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatC_Zprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatD_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatA_Zprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatC_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatE_Zprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatF_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatG_Zprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatH_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatE_Zprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatG_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')


ListOfIntegralLists=GetIntegralLOL( transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD2_inclusive_CatA_Zprime_M_beta_first"):plotnames.index("ABCD2_inclusive_CatH_Zprime_M_beta_first")+1]) 
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatA_Zprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatE_Zprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)


####Tprime

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatB_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatC_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatD_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatC_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatE_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatF_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatG_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatH_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatE_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatG_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')


#GetIntegralLOL( transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag_CatA_Tprime_M_beta_first"):plotnames.index("ABCD_notopbtag_CatH_Tprime_M_beta_first")+1]) 
##GetIntegralLOL( listOfHistoListsABCD )


#print listOfHistoListsABCD[plotnames.index("ABCD_notopbtag_CatA_Tprime_M_beta_first")][BackgroundSampleNames.index('QCD_HT')], '   integral ', listOfHistoListsABCD[plotnames.index("ABCD_notopbtag_CatA_Tprime_M_beta_first")][BackgroundSampleNames.index('QCD_HT')].Integral()
#writeListOfHistoLists([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Tprime_M_beta_first')]],BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], 'label','fuck',normalize=False,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False,ratio=False,DoProfile=False)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag_CatE_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)



divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatB_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatC_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatD_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatC_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatE_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatF_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatG_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatH_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatE_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatG_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag_CatE_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)


divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatB_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatC_Tprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatD_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatC_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatE_Tprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatF_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatG_Tprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatH_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatE_Tprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatG_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_inclusive_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_inclusive_CatE_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_inclusive_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)






divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatB_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatC_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatD_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatC_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatE_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatF_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatG_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatH_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatE_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatG_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')


ListOfIntegralLists=GetIntegralLOL( transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag2_CatA_Tprime_M_beta_first"):plotnames.index("ABCD_notopbtag2_CatH_Tprime_M_beta_first")+1]) 
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag2_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_notopbtag2_CatE_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag2_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_notopbtag2_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)



divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatB_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatC_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatD_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatC_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatE_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatF_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatG_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatH_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatE_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatG_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')


ListOfIntegralLists=GetIntegralLOL( transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_withtopbtag2_CatA_Tprime_M_beta_first"):plotnames.index("ABCD_withtopbtag2_CatH_Tprime_M_beta_first")+1]) 
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag2_CatA_Tprime_M_beta_first"), plotnames.index("ABCD_withtopbtag2_CatE_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag2_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag2_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)


divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatA_Tprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatB_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatC_Tprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatD_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatA_Tprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatC_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')

divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatE_Tprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatF_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatG_Tprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatH_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatE_Tprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatG_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')


ListOfIntegralLists=GetIntegralLOL( transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD2_inclusive_CatA_Tprime_M_beta_first"):plotnames.index("ABCD2_inclusive_CatH_Tprime_M_beta_first")+1]) 
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatE_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioEFoverGH_pol1", rebin=1, fitoption='pol1', labels=None, autoXrange=True)
divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD2_inclusive_CatA_Tprime_M_beta_first"), plotnames.index("ABCD2_inclusive_CatE_Tprime_M_beta_first"), normalizefirst=False,rebin=1,option='')
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol0_corrE", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD2_inclusive_CatA_Tprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD2_"+ABCDeventhandling+"_"+WPs+"_inclusive_ratioABoverCD_pol1_corrE", rebin=1, fitoption='pol1', labels=None, autoXrange=True)








#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_notopbtag_CatB_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')
#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatC_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_notopbtag_CatD_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')
#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_notopbtag_CatC_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')

#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatE_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_notopbtag_CatF_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')
#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatG_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_notopbtag_CatH_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')
#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatE_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_notopbtag_CatG_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')


#GetIntegralLOL( transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first_bottomcontribno"):plotnames.index("ABCD_notopbtag_CatH_Zprime_M_beta_first_bottomcontribno")+1]) 
##GetIntegralLOL( listOfHistoListsABCD )


##print listOfHistoListsABCD[plotnames.index("ABCD_withtopbtagalt_CatA_Zprime_M_beta_first")][BackgroundSampleNames.index('QCD_HT')], '   integral ', listOfHistoListsABCD[plotnames.index("ABCD_withtopbtagalt_CatA_Zprime_M_beta_first")][BackgroundSampleNames.index('QCD_HT')].Integral()
##writeListOfHistoLists([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtagalt_CatA_Zprime_M_beta_first')]],BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], 'label','fuck',normalize=False,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False,ratio=False,DoProfile=False)
#writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first_bottomcontribno')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_bottomcontribno_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
#writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatE_Zprime_M_beta_first_bottomcontribno')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_bottomcontribno_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
##writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtagalt_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtagalt_shaperatioAB_over_shaperatioCD", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
##writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtagalt_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforEFGH_shaperatioEG_over_shaperatioFH", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
##divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_notopbtag_CatE_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')
##writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first_bottomcontribno')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_bottomcontribno_ratioABoverCD_pol0_Ecorr", rebin=1, fitoption='pol0', labels=None, autoXrange=True)




#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_withtopbtag_CatB_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')
#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatC_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_withtopbtag_CatD_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')
#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_withtopbtag_CatC_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')

#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatE_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_withtopbtag_CatF_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')
#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatG_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_withtopbtag_CatH_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')
#divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatE_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_withtopbtag_CatG_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')


#GetIntegralLOL( transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first_bottomcontribno"):plotnames.index("ABCD_withtopbtag_CatH_Zprime_M_beta_first_bottomcontribno")+1]) 
##GetIntegralLOL( listOfHistoListsABCD )


##print listOfHistoListsABCD[plotnames.index("ABCD_withtopbtagalt_CatA_Zprime_M_beta_first")][BackgroundSampleNames.index('QCD_HT')], '   integral ', listOfHistoListsABCD[plotnames.index("ABCD_withtopbtagalt_CatA_Zprime_M_beta_first")][BackgroundSampleNames.index('QCD_HT')].Integral()
##writeListOfHistoLists([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtagalt_CatA_Zprime_M_beta_first')]],BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], 'label','fuck',normalize=False,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False,ratio=False,DoProfile=False)
#writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatA_Zprime_M_beta_first_bottomcontribno')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_bottomcontribno_ratioABoverCD_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
#writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatE_Zprime_M_beta_first_bottomcontribno')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_bottomcontribno_ratioEFoverGH_pol0", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
##writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtagalt_CatA_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtagalt_shaperatioAB_over_shaperatioCD", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
##writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtagalt_CatE_Zprime_M_beta_first')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforEFGH_shaperatioEG_over_shaperatioFH", rebin=1, fitoption='pol0', labels=None, autoXrange=True)
##divideHistos(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]), plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first_bottomcontribno"), plotnames.index("ABCD_withtopbtag_CatE_Zprime_M_beta_first_bottomcontribno"), normalizefirst=False,rebin=1,option='')
##writeHistoListwithXYErrors([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_withtopbtag_CatA_Zprime_M_beta_first_bottomcontribno')]], BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], name="checkforABCD_"+ABCDeventhandling+"_"+WPs+"_withtopbtag_bottomcontribno_ratioEFoverGH_pol0_Ecorr", rebin=1, fitoption='pol0', labels=None, autoXrange=True)





#################################################################################################################
##Here Starts: Plots And Calculating



##Stack Plot, Background and Signal, Z_Prime_M
##writeLOLSeveralOnTop(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1])[:plotnames.index("Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M")+1],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1],transposeLOL(lolSignalT),SignalSamples,-0.2,'Zprime',False ,'histoE','samehistoE')
##print "plot_Zprime_MC_Lena Len(listOfHistoListsABCD):"+str( len(listOfHistoListsABCD) )


#writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_bottom_csv_v2_vs_Zprime_M")+1], BackgroundSamples , plotnames[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_bottom_csv_v2_vs_Zprime_M")+1], 'ABCD_2D_Zprime' , True, False, False, "colz", False, False, False, True)
#writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_withtopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_W_tau21_vs_ZprimeM")+1], BackgroundSamples , plotnames[plotnames.index('ABCD_withtopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_W_tau21_vs_ZprimeM")+1], 'ABCD_2D_Zprime' , True, False, False, "colz", False, False, False, True)

#writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_notopbtag_CatA_Zprime_M" ) : plotnames.index( "ABCD_notopbtag_CatH_Zprime_M_first" ) +1] , "Integrallist_before_multiplication.tex" , SampleNames )
##writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_beta" ) : plotnames.index( "ABCD_notopbtag_CatH_Zprime_M_beta" ) +1] , "Integrallist_before_multiplication_beta.tex" , SampleNames )


##Compare BackgroundAndSignal in SignalSample (mistaged Signal infuences Background prediction )
#compareEntriesInBackgroundAndSignalRegion( transposeLOL(listOfHistoListsSignal), "ComparisonIntegralsinSignalSample.txt" )

## Correlationfactor  (with difference to selection with only first element)
#writeCorrLOL(listOfHistoListsABCD[plotnames.index('ABCD_notopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime45005000")+1]+listOfHistoListsABCD[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_bottom_csv_v2_vs_Zprime_M")+1] , "Correlationfactors_.txt", plotnames[plotnames.index('ABCD_notopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime45005000")+1]+plotnames[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_bottom_csv_v2_vs_Zprime_M")+1], ["tt-bar", "QCD_HT", "QCD_Pt", "QCD_comb"] , True )





##### Correlationfactor  (with difference to selection with only first element)
#writeCorrLOLinTEX( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime45005000")+1], "Correlationfactors.tex", plotnames[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_withtopbtag_top_tau32_vs_Bottom_CSV_v2_Zprime45005000")+1], ["tt-bar", "QCD_HT", "QCD_Pt", "QCD_comb"] , True )



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
