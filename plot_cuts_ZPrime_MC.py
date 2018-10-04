
    
#ABCDversion='ABCD2'  
#ABCDversion='ABCD3'  
ABCDversion='ABCD5'  

#if masscorrection:
    #WPs=WPs+"_masscorr"

# book plots
radi=''


PileUp='CHS'
#PileUp='PUPPI'
#JetDeclustering='SoftDrop'
JetDeclustering='Pruning'
radi=PileUp+JetDeclustering


masscorrection=False
WZwindow=False
#WZwindow=True
#old=True
old=False
MSDgap=False
fullWMSD=True
csvgap=False

#topSJWP='loose'
topSJWP='medium'
#topSJWP='custom'

topWP='loose'
#topWP='medium'
WWP='medium'
#WWP='loose'
bottomWP='medium'
#bottomWP='loose'

WPs='tWP'+topWP+'tSJWP'+topSJWP+'WWP'+WWP+'bWP'+bottomWP

if not csvgap:
    WPs=WPs+"nogap"
if masscorrection:
    WPs=WPs+"_masscorr"
if WZwindow:
    WPs=WPs+"_AnnaWindow"
if MSDgap:
    WPs=WPs+"_MSDgap"
if old:
    WPs=WPs+"_nodynHT"
if fullWMSD:
    WPs=WPs+"_fullWMSD"

plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"



#Own Plotselections for ABCD-method
if topWP=='loose':
    plotselection_tau32 = " Tops_ABCD"+radi+"_t32 < 0.81   "
    plotselection_tau32_i = " Tops_ABCD"+radi+"_t32[i] < 0.81   "
    plotselection_tau32_0 = " Tops_ABCD"+radi+"_t32[0] < 0.81   "
    
    MCSF_top_t32_MSD = " 1.06 "
    MCSF_top_t32anti_MSD = " 1.06 "
    MCSF_top_t32_MSDanti = " 1.06 "
    MCSF_top_t32anti_MSDanti = " 1.06 "
    
    MCSF_top_t32_MSD_up= " 0.09 "
    MCSF_top_t32anti_MSD_up = " 0.09 "
    MCSF_top_t32_MSDanti_up = " 0.09 "
    MCSF_top_t32anti_MSDanti_up = " 0.09 "
    
    MCSF_top_t32_MSD_down = " 0.04 "
    MCSF_top_t32anti_MSD_down = " 0.04 "
    MCSF_top_t32_MSDanti_down = " 0.04 "
    MCSF_top_t32anti_MSDanti_down = " 0.04 "
    
    MCSF_topmiss_t32_MSD = " 1.0 "
    MCSF_topmiss_t32anti_MSD = " 1.0 "
    MCSF_topmiss_t32_MSDanti = " 1.0 "
    MCSF_topmiss_t32anti_MSDanti = " 1.0 "
    
    MCSF_topmiss_t32_MSD_up= " 0.0 "
    MCSF_topmiss_t32anti_MSD_up = " 0.0 "
    MCSF_topmiss_t32_MSDanti_up = " 0.0 "
    MCSF_topmiss_t32anti_MSDanti_up = " 0.0 "
    
    MCSF_topmiss_t32_MSD_down = " 0.00 "
    MCSF_topmiss_t32anti_MSD_down = " 0.00 "
    MCSF_topmiss_t32_MSDanti_down = " 0.00 "
    MCSF_topmiss_t32anti_MSDanti_down = " 0.00 "
    
