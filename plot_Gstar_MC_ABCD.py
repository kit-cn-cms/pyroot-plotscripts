#############
# plot general control distributions 
##############

from plotconfig_Gstar_MC import *
from plot_additional_Zprime_MC import *
from plot_cuts_ZPrime_MC import *

sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy


ABCDeventhandling='oncefirst'

name='Gstar_MC_'+ABCDeventhandling+'_'+ABCDversion+radi+'_'+WPs

if doBR:
    name=name+'_'+BR_name
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
##plotselection="N_packedPatJetsAK8PFCHSSoftDrop>=2&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200&&Evt_HT_Jets>850"
#plotselection1="Evt_HT_Jets>850"
#plotselection3="Evt_HT_Jets>1000"
##plotselection1=""
#plotselection2="(N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 && Evt_HT_Jets>850) "





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


#plotselection_ABCD1_general=  plotselection2 + "&& Zprimes_ABCD"+radi+"_M>0   &&    Ws_ABCD1_t21 <  0.6    &&    100 < Tops_ABCD1_MSD     &&    Tops_ABCD1_MSD  < 210  "
#plotselection_ABCD1_general =  plotselection2 + "&& Zprimes_ABCD"+radi+"_M>0   &&    70 < Ws_ABCD1_MSD  &&   Ws_ABCD1_MSD < 100     &&    100 < Tops_ABCD1_MSD     &&    Tops_ABCD1_MSD  < 210   "
#plotselection_ABCD2_general =  plotselection2 + "&& Zprimes_ABCD"+radi+"_M>0   &&    70 < Ws_ABCD1_MSD  &&   Ws_ABCD1_MSD < 100     &&     Tops_ABCD1_t32 < 0.86   "
#plotselection_ABCD1_general_0 =  plotselection2 + "&& Zprimes_ABCD"+radi+"_M[0]>0   &&    Ws_ABCD1_t21[0] >  0.6    &&    100 < Tops_ABCD1_MSD[0]     &&    Tops_ABCD1_MSD[0]  < 210   "
#plotselection_ABCD1_general_0 =   plotselection2 + "&& Zprimes_ABCD"+radi+"_M[0]>0   &&    70 < Ws_ABCD1_MSD[0]  &&   Ws_ABCD1_MSD[0] < 100     &&    100 < Tops_ABCD1_MSD[0]     &&    Tops_ABCD1_MSD[0]  < 210   "

#plotselection_ABCD1_general_alt_notopbtag =  plotselection2 + " && Zprimes_ABCD1_masscorrnotopbtag_M>0 && 70 < Ws_ABCD1_masscorrnotopbtag_MSD && Ws_ABCD1_masscorrnotopbtag_MSD < 100 && Tops_ABCD1_masscorrnotopbtag_t32<0.86 "
#plotselection_ABCD1_general_alt_withtopbtag =  plotselection2 + " && Zprimes_ABCD1_masscorrwithtopbtag_M>0 && 70 < Ws_ABCD1_masscorrwithtopbtag_MSD && Ws_ABCD1_masscorrwithtopbtag_MSD < 100 && Tops_ABCD1_masscorrwithtopbtag_t32<0.86 "




plots=[

   


    ##doing only first element
    ##beta (tau21)
    ## no topsubbtag
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatA_notopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatB_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatC_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatD_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatE_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatF_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatG_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_notopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatH_notopbtag" + " && " +    plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2_anti+ " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,
    
    ## with topsubbtag
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatA_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatB_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatC_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatD_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatE_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatF_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatG_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    #Plot(ROOT.TH1F("ABCD1_withtopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD1_CatID==ABCD1_CatH_withtopbtag" + " && " + plotselection_ABCD1_general + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,
    
    ##inclusive
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD1_CatID==ABCD1_CatA_withtopbtag) || ABCD1_CatID==ABCD1_CatA_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD1_CatID==ABCD1_CatB_withtopbtag) || ABCD1_CatID==ABCD1_CatB_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD1_CatID==ABCD1_CatC_withtopbtag) || ABCD1_CatID==ABCD1_CatC_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD1_CatID==ABCD1_CatD_withtopbtag) || ABCD1_CatID==ABCD1_CatD_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    #Plot(ROOT.TH1F("ABCD1_inclusive_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD1_CatID==ABCD1_CatE_withtopbtag) || ABCD1_CatID==ABCD1_CatE_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD1_CatID==ABCD1_CatF_withtopbtag) || ABCD1_CatID==ABCD1_CatF_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD1_CatID==ABCD1_CatG_withtopbtag) || ABCD1_CatID==ABCD1_CatG_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    #Plot(ROOT.TH1F("ABCD1_inclusive_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD1_CatID==ABCD1_CatH_withtopbtag) || ABCD1_CatID==ABCD1_CatH_notopbtag)" + " && " + plotselection_ABCD1_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,


