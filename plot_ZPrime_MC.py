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
#]  N_Sideband_withtopbtag_bottom_anti_Topfirst_Bottoms


additionalvariables=[
			#'minimal_Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2:=Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2',
			#'anti_loose_btag:=Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2[0], for(int i =0, i<N_Sideband_top_withbtag_anti_Topfirst_Bottoms, i++){if(Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2[i]<0.46){minimal_Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2=Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2[i]}}',
                        #'minimal_Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2:=Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2<0.46',

			'anti_btag_withtopbtag:=anti_loose_btag(Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2,N_Sideband_top_withbtag_anti_Topfirst_Bottoms)',
			'anti_btag:=anti_loose_btag(Sideband_bottom_anti_Topfirst_Bottoms_CSVv2,N_Sideband_bottom_anti_Topfirst_Bottoms)',
			
			#"minimal_Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2",
                        "Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2","N_Sideband_top_withbtag_anti_Topfirst_Bottoms",
                        "Sideband_bottom_anti_Topfirst_Bottoms_CSVv2","N_Sideband_bottom_anti_Topfirst_Bottoms",
]

additionalfunctions=[
                        #'float temp=1',
                        #for(int i; i<N_Sideband_top_withbtag_anti_Topfirst_Bottoms;i++){temp*=(Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2[i]<0.46);};',
                        "float anti_loose_btag(const float* bottomCSVs, int sizeofarray){"+"\n"+"   float anti_tag=1;"+"\n"+"      for (int i;  i<sizeofarray;i++){"+"\n"+"        if (bottomCSVs[i]>0.46){"+"\n"+"        anti_tag=0;"+"\n"+"      }"+"\n"+"      }"+"\n"+"    return anti_tag;"+"}",
                        #"""
                        #float anti_
                        #"""

                        
    ]