if topWP=='medium':
    plotselection_tau32 = " Tops_ABCD"+radi+"_t32 < 0.67   "
    plotselection_tau32_i = " Tops_ABCD"+radi+"_t32[i] < 0.67   "
    plotselection_tau32_0 = " Tops_ABCD"+radi+"_t32[0] < 0.67   "
    
    MCSF_top_t32_MSD = " 1.06 "
    MCSF_top_t32anti_MSD = " 1.06 "
    MCSF_top_t32_MSDanti = " 1.06 "
    MCSF_top_t32anti_MSDanti = " 1.06 "
    
    MCSF_top_t32_MSD_up= " 0.08 "
    MCSF_top_t32anti_MSD_up = " 0.08 "
    MCSF_top_t32_MSDanti_up = " 0.08 "
    MCSF_top_t32anti_MSDanti_up = " 0.08 "
    
    MCSF_top_t32_MSD_down = " 0.04 "
    MCSF_top_t32anti_MSD_down = " 0.04 "
    MCSF_top_t32_MSDanti_down = " 0.04 "
    MCSF_top_t32anti_MSDanti_down = " 0.04 "
    
    MCSF_topmiss_t32_MSD = " 1.05 "
    MCSF_topmiss_t32anti_MSD = " 1.05 "
    MCSF_topmiss_t32_MSDanti = " 1.05 "
    MCSF_topmiss_t32anti_MSDanti = " 1.05 "
    
    MCSF_topmiss_t32_MSD_up= " 0.11 "
    MCSF_topmiss_t32anti_MSD_up = " 0.11 "
    MCSF_topmiss_t32_MSDanti_up = " 0.11 "
    MCSF_topmiss_t32anti_MSDanti_up = " 0.11 "
    
    MCSF_topmiss_t32_MSD_down = " 0.05 "
    MCSF_topmiss_t32anti_MSD_down = " 0.05 "
    MCSF_topmiss_t32_MSDanti_down = " 0.05 "
    MCSF_topmiss_t32anti_MSDanti_down = " 0.05 "
    
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
    plotselection_W_tau21 = " Ws_ABCD"+radi+"_t21 < 0.45 "
    plotselection_W_tau21_i = " Ws_ABCD"+radi+"_t21[i] < 0.45  "
    plotselection_W_tau21_0 = " Ws_ABCD"+radi+"_t21[0] < 0.45  "

    plotselection_W_tau21_anti = " Ws_ABCD"+radi+"_t21 > 0.45 "
    plotselection_W_tau21_anti_i = " Ws_ABCD"+radi+"_t21[i]  > 0.45 "
    plotselection_W_tau21_anti_0 = " Ws_ABCD"+radi+"_t21[0]  > 0.45 "

    #MCSF_W_t21_MSD = " 1.10 "
    #MCSF_W_t21anti_MSD = " 0.88 "
    #MCSF_W_t21_MSDanti = " 1.10 "
    #MCSF_W_t21anti_MSDanti = " 0.88 "

    #MCSF_W_t21_MSD_up = " 0.12 "
    #MCSF_W_t21anti_MSD_up = " 0.10 "
    #MCSF_W_t21_MSDanti_up = " 0.12 "
    #MCSF_W_t21anti_MSDanti_up = " 0.10 "

    #MCSF_W_t21_MSD_down = " 0.12 "
    #MCSF_W_t21anti_MSD_down = " 0.10 "
    #MCSF_W_t21_MSDanti_down = " 0.12 "
    #MCSF_W_t21anti_MSDanti_down = " 0.10 "
    if radi=='CHSSoftDrop':
        if WZwindow:
            MCSF_W_t21_MSD = " 0.9 "
            MCSF_W_t21anti_MSD = " 1.0 "
            MCSF_W_t21_MSDanti = " 0.9 "
            MCSF_W_t21anti_MSDanti = " 1.0 "

            MCSF_W_t21_MSD_up = " 0.11 "
            MCSF_W_t21_MSD_down = " 0.09 "
            MCSF_W_t21anti_MSD_up = " 0.11 "
            MCSF_W_t21anti_MSD_down = " 0.09 "
            MCSF_W_t21_MSDanti_up = " 0.11 "
            MCSF_W_t21_MSDanti_down = " 0.09 "
            MCSF_W_t21anti_MSDanti_up = " 0.11 "
            MCSF_W_t21anti_MSDanti_down = " 0.09 "
            
            MCSF_Wmiss_t21_MSD = " 1.05 "
            MCSF_Wmiss_t21anti_MSD = " 1.0 "
            MCSF_Wmiss_t21_MSDanti = " 1.05 "
            MCSF_Wmiss_t21anti_MSDanti = " 1.0 "

            MCSF_Wmiss_t21_MSD_up = " 0.007 "
            MCSF_Wmiss_t21_MSD_down = " 0.007 "

            MCSF_Wmiss_t21anti_MSD_up = " 0.007 "
            MCSF_Wmiss_t21anti_MSD_down = " 0.007 "

            MCSF_Wmiss_t21_MSDanti_up = " 0.007 "
            MCSF_Wmiss_t21_MSDanti_down = " 0.007 "
            
            MCSF_Wmiss_t21anti_MSDanti_up = " 0.007 "
            MCSF_Wmiss_t21anti_MSDanti_down = " 0.007 "
            
        else:
            MCSF_W_t21_MSD = " 1.0 "
            MCSF_W_t21anti_MSD = " 1.0 "
            MCSF_W_t21_MSDanti = " 1.0 "
            MCSF_W_t21anti_MSDanti = " 1.0 "

            MCSF_W_t21_MSD_up = " 0.24 "
            MCSF_W_t21anti_MSD_up = " 0.20 "
            MCSF_W_t21_MSDanti_up = " 0.24 "
            MCSF_W_t21anti_MSDanti_up = " 0.20 "

            MCSF_W_t21_MSD_down = " 0.24 "
            MCSF_W_t21anti_MSD_down = " 0.20 "
            MCSF_W_t21_MSDanti_down = " 0.24 "
            MCSF_W_t21anti_MSDanti_down = " 0.20 "
            
            MCSF_Wmiss_t21_MSD = " 1.0 "
            MCSF_Wmiss_t21anti_MSD = " 1.0 "
            MCSF_Wmiss_t21_MSDanti = " 1.0 "
            MCSF_Wmiss_t21anti_MSDanti = " 1.0 "

            MCSF_Wmiss_t21_MSD_up = " 0.24 "
            MCSF_Wmiss_t21anti_MSD_up = " 0.20 "
            MCSF_Wmiss_t21_MSDanti_up = " 0.24 "
            MCSF_Wmiss_t21anti_MSDanti_up = " 0.20 "

            MCSF_Wmiss_t21_MSD_down = " 0.24 "
            MCSF_Wmiss_t21anti_MSD_down = " 0.20 "
            MCSF_Wmiss_t21_MSDanti_down = " 0.24 "
            MCSF_Wmiss_t21anti_MSDanti_down = " 0.20 "            
            
        
    if radi=='CHSPruning':
            MCSF_W_t21_MSD = " 1.1 "
            MCSF_W_t21anti_MSD = " 0.88 "
            MCSF_W_t21_MSDanti = " 1.0 "
            MCSF_W_t21anti_MSDanti = " 1.0 "

            MCSF_W_t21_MSD_up = " 0.12 "
            MCSF_W_t21anti_MSD_up = " 0.10 "
            MCSF_W_t21_MSDanti_up = " 0.12 "
            MCSF_W_t21anti_MSDanti_up = " 0.10 "

            MCSF_W_t21_MSD_down = " 0.12 "
            MCSF_W_t21anti_MSD_down = " 0.10 "
            MCSF_W_t21_MSDanti_down = " 0.12 "
            MCSF_W_t21anti_MSDanti_down = " 0.10 "
            
            MCSF_Wmiss_t21_MSD = " 1.0 "
            MCSF_Wmiss_t21anti_MSD = " 1.0 "
            MCSF_Wmiss_t21_MSDanti = " 1.0 "
            MCSF_Wmiss_t21anti_MSDanti = " 1.0 "

            MCSF_Wmiss_t21_MSD_up = " 0.12 "
            MCSF_Wmiss_t21anti_MSD_up = " 0.10 "
            MCSF_Wmiss_t21_MSDanti_up = " 0.12 "
            MCSF_Wmiss_t21anti_MSDanti_up = " 0.10 "

            MCSF_Wmiss_t21_MSD_down = " 0.12 "
            MCSF_Wmiss_t21anti_MSD_down = " 0.10 "
            MCSF_Wmiss_t21_MSDanti_down = " 0.12 "
            MCSF_Wmiss_t21anti_MSDanti_down = " 0.10 "   
            
            #MCSF_JetMassScale=" 1.0*(smearWmassfactor(Ws_ABCD"+radi+"_MSD_smeared[i],Ws_ABCD"+radi+"_Phi[i],Ws_ABCD"+radi+"_Eta[i]))[0] "
            #MCSF_JetMassScale_up= " (1.0+0.023)*(smearWmassfactor(Ws_ABCD"+radi+"_MSD_smeared[i],Ws_ABCD"+radi+"_Phi[i],Ws_ABCD"+radi+"_Eta[i]))[0] "
            #MCSF_JetMassScale_down= " (1.0-0.023)*(smearWmassfactor(Ws_ABCD"+radi+"_MSD_smeared[i],Ws_ABCD"+radi+"_Phi[i],Ws_ABCD"+radi+"_Eta[i]))[0] "
            
            #MCSF_JetMassRes=" (smearWmassfactor(Ws_ABCD"+radi+"_MSD_smeared[i],Ws_ABCD"+radi+"_Phi[i],Ws_ABCD"+radi+"_Eta[i]))[0] "
            #MCSF_JetMassScale_up= " (smearWmassfactor(Ws_ABCD"+radi+"_MSD_smeared[i],Ws_ABCD"+radi+"_Phi[i],Ws_ABCD"+radi+"_Eta[i]))[1] "
            #MCSF_JetMassScale_down= " (smearWmassfactor(Ws_ABCD"+radi+"_MSD_smeared[i],Ws_ABCD"+radi+"_Phi[i],Ws_ABCD"+radi+"_Eta[i]))[2] "        
            
            MCSF_JetMassScale=" 1.0 "
            MCSF_JetMassScale_up= " (1.0 + 0.023) "
            MCSF_JetMassScale_down= " (1.0 - 0.023) "
            #MCSF_JetMassScale=" 1.0 "
            #MCSF_JetMassScale_up= " 1.0 "
            #MCSF_JetMassScale_down= " 1.0 "
                

        
            #MCSF_JetMassRes=" 1.0 "
            #MCSF_JetMassScale_up= " 1.0 "
            #MCSF_JetMassScale_down= " 1.0 "             
            
