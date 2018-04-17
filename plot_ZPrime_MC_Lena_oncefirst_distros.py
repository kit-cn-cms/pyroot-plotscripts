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

name='Zprime_MC_ABCD'+radi+'_'+ABCDeventhandling+'_'+WPs+'_distros'
#SampleNames=['ttbar' , 'QCD_HT', 'QCD_Pt' ]
#SignalSampleNames=['Zprime1500900',  'Zprime20001200',  'Zprime25001200']




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



#ABCD3 bottomCSV W_MSD
    #no topbtag
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatA_WMSD_beta_first" ,"m(Z') in GeV, CatA " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatB_WMSD_beta_first" ,"m(Z') in GeV, CatB " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatC_WMSD_beta_first" ,"m(Z') in GeV, CatC " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatD_WMSD_beta_first" ,"m(Z') in GeV, CatD " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD3_notopbtag_CatE_WMSD_beta_first" ,"m(Z') in GeV, CatE " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatF_WMSD_beta_first" ,"m(Z') in GeV, CatF " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatG_WMSD_beta_first" ,"m(Z') in GeV, CatG " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatH_WMSD_beta_first" ,"m(Z') in GeV, CatH " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatA_WMSD_beta_first" ,"m(Z') in GeV, CatA " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatB_WMSD_beta_first" ,"m(Z') in GeV, CatB " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatC_WMSD_beta_first" ,"m(Z') in GeV, CatC " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatD_WMSD_beta_first" ,"m(Z') in GeV, CatD " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatE_WMSD_beta_first" ,"m(Z') in GeV, CatE " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatF_WMSD_beta_first" ,"m(Z') in GeV, CatF " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatG_WMSD_beta_first" ,"m(Z') in GeV, CatG " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatH_WMSD_beta_first" ,"m(Z') in GeV, CatH " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD3_CatID==ABCD3_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    #inclusive
    Plot(ROOT.TH1F("ABCD3_inclusive_CatA_WMSD_beta_first" ,"m(Z') in GeV, CatA " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD3_CatID==ABCD3_CatA_withtopbtag) || ABCD3_CatID==ABCD3_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatB_WMSD_beta_first" ,"m(Z') in GeV, CatB " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD3_CatID==ABCD3_CatB_withtopbtag) || ABCD3_CatID==ABCD3_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatC_WMSD_beta_first" ,"m(Z') in GeV, CatC " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD3_CatID==ABCD3_CatC_withtopbtag) || ABCD3_CatID==ABCD3_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatD_WMSD_beta_first" ,"m(Z') in GeV, CatD " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD3_CatID==ABCD3_CatD_withtopbtag) || ABCD3_CatID==ABCD3_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD3_inclusive_CatE_WMSD_beta_first" ,"m(Z') in GeV, CatE " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD3_CatID==ABCD3_CatE_withtopbtag) || ABCD3_CatID==ABCD3_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatF_WMSD_beta_first" ,"m(Z') in GeV, CatF " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD3_CatID==ABCD3_CatF_withtopbtag) || ABCD3_CatID==ABCD3_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatG_WMSD_beta_first" ,"m(Z') in GeV, CatG " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD3_CatID==ABCD3_CatG_withtopbtag) || ABCD3_CatID==ABCD3_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatH_WMSD_beta_first" ,"m(Z') in GeV, CatH " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD3_CatID==ABCD3_CatH_withtopbtag) || ABCD3_CatID==ABCD3_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,


#ABCD5 W tau21 bottomCSV
    #no topbtag
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatA_WMSD_beta_first" ,"m(Z') in GeV, CatA " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatB_WMSD_beta_first" ,"m(Z') in GeV, CatB " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatC_WMSD_beta_first" ,"m(Z') in GeV, CatC " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatD_WMSD_beta_first" ,"m(Z') in GeV, CatD " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD5_notopbtag_CatE_WMSD_beta_first" ,"m(Z') in GeV, CatE " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatF_WMSD_beta_first" ,"m(Z') in GeV, CatF " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatG_WMSD_beta_first" ,"m(Z') in GeV, CatG " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatH_WMSD_beta_first" ,"m(Z') in GeV, CatH " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatA_WMSD_beta_first" ,"m(Z') in GeV, CatA " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatB_WMSD_beta_first" ,"m(Z') in GeV, CatB " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatC_WMSD_beta_first" ,"m(Z') in GeV, CatC " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatD_WMSD_beta_first" ,"m(Z') in GeV, CatD " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatE_WMSD_beta_first" ,"m(Z') in GeV, CatE " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatF_WMSD_beta_first" ,"m(Z') in GeV, CatF " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatG_WMSD_beta_first" ,"m(Z') in GeV, CatG " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatH_WMSD_beta_first" ,"m(Z') in GeV, CatH " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "ABCD5_CatID==ABCD5_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    #inclusive
    Plot(ROOT.TH1F("ABCD5_inclusive_CatA_WMSD_beta_first" ,"m(Z') in GeV, CatA " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD5_CatID==ABCD5_CatA_withtopbtag) || ABCD5_CatID==ABCD5_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatB_WMSD_beta_first" ,"m(Z') in GeV, CatB " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD5_CatID==ABCD5_CatB_withtopbtag) || ABCD5_CatID==ABCD5_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatC_WMSD_beta_first" ,"m(Z') in GeV, CatC " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD5_CatID==ABCD5_CatC_withtopbtag) || ABCD5_CatID==ABCD5_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatD_WMSD_beta_first" ,"m(Z') in GeV, CatD " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD5_CatID==ABCD5_CatD_withtopbtag) || ABCD5_CatID==ABCD5_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD5_inclusive_CatE_WMSD_beta_first" ,"m(Z') in GeV, CatE " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD5_CatID==ABCD5_CatE_withtopbtag) || ABCD5_CatID==ABCD5_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatF_WMSD_beta_first" ,"m(Z') in GeV, CatF " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD5_CatID==ABCD5_CatF_withtopbtag) || ABCD5_CatID==ABCD5_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatG_WMSD_beta_first" ,"m(Z') in GeV, CatG " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD5_CatID==ABCD5_CatG_withtopbtag) || ABCD5_CatID==ABCD5_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatH_WMSD_beta_first" ,"m(Z') in GeV, CatH " ,40,0,200),"Ws_ABCD"+radi+"_MSD", "((ABCD5_CatID==ABCD5_CatH_withtopbtag) || ABCD5_CatID==ABCD5_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,


#ABCD3 bottomCSV W_MSD
    #no topbtag
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatA_Wtau21_beta_first" ,"m(Z') in GeV, CatA " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatB_Wtau21_beta_first" ,"m(Z') in GeV, CatB " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatC_Wtau21_beta_first" ,"m(Z') in GeV, CatC " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatD_Wtau21_beta_first" ,"m(Z') in GeV, CatD " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD3_notopbtag_CatE_Wtau21_beta_first" ,"m(Z') in GeV, CatE " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatF_Wtau21_beta_first" ,"m(Z') in GeV, CatF " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatG_Wtau21_beta_first" ,"m(Z') in GeV, CatG " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatH_Wtau21_beta_first" ,"m(Z') in GeV, CatH " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatA_Wtau21_beta_first" ,"m(Z') in GeV, CatA " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatB_Wtau21_beta_first" ,"m(Z') in GeV, CatB " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatC_Wtau21_beta_first" ,"m(Z') in GeV, CatC " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatD_Wtau21_beta_first" ,"m(Z') in GeV, CatD " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatE_Wtau21_beta_first" ,"m(Z') in GeV, CatE " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatF_Wtau21_beta_first" ,"m(Z') in GeV, CatF " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatG_Wtau21_beta_first" ,"m(Z') in GeV, CatG " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatH_Wtau21_beta_first" ,"m(Z') in GeV, CatH " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD3_CatID==ABCD3_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    #inclusive
    Plot(ROOT.TH1F("ABCD3_inclusive_CatA_Wtau21_beta_first" ,"m(Z') in GeV, CatA " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD3_CatID==ABCD3_CatA_withtopbtag) || ABCD3_CatID==ABCD3_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatB_Wtau21_beta_first" ,"m(Z') in GeV, CatB " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD3_CatID==ABCD3_CatB_withtopbtag) || ABCD3_CatID==ABCD3_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatC_Wtau21_beta_first" ,"m(Z') in GeV, CatC " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD3_CatID==ABCD3_CatC_withtopbtag) || ABCD3_CatID==ABCD3_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatD_Wtau21_beta_first" ,"m(Z') in GeV, CatD " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD3_CatID==ABCD3_CatD_withtopbtag) || ABCD3_CatID==ABCD3_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD3_inclusive_CatE_Wtau21_beta_first" ,"m(Z') in GeV, CatE " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD3_CatID==ABCD3_CatE_withtopbtag) || ABCD3_CatID==ABCD3_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatF_Wtau21_beta_first" ,"m(Z') in GeV, CatF " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD3_CatID==ABCD3_CatF_withtopbtag) || ABCD3_CatID==ABCD3_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatG_Wtau21_beta_first" ,"m(Z') in GeV, CatG " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD3_CatID==ABCD3_CatG_withtopbtag) || ABCD3_CatID==ABCD3_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatH_Wtau21_beta_first" ,"m(Z') in GeV, CatH " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD3_CatID==ABCD3_CatH_withtopbtag) || ABCD3_CatID==ABCD3_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,



#ABCD5 W tau21 bottomCSV
    #no topbtag
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatA_Wtau21_beta_first" ,"m(Z') in GeV, CatA " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatB_Wtau21_beta_first" ,"m(Z') in GeV, CatB " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatC_Wtau21_beta_first" ,"m(Z') in GeV, CatC " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatD_Wtau21_beta_first" ,"m(Z') in GeV, CatD " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD5_notopbtag_CatE_Wtau21_beta_first" ,"m(Z') in GeV, CatE " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatF_Wtau21_beta_first" ,"m(Z') in GeV, CatF " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatG_Wtau21_beta_first" ,"m(Z') in GeV, CatG " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatH_Wtau21_beta_first" ,"m(Z') in GeV, CatH " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatA_Wtau21_beta_first" ,"m(Z') in GeV, CatA " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatB_Wtau21_beta_first" ,"m(Z') in GeV, CatB " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatC_Wtau21_beta_first" ,"m(Z') in GeV, CatC " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatD_Wtau21_beta_first" ,"m(Z') in GeV, CatD " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatE_Wtau21_beta_first" ,"m(Z') in GeV, CatE " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatF_Wtau21_beta_first" ,"m(Z') in GeV, CatF " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatG_Wtau21_beta_first" ,"m(Z') in GeV, CatG " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatH_Wtau21_beta_first" ,"m(Z') in GeV, CatH " ,20,0,1),"Ws_ABCD"+radi+"_t21", "ABCD5_CatID==ABCD5_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    #inclusive
    Plot(ROOT.TH1F("ABCD5_inclusive_CatA_Wtau21_beta_first" ,"m(Z') in GeV, CatA " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD5_CatID==ABCD5_CatA_withtopbtag) || ABCD5_CatID==ABCD5_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatB_Wtau21_beta_first" ,"m(Z') in GeV, CatB " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD5_CatID==ABCD5_CatB_withtopbtag) || ABCD5_CatID==ABCD5_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatC_Wtau21_beta_first" ,"m(Z') in GeV, CatC " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD5_CatID==ABCD5_CatC_withtopbtag) || ABCD5_CatID==ABCD5_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatD_Wtau21_beta_first" ,"m(Z') in GeV, CatD " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD5_CatID==ABCD5_CatD_withtopbtag) || ABCD5_CatID==ABCD5_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD5_inclusive_CatE_Wtau21_beta_first" ,"m(Z') in GeV, CatE " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD5_CatID==ABCD5_CatE_withtopbtag) || ABCD5_CatID==ABCD5_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatF_Wtau21_beta_first" ,"m(Z') in GeV, CatF " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD5_CatID==ABCD5_CatF_withtopbtag) || ABCD5_CatID==ABCD5_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatG_Wtau21_beta_first" ,"m(Z') in GeV, CatG " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD5_CatID==ABCD5_CatG_withtopbtag) || ABCD5_CatID==ABCD5_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatH_Wtau21_beta_first" ,"m(Z') in GeV, CatH " ,20,0,1),"Ws_ABCD"+radi+"_t21", "((ABCD5_CatID==ABCD5_CatH_withtopbtag) || ABCD5_CatID==ABCD5_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,



#ABCD3 bottomCSV W_MSD
    #no topbtag
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatA_EvtHT_beta_first" ,"m(Z') in GeV, CatA " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatB_EvtHT_beta_first" ,"m(Z') in GeV, CatB " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatC_EvtHT_beta_first" ,"m(Z') in GeV, CatC " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatD_EvtHT_beta_first" ,"m(Z') in GeV, CatD " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD3_notopbtag_CatE_EvtHT_beta_first" ,"m(Z') in GeV, CatE " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatF_EvtHT_beta_first" ,"m(Z') in GeV, CatF " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatG_EvtHT_beta_first" ,"m(Z') in GeV, CatG " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatH_EvtHT_beta_first" ,"m(Z') in GeV, CatH " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatA_EvtHT_beta_first" ,"m(Z') in GeV, CatA " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatB_EvtHT_beta_first" ,"m(Z') in GeV, CatB " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatC_EvtHT_beta_first" ,"m(Z') in GeV, CatC " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatD_EvtHT_beta_first" ,"m(Z') in GeV, CatD " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatE_EvtHT_beta_first" ,"m(Z') in GeV, CatE " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatF_EvtHT_beta_first" ,"m(Z') in GeV, CatF " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatG_EvtHT_beta_first" ,"m(Z') in GeV, CatG " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatH_EvtHT_beta_first" ,"m(Z') in GeV, CatH " ,40,1000,3000),"Evt_HT", "ABCD3_CatID==ABCD3_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    #inclusive
    Plot(ROOT.TH1F("ABCD3_inclusive_CatA_EvtHT_beta_first" ,"m(Z') in GeV, CatA " ,40,1000,3000),"Evt_HT", "((ABCD3_CatID==ABCD3_CatA_withtopbtag) || ABCD3_CatID==ABCD3_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatB_EvtHT_beta_first" ,"m(Z') in GeV, CatB " ,40,1000,3000),"Evt_HT", "((ABCD3_CatID==ABCD3_CatB_withtopbtag) || ABCD3_CatID==ABCD3_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatC_EvtHT_beta_first" ,"m(Z') in GeV, CatC " ,40,1000,3000),"Evt_HT", "((ABCD3_CatID==ABCD3_CatC_withtopbtag) || ABCD3_CatID==ABCD3_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatD_EvtHT_beta_first" ,"m(Z') in GeV, CatD " ,40,1000,3000),"Evt_HT", "((ABCD3_CatID==ABCD3_CatD_withtopbtag) || ABCD3_CatID==ABCD3_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD3_inclusive_CatE_EvtHT_beta_first" ,"m(Z') in GeV, CatE " ,40,1000,3000),"Evt_HT", "((ABCD3_CatID==ABCD3_CatE_withtopbtag) || ABCD3_CatID==ABCD3_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatF_EvtHT_beta_first" ,"m(Z') in GeV, CatF " ,40,1000,3000),"Evt_HT", "((ABCD3_CatID==ABCD3_CatF_withtopbtag) || ABCD3_CatID==ABCD3_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatG_EvtHT_beta_first" ,"m(Z') in GeV, CatG " ,40,1000,3000),"Evt_HT", "((ABCD3_CatID==ABCD3_CatG_withtopbtag) || ABCD3_CatID==ABCD3_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_inclusive_CatH_EvtHT_beta_first" ,"m(Z') in GeV, CatH " ,40,1000,3000),"Evt_HT", "((ABCD3_CatID==ABCD3_CatH_withtopbtag) || ABCD3_CatID==ABCD3_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,


