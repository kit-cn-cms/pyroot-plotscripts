#############
# plot general control distributions
##############

from plotconfig_Zprime_MC_Lena import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos

name='Zprime_MC'
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




# book plots
plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
#plotselection="N_packedPatJetsAK8PFCHSSoftDrop>=2&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200&&Evt_HT>850"
plotselection1="Evt_HT>850"
#plotselection1=""
plotselection2="N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 && Evt_HT>850 "



#Own Plotselections for ABCD-method
plotselection_ABCD_general=  plotselection2 + "&& Zprimes_ABCD_M>0   &&    Ws_ABCD_t21 <  0.6    &&    100 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210   "
plotselection_ABCD_general_beta =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    70 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 100     &&    100 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210   "

plotselection_tau32 = " Tops_ABCD_t32 < 0.86   "
plotselection_W_MSD =  " 70 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 100 "
plotselection_B_CSV = "  Bottoms_ABCD_CSV > 0.8   "
plotselection_W_tau21 = " Ws_ABCD_t21 < 0.6 "








plotselection_ABCD_general_0 =  plotselection2 + "&& Zprimes_ABCD_M[0]>0   &&    Ws_ABCD_t21[0] >  0.6    &&    100 < Tops_ABCD_MSD[0]     &&    Tops_ABCD_MSD[0]  < 210   "
plotselection_ABCD_general_beta_0 =   plotselection2 + "&& Zprimes_ABCD_M[0]>0   &&    70 < Ws_ABCD_MSD[0]  &&   Ws_ABCD_MSD[0] < 100     &&    100 < Tops_ABCD_MSD[0]     &&    Tops_ABCD_MSD[0]  < 210   "


plotselection_tau32_0 = " Tops_ABCD_t32[0] < 0.86   "
plotselection_W_MSD_0 =  " 70 < Ws_ABCD_MSD[0]  &&   Ws_ABCD_MSD[0] < 100 "
plotselection_B_CSV_0 = "  Bottoms_ABCD_CSV[0] > 0.8   "
plotselection_W_tau21_0 = " Ws_ABCD_t21[0] < 0.6  "

plotselection_tau32_anti=" Tops_ABCD_t32 > 0.86   "
plotselection_W_MSD_anti =  " 70 > Ws_ABCD_MSD  ||   Ws_ABCD_MSD > 100 "
plotselection_B_CSV_anti = "  Bottoms_ABCD_CSV < 0.8   "
plotselection_W_tau21_anti = " Ws_ABCD_t21 > 0.6 "


plotselection_tau32_anti_0 =" Tops_ABCD_t32[0] > 0.86   "
plotselection_W_MSD_anti_0 =  " 70 > Ws_ABCD_MSD[0]  ||   Ws_ABCD_MSD[0] > 100 "
plotselection_B_CSV_anti_0 = "  Bottoms_ABCD_CSV[0] < 0.8   "
plotselection_W_tau21_anti_0 = " Ws_ABCD_t21[0]  > 0.6 "




plotselection_W_MSD_one_sided =  " 70 < Ws_ABCD_MSD && Ws_ABCD_MSD < 100"
plotselection_W_MSD_one_sided_anti =  " 70 > Ws_ABCD_MSD && Ws_ABCD_MSD < 100"




plotselection_sideband = "Signal_Topfirst_Zprime_M < 0"




#Create Plots