if bottomWP=='medium':
    plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.8484  "    
    plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.8484   "
    plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.8484   " 
    
        
if bottomWP=='loose':
    plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.5426  "    
    plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.5426   "
    plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.5426   " 
    
    
if bottomWP=='tight':
    plotselection_B_CSV = "  Bottoms_ABCD"+radi+"_CSV > 0.935  "    
    plotselection_B_CSV_i = "  Bottoms_ABCD"+radi+"_CSV[i] > 0.935   "
    plotselection_B_CSV_0 = "  Bottoms_ABCD"+radi+"_CSV[0] > 0.935   "

plotselection_tau32_anti=" Tops_ABCD"+radi+"_t32 > 0.81   "
plotselection_tau32_anti_i =" Tops_ABCD"+radi+"_t32[i] > 0.81   "
plotselection_tau32_anti_0 =" Tops_ABCD"+radi+"_t32[0] > 0.81   "



if WZwindow:
   
   plotselection_W_MSD =  " ((60 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3) && ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 115)) "
   plotselection_W_MSD_i =  " ((60 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]) && ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 115)) "
   plotselection_W_MSD_0 =  " ((60 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]) && ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 115)) "
   if not MSDgap:
	plotselection_W_MSD_anti =  " ((60 > Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 > 115)) "
        plotselection_W_MSD_anti_i =  " ((60 > Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] > 115)) "
        plotselection_W_MSD_anti_0 =  " ((60 > Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] > 115)) "
   else:
        plotselection_W_MSD_anti =  " ((60 > Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 > 150)) "
        plotselection_W_MSD_anti_i =  " ((60 > Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] > 150)) "
        plotselection_W_MSD_anti_0 =  " ((60 > Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] > 150)) "
	

