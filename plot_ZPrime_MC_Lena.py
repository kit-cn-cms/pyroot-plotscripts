

#############
# plot general control distributions 
##############

from plotconfig_Zprime_MC_Lena import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos

name='Zprime_MC'


# definition of categories

#categoriesZprimeTprime=[
#	("(tWb&&N_BTagsM=1)","tWb1",""),#
#	("(tWb&&N_BTagsM=2)","tWb2",""),
#	("(ttH&&N_BTagsM=1)","ttH1",""),
#	("(ttH&&N_BTagsM=2)","ttH2",""),
#	("(ttH&&N_BTagsM=3)","ttH3",""),
#	("(ttH&&N_BTagsM=4)","ttH4",""),
#	("(ttZ)","ttZ",""),
#]

# book plots
plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
#plotselection="N_packedPatJetsAK8PFCHSSoftDrop>=2&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200&&Evt_HT>850"
plotselection1="Evt_HT>850"
#plotselection1=""
plotselection2="N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 && Evt_HT>850 "



#Own Plotselections for ABCD-method
plotselection_ABCD_general =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    Ws_ABCD_t21 >  0.6    &&    100 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210   "

plotselection_tau32 = " Tops_ABCD_t32 < 0.86   "
plotselection_W_MSD =  " 70 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 100 "
plotselection_B_CSV = "  Bottoms_ABCD_CSV > 0.8   "

plotselection_tau32_anti = "not (  " +plotselection_tau32+ " ) "
plotselection_W_MSD_anti = " not (  " +plotselection_W_MSD+ " ) "
plotselection_B_CSV_anti = " not (  " +plotselection_B_CSV+ " ) "




plotselection_ABCD_general_0 =  plotselection2 + "&& Zprimes_ABCD_M[0]>0   &&    Ws_ABCD_t21[0] >  0.6    &&    100 < Tops_ABCD_MSD[0]     &&    Tops_ABCD_MSD[0]  < 210   "

plotselection_tau32_0 = " Tops_ABCD_t32[0] < 0.86   "
plotselection_W_MSD_0 =  " 70 < Ws_ABCD_MSD[0]  &&   Ws_ABCD_MSD[0] < 100 "
plotselection_B_CSV_0 = "  Bottoms_ABCD_CSV[0] > 0.8   "

plotselection_tau32_anti_0 = "!(  " +plotselection_tau32_0+ " ) "
plotselection_W_MSD_anti_0 = " ! (  " +plotselection_W_MSD_0+ " ) "
plotselection_B_CSV_anti_0 = " ! (  " +plotselection_B_CSV_0+ " ) "








#Create Plots

