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

name='Zprime_efficiencies'+'_'+ABCDversion+radi+'_'+WPs

#if doBR:
    #name=name+'_'+BR_name
verybasicplotselection="Evt_HT_Jets>1000"



plots=[

    #Plot(ROOT.TH1F( ABCDversion + "_2AK8_nopt_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (packedPatJetsAK8PFCHSSoftDrop_Pt[0]>150 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>150)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ))" , ""),
    #Plot(ROOT.TH1F( ABCDversion + "_2AK8_nopt_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " packedPatJetsAK8PFCHSSoftDrop_Pt[0]>150 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>150 " + " && " + "Triggered_HLT_PFHT800_vX==1", ""),

    #Plot(ROOT.TH1F( ABCDversion + "_2AK8_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 " + " && " + "(Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 )", ""),
    #Plot(ROOT.TH1F( ABCDversion + "_2AK8_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " packedPatJetsAK8PFCHSSoftDrop_Pt[0]>400 && packedPatJetsAK8PFCHSSoftDrop_Pt[1]>200 " + " && " + "Triggered_HLT_PFHT800_vX==1", ""),

    #Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 )", ""),
    #Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " Triggered_HLT_PFHT800_vX==1", ""),

    #Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "  Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + "(Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 )", ""),
    #Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "  Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + "Triggered_HLT_PFHT800_vX==1", ""),
    
    #Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " Zprimes_ABCD"+radi+"_M>1000 " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + "(Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 )", ""),
    #Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " Zprimes_ABCD"+radi+"_M>1000 " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + "Triggered_HLT_PFHT800_vX==1", ""),
    
    #Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " Zprimes_ABCD"+radi+"_M>1000 " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + "(Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 )", ""),
    #Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " Zprimes_ABCD"+radi+"_M>1000 " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + "Triggered_HLT_PFHT800_vX==1", ""),  
   
    #Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " Zprimes_ABCD"+radi+"_M>1000 " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + " && " + "(Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 )" + " && " + "Triggered_HLT_PFHT800_vX==1", ""),
    #Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " Zprimes_ABCD"+radi+"_M>1000 " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + " && " + "Triggered_HLT_PFHT800_vX==1", ""),
  
    #Plot(ROOT.TH1F( ABCDversion + "_CatA_withtobbtag_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " Zprimes_ABCD"+radi+"_M>1000 " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + "(Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 )", ""),
    #Plot(ROOT.TH1F( ABCDversion + "_CatA_withtobbtag_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " Zprimes_ABCD"+radi+"_M>1000 " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_TprimeMass + " && " + "Triggered_HLT_PFHT800_vX==1", ""),


    #Plot(ROOT.TH1F( ABCDversion + "_2AK8_nopt_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (packedPatJetsAK8PF" + radi + "_Pt[0]>150 && packedPatJetsAK8PF" + radi + "_Pt[1]>150)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ))" , ""),
    #Plot(ROOT.TH1F( ABCDversion + "_2AK8_nopt_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (packedPatJetsAK8PF" + radi + "_Pt[0]>150 && packedPatJetsAK8PF" + radi + "_Pt[1]>150)*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),

    #Plot(ROOT.TH1F( ABCDversion + "_2AK8_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (packedPatJetsAK8PF" + radi + "_Pt[0]>400 && packedPatJetsAK8PF" + radi + "_Pt[1]>200)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ))", ""),
    #Plot(ROOT.TH1F( ABCDversion + "_2AK8_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (packedPatJetsAK8PF" + radi + "_Pt[0]>400 && packedPatJetsAK8PF" + radi + "_Pt[1]>200)*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),

    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " ((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),

    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " ( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " ( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),  
   
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),
  
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (Evt_HT_Jets>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.2*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(Evt_HT_Jets>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.2*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),
    
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Triggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " ((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Nontriggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " ((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),

    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Triggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " ( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Nontriggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " ( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Triggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Nontriggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Triggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Nontriggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),  
   
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Triggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Nontriggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),
  
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Triggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered_2" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),
    
    
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Triggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " ((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Nontriggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),

    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Triggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " ( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Nontriggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " ( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Triggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Nontriggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Triggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Nontriggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),  
   
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Triggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Nontriggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),
  
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Triggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (Evt_HT_Jets>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.2*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered_3" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", "(Evt_HT_Jets>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.2*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),
    
    #Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Triggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (Evt_HT_Jets>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.2*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ))", ""),
    #Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered" ,"H_{T} in GeV" ,40,0,2000),"Evt_HT_Jets", " (Evt_HT_Jets>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.2*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),



    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Triggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Nontriggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),

    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Triggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Nontriggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Triggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Nontriggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Triggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Nontriggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),  
   
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Triggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Nontriggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),
  
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Triggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*(Evt_HT_Jets>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.2*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(Evt_HT_Jets>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.2*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*(Triggered_HLT_PFHT800_vX==1)*Prescale_HLT_PFHT800_vX", ""),
    
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Triggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Nontriggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),

    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Triggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Nontriggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Triggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Nontriggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Triggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Nontriggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),  
   
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Triggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Nontriggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),
  
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Triggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*(Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && (Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))*Prescale_HLT_PFHT800_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered_2_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(Evt_HT_Jets>(0.75*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.25*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_IsoMu24_vX==1 || Triggered_HLT_IsoTkMu24_vX==1))", ""),
    
    
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Triggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_nopt_Nontriggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),

    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Triggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbcandidates_Nontriggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*( Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Triggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_nopt_Nontriggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + ")*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),
    
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Triggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_Nontriggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100)*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),  
   
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Triggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_withtobbtag_Nontriggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(" + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),
  
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Triggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", " (Evt_HT_Jets>1000)*(Evt_HT_Jets>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.2*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*((Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFJet450_vX==1 ) && Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX*Prescale_HLT_PFHT900_vX", ""),
    Plot(ROOT.TH1F( ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered_3_mZp" ,"m(Z') in GeV" ,40,0,4000),"Zprimes_ABCD"+radi+"_M", "(Evt_HT_Jets>1000)*(Evt_HT_Jets>(0.8*Zprimes_ABCD" +  radi + "_M) && Evt_HT_Jets<(1.2*Zprimes_ABCD" +  radi + "_M) " + " && " + plotselection_W_MSD + " && " +plotselection_W_tau21 + " && " + plotselection_t_MSD + " && " + plotselection_tau32 + " && " + " Tops_ABCD"+radi+"_Pt>400" + " && " + " Ws_ABCD"+radi+"_Pt>200" + " && " + " Bottoms_ABCD"+radi+"_Pt>100" + " && " + plotselection_topsubjetCSVv2 + ")*(Triggered_HLT_PFHT650_vX==1)*Prescale_HLT_PFHT650_vX", ""),
    



]





plotnames=[]
for i in plots:
    plotnames.append(i.name)

OnlyFirstList=len(plots)*[False]
#OnlyFirstList[plotnames.index("ABCD1_notopbtag_CatA_Zprime_M"):plotnames.index('ABCD2_inclusive_CatH_Tprime_M') +1 ] = len(OnlyFirstList[plotnames.index("ABCD1_notopbtag_CatA_Zprime_M"):plotnames.index('ABCD2_inclusive_CatH_Tprime_M') + 1 ] ) * [True]
#OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Bottom_Pt"):plotnames.index(ABCDversion + "_withtopbtag_CatA_HTtWb") +1 ] = len(OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Bottom_Pt"):plotnames.index(ABCDversion + "_withtopbtag_CatA_HTtWb") + 1 ] ) * [True]
OnlyFirstList[plotnames.index(ABCDversion + "_tWbcandidates_nopt_Triggered"):plotnames.index(ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered_3_mZp") +1 ] = len(OnlyFirstList[plotnames.index(ABCDversion + "_tWbcandidates_nopt_Triggered"):plotnames.index(ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered_3_mZp") + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'



#print allweightsystnames
#print allsystweights

#print name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM,systweightsbasic+systweightsMadgraphbantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weightsystnamesPythia8bantiZprimeM,systweightsPythia8bantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
#print allweightsystnames
#print allsystweights, "OK"
#raw_input()

#outputpath=plotParallel(name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples+systsamples,[""],["1"],allweightsystnames,allsystweights,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList,otherSystNames)
outputpath=plotParallel(name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples, [''], ['1'] , [''], ['1'],additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList,)

# plot dataMC comparison
listOfHistoLists_Signal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples,plots,1)
listOfHistoLists_Background=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples,plots,1)

addLOLtoLOL(transposeLOL([transposeLOL(listOfHistoLists_Background)[BackgroundSampleNames.index('ttbar')]]),transposeLOL([transposeLOL(listOfHistoLists_Background)[BackgroundSampleNames.index('ST_tW')]]))
addLOLtoLOL(transposeLOL([transposeLOL(listOfHistoLists_Background)[BackgroundSampleNames.index('ttbar')]]),transposeLOL([transposeLOL(listOfHistoLists_Background)[BackgroundSampleNames.index('ST_t')]]))
addLOLtoLOL(transposeLOL([transposeLOL(listOfHistoLists_Background)[BackgroundSampleNames.index('ttbar')]]),transposeLOL([transposeLOL(listOfHistoLists_Background)[BackgroundSampleNames.index('ST_s')]]))


listOfHistoLists_Background=transposeLOL([transposeLOL(listOfHistoLists_Background)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoLists_Background)[BackgroundSampleNames.index('QCDMadgraph')]])
BackgroundSamples=[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[BackgroundSamples[BackgroundSampleNames.index('QCDMadgraph')]]
BackgroundSampleNames=[BackgroundSampleNames[BackgroundSampleNames.index('ttbar')]]+[BackgroundSampleNames[BackgroundSampleNames.index('QCDMadgraph')]]
#listOfHistoLists_Signal=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)


#rebinnedHistosExist=False
#rebinnedHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned.root'
#rebinnedandaddedHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_added.root'
#rebinnedandaddedBRHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_added_'+BR_name+'.root'


#allweightsystnames=allweightsystnames+JECsystnames
#print allweightsystnames

##print 'debug filesave 1 ', rebinnedHistoPath[:-5]
##print 'debug filesave 2 ', rebinnedandaddedHistoPath[:-5]
##print 'debug filesave 3 ', rebinnedandaddedBRHistoPath[:-5]


#lllSignal=createLLL_fromSuperHistoFileSyst(outputpath,SignalSamples,plots,allweightsystnames)
#lllBackground=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,allweightsystnames)
##lllData=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,allweightsystnames)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,DataSamples,plots,1)

#print Datalll

DataLoL=[]

#numeratorindexlist=[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Triggered"),plotnames.index(ABCDversion + "_tWbcandidates_Triggered"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Triggered"),plotnames.index(ABCDversion + "_tWbtagged_Triggered"),plotnames.index(ABCDversion + "_tWbtagged_withtobbtag_Triggered"),plotnames.index(ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Triggered")]+[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Triggered_2"),plotnames.index(ABCDversion + "_tWbcandidates_Triggered_2"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Triggered_2"),plotnames.index(ABCDversion + "_tWbtagged_Triggered_2"),plotnames.index(ABCDversion + "_tWbtagged_withtobbtag_Triggered_2"),plotnames.index(ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Triggered_2")]+[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Triggered_3"),plotnames.index(ABCDversion + "_tWbcandidates_Triggered_3"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Triggered_3"),plotnames.index(ABCDversion + "_tWbtagged_Triggered_3"),plotnames.index(ABCDversion + "_tWbtagged_withtobbtag_Triggered_3"),plotnames.index(ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Triggered_3")]

#denumeratorindexlist=[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Nontriggered"),plotnames.index(ABCDversion + "_tWbcandidates_Nontriggered"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Nontriggered"),plotnames.index(ABCDversion + "_tWbtagged_Nontriggered"),plotnames.index(ABCDversion + "_tWbtagged_withtobbtag_Nontriggered"),plotnames.index(ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered")]+[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Nontriggered_2"),plotnames.index(ABCDversion + "_tWbcandidates_Nontriggered_2"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Nontriggered_2"),plotnames.index(ABCDversion + "_tWbtagged_Nontriggered_2"),plotnames.index(ABCDversion + "_tWbtagged_withtobbtag_Nontriggered_2"),plotnames.index(ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered_2")]+[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Nontriggered_3"),plotnames.index(ABCDversion + "_tWbcandidates_Nontriggered_3"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Nontriggered_3"),plotnames.index(ABCDversion + "_tWbtagged_Nontriggered_3"),plotnames.index(ABCDversion + "_tWbtagged_withtobbtag_Nontriggered_3"),plotnames.index(ABCDversion + "_tWbtagged_EvtHT_withtobbtag_Nontriggered_3")]





numeratorindexlist=[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Triggered_2"),plotnames.index(ABCDversion + "_tWbcandidates_Triggered_2"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Triggered_2"),plotnames.index(ABCDversion + "_tWbtagged_Triggered_2")]+[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Triggered_3"),plotnames.index(ABCDversion + "_tWbcandidates_Triggered_3"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Triggered_3"),plotnames.index(ABCDversion + "_tWbtagged_Triggered_3")]

denumeratorindexlist=[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Nontriggered_2"),plotnames.index(ABCDversion + "_tWbcandidates_Nontriggered_2"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Nontriggered_2"),plotnames.index(ABCDversion + "_tWbtagged_Nontriggered_2")]+[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Nontriggered_3"),plotnames.index(ABCDversion + "_tWbcandidates_Nontriggered_3"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Nontriggered_3"),plotnames.index(ABCDversion + "_tWbtagged_Nontriggered_3")]