#N_Gen_ZPrimes

    #Plot(ROOT.TH1F( "N_Gen_ZPrimes" ,"N_Gen_ZPrimes" ,3,0,3),"N_Gen_ZPrimes", "", "1 btag"),


    #ABCD
    #no topbtag
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatA_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatB_Zprime_M" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatB_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatC_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatD_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatE_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatF_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatG_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3  + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatH_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag") ,

    #withtopsubbtag
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatA_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatB_Zprime_M" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatB_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatC_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2_anti + "&& " + cut1  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatD_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1  ,"2 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatE_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1_anti  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatF_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1_anti  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatG_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3  + "&&" + cut2_anti + "&& " + cut1_anti  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatH_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1_anti  ,"2 btag") ,



    
#############ABCD JetmassScaleUp###########################
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatA_notopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassScaleUp, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatB_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatB_notopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassScaleUp  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatC_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatC_notopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassScaleUp  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatD_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatD_notopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassScaleUp  ,"1 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatE_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatE_notopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassScaleUp  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatF_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatF_notopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassScaleUp  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatG_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatG_notopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3  + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassScaleUp  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatH_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatH_notopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassScaleUp  ,"1 btag") ,

    #withtopsubbtag
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatA_withtopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassScaleUp, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatB_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatB_withtopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassScaleUp  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatC_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatC_withtopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassScaleUp  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatD_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatD_withtopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassScaleUp  ,"2 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatE_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatE_withtopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassScaleUp  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatF_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatF_withtopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassScaleUp  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatG_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatG_withtopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3  + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassScaleUp  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatH_Zprime_M_JetmassScaleUp" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleUp==ABCD_CatH_withtopbtag" + " && " + generalselection_JetMassScaleUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassScaleUp  ,"2 btag") ,
    
    
#############ABCD JetmassScaleDown###########################
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatA_notopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassScaleDown, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatB_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatB_notopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassScaleDown  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatC_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatC_notopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassScaleDown  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatD_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatD_notopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassScaleDown  ,"1 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatE_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatE_notopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassScaleDown  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatF_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatF_notopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassScaleDown  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatG_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatG_notopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3  + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassScaleDown  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatH_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatH_notopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassScaleDown  ,"1 btag") ,

    #withtopsubbtag
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatA_withtopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassScaleDown, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatB_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatB_withtopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassScaleDown  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatC_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatC_withtopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassScaleDown  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatD_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatD_withtopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassScaleDown  ,"2 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatE_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatE_withtopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassScaleDown  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatF_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatF_withtopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassScaleDown  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatG_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatG_withtopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3  + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassScaleDown  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatH_Zprime_M_JetmassScaleDown" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassScaleDown==ABCD_CatH_withtopbtag" + " && " + generalselection_JetMassScaleDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassScaleDown  ,"2 btag") ,
    
        
    