else:
   plotselection_W_MSD =  " ((65 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3) && ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 105)) "
   plotselection_W_MSD_i =  " ((65 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]) && ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 105)) "
   plotselection_W_MSD_0 =  " ((65 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]) && ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 105)) "
   
   plotselection_W_MSD_JetMassScaleUp =  " ((65 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3) && ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3 < 105)) "
   plotselection_W_MSD_JetMassScaleUp_i =  " ((65 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i]) && ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i] < 105)) "
   plotselection_W_MSD_JetMassScaleUp_0 =  " ((65 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0]) && ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0] < 105)) "
   
   plotselection_W_MSD_JetMassScaleDown =  " ((65 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3) && ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3 < 105)) "
   plotselection_W_MSD_JetMassScaleDown_i =  " ((65 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i]) && ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i] < 105)) "
   plotselection_W_MSD_JetMassScaleDown_0 =  " ((65 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0]) && ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0] < 105)) "
   
   plotselection_W_MSD_JetMassResUp =  " ((65 < Ws_ABCD"+radi+"_MSD_JetResup*Ws_ABCD"+radi+"_corrL2L3) && ( Ws_ABCD"+radi+"_MSD_JetResup*Ws_ABCD"+radi+"_corrL2L3 < 105)) "
   plotselection_W_MSD_JetMassResUp_i =  " ((65 < Ws_ABCD"+radi+"_MSD_JetResup[i]*Ws_ABCD"+radi+"_corrL2L3[i]) && ( Ws_ABCD"+radi+"_MSD_JetResup[i]*Ws_ABCD"+radi+"_corrL2L3[i] < 105)) "
   plotselection_W_MSD_JetMassResUp_0 =  " ((65 < Ws_ABCD"+radi+"_MSD_JetResup[0]*Ws_ABCD"+radi+"_corrL2L3[0]) && ( Ws_ABCD"+radi+"_MSD_JetResup[0]*Ws_ABCD"+radi+"_corrL2L3[0] < 105)) "
   
   plotselection_W_MSD_JetMassResDown =  " ((65 < Ws_ABCD"+radi+"_MSD_JetResdown*Ws_ABCD"+radi+"_corrL2L3) && ( Ws_ABCD"+radi+"_MSD_JetResdown*Ws_ABCD"+radi+"_corrL2L3 < 105)) "
   plotselection_W_MSD_JetMassResDown_i =  " ((65 < Ws_ABCD"+radi+"_MSD_JetResdown[i]*Ws_ABCD"+radi+"_corrL2L3[i]) && ( Ws_ABCD"+radi+"_MSD_JetResdown[i]*Ws_ABCD"+radi+"_corrL2L3[i] < 105)) "
   plotselection_W_MSD_JetMassResDown_0 =  " ((65 < Ws_ABCD"+radi+"_MSD_JetResdown[0]*Ws_ABCD"+radi+"_corrL2L3[0]) && ( Ws_ABCD"+radi+"_MSD_JetResdown[0]*Ws_ABCD"+radi+"_corrL2L3[0] < 105)) "
   
      
   
      
   if not MSDgap:
        plotselection_W_MSD_anti =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 > 105)) "
        plotselection_W_MSD_anti_i =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] > 105)) "
        plotselection_W_MSD_anti_0 =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] > 105)) "
        
        plotselection_W_MSD_anti_JetMassScaleUp =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3 > 105)) "
        plotselection_W_MSD_anti_JetMassScaleUp_i =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i] > 105)) "
        plotselection_W_MSD_anti_JetMassScaleUp_0 =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0] > 105)) "
        
        plotselection_W_MSD_anti_JetMassScaleDown =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3 > 105)) "
        plotselection_W_MSD_anti_JetMassScaleDown_i =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i] > 105)) "
        plotselection_W_MSD_anti_JetMassScaleDown_0 =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0] > 105)) "

        plotselection_W_MSD_anti_JetMassResUp =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResup*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_JetResup*Ws_ABCD"+radi+"_corrL2L3 > 105)) "
        plotselection_W_MSD_anti_JetMassResUp_i =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResup[i]*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_JetResup[i]*Ws_ABCD"+radi+"_corrL2L3[i] > 105)) "
        plotselection_W_MSD_anti_JetMassResUp_0 =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResup[0]*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_JetResup[0]*Ws_ABCD"+radi+"_corrL2L3[0] > 105)) "
        
        plotselection_W_MSD_anti_JetMassResDown =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResdown*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_JetResdown*Ws_ABCD"+radi+"_corrL2L3 > 105)) "
        plotselection_W_MSD_anti_JetMassResDown_i =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResdown[i]*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_JetResdown[i]*Ws_ABCD"+radi+"_corrL2L3[i] > 105)) "
        plotselection_W_MSD_anti_JetMassResDown_0 =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResdown[0]*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_JetResdown[0]*Ws_ABCD"+radi+"_corrL2L3[0] > 105)) "

                
   else:
        plotselection_W_MSD_anti =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 > 150)) "
        plotselection_W_MSD_anti_i =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] > 150)) "
        plotselection_W_MSD_anti_0 =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] > 150)) "

        plotselection_W_MSD_anti_JetMassScaleUp =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3 > 150)) "
        plotselection_W_MSD_anti_JetMassScaleUp_i =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i] > 150)) "
        plotselection_W_MSD_anti_JetMassScaleUp_0 =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0] > 150)) "

        plotselection_W_MSD_anti_JetMassScaleDown =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3 > 150)) "
        plotselection_W_MSD_anti_JetMassScaleDown_i =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i] > 150)) "
        plotselection_W_MSD_anti_JetMassScaleDown_0 =  " ((65 > Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0] > 150)) "

        plotselection_W_MSD_anti_JetMassResUp =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResup*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_JetResup*Ws_ABCD"+radi+"_corrL2L3 > 150)) "
        plotselection_W_MSD_anti_JetMassResUp_i =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResup[i]*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_JetResup[i]*Ws_ABCD"+radi+"_corrL2L3[i] > 150)) "
        plotselection_W_MSD_anti_JetMassResUp_0 =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResup[0]*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_JetResup[0]*Ws_ABCD"+radi+"_corrL2L3[0] > 150)) "

        plotselection_W_MSD_anti_JetMassResDown =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResdown*Ws_ABCD"+radi+"_corrL2L3)  ||  ( Ws_ABCD"+radi+"_MSD_JetResdown*Ws_ABCD"+radi+"_corrL2L3 > 150)) "
        plotselection_W_MSD_anti_JetMassResDown_i =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResdown[i]*Ws_ABCD"+radi+"_corrL2L3[i])  ||  ( Ws_ABCD"+radi+"_MSD_JetResdown[i]*Ws_ABCD"+radi+"_corrL2L3[i] > 150)) "
        plotselection_W_MSD_anti_JetMassResDown_0 =  " ((65 > Ws_ABCD"+radi+"_MSD_JetResdown[0]*Ws_ABCD"+radi+"_corrL2L3[0])  ||  ( Ws_ABCD"+radi+"_MSD_JetResdown[0]*Ws_ABCD"+radi+"_corrL2L3[0] > 150)) "



