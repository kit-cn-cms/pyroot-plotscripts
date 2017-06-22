# book plots
plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
plotselection1="Evt_HT>850"
plotselection2="N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 && Evt_HT>850 "

topWP='medium'
WWP='medium'
bottomWP=''

    
#Own Plotselections for ABCD-method
if topWP=='loose':
    plotselection_tau32 = " Tops_ABCD_t32 < 0.86   "
    plotselection_tau32_i = " Tops_ABCD_t32[i] < 0.86   "
if topWP=='medium':
    plotselection_tau32 = " Tops_ABCD_t32 < 0.67   "
    plotselection_tau32_i = " Tops_ABCD_t32[i] < 0.67   "
    
if WWP=='loose':
    plotselection_W_tau21 = " Ws_ABCD_t21 < 0.6 "
    plotselection_W_tau21_i = " Ws_ABCD_t21[i] < 0.6  "
if WWP=='medium':
    plotselection_W_tau21 = " Ws_ABCD_t21 < 0.45"
    plotselection_W_tau21_i = " Ws_ABCD_t21[i] < 0.45  "

plotselection_W_MSD =  " (65 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 105) "
plotselection_B_CSV = "  Bottoms_ABCD_CSV > 0.8  "    
plotselection_t_MSD = " (105 < Tops_ABCD_MSD && Tops_ABCD_MSD < 210) "
plotselection_topsubjetCSVv2 = " Tops_ABCD_maxsubjetCSVv2 > 0.8 "
plotselection_W_MSD_i =  " (65 < Ws_ABCD_MSD[i]  &&   Ws_ABCD_MSD[i] < 105) "
plotselection_B_CSV_i = "  Bottoms_ABCD_CSV[i] > 0.8   "
plotselection_topsubjetCSVv2_i = " Tops_ABCD_maxsubjetCSVv2[i] > 0.8 "


plotselection_tau32_anti=" Tops_ABCD_t32 > 0.86   "
plotselection_W_MSD_anti =  " (65 > Ws_ABCD_MSD  ||   Ws_ABCD_MSD > 105) "
plotselection_B_CSV_anti = "  Bottoms_ABCD_CSV < 0.46   "
plotselection_W_tau21_anti = " Ws_ABCD_t21 > 0.6 "
plotselection_t_MSD_anti = " (105 > Tops_ABCD_MSD || Tops_ABCD_MSD > 210) "
plotselection_topsubjetCSVv2_anti = " Tops_ABCD_maxsubjetCSVv2 < 0.8 "

plotselection_tau32_anti_i =" Tops_ABCD_t32[i] > 0.86   "
plotselection_W_MSD_anti_i =  " (65 > Ws_ABCD_MSD[i]  ||   Ws_ABCD_MSD[i] > 105) "
plotselection_B_CSV_anti_i = "  Bottoms_ABCD_CSV[i] < 0.46   "
plotselection_W_tau21_anti_i = " Ws_ABCD_t21[i]  > 0.6 "
plotselection_topsubjetCSVv2_anti_i = " Tops_ABCD_maxsubjetCSVv2[i] < 0.8 "




plotselection_W_MSD_one_sided =  " (65 < Ws_ABCD_MSD && Ws_ABCD_MSD < 105)"
plotselection_W_MSD_one_sided_anti =  " (65 > Ws_ABCD_MSD && Ws_ABCD_MSD < 105)"




plotselection_sideband = "Signal_Topfirst_Zprime_M < 0"
plotselection_sideband_withtopbtag = "Signal_withtopbtag_Topfirst_Zprime_M < 0"


#plotselection_ABCD_general=  plotselection2 + "&& Zprimes_ABCD_M>0   &&    Ws_ABCD_t21 <  0.6    &&    105 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210  "
plotselection_ABCD_general_beta =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    65 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 105     &&    105 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210   "
plotselection_ABCD_general_beta2 =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    65 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 105     &&     Tops_ABCD_t32 < 0.86   "
#plotselection_ABCD_general_i =  plotselection2 + "&& Zprimes_ABCD_M[i]>0   &&    Ws_ABCD_t21[i] >  0.6    &&    105 < Tops_ABCD_MSD[i]     &&    Tops_ABCD_MSD[i]  < 210   "
plotselection_ABCD_general_beta_i =   "Zprimes_ABCD_M[i]>0   &&    65 < Ws_ABCD_MSD[i]  &&   Ws_ABCD_MSD[i] < 105     &&    105 < Tops_ABCD_MSD[i]     &&    Tops_ABCD_MSD[i]  < 210   "
plotselection_ABCD_general_beta2_i =  "Zprimes_ABCD_M[i]>0   &&    65 < Ws_ABCD_MSD[i]  &&   Ws_ABCD_MSD[i] < 105     &&     Tops_ABCD_t32[i] < 0.86   "


plotselection_ABCD_general_alt_notopbtag =  plotselection2 + " && Zprimes_ABCD_masscorrnotopbtag_M>0 && 65 < Ws_ABCD_masscorrnotopbtag_MSD && Ws_ABCD_masscorrnotopbtag_MSD < 105 && Tops_ABCD_masscorrnotopbtag_t32<0.86 "
plotselection_ABCD_general_alt_withtopbtag =  plotselection2 + " && Zprimes_ABCD_masscorrwithtopbtag_M>0 && 65 < Ws_ABCD_masscorrwithtopbtag_MSD && Ws_ABCD_masscorrwithtopbtag_MSD < 105 && Tops_ABCD_masscorrwithtopbtag_t32<0.86 "