#ABCD5 W tau21 bottomCSV
    #no topbtag
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatA_EvtHT_beta_first" ,"m(Z') in GeV, CatA " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatB_EvtHT_beta_first" ,"m(Z') in GeV, CatB " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatC_EvtHT_beta_first" ,"m(Z') in GeV, CatC " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatD_EvtHT_beta_first" ,"m(Z') in GeV, CatD " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD5_notopbtag_CatE_EvtHT_beta_first" ,"m(Z') in GeV, CatE " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatF_EvtHT_beta_first" ,"m(Z') in GeV, CatF " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatG_EvtHT_beta_first" ,"m(Z') in GeV, CatG " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatH_EvtHT_beta_first" ,"m(Z') in GeV, CatH " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatA_EvtHT_beta_first" ,"m(Z') in GeV, CatA " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatB_EvtHT_beta_first" ,"m(Z') in GeV, CatB " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatC_EvtHT_beta_first" ,"m(Z') in GeV, CatC " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatD_EvtHT_beta_first" ,"m(Z') in GeV, CatD " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatE_EvtHT_beta_first" ,"m(Z') in GeV, CatE " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatF_EvtHT_beta_first" ,"m(Z') in GeV, CatF " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatG_EvtHT_beta_first" ,"m(Z') in GeV, CatG " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatH_EvtHT_beta_first" ,"m(Z') in GeV, CatH " ,40,1000,3000),"Evt_HT", "ABCD5_CatID==ABCD5_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    #inclusive
    Plot(ROOT.TH1F("ABCD5_inclusive_CatA_EvtHT_beta_first" ,"m(Z') in GeV, CatA " ,40,1000,3000),"Evt_HT", "((ABCD5_CatID==ABCD5_CatA_withtopbtag) || ABCD5_CatID==ABCD5_CatA_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatB_EvtHT_beta_first" ,"m(Z') in GeV, CatB " ,40,1000,3000),"Evt_HT", "((ABCD5_CatID==ABCD5_CatB_withtopbtag) || ABCD5_CatID==ABCD5_CatB_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatC_EvtHT_beta_first" ,"m(Z') in GeV, CatC " ,40,1000,3000),"Evt_HT", "((ABCD5_CatID==ABCD5_CatC_withtopbtag) || ABCD5_CatID==ABCD5_CatC_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatD_EvtHT_beta_first" ,"m(Z') in GeV, CatD " ,40,1000,3000),"Evt_HT", "((ABCD5_CatID==ABCD5_CatD_withtopbtag) || ABCD5_CatID==ABCD5_CatD_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD5_inclusive_CatE_EvtHT_beta_first" ,"m(Z') in GeV, CatE " ,40,1000,3000),"Evt_HT", "((ABCD5_CatID==ABCD5_CatE_withtopbtag) || ABCD5_CatID==ABCD5_CatE_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatF_EvtHT_beta_first" ,"m(Z') in GeV, CatF " ,40,1000,3000),"Evt_HT", "((ABCD5_CatID==ABCD5_CatF_withtopbtag) || ABCD5_CatID==ABCD5_CatF_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatG_EvtHT_beta_first" ,"m(Z') in GeV, CatG " ,40,1000,3000),"Evt_HT", "((ABCD5_CatID==ABCD5_CatG_withtopbtag) || ABCD5_CatID==ABCD5_CatG_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_inclusive_CatH_EvtHT_beta_first" ,"m(Z') in GeV, CatH " ,40,1000,3000),"Evt_HT", "((ABCD5_CatID==ABCD5_CatH_withtopbtag) || ABCD5_CatID==ABCD5_CatH_notopbtag)" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

]