if csvgap:
   plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.5426   "
   plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.5426   "
   plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.5426   "

else:
 if bottomWP=='medium':   
   plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.8484   "
   plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.8484   "
   plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.8484   "
 if bottomWP=='loose':   
   plotselection_B_CSV_anti = "  Bottoms_ABCD"+radi+"_CSV < 0.5426   "
   plotselection_B_CSV_anti_i = "  Bottoms_ABCD"+radi+"_CSV[i] < 0.5426   "
   plotselection_B_CSV_anti_0 = "  Bottoms_ABCD"+radi+"_CSV[0] < 0.5426   "
   
if WZwindow:
	plotselection_t_MSD = " ((150 < Tops_ABCD"+radi+"_MSD) && (Tops_ABCD"+radi+"_MSD < 240)) "
	plotselection_t_MSD_i = " ((150 < Tops_ABCD"+radi+"_MSD[i]) && (Tops_ABCD"+radi+"_MSD[i]< 240)) "
	plotselection_t_MSD_0 = " ((150 < Tops_ABCD"+radi+"_MSD[0]) && (Tops_ABCD"+radi+"_MSD[0]< 240)) "
        plotselection_t_MSD_anti = " ((150 > Tops_ABCD"+radi+"_MSD) || (Tops_ABCD"+radi+"_MSD > 240)) "
        plotselection_t_MSD_anti_i = " ((150 > Tops_ABCD"+radi+"_MSD[i]) || (Tops_ABCD"+radi+"_MSD[i]> 240)) "
        plotselection_t_MSD_anti_0 = " ((150 > Tops_ABCD"+radi+"_MSD[0]) || (Tops_ABCD"+radi+"_MSD[0]> 240)) "