#############ABCD JetmassResUp###########################
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatA_notopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassResUp, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatB_Zprime_M_JetmassResUp" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatB_notopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassResUp  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatC_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatC_notopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassResUp  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatD_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatD_notopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassResUp  ,"1 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatE_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatE_notopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassResUp  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatF_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatF_notopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassResUp  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatG_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatG_notopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3  + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassResUp  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatH_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatH_notopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassResUp  ,"1 btag") ,

    #withtopsubbtag
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatA_withtopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassResUp, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatB_Zprime_M_JetmassResUp" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatB_withtopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassResUp  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatC_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatC_withtopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassResUp  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatD_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatD_withtopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassResUp  ,"2 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatE_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatE_withtopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassResUp  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatF_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatF_withtopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassResUp  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatG_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatG_withtopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3  + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassResUp  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatH_Zprime_M_JetmassResUp" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResUp==ABCD_CatH_withtopbtag" + " && " + generalselection_JetMassResUp + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassResUp  ,"2 btag") ,
    
    
#############ABCD JetmassResDown###########################
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatA_notopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassResDown, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatB_Zprime_M_JetmassResDown" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatB_notopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassResDown  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatC_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatC_notopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassResDown  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatD_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatD_notopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassResDown  ,"1 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatE_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatE_notopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassResDown  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatF_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatF_notopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassResDown  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatG_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatG_notopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3  + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassResDown  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatH_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatH_notopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassResDown  ,"1 btag") ,

    #withtopsubbtag
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatA_withtopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassResDown, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatB_Zprime_M_JetmassResDown" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatB_withtopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_JetMassResDown  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatC_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatC_withtopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassResDown  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatD_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatD_withtopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_JetMassResDown  ,"2 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatE_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatE_withtopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassResDown  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatF_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatF_withtopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + plotselection_W_MSD_anti_JetMassResDown  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatG_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatG_withtopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3  + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassResDown  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatH_Zprime_M_JetmassResDown" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID_JetMassResDown==ABCD_CatH_withtopbtag" + " && " + generalselection_JetMassResDown + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + plotselection_W_MSD_anti_JetMassResDown  ,"2 btag") ,
    
        
   




    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Zprime_eff" ,"m(Z') in GeV, CatA " ,1,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatA_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Zprime_eff" ,"m(Z') in GeV, CatA " ,1,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatA_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "1 btag"),
    
    Plot(ROOT.TH1F( "N_Gen_ZPrimes" ,"N_Gen_ZPrimes" ,1,0,5000),"N_Gen_TPrimesandTPrimebars", "N_Gen_TPrimesandTPrimebars>0", ""),

    ##inclusive
    #Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatA_withtopbtag) || ABCD_CatID==ABCD_CatA_notopbtag)" + " && " + generalselection + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatB_withtopbtag) || ABCD_CatID==ABCD_CatB_notopbtag)" + " && " + generalselection + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1  ,"1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatC_withtopbtag) || ABCD_CatID==ABCD_CatC_notopbtag)" + " && " + generalselection + " && " + cut3 + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatD_withtopbtag) || ABCD_CatID==ABCD_CatD_notopbtag)" + " && " + generalselection + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),

    #Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatE_withtopbtag) || ABCD_CatID==ABCD_CatE_notopbtag)" + " && " + generalselection + " && " + cut3 + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatF_withtopbtag) || ABCD_CatID==ABCD_CatF_notopbtag)" + " && " + generalselection + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatG_withtopbtag) || ABCD_CatID==ABCD_CatG_notopbtag)" + " && " + generalselection + " && " + cut3  + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_inclusive_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "((ABCD_CatID==ABCD_CatH_withtopbtag) || ABCD_CatID==ABCD_CatH_notopbtag)" + " && " + generalselection + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag") ,

###Tprime
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
OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_M"):plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_eff") +1 ] = len(OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_M"):plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_eff") + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'



#print allweightsystnames
#print allsystweights

#print name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM,systweightsbasic+systweightsMadgraphbantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weightsystnamesPythia8bantiZprimeM,systweightsPythia8bantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
#print allweightsystnames
#print allsystweights, "OK"
#raw_input()

outputpath=plotParallel(name,2000000,plots,SignalSamples+systsamples,[""],["1"],allweightsystnames,allsystweights,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList,otherSystNames)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)


