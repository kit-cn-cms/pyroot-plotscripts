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
#plotselection="N_packedPatJetsAK8PFCHSSoftDrop>=2&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200&&Evt_HT>850"
plotselection="Evt_HT>850"
plots=[

        Plot(ROOT.TH1F("Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV",50,0,1000),"Signal_Topfirst_Zprime_Pt",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tprime_M" ,"m(T') in GeV",50,0,5000),"Signal_Topfirst_Tprime_M",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV",50,0,1000),"Signal_Topfirst_Tprime_Pt",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Signal_Topfirst_Tops_Pt",plotselection+"&&N_Signal_Topfirst_Tops>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tops_Eta" ,"eta(t)",60,-3,3),"Signal_Topfirst_Tops_Eta",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Signal_Topfirst_Ws_Pt",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Ws_Eta" ,"eta(W)",60,-3,3),"Signal_Topfirst_Ws_Eta",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV",50,0,2000),"Signal_Topfirst_Bottoms_Pt",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Bottoms_Eta" ,"eta(b)",60,-3,3),"Signal_Topfirst_Bottoms_Eta",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),

        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-btag",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV, anti-btag",50,0,1000),"Sideband_bottom_anti_Topfirst_Zprime_Pt",plotselection+"&&Sideband_bottom_anti_Topfirst_Zprime_Pt>0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tprime_M" ,"m(T') in GeV, anti-btag",50,0,5000),"Sideband_bottom_anti_Topfirst_Tprime_M",plotselection+"&&Sideband_bottom_anti_Topfirst_Tprime_M>0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV, anti-btag",50,0,1000),"Sideband_bottom_anti_Topfirst_Tprime_Pt",plotselection+"&&Sideband_bottom_anti_Topfirst_Tprime_Pt>0","1 anti-btag"),        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt",plotselection+"&&Sideband_bottom_anti_Topfirst_Tops_Pt>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tops_Eta" ,"eta(t)",60,-3,3),"Sideband_bottom_anti_Topfirst_Tops_Eta",plotselection+"","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Ws_Pt",plotselection+"&&Sideband_bottom_anti_Topfirst_Ws_Pt>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Ws_Eta" ,"eta(W)",60,-3,3),"Sideband_bottom_anti_Topfirst_Ws_Eta",plotselection+"","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Bottoms_Pt",plotselection+"&&Sideband_bottom_anti_Topfirst_Bottoms_Pt>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Bottoms_Eta" ,"eta(b)",60,-3,3),"Sideband_bottom_anti_Topfirst_Bottoms_Eta",plotselection+"","1 btag"),

        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-Wtag",50,0,5000),"Sideband_W_anti_Topfirst_Zprime_M",plotselection+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV, anti-Wtag",50,0,1000),"Sideband_W_anti_Topfirst_Zprime_Pt",plotselection+"&&Sideband_W_anti_Topfirst_Zprime_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tprime_M" ,"m(T') in GeV, anti-Wtag",50,0,5000),"Sideband_W_anti_Topfirst_Tprime_M",plotselection+"&&Sideband_W_anti_Topfirst_Tprime_M>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV, anti-Wtag",50,0,1000),"Sideband_W_anti_Topfirst_Tprime_Pt",plotselection+"&&Sideband_W_anti_Topfirst_Tprime_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, anti-Wtag",50,0,2000),"Sideband_W_anti_Topfirst_Tops_Pt",plotselection+"&&Sideband_W_anti_Topfirst_Tops_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tops_Eta" ,"eta(t), anti-Wtag",60,-3,3),"Sideband_W_anti_Topfirst_Tops_Eta",plotselection+"","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, anti-Wtag",50,0,2000),"Sideband_W_anti_Topfirst_Ws_Pt",plotselection+"&&Sideband_W_anti_Topfirst_Ws_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Ws_Eta" ,"eta(W), anti-Wtag",60,-3,3),"Sideband_W_anti_Topfirst_Ws_Eta",plotselection+"","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV, anti-Wtag",50,0,2000),"Sideband_W_anti_Topfirst_Bottoms_Pt",plotselection+"&&Sideband_W_anti_Topfirst_Bottoms_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Bottoms_Eta" ,"eta(b), anti-Wtag",60,-3,3),"Sideband_W_anti_Topfirst_Bottoms_Eta",plotselection+"","1 anti-Wtag"),
        
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV, anti-ttag",50,0,1000),"Sideband_top_anti_Topfirst_Zprime_Pt",plotselection+"&&Sideband_top_anti_Topfirst_Zprime_Pt>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tprime_M" ,"m(T') in GeV, anti-ttag",50,0,5000),"Sideband_top_anti_Topfirst_Tprime_M",plotselection+"&&Sideband_top_anti_Topfirst_Tprime_M>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV, anti-ttag",50,0,1000),"Sideband_top_anti_Topfirst_Tprime_Pt",plotselection+"&&Sideband_top_anti_Topfirst_Tprime_Pt>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt",plotselection+"&&Sideband_top_anti_Topfirst_Tops_Pt>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_Eta" ,"eta(t), anti-ttag",60,-3,3),"Sideband_top_anti_Topfirst_Tops_Eta",plotselection+"","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_Topfirst_Ws_Pt",plotselection+"&&Sideband_top_anti_Topfirst_Ws_Pt>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_Eta" ,"eta(W), anti-ttag",60,-3,3),"Sideband_top_anti_Topfirst_Ws_Eta",plotselection+"","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_Topfirst_Bottoms_Pt",plotselection+"&&Sideband_top_anti_Topfirst_Bottoms_Pt>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_Eta" ,"eta(b), anti-ttag",60,-3,3),"Sideband_top_anti_Topfirst_Bottoms_Eta",plotselection+"","1 anti-ttag"),        
        
        
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Tops_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Signal_Topfirst_Tops_Pt",plotselection+"&&Signal_Topfirst_Tops_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Ws_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Signal_Topfirst_Ws_Pt",plotselection+"&&Signal_Topfirst_Ws_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Bottoms_Pt" ,"p_{T}(b) in GeV",50,0,2000),"Signal_Topfirst_Bottoms_Pt",plotselection+"&&Signal_Topfirst_Bottoms_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_W_anti_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_W_anti_Tops_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Signal_Topfirst_Tops_Pt",plotselection+"&&Signal_Topfirst_Tops_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_W_anti_Ws_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Signal_Topfirst_Ws_Pt",plotselection+"&&Signal_Topfirst_Ws_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_W_anti_Bottoms_Pt" ,"p_{T}(b) in GeV",50,0,2000),"Signal_Topfirst_Bottoms_Pt",plotselection+"&&Signal_Topfirst_Bottoms_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_top_anti_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_top_anti_Tops_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Signal_Topfirst_Tops_Pt",plotselection+"&&Signal_Topfirst_Tops_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_top_anti_Ws_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Signal_Topfirst_Ws_Pt",plotselection+"&&Signal_Topfirst_Ws_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_top_anti_Bottoms_Pt" ,"p_{T}(b) in GeV",50,0,2000),"Signal_Topfirst_Bottoms_Pt",plotselection+"&&Signal_Topfirst_Bottoms_Pt>0","1 btag"),
        
        #Plot(ROOT.TH2F("ABCD_top_tau32_vs_top_MSD" ,"\tau_{32}(t) over m_{SD}(t)",20,0,1,30,0,300),"Tops_ABCD_MSD:Tops_ABCD_t32",plotselection+"","1 btag"),
        #Plot(ROOT.TH2F("ABCD_top_tau32_vs_W_tau21" ,"\tau_{32}(t) over \tau_{21}(W)",20,0,1,20,0,1),"Tops_ABCD_t32","Ws_ABCD_t21",plotselection+"","1 btag"),
        #Plot(ROOT.TH2F("ABCD_top_tau32_vs_W_MSD" ,"\tau_{32}(t) over m_{SD}(W)",20,0,1,30,0,300),"Tops_ABCD_t32","Ws_ABCD_MSD",plotselection+"","1 btag"),
        #Plot(ROOT.TH2F("ABCD_top_tau32_vs_Bottom_CSV_v2" ,"\tau_{32}(t) over CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection+"","1 btag"),
        #Plot(ROOT.TH2F("ABCD_top_MSD_vs_W_tau21" ,"m_{SD}(t) over \tau_{21}(W)",30,0,300,20,0,1),"Tops_ABCD_MSD","Ws_ABCD_t21",plotselection+"","1 btag"),
        #Plot(ROOT.TH2F("ABCD_top_MSD_vs_W_MSD" ,"m_{SD}(t) over \tau_{21}(W)",30,0,300,30,0,300),"Tops_ABCD_MSD","Ws_ABCD_MSD",plotselection+"","1 btag"),
        #Plot(ROOT.TH2F("ABCD_top_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(t) over CSV_v2(b)",30,0,300,20,0,1),"Tops_ABCD_MSD","Bottoms_ABCD_CSV",plotselection+"","1 btag"),
        #Plot(ROOT.TH2F("ABCD_W_MSD_vs_W_tau21" ,"m_{SD}(W) over \tau_{21}(W)",30,0,300,20,0,1),"Ws_ABCD_MSD","Ws_ABCD_t21",plotselection+"","1 btag"),
        #Plot(ROOT.TH2F("ABCD_W_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(W) over CSV_v2(b)",30,0,300,20,0,1),"Ws_ABCD_MSD","Bottoms_ABCD_CSV",plotselection+"","1 btag"),

        Plot(ROOT.TH1F("N_packedPatJetsAK8PFCHSSoftDrop" ,"N_packedPatJetsAK8PFCHSSoftDrop",10,0,10),"N_packedPatJetsAK8PFCHSSoftDrop",plotselection+"","1 btag"),
        Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_1_Pt" ,"p_{T}(AK8_1) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[0]",plotselection+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>0","1 btag"),
        Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_2_Pt" ,"p_{T}(AK8_2) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[1]",plotselection+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>0","1 btag"),
        Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_3_Pt" ,"p_{T}(AK8_3) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[2]",plotselection+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[2]>0","1 btag"),
        Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_4_Pt" ,"p_{T}(AK8_4) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[3]",plotselection+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[3]>0","1 btag"),

        Plot(ROOT.TH1F("N_Jets" ,"N_Jets",10,0,10),"N_Jets",plotselection+"","1 btag"),
        Plot(ROOT.TH1F("Jet_1_Pt" ,"p_{T}(AK4_1) in GeV",50,0,1000),"Jet_Pt[0]",plotselection+"&&Jet_Pt[0]>0","1 btag"),
        Plot(ROOT.TH1F("Jet_2_Pt" ,"p_{T}(AK4_2) in GeV",50,0,1000),"Jet_Pt[1]",plotselection+"&&Jet_Pt[1]>0","1 btag"),
        Plot(ROOT.TH1F("Jet_3_Pt" ,"p_{T}(AK4_3) in GeV",50,0,1000),"Jet_Pt[2]",plotselection+"&&Jet_Pt[2]>0","1 btag"),
        Plot(ROOT.TH1F("Jet_4_Pt" ,"p_{T}(AK4_4) in GeV",50,0,1000),"Jet_Pt[3]",plotselection+"&&Jet_Pt[3]>0","1 btag"),
]