else:	
	plotselection_t_MSD = " ((105 < Tops_ABCD"+radi+"_MSD) && (Tops_ABCD"+radi+"_MSD < 210)) "
        plotselection_t_MSD_i = " ((105 < Tops_ABCD"+radi+"_MSD[i]) && (Tops_ABCD"+radi+"_MSD[i]< 210)) "
        plotselection_t_MSD_0 = " ((105 < Tops_ABCD"+radi+"_MSD[0]) && (Tops_ABCD"+radi+"_MSD[0]< 210)) "
	plotselection_t_MSD_anti = " ((105 > Tops_ABCD"+radi+"_MSD) || (Tops_ABCD"+radi+"_MSD > 210)) "
	plotselection_t_MSD_anti_i = " ((105 > Tops_ABCD"+radi+"_MSD[i]) || (Tops_ABCD"+radi+"_MSD[i]> 210)) "
	plotselection_t_MSD_anti_0 = " ((105 > Tops_ABCD"+radi+"_MSD[0]) || (Tops_ABCD"+radi+"_MSD[0]> 210)) "


plotselection_t_MSD = " ((105 < Tops_ABCD"+radi+"_MSD) && (Tops_ABCD"+radi+"_MSD < 210)) "
plotselection_t_MSD_i = " ((105 < Tops_ABCD"+radi+"_MSD[i]) && (Tops_ABCD"+radi+"_MSD[i]< 210)) "
plotselection_t_MSD_0 = " ((105 < Tops_ABCD"+radi+"_MSD[0]) && (Tops_ABCD"+radi+"_MSD[0]< 210)) "
plotselection_t_MSD_anti = " ((105 > Tops_ABCD"+radi+"_MSD) || (Tops_ABCD"+radi+"_MSD > 210)) "
plotselection_t_MSD_anti_i = " ((105 > Tops_ABCD"+radi+"_MSD[i]) || (Tops_ABCD"+radi+"_MSD[i]> 210)) "
plotselection_t_MSD_anti_0 = " ((105 > Tops_ABCD"+radi+"_MSD[0]) || (Tops_ABCD"+radi+"_MSD[0]> 210)) "

if topSJWP=='medium':
    
    
    plotselection_topsubjetCSVv2 = " Tops_ABCD"+radi+"_maxsubjetCSVv2 > 0.8484 "
    plotselection_topsubjetCSVv2_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] > 0.8484 "
    plotselection_topsubjetCSVv2_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] > 0.8484 "

    plotselection_topsubjetCSVv2_anti = " Tops_ABCD"+radi+"_maxsubjetCSVv2 < 0.8484 "
    plotselection_topsubjetCSVv2_anti_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] < 0.8484 "
    plotselection_topsubjetCSVv2_anti_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] < 0.8484 "
    
elif topSJWP=='custom':
    
    plotselection_topsubjetCSVv2 = " Tops_ABCD"+radi+"_maxsubjetCSVv2 > 0.75 "
    plotselection_topsubjetCSVv2_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] > 0.75 "
    plotselection_topsubjetCSVv2_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] > 0.75 "

    plotselection_topsubjetCSVv2_anti = " Tops_ABCD"+radi+"_maxsubjetCSVv2 < 0.75 "
    plotselection_topsubjetCSVv2_anti_i = " Tops_ABCD"+radi+"_maxsubjetCSVv2[i] < 0.75 "
    plotselection_topsubjetCSVv2_anti_0 = " Tops_ABCD"+radi+"_maxsubjetCSVv2[0] < 0.75 "        
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


plotselection_W_MSD_one_sided =  " ((65 < Ws_ABCD_MSD && Ws_ABCD_MSD < 105)"
plotselection_W_MSD_one_sided_anti =  " ((65 > Ws_ABCD_MSD && Ws_ABCD_MSD < 105)"




plotselection_sideband = "Signal_Topfirst_Zprime_M < 0"
plotselection_sideband_withtopbtag = "Signal_withtopbtag_Topfirst_Zprime_M < 0"





if old:
    plotselection1="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt>200 && Tops_ABCD"+radi+"_Pt>400 && Bottoms_ABCD" + radi + "_Pt>100"
    plotselection1_i="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt[i]>200 && Tops_ABCD"+radi+"_Pt[i]>400 && Bottoms_ABCD" + radi + "_Pt[i]>100"
    plotselection1_0="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt[0]>200 && Tops_ABCD"+radi+"_Pt[0]>400 && Bottoms_ABCD" + radi + "_Pt[0]>100"
    #plotselection_EvtHT="Evt_HT_Jets>(0*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(10*Zprimes_ABCD" +  radi + "_M)"
    #plotselection_EvtHT_i="Evt_HT_Jets>(0*Zprimes_ABCD" +  radi + "_M[i]) && Evt_HT_Jets<(10*Zprimes_ABCD" +  radi + "_M[i])"
    #plotselection_EvtHT_0="Evt_HT_Jets>(0*Zprimes_ABCD" +  radi + "_M[0]) && Evt_HT_Jets<(10*Zprimes_ABCD" +  radi + "_M[0])"