#rebinnedHistosExist=False
rebinnedHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned.root'
#rebinnedandaddedHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_added.root'
rebinnedBRHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_'+BR_name+'.root'

rebinnedandaddedBRHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_'+BR_name+'_added.root'


allweightsystnames=allweightsystnames+JECsystnames
print allweightsystnames

print 'debug filesave 1 ', rebinnedHistoPath[:-5]
#print 'debug filesave 2 ', rebinnedandaddedHistoPath[:-5]
print 'debug filesave 3 ', rebinnedandaddedBRHistoPath[:-5]
print 'debug filesave 4 ', rebinnedBRHistoPath[:-5]



#if not os.path.isfile(rebinnedHistoPath):


    #lllSignal=createLLL_fromSuperHistoFileSyst(outputpath,SignalSamples,plots,allweightsystnames)
    #lllBackground=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,allweightsystnames)
    #lllData_Madgraph=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,allweightsystnames)
    ##lllData_Pythia=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,allweightsystnames)
    #forcombine=True
    #lllSignal=rebintovarbinsLLL(lllSignal,name,True,True,False,forcombine)
    #lllBackground=rebintovarbinsLLL(lllBackground,name,True,True,False,forcombine)
    #lllData_Madgraph=rebintovarbinsLLL(lllData_Madgraph,name,True,True,False,forcombine)
    
    #llltofile=lllSignal+lllBackground+lllData_Madgraph
    #writeLLLtoFile(llltofile,rebinnedHistoPath[:-5])
    ##lllData_Pythia=rebintovarbinsLLL(lllData_Pythia,name,False,True,False)
    #addLLLtoLLL(lllData_Madgraph,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),name,False,allweightsystnames,True)
    #addedllltofile=lllData_Madgraph+lllBackground+lllSignal
    #writeLLLtoFile(addedllltofile,rebinnedandaddedHistoPath[:-5])
    
    
    #createBRLLL(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_"+BR_name+""):SignalSampleNames.index("SigZprime25001500_"+BR_name+"")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_tWb"):SignalSampleNames.index("SigZprime25001500_tWb")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_ttZ"):SignalSampleNames.index("SigZprime25001500_ttZ")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_ttH"):SignalSampleNames.index("SigZprime25001500_ttH")+1]),BR[0],BR[1],BR[2])
    #createBRLLL(transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_"+BR_name+"_1pb"):BackgroundSampleNames.index("SC_Zprime25001500_"+BR_name+"_1pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_tWb_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_tWb_1_0pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_ttZ_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttZ_1_0pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_ttH_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttH_1_0pb")+1]),BR[0],BR[1],BR[2])
    #createBRLLL(transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_"+BR_name+"_1pb"):DataSampleNames.index("DATA_Zprime25001500_"+BR_name+"_1pb")+1]),transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_tWb_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_tWb_1_0pb")+1]),transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_ttZ_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_ttZ_1_0pb")+1]),transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_ttH_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_ttH_1_0pb")+1]),BR[0],BR[1],BR[2])
    
    #BRllltofile=lllData_Madgraph+lllBackground+lllSignal
    #writeLLLtoFile(BRllltofile,rebinnedandaddedBRHistoPath[:-5])    
    
