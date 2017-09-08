#############
# plot general control distributions 
##############

from plotconfig_Zprime_MC import *
from plot_additional_Zprime_MC import *
from plot_cuts_ZPrime_MC import *

sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy


ABCDeventhandling='oncefirst'

name='Zprime_MC_'+ABCDeventhandling+'_'+WPs
#name='Zprime_MC_'+ABCDversion+'_'+WPs

# definition of categories

#categoriesZprimeTprime=[
#	("(tWb&&N_BTagsM=1)","tWb1",""),#
#	("(tWb&&N_BTagsM=2)","tWb2",""),
#	("(ttH&&N_BTagsM=1)","ttH1",""),
#	("(ttH&&N_BTagsM=2)","ttH2",""),
#	("(ttH&&N_BTagsM=3)","ttH3",""),
#	("(ttH&&N_BTagsM=4)","ttH4",""),
#	("(ttZ)","ttZ",""),
#]  N_Sideband_withtopbtag_bottom_anti_Topfirst_Bottoms



## book plots
#plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
#plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
##plotselection="N_packedPatJetsAK8PFCHSSoftDrop>=2&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200&&Evt_HT>850"
#plotselection1="Evt_HT>850"
#plotselection3="Evt_HT>1000"
##plotselection1=""
#plotselection2="(N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 && Evt_HT>850) "





##Own Plotselections for ABCD-method

##plotselection_tau32 = " Tops_ABCD1_t32 < 0.67   "
#plotselection_tau32 = " Tops_ABCD1_t32 < 0.86   "
#plotselection_W_MSD =  " (70 < Ws_ABCD1_MSD  &&   Ws_ABCD1_MSD < 100) "
#plotselection_B_CSV = "  Bottoms_ABCD1_CSV > 0.8  "
##plotselection_W_tau21 = " Ws_ABCD1_t21 < 0.45 "
#plotselection_W_tau21 = " Ws_ABCD1_t21 < 0.6 "
#plotselection_t_MSD = " (105 < Tops_ABCD1_MSD && Tops_ABCD1_MSD < 210) "
#plotselection_topsubjetCSVv2 = " Tops_ABCD1_maxsubjetCSVv2 > 0.8 "




#plotselection_tau32_0 = " Tops_ABCD1_t32[0] < 0.86   "
##plotselection_tau32_0 = " Tops_ABCD1_t32[0] < 0.67   "
#plotselection_W_MSD_0 =  " (70 < Ws_ABCD1_MSD[0]  &&   Ws_ABCD1_MSD[0] < 100) "
##plotselection_B_CSV_0 = "  Bottoms_ABCD1_CSV[0] > 0.8   "
#plotselection_W_tau21_0 = " Ws_ABCD1_t21[0] < 0.6  "
#plotselection_W_tau21_0 = " Ws_ABCD1_t21[0] < 0.45  "

#plotselection_tau32_anti=" Tops_ABCD1_t32 > 0.86   "
#plotselection_W_MSD_anti =  " (70 > Ws_ABCD1_MSD  ||   Ws_ABCD1_MSD > 100) "
#plotselection_B_CSV_anti = "  Bottoms_ABCD1_CSV < 0.46   "
#plotselection_W_tau21_anti = " Ws_ABCD1_t21 > 0.6 "
#plotselection_t_MSD_anti = " (105 > Tops_ABCD1_MSD || Tops_ABCD1_MSD > 210) "
#plotselection_topsubjetCSVv2_anti = " Tops_ABCD1_maxsubjetCSVv2 < 0.8 "

#plotselection_tau32_anti_0 =" Tops_ABCD1_t32[0] > 0.86   "
#plotselection_W_MSD_anti_0 =  " (70 > Ws_ABCD1_MSD[0]  ||   Ws_ABCD1_MSD[0] > 100) "
#plotselection_B_CSV_anti_0 = "  Bottoms_ABCD1_CSV[0] < 0.46   "
#plotselection_W_tau21_anti_0 = " Ws_ABCD1_t21[0]  > 0.6 "




