# book plots
radi=''



PileUp='CHS'
#PileUp='PUPPI'
#JetDeclustering='SoftDrop'
JetDeclustering='Pruning'
radi=PileUp+JetDeclustering

masscorrection=False
#WZwindow=True
WZwindow=False
MSDgap=False
#old=True
old=False
fullMSD=True
toponsided=False
csvgap=False

#PVgecut=True
PVgecut=False
#PVlecut=True
PVlecut=False

#tau21varup=True
tau21varup=False
#tau21vardown=True
tau21vardown=False
#csvvarup=True
csvvarup=False
#csvvardown=True
csvvardown=False
varsize=0.05

#topSJWP='loose'
topSJWP='medium'
#topWP='medium'
topWP='loose'
WWP='medium'
#WWP='loose'
bottomWP='medium'
#bottomWP='loose'

WPs='tWP'+topWP+'tSJWP'+topSJWP+'WWP'+WWP+'bWP'+bottomWP


if varsize==0.05:
    

    if tau21varup:
        WPs+="_tauvar21up_5pc"
    if tau21vardown:
        WPs+="_tauvar21down_5pc"
    if csvvarup:
        WPs+="_csvvarup_5pc"
    if csvvardown:
        WPs+="_csvvardown_5pc"    


if varsize==0.10:
    

    if tau21varup:
        WPs+="_tauvar21up_10pc"
    if tau21vardown:
        WPs+="_tauvar21down_10pc"
    if csvvarup:
        WPs+="_csvvarup_10pc"
    if csvvardown:
        WPs+="_csvvardown_10pc"    

if varsize==0.15:
    

    if tau21varup:
        WPs+="_tauvar21up_15pc"
    if tau21vardown:
        WPs+="_tauvar21down_15pc"
    if csvvarup:
        WPs+="_csvvarup_15pc"
    if csvvardown:
        WPs+="_csvvardown_15pc"    



if not csvgap:
    WPs=WPs+"_nogap"
if masscorrection:
    WPs=WPs+"_masscorr"
if WZwindow:
    WPs=WPs+"_AnnaWindow"
if MSDgap:
    WPs=WPs+"_MSDgap"
if old:
    WPs=WPs+"_nodynHT"
if PVgecut:
    WPs=WPs+"_PVgecut"
if PVlecut:
    WPs=WPs+"_PVlecut"

if fullMSD:
    WPs=WPs+"_fullWMSD"
if toponsided:
    WPs=WPs+"_topMSDonesided"
   

    

plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
verybasicplotselection="Evt_HT_Jets>1000"

if old:
    plotselection1="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt>200 && Tops_ABCD"+radi+"_Pt>400 && Bottoms_ABCD" + radi + "_Pt>100"
    plotselection1_i="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt[i]>200 && Tops_ABCD"+radi+"_Pt[i]>400 && Bottoms_ABCD" + radi + "_Pt[i]>100"
    plotselection1_0="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt[0]>200 && Tops_ABCD"+radi+"_Pt[0]>400 && Bottoms_ABCD" + radi + "_Pt[0]>100"
    #plotselection_EvtHT="Evt_HT_Jets>(0*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(10*Zprimes_ABCD" +  radi + "_M)"
    #plotselection_EvtHT_i="Evt_HT_Jets>(0*Zprimes_ABCD" +  radi + "_M[i]) && Evt_HT_Jets<(10*Zprimes_ABCD" +  radi + "_M[i])"
    #plotselection_EvtHT_0="Evt_HT_Jets>(0*Zprimes_ABCD" +  radi + "_M[0]) && Evt_HT_Jets<(10*Zprimes_ABCD" +  radi + "_M[0])"
    if PVgecut:
        plotselection1=plotselection1+" && N_PrimaryVertices>=25"
        plotselection1_i=plotselection1_i+" && N_PrimaryVertices>=25"
        plotselection1_0=plotselection1_0+" && N_PrimaryVertices>=25"
    if PVlecut:
        plotselection1=plotselection1+" && N_PrimaryVertices<10"
        plotselection1_i=plotselection1_i+" && N_PrimaryVertices<10"
        plotselection1_0=plotselection1_0+" && N_PrimaryVertices<10"