#else:
  #if not os.path.isfile(rebinnedandaddedHistoPath):

    #lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,SignalSamples,plots,allweightsystnames)
    #lllBackground=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,BackgroundSamples,plots,allweightsystnames)
    #lllData_Madgraph=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,DataSamples,plots,allweightsystnames) 
    
    #llltofile=lllSignal+lllBackground+lllData_Madgraph
    #writeLLLtoFile(llltofile,rebinnedHistoPath[:-5])
    
    #addLLLtoLLL(lllData_Madgraph,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),name,False,allweightsystnames,True)
    #addedllltofile=lllData_Madgraph+lllBackground+lllSignal
    #writeLLLtoFile(addedllltofile,rebinnedandaddedHistoPath[:-5])
    
   
    #createBRLLL(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_"+BR_name+""):SignalSampleNames.index("SigZprime25001500_"+BR_name+"")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_tWb"):SignalSampleNames.index("SigZprime25001500_tWb")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_ttZ"):SignalSampleNames.index("SigZprime25001500_ttZ")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_ttH"):SignalSampleNames.index("SigZprime25001500_ttH")+1]),BR[0],BR[1],BR[2])
    
    #createBRLLL(transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_"+BR_name+"_1pb"):BackgroundSampleNames.index("SC_Zprime25001500_"+BR_name+"_1pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_tWb_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_tWb_1_0pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_ttZ_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttZ_1_0pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_ttH_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttH_1_0pb")+1]),BR[0],BR[1],BR[2])
    
    #createBRLLL(transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_"+BR_name+"_1pb"):DataSampleNames.index("DATA_Zprime25001500_"+BR_name+"_1pb")+1]),transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_tWb_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_tWb_1_0pb")+1]),transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_ttZ_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_ttZ_1_0pb")+1]),transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_ttH_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_ttH_1_0pb")+1]),BR[0],BR[1],BR[2])
    

    
    #BRllltofile=lllData_Madgraph+lllBackground+lllSignal
    #writeLLLtoFile(BRllltofile,rebinnedandaddedBRHistoPath[:-5])       
  #else:
      
    #if not os.path.isfile(rebinnedandaddedBRHistoPath):
        ##print "check here"
        ##print SignalSampleNames
        ##print allweightsystnames
        ##raw_input()
        #lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedandaddedHistoPath,SignalSamples,plots,allweightsystnames)
        #lllBackground=createLLL_fromSuperHistoFileSyst(rebinnedandaddedHistoPath,BackgroundSamples,plots,allweightsystnames)
        #lllData_Madgraph=createLLL_fromSuperHistoFileSyst(rebinnedandaddedHistoPath,DataSamples,plots,allweightsystnames) 
        ##print lllBackground
        ##for ll in lllBackground:
            ##for l in ll:
                ##for h in l: 
                    ##print h, "   ", h.Integral()
        ###raw_input()
        ##print lllData_Madgraph
        ##for ll in lllData_Madgraph:
            ##for l in ll:
                ##for h in l: 
                    ##print h, "   ", h.Integral()
        ###raw_input()
        
        #createBRLLL(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_"+BR_name+""):SignalSampleNames.index("SigZprime25001500_"+BR_name+"")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_tWb"):SignalSampleNames.index("SigZprime25001500_tWb")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_ttZ"):SignalSampleNames.index("SigZprime25001500_ttZ")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_ttH"):SignalSampleNames.index("SigZprime25001500_ttH")+1]),BR[0],BR[1],BR[2])
        
        #createBRLLL(transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_"+BR_name+"_1pb"):BackgroundSampleNames.index("SC_Zprime25001500_"+BR_name+"_1pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_tWb_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_tWb_1_0pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_ttZ_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttZ_1_0pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_ttH_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttH_1_0pb")+1]),BR[0],BR[1],BR[2])
        
        #createBRLLL(transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_"+BR_name+"_1pb"):DataSampleNames.index("DATA_Zprime25001500_"+BR_name+"_1pb")+1]),transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_tWb_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_tWb_1_0pb")+1]),transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_ttZ_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_ttZ_1_0pb")+1]),transposeLOL(transposeLOL(lllData_Madgraph)[DataSampleNames.index("DATA_Zprime15001200_ttH_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_ttH_1_0pb")+1]),BR[0],BR[1],BR[2])
        ##print lllBackground
        ##for ll in lllBackground:
            ##for l in ll:
                ##for h in l: 
                    ##print h, "   ", h.Integral()
        ###raw_input()
        ##print lllData_Madgraph
        ##for ll in lllData_Madgraph:
            ##for l in ll:
                ##for h in l: 
                    ##print h, "   ", h.Integral()
        ##raw_input()
        #BRllltofile=lllData_Madgraph+lllBackground+lllSignal
        #writeLLLtoFile(BRllltofile,rebinnedandaddedBRHistoPath[:-5])

    
    
    #else:
        #lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedandaddedBRHistoPath,SignalSamples,plots,allweightsystnames)
        #lllBackground=createLLL_fromSuperHistoFileSyst(rebinnedandaddedBRHistoPath,BackgroundSamples,plots,allweightsystnames)
        #lllData_Madgraph=createLLL_fromSuperHistoFileSyst(rebinnedandaddedBRHistoPath,DataSamples,plots,allweightsystnames)
        
        ##lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedandaddedHistoPath,SignalSamples,plots,allweightsystnames)
        ##lllBackground=createLLL_fromSuperHistoFileSyst(rebinnedandaddedHistoPath,BackgroundSamples,plots,allweightsystnames)
        ##lllData_Madgraph=createLLL_fromSuperHistoFileSyst(rebinnedandaddedHistoPath,DataSamples,plots,allweightsystnames) 