plots=[
    #Signalregion
    Plot(ROOT.TH1F("Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
    #One Anti
    Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-btag",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0","1 anti-btag"),
    Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-Wtag",50,0,5000),"Sideband_W_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 anti-Wtag"),
    Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 anti-ttag"),

    #Two Anti
    Plot(ROOT.TH1F("Sideband_top_anti_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag + anti-btag",50,0,5000),"Sideband_top_anti_bottom_anti_Topfirst_Zprime_M",plotselection2		+"&&Sideband_top_anti_bottom_anti_Topfirst_Zprime_M>0","1 anti-ttag + 1 anti-btag"),
    Plot(ROOT.TH1F("Sideband_W_anti_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-Wtag + anti-btag",50,0,5000),"Sideband_W_anti_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_W_anti_bottom_anti_Topfirst_Zprime_M>0","1 anti-Wtag + 1 anti-btag"),
    Plot(ROOT.TH1F("Sideband_top_anti_W_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag + anti-Wtag",50,0,5000),"Sideband_top_anti_W_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_W_anti_Topfirst_Zprime_M>0","1 anti-ttag + 1 anti-Wtag"),

    #Three Anti        
    Plot(ROOT.TH1F("Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag + anti-Wtag + anti-ttag",50,0,5000),"Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M>0","1 anti-ttag + 1 anti-Wtag + 1 anti-ttag"),	
    
    
    
    
    #All elements
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_top_MSD" ,"tau_{32}(t) VS m_{SD}(t)",20,0,1,30,0,300),"Tops_ABCD_MSD","Tops_ABCD_t32",plotselection2+"&&Tops_ABCD_MSD>0 && Tops_ABCD_t32>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_W_tau21" ,"tau_{32}(t) VS tau_{21}(W)",20,0,1,20,0,1),"Tops_ABCD_t32","Ws_ABCD_t21",plotselection2+"&&Tops_ABCD_t32>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_W_MSD" ,"tau_{32}(t) VS m_{SD}(W)",20,0,1,30,0,300),"Tops_ABCD_t32","Ws_ABCD_MSD",plotselection2+"&&Tops_ABCD_t32>0 && Ws_ABCD_MSD>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2+"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_W_tau21" ,"m_{SD}(t) VS tau_{21}(W)",30,0,300,20,0,1),"Tops_ABCD_MSD","Ws_ABCD_t21",plotselection2+"&&Tops_ABCD_MSD>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_W_MSD" ,"m_{SD}(t) VS m_{SD}(t)(W)",30,0,300,30,0,300),"Tops_ABCD_MSD","Ws_ABCD_MSD",plotselection2+"&&Tops_ABCD_MSD>0 && Ws_ABCD_MSD>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(t) VS CSV_v2(b)",30,0,300,20,0,1),"Tops_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2+"&&Tops_ABCD_MSD>0 && Bottoms_ABCD_CSV>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_W_MSD_vs_W_tau21" ,"m_{SD}(W) VS tau_{21}(W)",30,0,300,20,0,1),"Ws_ABCD_MSD","Ws_ABCD_t21",plotselection2+"&&Ws_ABCD_MSD>0 && Ws_ABCD_t21>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_W_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",30,0,300,20,0,1),"Ws_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2+"&&Ws_ABCD_MSD>0 &&Bottoms_ABCD_CSV>0","1 btag"),
    
    
    # Only first Element (not working)
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_top_MSD_dbl" ,"tau_{32}(t) VS m_{SD}(t) dbl",20,0,1,30,0,300),"Tops_ABCD_MSD[0]","Tops_ABCD_t32[0]",plotselection2+"&&Tops_ABCD_MSD[0]>0 && Tops_ABCD_t32[0]>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_W_tau21_dbl" ,"tau_{32}(t) VS tau_{21}(W) dbl",20,0,1,20,0,1),"Tops_ABCD_t32[0]","Ws_ABCD_t21[0]",plotselection2+"&&Tops_ABCD_t32[0]>0 && Ws_ABCD_t21[0]>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_W_MSD_dbl" ,"tau_{32}(t) VS m_{SD}(W) dbl",20,0,1,30,0,300),"Tops_ABCD_t32[0]","Ws_ABCD_MSD[0]",plotselection2+"&&Tops_ABCD_t32[0]>0 && Ws_ABCD_MSD[0]>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_Bottom_CSV_v2_dbl" ,"tau_{32}(t) VS CSV_v2(b) dbl",20,0,1,20,0,1),"Tops_ABCD_t32[0]","Bottoms_ABCD_CSV[0]",plotselection2+"&&Tops_ABCD_t32[0]>0 && Bottoms_ABCD_CSV[0]>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_W_tau21_dbl" ,"m_{SD}(t) VS tau_{21}(W) dbl",30,0,300,20,0,1),"Tops_ABCD_MSD[0]","Ws_ABCD_t21[0]",plotselection2+"&&Tops_ABCD_MSD[0]>0 && Ws_ABCD_t21[0]>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_W_MSD_dbl" ,"m_{SD}(t) VS m_{SD}(t)(W) dbl",30,0,300,30,0,300),"Tops_ABCD_MSD[0]","Ws_ABCD_MSD[0]",plotselection2+"&&Tops_ABCD_MSD[0]>0 && Ws_ABCD_MSD[0]>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_Bottom_CSV_v2_dbl" ,"m_{SD}(t) VS CSV_v2(b) dbl",30,0,300,20,0,1),"Tops_ABCD_MSD[0]","Bottoms_ABCD_CSV[0]",plotselection2+"&&Tops_ABCD_MSD[0]>0 && Bottoms_ABCD_CSV[0]>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_W_MSD_vs_W_tau21_dbl" ,"m_{SD}(W) VS tau_{21}(W) dbl",30,0,300,20,0,1),"Ws_ABCD_MSD[0]","Ws_ABCD_t21[0]",plotselection2+"&&Ws_ABCD_MSD[0]>0 && Ws_ABCD_t21[0]>0","1 btag"),
    TwoDimPlot(ROOT.TH2F("ABCD_W_MSD_vs_Bottom_CSV_v2_dbl" ,"m_{SD}(W) VS CSV_v2(b) dbl",30,0,300,20,0,1),"Ws_ABCD_MSD[0]","Bottoms_ABCD_CSV[0]",plotselection2+"&&Ws_ABCD_MSD[0]>0 &&Bottoms_ABCD_CSV[0]>0","1 btag") ,


    # Plots for ZPrime_M - with right plotselection - All Elements
    Plot(ROOT.TH1F("ABCD_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD, "1 btag"),
    Plot(ROOT.TH1F("ABCD_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD  ,"1 btag"),


    Plot(ROOT.TH1F("ABCD_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_MSD_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_MSD_anti  ,"1 btag"),


    



    
    # Plots for Z_Prime_M - right plotselection - Only First Element
    Plot(ROOT.TH1F("ABCD_CatA_Zprime_M_first" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M[0]",    plotselection_ABCD_general_0 + " && " + plotselection_tau32_0 + "&&" + plotselection_B_CSV_0 + "&& " + plotselection_W_MSD_0  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatB_Zprime_M_first" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M[0]",    plotselection_ABCD_general_0 + " && " + plotselection_tau32_anti_0 + "&&" + plotselection_B_CSV_0 + "&& " + plotselection_W_MSD_0  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatC_Zprime_M_first" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M[0]",    plotselection_ABCD_general_0 + " && " + plotselection_tau32_0 + "&&" + plotselection_B_CSV_anti_0 + "&& " + plotselection_W_MSD_0  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatD_Zprime_M_first" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M[0]",    plotselection_ABCD_general_0 + " && " + plotselection_tau32_anti_0 + "&&" + plotselection_B_CSV_anti_0 + "&& " + plotselection_W_MSD_0  ,"1 btag"),


    Plot(ROOT.TH1F("ABCD_CatE_Zprime_M_first" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M[0]",    plotselection_ABCD_general_0 + " && " + plotselection_tau32_0 + "&&" + plotselection_B_CSV_0 + "&& " + plotselection_W_MSD_anti_0  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatF_Zprime_M_first" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M[0]",    plotselection_ABCD_general_0 + " && " + plotselection_tau32_anti_0 + "&&" + plotselection_B_CSV_0 + "&& " + plotselection_W_MSD_anti_0  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatG_Zprime_M_first" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M[0]",    plotselection_ABCD_general_0 + " && " + plotselection_tau32_0  + "&&" + plotselection_B_CSV_anti_0 + "&& " + plotselection_W_MSD_anti_0  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD_CatH_Zprime_M_first" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M[0]",    plotselection_ABCD_general_0 + " && " + plotselection_tau32_anti_0 + "&&" + plotselection_B_CSV_anti_0 + "&& " + plotselection_W_MSD_anti_0  ,"1 btag"),


    
    
]



plotnames=[]
for i in plots:
    plotnames.append(i.name)





print name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,4000000,plots,samples)
outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples)
#outputpathBackground=plotParallel(name,4000000,plots,BackgroundSamples)
#outputpathData=plotParallel(name,4000000,plots,DataSamples)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)

# listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples,plots,1 )
listOfHistoListsBackground=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples,plots,1)
listOfHistoListsABCD=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples ,plots,1,[""], True ) #needed? Same as  Background?






labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)


lolBackgroundT=transposeLOL(listOfHistoListsBackground)
lolABCDT=transposeLOL(listOfHistoListsABCD)

#lolDataT=transposeLOL(listOfHistoListsData)


#Stack Plot, Background and Signal, Z_Prime_M
#writeLOLSeveralOnTop(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1])[:plotnames.index("Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M")+1],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1],transposeLOL(lolSignalT),SignalSamples,-0.2,'Zprime',False ,'histoE','samehistoE')
#print "plot_Zprime_MC_Lena Len(listOfHistoListsABCD):"+str( len(listOfHistoListsABCD) )


# writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('ABCD_W_MSD_vs_Bottom_CSV_v2')+1], BackgroundSamples , plotnames[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('ABCD_W_MSD_vs_Bottom_CSV_v2')+1], 'ABCD' , True, False, False, "colz", False, False, False, True)



# Correlationfactor
# writeCorrLOL( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('ABCD_W_MSD_vs_Bottom_CSV_v2')+1], "Correlationlist.txt", plotnames[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('ABCD_W_MSD_vs_Bottom_CSV_v2')+1], ["tt-bar", "QCD_HT", "QCD_Pt", "QCD_comb"] , True )


#Background Estimation with ABCD-Methode, wrong Tags
# multiplyHistos( listOfHistoListsBackground, plotnames.index("Sideband_bottom_anti_Topfirst_Zprime_M") , plotnames.index("Sideband_top_anti_Topfirst_Zprime_M"), False, 1 )
# divideHistos( listOfHistoListsBackground, plotnames.index("Sideband_bottom_anti_Topfirst_Zprime_M"), plotnames.index("Sideband_top_anti_bottom_anti_Topfirst_Zprime_M"), False, 1 )


# BackgroundEstimation = [ listOfHistoListsBackground[  plotnames.index("Sideband_bottom_anti_Topfirst_Zprime_M") ][i].Clone() for i in range(3) ]

# for Histo, SampleName in zip(RegionB, SampleNames):
#     Histo.SetName( "ABCD_Background_Estimation_"+SampleName )
    

# listOfHistoListsBackground.append(BackgroundEstimation)
# plotnames.append( [ ] )
# listOfHistoListsBackground.append(RegionC)
# listOfHistoListsBackground.append(RegionA)


# def BackgoundEstimationABCD(plots, plotnames, variable1, variable2):
#     # Clone Region B ( variable1 and not variable2 )
#     #Multiply and Divide, multiply( B C), divide( B , A )
#     #Set Name?
#     #append B zu plots
#     #Append name of B to plotnames

# def BackgoundEstimationABCDEFGH(plots, plotnames, varibale1, variable2, variable3, variable4):
#     #analog zu anderer Funktion, aber B hier variable 1 and not variable2, variable3, variable4) usw





# #Compare Background in SignalRegion With BackgoundEstimation from ABCD
# SampleNames=['ttbar' , 'QCD_HT', 'QCD_Pt' ]
# writeListOfHistoLists( transposeLOL(listOfHistoListsBackground[plotnames.index('Signal_Topfirst_Zprime_M'):plotnames.index('Sideband_bottom_anti_Topfirst_Zprime_M') +1]) , BackgroundSamples , SampleNames , 'ABCD_ZPrime_M' , False , False, False, "histoE", False, False, True, False)



#ABCD-Z_Prime_Plots Work?
writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_CatA_Zprime_M'):plotnames.index('ABCD_CatE_Zprime_M')+1], BackgroundSamples , plotnames[plotnames.index('ABCD_CatA_Zprime_M'):plotnames.index('ABCD_CatE_Zprime_M')+1], 'ABCD' , True, False, False, "histoE", False, False, False, True)




print "Plotnames contains:"
for i in plotnames:
    print i
    
