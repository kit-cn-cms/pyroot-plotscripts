#############
# plot general control distributions 
##############

from plotconfig_Zprime_MC_DATA_comparison import *
from plot_additional_Zprime_MC_DATA_comparison import *
from plot_cuts_ZPrime_MC_DATA_comparison import *

sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy


ABCDeventhandling='DATA_MC_comparison'

name='Zprime_DATA_MC_comparison'+'_'+ABCDversion+radi+'_'+WPs

#if doBR:
    #name=name+'_'+BR_name
verybasicplotselection="Evt_HT_Jets>1000"



plots=[

   


    #ABCD
    #no topbtag
    #Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatA_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatB_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1  ,"1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatC_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatD_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),

    #Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatE_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatF_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatG_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3  + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatH_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag") ,

    ##withtopsubbtag
    ##Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatA_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "2 btag"),
    ##Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatB_Zprime_M" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatB_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1  ,"2 btag"),
    ##Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatC_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2_anti + "&& " + cut1  ,"2 btag"),
    ##Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatD_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1  ,"2 btag"),

    #Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatE_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1_anti  ,"2 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatF_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1_anti  ,"2 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatG_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3  + "&&" + cut2_anti + "&& " + cut1_anti  ,"2 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD" + radi +"_M", "ABCD_CatID==ABCD_CatH_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1_anti  ,"2 btag") ,
    
   
    
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Bottom_Pt" ,"p_{T}(b-jet) in GeV, CatA " ,50,0,1000),"Bottoms_ABCD" + radi + "_Pt", "Bottoms_ABCD" + radi + "_Pt>0 &&" + verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2_anti + " && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Bottom_Pt" ,"p_{T}(b-jet) in GeV, CatA " ,50,0,1000),"Bottoms_ABCD" + radi + "_Pt","Bottoms_ABCD" + radi + "_Pt>0 &&" + verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2 + " && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Bottom_CSV" ,"CSV_v2(b-jet), CatA " ,51,-0.1,1),"Bottoms_ABCD" + radi + "_CSV",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2_anti + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Bottom_CSV" ,"CSV_v2(b-jet), CatA " ,51,-0.1,1),"Bottoms_ABCD" + radi + "_CSV",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2 + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD, "2 btag"),  
    
    
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_W_Pt" ,"p_{T}(t-jet) in GeV, CatA " ,50,0,1000),"Ws_ABCD" + radi + "_Pt","Ws_ABCD" + radi + "_Pt>0 &&" + verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2_anti + " && Bottoms_ABCD" + radi + "_Pt>100 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_W_Pt" ,"p_{T}(t-jet) in GeV, CatA " ,50,0,1000),"Ws_ABCD" + radi + "_Pt","Ws_ABCD" + radi + "_Pt>0 &&" +  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2 + " && Bottoms_ABCD" + radi + "_Pt>100 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_W_M" ,"m(W-jet) in GeV, CatA " ,50,0,500),"Ws_ABCD" + radi + "_MSD",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2_anti + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_B_CSV, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_W_M" ,"m(W-jet) in GeV, CatA " ,50,0,500),"Ws_ABCD" + radi + "_MSD",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2 + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_B_CSV, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_W_t21" ,"#tau_{21}(W-jet) in GeV, CatA " ,50,0,1),"Ws_ABCD" + radi + "_t21",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2_anti + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_W_t21" ,"#tau_{21}(W-jet) in GeV, CatA " ,50,0,1),"Ws_ABCD" + radi + "_t21",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2 + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "2 btag"),   
 
 
 
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Top_Pt" ,"p_{T}(t-jet) in GeV, CatA " ,50,0,1000),"Tops_ABCD" + radi + "_Pt","Tops_ABCD" + radi + "_Pt>0 &&" +  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2_anti + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Top_Pt" ,"p_{T}(t-jet) in GeV, CatA " ,50,0,1000),"Tops_ABCD" + radi + "_Pt","Tops_ABCD" + radi + "_Pt>0 &&" +  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2 + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Top_M" ,"m(t-jet) in GeV, CatA " ,50,0,500),"Tops_ABCD" + radi + "_MSD",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2_anti + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Top_M" ,"m(t-jet) in GeV, CatA " ,50,0,500),"Tops_ABCD" + radi + "_MSD",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2 + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Top_t32" ,"#tau_{32}(t-jet) in GeV, CatA " ,50,0,1),"Tops_ABCD" + radi + "_t32",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2_anti + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Top_t32" ,"#tau_{32}(t-jet) in GeV, CatA " ,50,0,1),"Tops_ABCD" + radi + "_t32",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && " + plotselection_topsubjetCSVv2 + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, "2 btag"),  
    
    Plot(ROOT.TH1F( ABCDversion + "_CatA_Topsubjets_MaxCSV" ,"maxCSV_v2(top sub-jet), CatA " ,50,0,1),"Tops_ABCD" + radi + "_maxsubjetCSVv2",  verybasicplotselection + " && " + plotselection_TprimeMass_anti + " && Bottoms_ABCD" + radi + "_Pt>100 && Ws_ABCD" + radi + "_Pt>200 && Tops_ABCD" + radi + "_Pt>400" + " && " + plotselection_tau32 + " && " + plotselection_t_MSD + " && " + plotselection_W_tau21 + " && " + plotselection_W_MSD + " && " + plotselection_B_CSV, ""),
        
    #Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_HTtWb" ,"HT_{tWb}, CatA " ,50,0,5000),"EvtHT_tWb","EvtHT_tWb>0 &&" + "ABCD_CatID==ABCD_CatA_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "1 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_HTtWb" ,"HT_{tWb}, CatA " ,50,0,5000),"EvtHT_tWb","EvtHT_tWb>0 &&" + "ABCD_CatID==ABCD_CatA_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "2 btag"),
        
        
    Plot(ROOT.TH1F( "N_PrimaryVertices" ,"N_PrimaryVertices" ,50,-0.5,49.5),"N_PrimaryVertices",verybasicplotselection, ""),
    Plot(ROOT.TH1F( "Evt_HT_Jets" ,"HT_{Evt} in GeV" ,50,0,5000),"Evt_HT_Jets",verybasicplotselection, ""),
    Plot(ROOT.TH1F( "NAK4" ,"N(AK4-jets)" ,9,2.5,11.5),"N_Jets",verybasicplotselection, ""),
    Plot(ROOT.TH1F( "NAK8" ,"N(AK4-jets" ,10,1.5,11.5),"N_packedPatJetsAK8PFCHSSoftDrop",verybasicplotselection + "&& N_packedPatJetsAK8PFCHSSoftDrop>-1", ""),    
    
    Plot(ROOT.TH1F( "N_BTagsM" ,"N(medium b-tagged AK4-jets)" ,10,-0.5,9.5),"N_BTagsM",verybasicplotselection, ""),
    
    Plot(ROOT.TH1F( "AK4_pT" ,"p_{T}(AK4-jets) in GeV" ,50,0,2000),"Jet_Pt","Jet_Pt &&" + verybasicplotselection, ""),        
    Plot(ROOT.TH1F( "AK4_Eta" ,"#eta (AK4-jets)" ,50,-2.5,2.5),"Jet_Eta",verybasicplotselection, ""),         
    Plot(ROOT.TH1F( "AK8_pT" ,"p_{T}(AK8-jets) in GeV" ,50,0,2000),"packedPatJetsAK8PFCHSSoftDrop_Pt","packedPatJetsAK8PFCHSSoftDrop_Pt>0 &&" + verybasicplotselection, ""),
    Plot(ROOT.TH1F( "AK8_Eta" ,"#eta (AK8-jets)" ,50,-2.5,2.5),"packedPatJetsAK8PFCHSSoftDrop_Eta",verybasicplotselection, ""),        
    
    Plot(ROOT.TH1F( "AK4_1_pT" ,"p_{T}(first AK4-jet) in GeV" ,50,0,2000),"Jet_Pt[0]","Jet_Pt[0] &&" + verybasicplotselection, ""),            
    Plot(ROOT.TH1F( "AK4_2_pT" ,"p_{T}(second AK4-jet) in GeV" ,50,0,2000),"Jet_Pt[1]","Jet_Pt[1] &&" + verybasicplotselection, ""),            
    Plot(ROOT.TH1F( "AK4_3_pT" ,"p_{T}(third AK4-jet) in GeV" ,50,0,1000),"Jet_Pt[2]","Jet_Pt[2] &&" + verybasicplotselection, ""),            
    Plot(ROOT.TH1F( "AK4_4_pT" ,"p_{T}(forth AK4-jet) in GeV" ,50,0,1000),"Jet_Pt[3]","Jet_Pt[3] &&" + verybasicplotselection, ""),            
    Plot(ROOT.TH1F( "AK4_1_Eta" ,"#eta (first AK4-jet)" ,50,-2.5,2.5),"Jet_Eta[0]","Jet_Pt[0] &&" + verybasicplotselection, ""),           
    Plot(ROOT.TH1F( "AK4_2_Eta" ,"#eta (second AK4-jet)" ,50,-2.5,2.5),"Jet_Eta[1]","Jet_Pt[1] &&" + verybasicplotselection, ""),           
    Plot(ROOT.TH1F( "AK4_3_Eta" ,"#eta (third AK4-jet)" ,50,-2.5,2.5),"Jet_Eta[2]","Jet_Pt[2] &&" + verybasicplotselection, ""),            
    Plot(ROOT.TH1F( "AK4_4_Eta" ,"#eta (fourth AK4-jet)" ,50,-2.5,2.5),"Jet_Eta[3]","Jet_Pt[3] &&" + verybasicplotselection, ""),           

    Plot(ROOT.TH1F( "AK8_1_pT" ,"p_{T}(first AK8-jet) in GeV" ,50,0,2000),"packedPatJetsAK8PFCHSSoftDrop_Pt[0]","packedPatJetsAK8PFCHSSoftDrop_Pt[0]>0 &&" +verybasicplotselection, ""),      
    Plot(ROOT.TH1F( "AK8_2_pT" ,"p_{T}(second AK8-jet) in GeV" ,50,0,2000),"packedPatJetsAK8PFCHSSoftDrop_Pt[1]","packedPatJetsAK8PFCHSSoftDrop_Pt[1]>0 &&" +verybasicplotselection, ""),
    Plot(ROOT.TH1F( "AK8_3_pT" ,"p_{T}(third AK8-jet) in GeV" ,50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[2]","packedPatJetsAK8PFCHSSoftDrop_Pt[2]>0 &&" +verybasicplotselection, ""),
    Plot(ROOT.TH1F( "AK8_4_pT" ,"p_{T}(forth AK8-jet) in GeV" ,50,0,1000),"packedPatJetsAK8PFCHSSoftDrop_Pt[3]","packedPatJetsAK8PFCHSSoftDrop_Pt[3]>0 &&" +verybasicplotselection, ""),
    Plot(ROOT.TH1F( "AK8_1_Eta" ,"#eta (first AK8-jet)" ,50,-2.5,2.5),"packedPatJetsAK8PFCHSSoftDrop_Eta[0]","packedPatJetsAK8PFCHSSoftDrop_Pt[0] &&" + verybasicplotselection, ""),
    Plot(ROOT.TH1F( "AK8_2_Eta" ,"#eta (second AK8-jet)" ,50,-2.5,2.5),"packedPatJetsAK8PFCHSSoftDrop_Eta[1]","packedPatJetsAK8PFCHSSoftDrop_Pt[1] &&" + verybasicplotselection, ""),
    Plot(ROOT.TH1F( "AK8_3_Eta" ,"#eta (third AK8-jet)" ,50,-2.5,2.5),"packedPatJetsAK8PFCHSSoftDrop_Eta[2]","packedPatJetsAK8PFCHSSoftDrop_Pt[2] &&" + verybasicplotselection, ""),
    Plot(ROOT.TH1F( "AK8_4_Eta" ,"#eta (fourth AK8-jet)" ,50,-2.5,2.5),"packedPatJetsAK8PFCHSSoftDrop_Eta[3]","packedPatJetsAK8PFCHSSoftDrop_Pt[3] &&" + verybasicplotselection, ""),
       
    
]





plotnames=[]
for i in plots:
    plotnames.append(i.name)

OnlyFirstList=len(plots)*[False]
#OnlyFirstList[plotnames.index("ABCD1_notopbtag_CatA_Zprime_M"):plotnames.index('ABCD2_inclusive_CatH_Tprime_M') +1 ] = len(OnlyFirstList[plotnames.index("ABCD1_notopbtag_CatA_Zprime_M"):plotnames.index('ABCD2_inclusive_CatH_Tprime_M') + 1 ] ) * [True]
#OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Bottom_Pt"):plotnames.index(ABCDversion + "_withtopbtag_CatA_HTtWb") +1 ] = len(OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Bottom_Pt"):plotnames.index(ABCDversion + "_withtopbtag_CatA_HTtWb") + 1 ] ) * [True]
OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Bottom_Pt"):plotnames.index(ABCDversion + "_CatA_Topsubjets_MaxCSV") +1 ] = len(OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Bottom_Pt"):plotnames.index(ABCDversion + "_CatA_Topsubjets_MaxCSV") + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'