plots=[


    #Signalregion
    Plot(ROOT.TH1F("Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
    #One Anti
    Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-btag",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0","1 anti-btag"),
    Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-Wtag",50,0,5000),"Sideband_W_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 anti-Wtag"),
    Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 anti-ttag"),

    #Two Anti
    Plot(ROOT.TH1F("Sideband_top_anti_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag + anti-btag",50,0,5000),"Sideband_top_anti_bottom_anti_Topfirst_Zprime_M",plotselection2		+"&&Sideband_top_anti_bottom_anti_Topfirst_Zprime_M>0","1 anti-ttag + 1 anti-btag"),
    Plot(ROOT.TH1F("Sideband_W_anti_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-Wtag + anti-btag",50,0,5000),"Sideband_W_anti_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_W_anti_bottom_anti_Topfirst_Zprime_M>0","1 anti-Wtag + 1 anti-btag"),
    Plot(ROOT.TH1F("Sideband_top_anti_W_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag + anti-Wtag",50,0,5000),"Sideband_top_anti_W_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_W_anti_Topfirst_Zprime_M>0","1 anti-ttag + 1 anti-Wtag"),

    #Three Anti
    Plot(ROOT.TH1F("Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag + anti-Wtag + anti-ttag",50,0,5000),"Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M>0","1 anti-ttag + 1 anti-Wtag + 1 anti-ttag"),





    #All elements
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_top_MSD" ,"tau_{32}(t) VS m_{SD}(t)",20,0,1,30,0,300),"Tops_ABCD_MSD","Tops_ABCD_t32",plotselection2+"&&Tops_ABCD_MSD>0 && Tops_ABCD_t32>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_W_tau21" ,"tau_{32}(t) VS tau_{21}(W)",20,0,1,20,0,1),"Tops_ABCD_t32","Ws_ABCD_t21",plotselection2+"&&Tops_ABCD_t32>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_W_MSD" ,"tau_{32}(t) VS m_{SD}(W)",20,0,1,30,0,300),"Tops_ABCD_t32","Ws_ABCD_MSD",plotselection2+"&&Tops_ABCD_t32>0 && Ws_ABCD_MSD>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2+"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_W_tau21" ,"m_{SD}(t) VS tau_{21}(W)",30,0,300,20,0,1),"Tops_ABCD_MSD","Ws_ABCD_t21",plotselection2+"&&Tops_ABCD_MSD>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_W_MSD" ,"m_{SD}(t) VS m_{SD}(t)(W)",30,0,300,30,0,300),"Tops_ABCD_MSD","Ws_ABCD_MSD",plotselection2+"&&Tops_ABCD_MSD>0 && Ws_ABCD_MSD>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(t) VS CSV_v2(b)",30,0,300,20,0,1),"Tops_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2+"&&Tops_ABCD_MSD>0 && Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_W_MSD_vs_W_tau21" ,"m_{SD}(W) VS tau_{21}(W)",30,0,300,20,0,1),"Ws_ABCD_MSD","Ws_ABCD_t21",plotselection2+"&&Ws_ABCD_MSD>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_W_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",30,0,300,20,0,1),"Ws_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2+"&&Ws_ABCD_MSD>0 &&Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_W_tau21_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",30,0,300,20,0,1),"Ws_ABCD_t21","Bottoms_ABCD_CSV",plotselection2+"&&Ws_ABCD_t21>0 &&Bottoms_ABCD_CSV>0","1 btag"),





    # Plots for ZPrime_M - with right plotselection - All Elements
    # W_ MSD is used as thrid variable


    Plot(ROOT.TH1F("ABCD_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD , "1 btag"),
    Plot(ROOT.TH1F("ABCD_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD + "&&" +plotselection_sideband ,"1 btag"),


    Plot(ROOT.TH1F("ABCD_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti + "&&" +plotselection_sideband ,"1 btag"),




    # Plots for W tau21 as third variable ---- beta



    # Plots for ZPrime_M - with right plotselection - All Elements
    Plot(ROOT.TH1F("ABCD_CatA_Zprime_M_beta" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD_CatB_Zprime_M_beta" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatC_Zprime_M_beta" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatD_Zprime_M_beta" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),


    Plot(ROOT.TH1F("ABCD_CatE_Zprime_M_beta" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatF_Zprime_M_beta" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatG_Zprime_M_beta" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatH_Zprime_M_beta" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),



    # #Test if one-sided cut on W_MSD changes Normalization

    # Plot(ROOT.TH1F("ABCD_CatA_Zprime_M_one_sided" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_one_sided, "1 btag"),
    # Plot(ROOT.TH1F("ABCD_CatB_Zprime_M_one_sided" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_one_sided  ,"1 btag"),
    # Plot(ROOT.TH1F("ABCD_CatC_Zprime_M_one_sided" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_one_sided  ,"1 btag"),
    # Plot(ROOT.TH1F("ABCD_CatD_Zprime_M_one_sided" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_one_sided  ,"1 btag"),


    # Plot(ROOT.TH1F("ABCD_CatE_Zprime_M_one_sided" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_one_sided_anti  ,"1 btag"),
    # Plot(ROOT.TH1F("ABCD_CatF_Zprime_M_one_sided" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_one_sided_anti  ,"1 btag"),
    # Plot(ROOT.TH1F("ABCD_CatG_Zprime_M_one_sided" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_one_sided_anti  ,"1 btag"),
    # Plot(ROOT.TH1F("ABCD_CatH_Zprime_M_one_sided" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_one_sided_anti  ,"1 btag"),




    #doing only first element
    #beta (tau21)

    Plot(ROOT.TH1F("ABCD_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),


    Plot(ROOT.TH1F("ABCD_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag") ,


    #only first element
    #W_msd as third variable

    Plot(ROOT.TH1F("ABCD_CatA_Zprime_M_first" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD_CatB_Zprime_M_first" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatC_Zprime_M_first" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  + "&&" +plotselection_sideband,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatD_Zprime_M_first" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),


    Plot(ROOT.TH1F("ABCD_CatE_Zprime_M_first" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatF_Zprime_M_first" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatG_Zprime_M_first" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatH_Zprime_M_first" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag")



]

CatAList=["ABCD_CatA_Zprime_M" , "ABCD_CatA_Zprime_M_beta", "ABCD_CatA_Zprime_M_beta_first", "ABCD_CatA_Zprime_M_first"]

plotnames=[]
for i in plots:
    plotnames.append(i.name)


OnlyFirstList=len(plots)*[False]
OnlyFirstList[plotnames.index("ABCD_CatA_Zprime_M_beta_first"):plotnames.index('ABCD_CatH_Zprime_M_first') +1 ] = len(OnlyFirstList[plotnames.index("ABCD_CatA_Zprime_M_beta_first"):plotnames.index('ABCD_CatH_Zprime_M_first') + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'





print name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,4000000,plots,samples)
outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+CombinedSamples, [''], ['1'] , [''], ['1'], [],  OnlyFirstList)
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


#lolBackgroundT=transposeLOL(listOfHistoListsBackground)
lolABCDT=transposeLOL(listOfHistoListsABCD)
#lolDataT=transposeLOL(listOfHistoListsData)






################################################################################################################
#Here Starts: Plots And Calculating



#Stack Plot, Background and Signal, Z_Prime_M
#writeLOLSeveralOnTop(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1])[:plotnames.index("Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M")+1],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1],transposeLOL(lolSignalT),SignalSamples,-0.2,'Zprime',False ,'histoE','samehistoE')
#print "plot_Zprime_MC_Lena Len(listOfHistoListsABCD):"+str( len(listOfHistoListsABCD) )



writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_CatA_Zprime_M" ) : plotnames.index( "ABCD_CatH_Zprime_M_first" ) +1] , "Integrallist_before_multiplication.tex" , SampleNames )
#writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_CatA_Zprime_M_beta" ) : plotnames.index( "ABCD_CatH_Zprime_M_beta" ) +1] , "Integrallist_before_multiplication_beta.tex" , SampleNames )


#Compare BackgroundAndSignal in SignalSample (mistaged Signal infuences Background prediction )
compareEntriesInBackgroundAndSignalRegion( transposeLOL(listOfHistoListsSignal), "ComparisonIntegralsinSignalSample.txt" )

# ## TwoDimPlots (with difference to selection with only first element)
writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index("ABCD_W_tau21_vs_Bottom_CSV_v2")+1] + listOfHistoListsABCD[-1], BackgroundSamples , plotnames[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index("ABCD_W_tau21_vs_Bottom_CSV_v2")+1], 'ABCD_2D' , True, False, False, "colz", False, False, False, True)





## Correlationfactor  (with difference to selection with only first element)
writeCorrLOLinTEX( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index("ABCD_W_tau21_vs_Bottom_CSV_v2")+1], "Correlationfactors.tex", plotnames[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index("ABCD_W_tau21_vs_Bottom_CSV_v2")+1], ["tt-bar", "QCD_HT", "QCD_Pt", "QCD_comb"] , True )











# # ABCD-Zprime_M Plots Work?
# writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_CatA_Zprime_M'):plotnames.index('ABCD_CatH_Zprime_M_first_beta')+1], BackgroundSamples , plotnames[plotnames.index('ABCD_CatA_Zprime_M'):plotnames.index('ABCD_CatH_Zprime_M_first_beta')+1], 'ABCD_ZPrime_M' , True, False, False, "histoE", False, False, False, True)


#
#
#
#
## Multiply and Divide for ABCD Methode - short verion with funktion ReconstructWithABCD()
for plotname in CatAList:
    ReconstructWithABCD(listOfHistoListsABCD, plotname, plotnames)
    ReconstructWithABCD(listOfHistoListsSignal, plotname, plotnames)

#
#
#
#
#Add Signal and Backgroundhistos
XC_Factor=1
weights= [ XC_Factor/138.07, XC_Factor/86.28, XC_Factor/37.6 ]
for plotnameindex in range(plotnames.index("ABCD_CatA_Zprime_M"), plotnames.index("ABCD_CatH_Zprime_M_first") ):
    for index, listOfHistoList, weight in zip(range(3),listOfHistoListsSignalAndBackground, weights):
        addHistos(listOfHistoList, plotnameindex, plotnameindex + len(plotnames), weight , True, index)

#Multiply and Divide for ABCD
for listOfHistoList in listOfHistoListsSignalAndBackground:
    for plotname in CatAList:
        ReconstructWithABCD(listOfHistoList, plotname, plotnames)

#
#
#
#
#
#
#
##Write ListOfIntegralLists
writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_CatA_Zprime_M" ) : plotnames.index( "ABCD_CatH_Zprime_M_first" ) +1] , "Integrallist_after_multiplication.tex" , SampleNames )
# writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_CatA_Zprime_M_beta" ) : plotnames.index( "ABCD_CatH_Zprime_M_beta" ) +1] , "Integrallist_after_multiplication_beta.tex" , SampleNames )
#
#
#
#
#

#Create and Write List Of RatioPlots
#Workaround to use writeListOfHistoLists with a Transposed ListOfHistoList (uses trnasposeLOLextendet in plotutils.py)

WASamples = 50*[ BackgroundSamples[0], BackgroundSamples[1] ]
WAPlotNames =  [   "ABCD_CatA_Zprime_M"   ,
                 "ABCD_CatE_Zprime_M"  ,
                 "ABCD_CatA_Zprime_M_beta" ,
                 "ABCD_CatE_Zprime_M_beta" ,
                 # "ABCD_CatA_Zprime_M_one_sided" ,
                 # "ABCD_CatE_Zprime_M_one_sided",
                 "ABCD_CatA_Zprime_M_beta_first",
                 "ABCD_CatE_Zprime_M_beta_first",
                 "ABCD_CatA_Zprime_M_first",
                 "ABCD_CatE_Zprime_M_first" ]

IndexListToTranspose = [ [plotnames.index( "ABCD_CatA_Zprime_M" ) , plotnames.index( "ABCD_CatB_Zprime_M" ) ] ,
    [ plotnames.index( "ABCD_CatE_Zprime_M" ), plotnames.index( "ABCD_CatF_Zprime_M" ) ],
    [plotnames.index( "ABCD_CatA_Zprime_M_beta" ), plotnames.index( "ABCD_CatB_Zprime_M_beta" ) ] ,
    [plotnames.index( "ABCD_CatE_Zprime_M_beta" ), plotnames.index( "ABCD_CatF_Zprime_M_beta" ) ] ,
    # [plotnames.index( "ABCD_CatA_Zprime_M_one_sided" ), plotnames.index( "ABCD_CatB_Zprime_M_one_sided" ) ],
    # [plotnames.index( "ABCD_CatE_Zprime_M_one_sided" ), plotnames.index( "ABCD_CatF_Zprime_M_one_sided" ) ],
    [plotnames.index( "ABCD_CatA_Zprime_M_beta_first") , plotnames.index("ABCD_CatB_Zprime_M_beta_first") ] ,
    [plotnames.index( "ABCD_CatE_Zprime_M_beta_first") , plotnames.index( "ABCD_CatF_Zprime_M_beta_first")],
    [plotnames.index( "ABCD_CatA_Zprime_M_first") , plotnames.index("ABCD_CatB_Zprime_M_first") ] ,
    [plotnames.index( "ABCD_CatE_Zprime_M_first") , plotnames.index( "ABCD_CatF_Zprime_M_first")]]





## For BackgroundSamples
WASLnames2 =[]
for string in WAPlotNames:
    for sample in SampleNames:
        WASLnames2.append( string + "_" + sample )

RatioPlotList = transposeLOLextended( listOfHistoListsABCD,  IndexListToTranspose)
writeListOfHistoLists( RatioPlotList , WASamples ,  WASLnames2 , 'RatioPlotList' , False , False, False, "histoE", False, False, True, False)



###Print all Plots for Z_Prime (Signal)
#WASignalSamplePlotNames2=[]
#for string in WAPlotNames:
    #for sample in SignalSampleNames:
        #WASignalSamplePlotNames2.append( string + "_" + sample)

#RatioPlotListSignal = transposeLOLextended( listOfHistoListsSignal, IndexListToTranspose )
#writeListOfHistoLists( RatioPlotListSignal , WASamples , WASignalSamplePlotNames2 , 'RatioPlotListSignal' , False , False, False, "histoE", False, False, True, False)




#RatioPlots for Combined Background and Signal Sample
WASignalSamplePlotNameListOfLists=[]
for SignalSampleName in SignalSampleNames:
    ListToAppend=[]
    for PlotName in WAPlotNames:
        for SampleName in SampleNames:
            ListToAppend.append(SignalSampleName+SampleName+PlotName)
    WASignalSamplePlotNameListOfLists.append(ListToAppend)

for WASignalSamplePlotNameList, SignalSampleName, listOfHistoListSignalAndBackground in zip(WASignalSamplePlotNameListOfLists, SignalSampleNames, listOfHistoListsSignalAndBackground):
    RatioPlotListComb = transposeLOLextended( listOfHistoListSignalAndBackground, IndexListToTranspose )
    writeListOfHistoLists( RatioPlotListComb , WASamples , WASignalSamplePlotNameList , 'RatioPlotListComb'+SignalSampleName , False , False, False, "histoE", False, False, True, False)




### RatioPlots and Error Fit Polinomial , A/B - Signal over Background
#for WASignalSamplePlotNameList, SignalSampleName, listOfHistoListSignalAndBackground in zip(WASignalSamplePlotNameListOfLists, SignalSampleNames, listOfHistoListsSignalAndBackground):
    #RatioPlotListComb = transposeLOLextended( listOfHistoListSignalAndBackground, IndexListToTranspose )
    #ListOfPureRatioPlots = []
    #for HistoList in RatioPlotListComb:
        #HistoList[0].Divide(HistoList[1])
        #ListOfPureRatioPlots.append( [HistoList[0] ]  )
    ## writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol2_"+SignalSampleName, 1, "pol2", WASignalSamplePlotNameList, True)
    #writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol1_"+SignalSampleName, 1, "pol1", WASignalSamplePlotNameList, True)
    ## writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol0_"+SignalSampleName, 1, "pol0", WASignalSamplePlotNameList, True)


## Ratio Plot with Errors, A/B - Signal over Background, without Signalcontamination
ListOfPureRatioPlots=[]
for histoList in RatioPlotList:
    histoList[0].Divide(histoList[1])
    ListOfPureRatioPlots.append( [histoList[0] ])
writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol1_Background", 1, "pol1", WASLnames2, True)
# writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol2_Background", 1, "pol2", WASLnames2, True)
# writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol0_Background", 1, "pol0", WASLnames2, True)




## Uncomple STACK PLOT


###Modify Signal And Background listOfHistoList (substract from backgroundprediction)
#for index in range( plotnames.index("ABCD_CatA_Zprime_M"),plotnames.index("ABCD_CatH_Zprime_M_first") +1):
    #if plotnames[index][8] =="B":
        #listOfHistoListsSignalAndBackground25001200[index][1].Add(listOfHistoListsABCD[index][1], -1)
        ##listOfHistoListsSignalAndBackground25001200[index][1].Multiply(-1)

        #listOfHistoListsSignalAndBackground25001200[index-1][1].Add(listOfHistoListsABCD[index-1][0])#Add to Signal and QCD-Background in Signal ttbar in Signal Region

###Create a hISTOlIST TO DO stackPlotABCD
#ListOfHistoListsFinalStackPlot = []
#titlelist = []
#for index in range( plotnames.index("ABCD_CatA_Zprime_M"), plotnames.index("ABCD_CatH_Zprime_M_first") +1):
    #if plotnames[index][8] =="A":
        #ListToAppend = []
        #titlelist.append( listOfHistoListsABCD[index][0].GetName()[5:] )
        #ListToAppend.append(listOfHistoListsSignalAndBackground25001200[index+1][0]) #Signal
        #ListToAppend.append(listOfHistoListsSignalAndBackground25001200[index+1][1]) #Signalkontamination
        #ListToAppend.append(listOfHistoListsABCD[index+1][1]) #QCD_HAT in CatB
        #ListToAppend.append(listOfHistoListsABCD[index][0]) #ttbar in Signal Region
        #ListOfHistoListsFinalStackPlot.append(ListToAppend)

#colorlist =[ ROOT.kBlack , ROOT.kRed, ROOT.kYellow,ROOT.kBlue]
#stacklist = [False, True, True, True]
#optionlist = ["E", "histoE", "histoE", "histoE"]
#stackPlotABCD(ListOfHistoListsFinalStackPlot, "StackPlotsABCD", colorlist=colorlist, labellist=["ttbar", "QCD-Backgroundestimation", "Signalcontamination", "Signal"], titlelist = titlelist, stacklist = stacklist, optionlist = optionlist)

#print "Plotnames contains:"
#for i in plotnames:
    #print i
    
    
    
    


#Anmerkungen fuer Simon:
#Das Skript erzeugt die folgenden Dateien:
#
#Integrallist_before_multiplication.tex
#2D Histogramme in Ordner "ABCD_2D"
#Correlationfactors.tex
#Integrallist_after_multiplication.tex
#Rekonstruktion von Kategoie A und E in "RatioPlotList"
#Signalkontamination in "RatioPlotListComb"+SignalSampleName
#Fehlerbaender in "RatioPlotFit_pol1_Background"