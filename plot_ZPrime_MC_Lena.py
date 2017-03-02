
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
plots=[
	#Signal
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

	
        TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_top_MSD" ,"tau_{32}(t) VS m_{SD}(t)",20,0,1,30,0,300),"Tops_ABCD_MSD","Tops_ABCD_t32",plotselection2+"&&Tops_ABCD_MSD>0 && Tops_ABCD_t32>0","1 btag"),
        TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_W_tau21" ,"tau_{32}(t) VS tau_{21}(W)",20,0,1,20,0,1),"Tops_ABCD_t32","Ws_ABCD_t21",plotselection2+"&&Tops_ABCD_t32>0 && Ws_ABCD_t21>0","1 btag"),
        TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_W_MSD" ,"tau_{32}(t) VS m_{SD}(W)",20,0,1,30,0,300),"Tops_ABCD_t32","Ws_ABCD_MSD",plotselection2+"&&Tops_ABCD_t32>0 && Ws_ABCD_MSD>0","1 btag"),
        TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2+"&&Tops_ABCD_t32>0 && Bottoms_ABCD_CSV>0","1 btag"),
        TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_W_tau21" ,"m_{SD}(t) VS tau_{21}(W)",30,0,300,20,0,1),"Tops_ABCD_MSD","Ws_ABCD_t21",plotselection2+"&&Tops_ABCD_MSD>0 && Ws_ABCD_t21>0","1 btag"),
        TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_W_MSD" ,"m_{SD}(t) VS m_{SD}(t)(W)",30,0,300,30,0,300),"Tops_ABCD_MSD","Ws_ABCD_MSD",plotselection2+"&&Tops_ABCD_MSD>0 && Ws_ABCD_MSD>0","1 btag"),
        TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(t) VS CSV_v2(b)",30,0,300,20,0,1),"Tops_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2+"&&Tops_ABCD_MSD>0 && Bottoms_ABCD_CSV>0","1 btag"),
        TwoDimPlot(ROOT.TH2F("ABCD_W_MSD_vs_W_tau21" ,"m_{SD}(W) VS tau_{21}(W)",30,0,300,20,0,1),"Ws_ABCD_MSD","Ws_ABCD_t21",plotselection2+"&&Ws_ABCD_MSD>0 && Ws_ABCD_t21>0","1 btag"),
        TwoDimPlot(ROOT.TH2F("ABCD_W_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",30,0,300,20,0,1),"Ws_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2+"&&Ws_ABCD_MSD>0 &&Bottoms_ABCD_CSV>0","1 btag"),

      
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

#listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples,plots,1 )
#listOfHistoListsBackground=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples,plots,1)
listOfHistoListsABCD=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples ,plots,1,[""], True )





labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)

#lolSignalT=transposeLOL(listOfHistoListsSignal)
#lolBackgroundT=transposeLOL(listOfHistoListsBackground)
lolABCDT=transposeLOL(listOfHistoListsABCD)

#lolDataT=transposeLOL(listOfHistoListsData)



#writeLOLSeveralOnTop(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1])[:plotnames.index("Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M")+1],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1],transposeLOL(lolSignalT),SignalSamples,-0.2,'Zprime',False ,'histoE','samehistoE')

#print listOfHistoListsABCD
print "plot_Zprime_MC_Lena Len(listOfHistoListsABCD):"+str( len(listOfHistoListsABCD) )
#writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('ABCD_W_MSD_vs_Bottom_CSV_v2')+1], BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1] , "label", 'ABCD' , True, False, False, "colz", False, False, False, False)
writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('ABCD_W_MSD_vs_Bottom_CSV_v2')+1], BackgroundSamples , plotnames[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('ABCD_W_MSD_vs_Bottom_CSV_v2')+1], 'ABCD' , True, False, False, "colz", False, False, False, False)

for i in plotnames:
    print i
    

# Correlationfactor

writeCorrLOL( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('ABCD_W_MSD_vs_Bottom_CSV_v2')+1] )