#plotselection_W_MSD_one_sided =  " (70 < Ws_ABCD1_MSD && Ws_ABCD1_MSD < 100)"
#plotselection_W_MSD_one_sided_anti =  " (70 > Ws_ABCD1_MSD && Ws_ABCD1_MSD < 100)"


#plotselection_ABCD1_general=  plotselection2 + "&& Zprimes_ABCD_M>0   &&    Ws_ABCD1_t21 <  0.6    &&    100 < Tops_ABCD1_MSD     &&    Tops_ABCD1_MSD  < 210  "
#plotselection_ABCD1_general =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    70 < Ws_ABCD1_MSD  &&   Ws_ABCD1_MSD < 100     &&    100 < Tops_ABCD1_MSD     &&    Tops_ABCD1_MSD  < 210   "
#plotselection_ABCD2_general =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    70 < Ws_ABCD1_MSD  &&   Ws_ABCD1_MSD < 100     &&     Tops_ABCD1_t32 < 0.86   "
#plotselection_ABCD1_general_0 =  plotselection2 + "&& Zprimes_ABCD_M[0]>0   &&    Ws_ABCD1_t21[0] >  0.6    &&    100 < Tops_ABCD1_MSD[0]     &&    Tops_ABCD1_MSD[0]  < 210   "
#plotselection_ABCD1_general_0 =   plotselection2 + "&& Zprimes_ABCD_M[0]>0   &&    70 < Ws_ABCD1_MSD[0]  &&   Ws_ABCD1_MSD[0] < 100     &&    100 < Tops_ABCD1_MSD[0]     &&    Tops_ABCD1_MSD[0]  < 210   "

#plotselection_ABCD1_general_alt_notopbtag =  plotselection2 + " && Zprimes_ABCD1_masscorrnotopbtag_M>0 && 70 < Ws_ABCD1_masscorrnotopbtag_MSD && Ws_ABCD1_masscorrnotopbtag_MSD < 100 && Tops_ABCD1_masscorrnotopbtag_t32<0.86 "
#plotselection_ABCD1_general_alt_withtopbtag =  plotselection2 + " && Zprimes_ABCD1_masscorrwithtopbtag_M>0 && 70 < Ws_ABCD1_masscorrwithtopbtag_MSD && Ws_ABCD1_masscorrwithtopbtag_MSD < 100 && Tops_ABCD1_masscorrwithtopbtag_t32<0.86 "




plots=[

   


    ##doing only first element
    ##beta (tau21)
    ## no topsubbtag
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatA_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatB_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatC_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatD_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatE_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatF_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatG_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatH_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,
    
    ## with topsubbtag
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatA_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatB_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatC_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatD_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatE_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatF_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatG_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatH_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,
    
    ##inclusive
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatA_withtopbtag) || ABCD1_CatID==ABCD1_CatA_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatB_withtopbtag) || ABCD1_CatID==ABCD1_CatB_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatC_withtopbtag) || ABCD1_CatID==ABCD1_CatC_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatD_withtopbtag) || ABCD1_CatID==ABCD1_CatD_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD1_inclusive_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatE_withtopbtag) || ABCD1_CatID==ABCD1_CatE_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatF_withtopbtag) || ABCD1_CatID==ABCD1_CatF_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatG_withtopbtag) || ABCD1_CatID==ABCD1_CatG_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatH_withtopbtag) || ABCD1_CatID==ABCD1_CatH_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,




    #ABCD
    #no topbtag
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatA_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatB_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatC_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatD_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatE_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatF_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatG_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3  + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatH_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag") ,

    #withtopsubbtag
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatA_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatB_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatC_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2_anti + "&& " + cut1  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatD_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1  ,"2 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatE_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1_anti  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatF_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1_anti  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatG_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3  + "&&" + cut2_anti + "&& " + cut1_anti  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "ABCD_CatID==ABCD_CatH_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1_anti  ,"2 btag") ,

    #inclusive
    Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatA_withtopbtag) || ABCD_CatID==ABCD_CatA_notopbtag)" + " && " + generalselection + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatB_withtopbtag) || ABCD_CatID==ABCD_CatB_notopbtag)" + " && " + generalselection + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatC_withtopbtag) || ABCD_CatID==ABCD_CatC_notopbtag)" + " && " + generalselection + " && " + cut3 + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatD_withtopbtag) || ABCD_CatID==ABCD_CatD_notopbtag)" + " && " + generalselection + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatE_withtopbtag) || ABCD_CatID==ABCD_CatE_notopbtag)" + " && " + generalselection + " && " + cut3 + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatF_withtopbtag) || ABCD_CatID==ABCD_CatF_notopbtag)" + " && " + generalselection + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatG_withtopbtag) || ABCD_CatID==ABCD_CatG_notopbtag)" + " && " + generalselection + " && " + cut3  + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD_M", "((ABCD_CatID==ABCD_CatH_withtopbtag) || ABCD_CatID==ABCD_CatH_notopbtag)" + " && " + generalselection + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag") ,