if not os.path.isfile(rebinnedHistoPath):


    lllSignal=createLLL_fromSuperHistoFileSyst(outputpath,SignalSamples,plots,allweightsystnames)
    
    print lllSignal
    #raw_input()

    create_envelopes_new(lllSignal)
    renormshapestonom(lllSignal)
    
    forcombine=True
    lllSignal=rebintovarbinsLLL(lllSignal,name,True,True,False,forcombine)
    
    llltofile=lllSignal
    writeLLLtoFile(llltofile,rebinnedHistoPath[:-5])

    createBRLLL(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_"+BR_name+"Nar"):SignalSampleNames.index("SigGstar40003000_"+BR_name+"Nar")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_tWb"+"Nar"):SignalSampleNames.index("SigGstar40003000_tWb"+"Nar")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_ttZ"+"Nar"):SignalSampleNames.index("SigGstar40003000_ttZ"+"Nar")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_ttH"+"Nar"):SignalSampleNames.index("SigGstar40003000_ttH"+"Nar")+1]),BR[0],BR[1],BR[2])
    
    createBRLLL(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_"+BR_name+"Wid"):SignalSampleNames.index("SigGstar40003000_"+BR_name+"Wid")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_tWb"+"Wid"):SignalSampleNames.index("SigGstar40003000_tWb"+"Wid")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_ttZ"+"Wid"):SignalSampleNames.index("SigGstar40003000_ttZ"+"Wid")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_ttH"+"Wid"):SignalSampleNames.index("SigGstar40003000_ttH"+"Wid")+1]),BR[0],BR[1],BR[2])  ,
    
    
    BRllltofile=lllSignal
    writeLLLtoFile(BRllltofile,rebinnedBRHistoPath[:-5])     

   
    
else:
    if not os.path.isfile(rebinnedBRHistoPath):
        
        
        
        lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,SignalSamples,plots,allweightsystnames)
        renormshapestonom(lllSignal)
        print lllSignal
        #raw_input()        
        

        createBRLLL(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_"+BR_name+"Nar"):SignalSampleNames.index("SigGstar40003000_"+BR_name+"Nar")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_tWb"+"Nar"):SignalSampleNames.index("SigGstar40003000_tWb"+"Nar")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_ttZ"+"Nar"):SignalSampleNames.index("SigGstar40003000_ttZ"+"Nar")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_ttH"+"Nar"):SignalSampleNames.index("SigGstar40003000_ttH"+"Nar")+1]),BR[0],BR[1],BR[2])
        
        createBRLLL(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_"+BR_name+"Wid"):SignalSampleNames.index("SigGstar40003000_"+BR_name+"Wid")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_tWb"+"Wid"):SignalSampleNames.index("SigGstar40003000_tWb"+"Wid")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_ttZ"+"Wid"):SignalSampleNames.index("SigGstar40003000_ttZ"+"Wid")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigGstar1500800_ttH"+"Wid"):SignalSampleNames.index("SigGstar40003000_ttH"+"Wid")+1]),BR[0],BR[1],BR[2])  

        BRllltofile=lllSignal
        writeLLLtoFile(BRllltofile,rebinnedBRHistoPath[:-5])

    
    else:
        
        
        if not os.path.isfile(rebinnedandaddedBRHistoPath):
            
            
              
            lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedBRHistoPath,SignalSamples,plots,allweightsystnames)
            renormshapestonom(lllSignal)
            print lllSignal
            #raw_input()            
        else:

            
            lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedandaddedBRHistoPath,SignalSamples,plots,allweightsystnames)
            renormshapestonom(lllSignal)

            print lllSignal
            #raw_input()  






