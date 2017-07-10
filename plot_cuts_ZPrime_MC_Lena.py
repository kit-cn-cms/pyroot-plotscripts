# book plots
plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
plotselection1="Evt_HT>1000"
plotselection2="N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 && Evt_HT>1000 "
#plotselection2=plotselection1


jetradius_top="12"
jetradius_W="8"
jetradius_bottom="4"

radi=''

if(jetradius_top=="15" and jetradius_W=="8" and jetradius_bottom=="4"):
    radi='_tAK'+jetradius_top+"WAK"+jetradius_W+"bAK"+jetradius_bottom
    #plotselection2= "Ws_ABCD"+radi+"_Pt[ > 200" + " && " + "Tops_ABCD"+radi+"_Pt > 200"+" && Evt_HT>1000 "
    plotselection2=plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200"
    
if(jetradius_top=="15" and jetradius_W=="15" and jetradius_bottom=="4"):
    radi='_tAK'+jetradius_top+"WAK"+jetradius_W+"bAK"+jetradius_bottom
    #plotselection2= "Ws_ABCD"+radi+"_Pt > 200" + " && " + "Tops_ABCD"+radi+"_Pt > 200"+" && Evt_HT>1000 "
    plotselection2=plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200"

if(jetradius_top=="12" and jetradius_W=="8" and jetradius_bottom=="4"):
    radi='_tAK'+jetradius_top+"WAK"+jetradius_W+"bAK"+jetradius_bottom
    #plotselection2= "Ws_ABCD"+radi+"_Pt > 200" + " && " + "Tops_ABCD"+radi+"_Pt > 200"+" && Evt_HT>1000 "
    plotselection2=plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200"

if(jetradius_top=="12" and jetradius_W=="8" and jetradius_bottom=="4"):
    radi='_tAK'+jetradius_top+"WAK"+jetradius_W+"bAK"+jetradius_bottom
    #plotselection2= "Ws_ABCD"+radi+"_Pt > 200" + " && " + "Tops_ABCD"+radi+"_Pt > 200"+" && Evt_HT>1000 "
    plotselection2=plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200"







topWP='loose'
WWP='loose'
bottomWP='medium'

WPs='tWP'+topWP+'WWP'+WWP+'bWP'+bottomWP
    
#Own Plotselections for ABCD-method
if topWP=='loose':
    plotselection_tau32 = " Tops_ABCD"+radi+"_t32 < 0.86   "
    plotselection_tau32_i = " Tops_ABCD"+radi+"_t32[i] < 0.86   "
    plotselection_tau32_0 = " Tops_ABCD"+radi+"_t32[0] < 0.86   "

if topWP=='medium':
    plotselection_tau32 = " Tops_ABCD"+radi+"_t32 < 0.67   "
    plotselection_tau32_i = " Tops_ABCD"+radi+"_t32[i] < 0.67   "
    plotselection_tau32_0 = " Tops_ABCD"+radi+"_t32[0] < 0.67   "

if WWP=='loose':
    plotselection_W_tau21 = " Ws_ABCD"+radi+"_t21 < 0.6 "
    plotselection_W_tau21_i = " Ws_ABCD"+radi+"_t21[i] < 0.6  "
    plotselection_W_tau21_0 = " Ws_ABCD"+radi+"_t21[0] < 0.6  "

if WWP=='medium':
    plotselection_W_tau21 = " Ws_ABCD"+radi+"_t21 < 0.45"
    plotselection_W_tau21_i = " Ws_ABCD"+radi+"_t21[i] < 0.45  "
    plotselection_W_tau21_0 = " Ws_ABCD"+radi+"_t21[0] < 0.45  "

if bottomWP=='medium':
    plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.8  "    
    plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.8   "
    plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.8   " 

if bottomWP=='tight':
    plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.935  "    
    plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.935   "
    plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.935   " 

plotselection_tau32_anti=" Tops_ABCD"+radi+"_t32 > 0.86   "
plotselection_tau32_anti_i =" Tops_ABCD"+radi+"_t32[i] > 0.86   "
plotselection_tau32_anti_0 =" Tops_ABCD"+radi+"_t32[0] > 0.86   "