else:
    plotselection1="Evt_HT_Jets>1000 && Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M) && Ws_ABCD"+radi+"_Pt>200 && Tops_ABCD"+radi+"_Pt>400 && Bottoms_ABCD" + radi + "_Pt>100"
    plotselection1_i="Evt_HT_Jets>1000 && Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M[i]) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M[i]) && Ws_ABCD"+radi+"_Pt[i]>200 && Tops_ABCD"+radi+"_Pt[i]>400 && Bottoms_ABCD" + radi + "_Pt[i]>100"
    plotselection1_0="Evt_HT_Jets>1000 && Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M[0]) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M[0]) && Ws_ABCD"+radi+"_Pt[0]>200 && Tops_ABCD"+radi+"_Pt[0]>400 && Bottoms_ABCD" + radi + "_Pt[0]>100"
    #plotselection1="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt>200 && Tops_ABCD"+radi+"_Pt>400 && Bottoms_ABCD" + radi + "_Pt>100"
    #plotselection1_i="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt[i]>200 && Tops_ABCD"+radi+"_Pt[i]>400 && Bottoms_ABCD" + radi + "_Pt[i]>100"
    #plotselection1_0="Evt_HT_Jets>1000 && Ws_ABCD"+radi+"_Pt[0]>200 && Tops_ABCD"+radi+"_Pt[0]>400 && Bottoms_ABCD" + radi + "_Pt[0]>100"
    #plotselection_EvtHT="Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M)"
    #plotselection_EvtHT_i="Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M[i]) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M[i])"
    #plotselection_EvtHT_0="Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M[0]) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M[0])"

