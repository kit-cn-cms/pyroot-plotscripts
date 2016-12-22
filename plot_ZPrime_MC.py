#############
# plot general control distributions 
##############

from plotconfig_Zprime_MC import *
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
plotselection="N_packedPatJetsAK8PFCHSSoftDrop>=2&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200&&Evt_HT>800"
plots=[
        Plot(ROOT.TH1F("Zprime_M" ,"m(Z') in GeV",50,0,5000),"Zprime_M",plotselection+"&&Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Zprime_Pt" ,"p_{T}(Z') in GeV",50,0,1000),"Zprime_Pt",plotselection+"&&Zprime_Pt>0","1 btag"),
        Plot(ROOT.TH1F("Zprime_bottom_anti_M" ,"m(Z') in GeV, anti-btag",50,0,5000),"Zprime_bottom_anti_M",plotselection+"&&Zprime_bottom_anti_M>0","1 anti-btag"),
        Plot(ROOT.TH1F("Zprime_bottom_anti_Pt" ,"p_{T}(Z') in GeV, anti-btag",50,0,1000),"Zprime_bottom_anti_Pt",plotselection+"&&Zprime_bottom_anti_Pt>0","1 anti-btag"),
        Plot(ROOT.TH1F("Zprime_W_anti_M" ,"m(Z') in GeV, anti-Wtag",50,0,5000),"Zprime_W_anti_M",plotselection+"&&Zprime_W_anti_M>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Zprime_W_anti_Pt" ,"p_{T}(Z') in GeV, anti-Wtag",50,0,1000),"Zprime_W_anti_Pt",plotselection+"&&Zprime_W_anti_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Zprime_top_anti_M" ,"m(Z') in GeV, anti-ttag",50,0,5000),"Zprime_top_anti_M",plotselection+"&&Zprime_top_anti_M>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Zprime_top_anti_Pt" ,"p_{T}(Z') in GeV, anti-ttag",40,0,4000),"Zprime_top_anti_Pt",plotselection+"&&Zprime_top_anti_Pt>0","1 anti-ttag"),
        

        
        Plot(ROOT.TH1F("Tops_pt" ,"p_{T}(t) in GeV",50,0,2000),"Tops_pt[0]",plotselection+"&&Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Tops_eta" ,"eta(t)",60,-3,3),"Tops_eta[0]",plotselection+"&&Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Ws_pt" ,"p_{T}(W) in GeV",50,0,2000),"Ws_pt[0]",plotselection+"&&Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Ws_eta" ,"eta(W)",60,-3,3),"Ws_eta[0]",plotselection+"&&Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Bottoms_pt" ,"p_{T}(b) in GeV",50,0,2000),"Bottoms_pt[0]",plotselection+"&&Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Bottoms_eta" ,"eta(b)",60,-3,3),"Bottoms_eta[0]",plotselection+"&&Zprime_M>0","1 btag"),

        Plot(ROOT.TH1F("Tops_pt_Zprimebottomanti" ,"p_{T}(t) in GeV, anti-btag",50,0,2000),"Tops_pt[0]",plotselection+"&&Zprime_bottom_anti_M>0","1 anti-btag"),
        Plot(ROOT.TH1F("Tops_eta_Zprimebottomanti" ,"eta(t) anti-btag",60,-3,3),"Tops_eta[0]",plotselection+"&&Zprime_bottom_anti_M>0","1 anti-btag"), 
        Plot(ROOT.TH1F("Ws_pt_Zprimebottomanti" ,"p_{T}(W) in GeV, anti-btag",50,0,2000),"Ws_pt[0]",plotselection+"&&Zprime_bottom_anti_M>0","1 anti-btag"),
        Plot(ROOT.TH1F("Ws_eta_Zprimebottomanti" ,"eta(W) anti-btag",60,-3,3),"Ws_eta[0]",plotselection+"&&Zprime_bottom_anti_M>0","1 anti-btag"),
        Plot(ROOT.TH1F("Bottoms_anti_pt_Zprimebottomanti" ,"p_{T}(b) in GeV, anti-btag",50,0,2000),"Bottoms_anti_pt[0]",plotselection+"&&Zprime_bottom_anti_M>0","1 anti-btag"),
        Plot(ROOT.TH1F("Bottoms_anti_eta_Zprimebottomanti" ,"eta(b) anti-btag",60,-3,3),"Bottoms_anti_eta[0]",plotselection+"&&Zprime_bottom_anti_M>0","1 anti-btag"),
        
        Plot(ROOT.TH1F("Zprime_M_ratio_bottom" ,"m(Z') in GeV",50,0,5000),"Zprime_M",plotselection+"&&Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Zprime_M_ratio_W" ,"m(Z') in GeV",50,0,5000),"Zprime_M",plotselection+"&&Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Zprime_M_ratio_top" ,"m(Z') in GeV",50,0,5000),"Zprime_M",plotselection+"&&Zprime_M>0","1 btag"),        
        ]
plotnames=['Zprime_M','Zprime_Pt','Zprime_bottom_anti_M','Zprime_bottom_anti_Pt','Zprime_W_anti_M','Zprime_W_anti_Pt','Zprime_top_anti_M','Zprime_top_anti_Pt','Tops_pt','Tops_eta','Ws_pt','Ws_eta','Bottoms_pt','Bottoms_eta','Tops_pt_Zprimebottomanti','Tops_eta_Zprimebottomanti','Ws_pt_Zprimebottomanti','Ws_eta_Zprimebottomanti','Bottoms_anti_pt_Zprimebottomanti','Bottoms_anti_eta_Zprimebottomanti','Zprime_M_ratio_bottom','Zprime_M_ratio_W','Zprime_M_ratio_top']



#plotlabel="Wbt, #geq 3 jets, #geq 2 b-tags"
#plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 2 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
#plotselection="(Wbt&&N_BTagsM=2)"
#plots=[

  
#]



print name,4000000,plots,samples,[''],['1.']
outputpath=plotParallel(name,4000000,plots,samples)

# plot dataMC comparison
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples[:5],plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples[5:],plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
#if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    #renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames,False)
#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)
#lllcsv=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,CSVSystnames)
divideHistos(listOfHistoLists,plotnames.index("Zprime_M_ratio_bottom"),plotnames.index("Zprime_bottom_anti_M"),True, 5)
divideHistos(listOfHistoLists,plotnames.index("Zprime_M_ratio_W"),plotnames.index("Zprime_W_anti_M"),True,5)
divideHistos(listOfHistoLists,plotnames.index("Zprime_M_ratio_top"),plotnames.index("Zprime_top_anti_M"),True,5)

#LOLSumw2(listOfHistoLists)
#dummylist=[[]]
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
loldataT=transposeLOL(listOfHistoListsData)
writeLOLSeveralOneOnTop(transposeLOL(lolT[3:]),samples[3:],transposeLOL(lolT[:3]),samples[:3],-0.2,'Zprime',False ,'histoE','samehistoE')
writeHistoListwithXYErrors(transposeLOL(lolT[3:5])[20:],samples[2:5],'Zprime_BKG')
#plotDataMC(transposeLOL(lolT[3][20:]),[],samples[3],'QCD_BKG',False,'',False)
#plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name,[[lll,3354,ROOT.kBlack,True]],False,labels)
#printCanvases(canvas,output)