# book plots
plotlabel="Wbt, #geq 3 jets, #geq 1 b-tags"
plotlabelboosted="#splitline{Wbt, #geq 3 jets, #geq 1 b-tags}{#geq 1 AK8 jet p_{T} > 400 GeV, #geq 1 AK8 jet p_{T} > 200 GeV, #geq 1 AK4 jet p_{T} > 100 GeV}"
#plotselection="N_packedPatJetsAK8PFCHSSoftDrop>=2&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200&&Evt_HT>850"
plotselection1="Evt_HT>850"
plotselection3="Evt_HT>1000"
#plotselection1=""
plotselection2="(N_packedPatJetsAK8PFCHSSoftDrop>=2 && packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 && Evt_HT>850) "
plots=[

        Plot(ROOT.TH1F("Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV",50,0,1000),"Signal_Topfirst_Zprime_Pt",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tprime_M" ,"m(T') in GeV",50,0,5000),"Signal_Topfirst_Tprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV",50,0,1000),"Signal_Topfirst_Tprime_Pt",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Signal_Topfirst_Tops_Pt",plotselection2+"&&N_Signal_Topfirst_Tops>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tops_Eta" ,"eta(t)",60,-3,3),"Signal_Topfirst_Tops_Eta",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tops_MSD" ,"m_{SD}(t) in GeV",60,0,300),"Signal_Topfirst_Tops_MSD",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Tops_t32" ,"tau_{32}(t)",20,0,1),"Signal_Topfirst_Tops_t32",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Signal_Topfirst_Ws_Pt",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Ws_Eta" ,"eta(W)",60,-3,3),"Signal_Topfirst_Ws_Eta",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Ws_MSD" ,"m_{SD}(W) in GeV",60,0,300),"Signal_Topfirst_Ws_MSD",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Ws_t21" ,"tau_{21}(W)",20,0,1),"Signal_Topfirst_Ws_t21",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV",50,0,2000),"Signal_Topfirst_Bottoms_Pt",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Bottoms_Eta" ,"eta(b)",60,-3,3),"Signal_Topfirst_Bottoms_Eta",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Signal_Topfirst_Bottoms_CSVv2" ,"CSVv2",40,-1,1),"Signal_Topfirst_Bottoms_CSVv2",plotselection2+"&&Signal_Topfirst_Bottoms_CSVv2>-1","1 btag"),

        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-btag",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag>0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV, anti-btag",50,0,1000),"Sideband_bottom_anti_Topfirst_Zprime_Pt",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_Pt>0 && anti_btag>0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tprime_M" ,"m(T') in GeV, anti-btag",50,0,5000),"Sideband_bottom_anti_Topfirst_Tprime_M",plotselection2+"&&Sideband_bottom_anti_Topfirst_Tprime_M>0 && anti_btag>0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV, anti-btag",50,0,1000),"Sideband_bottom_anti_Topfirst_Tprime_Pt",plotselection2+"&&Sideband_bottom_anti_Topfirst_Tprime_Pt>0 && anti_btag>0","1 anti-btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt",plotselection2+"&&Sideband_bottom_anti_Topfirst_Tops_Pt>0 && anti_btag>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tops_Eta" ,"eta(t), anti-btag",60,-3,3),"Sideband_bottom_anti_Topfirst_Tops_Eta",plotselection2+" && anti_btag>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tops_MSD" ,"m_{SD}(t) in GeV, anti-btag",60,0,300),"Sideband_bottom_anti_Topfirst_Tops_MSD",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Tops_t32" ,"tau_{32}(t), anti-btag",20,0,1),"Sideband_bottom_anti_Topfirst_Tops_t32",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, anti-btag",50,0,2000),"Sideband_bottom_anti_Topfirst_Ws_Pt",plotselection2+"&&Sideband_bottom_anti_Topfirst_Ws_Pt>0 && anti_btag>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Ws_Eta" ,"eta(W), anti-btag",60,-3,3),"Sideband_bottom_anti_Topfirst_Ws_Eta",plotselection2+" && anti_btag>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Ws_MSD" ,"m_{SD}(W) in GeV, anti-btag",60,0,300),"Sideband_bottom_anti_Topfirst_Ws_MSD",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Ws_t21" ,"tau_{21}(W), anti-btag",20,0,1),"Sideband_bottom_anti_Topfirst_Ws_t21",plotselection2+"&&Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV, anti-btag",50,0,2000),"Sideband_bottom_anti_Topfirst_Bottoms_Pt",plotselection2+"&&Sideband_bottom_anti_Topfirst_Bottoms_Pt>0 && anti_btag>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Bottoms_Eta" ,"eta(b), anti-btag",60,-3,3),"Sideband_bottom_anti_Topfirst_Bottoms_Eta",plotselection2+" && anti_btag>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_bottom_anti_Topfirst_Bottoms_CSVv2" ,"CSVv2, anti-btag",40,-1,1),"Sideband_bottom_anti_Topfirst_Bottoms_CSVv2",plotselection2+"&&Sideband_bottom_anti_Topfirst_Bottoms_CSVv2>-1 && anti_btag>0","1 btag"),

        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-Wtag",50,0,5000),"Sideband_W_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV, anti-Wtag",50,0,1000),"Sideband_W_anti_Topfirst_Zprime_Pt",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tprime_M" ,"m(T') in GeV, anti-Wtag",50,0,5000),"Sideband_W_anti_Topfirst_Tprime_M",plotselection2+"&&Sideband_W_anti_Topfirst_Tprime_M>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV, anti-Wtag",50,0,1000),"Sideband_W_anti_Topfirst_Tprime_Pt",plotselection2+"&&Sideband_W_anti_Topfirst_Tprime_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, anti-Wtag",50,0,2000),"Sideband_W_anti_Topfirst_Tops_Pt",plotselection2+"&&Sideband_W_anti_Topfirst_Tops_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tops_Eta" ,"eta(t), anti-Wtag",60,-3,3),"Sideband_W_anti_Topfirst_Tops_Eta",plotselection2+"","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tops_MSD" ,"m_{SD}(t) in GeV, anti-Wtag",60,0,300),"Sideband_W_anti_Topfirst_Tops_MSD",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Tops_t32" ,"tau_{32}(t), anti-Wtag",20,0,1),"Sideband_W_anti_Topfirst_Tops_t32",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 btag"),       
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, anti-Wtag",50,0,2000),"Sideband_W_anti_Topfirst_Ws_Pt",plotselection2+"&&Sideband_W_anti_Topfirst_Ws_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Ws_Eta" ,"eta(W), anti-Wtag",60,-3,3),"Sideband_W_anti_Topfirst_Ws_Eta",plotselection2+"","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Ws_MSD" ,"m_{SD}(W) in GeV, anti-Wtag",60,0,300),"Sideband_W_anti_Topfirst_Ws_MSD",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Ws_t21" ,"tau_{21}(W), anti-Wtag",20,0,1),"Sideband_W_anti_Topfirst_Ws_t21",plotselection2+"&&Sideband_W_anti_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV, anti-Wtag",50,0,2000),"Sideband_W_anti_Topfirst_Bottoms_Pt",plotselection2+"&&Sideband_W_anti_Topfirst_Bottoms_Pt>0","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Bottoms_Eta" ,"eta(b), anti-Wtag",60,-3,3),"Sideband_W_anti_Topfirst_Bottoms_Eta",plotselection2+"","1 anti-Wtag"),
        Plot(ROOT.TH1F("Sideband_W_anti_Topfirst_Bottoms_CSVv2" ,"CSVv2, anti-Wtag",40,-1,1),"Sideband_W_anti_Topfirst_Bottoms_CSVv2",plotselection2+"&&Sideband_W_anti_Topfirst_Bottoms_CSVv2>-1","1 btag"),
        
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, anti-ttag",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Zprime_Pt" ,"p_{T}(Z') in GeV, anti-ttag",50,0,1000),"Sideband_top_anti_Topfirst_Zprime_Pt",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_Pt>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tprime_M" ,"m(T') in GeV, anti-ttag",50,0,5000),"Sideband_top_anti_Topfirst_Tprime_M",plotselection2+"&&Sideband_top_anti_Topfirst_Tprime_M>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tprime_Pt" ,"p_{T}(T') in GeV, anti-ttag",50,0,1000),"Sideband_top_anti_Topfirst_Tprime_Pt",plotselection2+"&&Sideband_top_anti_Topfirst_Tprime_Pt>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt",plotselection2+"&&Sideband_top_anti_Topfirst_Tops_Pt>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_Eta" ,"eta(t), anti-ttag",60,-3,3),"Sideband_top_anti_Topfirst_Tops_Eta",plotselection2+"","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_MSD" ,"m_{SD}(t) in GeV, anti-ttag",60,0,300),"Sideband_top_anti_Topfirst_Tops_MSD",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Tops_t32" ,"tau_{32}(t), anti-ttag",20,0,1),"Sideband_top_anti_Topfirst_Tops_t32",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 btag"),       
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_Topfirst_Ws_Pt",plotselection2+"&&Sideband_top_anti_Topfirst_Ws_Pt>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_Eta" ,"eta(W), anti-ttag",60,-3,3),"Sideband_top_anti_Topfirst_Ws_Eta",plotselection2+"","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_MSD" ,"m_{SD}(W) in GeV, anti-ttag",60,0,300),"Sideband_top_anti_Topfirst_Ws_MSD",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Ws_t21" ,"tau_{21}(W), anti-ttag",20,0,1),"Sideband_top_anti_Topfirst_Ws_t21",plotselection2+"&&Sideband_top_anti_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_Pt" ,"p_{T}(b) in GeV, anti-ttag",50,0,2000),"Sideband_top_anti_Topfirst_Bottoms_Pt",plotselection2+"&&Sideband_top_anti_Topfirst_Bottoms_Pt>0","1 anti-ttag"),
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_Eta" ,"eta(b), anti-ttag",60,-3,3),"Sideband_top_anti_Topfirst_Bottoms_Eta",plotselection2+"","1 anti-ttag"),        
        Plot(ROOT.TH1F("Sideband_top_anti_Topfirst_Bottoms_CSVv2" ,"CSVv2, anti-ttag",40,-1,1),"Sideband_top_anti_Topfirst_Bottoms_CSVv2",plotselection2+"&&Sideband_top_anti_Topfirst_Bottoms_CSVv2>-1","1 btag"),
        
        
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Zprime_M" ,"m(Z') in GeV, signal-anti-ttag ratio",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Tops_Pt" ,"p_{T}(t) in GeV, signal-anti-ttag ratio",50,0,2000),"Signal_Topfirst_Tops_Pt",plotselection2+"&&Signal_Topfirst_Tops_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Tops_MSD" ,"m_{SD}(t) in GeV, signal-anti-ttag ratio",60,0,300),"Signal_Topfirst_Tops_MSD",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Tops_t32" ,"tau_{32}(t), signal-anti-ttag ratio",20,0,1),"Signal_Topfirst_Tops_t32",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Ws_Pt" ,"p_{T}(W) in GeV, signal-anti-ttag ratio",50,0,2000),"Signal_Topfirst_Ws_Pt",plotselection2+"&&Signal_Topfirst_Ws_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Ws_MSD" ,"m_{SD}(W) in GeV, signal-anti-ttag ratio",60,0,300),"Signal_Topfirst_Ws_MSD",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Ws_t21" ,"tau_{21}(W), signal-anti-ttag ratio",20,0,1),"Signal_Topfirst_Ws_t21",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_bottom_anti_Bottoms_Pt" ,"p_{T}(b) in GeV, signal-anti-ttag ratio",50,0,2000),"Signal_Topfirst_Bottoms_Pt",plotselection2+"&&Signal_Topfirst_Bottoms_Pt>0","1 btag"),

        Plot(ROOT.TH1F("SB_SF_W_anti_Zprime_M" ,"m(Z') in GeV, signal-anti-Wtag ratio",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_W_anti_Tops_Pt" ,"p_{T}(t) in GeV, signal-anti-Wtag ratio",50,0,2000),"Signal_Topfirst_Tops_Pt",plotselection2+"&&Signal_Topfirst_Tops_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_W_anti_Tops_MSD" ,"m_{SD}(t) in GeV, signal-anti-Wtag ratio",60,0,300),"Signal_Topfirst_Tops_MSD",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_W_anti_Tops_t32" ,"tau_{32}(t), signal-anti-Wtag ratio",20,0,1),"Signal_Topfirst_Tops_t32",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_W_anti_Ws_Pt" ,"p_{T}(W) in GeV, signal-anti-Wtag ratio",50,0,2000),"Signal_Topfirst_Ws_Pt",plotselection2+"&&Signal_Topfirst_Ws_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_W_anti_Bottoms_Pt" ,"p_{T}(b) in GeV, signal-anti-Wtag ratio",50,0,2000),"Signal_Topfirst_Bottoms_Pt",plotselection2+"&&Signal_Topfirst_Bottoms_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_W_anti_Bottoms_CSVv2" ,"CSVv2, signal-anti-Wtag ratio",40,-1,1),"Signal_Topfirst_Bottoms_CSVv2",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        
        Plot(ROOT.TH1F("SB_SF_top_anti_Zprime_M" ,"m(Z') in GeV, signal-anti-btag ratio",50,0,5000),"Signal_Topfirst_Zprime_M",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_top_anti_Tops_Pt" ,"p_{T}(t) in GeV, signal-anti-btag ratio",50,0,2000),"Signal_Topfirst_Tops_Pt",plotselection2+"&&Signal_Topfirst_Tops_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_top_anti_Ws_Pt" ,"p_{T}(W) in GeV, signal-anti-btag ratio",50,0,2000),"Signal_Topfirst_Ws_Pt",plotselection2+"&&Signal_Topfirst_Ws_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_top_anti_Ws_MSD" ,"m_{SD}(W) in GeV, signal-anti-btag ratio",60,0,300),"Signal_Topfirst_Ws_MSD",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_top_anti_Ws_t21" ,"tau_{21}(W), signal-anti-btag ratio",20,0,1),"Signal_Topfirst_Ws_t21",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_top_anti_Bottoms_Pt" ,"p_{T}(b) in GeV, signal-anti-btag ratio",50,0,2000),"Signal_Topfirst_Bottoms_Pt",plotselection2+"&&Signal_Topfirst_Bottoms_Pt>0","1 btag"),
        Plot(ROOT.TH1F("SB_SF_top_anti_Bottoms_CSVv2" ,"CSVv2, signal-anti-btag ratio",40,-1,1),"Signal_Topfirst_Bottoms_CSVv2",plotselection2+"&&Signal_Topfirst_Zprime_M>0","1 btag"),



        Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M>0)"+"*QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M","1 btag"),
        Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt",plotselection2+"*(Sideband_bottom_anti_Topfirst_Tops_Pt>0 && QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0)"+"*QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0)"+"*QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),

        Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt",plotselection2+"*(Sideband_top_anti_Topfirst_Tops_Pt>0 && QCD_HT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)"+"*QCD_HT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_top_anti_Topfirst_Zprime_M>0 && QCD_HT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)"+"*QCD_HT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDMadgraph_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Ws_Pt",plotselection2+"*( Sideband_top_anti_Topfirst_Ws_Pt>0 && QCD_HT_SF_SB_top_anti_Signal_Topfirst_Ws_Pt>0)"+"*QCD_HT_SF_SB_top_anti_Signal_Topfirst_Ws_Pt","1 btag"),

        Plot(ROOT.TH1F("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,3),"QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M",plotselection2+"*(QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M>0)","1 btag"),
        Plot(ROOT.TH1F("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt" ,"m(Z') in GeV",50,0,3),"QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt",plotselection2+"*(QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0)","1 btag"),


        Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M>0)"+"*QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M","1 btag"),        
        Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt",plotselection2+"*(Sideband_bottom_anti_Topfirst_Tops_Pt>0 && QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0 )"+"*QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        Plot(ROOT.TH1F("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0 )"+"*QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
               
        Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt",plotselection2+"*(Sideband_top_anti_Topfirst_Tops_Pt>0 && QCD_PT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)"+"*QCD_PT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_top_anti_Topfirst_Zprime_M>0 && QCD_PT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt>0)"+"*QCD_PT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        Plot(ROOT.TH1F("Signal_SB_PredictiontantiQCDPythia8_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Ws_Pt",plotselection2+"*( Sideband_top_anti_Topfirst_Ws_Pt>0 && QCD_PT_SF_SB_top_anti_Signal_Topfirst_Ws_Pt>0)"+"*QCD_PT_SF_SB_top_anti_Signal_Topfirst_Ws_Pt","1 btag"),

        Plot(ROOT.TH1F("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,3),"QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M",plotselection2+"*(QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M>0 && anti_btag>0)","1 btag"),
        Plot(ROOT.TH1F("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt" ,"m(Z') in GeV",50,0,3),"QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt",plotselection2+"*(QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt>0 && anti_btag>0)","1 btag"),








        Plot(ROOT.TH1F("Signal_withtopbtag_Topfirst_Zprime_M" ,"m(Z') in GeV, withtopbtag",50,0,5000),"Signal_withtopbtag_Topfirst_Zprime_M",plotselection2+"&&Signal_withtopbtag_Topfirst_Zprime_M>0","2 btags"),
        Plot(ROOT.TH1F("Signal_withtopbtag_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, withtopbtag",50,0,2000),"Signal_withtopbtag_Topfirst_Tops_Pt",plotselection2+"&&Signal_withtopbtag_Topfirst_Tops_Pt>0","2 btag"),
        Plot(ROOT.TH1F("Signal_withtopbtag_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, withtopbtag",50,0,2000),"Signal_withtopbtag_Topfirst_Ws_Pt",plotselection2+"&&Signal_withtopbtag_Topfirst_Ws_Pt>0","2 btag"),
        
        Plot(ROOT.TH1F("Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M" ,"m(Z') in GeV, withtopbtag and anti-btag",50,0,5000),"Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M",plotselection2+"&&Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M>0 && anti_btag_withtopbtag>0","1 anti-btag, 1 topbtag"),
        Plot(ROOT.TH1F("Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, withtopbtag and anti-btag",50,0,2000),"Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt",plotselection2+"&&Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt>0 && anti_btag_withtopbtag>0","1 anti-btag, 1 topbtag"),

        Plot(ROOT.TH1F("Sideband_top_withbtag_anti_Topfirst_Tops_Pt" ,"p_{T}(t) in GeV, withtopbtag anti-ttag",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Tops_Pt",plotselection2+"&&Sideband_top_withbtag_anti_Topfirst_Tops_Pt>0","1 anti-ttag withb"),
        Plot(ROOT.TH1F("Sideband_top_withbtag_anti_Topfirst_Ws_Pt" ,"p_{T}(W) in GeV, withtopbtag anti-ttag",50,0,2000),"Sideband_top_withbtag_anti_Topfirst_Ws_Pt",plotselection2+"&&Sideband_top_withbtag_anti_Topfirst_Ws_Pt>0","1 anti-ttag withb"),

        Plot(ROOT.TH1F("SB_SF_withtopbtag_bottom_anti_Zprime_M" ,"m(Z') in GeV, withtopbtag",50,0,5000),"Signal_withtopbtag_Topfirst_Zprime_M",plotselection2+"&&Signal_withtopbtag_Topfirst_Zprime_M>0","2 btags"),
        Plot(ROOT.TH1F("SB_SF_withtopbtag_bottom_anti_Tops_Pt" ,"m(Z') in GeV, withtopbtag",50,0,2000),"Signal_withtopbtag_Topfirst_Tops_Pt",plotselection2+"&&Signal_withtopbtag_Topfirst_Tops_Pt>0","2 btags"),
        Plot(ROOT.TH1F("SB_SF_withtopbtag_top_anti_Tops_Pt" ,"p_{T}(t) in GeV, withtopbtag",50,0,2000),"Signal_withtopbtag_Topfirst_Tops_Pt",plotselection2+"&&Signal_withtopbtag_Topfirst_Tops_Pt>0","2 btag"),
        Plot(ROOT.TH1F("SB_SF_withtopbtag_top_anti_Ws_Pt" ,"p_{T}(W) in GeV, withtopbtag",50,0,2000),"Signal_withtopbtag_Topfirst_Ws_Pt",plotselection2+"&&Signal_withtopbtag_Topfirst_Ws_Pt>0","2 btag"),



        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag_withtopbtag>0)"+"*QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt",plotselection2+"*(Sideband_bottom_anti_Topfirst_Tops_Pt>0 && anti_btag_withtopbtag>0)"+"*QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag_withtopbtag>0)"+"*QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),

        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt",plotselection2+"*(Sideband_top_anti_Topfirst_Tops_Pt>0)"+"*QCD_HT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_top_anti_Topfirst_Zprime_M>0)"+"*QCD_HT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDMadgraph_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Ws_Pt",plotselection2+"*( Sideband_top_anti_Topfirst_Ws_Pt>0)"+"*QCD_HT_SF_SB_top_anti_Signal_Topfirst_Ws_Pt","1 btag"),

        #Plot(ROOT.TH1F("QCDMadgraph_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,3),"QCD_HT_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M",plotselection2+"*(QCD_HT_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M>0)","1 btag"),
        #Plot(ROOT.TH1F("QCDMadgraph_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt" ,"m(Z') in GeV",50,0,3),"QCD_HT_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt",plotselection2+"*(QCD_HT_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt>0)","1 btag"),


        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag_withtopbtag>0)"+"*QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M","1 btag"),        
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_bottom_anti_Topfirst_Tops_Pt",plotselection2+"*(Sideband_bottom_anti_Topfirst_Tops_Pt>0 && anti_btag_withtopbtag>0)"+"*QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_bottom_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_bottom_anti_Topfirst_Zprime_M>0 && anti_btag_withtopbtag>0)"+"*QCD_PT_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt","1 btag"),
               
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt" ,"p_{T}(t) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Tops_Pt",plotselection2+"*(Sideband_top_anti_Topfirst_Tops_Pt>0)"+"*QCD_PT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,5000),"Sideband_top_anti_Topfirst_Zprime_M",plotselection2+"*(Sideband_top_anti_Topfirst_Zprime_M>0)"+"*QCD_PT_SF_SB_top_anti_Signal_Topfirst_Tops_Pt","1 btag"),
        #Plot(ROOT.TH1F("Signal_withtopbtag_SB_PredictiontantiQCDPythia8_Topfirst_W_Pt" ,"p_{T}(W) in GeV",50,0,2000),"Sideband_top_anti_Topfirst_Ws_Pt",plotselection2+"*( Sideband_top_anti_Topfirst_Ws_Pt>0)"+"*QCD_PT_SF_SB_top_anti_Signal_Topfirst_Ws_Pt","1 btag"),

        #Plot(ROOT.TH1F("QCDPythia8_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M" ,"m(Z') in GeV",50,0,3),"QCD_PT_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M",plotselection2+"*(QCD_PT_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Zprime_M>0)","1 btag"),
        #Plot(ROOT.TH1F("QCDPythia8_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt" ,"m(Z') in GeV",50,0,3),"QCD_PT_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt",plotselection2+"*(QCD_PT_SF_SB_bottom_anti_Signal_withtopbtag_Topfirst_Tops_Pt>0)","1 btag"),




        Plot(ROOT.TH1F("N_packedPatJetsAK8PFCHSSoftDrop" ,"N_packedPatJetsAK8PFCHSSoftDrop",10,0,10),"N_packedPatJetsAK8PFCHSSoftDrop",plotselection1+"",""),
        Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_1_Pt" ,"p_{T}(AK8_1) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[0]",plotselection1+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[0]>0",""),
        Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_2_Pt" ,"p_{T}(AK8_2) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[1]",plotselection1+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[1]>0",""),
        Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_3_Pt" ,"p_{T}(AK8_3) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[2]",plotselection1+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[2]>0",""),
        Plot(ROOT.TH1F("packedPatJetsAK8PFCHSSoftDrop_4_Pt" ,"p_{T}(AK8_4) in GeV",50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[3]",plotselection1+"&&packedPatJetsAK8PFCHSSoftDrop_Pt[3]>0",""),

        Plot(ROOT.TH1F("N_Jets" ,"N_Jets",10,0,10),"N_Jets",plotselection1+"",""),
        Plot(ROOT.TH1F("Jet_1_Pt" ,"p_{T}(AK4_1) in GeV",50,0,1000),"Jet_Pt[0]",plotselection1+"&&Jet_Pt[0]>0",""),
        Plot(ROOT.TH1F("Jet_2_Pt" ,"p_{T}(AK4_2) in GeV",50,0,1000),"Jet_Pt[1]",plotselection1+"&&Jet_Pt[1]>0",""),
        Plot(ROOT.TH1F("Jet_3_Pt" ,"p_{T}(AK4_3) in GeV",50,0,1000),"Jet_Pt[2]",plotselection1+"&&Jet_Pt[2]>0",""),
        Plot(ROOT.TH1F("Jet_4_Pt" ,"p_{T}(AK4_4) in GeV",50,0,1000),"Jet_Pt[3]",plotselection1+"&&Jet_Pt[3]>0",""),
        
        Plot(ROOT.TH1F("Evt_HT" ,"Evt_HT",60,0,3000),"Evt_HT",plotselection3+"",""),
        Plot(ROOT.TH1F("Evt_HT_Jets" ,"Evt_HT_Jets",60,0,3000),"Evt_HT_Jets",plotselection3+"",""),
        
        Plot(ROOT.TH1F("Jet_GenJet_Pt" ,"Jet_GenJet_Pt",40,0,2000),"Jet_GenJet_Pt",plotselection1+"",""),
        
        
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
        #TwoDimPlot(ROOT.TH2F("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M_VS_Sideband_bottom_anti_Topfirst_Zprime_M" ,"",50,-1,2,50,0,5000),"QCD_HT_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M","Sideband_bottom_anti_Topfirst_Zprime_M","","1 btag"),






]





plotnames=[]
for i in plots:
    plotnames.append(i.name)

#plotnamesABCD=[]
#for i in plotsABCD:
    #plotnamesABCD.append(i.name)



print name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples)
outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples,[""],["1"],[""],["1"],additionalvariables,additionalfunctions)
#outputpath=plotParallel(name,2000000,plotsABCD,SignalSamples)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)

listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples,plots,1)
listOfHistoListsBackground=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,DataSamples,plots,1)


#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
#if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    #renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames,False)
#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)
#lllcsv=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,CSVSystnames)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_bottom_anti_Zprime_M"),plotnames.index("Sideband_bottom_anti_Topfirst_Zprime_M"),True, 1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_bottom_anti_Tops_Pt"),plotnames.index("Sideband_bottom_anti_Topfirst_Tops_Pt"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_bottom_anti_Tops_MSD"),plotnames.index("Sideband_bottom_anti_Topfirst_Tops_MSD"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_bottom_anti_Tops_t32"),plotnames.index("Sideband_bottom_anti_Topfirst_Tops_t32"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_bottom_anti_Ws_Pt"),plotnames.index("Sideband_bottom_anti_Topfirst_Ws_Pt"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_bottom_anti_Ws_MSD"),plotnames.index("Sideband_bottom_anti_Topfirst_Ws_MSD"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_bottom_anti_Ws_t21"),plotnames.index("Sideband_bottom_anti_Topfirst_Ws_t21"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_bottom_anti_Bottoms_Pt"),plotnames.index("Sideband_bottom_anti_Topfirst_Bottoms_Pt"),True, 1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_W_anti_Zprime_M"),plotnames.index("Sideband_top_anti_Topfirst_Zprime_M"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_W_anti_Tops_Pt"),plotnames.index("Sideband_W_anti_Topfirst_Tops_Pt"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_W_anti_Tops_MSD"),plotnames.index("Sideband_W_anti_Topfirst_Tops_MSD"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_W_anti_Tops_t32"),plotnames.index("Sideband_W_anti_Topfirst_Tops_t32"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_W_anti_Ws_Pt"),plotnames.index("Sideband_W_anti_Topfirst_Ws_Pt"),True, 1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_W_anti_Bottoms_Pt"),plotnames.index("Sideband_W_anti_Topfirst_Bottoms_Pt"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_W_anti_Bottoms_CSVv2"),plotnames.index("Sideband_W_anti_Topfirst_Bottoms_CSVv2"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_top_anti_Zprime_M"),plotnames.index("Sideband_top_anti_Topfirst_Zprime_M"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_top_anti_Tops_Pt"),plotnames.index("Sideband_top_anti_Topfirst_Tops_Pt"),True, 1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_top_anti_Ws_Pt"),plotnames.index("Sideband_top_anti_Topfirst_Ws_Pt"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_top_anti_Ws_MSD"),plotnames.index("Sideband_top_anti_Topfirst_Ws_MSD"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_top_anti_Ws_t21"),plotnames.index("Sideband_top_anti_Topfirst_Ws_t21"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_top_anti_Bottoms_Pt"),plotnames.index("Sideband_top_anti_Topfirst_Bottoms_Pt"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_top_anti_Bottoms_CSVv2"),plotnames.index("Sideband_top_anti_Topfirst_Bottoms_CSVv2"),True,1)


divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_withtopbtag_bottom_anti_Zprime_M"),plotnames.index("Sideband_withtopbtag_bottom_anti_Topfirst_Zprime_M"),True, 1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_withtopbtag_bottom_anti_Tops_Pt"),plotnames.index("Sideband_withtopbtag_bottom_anti_Topfirst_Tops_Pt"),True,1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_withtopbtag_top_anti_Tops_Pt"),plotnames.index("Sideband_top_withbtag_anti_Topfirst_Tops_Pt"),True, 1)
divideHistos(listOfHistoListsBackground,plotnames.index("SB_SF_withtopbtag_top_anti_Ws_Pt"),plotnames.index("Sideband_top_withbtag_anti_Topfirst_Ws_Pt"),True,1)



#print listOfHistoListsData[plotnames.index("AK8_top_misstagged_candidates_pt")]

#divideHistos(listOfHistoListsData,plotnames.index("t_tagrate_pt"),plotnames.index("AK8_top_tag_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("W_tagrate_pt"),plotnames.index("AK8_W_tag_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("b_tagrate_pt"),plotnames.index("AK4_bottom_tag_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("t_misstagrate_pt"),plotnames.index("AK8_top_misstagged_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("W_misstagrate_pt"),plotnames.index("AK8_W_misstagged_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("b_misstagrate_pt"),plotnames.index("AK4_bottom_misstagged_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("tanti_tagrate_pt"),plotnames.index("AK8_top_misstagged_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("Wanti_tagrate_pt"),plotnames.index("AK8_W_misstagged_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("banti_tagrate_pt"),plotnames.index("AK4_bottom_misstagged_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("tanti_misstagrate_pt"),plotnames.index("AK8_top_tag_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("Wanti_misstagrate_pt"),plotnames.index("AK8_W_tag_candidates_pt"),False,1,'B')
#divideHistos(listOfHistoListsData,plotnames.index("banti_misstagrate_pt"),plotnames.index("AK4_bottom_tag_candidates_pt"),False,1,'B')