print listOfHistoLists_Signal
print SignalSamples
print SignalSampleNames
raw_input()

print listOfHistoLists_Background
print BackgroundSamples
print BackgroundSampleNames
raw_input()

print listOfHistoListsData
print DataSamples
print DataSampleNames
raw_input()


writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoLists_Signal)[SignalSampleNames.index('Zprimeall')]]+[transposeLOL(listOfHistoLists_Background)[BackgroundSampleNames.index('QCDMadgraph')]]+[transposeLOL(listOfHistoLists_Background)[BackgroundSampleNames.index('ttbar')]]+[transposeLOL(listOfHistoListsData)[DataSampleNames.index('DATA_2016')]])[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Triggered_2"):plotnames.index(ABCDversion + "_tWbtagged_Triggered_3")+1],[SignalSamples[SignalSampleNames.index('Zprimeall')]]+[BackgroundSamples[BackgroundSampleNames.index('QCDMadgraph')]]+[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+[DataSamples[DataSampleNames.index('DATA_2016')]], "","test2",True,False,False,'histoE')


effLOL_Data=efficiencies(listOfHistoListsData,BackgroundSamples+DataSamples,numeratorindexlist, denumeratorindexlist,name)

effLOL_background=efficiencies(listOfHistoLists_Background,BackgroundSamples+DataSamples,numeratorindexlist,denumeratorindexlist ,name)
effLOL_signal=efficiencies(listOfHistoLists_Signal,SignalSamples+BackgroundSamples+DataSamples,numeratorindexlist,denumeratorindexlist ,name)


writeListOfHistoLists(transposeLOL(transposeLOL(effLOL_signal)+transposeLOL(effLOL_background)+transposeLOL(effLOL_Data)),SignalSamples+BackgroundSamples+DataSamples, "","test3",False,False,False,'histoE')

writeHistoListwithXYErrors(transposeLOL(transposeLOL(effLOL_Data)), DataSamples, 'test', 1, '0.5*[0]*erf((x-[2])/[1])+0.5')
#writeHistoListwithXYErrors(transposeLOL(transposeLOL(effLOL_background)), BackgroundSamples, 'test', 1, '0.5*[0]*erf((x-[2])/[1])+0.5')
#writeHistoListwithXYErrors(transposeLOL(transposeLOL(effLOL_signal)), SignalSamples, 'test', 1, '0.5*[0]*erf((x-[2])/[1])+0.5')



###############again for mZp################


numeratorindexlist=[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Triggered_2_mZp"),plotnames.index(ABCDversion + "_tWbcandidates_Triggered_2_mZp"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Triggered_2_mZp"),plotnames.index(ABCDversion + "_tWbtagged_Triggered_2_mZp")]+[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Triggered_3_mZp"),plotnames.index(ABCDversion + "_tWbcandidates_Triggered_3_mZp"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Triggered_3_mZp"),plotnames.index(ABCDversion + "_tWbtagged_Triggered_3_mZp")]