#CatAList=["ABCD_notopbtag_CatA_Zprime_M" , "ABCD_notopbtag_CatA_Zprime_M_beta", "ABCD_notopbtag_CatA_Zprime_M_beta_first", "ABCD_notopbtag_CatA_Zprime_M_first"]

plotnames=[]
for i in plots:
    plotnames.append(i.name)


OnlyFirstList=len(plots)*[False]
#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
OnlyFirstList[plotnames.index("ABCD3_notopbtag_CatA_WMSD_beta_first"):plotnames.index('ABCD5_inclusive_CatH_EvtHT_beta_first') +1 ] = len(OnlyFirstList[plotnames.index("ABCD3_notopbtag_CatA_WMSD_beta_first"):plotnames.index('ABCD5_inclusive_CatH_EvtHT_beta_first') + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'

#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
assert len(OnlyFirstList)==len(plots)
#raw_input()




print name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,4000000,plots,samples)
outputpath=plotParallel(name,2000000,plots,SignalSamples+BackgroundSamples, [''], ['1'] , [''], ['1'],additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)
#outputpath=plotParallel(name,2000000,plots,SignalSamples, [''], ['1'] , [''], ['1'],additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)
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

#writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime15001200')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime20001200')]]+[transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime25001200')]])[plotnames.index('Notopbtag_EvtHT'):plotnames.index('Withtopbtag_Zprime_M_vs_N_JetsAK4')+1],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]]+[SignalSamples[SignalSampleNames.index('Zprime15001200')]]+[SignalSamples[SignalSampleNames.index('Zprime20001200')]]+[SignalSamples[SignalSampleNames.index('Zprime25001200')]], '','additionalcuts'+radi,True)

#writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('Notopbtag_Tprime_M'):plotnames.index('Withtopbtag_W_t21')+1],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]], 'label','MSDs'+radi,True)
#print SignalSampleNames
#writeListOfHistoLists(transposeLOL(transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500900'):SignalSampleNames.index('Zprime25001200')+1])[plotnames.index('Notopbtag_Tprime_M'):plotnames.index('Withtopbtag_W_t21')+1],SignalSamples[SignalSampleNames.index('Zprime1500900'):SignalSampleNames.index('Zprime25001200')+1], 'label','MSDs'+radi,True)
#writeListOfHistoLists([transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first')]],BackgroundSamples[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1], 'label','MSDs_QCD ')
#print listOfHistoListsABCD
print plotnames
#raw_input()


lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD)
listOfHistoListsABCD=lolABCD_rebinned
chekcNbins(listOfHistoListsABCD)


#lolBackgroundT=transposeLOL(listOfHistoListsBackground)
lolABCDT=transposeLOL(listOfHistoListsABCD)
#lolDataT=transposeLOL(listOfHistoListsData)

#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)
#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)


lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD)

chekcNbins(lolABCD_rebinned)

writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('ABCD3_notopbtag_CatA_WMSD_beta_first'):plotnames.index('ABCD5_inclusive_CatH_EvtHT_beta_first')+1],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]], '','single_regions_QCD_distros_'+radi,False,False,False,'histoE')