#LOLSumw2(listOfHistoLists)
#dummylist=[[]]
labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)
lolSignalT=transposeLOL(listOfHistoListsSignal)
lolBackgroundT=transposeLOL(listOfHistoListsBackground)
#lolDataT=transposeLOL(listOfHistoListsData)

#writeLOLSeveralOnTop(transposeLOL(lolT[3:5]),samples[3:5],transposeLOL(lolT[:3]),samples[:3],-0.2,'Zprime',False ,'histoE','samehistoE')
#writeListOfHistoLists(transposeLOL(lolT[3:5])[:92],samples[3:5],'Zprime_HT_Pt_comparison','Zprime_HT_Pt_comparison',True,False,False,'EL',False,False,True)
#writeHistoListwithXYErrors(transposeLOL(lolT[3:5])[60:82],samples[3:5],'Zprime_BKG',1)
#writeListOfHistoLists(transposeLOL(lolT[5:6])[92:110],samples[5:6],'tagrates','tagrates',False,False,False,'EL')


#writeLOLSeveralOnTop(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("ttbar")+1])[:plotnames.index("Sideband_top_anti_Topfirst_Bottoms_CSVv2")+1],BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("ttbar")+1],transposeLOL(lolSignalT),SignalSamples,-0.2,'Zprime',True,False ,'histoE','samehistoE')