##Tprime
    ## no topsubbtag
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatA_Tprime_M" ,"m(Z') in GeV, CatA " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatA_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatB_Tprime_M" ,"m(Z') in GeV, CatB " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatB_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatC_Tprime_M" ,"m(Z') in GeV, CatC " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatC_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatD_Tprime_M" ,"m(Z') in GeV, CatD " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatD_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatE_Tprime_M" ,"m(Z') in GeV, CatE " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatE_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatF_Tprime_M" ,"m(Z') in GeV, CatF " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatF_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatG_Tprime_M" ,"m(Z') in GeV, CatG " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatG_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatH_Tprime_M" ,"m(Z') in GeV, CatH " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatH_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti ,"1 btag") ,
    
    ## with topsubbtag
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatA_Tprime_M" ,"m(Z') in GeV, CatA " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatA_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatB_Tprime_M" ,"m(Z') in GeV, CatB " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatB_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatC_Tprime_M" ,"m(Z') in GeV, CatC " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatC_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatD_Tprime_M" ,"m(Z') in GeV, CatD " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatD_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatE_Tprime_M" ,"m(Z') in GeV, CatE " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatE_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatF_Tprime_M" ,"m(Z') in GeV, CatF " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatF_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatG_Tprime_M" ,"m(Z') in GeV, CatG " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatG_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatH_Tprime_M" ,"m(Z') in GeV, CatH " ,60,0,3000),"Tprimes_ABCD_M", "ABCD1_CatID==ABCD1_CatH_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatA_Tprime_M" ,"m(Z') in GeV, CatA " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatA_withtopbtag) || ABCD1_CatID==ABCD1_CatA_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatB_Tprime_M" ,"m(Z') in GeV, CatB " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatB_withtopbtag) || ABCD1_CatID==ABCD1_CatB_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatC_Tprime_M" ,"m(Z') in GeV, CatC " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatC_withtopbtag) || ABCD1_CatID==ABCD1_CatC_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatD_Tprime_M" ,"m(Z') in GeV, CatD " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatD_withtopbtag) || ABCD1_CatID==ABCD1_CatD_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD1_inclusive_CatE_Tprime_M" ,"m(Z') in GeV, CatE " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatE_withtopbtag) || ABCD1_CatID==ABCD1_CatE_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatF_Tprime_M" ,"m(Z') in GeV, CatF " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatF_withtopbtag) || ABCD1_CatID==ABCD1_CatF_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatG_Tprime_M" ,"m(Z') in GeV, CatG " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatG_withtopbtag) || ABCD1_CatID==ABCD1_CatG_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatH_Tprime_M" ,"m(Z') in GeV, CatH " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD1_CatID==ABCD1_CatH_withtopbtag) || ABCD1_CatID==ABCD1_CatH_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