else:
    #plotselection1="Evt_HT_Jets>1000 && Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M) && Ws_ABCD"+radi+"_Pt>200 && Tops_ABCD"+radi+"_Pt>400 && Bottoms_ABCD" + radi + "_Pt>100"
    #plotselection1_i="Evt_HT_Jets>1000 && Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M[i]) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M[i]) && Ws_ABCD"+radi+"_Pt[i]>200 && Tops_ABCD"+radi+"_Pt[i]>400 && Bottoms_ABCD" + radi + "_Pt[i]>100"
    #plotselection1_0="Evt_HT_Jets>1000 && Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M[0]) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M[0]) && Ws_ABCD"+radi+"_Pt[0]>200 && Tops_ABCD"+radi+"_Pt[0]>400 && Bottoms_ABCD" + radi + "_Pt[0]>100"
    plotselection1="Evt_HT_Jets>1000 && Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M) && Ws_ABCD"+radi+"_Pt>150 && Tops_ABCD"+radi+"_Pt>150 && Bottoms_ABCD" + radi + "_Pt>75"
    plotselection1_i="Evt_HT_Jets>1000 && Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M[i]) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M[i]) && Ws_ABCD"+radi+"_Pt[i]>150 && Tops_ABCD"+radi+"_Pt[i]>150 && Bottoms_ABCD" + radi + "_Pt[i]>75"
    plotselection1_0="Evt_HT_Jets>1000 && Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M[0]) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M[0]) && Ws_ABCD"+radi+"_Pt[0]>150 && Tops_ABCD"+radi+"_Pt[0]>150 && Bottoms_ABCD" + radi + "_Pt[0]>75"
        #plotselection1="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt>200 && Tops_ABCD"+radi+"_Pt>400 && Bottoms_ABCD" + radi + "_Pt>100"
    #plotselection1_i="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt[i]>200 && Tops_ABCD"+radi+"_Pt[i]>400 && Bottoms_ABCD" + radi + "_Pt[i]>100"
    #plotselection1_0="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt[0]>200 && Tops_ABCD"+radi+"_Pt[0]>400 && Bottoms_ABCD" + radi + "_Pt[0]>100"    
    #plotselection_EvtHT="Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M)"
    #plotselection_EvtHT_i="Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M[i]) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M[i])"
    #plotselection_EvtHT_0="Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M[0]) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M[0])"
    if PVgecut:
        plotselection1=plotselection1+" && N_PrimaryVertices>=15"
        plotselection1_i=plotselection1_i+" && N_PrimaryVertices>=15"
        plotselection1_0=plotselection1_0+" && N_PrimaryVertices>=15"
    if PVlecut:
        plotselection1=plotselection1+" && N_PrimaryVertices<15"
        plotselection1_i=plotselection1_i+" && N_PrimaryVertices<15"
        plotselection1_0=plotselection1_0+" && N_PrimaryVertices<15"
        
if not MSDgap:
	plotselection2=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 1000) && Ws_ABCD"+radi+"_t21 <0.75"
	plotselection2_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 1000)  && Ws_ABCD"+radi+"_t21[i] <0.75"
	plotselection2_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 1000)  && Ws_ABCD"+radi+"_t21[0] <0.75"
else:
	plotselection2=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 < 1000) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500)  && Ws_ABCD"+radi+"_t21 <0.75"
        plotselection2_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i] < 1000) " + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 1000)  && Ws_ABCD"+radi+"_t21[i] <0.75"
        plotselection2_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0] < 1000) " + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 1000)  && Ws_ABCD"+radi+"_t21[0] <0.75"

