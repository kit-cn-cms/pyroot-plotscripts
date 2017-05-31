#############
# plot general control distributions 
##############

from plotconfig_Zprime_MC import *
from plot_additional_Zprime_MC import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy
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
#]  N_Sideband_withtopbtag_bottom_anti_Topfirst_Bottoms



# book plots
plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
#plotselection="N_packedPatJetsAK8PFCHSSoftDrop>=2&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200&&Evt_HT>850"
plotselection1="Evt_HT>850"
plotselection3="Evt_HT>1000"
#plotselection1=""
plotselection2="(N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 && Evt_HT>850) "





#Own Plotselections for ABCD-method
plotselection_ABCD_general=  plotselection2 + "&& Zprimes_ABCD_M>0   &&    Ws_ABCD_t21 <  0.6    &&    100 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210   "
plotselection_ABCD_general_beta =  plotselection2 + "&& Zprimes_ABCD_M>0   &&    70 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 100     &&    100 < Tops_ABCD_MSD     &&    Tops_ABCD_MSD  < 210   "

plotselection_tau32 = " Tops_ABCD_t32 < 0.86   "
plotselection_W_MSD =  " 70 < Ws_ABCD_MSD  &&   Ws_ABCD_MSD < 100 "
plotselection_B_CSV = "  Bottoms_ABCD_CSV > 0.8   "
plotselection_W_tau21 = " Ws_ABCD_t21 < 0.6 "
#plotselection_topsubjetCSVv2 = " Tops_ABCD_maxsubjetCSVv2 > 0.8 "

plotselection_tau32_anti=" Tops_ABCD_t32 > 0.86   "
plotselection_W_MSD_anti =  " 70 > Ws_ABCD_MSD  ||   Ws_ABCD_MSD > 100 "
plotselection_B_CSV_anti = "  Bottoms_ABCD_CSV < 0.8   "
plotselection_W_tau21_anti = " Ws_ABCD_t21 > 0.6 "
#plotselection_topsubjetCSVv2_anti = " Tops_ABCD_maxsubjetCSVv2 < 0.8 "


plotselection_sideband = "Signal_Topfirst_Zprime_M < 0"
plotselection_sideband_withtopbtag = "Signal_Topfirst_Zprime_M < 0"