#writeListOfHistoLists(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("ttbar")+1])[plotnames.index("Signal_Topfirst_Zprime_M"):plotnames.index("Sideband_bottom_anti_Topfirst_Zprime_M")+1],BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("ttbar")+1],labels,'Zprime_DPG',True,True,False,'histoE')
#writeListOfHistoLists( transposeLOL([listOfHistoListsBackground[plotnames.index('Signal_Topfirst_Zprime_M')]]+[listOfHistoListsBackground[plotnames.index('Signal_SB_Predictionbanti_Topfirst_Zprime_M')]]) , BackgroundSamples , BackgroundSampleNames , 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)


################################### AB Closure ########################################
######Using HT SBSSSSF
####from banti sideband
writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#####from tanti sideband
writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] ,[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#####same?
writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("QCDMadgraph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("QCDPythia8_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)


writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#####from tanti sideband
writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDMadgraphTopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingMadgraphSBSSSF' , True , False, False, "histoE", False, False, True, False)

#####same?
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation_PT' , True , False, False, "histoE", False, False, True, False)

#######Using PT SBSSSF
####from banti sideband
writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#####from tanti sideband
writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] ,[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#####same?
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]])[plotnames.index('SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]] , [plotnames[plotnames.index("SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation' , True , False, False, "histoE", False, False, True, False)


writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8ZprimeM_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("Signal_SB_PredictionbantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#####from tanti sideband
writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Top_Pt")]]+[plotnames[plotnames.index("Signal_Topfirst_Tops_Pt")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('Signal_Topfirst_Zprime_M')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("Signal_SB_PredictiontantiQCDPythia8TopPt_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("Signal_Topfirst_Zprime_M")]], 'ABbackgroundestimation_usingPythia8SBSSSF' , True , False, False, "histoE", False, False, True, False)