##ABCD2
    ##with topbtag
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatA_Tprime_M" ,"m(Z') in GeV, CatA " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatA_notopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatB_Tprime_M" ,"m(Z') in GeV, CatB " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatB_notopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatC_Tprime_M" ,"m(Z') in GeV, CatC " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatC_notopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatD_Tprime_M" ,"m(Z') in GeV, CatD " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatD_notopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatE_Tprime_M" ,"m(Z') in GeV, CatE " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatE_notopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatF_Tprime_M" ,"m(Z') in GeV, CatF " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatF_notopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatG_Tprime_M" ,"m(Z') in GeV, CatG " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatG_notopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_notopbtag_CatH_Tprime_M" ,"m(Z') in GeV, CatH " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatH_notopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    ##no topbtag
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatA_Tprime_M" ,"m(Z') in GeV, CatA " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatA_withtopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatB_Tprime_M" ,"m(Z') in GeV, CatB " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatB_withtopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatC_Tprime_M" ,"m(Z') in GeV, CatC " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatC_withtopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatD_Tprime_M" ,"m(Z') in GeV, CatD " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatD_withtopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatE_Tprime_M" ,"m(Z') in GeV, CatE " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatE_withtopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatF_Tprime_M" ,"m(Z') in GeV, CatF " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatF_withtopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatG_Tprime_M" ,"m(Z') in GeV, CatG " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatG_withtopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD2_withtopbtag_CatH_Tprime_M" ,"m(Z') in GeV, CatH " ,60,0,3000),"Tprimes_ABCD_M", "ABCD2_CatID==ABCD2_CatH_withtopbtag" + " && " + plotselection_ABCD2_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

    ##inclusive
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatA_Tprime_M" ,"m(Z') in GeV, CatA " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatA_withtopbtag) || ABCD2_CatID==ABCD2_CatA_notopbtag)" + " && " + plotselection_ABCD2_general + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatB_Tprime_M" ,"m(Z') in GeV, CatB " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatB_withtopbtag) || ABCD2_CatID==ABCD2_CatB_notopbtag)" + " && " + plotselection_ABCD2_general + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatC_Tprime_M" ,"m(Z') in GeV, CatC " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatC_withtopbtag) || ABCD2_CatID==ABCD2_CatC_notopbtag)" + " && " + plotselection_ABCD2_general + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatD_Tprime_M" ,"m(Z') in GeV, CatD " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatD_withtopbtag) || ABCD2_CatID==ABCD2_CatD_notopbtag)" + " && " + plotselection_ABCD2_general + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD2_inclusive_CatE_Tprime_M" ,"m(Z') in GeV, CatE " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatE_withtopbtag) || ABCD2_CatID==ABCD2_CatE_notopbtag)" + " && " + plotselection_ABCD2_general + " && " + plotselection_t_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatF_Tprime_M" ,"m(Z') in GeV, CatF " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatF_withtopbtag) || ABCD2_CatID==ABCD2_CatF_notopbtag)" + " && " + plotselection_ABCD2_general + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatG_Tprime_M" ,"m(Z') in GeV, CatG " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatG_withtopbtag) || ABCD2_CatID==ABCD2_CatG_notopbtag)" + " && " + plotselection_ABCD2_general + " && " + plotselection_t_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD2_inclusive_CatH_Tprime_M" ,"m(Z') in GeV, CatH " ,60,0,3000),"Tprimes_ABCD_M", "((ABCD2_CatID==ABCD2_CatH_withtopbtag) || ABCD2_CatID==ABCD2_CatH_notopbtag)" + " && " + plotselection_ABCD2_general + " && " + plotselection_t_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,


    #Plot(ROOT.TH1F("MCSF_Weight_ABCD1_CatA" ,"m(Z') in GeV, CatA " ,100,0,1000),"MCSF_Weight_ABCD1", "ABCD1_CatID==ABCD1_CatA_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("MCSF_Weight_ABCD1_CatB" ,"m(Z') in GeV, CatB " ,100,0,1000),"MCSF_Weight_ABCD1", "ABCD1_CatID==ABCD1_CatB_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("MCSF_Weight_ABCD1_CatC" ,"m(Z') in GeV, CatC " ,100,0,1000),"MCSF_Weight_ABCD1", "ABCD1_CatID==ABCD1_CatC_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("MCSF_Weight_ABCD1_CatD" ,"m(Z') in GeV, CatD " ,100,0,1000),"MCSF_Weight_ABCD1", "ABCD1_CatID==ABCD1_CatD_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("MCSF_Weight_ABCD1_CatE" ,"m(Z') in GeV, CatE " ,100,0,1000),"MCSF_Weight_ABCD1", "ABCD1_CatID==ABCD1_CatE_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("MCSF_Weight_ABCD1_CatF" ,"m(Z') in GeV, CatF " ,100,0,1000),"MCSF_Weight_ABCD1", "ABCD1_CatID==ABCD1_CatF_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("MCSF_Weight_ABCD1_CatG" ,"m(Z') in GeV, CatG " ,100,0,1000),"MCSF_Weight_ABCD1", "ABCD1_CatID==ABCD1_CatG_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("MCSF_Weight_ABCD1_CatH" ,"m(Z') in GeV, CatH " ,100,0,1000),"MCSF_Weight_ABCD1", "ABCD1_CatID==ABCD1_CatH_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti ,"1 btag") ,

  

]





