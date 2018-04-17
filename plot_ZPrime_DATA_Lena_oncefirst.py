#############
# plot general control distributions
##############

from plotconfig_Zprime_DATA_Lena import *
from plot_additional_Zprime_DATA_Lena import *
from plot_cuts_ZPrime_MC_Lena import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy



ABCDeventhandling='oncefirst'
#ABCDeventhandling='reweight'

name='Zprime_MC_ABCD_DATAclosure'+radi+'_'+ABCDeventhandling+'_'+WPs
SampleNames=['ttbar' , 'QCD_HT', 'QCD_Pt' ]
SignalSampleNames=['Zprime1500900',  'Zprime20001200',  'Zprime25001200']




#Create Plots

plots=[


#ABCD1 t-tau32 bottomCSV    
    # no topsubbtag

    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatE_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatF_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatG_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatH_notopbtag" + " && " +    plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,
    
    ## with topsubbtag


    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,
    


##ABCD2 topMSD bottomCSV
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD2_CatID==ABCD2_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta2 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,


##ABCD3 bottomCSV W_MSD
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD3_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD3_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

##ABCD4 TprimeMass bottomCSV
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD4_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD4_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD4_CatID==ABCD4_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta4 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,


#ABCD5 W tau21 bottomCSV
    #no topbtag
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,


##ABCD6 W tau21 topMSD
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD6_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD6_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD6_CatID==ABCD6_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta6 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,


##ABCD7 WMSD topMSD
    ##no topbtag
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD7_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"1 btag") ,

    ## withtopsubbtag
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD7_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD7_CatID==ABCD7_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta7 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"2 btag") ,




##ABCD8 W tau21 bottomCSV  tmsd as third
    ##no topbtag

    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD8_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag

    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD8_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD8_CatID==ABCD8_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta8 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,



##ABCD9 W tau21 bottomCSV  tau32 as third
    ##no topbtag

    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD9_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag

    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD9_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD9_CatID==ABCD9_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta9 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,



##ABCD10 W tau21 bottomCSV  TprimeM as third
    ##no topbtag

    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD10_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ## withtopsubbtag

    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD10_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD10_CatID==ABCD10_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta10 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,







##MSD manual sepaTest


    #Plot(ROOT.TH1F("Notopbtag_Top_MSD" ,"m_{SD}(t-jet) in GeV, 1 b-tag" ,60,0,300),"Tops_ABCD"+radi+"_MSD",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    #Plot(ROOT.TH1F("Withtopbtag_Top_MSD" ,"m_{SD}(t-jet) in GeV, 2 b-tag",60,0,300),"Tops_ABCD"+radi+"_MSD",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    #Plot(ROOT.TH1F("Notopbtag_W_MSD" ,"m_{SD}(W-jet) in GeV, 1 b-tag" ,60,0,300),"Ws_ABCD"+radi+"_MSD",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    #Plot(ROOT.TH1F("Withtopbtag_W_MSD" ,"m_{SD}(W-jet) in GeV, 2 b-tag" ,60,0,300),"Ws_ABCD"+radi+"_MSD",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
 
    #Plot(ROOT.TH1F("Notopbtag_Bottom_CSV" ,"CSV_v2(b-jet), 1 b-tag" ,50,0,1),"Bottoms_ABCD"+radi+"_CSV",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_tau32 + "&&" + plotselection_t_MSD + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    #Plot(ROOT.TH1F("Withtopbtag_Bottom_CSV" ,"CSV_v2(b-jet), 2 b-tag",50,0,1),"Bottoms_ABCD"+radi+"_CSV",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_t_MSD + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"), 
 
    #Plot(ROOT.TH1F("Notopbtag_Top_t32" ,"#tau_{32}(t-jet), 1 b-tag" ,20,0,1),"Tops_ABCD"+radi+"_t32",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    #Plot(ROOT.TH1F("Withtopbtag_Top_t32" ,"#tau_{32}(t-jet), 2 b-tag",20,0,1),"Tops_ABCD"+radi+"_t32",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_W_tau21 + " && " + plotselection_TprimeMass, "1 btag"),
    #Plot(ROOT.TH1F("Notopbtag_W_t21" ,"#tau_{21}(W-jet), 1 b-tag" ,20,0,1),"Ws_ABCD"+radi+"_t21",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_tau32 + " && " + plotselection_TprimeMass, "1 btag"),
    #Plot(ROOT.TH1F("Withtopbtag_W_t21" ,"#tau_{21}(W-jet), 2 b-tag" ,20,0,1),"Ws_ABCD"+radi+"_t21",    plotselection3 + "&& Zprimes_ABCD"+radi+"_M>0 && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD + " &&" + plotselection_tau32 + " && " + plotselection_TprimeMass, "1 btag"),








]






plotnames=[]
for i in plots:
    plotnames.append(i.name)