denumeratorindexlist=[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Nontriggered_2_mZp"),plotnames.index(ABCDversion + "_tWbcandidates_Nontriggered_2_mZp"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Nontriggered_2_mZp"),plotnames.index(ABCDversion + "_tWbtagged_Nontriggered_2_mZp")]+[plotnames.index( ABCDversion + "_tWbcandidates_nopt_Nontriggered_3_mZp"),plotnames.index(ABCDversion + "_tWbcandidates_Nontriggered_3_mZp"),plotnames.index(ABCDversion + "_tWbtagged_nopt_Nontriggered_3_mZp"),plotnames.index(ABCDversion + "_tWbtagged_Nontriggered_3_mZp")]


effLOL_Data=efficiencies(listOfHistoListsData,BackgroundSamples+DataSamples,numeratorindexlist, denumeratorindexlist,name)

effLOL_background=efficiencies(listOfHistoLists_Background,BackgroundSamples+DataSamples,numeratorindexlist,denumeratorindexlist ,name)
effLOL_signal=efficiencies(listOfHistoLists_Signal,SignalSamples+BackgroundSamples+DataSamples,numeratorindexlist,denumeratorindexlist ,name)

writeListOfHistoLists(transposeLOL(transposeLOL(effLOL_signal)+transposeLOL(effLOL_background)+transposeLOL(effLOL_Data)),SignalSamples+BackgroundSamples+DataSamples, "","test3",False,False,False,'histoE')


writeHistoListwithXYErrors(transposeLOL(transposeLOL(effLOL_Data)), DataSamples, 'test', 1, '0.5*[0]*erf((x-[2])/[1])+0.5')
#writeHistoListwithXYErrors(transposeLOL(transposeLOL(effLOL_background)), BackgroundSamples, 'test', 1, '0.5*[0]*erf((x-[2])/[1])+0.5')
#writeHistoListwithXYErrors(transposeLOL(transposeLOL(effLOL_signal)), SignalSamples, 'test', 1, '0.5*[0]*erf((x-[2])/[1])+0.5')