plotnames=[]
for i in plots:
    plotnames.append(i.name)

OnlyFirstList=len(plots)*[False]
#OnlyFirstList[plotnames.index("ABCD1_notopbtag_CatA_Zprime_M"):plotnames.index('ABCD2_inclusive_CatH_Tprime_M') +1 ] = len(OnlyFirstList[plotnames.index("ABCD1_notopbtag_CatA_Zprime_M"):plotnames.index('ABCD2_inclusive_CatH_Tprime_M') + 1 ] ) * [True]
OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_M"):plotnames.index(ABCDversion + "_inclusive_CatH_Zprime_M") +1 ] = len(OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_M"):plotnames.index(ABCDversion + "_inclusive_CatH_Zprime_M") + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'

#print allweightsystnames
#print allsystweights

#print name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM,systweightsbasic+systweightsMadgraphbantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weightsystnamesPythia8bantiZprimeM,systweightsPythia8bantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)



outputpath=plotParallel(name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples+systsamples,[""],["1"],allweightsystnames,allsystweights,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList,otherSystNames)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)

rebinnedHistosExist=False
rebinnedHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned.root'
rebinnedandaddedHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_added.root'

allweightsystnames=allweightsystnames+JECsystnames
print allweightsystnames
if not os.path.isfile(rebinnedHistoPath):

    #listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples,plots,1)
    #listOfHistoListsBackground=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples,plots,1)
    #listOfHistoListsDataMadgraph=createHistoLists_fromSuperHistoFile(outputpath,DataSamples,plots,1)
    #listOfHistoListsDataPythia=createHistoLists_fromSuperHistoFile(outputpath,DataSamples,plots,1)

    #listOfHistoListsSignal=rebintovarbinsLOL(listOfHistoListsSignal,name,False,True,False)
    #listOfHistoListsBackground=rebintovarbinsLOL(listOfHistoListsBackground,name,False,True,False)
    #listOfHistoListsDataMadgraph=rebintovarbinsLOL(listOfHistoListsDataMadgraph,name,False,True,False)
    #listOfHistoListsDataPythia=rebintovarbinsLOL(listOfHistoListsDataPythia,name,False,True,False)

    lllSignal=createLLL_fromSuperHistoFileSyst(outputpath,SignalSamples,plots,allweightsystnames)
    lllBackground=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,allweightsystnames)
    lllData_Madgraph=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,allweightsystnames)
    #lllData_Pythia=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,allweightsystnames)

    lllSignal=rebintovarbinsLLL(lllSignal,name,True,False,False,True)
    lllBackground=rebintovarbinsLLL(lllBackground,name,True,False,False,True)
    lllData_Madgraph=rebintovarbinsLLL(lllData_Madgraph,name,True,False,False,True)
    #lllData_Pythia=rebintovarbinsLLL(lllData_Pythia,name,False,True,False)
    addLLLtoLLL(lllData_Madgraph,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),name,False,allweightsystnames,True)