if fullMSD:
	plotselection2=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 < 1000) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500)  && Ws_ABCD"+radi+"_t21 <0.75"
        plotselection2_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i] < 1000) " + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 1000)  && Ws_ABCD"+radi+"_t21[i] <0.75"
        plotselection2_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0] < 1000) " + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 1000)  && Ws_ABCD"+radi+"_t21[0] <0.75"

plotselection3=plotselection1 + "&&" + "N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200"




#Own Plotselections for ABCD-method
#Own Plotselections for ABCD-method
if topWP=='loose':
    plotselection_tau32 = " Tops_ABCD"+radi+"_t32 < 0.81   "
    plotselection_tau32_i = " Tops_ABCD"+radi+"_t32[i] < 0.81   "
    plotselection_tau32_0 = " Tops_ABCD"+radi+"_t32[0] < 0.81   "
    
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
    if not WZwindow:
        
        if tau21vardown:
            plotselection_W_tau21 = " Ws_ABCD"+radi+"_t21 < 0.45*(1.0-"+str(varsize)+")"
            plotselection_W_tau21_i = " Ws_ABCD"+radi+"_t21[i] < 0.45*(1.0-"+str(varsize)+") "
            plotselection_W_tau21_0 = " Ws_ABCD"+radi+"_t21[0] < 0.45*(1.0-"+str(varsize)+") "

            plotselection_W_tau21_anti = " 0.75 > Ws_ABCD"+radi+"_t21 > 0.45*(1.0-"+str(varsize)+") "
            plotselection_W_tau21_anti_i = " 0.75 > Ws_ABCD"+radi+"_t21[i]  > 0.45*(1.0-"+str(varsize)+") "
            plotselection_W_tau21_anti_0 = " 0.75 > Ws_ABCD"+radi+"_t21[0]  > 0.45*(1.0-"+str(varsize)+") "
    	
    	elif tau21varup:
            plotselection_W_tau21 = " Ws_ABCD"+radi+"_t21 < 0.45*(1.0+"+str(varsize)+")"
            plotselection_W_tau21_i = " Ws_ABCD"+radi+"_t21[i] < 0.45*(1.0+"+str(varsize)+") "
            plotselection_W_tau21_0 = " Ws_ABCD"+radi+"_t21[0] < 0.45*(1.0+"+str(varsize)+") "

            plotselection_W_tau21_anti = " 0.75 > Ws_ABCD"+radi+"_t21 > 0.45*(1.0+"+str(varsize)+") "
            plotselection_W_tau21_anti_i = " 0.75 > Ws_ABCD"+radi+"_t21[i]  > 0.45*(1.0+"+str(varsize)+") "
            plotselection_W_tau21_anti_0 = " 0.75 > Ws_ABCD"+radi+"_t21[0]  > 0.45*(1.0+"+str(varsize)+") "    	
            
        else:
            plotselection_W_tau21 = " Ws_ABCD"+radi+"_t21 < 0.45"
            plotselection_W_tau21_i = " Ws_ABCD"+radi+"_t21[i] < 0.45  "
            plotselection_W_tau21_0 = " Ws_ABCD"+radi+"_t21[0] < 0.45  "

            plotselection_W_tau21_anti = " 0.75 > Ws_ABCD"+radi+"_t21 > 0.45 "
            plotselection_W_tau21_anti_i = " 0.75 > Ws_ABCD"+radi+"_t21[i]  > 0.45 "
            plotselection_W_tau21_anti_0 = " 0.75 > Ws_ABCD"+radi+"_t21[0]  > 0.45 "
            
            
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
        
    else:
    	plotselection_W_tau21 = " Ws_ABCD"+radi+"_t21 < 0.5"
    	plotselection_W_tau21_i = " Ws_ABCD"+radi+"_t21[i] < 0.5  "
    	plotselection_W_tau21_0 = " Ws_ABCD"+radi+"_t21[0] < 0.5  "

        plotselection_W_tau21_anti = " Ws_ABCD"+radi+"_t21 > 0.5 "
    	plotselection_W_tau21_anti_i = " Ws_ABCD"+radi+"_t21[i]  > 0.5 "
        plotselection_W_tau21_anti_0 = " Ws_ABCD"+radi+"_t21[0]  > 0.5 "    

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
        
        MCSF_Wanti_t21_MSD = " 1.049 "
        MCSF_Wanti_t21anti_MSD = " 1.0 "
        MCSF_Wanti_t21_MSDanti = " 1.049 "
        MCSF_Wanti_t21anti_MSDanti = " 1.0 "

        MCSF_Wanti_t21_MSD_up = " 0.0069 "
        MCSF_Wanti_t21anti_MSD_up = " 0.10 "
        MCSF_Wanti_t21_MSDanti_up = " 0.0069 "
        MCSF_Wanti_t21anti_MSDanti_up = " 0.10 "

        MCSF_Wanti_t21_MSD_down = " 0.0069 "
        MCSF_Wanti_t21anti_MSD_down = " 0.10 "
        MCSF_Wanti_t21_MSDanti_down = " 0.0069 "
        MCSF_Wanti_t21anti_MSDanti_down = " 0.10 "        
    
    