OnlyFirstList=len(plots)*[False]
#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
OnlyFirstList[plotnames.index("ABCD5_notopbtag_CatE_Zprime_M_beta_first"):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first') +1 ] = len(OnlyFirstList[plotnames.index("ABCD5_notopbtag_CatE_Zprime_M_beta_first"):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first') + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'

#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
assert len(OnlyFirstList)==len(plots)
#raw_input()




print name,2000000,plots,SignalSamples+[BackgroundSamples[0]]+DataSamples,[''],['1.']
#outputpath=plotParallel(name,4000000,plots,samples)
outputpath=plotParallel(name,2000000,plots,SignalSamples+BackgroundSamples[BackgroundSampleNames.index('ttbar'):BackgroundSampleNames.index('ST_s')+1]+DataSamples, [''], ['1'] , weigthsystnamesMCSFs, systweightnamesMCSFs,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)

listOfHistoListsABCD=createHistoLists_fromSuperHistoFile(outputpath,DataSamples ,plots,1,[""], True )
listOfHistoListsABCDttbar=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples[BackgroundSampleNames.index('ttbar'):BackgroundSampleNames.index('ST_s')+1] ,plots,1,[""], True )



Datalll=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,weigthsystnamesMCSFs)
ttbarlll=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples[BackgroundSampleNames.index('ttbar'):BackgroundSampleNames.index('ST_s')+1],plots,weigthsystnamesMCSFs)

#print listOfHistoListsABCDttbar
#print [transposeLOL(listOfHistoListsABCDttbar)[BackgroundSampleNames.index('ttbar')]]

#print [transposeLOL(listOfHistoListsABCDttbar)[BackgroundSampleNames.index('ST_tW')]]


addLOLTtoLOLT([transposeLOL(listOfHistoListsABCDttbar)[BackgroundSampleNames.index('ttbar')]],[transposeLOL(listOfHistoListsABCDttbar)[BackgroundSampleNames.index('ST_tW')]])
addLOLTtoLOLT([transposeLOL(listOfHistoListsABCDttbar)[BackgroundSampleNames.index('ttbar')]],[transposeLOL(listOfHistoListsABCDttbar)[BackgroundSampleNames.index('ST_t')]])
addLOLTtoLOLT([transposeLOL(listOfHistoListsABCDttbar)[BackgroundSampleNames.index('ttbar')]],[transposeLOL(listOfHistoListsABCDttbar)[BackgroundSampleNames.index('ST_s')]])


#ttbarlll=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples[BackgroundSampleNames.index('ttbar'):BackgroundSampleNames.index('ST_s')+1],plots,weigthsystnamesMCSFs)

#print ttbarlll[0]
#print transposeLOL(ttbarlll)[0]
#raw_i<nput()
for ll1,ll2,ll3,ll4 in zip(transposeLOL([transposeLOL(ttbarlll)[BackgroundSampleNames.index('ttbar')]]),transposeLOL([transposeLOL(ttbarlll)[BackgroundSampleNames.index('ST_tW')]]),transposeLOL([transposeLOL(ttbarlll)[BackgroundSampleNames.index('ST_t')]]),transposeLOL([transposeLOL(ttbarlll)[BackgroundSampleNames.index('ST_s')]])):
    for l1,l2,l3,l4 in zip(ll1,ll2,ll3,ll4):
        for h1, h2,h3,h4 in zip(l1,l2,l3,l4):
            h1.Add(h2)
            h1.Add(h3)
            h1.Add(h4)


listOfHistoListsABCDttbar=transposeLOL([transposeLOL(listOfHistoListsABCDttbar)[BackgroundSampleNames.index('ttbar')]])
ttbarlll=transposeLOL([transposeLOL(ttbarlll)[BackgroundSampleNames.index('ttbar')]])

BackgroundSamples=[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]
BackgroundSampleNames=[BackgroundSampleNames[BackgroundSampleNames.index('ttbar')]]
#for lol in listOfHistoListsSignalAndBackground:
    #print lol[0][0], "Sind die pointer anders fuer die verschiedenen listOfHistoLists?"

labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)



print plotnames
#raw_input()

lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD,False,False,False,True)

#lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD)
listOfHistoListsABCD=lolABCD_rebinned
lolABCDttbar_rebinned=rebintovarbinsLOL(listOfHistoListsABCDttbar,False,False,False,True)
listOfHistoListsABCDttbar=lolABCDttbar_rebinned

Datalll=rebintovarbinsLLL(Datalll,False,False,False,False)
ttbarlll=rebintovarbinsLLL(ttbarlll,False,False,False,False)


#chekcNbins(listOfHistoListsABCD)


#lolBackgroundT=transposeLOL(listOfHistoListsBackground)
lolABCDT=transposeLOL(listOfHistoListsABCD)
lolABCDttbarT=transposeLOL(listOfHistoListsABCDttbar)
#lolDataT=transposeLOL(listOfHistoListsData)