else:
  if not os.path.isfile(rebinnedandaddedHistoPath):

    #listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(rebinnedHistoPath,SignalSamples,plots,1)
    #listOfHistoListsBackground=createHistoLists_fromSuperHistoFile(rebinnedHistoPath,BackgroundSamples,plots,1)
    #listOfHistoListsDataMadgraph=createHistoLists_fromSuperHistoFile(rebinnedHistoPath,DataSamples,plots,1)
    #listOfHistoListsDataPythia=createHistoLists_fromSuperHistoFile(rebinnedHistoPath,DataSamples,plots,1)

    lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,SignalSamples,plots,allweightsystnames)
    lllBackground=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,BackgroundSamples,plots,allweightsystnames)
    lllData_Madgraph=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,DataSamples,plots,allweightsystnames) 
    addLLLtoLLL(lllData_Madgraph,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),name,False,allweightsystnames,True)
    #lllData_Pythia=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,DataSamples,plots,allweightsystnames)
  else:
    lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedandaddedHistoPath,SignalSamples,plots,allweightsystnames)
    lllBackground=createLLL_fromSuperHistoFileSyst(rebinnedandaddedHistoPath,BackgroundSamples,plots,allweightsystnames)
    lllData_Madgraph=createLLL_fromSuperHistoFileSyst(rebinnedandaddedHistoPath,DataSamples,plots,allweightsystnames) 


#addLOLtoLOL(listOfHistoListsDataMadgraph,transposeLOL([transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("ttbar")]]))
#addLOLtoLOL(listOfHistoListsDataPythia,transposeLOL([transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("QCDPythia8")]]+[transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("ttbar")]]))

#addLLLtoLLL(lllData_Madgraph,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),True,allweightsystnames)
#addLLLtoLLL(lllData_Pythia,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDPythia8")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),True,allweightsystnames)


#################################################################Transosed LOL ######################
#LOLSumw2(listOfHistoLists)
#dummylist=[[]]
labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)
#lolSignalT=transposeLOL(listOfHistoListsSignal)
#lolBackgroundT=transposeLOL(listOfHistoListsBackground)
#lolDataMadgraphT=transposeLOL(listOfHistoListsDataMadgraph)
#lolDataPythiaT=transposeLOL(listOfHistoListsDataPythia)


######### create Envelope for renorm and factorization ##############

#writeListOfHistoLists2(transposeLOL(transposeLOL(lllBackground[plotnames.index('ABCD1_notopbtag_CatA_Zprime_M')])[allweightsystnames.index('_MCSF_PDF0'),allweightsystnames.index('_MCSF_PDF100')]),BackgroundSamples, '','PDFstuff',False,False,False,'histo',False, False,True)

#envlll_nom=selectsubLLL(lllBackground,range(plotnames.index('ABCD1_notopbtag_CatA_Zprime_M'),plotnames.index('ABCD2_inclusive_CatE_Tprime_M')+1),[allweightsystnames.index('')],range(BackgroundSampleNames.index('QCDMadgraph'),BackgroundSampleNames.index('QCDPythia8')+1))
#envlll_up=selectsubLLL(lllBackground,range(plotnames.index('ABCD1_notopbtag_CatA_Zprime_M'),plotnames.index('ABCD2_inclusive_CatE_Tprime_M')+1),[allweightsystnames.index('_MCSF_renfac_envUp')],range(BackgroundSampleNames.index('QCDMadgraph'),BackgroundSampleNames.index('QCDPythia8')+1))
#envlll_down=selectsubLLL(lllBackground,range(plotnames.index('ABCD1_notopbtag_CatA_Zprime_M'),plotnames.index('ABCD2_inclusive_CatE_Tprime_M')+1),[allweightsystnames.index('_MCSF_renfac_envDown')],range(BackgroundSampleNames.index('QCDMadgraph'),BackgroundSampleNames.index('QCDPythia8')+1))
#envlll_lll=selectsubLLL(lllBackground,range(plotnames.index('ABCD1_notopbtag_CatA_Zprime_M'),plotnames.index('ABCD2_inclusive_CatE_Tprime_M')+1),range(allweightsystnames.index('_MCSF_renfacUp'),allweightsystnames.index('_MCSF_facDown')+1),range(BackgroundSampleNames.index('QCDMadgraph'),BackgroundSampleNames.index('QCDPythia8')+1))