#def createBRLLL(final_lllBR,lll1,lll2,lll3, c1=1.0, c2=1.0, c2=1.0):


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

#doABCD=True

#if doABCD:

  #if not doBR:
    #for dataname, signalname, SC_name in zip(DataSampleNames,SignalSampleNames+[SignalSampleNames[0]],BackgroundSampleNames[BackgroundSampleNames.index('SC_Zprime15001200_tWb_8_6pb'):BackgroundSampleNames.index('SC_none')+1]):
    ##for dataname, signalname, SC_name in zip([DataSampleNames[DataSampleNames.index('DATA_noSignal')]],[SignalSampleNames[0]],[BackgroundSampleNames[BackgroundSampleNames.index('SC_none')]]):
        #for QCDname in ['QCDMadgraph']:
            ##for ABCDversion in ['ABCD1','ABCD2']:
            #for ABCDversion in [ABCDversion]:
                #for Category in ['notopbtag','withtopbtag']:#,'inclusive']:
          
#################Final with ABCD only ###################
##################with Syst notoptag #####################R
                    #if QCDname is 'QCDMadgraph':
                        #for ABCD_syst,ABCD_syst_name in zip([False,True],['Rateonly','RateAndShape']):
                        ##for ABCD_syst,ABCD_syst_name in zip([True],['RateAndShape']):
                            #ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(lllData_Madgraph,lllBackground,lllSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,dataname,SC_name,signalname,ABCDversion+'_'+Category+'_CatA', ABCDversion+'_'+Category+'_CatB', ABCDversion+'_'+Category+'_CatC', ABCDversion+'_'+Category+'_CatD',QCDname, ABCDversion+'/fancy_'+ABCDversion+'_'+ABCDeventhandling+'_'+WPs+'_'+ABCD_syst_name,ABCD_syst)



  #else:
    #for dataname, signalname, SC_name in zip(DataSampleNames,SignalSampleNames+[SignalSampleNames[0]],BackgroundSampleNames[BackgroundSampleNames.index('SC_Zprime15001200_tWb_1_0pb'):BackgroundSampleNames.index('SC_none')+1]):
    ##for dataname, signalname, SC_name in zip([DataSampleNames[DataSampleNames.index('DATA_noSignal')]],[SignalSampleNames[0]],[BackgroundSampleNames[BackgroundSampleNames.index('SC_none')]]):
        #for QCDname in ['QCDMadgraph']:
            ##for ABCDversion in ['ABCD1','ABCD2']:
            #for ABCDversion in [ABCDversion]:
                #for Category in ['notopbtag','withtopbtag']:#,'inclusive']:
          
################Final with ABCD only ###################
#################with Syst notoptag #####################R
                    #if QCDname is 'QCDMadgraph':
                        #for ABCD_syst,ABCD_syst_name in zip([False,True],['Rateonly','RateAndShape']):
                        ##for ABCD_syst,ABCD_syst_name in zip([True],['RateAndShape']):
                            #ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(lllData_Madgraph,lllBackground,lllSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,dataname,SC_name,signalname,ABCDversion+'_'+Category+'_CatA', ABCDversion+'_'+Category+'_CatB', ABCDversion+'_'+Category+'_CatC', ABCDversion+'_'+Category+'_CatD',QCDname, ABCDversion+'/fancy_'+ABCDversion+'_'+ABCDeventhandling+'_'+WPs+'_'+ABCD_syst_name,ABCD_syst)
print "signal efficiency in %"

text=""




