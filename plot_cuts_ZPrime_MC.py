# book plots
plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
plotselection1="Evt_HT>1000"
plotselection2="N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 && Evt_HT>850 "

topWP='loose'
WWP='loose'
bottomWP='medium'

WPs='tWP'+topWP+'WWP'+WWP+'bWP'+bottomWP
    
    
ABCDversion='ABCD2'  

#Own Plotselections for ABCD-method
if topWP=='loose':
    plotselection_tau32 = " Tops_ABCD_t32 < 0.86   "
    plotselection_tau32_i = " Tops_ABCD_t32[i] < 0.86   "
    plotselection_tau32_0 = " Tops_ABCD_t32[0] < 0.86   "
    
    MCSF_topntb_t32_MSD = " 1.06 "
    MCSF_topntb_t32anti_MSD = " 1.06 "
    MCSF_topntb_t32_MSDanti = " 1.06 "
    MCSF_topntb_t32anti_MSDanti = " 1.06 "
    
    MCSF_topntb_t32_MSD_up= " 0.09 "
    MCSF_topntb_t32anti_MSD_up = " 0.09 "
    MCSF_topntb_t32_MSDanti_up = " 0.09 "
    MCSF_topntb_t32anti_MSDanti_up = " 0.09 "
    
    MCSF_topntb_t32_MSD_down = " 0.04 "
    MCSF_topntb_t32anti_MSD_down = " 0.04 "
    MCSF_topntb_t32_MSDanti_down = " 0.04 "
    MCSF_topntb_t32anti_MSDanti_down = " 0.04 "
    
    MCSF_topwtb_t32_MSD = " 1.08 "
    MCSF_topwtb_t32anti_MSD = " 1.08 "
    MCSF_topwtb_t32_MSDanti = " 1.08 "
    MCSF_topwtb_t32anti_MSDanti = " 1.08 "
    
    MCSF_topwtb_t32_MSD_up= " 0.10 "
    MCSF_topwtb_t32anti_MSD_up = " 0.10 "
    MCSF_topwtb_t32_MSDanti_up = " 0.10 "
    MCSF_topwtb_t32anti_MSDanti_up = " 0.10 "
    
    MCSF_topwtb_t32_MSD_down = " 0.04 "
    MCSF_topwtb_t32anti_MSD_down = " 0.04 "
    MCSF_topwtb_t32_MSDanti_down = " 0.04 "
    MCSF_topwtb_t32anti_MSDanti_down = " 0.04 "
    
if topWP=='medium':
    plotselection_tau32 = " Tops_ABCD_t32 < 0.67   "
    plotselection_tau32_i = " Tops_ABCD_t32[i] < 0.67   "
    plotselection_tau32_0 = " Tops_ABCD_t32[0] < 0.67   "
    
    MCSF_topntb_t32_MSD = " 1.06 "
    MCSF_topntb_t32anti_MSD = " 1.06 "
    MCSF_topntb_t32_MSDanti = " 1.06 "
    MCSF_topntb_t32anti_MSDanti = " 1.06 "
    
    MCSF_topntb_t32_MSD_up= " 0.08 "
    MCSF_topntb_t32anti_MSD_up = " 0.08 "
    MCSF_topntb_t32_MSDanti_up = " 0.08 "
    MCSF_topntb_t32anti_MSDanti_up = " 0.08 "
    
    MCSF_topntb_t32_MSD_down = " 0.04 "
    MCSF_topntb_t32anti_MSD_down = " 0.04 "
    MCSF_topntb_t32_MSDanti_down = " 0.04 "
    MCSF_topntb_t32anti_MSDanti_down = " 0.04 "
    
    MCSF_topwtb_t32_MSD = " 1.05 "
    MCSF_topwtb_t32anti_MSD = " 1.05 "
    MCSF_topwtb_t32_MSDanti = " 1.05 "
    MCSF_topwtb_t32anti_MSDanti = " 1.05 "
    
    MCSF_topwtb_t32_MSD_up= " 0.11 "
    MCSF_topwtb_t32anti_MSD_up = " 0.11 "
    MCSF_topwtb_t32_MSDanti_up = " 0.11 "
    MCSF_topwtb_t32anti_MSDanti_up = " 0.11 "
    
    MCSF_topwtb_t32_MSD_down = " 0.05 "
    MCSF_topwtb_t32anti_MSD_down = " 0.05 "
    MCSF_topwtb_t32_MSDanti_down = " 0.05 "
    MCSF_topwtb_t32anti_MSDanti_down = " 0.05 "
    