if bottomWP=='medium':
    #plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.8484  "    
    #plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.8484  "
    #plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.8484   " 
    
    if csvvarup:
        plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.8484*(1.0+"+str(varsize)+")  "    
        plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.8484*(1.0+"+str(varsize)+")  "
        plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.8484*(1.0+"+str(varsize)+")   " 
    
    elif csvvardown:
        plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.8484*(1.0-"+str(varsize)+") "    
        plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.8484*(1.0-"+str(varsize)+") "
        plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.8484*(1.0-"+str(varsize)+")  " 
    else:
    
        plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.8484  "    
        plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.8484  "
        plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.8484   " 



if bottomWP=='loose':
    #plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.8484  "    
    #plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.8484  "
    #plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.8484   " 
    
    if csvvarup:
        plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.5426*(1.0+"+str(varsize)+")  "    
        plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.5426*(1.0+"+str(varsize)+")  "
        plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.5426*(1.0+"+str(varsize)+")   " 
    
    elif csvvardown:
        plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.5426*(1.0-"+str(varsize)+") "    
        plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.5426*(1.0-"+str(varsize)+") "
        plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.5426*(1.0-"+str(varsize)+")  " 
    else:
    
        plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.5426  "    
        plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.5426  "
        plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.5426   " 


if bottomWP=='tight':
    plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.935  "    
    plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.935   "
    plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.935   "


if csvgap:
   plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.5426   "
   plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.5426   "
   plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.5426   "
else:
    if bottomWP=='medium': 
        if csvvarup:
            plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.8484*(1.0+"+str(varsize)+")   "
            plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.8484*(1.0+"+str(varsize)+")   "
            plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.8484*(1.0+"+str(varsize)+")   "
        elif csvvardown:
            plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.8484*(1.0-"+str(varsize)+") "
            plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.8484*(1.0-"+str(varsize)+") "
            plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.8484*(1.0-"+str(varsize)+") "

        else:
            plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.8484   "
            plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.8484   "
            plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.8484   "
    if bottomWP=='loose': 
        if csvvarup:
            plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.5426*(1.0+"+str(varsize)+")   "
            plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.5426*(1.0+"+str(varsize)+")   "
            plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.5426*(1.0+"+str(varsize)+")   "
        elif csvvardown:
            plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.5426*(1.0-"+str(varsize)+") "
            plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.5426*(1.0-"+str(varsize)+") "
            plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.5426*(1.0-"+str(varsize)+") "

        else:
            plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.5426   "
            plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.5426   "
            plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.5426   "