plots=[

        Plot(ROOT.TH1F("Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV",50,0,1000),"Signal_Topfirst_Zprime_Pt",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tprime_M" ,"m(T') in GeV",50,0,5000),"Signal_Topfirst_Tprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV",50,0,1000),"Signal_Topfirst_Tprime_Pt",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Signal_Topfirst_Tops_Pt[0]",plotselection2+"&&N_Signal_Topfirst_Tops>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tops_Eta" ,"eta(t)",60,-3,3),"Signal_Topfirst_Tops_Eta[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tops_MSD" ,"m_{SD}(t) in GeV",60,0,300),"Signal_Topfirst_Tops_MSD[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tops_t32" ,"tau_{32}(t)",20,0,1),"Signal_Topfirst_Tops_t32[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Signal_Topfirst_Ws_Pt[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Ws_Eta" ,"eta(W)",60,-3,3),"Signal_Topfirst_Ws_Eta[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Ws_MSD" ,"m_{SD}(W) in GeV",60,0,300),"Signal_Topfirst_Ws_MSD[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Ws_t21" ,"tau_{21}(W)",20,0,1),"Signal_Topfirst_Ws_t21[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV",50,0,2000),"Signal_Topfirst_Bottoms_Pt[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Bottoms_Eta" ,"eta(b)",60,-3,3),"Signal_Topfirst_Bottoms_Eta[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Bottoms_CSVv2" ,"CSVv2",40,-1,1),"Signal_Topfirst_Bottoms_CSVv2[0]",plotselection2+"&&Signal_Topfirst_Bottoms_CSVv2>-1 && Signal_withtopbtag_Topfirst_Zprime_M<0","1 btag"),

        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV, anti-btag",50,0,1000),"Sideband_bottom_anti_Topfirst_Zprime_Pt",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_Pt>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tprime_M" ,"m(T') in GeV, anti-btag",50,0,5000),"Sideband_bottom_anti_Topfirst_Tprime_M",plotselection2+"&&Sideband_bottom_anti_Topfirst_Tprime_M>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV, anti-btag",50,0,1000),"Sideband_bottom_anti_Topfirst_Tprime_Pt",plotselection2+"&&Sideband_bottom_anti_Topfirst_Tprime_Pt>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt[0]",plotselection2+"&&Sideband_bottom_anti_Topfirst_Tops_Pt[0]>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tops_Eta" ,"eta(t), anti-btag",60,-3,3),"Sideband_bottom_anti_Topfirst_Tops_Eta[0]",plotselection2+" && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tops_MSD" ,"m_{SD}(t) in GeV, anti-btag",60,0,300),"Sideband_bottom_anti_Topfirst_Tops_MSD[0]",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tops_t32" ,"tau_{32}(t), anti-btag",20,0,1),"Sideband_bottom_anti_Topfirst_Tops_t32[0]",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, anti-btag",50,0,2000),"Sideband_bottom_anti_Topfirst_Ws_Pt[0]",plotselection2+"&&Sideband_bottom_anti_Topfirst_Ws_Pt[0]>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Ws_Eta" ,"eta(W), anti-btag",60,-3,3),"Sideband_bottom_anti_Topfirst_Ws_Eta[0]",plotselection2+" && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Ws_MSD" ,"m_{SD}(W) in GeV, anti-btag",60,0,300),"Sideband_bottom_anti_Topfirst_Ws_MSD[0]",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Ws_t21" ,"tau_{21}(W), anti-btag",20,0,1),"Sideband_bottom_anti_Topfirst_Ws_t21[0]",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV, anti-btag",50,0,2000),"Sideband_bottom_anti_Topfirst_Bottoms_Pt[0]",plotselection2+"&&Sideband_bottom_anti_Topfirst_Bottoms_Pt[0]>0 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Bottoms_Eta" ,"eta(b), anti-btag",60,-3,3),"Sideband_bottom_anti_Topfirst_Bottoms_Eta[0]",plotselection2+" && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Bottoms_CSVv2" ,"CSVv2, anti-btag",40,-1,1),"Sideband_bottom_anti_Topfirst_Bottoms_CSVv2[0]",plotselection2+"&&Sideband_bottom_anti_Topfirst_Bottoms_CSVv2[0]>-1 && anti_btag==1 && Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M<0","1 btag"),

        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-Wtag",50,0,5000),"Sideband_W_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 anti-Wtag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV, anti-Wtag",50,0,1000),"Sideband_W_anti_Topfirst_Zprime_Pt",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_Pt>0","1 anti-Wtag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tprime_M" ,"m(T') in GeV, anti-Wtag",50,0,5000),"Sideband_W_anti_Topfirst_Tprime_M",plotselection2+"&&Sideband_W_anti_Topfirst_Tprime_M>0","1 anti-Wtag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV, anti-Wtag",50,0,1000),"Sideband_W_anti_Topfirst_Tprime_Pt",plotselection2+"&&Sideband_W_anti_Topfirst_Tprime_Pt>0","1 anti-Wtag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, anti-Wtag",50,0,2000),"Sideband_W_anti_Topfirst_Tops_Pt[0]",plotselection2+"&&Sideband_W_anti_Topfirst_Tops_Pt[0]>0","1 anti-Wtag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tops_Eta" ,"eta(t), anti-Wtag",60,-3,3),"Sideband_W_anti_Topfirst_Tops_Eta[0]",plotselection2+"","1 anti-Wtag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tops_MSD" ,"m_{SD}(t) in GeV, anti-Wtag",60,0,300),"Sideband_W_anti_Topfirst_Tops_MSD[0]",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tops_t32" ,"tau_{32}(t), anti-Wtag",20,0,1),"Sideband_W_anti_Topfirst_Tops_t32[0]",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 btag"),       
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, anti-Wtag",50,0,2000),"Sideband_W_anti_Topfirst_Ws_Pt[0]",plotselection2+"&&Sideband_W_anti_Topfirst_Ws_Pt[0]>0","1 anti-Wtag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Ws_Eta" ,"eta(W), anti-Wtag",60,-3,3),"Sideband_W_anti_Topfirst_Ws_Eta[0]",plotselection2+"","1 anti-Wtag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Ws_MSD" ,"m_{SD}(W) in GeV, anti-Wtag",60,0,300),"Sideband_W_anti_Topfirst_Ws_MSD[0]",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Ws_t21" ,"tau_{21}(W), anti-Wtag",20,0,1),"Sideband_W_anti_Topfirst_Ws_t21[0]",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV, anti-Wtag",50,0,2000),"Sideband_W_anti_Topfirst_Bottoms_Pt[0]",plotselection2+"&&Sideband_W_anti_Topfirst_Bottoms_Pt[0]>0","1 anti-Wtag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Bottoms_Eta" ,"eta(b), anti-Wtag",60,-3,3),"Sideband_W_anti_Topfirst_Bottoms_Eta[0]",plotselection2+"","1 anti-Wtag"),
        #Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Bottoms_CSVv2" ,"CSVv2, anti-Wtag",40,-1,1),"Sideband_W_anti_Topfirst_Bottoms_CSVv2[0]",plotselection2+"&&Sideband_W_anti_Topfirst_Bottoms_CSVv2[0]>-1","1 btag"),
        
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV, anti-ttag",50,0,1000),"Sideband_top_anti_Topfirst_Zprime_Pt",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tprime_M" ,"m(T') in GeV, anti-ttag",50,0,5000),"Sideband_top_anti_Topfirst_Tprime_M",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV, anti-ttag",50,0,1000),"Sideband_top_anti_Topfirst_Tprime_Pt",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt[0]",plotselection2+"&&Sideband_top_anti_Topfirst_Tops_Pt[0]>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_Eta" ,"eta(t), anti-ttag",60,-3,3),"Sideband_top_anti_Topfirst_Tops_Eta[0]",plotselection2+"","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_MSD" ,"m_{SD}(t) in GeV, anti-ttag",60,0,300),"Sideband_top_anti_Topfirst_Tops_MSD[0]",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_t32" ,"tau_{32}(t), anti-ttag",20,0,1),"Sideband_top_anti_Topfirst_Tops_t32[0]",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 btag"),       
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_Topfirst_Ws_Pt[0]",plotselection2+"&&Sideband_top_anti_Topfirst_Ws_Pt[0]>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_Eta" ,"eta(W), anti-ttag",60,-3,3),"Sideband_top_anti_Topfirst_Ws_Eta[0]",plotselection2+"","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_MSD" ,"m_{SD}(W) in GeV, anti-ttag",60,0,300),"Sideband_top_anti_Topfirst_Ws_MSD[0]",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_t21" ,"tau_{21}(W), anti-ttag",20,0,1),"Sideband_top_anti_Topfirst_Ws_t21[0]",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_Topfirst_Bottoms_Pt[0]",plotselection2+"&&Sideband_top_anti_Topfirst_Bottoms_Pt[0]>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_Eta" ,"eta(b), anti-ttag",60,-3,3),"Sideband_top_anti_Topfirst_Bottoms_Eta[0]",plotselection2+"","1 anti-ttag"),        
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_CSVv2" ,"CSVv2, anti-ttag",40,-1,1),"Sideband_top_anti_Topfirst_Bottoms_CSVv2[0]",plotselection2+"&&Sideband_top_anti_Topfirst_Bottoms_CSVv2[0]>-1","1 btag"),
        
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_anti_MCtopmass_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Zprime_M>0","1 anti-ttag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV, anti-ttag",50,0,1000),"Sideband_top_anti_MCtopmass_Topfirst_Zprime_Pt",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Zprime_M>0","1 anti-ttag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tprime_M" ,"m(T') in GeV, anti-ttag",50,0,5000),"Sideband_top_anti_MCtopmass_Topfirst_Tprime_M",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Zprime_M>0","1 anti-ttag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV, anti-ttag",50,0,1000),"Sideband_top_anti_MCtopmass_Topfirst_Tprime_Pt",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Zprime_M>0","1 anti-ttag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_MCtopmass_Topfirst_Tops_Pt[0]",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Tops_Pt[0]>0","1 anti-ttag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_Eta" ,"eta(t), anti-ttag",60,-3,3),"Sideband_top_anti_MCtopmass_Topfirst_Tops_Eta[0]",plotselection2+"","1 anti-ttag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_MSD" ,"m_{SD}(t) in GeV, anti-ttag",60,0,300),"Sideband_top_anti_MCtopmass_Topfirst_Tops_MSD[0]",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_t32" ,"tau_{32}(t), anti-ttag",20,0,1),"Sideband_top_anti_MCtopmass_Topfirst_Tops_t32[0]",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Zprime_M>0","1 btag"),       
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_MCtopmass_Topfirst_Ws_Pt[0]",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Ws_Pt[0]>0","1 anti-ttag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_Eta" ,"eta(W), anti-ttag",60,-3,3),"Sideband_top_anti_MCtopmass_Topfirst_Ws_Eta[0]",plotselection2+"","1 anti-ttag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_MSD" ,"m_{SD}(W) in GeV, anti-ttag",60,0,300),"Sideband_top_anti_MCtopmass_Topfirst_Ws_MSD[0]",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_t21" ,"tau_{21}(W), anti-ttag",20,0,1),"Sideband_top_anti_MCtopmass_Topfirst_Ws_t21[0]",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_MCtopmass_Topfirst_Bottoms_Pt[0]",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Bottoms_Pt[0]>0","1 anti-ttag"),
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_Eta" ,"eta(b), anti-ttag",60,-3,3),"Sideband_top_anti_MCtopmass_Topfirst_Bottoms_Eta[0]",plotselection2+"","1 anti-ttag"),        
        #Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_CSVv2" ,"CSVv2, anti-ttag",40,-1,1),"Sideband_top_anti_MCtopmass_Topfirst_Bottoms_CSVv2[0]",plotselection2+"&&Sideband_top_anti_MCtopmass_Topfirst_Bottoms_CSVv2[0]>-1","1 btag"),
        
        
        #Plot(ROOT.TH1F("SB_SF_bottom_anti_Zprime_M" ,"m(Z') in GeV, signal-anti-ttag ratio",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_bottom_anti_Tops_Pt" ,"p_{T}(t) in GeV, signal-anti-ttag ratio",50,0,2000),"Signal_Topfirst_Tops_Pt[0]",plotselection2+"&&Signal_Topfirst_Tops_Pt[0]>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_bottom_anti_Tops_MSD" ,"m_{SD}(t) in GeV, signal-anti-ttag ratio",60,0,300),"Signal_Topfirst_Tops_MSD[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_bottom_anti_Tops_t32" ,"tau_{32}(t), signal-anti-ttag ratio",20,0,1),"Signal_Topfirst_Tops_t32[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_bottom_anti_Ws_Pt" ,"p_{T}(W) in GeV, signal-anti-ttag ratio",50,0,2000),"Signal_Topfirst_Ws_Pt[0]",plotselection2+"&&Signal_Topfirst_Ws_Pt[0]>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_bottom_anti_Ws_MSD" ,"m_{SD}(W) in GeV, signal-anti-ttag ratio",60,0,300),"Signal_Topfirst_Ws_MSD[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_bottom_anti_Ws_t21" ,"tau_{21}(W), signal-anti-ttag ratio",20,0,1),"Signal_Topfirst_Ws_t21[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_bottom_anti_Bottoms_Pt" ,"p_{T}(b) in GeV, signal-anti-ttag ratio",50,0,2000),"Signal_Topfirst_Bottoms_Pt[0]",plotselection2+"&&Signal_Topfirst_Bottoms_Pt[0]>0","1 btag"),

        #Plot(ROOT.TH1F("SB_SF_W_anti_Zprime_M" ,"m(Z') in GeV, signal-anti-Wtag ratio",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_W_anti_Tops_Pt" ,"p_{T}(t) in GeV, signal-anti-Wtag ratio",50,0,2000),"Signal_Topfirst_Tops_Pt[0]",plotselection2+"&&Signal_Topfirst_Tops_Pt[0]>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_W_anti_Tops_MSD" ,"m_{SD}(t) in GeV, signal-anti-Wtag ratio",60,0,300),"Signal_Topfirst_Tops_MSD[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_W_anti_Tops_t32" ,"tau_{32}(t), signal-anti-Wtag ratio",20,0,1),"Signal_Topfirst_Tops_t32[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_W_anti_Ws_Pt" ,"p_{T}(W) in GeV, signal-anti-Wtag ratio",50,0,2000),"Signal_Topfirst_Ws_Pt[0]",plotselection2+"&&Signal_Topfirst_Ws_Pt[0]>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_W_anti_Bottoms_Pt" ,"p_{T}(b) in GeV, signal-anti-Wtag ratio",50,0,2000),"Signal_Topfirst_Bottoms_Pt[0]",plotselection2+"&&Signal_Topfirst_Bottoms_Pt[0]>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_W_anti_Bottoms_CSVv2" ,"CSVv2, signal-anti-Wtag ratio",40,-1,1),"Signal_Topfirst_Bottoms_CSVv2[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        
        #Plot(ROOT.TH1F("SB_SF_top_anti_Zprime_M" ,"m(Z') in GeV, signal-anti-btag ratio",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_top_anti_Tops_Pt" ,"p_{T}(t) in GeV, signal-anti-btag ratio",50,0,2000),"Signal_Topfirst_Tops_Pt[0]",plotselection2+"&&Signal_Topfirst_Tops_Pt[0]>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_top_anti_Ws_Pt" ,"p_{T}(W) in GeV, signal-anti-btag ratio",50,0,2000),"Signal_Topfirst_Ws_Pt[0]",plotselection2+"&&Signal_Topfirst_Ws_Pt[0]>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_top_anti_Ws_MSD" ,"m_{SD}(W) in GeV, signal-anti-btag ratio",60,0,300),"Signal_Topfirst_Ws_MSD[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_top_anti_Ws_t21" ,"tau_{21}(W), signal-anti-btag ratio",20,0,1),"Signal_Topfirst_Ws_t21[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_top_anti_Bottoms_Pt" ,"p_{T}(b) in GeV, signal-anti-btag ratio",50,0,2000),"Signal_Topfirst_Bottoms_Pt[0]",plotselection2+"&&Signal_Topfirst_Bottoms_Pt[0]>0","1 btag"),
        #Plot(ROOT.TH1F("SB_SF_top_anti_Bottoms_CSVv2" ,"CSVv2, signal-anti-btag ratio",40,-1,1),"Signal_Topfirst_Bottoms_CSVv2[0]",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),





        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M>0 && anti_btag==1)","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_bottom_anti_Topfirst_Tops_Pt[0]>0 && QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0 && anti_btag==1)","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0 && anti_btag==1)","1 btag"),

        #Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_top_anti_Topfirst_Tops_Pt[0]>0 && QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_top_anti_Topfirst_Zprime_M>0 && QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),

        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M>0 && anti_btag==1)","1 btag"),        
        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_bottom_anti_Topfirst_Tops_Pt[0]>0 && QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0  && anti_btag==1)","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0  && anti_btag==1)","1 btag"),
               
        #Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_top_anti_Topfirst_Tops_Pt[0]>0 && QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_top_anti_Topfirst_Zprime_M>0 && QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDPythia8_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Ws_Pt[0]",plotselection2+"*( Sideband_top_anti_Topfirst_Ws_Pt[0]>0 && QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Ws_Pt>0)","1 btag"),





        Plot(ROOT.TH1F("Signal_withtopbtag_Topfirst_Zprime_M" ,"m(Z') in GeV, topbtag",50,0,5000),"Signal_withtopbtag_Topfirst_Zprime_M",plotselection2+"&&Signal_withtopbtag_Topfirst_Zprime_M>0","2 btags"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, withtopbtag",50,0,2000),"Signal_withtopbtag_Topfirst_Tops_Pt[0]",plotselection2+"&&Signal_withtopbtag_Topfirst_Tops_Pt[0]>0","2 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, withtopbtag",50,0,2000),"Signal_withtopbtag_Topfirst_Ws_Pt[0]",plotselection2+"&&Signal_withtopbtag_Topfirst_Ws_Pt[0]>0","2 btag"),
        
        Plot(ROOT.TH1F("Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, topbtag",50,0,5000),"Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M>0 && anti_btag_withtopbtag==1","1 anti-btag, 1 topbtag"),
        #Plot(ROOT.TH1F("Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, withtopbtag and anti-btag",50,0,2000),"Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0]",plotselection2+"&&Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0]>0 && anti_btag_withtopbtag==1","1 anti-btag, 1 topbtag"),

        Plot(ROOT.TH1F("Sideband_top_withbtag_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, topbtag",50,0,5000),"Sideband_top_withbtag_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_withbtag_anti_Topfirst_Zprime_M>0","1 anti-ttag withb"),
        #Plot(ROOT.TH1F("Sideband_top_withbtag_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, topbtag",50,0,5000),"Sideband_top_withbtag_anti_MCtopmass_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_withbtag_anti_MCtopmass_Topfirst_Zprime_M>0","1 anti-ttag withb"),
        #Plot(ROOT.TH1F("Sideband_top_withbtag_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, withtopbtag anti-ttag",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0]",plotselection2+"&&Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0]>0","1 anti-ttag withb"),
        #Plot(ROOT.TH1F("Sideband_top_withbtag_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, withtopbtag anti-ttag",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0]",plotselection2+"&&Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0]>0","1 anti-ttag withb"),

        #Plot(ROOT.TH1F("SB_SF_withtopbtag_bottom_anti_Zprime_M" ,"m(Z') in GeV, withtopbtag",50,0,5000),"Signal_withtopbtag_Topfirst_Zprime_M",plotselection2+"&&Signal_withtopbtag_Topfirst_Zprime_M>0","2 btags"),
        #Plot(ROOT.TH1F("SB_SF_withtopbtag_bottom_anti_Tops_Pt" ,"m(Z') in GeV, withtopbtag",50,0,2000),"Signal_withtopbtag_Topfirst_Tops_Pt[0]",plotselection2+"&&Signal_withtopbtag_Topfirst_Tops_Pt[0]>0","2 btags"),
        #Plot(ROOT.TH1F("SB_SF_withtopbtag_top_anti_Tops_Pt" ,"p_{T}(t) in GeV, withtopbtag",50,0,2000),"Signal_withtopbtag_Topfirst_Tops_Pt[0]",plotselection2+"&&Signal_withtopbtag_Topfirst_Tops_Pt[0]>0","2 btag"),
        #Plot(ROOT.TH1F("SB_SF_withtopbtag_top_anti_Ws_Pt" ,"p_{T}(W) in GeV, withtopbtag",50,0,2000),"Signal_withtopbtag_Topfirst_Ws_Pt[0]",plotselection2+"&&Signal_withtopbtag_Topfirst_Ws_Pt[0]>0","2 btag"),



        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M>0 && QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M>0 && anti_btag_withtopbtag==1)","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0]>0 && QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt>0 && anti_btag_withtopbtag==1)","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M>0 && QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt>0 && anti_btag_withtopbtag==1)","1 btag"),

        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0]>0 && QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_withbtag_anti_Topfirst_Zprime_M",plotselection2+"*(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt>0 && Sideband_top_withbtag_anti_Topfirst_Zprime_M>0)","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDMadgraph_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0]",plotselection2+"*( Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0]>0 && QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt>0)","1 btag"),


        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M>0 && anti_btag_withtopbtag==1 && QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M>0)","1 btag"),        
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0]>0 && anti_btag_withtopbtag==1 && QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M>0 && anti_btag_withtopbtag==1 && QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),
               
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0]>0 && QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_withbtag_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_top_withbtag_anti_Topfirst_Zprime_M>0 && QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDPythia8_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0]",plotselection2+"*( Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0]>0 && QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt>0)","1 btag"),





        #Plot(ROOT.TH1F("N_packedPatJetsAK8PFCHSSoftDrop" ,"N_packedPatJetsAK8PFCHSSoftDrop",10,0,10),"N_packedPatJetsAK8PFCHSSoftDrop",plotselection1+"",""),
        #Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_1_Pt" ,"p_{T}(AK8_1) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[0]",plotselection1+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>0",""),
        #Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_2_Pt" ,"p_{T}(AK8_2) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[1]",plotselection1+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>0",""),
        #Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_3_Pt" ,"p_{T}(AK8_3) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[2]",plotselection1+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[2]>0",""),
        #Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_4_Pt" ,"p_{T}(AK8_4) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[3]",plotselection1+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[3]>0",""),

        #Plot(ROOT.TH1F("N_Jets" ,"N_Jets",10,0,10),"N_Jets",plotselection1+"",""),
        #Plot(ROOT.TH1F("Jet_1_Pt" ,"p_{T}(AK4_1) in GeV",50,0,1000),"Jet_Pt[0]",plotselection1+"&&Jet_Pt[0]>0",""),
        #Plot(ROOT.TH1F("Jet_2_Pt" ,"p_{T}(AK4_2) in GeV",50,0,1000),"Jet_Pt[1]",plotselection1+"&&Jet_Pt[1]>0",""),
        #Plot(ROOT.TH1F("Jet_3_Pt" ,"p_{T}(AK4_3) in GeV",50,0,1000),"Jet_Pt[2]",plotselection1+"&&Jet_Pt[2]>0",""),
        #Plot(ROOT.TH1F("Jet_4_Pt" ,"p_{T}(AK4_4) in GeV",50,0,1000),"Jet_Pt[3]",plotselection1+"&&Jet_Pt[3]>0",""),
        
        #Plot(ROOT.TH1F("Evt_HT" ,"Evt_HT",60,0,3000),"Evt_HT",plotselection3+"",""),
        #Plot(ROOT.TH1F("Evt_HT_Jets" ,"Evt_HT_Jets",60,0,3000),"Evt_HT_Jets",plotselection3+"",""),
        
        #Plot(ROOT.TH1F("Jet_GenJet_Pt" ,"Jet_GenJet_Pt",40,0,2000),"Jet_GenJet_Pt",plotselection1+"",""),
        
        
        #Plot(ROOT.TH1F("t_tagrate_pt","p_{T} in GeV, t-tagrate",50,0,2000),"tagged_top_pt",plotselection1+"&&tagged_top_pt>0","1 btag"),
        #Plot(ROOT.TH1F("W_tagrate_pt","p_{T} in GeV, W-tagrate",50,0,2000),"tagged_W_pt",plotselection1+"&&tagged_W_pt>0","1 btag"),
        #Plot(ROOT.TH1F("b_tagrate_pt","p_{T} in GeV, b-tagrate",50,0,2000),"tagged_bottom_pt",plotselection1+"&&tagged_bottom_pt>0","1 btag"),
        #Plot(ROOT.TH1F("t_misstagrate_pt","p_{T} in GeV, t-misstagrate",50,0,2000),"misstagged_top_pt",plotselection1+"&&misstagged_top_pt>0","1 btag"),
        #Plot(ROOT.TH1F("W_misstagrate_pt","p_{T} in GeV, W-misstagrate",50,0,2000),"misstagged_W_pt",plotselection1+"&&misstagged_W_pt>0","1 btag"),
        #Plot(ROOT.TH1F("b_misstagrate_pt","p_{T} in GeV, b-misstagrate",50,0,2000),"misstagged_bottom_pt",plotselection1+"&&misstagged_bottom_pt>0","1 btag"),
        #Plot(ROOT.TH1F("tanti_tagrate_pt","p_{T} in GeV, tanti-tagrate",50,0,2000),"tagged_top_anti_pt",plotselection1+"&&tagged_top_anti_pt>0","1 btag"),
        #Plot(ROOT.TH1F("Wanti_tagrate_pt","p_{T} in GeV, Wanti-tagrate",50,0,2000),"tagged_W_anti_pt",plotselection1+"&&tagged_W_anti_pt>0","1 btag"),
        #Plot(ROOT.TH1F("banti_tagrate_pt","p_{T} in GeV, banti-tagrate",50,0,2000),"tagged_bottom_anti_pt",plotselection1+"&&tagged_bottom_anti_pt>0","1 btag"),
        #Plot(ROOT.TH1F("tanti_misstagrate_pt","p_{T} in GeV, tanti-misstagrate",50,0,2000),"misstagged_top_anti_pt",plotselection1+"&&misstagged_top_anti_pt>0","1 btag"),
        #Plot(ROOT.TH1F("Wanti_misstagrate_pt","p_{T} in GeV, Wanti-misstagrate",50,0,2000),"misstagged_W_anti_pt",plotselection1+"&&misstagged_W_anti_pt>0","1 btag"),
        #Plot(ROOT.TH1F("banti_misstagrate_pt","p_{T} in GeV, banti-misstagrate",50,0,2000),"misstagged_bottom_anti_pt",plotselection1+"&&misstagged_bottom_anti_pt>0","1 btag"),
        
        #Plot(ROOT.TH1F("AK8_top_tag_candidates_pt","p_{T} in GeV, t-tagrate",50,0,2000),"AK8_top_tag_candidates_pt",plotselection1+"&&AK8_top_tag_candidates_pt>0","1 btag"),
        #Plot(ROOT.TH1F("AK8_W_tag_candidates_pt","p_{T} in GeV, W-tagrate",50,0,2000),"AK8_W_tag_candidates_pt",plotselection1+"&&AK8_W_tag_candidates_pt>0","1 btag"),
        #Plot(ROOT.TH1F("AK4_bottom_tag_candidates_pt","p_{T} in GeV, b-tagrate",50,0,2000),"AK4_bottom_tag_candidates_pt",plotselection1+"&&AK4_bottom_tag_candidates_pt>0","1 btag"),
        #Plot(ROOT.TH1F("AK8_top_misstagged_candidates_pt","p_{T} in GeV, t-misstagrate",50,0,2000),"AK8_top_misstagged_candidates_pt",plotselection1+"&&AK8_top_misstagged_candidates_pt>0","1 btag"),
        #Plot(ROOT.TH1F("AK8_W_misstagged_candidates_pt","p_{T} in GeV, W-misstagrate",50,0,2000),"AK8_W_misstagged_candidates_pt",plotselection1+"&&AK8_W_misstagged_candidates_pt>0","1 btag"),
        #Plot(ROOT.TH1F("AK4_bottom_misstagged_candidates_pt","p_{T} in GeV, b-misstagrate",50,0,2000),"AK4_bottom_misstagged_candidates_pt",plotselection1+"&&AK4_bottom_misstagged_candidates_pt>0","1 btag"),

    
        #TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_top_MSD" ,"tau_{32}(t) VS m_{SD}(t)",20,0,1,30,0,300),"Tops_ABCD_MSD","Tops_ABCD_t32",plotselection2+"&& Tops_ABCD_MSD>0 && Tops_ABCD_t32>0","1 btag"),
        #TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_W_tau21" ,"tau_{32}(t) VS tau_{21}(W)",20,0,1,20,0,1),"Tops_ABCD_t32","Ws_ABCD_t21",plotselection2+"&& Tops_ABCD_t32>0 && Ws_ABCD_t21>0","1 btag"),
        #TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_W_MSD" ,"tau_{32}(t) VS m_{SD}(W)",20,0,1,30,0,300),"Tops_ABCD_t32","Ws_ABCD_MSD",plotselection2+"&&Tops_ABCD_t32>0 && Ws_ABCD_MSD>0","1 btag"),
        #TwoDimPlot(ROOT.TH2F("ABCD_top_tau32_vs_Bottom_CSV_v2" ,"tau_{32}(t) VS CSV_v2(b)",20,0,1,20,0,1),"Tops_ABCD_t32","Bottoms_ABCD_CSV",plotselection2+"&&Tops_ABCD_t32>0 &&Bottoms_ABCD_CSV>0","1 btag"),
        #TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_W_tau21" ,"m_{SD}(t) VS tau_{21}(W)",30,0,300,20,0,1),"Tops_ABCD_MSD","Ws_ABCD_t21",plotselection2+"&&Tops_ABCD_MSD>0&&Ws_ABCD_t21>0","1 btag"),
        #TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_W_MSD" ,"m_{SD}(t) VS tau_{21}(W)",30,0,300,30,0,300),"Tops_ABCD_MSD","Ws_ABCD_MSD",plotselection2+"&&Tops_ABCD_MSD>0&&Ws_ABCD_MSD>0","1 btag"),
        #TwoDimPlot(ROOT.TH2F("ABCD_top_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(t) VS CSV_v2(b)",30,0,300,20,0,1),"Tops_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2+"&&Tops_ABCD_MSD>0&&Bottoms_ABCD_CSV>0","1 btag"),
        #TwoDimPlot(ROOT.TH2F("ABCD_W_MSD_vs_W_tau21" ,"m_{SD}(W) VS tau_{21}(W)",30,0,300,20,0,1),"Ws_ABCD_MSD","Ws_ABCD_t21",plotselection2+"&&Ws_ABCD_MSD>0&&Ws_ABCD_t21>0","1 btag"),
        #TwoDimPlot(ROOT.TH2F("ABCD_W_MSD_vs_Bottom_CSV_v2" ,"m_{SD}(W) VS CSV_v2(b)",30,0,300,20,0,1),"Ws_ABCD_MSD","Bottoms_ABCD_CSV",plotselection2+"&&Ws_ABCD_MSD>0&&Bottoms_ABCD_CSV>0","1 btag"),
        #TwoDimPlot(ROOT.TH2F("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M_VS_Sideband_bottom_anti_Topfirst_Zprime_M" ,"",50,-1,2,50,0,5000),"QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M","Sideband_bottom_anti_Topfirst_Zprime_M","","1 btag"),




        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M>0 && anti_btag==1)"+"* QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_bottom_anti_Topfirst_Tops_Pt[0]>0 && QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0 && anti_btag==1)"+"* QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0 && anti_btag==1)"+"* QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),

        #Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_top_anti_Topfirst_Tops_Pt[0]>0 && QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)"+"* QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_top_anti_Topfirst_Zprime_M>0 && QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)"+"* QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        ##Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDMadgraph_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Ws_Pt[0]",plotselection2+"*( Sideband_top_anti_Topfirst_Ws_Pt[0]>0 && QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt>0)"+"* QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt","1 btag"),

        Plot(ROOT.TH1F("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,3),"QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M",plotselection2+"*(QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M>0)","1 btag"),
        Plot(ROOT.TH1F("QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt" ,"pT(t) in GeV",50,0,3),"QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt",plotselection2+"*(QCDMadgraph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),

        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M>0 && anti_btag==1)"+"* QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M","1 btag"),        
        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_bottom_anti_Topfirst_Tops_Pt[0]>0 && QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0  && anti_btag==1)"+"* QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0  && anti_btag==1)"+"* QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
               
        #Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_top_anti_Topfirst_Tops_Pt[0]>0 && QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)"+"* QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_top_anti_Topfirst_Zprime_M>0 && QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)"+"* QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDPythia8_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Ws_Pt[0]",plotselection2+"*( Sideband_top_anti_Topfirst_Ws_Pt[0]>0 && QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Ws_Pt>0)"+"* QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Ws_Pt","1 btag"),

        Plot(ROOT.TH1F("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,3),"QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M",plotselection2+"*(QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M>0 && anti_btag==1)","1 btag"),
        Plot(ROOT.TH1F("QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt" ,"pT(t) in GeV",50,0,3),"QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt",plotselection2+"*(QCDPythia8_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0 && anti_btag==1)","1 btag"),


        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M>0 && QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M>0 && anti_btag_withtopbtag==1)"+"* QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0]>0 && QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt>0 && anti_btag_withtopbtag==1)"+"* QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt * ","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M>0 && QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt>0 && anti_btag_withtopbtag==1)"+"* QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),

        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0]>0 && QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt>0)"+"* QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_withbtag_anti_Topfirst_Zprime_M",plotselection2+"*(QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt[0]>0 && Sideband_top_withbtag_anti_Topfirst_Zprime_M>0)"+"* QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDMadgraph_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0]",plotselection2+"*( Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0]>0 && QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt>0)"+"* QCDMadgraph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt","1 btag"),



        #Plot(ROOT.TH1F("QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,3),"QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M",plotselection2+"*(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M>0)","1 btag"),
        #Plot(ROOT.TH1F("QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt" ,"m(Z') in GeV",50,0,3),"QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt",plotselection2+"*(QCDMadgraph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),


        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M>0 && anti_btag_withtopbtag==1 && QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M>0)"+"* QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M","1 btag"),        
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt[0]>0 && anti_btag_withtopbtag==1 && QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt>0)"+"* QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M>0 && anti_btag_withtopbtag==1 && QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt>0)"+"* QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
               
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0]",plotselection2+"*(Sideband_top_withbtag_anti_Topfirst_Tops_Pt[0]>0 && QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt>0)"+"* QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_withbtag_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_top_withbtag_anti_Topfirst_Zprime_M>0 && QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt>0)"+"* QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDPythia8_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0]",plotselection2+"*( Sideband_top_withbtag_anti_Topfirst_Ws_Pt[0]>0 && QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt>0)"+"* QCDPythia8_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt","1 btag"),

        #Plot(ROOT.TH1F("QCDPythia8_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,3),"QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M",plotselection2+"*(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M>0)","1 btag"),
        #Plot(ROOT.TH1F("QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt" ,"m(Z') in GeV",50,0,3),"QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt",plotselection2+"*(QCDPythia8_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),





    #doing only first element
    #beta (tau21)

        Plot(ROOT.TH1F("ABCD_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
        Plot(ROOT.TH1F("ABCD_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
        Plot(ROOT.TH1F("ABCD_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
        Plot(ROOT.TH1F("ABCD_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),


        Plot(ROOT.TH1F("ABCD_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
        Plot(ROOT.TH1F("ABCD_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
        Plot(ROOT.TH1F("ABCD_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
        Plot(ROOT.TH1F("ABCD_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag") ,



        Plot(ROOT.TH1F("ABCD_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
        Plot(ROOT.TH1F("ABCD_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
        Plot(ROOT.TH1F("ABCD_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),
        Plot(ROOT.TH1F("ABCD_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21 + "&&" +plotselection_sideband ,"1 btag"),


        Plot(ROOT.TH1F("ABCD_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32 + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
        Plot(ROOT.TH1F("ABCD_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
        Plot(ROOT.TH1F("ABCD_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag"),
        Plot(ROOT.TH1F("ABCD_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,50,0,5000),"Zprimes_ABCD_M",    plotselection_ABCD_general_beta + " && " + plotselection_tau32_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti + "&&" +plotselection_sideband ,"1 btag") ,
]





plotnames=[]
for i in plots:
    plotnames.append(i.name)

OnlyFirstList=len(plots)*[False]
OnlyFirstList[plotnames.index("ABCD_CatA_Zprime_M_beta_first"):plotnames.index('ABCD_withtopbtag_CatH_Zprime_M_beta_first') +1 ] = len(OnlyFirstList[plotnames.index("ABCD_CatA_Zprime_M_beta_first"):plotnames.index('ABCD_withtopbtag_CatH_Zprime_M_beta_first') + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'

#print allweightsystnames
#print allsystweights

#print name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM,systweightsbasic+systweightsMadgraphbantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weightsystnamesPythia8bantiZprimeM,systweightsPythia8bantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
outputpath=plotParallel(name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],allweightsystnames,allsystweights,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)

listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples,plots,1)

listOfHistoListsBackground=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples,plots,1)
listOfHistoListsDataMadgraph=createHistoLists_fromSuperHistoFile(outputpath,DataSamples,plots,1)
listOfHistoListsDataPythia=createHistoLists_fromSuperHistoFile(outputpath,DataSamples,plots,1)


addLOLtoLOL(listOfHistoListsDataMadgraph,transposeLOL([transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("ttbar")]]))
addLOLtoLOL(listOfHistoListsDataPythia,transposeLOL([transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("QCDPythia8")]]+[transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("ttbar")]]))


#listOfHistoListsDataNoTtbar=createHistoLists_fromSuperHistoFile(outputpath,DataSamples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,DataSamples,plots,1)


lllBackgroundnosyst=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,weigthsystnamesbasic)



lllBackground=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,allweightsystnames)
lllData_Madgraph=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,allweightsystnames)
lllData_Pythia=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,allweightsystnames)

#lllBackground=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,ABweightsystnames)
#lllData_Madgraph=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,ABweightsystnames)
#lllData_Pythia=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,ABweightsystnames)

#lllBackground=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,weightsystnamesABCD)
#lllData_Madgraph=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,weightsystnamesABCD)
#lllData_Pythia=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,weightsystnamesABCD)

addLLLtoLLL(lllData_Madgraph,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]))
addLLLtoLLL(lllData_Pythia,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDPythia8")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]))



#lllQCDPythia8bantiZprimeM=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,weightsystnamesPythia8bantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM)
#lllQCDPythia8bantiZprimeMData_Madgraph=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,weightsystnamesPythia8bantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM)
#lllQCDPythia8bantiZprimeMData_Pythia=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,weightsystnamesPythia8bantiZprimeM+weightsystnamesGeneratorDiffPythia8bantiZprimeM)


#lllQCDMadgraphtantiTopPt=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,weightsystnamesMadgraphtantiTopPt+weightsystnamesGeneratorDiffMadgraphtantiTopPt)
#lllQCDMadgraphtantiTopPtData_Madgraph=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,weightsystnamesMadgraphtantiTopPt+weightsystnamesGeneratorDiffMadgraphtantiTopPt)
#lllQCDMadgraphtantiTopPtData_Pythia=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,weightsystnamesMadgraphtantiTopPt+weightsystnamesGeneratorDiffMadgraphtantiTopPt)

#lllQCDPythia8tantiTopPt=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt)
#lllQCDPythia8tantiTopPtData_Madgraph=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt)
#lllQCDPythia8tantiTopPtData_Pythia=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,weightsystnamesPythia8tantiTopPt+weightsystnamesGeneratorDiffPythia8tantiTopPt)






#print listOfHistoListsData



#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
#if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    #renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames,False)
#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)
#lllcsv=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,CSVSystnames)


#listofratios_Signal_bantiSB_ZprimeM=divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_bottom_anti_Zprime_M"),plotnames.index("Sideband_bottom_anti_Topfirst_Zprime_M"),True, 1)
#listofratios_Signal_bantiSB_TopPt=divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_bottom_anti_Tops_Pt"),plotnames.index("Sideband_bottom_anti_Topfirst_Tops_Pt"),True,1)
#listofratios_Signal_tantiSB_TopPt=divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_top_anti_Tops_Pt"),plotnames.index("Sideband_top_anti_Topfirst_Tops_Pt"),True, 1)
#listofratios_Signal_tantiSB_WPt=divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_top_anti_Ws_Pt"),plotnames.index("Sideband_top_anti_Topfirst_Ws_Pt"),True,1)

#listofratios_Signal_withtopbtag_bantiSB_ZprimeM=divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_withtopbtag_bottom_anti_Zprime_M"),plotnames.index("Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M"),True, 1)
#listofratios_Signal_withtopbtag_bantiSB_TopPt=divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_withtopbtag_bottom_anti_Tops_Pt"),plotnames.index("Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt"),True,1)
#listofratios_Signal_withtopbtag_tantiSB_TopPt=divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_withtopbtag_top_anti_Tops_Pt"),plotnames.index("Sideband_top_withbtag_anti_Topfirst_Tops_Pt"),True, 1)
#listofratios_Signal_withtopbtag_tantiSB_WPt=divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_withtopbtag_top_anti_Ws_Pt"),plotnames.index("Sideband_top_withbtag_anti_Topfirst_Ws_Pt"),True,1)


#################################################################Transosed LOL ######################
#LOLSumw2(listOfHistoLists)
#dummylist=[[]]
labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)
lolSignalT=transposeLOL(listOfHistoListsSignal)
lolBackgroundT=transposeLOL(listOfHistoListsBackground)
lolDataMadgraphT=transposeLOL(listOfHistoListsDataMadgraph)
lolDataPythiaT=transposeLOL(listOfHistoListsDataPythia)
#addLOLtoLOL(listOfHistoListsData,transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("SC_Zprime25001200_1pb")+1]))
#addLOLtoLOL(listOfHistoListsData,transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("ttbar")+1]))
#addLOLtoLOL(listOfHistoListsDataNoTtbar,transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]))

#print transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]])[plotnames.index('Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M')]

 
#print lllData_Madgraph[plotnames.index('Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M')][DataSampleNames.index('DATA_BKG')][allweightsystnames.index('_ABMadgraphbantiZprimeM'+'_nominal')].Integral()



#print lllData_Madgraph[plotnames.index('Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M')][DataSampleNames.index('DATA_BKG')][allweightsystnames.index('_ABMadgraphbantiZprimeM'+'_nominal')].Integral()



#addLLLtoLLL(lllQCDPythia8bantiZprimeMData_Pythia,[[lllQCDPythia8bantiZprimeM[0][BackgroundSampleNames.index("QCDPythia8")]]])
#addLLLtoLLL(lllQCDMadgraphtantiTopPtData_Madgraph,[[lllQCDMadgraphtantiTopPt[0][BackgroundSampleNames.index("QCDMadgraph")]]])
#addLLLtoLLL(lllQCDPythia8tantiTopPtData_Pythia,[[lllQCDPythia8tantiTopPt[0][BackgroundSampleNames.index("QCDPythia8")]]])

#addLLLtoLLL(lllQCDMadgraphbantiZprimeMData_Pythia,[[lllQCDMadgraphbantiZprimeM[0][BackgroundSampleNames.index("QCDPythia8")]]])
#addLLLtoLLL(lllQCDPythia8bantiZprimeMData_Madgraph,[[lllQCDPythia8bantiZprimeM[0][BackgroundSampleNames.index("QCDMadgraph")]]])
#addLLLtoLLL(lllQCDMadgraphtantiTopPtData_Pythia,[[lllQCDMadgraphtantiTopPt[0][BackgroundSampleNames.index("QCDPythia8")]]])
#addLLLtoLLL(lllQCDPythia8tantiTopPtData_Madgraph,[[lllQCDPythia8tantiTopPt[0][BackgroundSampleNames.index("QCDMadgraph")]]])




#lolDataNoTtbarT=transposeLOL(listOfHistoListsDataNoTtbar)
#################################################################Transosed LOL end ######################

#ratio_signal_banti_notopbtag=signal_sideband_integralratio(listOfHistoListsBackground[BackgroundSampleNames.index('QCDMadgraph')][plotnames.index('Signal_Topfirst_Zprime_M')],listOfHistoListsBackground[BackgroundSampleNames.index('QCDMadgraph')][plotnames.index('Sideband_bottom_anti_Topfirst_Zprime_M')])
#ratio_signal_banti_withtopbtag=signal_sideband_integralratio(listOfHistoListsBackground[BackgroundSampleNames.index('QCDMadgraph')][plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')],listOfHistoListsBackground[BackgroundSampleNames.index('QCDMadgraph')][plotnames.index('Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M')])
#ratio_signal_banti_notopbtag=signal_sideband_integralratio(transposeLOL([lolBackgroundT[BackgroundSampleNames.index('QCDMadgraph')]])[plotnames.index('Signal_Topfirst_Zprime_M')],transposeLOL(lolBackgroundT[BackgroundSampleNames.index('QCDMadgraph')])[plotnames.index('Sideband_bottom_anti_Topfirst_Zprime_M')])
#ratio_signal_banti_withtopbtag=signal_sideband_integralratio(transposeLOL(lolBackgroundT[BackgroundSampleNames.index('QCDMadgraph')])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')],transposeLOL(lolBackgroundT[BackgroundSampleNames.index('QCDMadgraph')])[plotnames.index('Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M')])






#writeLOLSeveralOnTop(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("ttbar")+1])[:plotnames.index("Sideband_top_anti_Topfirst_Bottoms_CSVv2")+1],BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("ttbar")+1],transposeLOL(lolSignalT),SignalSamples,-0.2,'Zprime',True,False ,'histoE','samehistoE')

#writeListOfHistoLists(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("ttbar")+1])[plotnames.index("Signal_Topfirst_Zprime_M"):plotnames.index("Sideband_bottom_anti_Topfirst_Zprime_M")+1],BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("ttbar")+1],labels,'Zprime_DPG',True,True,False,'histoE')
#writeListOfHistoLists( transposeLOL([listOfHistoListsBackground[plotnames.index('Signal_Topfirst_Zprime_M')]]+[listOfHistoListsBackground[plotnames.index('Signal_SB_Predictionbanti_Topfirst_Zprime_M')]]) , BackgroundSamples , BackgroundSampleNames , 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)


#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("SC_Zprime25001200_1pb")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("SC_Zprime25001200_1pb")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("SC_Zprime25001200_1pb")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'huuuu' , False , False, False, "histoE", False, False, True, False)
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("SC_Zprime25001200_1pb")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("SC_Zprime25001200_1pb")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("SC_Zprime25001200_1pb")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'huuuu' , False , False, False, "histoE", False, False, True, False)




#writeListOfHistoLists( listOfHistoListsBackground , BackgroundSamples , plotnames, 'chekc' , False , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( listOfHistoListsData , DataSamples , plotnames, 'datacheck' , False , False, False, "histoE", False, False, False, False)






#multiplyListofHistoswithfactors(listOfHistoListsBackground[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")],listofratios_Signal_bantiSB_ZprimeM)
#multiplyListofHistoswithfactors(listOfHistoListsBackground[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')],listofratios_Signal_bantiSB_TopPt)
#multiplyListofHistoswithfactors(listOfHistoListsBackground[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')],listofratios_Signal_bantiSB_TopPt)
#multiplyListofHistoswithfactors(listOfHistoListsBackground[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')],listofratios_Signal_tantiSB_TopPt)
#multiplyListofHistoswithfactors(listOfHistoListsBackground[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')],listofratios_Signal_tantiSB_TopPt)

#multiplyListofHistoswithfactors(listOfHistoListsBackground[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')],listofratios_Signal_withtopbtag_bantiSB_ZprimeM)
#multiplyListofHistoswithfactors(listOfHistoListsBackground[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')],listofratios_Signal_withtopbtag_bantiSB_TopPt)
#multiplyListofHistoswithfactors(listOfHistoListsBackground[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')],listofratios_Signal_withtopbtag_tantiSB_TopPt)
#multiplyListofHistoswithfactors(listOfHistoListsBackground[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')],listofratios_Signal_withtopbtag_tantiSB_TopPt)




################################### AB Closure ########################################
######Using Madgraph SBSSSSF
####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] ,[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)



#####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)
                      
                      
                      
########Using PT SBSSSF
#####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] ,[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)


#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)









#####################################AB Closure withtopbtag#########################
#####Using Madgraph SBSSSSF
####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] ,[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)



#####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt")]], 'AB_background_estimation_PT' , True , False, False, "histoE", False, False, True, False)

########Using PT SBSSSF
#####from banti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] ,[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)


#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######from tanti sideband
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_withtopbtag_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]]+[BackgroundSamples[BackgroundSampleNames.index("ttbar")]] , [plotnames[plotnames.index("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

######same?
##writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt")]], 'AB_background_estimation_PT' , True , False, False, "histoE", False, False, True, False)



################################################################################### AB Scale factors

#writeHistoListwithXYErrors(transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_bottom_anti_Zprime_M"):plotnames.index("SB_SF_bottom_anti_Tops_Pt")+1]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_withtopbtag_bottom_anti_Zprime_M"):plotnames.index("SB_SF_withtopbtag_bottom_anti_Tops_Pt")+1],[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]],'Zprime_SBSSSFs_banti',1,'pol2')

#writeHistoListwithXYErrors(transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_top_anti_Tops_Pt"):plotnames.index("SB_SF_top_anti_Ws_Pt")+1]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_withtopbtag_top_anti_Tops_Pt"):plotnames.index("SB_SF_withtopbtag_top_anti_Ws_Pt")+1],[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]],'Zprime_SBSSSFs_tanti',1,"[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))/x")


######################TAGRATES############################
##writeListOfHistoLists(transposeLOL(lolDataT[DataSampleNames.index("MC_BKG_DATA"):])[plotnames.index("t_tagrate_pt"):plotnames.index("b_misstagrate_pt")+1],DataSamples,'tagrates','tagrates',False,False,False,'EL') 
##writeHistoListwithXYErrors(transposeLOL(lolDataT[DataSampleNames.index("MC_BKG_DATA"):])[plotnames.index("t_tagrate_pt"):plotnames.index("b_misstagrate_pt")+1],DataSamples,'tagrates_fit',1,"[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))/x")



##SchmonCorrelation(transposeLOL(lolT[3:5])[plotnames.index("SB_SF_bottom_anti_Bottoms_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_W_anti_Ws_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_top_anti_Tops_Pt")],transposeLOL(lolT[3:5])[plotnames.index("SB_SF_bottom_anti_Bottoms_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_W_anti_Ws_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_top_anti_Tops_Pt")],name='lada', rebin=1)
##SchmonCorrelation(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("SB_SF_bottom_anti_Bottoms_Pt")]+transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("SB_SF_W_anti_Ws_Pt")]+transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("SB_SF_top_anti_Tops_Pt")],transposeLOL(lolDataT)[plotnames.index("t_misstagrate_pt")]+transposeLOL(lolDataT)[plotnames.index("W_misstagrate_pt")]+transposeLOL(lolDataT)[plotnames.index("b_misstagrate_pt")],name='correlations', rebin=1)


##print transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("N_packedPatJetsAK8PFCHSSoftDrop"):plotnames.index("Evt_HT_Jets")+1]



##writeListOfHistoLists(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("ABCD_top_tau32_vs_top_MSD"):plotnames.index("ABCD_top_tau32_vs_W_MSD")],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1],plotnames[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('ABCD_W_MSD_vs_Bottom_CSV_v2')+1],'ABCD',True,False,False,'colz',False,False,False,False)

#writeListOfHistoLists(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("Signal_Topfirst_Zprime_M"):plotnames.index("Sideband_top_withbtag_anti_Topfirst_Zprime_M")+1],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1],plotnames[plotnames.index('Signal_Topfirst_Zprime_M'):plotnames.index('Sideband_top_withbtag_anti_Topfirst_Zprime_M')+1],'ahhh',True,False,False,'colz',False,False,False,False)




#print listOfHistoListsData


################Final ###################

#################with Syst notoptag #####################R

#####################################BANTI ZPRIME CLOSURE######################


#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_', True)


#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_', False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_', False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_', False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_', False)




####################################TANTI Top CLOSURE######################
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_',True)


#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_',False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_',False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_',False)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_',False)



#################with Syst withtopbtag ############################

####################################BANTI ZPRIME CLOSURE######################
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)

#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)


####################################TANTI Top CLOSURE######################
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)

#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)





################Final with ABCD ###################

#################with Syst notoptag #####################R

#####################################BANTI ZPRIME CLOSURE######################


#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_', True)


#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M','ABCD_CatB_Zprime_M_beta_first', 'ABCD_CatC_Zprime_M_beta_first', 'ABCD_CatD_Zprime_M_beta_first', 'QCDMadgraph','fancy_notopbtag_withABCD_', False)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M','ABCD_CatB_Zprime_M_beta_first', 'ABCD_CatC_Zprime_M_beta_first', 'ABCD_CatD_Zprime_M_beta_first', 'QCDPythia8','fancy_notopbtag_withABCD_', False)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M','ABCD_CatB_Zprime_M_beta_first', 'ABCD_CatC_Zprime_M_beta_first', 'ABCD_CatD_Zprime_M_beta_first', 'QCDPythia8','fancy_notopbtag_withABCD_', False)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeM','Signal_Topfirst_Zprime_M','Sideband_bottom_anti_Topfirst_Zprime_M','ABCD_CatB_Zprime_M_beta_first', 'ABCD_CatC_Zprime_M_beta_first', 'ABCD_CatD_Zprime_M_beta_first', 'QCDMadgraph','fancy_notopbtag_withABCD_', False)




####################################TANTI Top CLOSURE######################
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_gendiff_',True)


#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_',False)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_',False)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_notopbtag_',False)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPt','Signal_Topfirst_Zprime_M','Sideband_top_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_notopbtag_',False)



#################with Syst withtopbtag ############################

####################################BANTI ZPRIME CLOSURE######################
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)

#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphbantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_', True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiabantiZprimeMWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_', True)


####################################TANTI Top CLOSURE######################
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)

#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataPythia,lllData_Pythia,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABMadgraphtantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDPythia8','fancy_withtopbtag_gendiff_',True)
#ABBackgroundEstimationCalculationABCDNormAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,DataSamples,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames,SignalSampleNames,plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','_ABPythiatantiTopPtWithtopbtag','Signal_withtopbtag_Topfirst_Zprime_M','Sideband_top_withbtag_anti_Topfirst_Zprime_M', 'QCDMadgraph','fancy_withtopbtag_gendiff_',True)

################Final with ABCD only ###################
#################with Syst notoptag #####################R

ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','ABCD_CatA_Zprime_M_beta_first', 'ABCD_CatB_Zprime_M_beta_first', 'ABCD_CatC_Zprime_M_beta_first', 'ABCD_CatD_Zprime_M_beta_first','QCDMadgraph', 'fancy_ABCD')
ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','ABCD_CatA_Zprime_M_beta_first', 'ABCD_CatB_Zprime_M_beta_first', 'ABCD_CatC_Zprime_M_beta_first', 'ABCD_CatD_Zprime_M_beta_first','QCDMadgraph', 'fancy_ABCD')


ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','ABCD_CatE_Zprime_M_beta_first', 'ABCD_CatF_Zprime_M_beta_first', 'ABCD_CatG_Zprime_M_beta_first', 'ABCD_CatH_Zprime_M_beta_first','QCDMadgraph', 'fancy_ABCD')
ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','ABCD_CatE_Zprime_M_beta_first', 'ABCD_CatF_Zprime_M_beta_first', 'ABCD_CatG_Zprime_M_beta_first', 'ABCD_CatH_Zprime_M_beta_first','QCDMadgraph', 'fancy_ABCD')


#################with Syst withtopbtag ############################
#ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','ABCD_withtopbtag_CatA_Zprime_M_beta_first','QCDMadgraph', 'fancy_ABCD', 'ABCD_withtopbtag_CatB_Zprime_M_beta_first', 'ABCD_withtopbtag_CatC_Zprime_M_beta_first', 'ABCD_withtopbtag_CatD_Zprime_M_beta_first')
#ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','ABCD_withtopbtag_CatA_Zprime_M_beta_first','QCDMadgraph', 'fancy_ABCD', 'ABCD_withtopbtag_CatB_Zprime_M_beta_first', 'ABCD_withtopbtag_CatC_Zprime_M_beta_first', 'ABCD_withtopbtag_CatD_Zprime_M_beta_first')


#ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,'DATA_BKG','SC_none','Zprime25001200','ABCD_withtopbtag_CatE_Zprime_M_beta_first','QCDMadgraph', 'fancy_ABCD', 'ABCD_withtopbtag_CatF_Zprime_M_beta_first', 'ABCD_withtopbtag_CatG_Zprime_M_beta_first', 'ABCD_withtopbtag_CatH_Zprime_M_beta_first')
#ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(listOfHistoListsDataMadgraph,lllData_Madgraph,listOfHistoListsBackground,lllBackground,lllBackgroundnosyst,listOfHistoListsSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,'BKG_Zprime25001200_1pb','SC_Zprime25001200_1pb','Zprime25001200','ABCD_withtopbtag_CatE_Zprime_M_beta_first','QCDMadgraph', 'fancy_ABCD', 'ABCD_withtopbtag_CatF_Zprime_M_beta_first', 'ABCD_withtopbtag_CatG_Zprime_M_beta_first', 'ABCD_withtopbtag_CatH_Zprime_M_beta_first')