if WWP=='loose':
    plotselection_W_tau21 = " Ws_ABCD_t21 < 0.6 "
    plotselection_W_tau21_i = " Ws_ABCD_t21[i] < 0.6  "
    plotselection_W_tau21_0 = " Ws_ABCD_t21[0] < 0.6  "

    MCSF_W_t21_MSD = " 1.11 "
    MCSF_W_t21anti_MSD = " 1.11 "
    MCSF_W_t21_MSDanti = " 1.11 "
    MCSF_W_t21anti_MSDanti = " 1.11 "

    MCSF_W_t21_MSD_up = " 0.08 "
    MCSF_W_t21anti_MSD_up = " 0.08 "
    MCSF_W_t21_MSDanti_up = " 0.08 "
    MCSF_W_t21anti_MSDanti_up = " 0.08 "

    MCSF_W_t21_MSD_down = " 0.08 "
    MCSF_W_t21anti_MSD_down = " 0.08 "
    MCSF_W_t21_MSDanti_down = " 0.08 "
    MCSF_W_t21anti_MSDanti_down = " 0.08 "
    
if WWP=='medium':
    plotselection_W_tau21 = " Ws_ABCD_t21 < 0.45"
    plotselection_W_tau21_i = " Ws_ABCD_t21[i] < 0.45  "
    plotselection_W_tau21_0 = " Ws_ABCD_t21[0] < 0.45  "

    MCSF_W_t21_MSD = " 1.10 "
    MCSF_W_t21anti_MSD = " 0.88 "
    MCSF_W_t21_MSDanti = " 1.10 "
    MCSF_W_t21anti_MSDanti = " 0.88 "

    MCSF_W_t21_MSD_up = " 0.12 "
    MCSF_W_t21anti_MSD_up = " 0.10 "
    MCSF_W_t21_MSDanti_up = " 0.12 "
    MCSF_W_t21anti_MSDanti_up = " 0.10 "

    MCSF_W_t21_MSD_down = " 0.12 "
    MCSF_W_t21anti_MSD_down = " 0.10 "
    MCSF_W_t21_MSDanti_down = " 0.12 "
    MCSF_W_t21anti_MSDanti_down = " 0.10 "


if bottomWP=='medium':
    plotselection_B_CSV = "  Bottoms_ABCD_CSV > 0.8  "    
    plotselection_B_CSV_i = "  Bottoms_ABCD_CSV[i] > 0.8   "
    plotselection_B_CSV_0 = "  Bottoms_ABCD_CSV[0] > 0.8   " 

if bottomWP=='tight':
    plotselection_B_CSV = "  Bottoms_ABCD_CSV > 0.935  "    
    plotselection_B_CSV_i = "  Bottoms_ABCD_CSV[i] > 0.935   "
    plotselection_B_CSV_0 = "  Bottoms_ABCD_CSV[0] > 0.935   " 

plotselection_tau32_anti=" Tops_ABCD_t32 > 0.86   "
plotselection_tau32_anti_i =" Tops_ABCD_t32[i] > 0.86   "
plotselection_tau32_anti_0 =" Tops_ABCD_t32[0] > 0.86   "

plotselection_W_tau21_anti = " Ws_ABCD_t21 > 0.6 "
plotselection_W_tau21_anti_i = " Ws_ABCD_t21[i]  > 0.6 "
plotselection_W_tau21_anti_0 = " Ws_ABCD_t21[0]  > 0.6 "





plotselection_W_MSD =  " (65 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 105) "
plotselection_W_MSD_i =  " (65 < Ws_ABCD_MSD[i]  &&   Ws_ABCD_MSD[i] < 105) "
plotselection_W_MSD_0 =  " (65 < Ws_ABCD_MSD[0]  &&   Ws_ABCD_MSD[0] < 105) "
plotselection_W_MSD_anti =  " (65 > Ws_ABCD_MSD  ||   Ws_ABCD_MSD > 105) "
plotselection_W_MSD_anti_i =  " (65 > Ws_ABCD_MSD[i]  ||   Ws_ABCD_MSD[i] > 105) "
plotselection_W_MSD_anti_0 =  " (65 > Ws_ABCD_MSD[0]  ||   Ws_ABCD_MSD[0] > 105) "



plotselection_B_CSV_anti = "  Bottoms_ABCD_CSV < 0.46   "
plotselection_B_CSV_anti_i = "  Bottoms_ABCD_CSV[i] < 0.46   "
plotselection_B_CSV_anti_0 = "  Bottoms_ABCD_CSV[0] < 0.46   "