#####same?
#writeListOfHistoLists( [transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_Topfirst_Zprime_M')]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index('SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt')]] , [BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]] , [plotnames[plotnames.index("SF_SB_bottom_anti_Signal_Topfirst_Zprime_M")]]+[plotnames[plotnames.index("SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt")]], 'AB_background_estimation_PT' , True , False, False, "histoE", False, False, True, False)



#################################################################################



#BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1],labels,'Zprime_HT_Pt_comparison',True,False,False,'EL',False,False,True)

#writeListOfHistoLists(transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("Signal_Topfirst_Zprime_M"):plotnames.index("Jet_GenJet_Pt")+1],[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]],labels,'Zprime_HT_Pt_comparison',True,False,False,'histoE',False,False,True)
#BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1],labels,'Zprime_HT_Pt_comparison',True,False,False,'EL',False,False,True)


#writeHistoListwithXYErrors(transposeLOL(lolBackgroundT)[plotnames.index("SB_SF_top_anti_Tops_Pt"):plotnames.index("SB_SF_top_anti_Ws_MSD")],BackgroundSamples,'Zprime_SBSSFs_tanti',1,"[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))/x")
#writeHistoListwithXYErrors(transposeLOL(lolBackgroundT)[plotnames.index("SB_SF_bottom_anti_Zprime_M"):plotnames.index("SB_SF_bottom_anti_Tops_MSD")],BackgroundSamples,'Zprime_SBSSFs_banti',1,'pol2')