if not MSDgap:
	plotselection2=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) "
	plotselection2_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 300) "
	plotselection2_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 300) "


	plotselection2_JetMassScaleUp=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3 < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) "
	plotselection2_JetMassScaleUp_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 300) "
	plotselection2_JetMassScaleUp_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 300) "

	plotselection2_JetMassScaleDown=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3 < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) "
	plotselection2_JetMassScaleDown_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 300) "
	plotselection2_JetMassScaleDown_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 300) "
	
	plotselection2_JetMassResUp=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResup*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_JetResup*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) "
	plotselection2_JetMassResUp_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_JetResup[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_JetResup[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 300) "
	plotselection2_JetMassResUp_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResup[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_JetResup[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 300) "
	
	plotselection2_JetMassResDown=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResdown*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_JetResdown*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 300) "
	plotselection2_JetMassResDown_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_JetResdown[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_JetResdown[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 300) "
	plotselection2_JetMassResDown_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResdown[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_JetResdown[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 130) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 300) "	
	
	
	
	
else:
	plotselection2=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 500) "
        plotselection2_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 500) "
        
        
	plotselection2_JetMassScaleUp=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_JetMassScaleUp_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 500) "
        plotselection2_JetMassScaleUp_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 500) "
        
	plotselection2_JetMassScaleDown=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_JetMassScaleDown_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 500) "
        plotselection2_JetMassScaleDown_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 500) "        
        
	plotselection2_JetMassResUp=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResup*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_JetResup*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_JetMassResUp_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_JetResup[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_JetResup[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 500) "
        plotselection2_JetMassResUp_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResup[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_JetResup[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 500) "
        
	plotselection2_JetMassResDown=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResdown*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_JetResdown*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_JetMassResDown_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_JetResdown[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_JetResdown[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 500) "
        plotselection2_JetMassResDown_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResdown[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_JetResdown[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 500) "        
        
        
if fullWMSD:
        plotselection2=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 500) "
        plotselection2_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 500) "
        
        
        plotselection2_JetMassScaleUp=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_JetMassScaleUp_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 500) "
        plotselection2_JetMassScaleUp_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_up+"*Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 500) "
                
        plotselection2_JetMassScaleDown=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_smeared*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_JetMassScaleDown_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_smeared[i]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 500) "
        plotselection2_JetMassScaleDown_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_smeared[0]*"+MCSF_JetMassScale_down+"*Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 500) "
        
        plotselection2_JetMassResUp=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResup*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_JetResup*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_JetMassResUp_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_JetResup[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_JetResup[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 500) "
        plotselection2_JetMassResUp_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResup[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_JetResup[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 500) "
                
        plotselection2_JetMassResDown=plotselection1 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResdown*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3  &&   Ws_ABCD"+radi+"_MSD_JetResdown*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3 < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD  &&   Tops_ABCD"+radi+"_MSD < 500) "
        plotselection2_JetMassResDown_i=plotselection1_i + " && (40 < Ws_ABCD"+radi+"_MSD_JetResdown[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i]  &&   Ws_ABCD"+radi+"_MSD_JetResdown[i]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[i] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[i] &&   Tops_ABCD"+radi+"_MSD[i]< 500) "
        plotselection2_JetMassResDown_0=plotselection1_0 + " && (40 < Ws_ABCD"+radi+"_MSD_JetResdown[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0]  &&   Ws_ABCD"+radi+"_MSD_JetResdown[0]*"+MCSF_JetMassScale+"*Ws_ABCD"+radi+"_corrL2L3[0] < 500) " + " && (40 < Tops_ABCD"+radi+"_MSD[0] &&   Tops_ABCD"+radi+"_MSD[0]< 500) "
                

plotselection3=plotselection1 + "&&" + "N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200"




#plotselection_ABCD1_general =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  "+ plotselection_TprimeMass + "  &&  "+ plotselection_W_MSD + " && " + plotselection_t_MSD   
#plotselection_ABCD1_general_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "   &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_t_MSD_0  
#plotselection_ABCD1_general_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_W_MSD_i + " && " + plotselection_t_MSD_i  

#plotselection_ABCD2_general =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  " + plotselection_TprimeMass + "  &&  "+ plotselection_W_MSD + " && " + plotselection_tau32 
#plotselection_ABCD2_general_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "  &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_W_MSD_0 + " && " + plotselection_tau32_0  
#plotselection_ABCD2_general_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_W_MSD_i + " && " + plotselection_tau32_i  

#plotselection_ABCD3_general =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  " + plotselection_TprimeMass + "  &&  "+ plotselection_t_MSD + " && " + plotselection_tau32  
#plotselection_ABCD3_general_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "  &&  " + plotselection_TprimeMass_0 + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0  
#plotselection_ABCD3_general_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_TprimeMass_i + "  &&  "+ plotselection_t_MSD_i + " && " + plotselection_tau32_i  

#plotselection_ABCD4_general =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  " + plotselection_W_MSD + "  &&  "+ plotselection_t_MSD + " && " + plotselection_tau32  
#plotselection_ABCD4_general_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "  &&  " + plotselection_W_MSD_0 + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0  
#plotselection_ABCD4_general_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_W_MSD_i + "  &&  "+ plotselection_t_MSD_i + " && " + plotselection_tau32_i  





plotselection_ABCD5_general =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  " + plotselection_t_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass  
plotselection_ABCD5_general_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0  
plotselection_ABCD5_general_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_t_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i  


plotselection_ABCD5_general_JetMassScaleUp =  plotselection2_JetMassScaleUp +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  " + plotselection_t_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass  
plotselection_ABCD5_general_JetMassScaleUp_0 =  plotselection2_JetMassScaleUp_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0  
plotselection_ABCD5_general_JetMassScaleUp_i =  plotselection2_JetMassScaleUp_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_t_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i  

plotselection_ABCD5_general_JetMassScaleDown =  plotselection2_JetMassScaleDown +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  " + plotselection_t_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass  
plotselection_ABCD5_general_JetMassScaleDown_0 =  plotselection2_JetMassScaleDown_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0  
plotselection_ABCD5_general_JetMassScaleDown_i =  plotselection2_JetMassScaleDown_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_t_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i  

plotselection_ABCD5_general_JetMassResUp =  plotselection2_JetMassResUp +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  " + plotselection_t_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass  
plotselection_ABCD5_general_JetMassResUp_0 =  plotselection2_JetMassResUp_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0  
plotselection_ABCD5_general_JetMassResUp_i =  plotselection2_JetMassResUp_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_t_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i  

plotselection_ABCD5_general_JetMassResDown =  plotselection2_JetMassResDown +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  " + plotselection_t_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass  
plotselection_ABCD5_general_JetMassResDown_0 =  plotselection2_JetMassResDown_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "  &&  "+ plotselection_t_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0  
plotselection_ABCD5_general_JetMassResDown_i =  plotselection2_JetMassResDown_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_t_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i  










#plotselection_ABCD6_general =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  " + plotselection_W_MSD + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass   
#plotselection_ABCD6_general_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "  &&  " + plotselection_W_MSD_0 + " && " + plotselection_tau32_0 + "  &&  " + plotselection_TprimeMass_0  
#plotselection_ABCD6_general_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_W_MSD_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i  

#plotselection_ABCD7_general =  plotselection2 +  "  &&  " + " Ws_ABCD"+radi+"_Pt>200" +  "  &&  " + " Zprimes_ABCD"+radi+"_M>1000 " +  "  &&  " + " Zprimes_ABCD"+radi+"_M<14000 " + "  &&  " + plotselection_W_tau21 + " && " + plotselection_tau32 + "  &&  " + plotselection_TprimeMass  
#plotselection_ABCD7_general_0 =  plotselection2_0 +  "  &&  " + " Ws_ABCD"+radi+"_Pt[0]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[0]<14000 " + "  &&  " + plotselection_W_tau21_0 + " && " + plotselection_tau32_0 + "  &&  " +  plotselection_TprimeMass_0  
#plotselection_ABCD7_general_i =  plotselection2_i +  "  &&  " + " Ws_ABCD"+radi+"_Pt[i]>200" + "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]>1000 " +  "  &&  "+ " Zprimes_ABCD"+radi+"_M[i]<14000 " + "  &&  " + plotselection_W_tau21_i + " && " + plotselection_tau32_i + "  &&  " + plotselection_TprimeMass_i  