#create_envelope(envlll_nom,envlll_up,envlll_down,envlll_lll)

##transposeLOL(transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index('_ABCD1_notopbtag_CatA_Zprime_M')])[weightsystnames.index('_MCSF_renfacUp'):weightsystnames.index('_MCSF_renfacDown')+1])[BackgroundSampleNames.index('ttbar')]

#writeListOfHistoLists([transposeLOL(transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index('ABCD1_notopbtag_CatA_Zprime_M')])[weightsystnames.index('_MCSF_PDF000'):weightsystnames.index('_MCSF_PDF100')+1])[BackgroundSampleNames.index('ttbar')]], 'PDFs_ttbar','PDFs_ttbar',False,False,False,'histo',False, False,True)
#writeListOfHistoLists([transposeLOL(transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index('ABCD1_withtopbtag_CatA_Zprime_M')])[weightsystnames.index('_MCSF_PDF000'):weightsystnames.index('_MCSF_PDF100')+1])[BackgroundSampleNames.index('ttbar')]], 'PDFs_ttbar','PDFs_ttbar',False,False,False,'histo',False, False,True)
#writeListOfHistoLists([transposeLOL(transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index('ABCD1_inclusive_CatA_Zprime_M')])[weightsystnames.index('_MCSF_PDF000'):weightsystnames.index('_MCSF_PDF100')+1])[BackgroundSampleNames.index('ttbar')]], 'PDFs_ttbar','PDFs_ttbar',False,False,False,'histo',False, False,True)



################################### AB Closure ########################################
######Using Madgraph SBSSSSF
####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] ,[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)



#####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)
                      
                      
                      
########Using PT SBSSSF
#####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] ,[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)


#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)









#####################################AB Closure withtopbtag#########################
#####Using Madgraph SBSSSSF
####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] ,[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)



#####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt")]], 'AB_background_estimation_PT' , True , False, False, "histoE", False, False, True, False)

########Using PT SBSSSF
#####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] ,[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)


#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt")]], 'AB_background_estimation_PT' , True , False, False, "histoE", False, False, True, False)



################################################################################### AB Scale factors

#writeHistoListwithXYErrors(transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_bottom_anti_Zprime_M"):plotnames.index("SB_SF_bottom_anti_Tops_Pt")+1]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_withtopbtag_bottom_anti_Zprime_M"):plotnames.index("SB_SF_withtopbtag_bottom_anti_Tops_Pt")+1],[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]],'Zprime_SBSSSFs_banti',1,'pol2')

#writeHistoListwithXYErrors(transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_top_anti_Tops_Pt"):plotnames.index("SB_SF_top_anti_Ws_Pt")+1]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_withtopbtag_top_anti_Tops_Pt"):plotnames.index("SB_SF_withtopbtag_top_anti_Ws_Pt")+1],[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]],'Zprime_SBSSSFs_tanti',1,"[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))/x")


######################TAGRATES############################
##writeListOfHistoLists(transposeLOL(lolDataT[DataSampleNames.index("MC_BKG_DATA"):])[plotnames.index("t_tagrate_pt"):plotnames.index("b_misstagrate_pt")+1],DataSamples,'tagrates','tagrates',False,False,False,'EL') 
##writeHistoListwithXYErrors(transposeLOL(lolDataT[DataSampleNames.index("MC_BKG_DATA"):])[plotnames.index("t_tagrate_pt"):plotnames.index("b_misstagrate_pt")+1],DataSamples,'tagrates_fit',1,"[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))/x")



