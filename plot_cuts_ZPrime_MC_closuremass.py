# book plots
radi=''

jetradius_top="8"
jetradius_W="8"
jetradius_bottom="4"

masscorrection=True
WZwindow=True
MSDgap=False
old=False


topWP='loose'
WWP='medium'
#WWP='loose'
bottomWP='medium'

WPs='tWP'+topWP+'WWP'+WWP+'bWP'+bottomWP+'nogap'

if masscorrection:
    WPs=WPs+"_masscorr"
if WZwindow:
    WPs=WPs+"_MZWindow3"
if MSDgap:
    WPs=WPs+"_MSDgap"
if old:
    WPs=WPs+"_nodynHT"


plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"

if old:
    plotselection1="Evt_HT>1000"
    plotselection1_i="Evt_HT>1000"
    plotselection1_0="Evt_HT>1000"
else:
    plotselection1="Evt_HT>1000 && Evt_HT>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT<(1.2*Zprimes_ABCD" +  radi + "_M) && N_Jets<9 && N_packedPatJetsAK8PFCHSSoftDrop<9"
    plotselection1_i="Evt_HT>1000 && Evt_HT>(0.8*Zprimes_ABCD" +  radi + "_M[i]) && Evt_HT<(1.2*Zprimes_ABCD" +  radi + "_M[i]) && N_Jets<9 && N_packedPatJetsAK8PFCHSSoftDrop<9"
    plotselection1_0="Evt_HT>1000 && Evt_HT>(0.8*Zprimes_ABCD" +  radi + "_M[0]) && Evt_HT<(1.2*Zprimes_ABCD" +  radi + "_M[0]) && N_Jets<9 && N_packedPatJetsAK8PFCHSSoftDrop<9"



if not MSDgap:
	plotselection2=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) "
	plotselection2_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 300) "
	plotselection2_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 300) "
else:
	plotselection2=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 500) "
        plotselection2_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 500) "


plotselection3=plotselection1 + "&&" + "N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200"


if(jetradius_top=="15" and jetradius_W=="8" and jetradius_bottom=="4"):
    radi='_tAK'+jetradius_top+"WAK"+jetradius_W+"bAK"+jetradius_bottom
    if masscorrection:
        radi="_masscorrnotopbtag"
    #plotselection2= "Ws_ABCD"+radi+"_Pt[ > 200" + " && " + "Tops_ABCD"+radi+"_Pt > 200"+" && Evt_HT>1000 "
    plotselection2=plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) "

if(jetradius_top=="15" and jetradius_W=="15" and jetradius_bottom=="4"):
    radi='_tAK'+jetradius_top+"WAK"+jetradius_W+"bAK"+jetradius_bottom
    #plotselection2= "Ws_ABCD"+radi+"_Pt > 200" + " && " + "Tops_ABCD"+radi+"_Pt > 200"+" && Evt_HT>1000 "
    plotselection2=plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) "

if(jetradius_top=="12" and jetradius_W=="8" and jetradius_bottom=="4"):
    radi='_tAK'+jetradius_top+"WAK"+jetradius_W+"bAK"+jetradius_bottom
    #plotselection2= "Ws_ABCD"+radi+"_Pt > 200" + " && " + "Tops_ABCD"+radi+"_Pt > 200"+" && Evt_HT>1000 "
    plotselection2=plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) "

if(jetradius_top=="12" and jetradius_W=="8" and jetradius_bottom=="4"):
    radi='_tAK'+jetradius_top+"WAK"+jetradius_W+"bAK"+jetradius_bottom
    #plotselection2= "Ws_ABCD"+radi+"_Pt > 200" + " && " + "Tops_ABCD"+radi+"_Pt > 200"+" && Evt_HT>1000 "
    plotselection2=plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) "





#Own Plotselections for ABCD-method
#Own Plotselections for ABCD-method
if topWP=='loose':
    plotselection_tau32 = " Tops_ABCD"+radi+"_t32 < 0.86   "
    plotselection_tau32_i = " Tops_ABCD"+radi+"_t32[i] < 0.86   "
    plotselection_tau32_0 = " Tops_ABCD"+radi+"_t32[0] < 0.86   "
    
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
    plotselection_tau32 = " Tops_ABCD"+radi+"_t32 < 0.67   "
    plotselection_tau32_i = " Tops_ABCD"+radi+"_t32[i] < 0.67   "
    plotselection_tau32_0 = " Tops_ABCD"+radi+"_t32[0] < 0.67   "
    
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
    plotselection_W_tau21 = " Ws_ABCD"+radi+"_t21 < 0.6 "
    plotselection_W_tau21_i = " Ws_ABCD"+radi+"_t21[i] < 0.6  "
    plotselection_W_tau21_0 = " Ws_ABCD"+radi+"_t21[0] < 0.6  "

    plotselection_W_tau21_anti = " Ws_ABCD"+radi+"_t21 > 0.6 "
    plotselection_W_tau21_anti_i = " Ws_ABCD"+radi+"_t21[i]  > 0.6 "
    plotselection_W_tau21_anti_0 = " Ws_ABCD"+radi+"_t21[0]  > 0.6 "

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
    plotselection_W_tau21 = " Ws_ABCD"+radi+"_t21 < 0.45"
    plotselection_W_tau21_i = " Ws_ABCD"+radi+"_t21[i] < 0.45  "
    plotselection_W_tau21_0 = " Ws_ABCD"+radi+"_t21[0] < 0.45  "

    plotselection_W_tau21_anti = " Ws_ABCD"+radi+"_t21 > 0.45 "
    plotselection_W_tau21_anti_i = " Ws_ABCD"+radi+"_t21[i]  > 0.45 "
    plotselection_W_tau21_anti_0 = " Ws_ABCD"+radi+"_t21[0]  > 0.45 "


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