plotselection_tau32_anti=" Tops_ABCD"+radi+"_t32 > 0.81   "
plotselection_tau32_anti_i =" Tops_ABCD"+radi+"_t32[i] > 0.81   "
plotselection_tau32_anti_0 =" Tops_ABCD"+radi+"_t32[0] > 0.81   "




if WZwindow:
   
   plotselection_W_MSD =  " (60 < Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 < 115) "
   plotselection_W_MSD_i =  " (60 < Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i] < 115) "
   plotselection_W_MSD_0 =  " (60 < Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0] < 115) "
   if not MSDgap:
	plotselection_W_MSD_anti =  " (60 > Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3  ||   Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 > 115) "
        plotselection_W_MSD_anti_i =  " (60 > Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i]  ||   Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i] > 115) "
        plotselection_W_MSD_anti_0 =  " (60 > Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0]  ||   Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0] > 115) "
   else:
        plotselection_W_MSD_anti =  " (60 > Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3  ||   Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 > 150) "
        plotselection_W_MSD_anti_i =  " (60 > Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i]  ||   Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i] > 150) "
        plotselection_W_MSD_anti_0 =  " (60 > Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0]  ||   Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0] > 150) "
	

else:
   plotselection_W_MSD =  " (65 < Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 < 105) "
   plotselection_W_MSD_i =  " (65 < Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i] < 105) "
   plotselection_W_MSD_0 =  " (65 < Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0] < 105) "
   if not MSDgap:
        plotselection_W_MSD_anti =  " (65 > Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3  ||   Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 > 105) "
        plotselection_W_MSD_anti_i =  " (65 > Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i]  ||   Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i] > 105) "
        plotselection_W_MSD_anti_0 =  " (65 > Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0]  ||   Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0] > 105) "
   else:
        plotselection_W_MSD_anti =  " (65 > Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3  ||   Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 > 300) "
        plotselection_W_MSD_anti_i =  " (65 > Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i]  ||   Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i] > 300) "
        plotselection_W_MSD_anti_0 =  " (65 > Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0]  ||   Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0] > 300) "



plotselection_t_MSD = " (105 < Tops_ABCD"+radi+"_MSD && Tops_ABCD"+radi+"_MSD < 210) "
plotselection_t_MSD_i = " (105 < Tops_ABCD"+radi+"_MSD[i] && Tops_ABCD"+radi+"_MSD[i] < 210) "
plotselection_t_MSD_0 = " (105 < Tops_ABCD"+radi+"_MSD[0] && Tops_ABCD"+radi+"_MSD[0] < 210) "
if not toponsided:
    plotselection_t_MSD_anti = " (105 > Tops_ABCD"+radi+"_MSD || Tops_ABCD"+radi+"_MSD > 210) "
    plotselection_t_MSD_anti_i = " (105 > Tops_ABCD"+radi+"_MSD[i] || Tops_ABCD"+radi+"_MSD[i] > 210) "
    plotselection_t_MSD_anti_0 = " (105 > Tops_ABCD"+radi+"_MSD[0] || Tops_ABCD"+radi+"_MSD[0] > 210) "
else:
    plotselection_t_MSD_anti = " (60 > Tops_ABCD"+radi+"_MSD || Tops_ABCD"+radi+"_MSD > 210) "
    plotselection_t_MSD_anti_i = " (60 > Tops_ABCD"+radi+"_MSD[i] || Tops_ABCD"+radi+"_MSD[i] > 210) "
    plotselection_t_MSD_anti_0 = " (60 > Tops_ABCD"+radi+"_MSD[0] || Tops_ABCD"+radi+"_MSD[0] > 210) "


#plotselection_topsubjetCSVv2 = " Tops_ABCD"+radi+"_maxsubjetCSVv2 > 0.5426 "
#plotselection_topsubjetCSVv2_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] > 0.5426 "
#plotselection_topsubjetCSVv2_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] > 0.5426 "