##SchmonCorrelation(transposeLOL(lolT[3:5])[plotnames.index("SB_SF_bottom_anti_Bottoms_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_W_anti_Ws_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_top_anti_Tops_Pt")],transposeLOL(lolT[3:5])[plotnames.index("SB_SF_bottom_anti_Bottoms_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_W_anti_Ws_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_top_anti_Tops_Pt")],name='lada', rebin=1)
##SchmonCorrelation(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("SB_SF_bottom_anti_Bottoms_Pt")]+transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("SB_SF_W_anti_Ws_Pt")]+transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("SB_SF_top_anti_Tops_Pt")],transposeLOL(lolDataT)[plotnames.index("t_misstagrate_pt")]+transposeLOL(lolDataT)[plotnames.index("W_misstagrate_pt")]+transposeLOL(lolDataT)[plotnames.index("b_misstagrate_pt")],name='correlations', rebin=1)


##print transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("N_packedPatJetsAK8PFCHSSoftDrop"):plotnames.index("Evt_HT_Jets")+1]



##writeListOfHistoLists(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("ABCD1_top_tau32_vs_top_MSD"):plotnames.index("ABCD1_top_tau32_vs_W_MSD")],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1],plotnames[plotnames.index('ABCD1_top_tau32_vs_top_MSD'):plotnames.index('ABCD1_W_MSD_vs_Bottom_CSV_v2')+1],'ABCD',True,False,False,'colz',False,False,False,False)

#writeListOfHistoLists(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("Signal_Topfirst_Zprime_M"):plotnames.index("Sideband_top_withbtag_anti_Topfirst_Zprime_M")+1],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1],plotnames[plotnames.index('Signal_Topfirst_Zprime_M'):plotnames.index('Sideband_top_withbtag_anti_Topfirst_Zprime_M')+1],'ahhh',True,False,False,'colz',False,False,False,False)




#print listOfHistoListsData


################Final ###################

#################with Syst notoptag #####################R

#####################################BANTI ZPRIME CLOSURE######################


#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_', True)


#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_', False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_', False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_', False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_', False)




####################################TANTI Top CLOSURE######################
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_',True)


#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_',False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_',False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_',False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_',False)



#################with Syst withtopbtag ############################

####################################BANTI ZPRIME CLOSURE######################
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)

#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)


####################################TANTI Top CLOSURE######################
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_0.3pb','SC_Zprime25001200_0.3pb','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)

#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)






for dataname, signalname, SC_name in zip(DataSampleNames,SignalSampleNames+[SignalSampleNames[0]],BackgroundSampleNames[BackgroundSampleNames.index('SC_Zprime15001200_8_6pb'):BackgroundSampleNames.index('SC_none')+1]):
    for QCDname in ['QCDMadgraph','QCDPythia8']:
        #for ABCDversion in ['ABCD1','ABCD2']:
        for ABCDversion in [ABCDversion]:
            for Category in ['notopbtag','withtopbtag','inclusive']:
          
################Final with ABCD only ###################
#################with Syst notoptag #####################R
              if QCDname is 'QCDMadgraph':
                ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(lllData_Madgraph,lllBackground,lllSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,dataname,SC_name,signalname,ABCDversion+'_'+Category+'_CatA', ABCDversion+'_'+Category+'_CatB', ABCDversion+'_'+Category+'_CatC', ABCDversion+'_'+Category+'_CatD',QCDname, 'fancy_'+ABCDversion+'_'+ABCDeventhandling+'_'+WPs)
                
              #if QCDname is 'QCDPythia8':
                #ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(lllData_Pythia,lllBackground,lllSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,dataname,SC_name,signalname,ABCDversion+'_'+Category+'_CatA', ABCDversion+'_'+Category+'_CatB', ABCDversion+'_'+Category+'_CatC', ABCDversion+'_'+Category+'_CatD',QCDname, 'fancy_'+ABCDversion+'_'+ABCDeventhandling+'_'+WPs)