if WZwindow:
   
   plotselection_W_MSD =  " (65 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 105) "
   plotselection_W_MSD_i =  " (65 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 105) "
   plotselection_W_MSD_0 =  " (650 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 105) "
   
   if not MSDgap:
	plotselection_W_MSD_anti =  " (65 > Ws_ABCD"+radi+"_MSD  ||   Ws_ABCD"+radi+"_MSD > 105) "
        plotselection_W_MSD_anti_i =  " (65 > Ws_ABCD"+radi+"_MSD[i]  ||   Ws_ABCD"+radi+"_MSD[i] > 105) "
        plotselection_W_MSD_anti_0 =  " (65 > Ws_ABCD"+radi+"_MSD[0]  ||   Ws_ABCD"+radi+"_MSD[0] > 105) "
   else:
        plotselection_W_MSD_anti =  " (65 > Ws_ABCD"+radi+"_MSD  ||   Ws_ABCD"+radi+"_MSD > 150) "
        plotselection_W_MSD_anti_i =  " (65 > Ws_ABCD"+radi+"_MSD[i]  ||   Ws_ABCD"+radi+"_MSD[i] > 150) "
        plotselection_W_MSD_anti_0 =  " (65 > Ws_ABCD"+radi+"_MSD[0]  ||   Ws_ABCD"+radi+"_MSD[0] > 150) "
	

else:
   plotselection_W_MSD =  " (75 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 95) "
   plotselection_W_MSD_i =  " (75 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 95) "
   plotselection_W_MSD_0 =  " (75 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 95) "
   if not MSDgap:
        plotselection_W_MSD_anti =  " (75 > Ws_ABCD"+radi+"_MSD  ||   Ws_ABCD"+radi+"_MSD > 95) "
        plotselection_W_MSD_anti_i =  " (75 > Ws_ABCD"+radi+"_MSD[i]  ||   Ws_ABCD"+radi+"_MSD[i] > 95) "
        plotselection_W_MSD_anti_0 =  " (75 > Ws_ABCD"+radi+"_MSD[0]  ||   Ws_ABCD"+radi+"_MSD[0] > 95) "
   else:
        plotselection_W_MSD_anti =  " (75 > Ws_ABCD"+radi+"_MSD  ||   Ws_ABCD"+radi+"_MSD > 150) "
        plotselection_W_MSD_anti_i =  " (75 > Ws_ABCD"+radi+"_MSD[i]  ||   Ws_ABCD"+radi+"_MSD[i] > 150) "
        plotselection_W_MSD_anti_0 =  " (75 > Ws_ABCD"+radi+"_MSD[0]  ||   Ws_ABCD"+radi+"_MSD[0] > 150) "


#plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.46   "
#plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.46   "
#plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.46   "
plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.8   "
plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.8   "
plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.8   "

if WZwindow or MSDgap:
	plotselection_t_MSD = " (150 < Tops_ABCD"+radi+"_MSD && Tops_ABCD"+radi+"_MSD < 240) "
	plotselection_t_MSD_i = " (150 < Tops_ABCD"+radi+"_MSD[i] && Tops_ABCD"+radi+"_MSD[i] < 240) "
	plotselection_t_MSD_0 = " (150 < Tops_ABCD"+radi+"_MSD[0] && Tops_ABCD"+radi+"_MSD[0] < 240) "
        plotselection_t_MSD_anti = " (150 > Tops_ABCD"+radi+"_MSD || Tops_ABCD"+radi+"_MSD > 240) "
        plotselection_t_MSD_anti_i = " (150 > Tops_ABCD"+radi+"_MSD[i] || Tops_ABCD"+radi+"_MSD[i] > 240) "
        plotselection_t_MSD_anti_0 = " (150 > Tops_ABCD"+radi+"_MSD[0] || Tops_ABCD"+radi+"_MSD[0] > 240) "

else:	
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
plotselection_ABCD_general_beta =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>0 " + "  &&  "+ plotselection_TprimeMass + "  &&  "+ plotselection_W_MSD + " && " + plotselection_t_MSD  
plotselection_ABCD_general_beta_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "   &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_t_MSD_0 
plotselection_ABCD_general_beta_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_W_MSD_i + " && " + plotselection_t_MSD_i 
plotselection_ABCD_general_beta2 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_TprimeMass + "  &&  "+ plotselection_W_MSD + " && " + plotselection_tau32 
plotselection_ABCD_general_beta2_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_tau32_0 
plotselection_ABCD_general_beta2_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_W_MSD_i + " && " + plotselection_tau32_i 