#print allweightsystnames
#print allsystweights

#print name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM,systweightsbasic+systweightsMadgraphbantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weightsystnamesPythia8bantiZprimeM,systweightsPythia8bantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
#print allweightsystnames
#print allsystweights, "OK"
#raw_input()

outputpath=plotParallel(name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples+systsamples,[""],["1"],allweightsystnames,allsystweights,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList,otherSystNames)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)


#rebinnedHistosExist=False
#rebinnedHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned.root'
#rebinnedandaddedHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_added.root'
#rebinnedandaddedBRHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_added_'+BR_name+'.root'


allweightsystnames=allweightsystnames+JECsystnames
print allweightsystnames

#print 'debug filesave 1 ', rebinnedHistoPath[:-5]
#print 'debug filesave 2 ', rebinnedandaddedHistoPath[:-5]
#print 'debug filesave 3 ', rebinnedandaddedBRHistoPath[:-5]


lllSignal=createLLL_fromSuperHistoFileSyst(outputpath,SignalSamples,plots,allweightsystnames)
lllBackground=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,allweightsystnames)
#lllData=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,allweightsystnames)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,DataSamples,plots,1)

#print Datalll

DataLoL=[]


for plotname in plotnames:
    
    if plotname=="N_BTagsM":

        BackgroundLOL=transposeLOL([[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')][allweightsystnames.index('_All_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ttbar')][allweightsystnames.index('_All_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_tW')][allweightsystnames.index('_All_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_t')][allweightsystnames.index('_All_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_s')][allweightsystnames.index('_All_nominal')]]])
        SignalLOL=[[lllSignal[plotnames.index(plotname)][SignalSampleNames.index('Zprimeall')][allweightsystnames.index('_All_nominal')]]]
    
        QCDlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_MCSF_CSVLFUp'):allweightsystnames.index('_All_MCSF_renfac_envDown')])[BackgroundSampleNames.index('QCDMadgraph')]]

        ttbarlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_MCSF_CSVLFUp'):allweightsystnames.index('_All_ttbarXSDown')])[BackgroundSampleNames.index('ttbar')]]
        
        STlll=transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_MCSF_CSVLFUp'):allweightsystnames.index('_All_ttbarXSDown')])[BackgroundSampleNames.index('ST_tW'):BackgroundSampleNames.index('ST_s')+1]

        listOflll=[[[QCDlll+ttbarlll+STlll],3354,ROOT.kBlack,True]]

    
        BackgroundSamples_list=[BackgroundSamples[BackgroundSampleNames.index('QCDMadgraph')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_tW')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_t')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_s')]]
     
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison',listOflll,False,'',True,False,True,False)
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison_log',listOflll,True,'',True,False,True,False)
        
    elif ABCDversion in plotname:

        BackgroundLOL=transposeLOL([[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ttbar')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_tW')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_t')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_s')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]])
        SignalLOL=[[lllSignal[plotnames.index(plotname)][SignalSampleNames.index('Zprimeall')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]]
    
        QCDlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_nominal")]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_MCSF_CSVLFUp"):allweightsystnames.index("_" + ABCDversion + "_MCSF_renfac_envDown")])[BackgroundSampleNames.index('QCDMadgraph')]]

        ttbarlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_nominal")]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_MCSF_CSVLFUp"):allweightsystnames.index("_" + ABCDversion + "_ttbarXSDown")])[BackgroundSampleNames.index('ttbar')]]

        STlll=transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_nominal")]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_MCSF_CSVLFUp"):allweightsystnames.index("_" + ABCDversion + "_ttbarXSDown")])[BackgroundSampleNames.index('ST_tW'):BackgroundSampleNames.index('ST_s')+1]

        listOflll=[[[QCDlll+ttbarlll+STlll],3354,ROOT.kBlack,True]]

    
        BackgroundSamples_list=[BackgroundSamples[BackgroundSampleNames.index('QCDMadgraph')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_tW')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_t')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_s')]]
     
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison',listOflll,False,'',True,False,True,False)
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison_log',listOflll,True,'',True,False,True,False)
                
    else:
        
        BackgroundLOL=transposeLOL([[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')][allweightsystnames.index('_Nobtagging_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ttbar')][allweightsystnames.index('_Nobtagging_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_tW')][allweightsystnames.index('_Nobtagging_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_t')][allweightsystnames.index('_Nobtagging_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_s')][allweightsystnames.index('_Nobtagging_nominal')]]])
        SignalLOL=[[lllSignal[plotnames.index(plotname)][SignalSampleNames.index('Zprimeall')][allweightsystnames.index('_Nobtagging_nominal')]]]
    
        QCDlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_MCSF_PUUp'):allweightsystnames.index('_Nobtagging_MCSF_renfac_envDown')])[BackgroundSampleNames.index('QCDMadgraph')]]

        ttbarlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_MCSF_PUUp'):allweightsystnames.index('_Nobtagging_ttbarXSDown')])[BackgroundSampleNames.index('ttbar')]]

        STlll=transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_MCSF_PUUp'):allweightsystnames.index('_Nobtagging_ttbarXSDown')])[BackgroundSampleNames.index('ST_tW'):BackgroundSampleNames.index('ST_s')+1]

        listOflll=[[[QCDlll+ttbarlll+STlll],3354,ROOT.kBlack,True]]
    
        BackgroundSamples_list=[BackgroundSamples[BackgroundSampleNames.index('QCDMadgraph')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_tW')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_t')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_s')]]
     
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison',listOflll,False,'',True,False,True,False)
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison_log',listOflll,True,'',True,False,True,False)


avgscale=0
    
for plotname in plotnames:
    
    if plotname=="N_BTagsM":
    #print lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')]
    #print lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')][allweightsystnames.index('_'+ABCDversion+'_nominal')]
    #print lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ttbar')][allweightsystnames.index('_'+ABCDversion+'_nominal')]
    
    #print listOfHistoListsData[plotnames.index(plotname)][0]
        scale=(listOfHistoListsData[plotnames.index(plotname)][0].Integral()-lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ttbar')][allweightsystnames.index('_All_nominal')].Integral())/(lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')][allweightsystnames.index('_All_nominal')]).Integral()
        print plotname, "QCD-multijet DATA/MC scale=",scale
        avgscale=avgscale+scale
        for h in lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')]:
            h.Scale(scale)
        
    
        BackgroundLOL=transposeLOL([[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')][allweightsystnames.index('_All_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ttbar')][allweightsystnames.index('_All_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_tW')][allweightsystnames.index('_All_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_t')][allweightsystnames.index('_All_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_s')][allweightsystnames.index('_All_nominal')]]])
        SignalLOL=[[lllSignal[plotnames.index(plotname)][SignalSampleNames.index('Zprimeall')][allweightsystnames.index('_All_nominal')]]]
    
        QCDlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_MCSF_CSVLFUp'):allweightsystnames.index('_All_MCSF_renfac_envDown')])[BackgroundSampleNames.index('QCDMadgraph')]]

        ttbarlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_MCSF_CSVLFUp'):allweightsystnames.index('_All_ttbarXSDown')])[BackgroundSampleNames.index('ttbar')]]

        STlll=transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_All_MCSF_CSVLFUp'):allweightsystnames.index('_All_ttbarXSDown')])[BackgroundSampleNames.index('ST_tW'):BackgroundSampleNames.index('ST_s')+1]

        listOflll=[[[QCDlll+ttbarlll+STlll],3354,ROOT.kBlack,True]]
    
        BackgroundSamples_list=[BackgroundSamples[BackgroundSampleNames.index('QCDMadgraph')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_tW')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_t')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_s')]]
     
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison_QCDrenorm',listOflll,False,'',True,False,True,False)
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison_QCDrenorm_log',listOflll,True,'',True,False,True,False)
        
    elif ABCDversion in plotname:
        scale=(listOfHistoListsData[plotnames.index(plotname)][0].Integral()-lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ttbar')][allweightsystnames.index("_" + ABCDversion + "_nominal")].Integral()-lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_tW')][allweightsystnames.index("_" + ABCDversion + "_nominal")].Integral()-lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_t')][allweightsystnames.index("_" + ABCDversion + "_nominal")].Integral()-lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_s')][allweightsystnames.index("_" + ABCDversion + "_nominal")].Integral())/(lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')][allweightsystnames.index("_" + ABCDversion + "_nominal")]).Integral()
        print plotname, "QCD-multijet DATA/MC scale=",scale
        avgscale=avgscale+scale
        for h in lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')]:
            h.Scale(scale)
        
    
        BackgroundLOL=transposeLOL([[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ttbar')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_tW')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_t')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_s')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]])
        SignalLOL=[[lllSignal[plotnames.index(plotname)][SignalSampleNames.index('Zprimeall')][allweightsystnames.index("_" + ABCDversion + "_nominal")]]]
    
        QCDlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_nominal")]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_MCSF_CSVLFUp"):allweightsystnames.index("_" + ABCDversion + "_MCSF_renfac_envDown")])[BackgroundSampleNames.index('QCDMadgraph')]]

        ttbarlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_nominal")]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_MCSF_CSVLFUp"):allweightsystnames.index("_" + ABCDversion + "_ttbarXSDown")])[BackgroundSampleNames.index('ttbar')]]

        STlll=transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_nominal")]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index("_" + ABCDversion + "_MCSF_CSVLFUp"):allweightsystnames.index("_" + ABCDversion + "_ttbarXSDown")])[BackgroundSampleNames.index('ST_tW'):BackgroundSampleNames.index('ST_s')+1]

        listOflll=[[[QCDlll+ttbarlll+STlll],3354,ROOT.kBlack,True]]
    
        BackgroundSamples_list=[BackgroundSamples[BackgroundSampleNames.index('QCDMadgraph')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_tW')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_t')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_s')]]
     
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison_QCDrenorm',listOflll,False,'',True,False,True,False)
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison_QCDrenorm_log',listOflll,True,'',True,False,True,False)
        

    else:
        scale=(listOfHistoListsData[plotnames.index(plotname)][0].Integral()-lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ttbar')][allweightsystnames.index('_Nobtagging_nominal')].Integral()-lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_tW')][allweightsystnames.index('_Nobtagging_nominal')].Integral()-lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_t')][allweightsystnames.index('_Nobtagging_nominal')].Integral()-lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_s')][allweightsystnames.index('_Nobtagging_nominal')].Integral())/(lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')][allweightsystnames.index('_Nobtagging_nominal')]).Integral()
        print plotname, "QCD-multijet DATA/MC scale=",scale
        avgscale=avgscale+scale
        for h in lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')]:
            h.Scale(scale)
                
        BackgroundLOL=transposeLOL([[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('QCDMadgraph')][allweightsystnames.index('_Nobtagging_nominal')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ttbar')][allweightsystnames.index('')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_tW')][allweightsystnames.index('')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_t')][allweightsystnames.index('')]]]+[[lllBackground[plotnames.index(plotname)][BackgroundSampleNames.index('ST_s')][allweightsystnames.index('')]]])
        SignalLOL=[[lllSignal[plotnames.index(plotname)][SignalSampleNames.index('Zprimeall')][allweightsystnames.index('_Nobtagging_nominal')]]]
    
        QCDlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_MCSF_PUUp'):allweightsystnames.index('_Nobtagging_MCSF_renfac_envDown')])[BackgroundSampleNames.index('QCDMadgraph')]]

        ttbarlll=[transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_MCSF_PUUp'):allweightsystnames.index('_Nobtagging_ttbarXSDown')])[BackgroundSampleNames.index('ttbar')]]

        STlll=transposeLOL([transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_nominal')]]+transposeLOL(lllBackground[plotnames.index(plotname)])[allweightsystnames.index('_Nobtagging_MCSF_PUUp'):allweightsystnames.index('_Nobtagging_ttbarXSDown')])[BackgroundSampleNames.index('ST_tW'):BackgroundSampleNames.index('ST_s')+1]

        listOflll=[[[QCDlll+ttbarlll+STlll],3354,ROOT.kBlack,True]]
    
        BackgroundSamples_list=[BackgroundSamples[BackgroundSampleNames.index('QCDMadgraph')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_tW')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_t')]]+[BackgroundSamples[BackgroundSampleNames.index('ST_s')]]
     
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison_QCDrenorm',listOflll,False,'',True,False,True,False)
        plotDataMCanWsyst([listOfHistoListsData[plotnames.index(plotname)]],BackgroundLOL,BackgroundSamples_list,SignalLOL[0],SignalSamples[0],1.0,'DATA_MC_comparison_QCDrenorm_log',listOflll,True,'',True,False,True,False)

avgscale=avgscale/len(plots)
print avgscale