#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)
#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)


#lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD)

#chekcNbins(lolABCD_rebinned)

subtract_lols(listOfHistoListsABCD,listOfHistoListsABCDttbar)
subtract_llls(Datalll,ttbarlll)



print Datalll

DataLoL=[]
toplol=[]

for ll,topll,plotname in zip(Datalll,ttbarlll,plotnames):
    templ=[]
    temptopl=[]
    for l,topl in zip(ll,topll):
        for h,toph,systname in zip(l,topl,weigthsystnamesMCSFs):
          #for ABCDversion in ['ABCD1','ABCD2','ABCD3','ABCD4','ABCD5','ABCD6','ABCD7','ABCD8','ABCD9','ABCD10']:
          for ABCDversion in ['ABCD5']:
            if ABCDversion in plotname and ABCDversion in systname:
                print "if ",h, "    ", systname, "    " ,plotname , "      ", h.Integral()
                templ.append(h)
                temptopl.append(toph)
    DataLoL.append(templ)
    toplol.append(temptopl)
    
    
print Datalll

print "right? ",  DataLoL

writeListOfHistoLists(transposeLOL([transposeLOL(DataLoL)[0]])[plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first'):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first')+1],[DataSamples[0]], '','single_regions_DATA_'+name,False,False,False,'histoE')

writeListOfHistoLists(transposeLOL([transposeLOL(DataLoL)[0]]+[transposeLOL(toplol)[0]])[plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first'):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first')+1],[DataSamples[0]]+[BackgroundSamples[0]], '','single_regions_DATA_and_ttbar_'+name,False,True,False,'histoE')


#writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]+transposeLOL(listOfHistoListsSignal)[SignalSampleNames.index('Zprime1500700'):SignalSampleNames.index('Zprime25001200')])[plotnames.index('Notopbtag_Tprime_M'):plotnames.index('Withtopbtag_W_t21')+1],[[BackgroundSamples[0]][BackgroundSampleNames.index('QCD_HT')]]+SignalSamples[SignalSampleNames.index('Zprime1500700'):SignalSampleNames.index('Zprime25001200')], '','MSDs'+radi,True)

#writeListOfHistoLists(transposeLOL([transposeLOL(DataLoL)[DataSampleNames.index('DATA_2016')]])[plotnames.index('ABCD1_notopbtag_CatE_Zprime_M_beta_first'):plotnames.index('ABCD8_withtopbtag_CatH_Zprime_M_beta_first')+1],[DataSamples[DataSampleNames.index('DATA_2016')]], '','single_regions_Data'+radi,False,False,False,'histoE')


#for ABCDversion in ['ABCD1','ABCD2','ABCD3','ABCD4','ABCD5','ABCD6','ABCD7','ABCD8','ABCD9','ABCD10']:
#for ABCDversion in ['ABCD5','ABCD8','ABCD9']:
for ABCDversion in ['ABCD5']:
    ABCDclosure1D_final(transposeLOL(transposeLOL(DataLoL)),plotnames,DataSamples,ABCDversion + '_notopbtag_CatA_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatB_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatC_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatD_Zprime_M_beta_first', ABCDversion + '_notopbtag_CatE_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatF_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatG_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/DATAclosureABCD'+radi+ABCDeventhandling+'_'+WPs+'_notopbtag', True)
    ABCDclosure1D_final(transposeLOL(transposeLOL(DataLoL)),plotnames,DataSamples,ABCDversion + '_withtopbtag_CatA_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatB_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatC_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatD_Zprime_M_beta_first', ABCDversion + '_withtopbtag_CatE_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatF_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatG_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/DATAclosureABCD'+radi+ABCDeventhandling+'_'+WPs+'_withtopbtag',True)

    #ABCDclosure1D_new(transposeLOL(transposeLOL(DataLoL)),plotnames,DataSamples,ABCDversion + '_notopbtag_CatA_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatB_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatC_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatD_Zprime_M_beta_first', ABCDversion + '_notopbtag_CatE_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatF_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatG_Zprime_M_beta_first',ABCDversion + '_notopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/DATAclosureABCD'+radi+ABCDeventhandling+'_'+WPs+'_notopbtag', True)
    #ABCDclosure1D_new(transposeLOL(transposeLOL(DataLoL)),plotnames,DataSamples,ABCDversion + '_withtopbtag_CatA_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatB_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatC_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatD_Zprime_M_beta_first', ABCDversion + '_withtopbtag_CatE_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatF_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatG_Zprime_M_beta_first',ABCDversion + '_withtopbtag_CatH_Zprime_M_beta_first',False,1,'',ABCDversion+'/DATAclosureABCD'+radi+ABCDeventhandling+'_'+WPs+'_withtopbtag',True)