plotselection_W_tau21_anti = " Ws_ABCD"+radi+"_t21 > 0.6 "
plotselection_W_tau21_anti_i = " Ws_ABCD"+radi+"_t21[i]  > 0.6 "
plotselection_W_tau21_anti_0 = " Ws_ABCD"+radi+"_t21[0]  > 0.6 "





plotselection_W_MSD =  " (65 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 105) "
plotselection_W_MSD_i =  " (65 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 105) "
plotselection_W_MSD_0 =  " (65 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 105) "
plotselection_W_MSD_anti =  " (65 > Ws_ABCD"+radi+"_MSD  ||   Ws_ABCD"+radi+"_MSD > 105) "
plotselection_W_MSD_anti_i =  " (65 > Ws_ABCD"+radi+"_MSD[i]  ||   Ws_ABCD"+radi+"_MSD[i] > 105) "
plotselection_W_MSD_anti_0 =  " (65 > Ws_ABCD"+radi+"_MSD[0]  ||   Ws_ABCD"+radi+"_MSD[0] > 105) "



plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.46   "
plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.46   "
plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.46   "


plotselection_t_MSD = " (105 < Tops_ABCD"+radi+"_MSD && Tops_ABCD"+radi+"_MSD < 210) "
plotselection_t_MSD_i = " (105 < Tops_ABCD"+radi+"_MSD[i] && Tops_ABCD"+radi+"_MSD[i] < 210) "
plotselection_t_MSD_0 = " (105 < Tops_ABCD"+radi+"_MSD[0] && Tops_ABCD"+radi+"_MSD[0] < 210) "
plotselection_t_MSD_anti = " (105 > Tops_ABCD"+radi+"_MSD || Tops_ABCD"+radi+"_MSD > 210) "
plotselection_t_MSD_anti_i = " (105 > Tops_ABCD"+radi+"_MSD[i] || Tops_ABCD"+radi+"_MSD[i] > 210) "
plotselection_t_MSD_anti_0 = " (105 > Tops_ABCD"+radi+"_MSD[0] || Tops_ABCD"+radi+"_MSD[0] > 210) "


plotselection_topsubjetCSVv2 = " Tops_ABCD"+radi+"_maxsubjetCSVv2 > 0.8 "
plotselection_topsubjetCSVv2_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] > 0.8 "
plotselection_topsubjetCSVv2_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] > 0.8 "

plotselection_topsubjetCSVv2_anti = " Tops_ABCD"+radi+"_maxsubjetCSVv2 < 0.8 "
plotselection_topsubjetCSVv2_anti_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] < 0.8 "
plotselection_topsubjetCSVv2_anti_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] < 0.8 "

plotselection_TprimeMass = " Tprimes_ABCD"+radi+"_M>500 "
plotselection_TprimeMass_i = " Tprimes_ABCD"+radi+"_M[i]>500 "
plotselection_TprimeMass_0 = " Tprimes_ABCD"+radi+"_M[0]>500 "

plotselection_TprimeMass_anti = " Tprimes_ABCD"+radi+"_M<500 "
plotselection_TprimeMass_anti_i = " Tprimes_ABCD"+radi+"_M[i]<500 "
plotselection_TprimeMass_anti_0 = " Tprimes_ABCD"+radi+"_M[0]<500 "


plotselection_W_MSD_one_sided =  " (65 < Ws_ABCD"+radi+"_MSD && Ws_ABCD"+radi+"_MSD < 105)"
plotselection_W_MSD_one_sided_anti =  " (65 > Ws_ABCD"+radi+"_MSD && Ws_ABCD"+radi+"_MSD < 105)"




plotselection_sideband = "Signal_Topfirst_Zprime_M < 0"
plotselection_sideband_withtopbtag = "Signal_withtopbtag_Topfirst_Zprime_M < 0"