for l1,l2,l3,signame in zip(lllSignal[plotnames.index(ABCDversion + "_withtopbtag_CatA_Zprime_eff")],lllSignal[plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_eff")],lllSignal[plotnames.index("N_Gen_ZPrimes")], SignalSampleNames):
    #print "allweightsystnames.index('_'+ABCDversion+'_nominal')", allweightsystnames.index('_'+ABCDversion+'_nominal')
    
    #print "l1", l1
    #print "l2", l2
    #print "l3", l3
    if len(l1)>0 and len(l2)>0 and len(l3)>0:
        if l1[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()>0 and l2[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()>0 and l3[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()>0:
            
            if "ttH" in signame:
                decay="HT"
            if "ttZ" in signame:
                decay="ZT"                
            if "tWb" in signame:
                decay="WB"
                
            if "Wid" in signame:
                width="WID"
            if "Nar" in signame:
                width="Nar"
            
            mZ=signame[8:12]
            mT=signame[12:15]
                
            filename=glob.glob("/nfs/dust/cms/user/skudella/processed_MC/scripts/cutflow/*"+decay+"*Zp"+mZ+width+"*"+mT+"*.txt")
            #print filename
            f=open(filename[0],"r")
            for line in f:
                if ("0 : all : " in line):
                    first=re.findall("\d+\.\d+",line)
                if ("16 : >=3 jets >=0 tags : " in line):
                    last=re.findall("\d+\.\d+",line)
                    
            taggeff=float(last[0])/float(first[0])
            #print "taggeff",taggeff
          
            eff2b=l1[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()/l3[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()*100.0*taggeff
            eff1b=l2[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()/l3[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()*100.0*taggeff
            
            eff2b_unc= (1.0/math.sqrt(l1[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral())+1.0/math.sqrt(240000))*eff2b
            eff1b_unc= (1.0/math.sqrt(l2[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral())+1.0/math.sqrt(240000))*eff1b
            
            #print 1.0/math.sqrt(l1[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()), "  ", 1.0/math.sqrt(float(first[0])), "  ", first[0]
          
            roundigit0=0
            roundlimit0=eff2b
            for i in range(10):
                if roundlimit0<1.0:
                    roundlimit0=roundlimit0*10
                    roundigit0+=1
            
            roundigit1=0
            roundlimit1=eff2b_unc
            for i in range(10):
                if roundlimit1<1.0:
                    roundlimit1=roundlimit1*10
                    roundigit1+=1
                    
            roundigit2=0
            roundlimit2=eff1b
            for i in range(10):
                if roundlimit2<1.0:
                    roundlimit2=roundlimit2*10
                    roundigit2+=1
                    
                    
            roundigit3=0
            roundigit32=0
            roundlimit3=eff1b_unc
            for i in range(10):
                if roundlimit3<1.0:
                    roundlimit3=roundlimit3*10
                    roundigit3+=1
         
            if roundigit1<2.0:
                roundigit12=roundigit1+1
            else:
                roundigit12=roundigit1         
         
            if roundlimit3<2.0:
                roundigit32=roundigit3+1
            else:
                roundigit32=roundigit3
            
            print signame, " 2 b-tag:", str(round(eff2b,roundigit1))," pm ",str(round(eff2b_unc,roundigit12)) ,"   1 b-tag:", str(round(eff1b,roundigit3))," pm ",str(round(eff1b_unc,roundigit32)) 
            text=text+signame+""" & """+ str(round(eff2b,roundigit1))+"""\pm """+ str(round(eff2b_unc,roundigit12)) + """ & """+ str(round(eff1b,roundigit3))+"""\pm """+ str(round(eff1b_unc,roundigit32))+"""        
"""
        else:
            print "l1",l1[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral(),"l2",l2[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral(),"l3",l3[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()
            print signame, " 2 b-tag: empty   1 b-tag: empty"
            text=text+signame+"""& empty & empty"""+"""      
"""            
    else:
        print signame, " 2 b-tag: buggy  1 b-tag: buggy"
        text=text+signame+"""& buggy & buggy"""+"""        
"""


f=open("signal efficiency_Gstar.txt",'w')
f.write(text)
f.close()