writeHistoListwithXYErrors(transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_top_anti_Tops_Pt"):plotnames.index("SB_SF_top_anti_Ws_MSD")+1]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_withtopbtag_top_anti_Tops_Pt"):plotnames.index("SB_SF_withtopbtag_top_anti_Ws_Pt")+1],[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]],'Zprime_SBSSSFs_tanti',1,"[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))/x")
writeHistoListwithXYErrors(transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_bottom_anti_Zprime_M"):plotnames.index("SB_SF_bottom_anti_Tops_MSD")+1]+transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_withtopbtag_bottom_anti_Zprime_M"):plotnames.index("SB_SF_withtopbtag_bottom_anti_Tops_Pt")+1],[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]],'Zprime_SBSSSFs_banti',1,'pol2')


#writeHistoListwithXYErrors(transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_withtopbtag_top_anti_Tops_Pt"):plotnames.index("SB_SF_withtopbtag_top_anti_Ws_Pt")],[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]],'Zprime_SBSSSFs_tanti',1,"[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))/x")
#writeHistoListwithXYErrors(transposeLOL([lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph")]]+[lolBackgroundT[BackgroundSampleNames.index("QCDPythia8")]])[plotnames.index("SB_SF_withtopbtag_bottom_anti_Zprime_M"):plotnames.index("SB_SF_withtopbtag_bottom_anti_Tops_Pt")],[BackgroundSamples[BackgroundSampleNames.index("QCDMadgraph")]]+[BackgroundSamples[BackgroundSampleNames.index("QCDPythia8")]],'Zprime_SBSSSFs_banti',1,'pol2')

#####################TAGRATES############################
#writeListOfHistoLists(transposeLOL(lolDataT[DataSampleNames.index("MC_BKG_DATA"):])[plotnames.index("t_tagrate_pt"):plotnames.index("b_misstagrate_pt")+1],DataSamples,'tagrates','tagrates',False,False,False,'EL') 
#writeHistoListwithXYErrors(transposeLOL(lolDataT[DataSampleNames.index("MC_BKG_DATA"):])[plotnames.index("t_tagrate_pt"):plotnames.index("b_misstagrate_pt")+1],DataSamples,'tagrates_fit',1,"[0]+([1]*log(x-[3])+[2]*log(x-[3])*log(x-[3]))/x")



#SchmonCorrelation(transposeLOL(lolT[3:5])[plotnames.index("SB_SF_bottom_anti_Bottoms_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_W_anti_Ws_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_top_anti_Tops_Pt")],transposeLOL(lolT[3:5])[plotnames.index("SB_SF_bottom_anti_Bottoms_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_W_anti_Ws_Pt")]+transposeLOL(lolT[3:5])[plotnames.index("SB_SF_top_anti_Tops_Pt")],name='lada', rebin=1)
#SchmonCorrelation(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("SB_SF_bottom_anti_Bottoms_Pt")]+transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("SB_SF_W_anti_Ws_Pt")]+transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("SB_SF_top_anti_Tops_Pt")],transposeLOL(lolDataT)[plotnames.index("t_misstagrate_pt")]+transposeLOL(lolDataT)[plotnames.index("W_misstagrate_pt")]+transposeLOL(lolDataT)[plotnames.index("b_misstagrate_pt")],name='correlations', rebin=1)


#print transposeLOL(lolBackgroundT[BackgroundSampleNames.index("QCDMadgraph"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("N_packedPatJetsAK8PFCHSSoftDrop"):plotnames.index("Evt_HT_Jets")+1]



#writeListOfHistoLists(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("ABCD_top_tau32_vs_top_MSD"):plotnames.index("ABCD_top_tau32_vs_W_MSD")],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1],plotnames[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('ABCD_W_MSD_vs_Bottom_CSV_v2')+1],'ABCD',True,False,False,'colz',False,False,False,False)

#writeListOfHistoLists(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1])[plotnames.index("ABCD_top_tau32_vs_top_MSD"):plotnames.index("Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M_VS_Sideband_bottom_anti_Topfirst_Zprime_M")],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCDPythia8")+1],plotnames[plotnames.index('ABCD_top_tau32_vs_top_MSD'):plotnames.index('Signal_SB_PredictionbantiQCDMadgraphZprimeM_Topfirst_Zprime_M_VS_Sideband_bottom_anti_Topfirst_Zprime_M')+1],'ahhh',True,False,False,'colz',False,False,False,False)