#plotselection_ABCD_general=  plotselection1 + "&& Zprimes_ABCD_M>0   &&    Ws_ABCD_t21 <  0.6    &&    105 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210  "
plotselection_ABCD_general_beta =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>0 " + "  &&  "+ plotselection_TprimeMass + "  &&  "+ plotselection_W_MSD + " && " + plotselection_t_MSD
plotselection_ABCD_general_beta_0 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "   &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_t_MSD_0
plotselection_ABCD_general_beta_i =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_W_MSD_i + " && " + plotselection_t_MSD_i

plotselection_ABCD_general_beta2 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_TprimeMass + "  &&  "+ plotselection_W_MSD + " && " + plotselection_tau32
plotselection_ABCD_general_beta2_0 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_tau32_0
plotselection_ABCD_general_beta2_i =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_W_MSD_i + " && " + plotselection_tau32_i

plotselection_ABCD_general_beta3 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_TprimeMass + "  &&  "+ plotselection_t_MSD + " && " + plotselection_tau32
plotselection_ABCD_general_beta3_0 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0
plotselection_ABCD_general_beta3_i =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_t_MSD_i + " && " + plotselection_tau32_i

plotselection_ABCD_general_beta4 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_W_MSD + "  &&  "+ plotselection_t_MSD + " && " + plotselection_tau32
plotselection_ABCD_general_beta4_0 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_W_MSD_0 + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0
plotselection_ABCD_general_beta4_i =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_W_MSD_i + "  &&  "+ plotselection_t_MSD_i + " && " + plotselection_tau32_i

plotselection_ABCD_general_beta5 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_t_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass
plotselection_ABCD_general_beta5_0 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0
plotselection_ABCD_general_beta5_i =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_t_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i

plotselection_ABCD_general_beta6 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_W_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass
plotselection_ABCD_general_beta6_0 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_W_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0
plotselection_ABCD_general_beta6_i =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_W_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i

plotselection_ABCD_general_beta7 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_W_tau21 + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass
plotselection_ABCD_general_beta7_0 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_W_tau21_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0
plotselection_ABCD_general_beta7_i =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_W_tau21_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i


##plotselection_ABCD_general_i =  plotselection1 + "&& Zprimes_ABCD"+radi+"_M[i]>0   &&    Ws_ABCD"+radi+"_t21[i] >  0.6    &&    105 < Tops_ABCD"+radi+"_MSD[i]     &&    Tops_ABCD"+radi+"_MSD[i]  < 210   "
#plotselection_ABCD_general_beta_i =   "Zprimes_ABCD"+radi+"_M[i]>0   &&    65 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 105     &&    105 < Tops_ABCD"+radi+"_MSD[i]     &&    Tops_ABCD"+radi+"_MSD[i]  < 210   "
#plotselection_ABCD_general_beta2_i =  "Zprimes_ABCD"+radi+"_M[i]>0   &&    65 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 105     && "+ plotselection_tau32_i
#plotselection_ABCD_general_beta_0 =   "Zprimes_ABCD"+radi+"_M[0]>0   &&    65 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 105     &&    105 < Tops_ABCD"+radi+"_MSD[0]     &&    Tops_ABCD"+radi+"_MSD[0]  < 210   "
#plotselection_ABCD_general_beta2_0 =  "Zprimes_ABCD"+radi+"_M[0]>0   &&    65 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 105     && "+ plotselection_tau32_0


plotselection_ABCD_general_alt_notopbtag =  plotselection1 + " && Zprimes_ABCD_masscorrnotopbtag_M>0 && 65 < Ws_ABCD_masscorrnotopbtag_MSD && Ws_ABCD_masscorrnotopbtag_MSD < 105 && Tops_ABCD_masscorrnotopbtag_t32<0.86 "
plotselection_ABCD_general_alt_withtopbtag =  plotselection1 + " && Zprimes_ABCD_masscorrwithtopbtag_M>0 && 65 < Ws_ABCD_masscorrwithtopbtag_MSD && Ws_ABCD_masscorrwithtopbtag_MSD < 105 && Tops_ABCD_masscorrwithtopbtag_t32<0.86 "