plotselection_ABCD_general_beta3 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_TprimeMass + "  &&  "+ plotselection_t_MSD + " && " + plotselection_tau32 
plotselection_ABCD_general_beta3_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 
plotselection_ABCD_general_beta3_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_t_MSD_i + " && " + plotselection_tau32_i

plotselection_ABCD_general_beta4 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_W_MSD + "  &&  "+ plotselection_t_MSD + " && " + plotselection_tau32 
plotselection_ABCD_general_beta4_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_W_MSD_0 + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 
plotselection_ABCD_general_beta4_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_W_MSD_i + "  &&  "+ plotselection_t_MSD_i + " && " + plotselection_tau32_i

plotselection_ABCD_general_beta5 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_t_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass 
plotselection_ABCD_general_beta5_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0 
plotselection_ABCD_general_beta5_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_t_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i 

plotselection_ABCD_general_beta6 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_W_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass 
plotselection_ABCD_general_beta6_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_W_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0 
plotselection_ABCD_general_beta6_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_W_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i 

plotselection_ABCD_general_beta7 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_W_tau21 + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass 
plotselection_ABCD_general_beta7_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_W_tau21_0 + " && " + plotselection_tau32_0 + "  &&  " +  plotselection_TprimeMass_0 
plotselection_ABCD_general_beta7_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_W_tau21_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i 



##plotselection_ABCD_general=  plotselection1 + "&& Zprimes_ABCD_M>0   &&    Ws_ABCD_t21 <  0.6    &&    105 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210  "
#plotselection_ABCD_general_beta =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>0 " + "  &&  "+ plotselection_TprimeMass + "  &&  "+ plotselection_W_MSD + " && " + plotselection_t_MSD + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) " 
#plotselection_ABCD_general_beta_0 =  plotselection1_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "   &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_t_MSD_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 300) " 
#plotselection_ABCD_general_beta_i =  plotselection1_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_W_MSD_i + " && " + plotselection_t_MSD_i + " && (40 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 300) " 

#plotselection_ABCD_general_beta2 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_TprimeMass + "  &&  "+ plotselection_W_MSD + " && " + plotselection_tau32 + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) " 
#plotselection_ABCD_general_beta2_0 =  plotselection1_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_tau32_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 300) " 
#plotselection_ABCD_general_beta2_i =  plotselection1_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_W_MSD_i + " && " + plotselection_tau32_i + " && (40 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 300) " 

#plotselection_ABCD_general_beta3 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_TprimeMass + "  &&  "+ plotselection_t_MSD + " && " + plotselection_tau32 + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) " 
#plotselection_ABCD_general_beta3_0 =  plotselection1_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 300) " 
#plotselection_ABCD_general_beta3_i =  plotselection1_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_t_MSD_i + " && " + plotselection_tau32_i + " && (40 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 300) " 

#plotselection_ABCD_general_beta4 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_W_MSD + "  &&  "+ plotselection_t_MSD + " && " + plotselection_tau32 + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) " 
#plotselection_ABCD_general_beta4_0 =  plotselection1_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_W_MSD_0 + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 300) " 
#plotselection_ABCD_general_beta4_i =  plotselection1_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_W_MSD_i + "  &&  "+ plotselection_t_MSD_i + " && " + plotselection_tau32_i + " && (40 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 300) " 

#plotselection_ABCD_general_beta5 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_t_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) " 
#plotselection_ABCD_general_beta5_0 =  plotselection1_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 300) " 
#plotselection_ABCD_general_beta5_i =  plotselection1_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_t_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i + " && (40 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 300) " 

#plotselection_ABCD_general_beta6 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_W_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) " 
#plotselection_ABCD_general_beta6_0 =  plotselection1_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_W_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 300) " 
#plotselection_ABCD_general_beta6_i =  plotselection1_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_W_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i + " && (40 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 300) " 

#plotselection_ABCD_general_beta7 =  plotselection1 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>0 " + "  &&  " + plotselection_W_tau21 + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass + " && (40 < Ws_ABCD"+radi+"_MSD  &&   Ws_ABCD"+radi+"_MSD < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) " 
#plotselection_ABCD_general_beta7_0 =  plotselection1_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>0 " + "  &&  " + plotselection_W_tau21_0 + " && " + plotselection_tau32_0 + "  &&  " +  plotselection_TprimeMass_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0]  &&   Ws_ABCD"+radi+"_MSD[0] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 300) " 
#plotselection_ABCD_general_beta7_i =  plotselection1_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>0 " + "  &&  " + plotselection_W_tau21_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i + " && (40 < Ws_ABCD"+radi+"_MSD[i]  &&   Ws_ABCD"+radi+"_MSD[i] < 130) "  + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 300) " 