plotselection_t_MSD = " (105 < Tops_ABCD_MSD && Tops_ABCD_MSD < 210) "
plotselection_t_MSD_i = " (105 < Tops_ABCD_MSD[i] && Tops_ABCD_MSD[i] < 210) "
plotselection_t_MSD_0 = " (105 < Tops_ABCD_MSD[0] && Tops_ABCD_MSD[0] < 210) "
plotselection_t_MSD_anti = " (105 > Tops_ABCD_MSD || Tops_ABCD_MSD > 210) "
plotselection_t_MSD_anti_i = " (105 > Tops_ABCD_MSD[i] || Tops_ABCD_MSD[i] > 210) "
plotselection_t_MSD_anti_0 = " (105 > Tops_ABCD_MSD[0] || Tops_ABCD_MSD[0] > 210) "
#plotselection_t_MSD_anti = " (75 > Tops_ABCD_MSD || Tops_ABCD_MSD > 250) "
#plotselection_t_MSD_anti_i = " (75 > Tops_ABCD_MSD[i] || Tops_ABCD_MSD[i] > 250) "
#plotselection_t_MSD_anti_0 = " (75 > Tops_ABCD_MSD[0] || Tops_ABCD_MSD[0] > 250) "


plotselection_topsubjetCSVv2 = " Tops_ABCD_maxsubjetCSVv2 > 0.8 "
plotselection_topsubjetCSVv2_i = " Tops_ABCD_maxsubjetCSVv2[i] > 0.8 "
plotselection_topsubjetCSVv2_0 = " Tops_ABCD_maxsubjetCSVv2[0] > 0.8 "

plotselection_topsubjetCSVv2_anti = " Tops_ABCD_maxsubjetCSVv2 < 0.8 "
plotselection_topsubjetCSVv2_anti_i = " Tops_ABCD_maxsubjetCSVv2[i] < 0.8 "
plotselection_topsubjetCSVv2_anti_0 = " Tops_ABCD_maxsubjetCSVv2[0] < 0.8 "




plotselection_W_MSD_one_sided =  " (65 < Ws_ABCD_MSD && Ws_ABCD_MSD < 105)"
plotselection_W_MSD_one_sided_anti =  " (65 > Ws_ABCD_MSD && Ws_ABCD_MSD < 105)"




plotselection_sideband = "Signal_Topfirst_Zprime_M < 0"
plotselection_sideband_withtopbtag = "Signal_withtopbtag_Topfirst_Zprime_M < 0"


#plotselection_ABCD_general=  plotselection2 + "&& Zprimes_ABCD_M>0   &&    Ws_ABCD_t21 <  0.6    &&    105 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210  "
plotselection_ABCD1_general =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    65 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 105     &&    105 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210  &&  Bottoms_ABCD_CSV>=0"
plotselection_ABCD2_general =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    65 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 105  &&  Bottoms_ABCD_CSV>=0     && "+ plotselection_tau32
#plotselection_ABCD_general_i =  plotselection2 + "&& Zprimes_ABCD_M[i]>0   &&    Ws_ABCD_t21[i] >  0.6    &&    105 < Tops_ABCD_MSD[i]     &&    Tops_ABCD_MSD[i]  < 210   "
plotselection_ABCD1_general_i =   "Zprimes_ABCD_M[i]>0   &&    65 < Ws_ABCD_MSD[i]  &&   Ws_ABCD_MSD[i] < 105     &&    105 < Tops_ABCD_MSD[i]     &&    Tops_ABCD_MSD[i]  < 210   &&  Bottoms_ABCD_CSV[i]>=0  "
plotselection_ABCD2_general_i =  "Zprimes_ABCD_M[i]>0   &&    65 < Ws_ABCD_MSD[i]  &&   Ws_ABCD_MSD[i] < 105   &&  Bottoms_ABCD_CSV[i]>=0    && "+ plotselection_tau32_i
plotselection_ABCD1_general_0 =   "Zprimes_ABCD_M[0]>0   &&    65 < Ws_ABCD_MSD[0]  &&   Ws_ABCD_MSD[0] < 105     &&    105 < Tops_ABCD_MSD[0]     &&    Tops_ABCD_MSD[0]  < 210   &&  Bottoms_ABCD_CSV[0]>=0  "
plotselection_ABCD2_general_0 =  "Zprimes_ABCD_M[0]>0   &&    65 < Ws_ABCD_MSD[0]  &&   Ws_ABCD_MSD[0] < 105    &&  Bottoms_ABCD_CSV[0]>0   && "+ plotselection_tau32_0


plotselection_ABCD_general_alt_notopbtag =  plotselection2 + " && Zprimes_ABCD_masscorrnotopbtag_M>0 && 65 < Ws_ABCD_masscorrnotopbtag_MSD && Ws_ABCD_masscorrnotopbtag_MSD < 105 && Tops_ABCD_masscorrnotopbtag_t32<0.86 "
plotselection_ABCD_general_alt_withtopbtag =  plotselection2 + " && Zprimes_ABCD_masscorrwithtopbtag_M>0 && 65 < Ws_ABCD_masscorrwithtopbtag_MSD && Ws_ABCD_masscorrwithtopbtag_MSD < 105 && Tops_ABCD_masscorrwithtopbtag_t32<0.86 "