#plotselection_topsubjetCSVv2_anti = " Tops_ABCD"+radi+"_maxsubjetCSVv2 < 0.5426 "
#plotselection_topsubjetCSVv2_anti_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] < 0.5426 "
#plotselection_topsubjetCSVv2_anti_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] < 0.5426 "

#plotselection_topsubjetCSVv2 = " Tops_ABCD"+radi+"_maxsubjetCSVv2 > 0.8484 "
#plotselection_topsubjetCSVv2_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] > 0.8484 "
#plotselection_topsubjetCSVv2_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] > 0.8484 "

#plotselection_topsubjetCSVv2_anti = " Tops_ABCD"+radi+"_maxsubjetCSVv2 < 0.8484 "
#plotselection_topsubjetCSVv2_anti_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] < 0.8484 "
#plotselection_topsubjetCSVv2_anti_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] < 0.8484 "

if topSJWP=='medium':
    
    
    plotselection_topsubjetCSVv2 = " Tops_ABCD"+radi+"_maxsubjetCSVv2 > 0.8484 "
    plotselection_topsubjetCSVv2_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] > 0.8484 "
    plotselection_topsubjetCSVv2_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] > 0.8484 "

    plotselection_topsubjetCSVv2_anti = " Tops_ABCD"+radi+"_maxsubjetCSVv2 < 0.8484 "
    plotselection_topsubjetCSVv2_anti_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] < 0.8484 "
    plotselection_topsubjetCSVv2_anti_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] < 0.8484 "
else:

    
    plotselection_topsubjetCSVv2 = " Tops_ABCD"+radi+"_maxsubjetCSVv2 > 0.5426 "
    plotselection_topsubjetCSVv2_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] > 0.5426 "
    plotselection_topsubjetCSVv2_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] > 0.5426 "

    plotselection_topsubjetCSVv2_anti = " Tops_ABCD"+radi+"_maxsubjetCSVv2 < 0.5426 "
    plotselection_topsubjetCSVv2_anti_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] < 0.5426 "
    plotselection_topsubjetCSVv2_anti_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] < 0.5426 "


plotselection_TprimeMass = " Tprimes_ABCD"+radi+"_M>500 "
plotselection_TprimeMass_i = " Tprimes_ABCD"+radi+"_M[i]>500 "
plotselection_TprimeMass_0 = " Tprimes_ABCD"+radi+"_M[0]>500 "

plotselection_TprimeMass_anti = " Tprimes_ABCD"+radi+"_M<500 "
plotselection_TprimeMass_anti_i = " Tprimes_ABCD"+radi+"_M[i]<500 "
plotselection_TprimeMass_anti_0 = " Tprimes_ABCD"+radi+"_M[0]<500 "


plotselection_W_MSD_one_sided =  " (65 < Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 && Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 < 105)"
plotselection_W_MSD_one_sided_anti =  " (65 > Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 && Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 < 105)"




plotselection_sideband = "Signal_Topfirst_Zprime_M < 0"
plotselection_sideband_withtopbtag = "Signal_withtopbtag_Topfirst_Zprime_M < 0"


#plotselection_ABCD_general=  plotselection1 + "&& Zprimes_ABCD_M>0   &&    Ws_ABCD_t21 <  0.6    &&    105 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210  "
plotselection_ABCD_general_beta =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " + "  &&  "+ plotselection_TprimeMass + "  &&  "+ plotselection_W_MSD + " && " + plotselection_t_MSD  
plotselection_ABCD_general_beta_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " + "   &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_t_MSD_0 
plotselection_ABCD_general_beta_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_W_MSD_i + " && " + plotselection_t_MSD_i 
plotselection_ABCD_general_beta2 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M>1000 " + "  &&  " + plotselection_TprimeMass + "  &&  "+ plotselection_W_MSD + " && " + plotselection_tau32 
plotselection_ABCD_general_beta2_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " + "  &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_tau32_0 
plotselection_ABCD_general_beta2_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_W_MSD_i + " && " + plotselection_tau32_i 