plotnames=['Signal_Topfirst_Zprime_M','Signal_Topfirst_Zprime_Pt','Signal_Topfirst_Tprime_M','Signal_Topfirst_Tprime_Pt','Signal_Topfirst_Tops_Pt','Signal_Topfirst_Tops_Eta','Signal_Topfirst_Ws_Pt','Signal_Topfirst_Ws_Eta','Signal_Topfirst_Bottoms_Pt','Signal_Topfirst_Bottoms_Eta','Sideband_bottom_anti_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_Pt','Sideband_bottom_anti_Topfirst_Tprime_M','Sideband_bottom_anti_Topfirst_Tprime_Pt','Sideband_bottom_anti_Topfirst_Tops_Pt','Sideband_bottom_anti_Topfirst_Tops_Eta','Sideband_bottom_anti_Topfirst_Ws_Pt','Sideband_bottom_anti_Topfirst_Ws_Eta','Sideband_bottom_anti_Topfirst_Bottoms_Pt','Sideband_bottom_anti_Topfirst_Bottoms_Eta','Sideband_W_anti_Topfirst_Zprime_M','Sideband_W_anti_Topfirst_Zprime_Pt','Sideband_W_anti_Topfirst_Tprime_M','Sideband_W_anti_Topfirst_Tprime_Pt','Sideband_W_anti_Topfirst_Tops_Pt','Sideband_W_anti_Topfirst_Tops_Eta','Sideband_W_anti_Topfirst_Ws_Pt','Sideband_W_anti_Topfirst_Ws_Eta','Sideband_W_anti_Topfirst_Bottoms_Pt','Sideband_W_anti_Topfirst_Bottoms_Eta','Sideband_top_anti_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_Pt','Sideband_top_anti_Topfirst_Tprime_M','Sideband_top_anti_Topfirst_Tprime_Pt','Sideband_top_anti_Topfirst_Tops_Pt','Sideband_top_anti_Topfirst_Tops_Eta','Sideband_top_anti_Topfirst_Ws_Pt','Sideband_top_anti_Topfirst_Ws_Eta','Sideband_top_anti_Topfirst_Bottoms_Pt','Sideband_top_anti_Topfirst_Bottoms_Eta','SB_SF_bottom_anti_Zprime_M','SB_SF_bottom_anti_Tops_Pt','SB_SF_bottom_anti_Ws_Pt','SB_SF_bottom_anti_Bottoms_Pt','SB_SF_W_anti_Zprime_M','SB_SF_W_anti_Tops_Pt','SB_SF_W_anti_Ws_Pt','SB_SF_W_anti_Bottoms_Pt','SB_SF_top_anti_Zprime_M','SB_SF_top_anti_Tops_Pt','SB_SF_top_anti_Ws_Pt','SB_SF_top_anti_Bottoms_Pt'
,'N_packedPatJetsAK8PFCHSSoftDrop','packedPatJetsAK8PFCHSSoftDrop_1_Pt','packedPatJetsAK8PFCHSSoftDrop_2_Pt','packedPatJetsAK8PFCHSSoftDrop_3_Pt','packedPatJetsAK8PFCHSSoftDrop_4_Pt'
,'N_Jets','Jet_1_Pt','Jet_2_Pt','Jet_3_Pt','Jet_4_Pt'
#,'ABCD_top_tau32_vs_top_MSD'
           #,'ABCD_top_tau32_vs_W_tau21','ABCD_top_tau32_vs_W_MSD','ABCD_top_tau32_vs_Bottom_CSV_v2','ABCD_top_MSD_vs_W_tau21','ABCD_top_MSD_vs_W_MSD','ABCD_top_MSD_vs_Bottom_CSV_v2','ABCD_W_MSD_vs_W_tau21','ABCD_W_MSD_vs_Bottom_CSV_v2'
]



#plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
#plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
#plotselection="N_packedPatJetsAK8PFCHSSoftDrop>=2&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200&&Evt_HT>850"
#plots=[

#]
#plotlabel="Wbt, #geq 3 jets, #geq 2 b-tags"
#plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 2 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
#plotselection="(Wbt&&N_BTagsM=2)"
#plots=[

  
#]



print name,4000000,plots,samples,[''],['1.']
outputpath=plotParallel(name,4000000,plots,samples)

# plot dataMC comparison
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
#if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    #renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames,False)
#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)
#lllcsv=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,CSVSystnames)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_bottom_anti_Zprime_M"),plotnames.index("Sideband_bottom_anti_Topfirst_Zprime_M"),True, 1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_bottom_anti_Tops_Pt"),plotnames.index("Sideband_bottom_anti_Topfirst_Tops_Pt"),True,1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_bottom_anti_Ws_Pt"),plotnames.index("Sideband_bottom_anti_Topfirst_Ws_Pt"),True,1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_bottom_anti_Bottoms_Pt"),plotnames.index("Sideband_bottom_anti_Topfirst_Bottoms_Pt"),True, 1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_W_anti_Zprime_M"),plotnames.index("Sideband_top_anti_Topfirst_Zprime_M"),True,1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_W_anti_Tops_Pt"),plotnames.index("Sideband_W_anti_Topfirst_Tops_Pt"),True,1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_W_anti_Ws_Pt"),plotnames.index("Sideband_W_anti_Topfirst_Ws_Pt"),True, 1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_W_anti_Bottoms_Pt"),plotnames.index("Sideband_W_anti_Topfirst_Bottoms_Pt"),True,1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_top_anti_Zprime_M"),plotnames.index("Sideband_top_anti_Topfirst_Zprime_M"),True,1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_top_anti_Tops_Pt"),plotnames.index("Sideband_top_anti_Topfirst_Tops_Pt"),True, 1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_top_anti_Ws_Pt"),plotnames.index("Sideband_top_anti_Topfirst_Ws_Pt"),True,1)
divideHistos(listOfHistoLists,plotnames.index("SB_SF_top_anti_Bottoms_Pt"),plotnames.index("Sideband_top_anti_Topfirst_Bottoms_Pt"),True,1)

#LOLSumw2(listOfHistoLists)
#dummylist=[[]]
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
loldataT=transposeLOL(listOfHistoListsData)
writeLOLSeveralOneOnTop(transposeLOL(lolT[3:]),samples[3:],transposeLOL(lolT[:3]),samples[:3],-0.2,'Zprime',False ,'histoE','samehistoE')
writeHistoListwithXYErrors(transposeLOL(lolT[3:5])[40:52],samples[2:5],'Zprime_BKG',1)
#plotDataMC(transposeLOL(lolT[3][20:]),[],samples[3],'QCD_BKG',False,'',False)
#plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name,[[lll,3354,ROOT.kBlack,True]],False,labels)
#printCanvases(canvas,output)