plotselection_ABCD_general_beta3 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>1000 " + "  &&  " + plotselection_TprimeMass + "  &&  "+ plotselection_t_MSD + " && " + plotselection_tau32 
plotselection_ABCD_general_beta3_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " + "  &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 
plotselection_ABCD_general_beta3_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_t_MSD_i + " && " + plotselection_tau32_i

plotselection_ABCD_general_beta4 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>1000 " + "  &&  " + plotselection_W_MSD + "  &&  "+ plotselection_t_MSD + " && " + plotselection_tau32 
plotselection_ABCD_general_beta4_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " + "  &&  " + plotselection_W_MSD_0 + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 
plotselection_ABCD_general_beta4_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " + "  &&  " + plotselection_W_MSD_i + "  &&  "+ plotselection_t_MSD_i + " && " + plotselection_tau32_i

plotselection_ABCD_general_beta5 =  plotselection2 + "  &&  "+" Zprimes_ABCD"+radi+"_M>1000 " + "  &&  " + plotselection_t_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass 
plotselection_ABCD_general_beta5_0 =  plotselection2_0 + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0 
plotselection_ABCD_general_beta5_i =  plotselection2_i + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " + "  &&  " + plotselection_t_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i 

plotselection_ABCD_general_beta6 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>1000 " + "  &&  " + plotselection_W_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass 
plotselection_ABCD_general_beta6_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " + "  &&  " + plotselection_W_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0 
plotselection_ABCD_general_beta6_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " + "  &&  " + plotselection_W_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i 

plotselection_ABCD_general_beta7 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>1000 " + "  &&  " + plotselection_W_tau21 + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass 
plotselection_ABCD_general_beta7_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " + "  &&  " + plotselection_W_tau21_0 + " && " + plotselection_tau32_0 + "  &&  " +  plotselection_TprimeMass_0 
plotselection_ABCD_general_beta7_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " + "  &&  " + plotselection_W_tau21_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i 

plotselection_ABCD_general_beta8 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>1000 " + "  &&  " + plotselection_W_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass 
plotselection_ABCD_general_beta8_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0 
plotselection_ABCD_general_beta8_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " + "  &&  " + plotselection_W_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i 

plotselection_ABCD_general_beta9 =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>1000 " + "  &&  " + plotselection_W_MSD + " && " + plotselection_t_MSD + "  &&  " + plotselection_TprimeMass 
plotselection_ABCD_general_beta9_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_t_MSD_0 + "  &&  " + plotselection_TprimeMass_0 
plotselection_ABCD_general_beta9_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " + "  &&  " + plotselection_W_MSD_i + " && " + plotselection_t_MSD_i + "  &&  " + plotselection_TprimeMass_i 

plotselection_ABCD_general_beta10 =  "Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt>200 && Tops_ABCD"+radi+"_Pt>400 && Bottoms_ABCD" + radi + "_Pt>100" + " && (40 < Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD * Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500)  && Ws_ABCD"+radi+"_t21 <0.75" +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M>1000 " + "  &&  " + plotselection_W_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_t_MSD 
plotselection_ABCD_general_beta10_0 =  "Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt[0]>200 && Tops_ABCD"+radi+"_Pt[0]>400 && Bottoms_ABCD" + radi + "_Pt[0]>100" + " && (40 < Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD[0] * Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0]  &&   Tops_ABCD"+radi+"_MSD[0] < 1000)  && Ws_ABCD"+radi+"_t21[0] <0.75" +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_t_MSD_0 
plotselection_ABCD_general_beta10_i =  "Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt[i]>200 && Tops_ABCD"+radi+"_Pt[i]>400 && Bottoms_ABCD" + radi + "_Pt[i]>100" + " && (40 < Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD[i] * Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i]  &&   Tops_ABCD"+radi+"_MSD[i] < 1000)  && Ws_ABCD"+radi+"_t21[i] <0.75" +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " + "  &&  " + plotselection_W_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_t_MSD_i 
