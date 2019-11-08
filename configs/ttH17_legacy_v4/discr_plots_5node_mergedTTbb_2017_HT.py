
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import ROOT
from array import array
from copy import deepcopy


memexp = ""


def plots_ge4j_3t(data = None):
    ndefaultbins = 50
    category_dict = {}
    this_dict = {}

    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    # plots = [
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_avg","average b-tag value",50,0.1,0.9),"Evt_CSV_avg",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_dev","average deviation of b-tag value",50,0.0,0.24),"Evt_CSV_dev",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",50,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_min","minimal b-tag value",50,0.0,1.0),"Evt_CSV_min",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",50,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",50,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
    #     plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_HT","H_{T}",50,200.0,1700.0),"Evt_HT",selection,label),
        
    #     plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_HT_jets","H_{T}(jets)",50,200.0,1500.0),"Evt_HT_jets",selection,label),
    #     plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_HT_wo_MET","H_{T} without MET",50,200.0,1500.0),"Evt_HT_wo_MET",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",50,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_sphericity_jets","sphericity of jets",50,0.0,1.0),"Evt_sphericity_jets",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_transverse_sphericity_jets","transverse sphericity of jets",50,0.00177236890886,0.999349296093),"Evt_transverse_sphericity_jets",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_N_BTagsT","number of b-tags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",20,0.0,1.0),"Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
    #     # # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1 ","Reco_JABDT_ttbar_Jet_CSV_whaddau1 ",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1 ",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_log_toplep_pt","Reco_JABDT_ttbar_log_toplep_pt",50,0.0,10.0),"Reco_JABDT_ttbar_log_toplep_pt",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_h_eta","Reco_ttH_h_eta",50,-4.0,-4.0),"Reco_ttH_h_eta",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_h_phi","Reco_ttH_h_phi",50,-4.0,4.0),"Reco_ttH_h_phi",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_tophad_m","Reco_ttH_tophad_m",50,0.0,800.0),"Reco_ttH_tophad_m",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_tophad_pt","Reco_ttH_tophad_pt",50,0.0,800.0),"Reco_ttH_tophad_pt",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_whad_dr","Reco_ttH_whad_dr",50,0.0,4.0),"Reco_ttH_whad_dr",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_whaddau_m2","Reco_ttH_whaddau_m2",50,0.0,50.0),"Reco_ttH_whaddau_m2",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttbar_btophad_eta","Reco_ttbar_btophad_eta",50,-4.0,4.0),"Reco_ttbar_btophad_eta",selection,label),
    #     ]
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.))","ljets_ge4j_3t_Evt_HT","")
    category_dict["varname"] = "Evt_HT"
    category_dict["catlabel"] = label
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [200.0,230.0,260.0,290.0,320.0,350.0,380.0,410.0,440.0,470.0,500.0,530.0,560.0,590.0,620.0,650.0,680.0,710.0,740.0,770.0,800.0,830.0,860.0,890.0,920.0,950.0,980.0,1010.0,1040.0,1070.0,1100.0,1130.0,1160.0,1190.0,1220.0,1250.0,1280.0,1310.0,1340.0,1370.0,1400.0,1430.0,1460.0,1490.0,1520.0,1550.0,1580.0,1610.0,1640.0,1670.0,1700.0]
    category_dict["histoname"] = "ljets_ge4j_3t_Evt_HT"
    category_dict["histotitle"] = "H_{T}"
    category_dict["plotPreselections"] = category_dict["category"][0]

    this_dict["ljets_ge4j_3t_Evt_HT"] = deepcopy(category_dict)
    category_dict.clear()

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.))","ljets_ge4j_3t_Evt_HT_jets","")
    category_dict["varname"] = "Evt_HT_jets"
    category_dict["catlabel"] = label
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [200.0,226.0,252.0,278.0,304.0,330.0,356.0,382.0,408.0,434.0,460.0,486.0,512.0,538.0,564.0,590.0,616.0,642.0,668.0,694.0,720.0,746.0,772.0,798.0,824.0,850.0,876.0,902.0,928.0,954.0,980.0,1006.0,1032.0,1058.0,1084.0,1110.0,1136.0,1162.0,1188.0,1214.0,1240.0,1266.0,1292.0,1318.0,1344.0,1370.0,1396.0,1422.0,1448.0,1474.0,1500.0]
    category_dict["histoname"] = "ljets_ge4j_3t_Evt_HT_jets"
    category_dict["histotitle"] = "H_{T}(jets)"
    category_dict["plotPreselections"] = category_dict["category"][0]

    this_dict["ljets_ge4j_3t_Evt_HT_jets"] = deepcopy(category_dict)
    category_dict.clear()

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.))","ljets_ge4j_3t_Evt_HT_wo_MET","")
    category_dict["varname"] = "Evt_HT_wo_MET"
    category_dict["catlabel"] = label
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [200.0,226.0,252.0,278.0,304.0,330.0,356.0,382.0,408.0,434.0,460.0,486.0,512.0,538.0,564.0,590.0,616.0,642.0,668.0,694.0,720.0,746.0,772.0,798.0,824.0,850.0,876.0,902.0,928.0,954.0,980.0,1006.0,1032.0,1058.0,1084.0,1110.0,1136.0,1162.0,1188.0,1214.0,1240.0,1266.0,1292.0,1318.0,1344.0,1370.0,1396.0,1422.0,1448.0,1474.0,1500.0]
    category_dict["histoname"] = "ljets_ge4j_3t_Evt_HT_wo_MET"
    category_dict["histotitle"] = "H_{T} without MET"
    category_dict["plotPreselections"] = category_dict["category"][0]
    
    this_dict["ljets_ge4j_3t_Evt_HT_wo_MET"] = deepcopy(category_dict)
    category_dict.clear()
    
    plots = init_plots(dictionary = this_dict)
    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_ge4j_ge4t(data = None):
    ndefaultbins = 50
    category_dict = {}
    this_dict = {}


    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    # plots = [
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_CSV_3","fourth highest b-tag value",50,0.0,1.0),"CSV[3]",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_avg","average b-tag value",50,0.1,0.9),"Evt_CSV_avg",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_dev","average deviation of b-tag value",50,0.0,0.24),"Evt_CSV_dev",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_min","minimal b-tag value",50,0.0,1.0),"Evt_CSV_min",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",50,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
    #     plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_HT","H_{T}",50,200.0,1700.0),"Evt_HT",selection,label),
    #     plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_HT_jets","H_{T}(jets)",50,200.0,1500.0),"Evt_HT_jets",selection,label),
    #     plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_HT_wo_MET","H_{T} without MET",50,200.0,1500.0),"Evt_HT_wo_MET",selection,label),        
        
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",50,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_sphericity_jets","sphericity of jets",50,0.0,1.0),"Evt_sphericity_jets",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_transverse_sphericity_jets","transverse sphericity of jets",50,0.00177236890886,0.999349296093),"Evt_transverse_sphericity_jets",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_N_BTagsT","number of b-tags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",20,0.0,1.0),"Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
    #     # # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1 ","Reco_JABDT_ttbar_Jet_CSV_whaddau1 ",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1 ",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttbar_log_toplep_pt","Reco_JABDT_ttbar_log_toplep_pt",50,0.0,10.0),"Reco_JABDT_ttbar_log_toplep_pt",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_h_eta","Reco_ttH_h_eta",50,-4.0,-4.0),"Reco_ttH_h_eta",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_h_phi","Reco_ttH_h_phi",50,-4.0,4.0),"Reco_ttH_h_phi",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_tophad_m","Reco_ttH_tophad_m",50,0.0,800.0),"Reco_ttH_tophad_m",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_tophad_pt","Reco_ttH_tophad_pt",50,0.0,800.0),"Reco_ttH_tophad_pt",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_whad_dr","Reco_ttH_whad_dr",50,0.0,4.0),"Reco_ttH_whad_dr",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_whaddau_m2","Reco_ttH_whaddau_m2",50,0.0,50.0),"Reco_ttH_whaddau_m2",selection,label),
    #     # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttbar_btophad_eta","Reco_ttbar_btophad_eta",50,-4.0,4.0),"Reco_ttbar_btophad_eta",selection,label),
    #     ]

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.))","ljets_ge4j_ge4t_Evt_HT","")
    category_dict["varname"] = "Evt_HT"
    category_dict["catlabel"] = label
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [200.0,260.0,290.0,320.0,350.0,380.0,410.0,440.0,470.0,500.0,530.0,560.0,590.0,620.0,650.0,680.0,710.0,740.0,770.0,800.0,830.0,860.0,890.0,920.0,950.0,980.0,1010.0,1040.0,1070.0,1100.0,1130.0,1160.0,1190.0,1220.0,1250.0,1280.0,1310.0,1340.0,1370.0,1400.0,1460.0,1520.0,1580.0,1670.0,1700.0]
    category_dict["histoname"] = "ljets_ge4j_ge4t_Evt_HT"
    category_dict["histotitle"] = "H_{T}"
    category_dict["plotPreselections"] = category_dict["category"][0]
    
    this_dict["ljets_ge4j_ge4t_Evt_HT"] = deepcopy(category_dict)
    category_dict.clear()

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.))","ljets_ge4j_ge4t_Evt_HT_jets","")
    category_dict["varname"] = "Evt_HT_jets"
    category_dict["catlabel"] = label
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [200.0,226.0,252.0,278.0,304.0,330.0,356.0,382.0,408.0,434.0,460.0,486.0,512.0,538.0,564.0,590.0,616.0,642.0,668.0,694.0,720.0,746.0,772.0,798.0,824.0,850.0,876.0,902.0,928.0,954.0,980.0,1006.0,1032.0,1058.0,1084.0,1110.0,1162.0,1188.0,1240.0,1292.0,1344.0,1396.0,1474.0,1500.0]
    category_dict["histoname"] = "ljets_ge4j_ge4t_Evt_HT_jets"
    category_dict["histotitle"] = "H_{T}(jets)"
    category_dict["plotPreselections"] = category_dict["category"][0]

    this_dict["ljets_ge4j_ge4t_Evt_HT_jets"] = deepcopy(category_dict)
    category_dict.clear()

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.))","ljets_ge4j_ge4t_Evt_HT_wo_MET","")
    category_dict["varname"] = "Evt_HT_wo_MET"
    category_dict["catlabel"] = label
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [200.0,226.0,252.0,278.0,304.0,330.0,356.0,382.0,408.0,434.0,460.0,486.0,512.0,538.0,564.0,590.0,616.0,642.0,668.0,694.0,720.0,746.0,772.0,798.0,824.0,850.0,876.0,902.0,928.0,954.0,980.0,1006.0,1032.0,1058.0,1084.0,1110.0,1136.0,1162.0,1188.0,1214.0,1240.0,1292.0,1318.0,1370.0,1422.0,1474.0,1500.0]
    category_dict["histoname"] = "ljets_ge4j_ge4t_Evt_HT_wo_MET"
    category_dict["histotitle"] = "H_{T} without MET"
    category_dict["plotPreselections"] = category_dict["category"][0]

    this_dict["ljets_ge4j_ge4t_Evt_HT_wo_MET"] = deepcopy(category_dict)
    category_dict.clear()

    plots = init_plots(dictionary = this_dict)

    if data:
        add_data_plots(plots=plots,data=data)
    return plots




def plots_dnn(data, discrname):

    ndefaultbins = 15
    category_dict = {}
    this_dict = {}




    # plots for ge4j_3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttH_node","")
    category_dict["varname"] = "DNNOutput_ge4j_3t_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.8

    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttb_bb_node","")
    category_dict["varname"] = "DNNOutput_ge4j_3t_node_ttb_bb"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.64

    this_dict["ljets_ge4j_3t_ttb_bb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tt2b_node","")
    category_dict["varname"] = "DNNOutput_ge4j_3t_node_tt2b"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.78

    this_dict["ljets_ge4j_3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttcc_node","")
    category_dict["varname"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.44

    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttlf_node","")
    category_dict["varname"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.73

    this_dict["ljets_ge4j_3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttH_node","")
    category_dict["varname"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.76

    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttb_bb_node","")
    category_dict["varname"] = "DNNOutput_ge4j_ge4t_node_ttb_bb"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.74

    this_dict["ljets_ge4j_ge4t_ttb_bb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_tt2b_node","")
    category_dict["varname"] = "DNNOutput_ge4j_ge4t_node_tt2b"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.67

    this_dict["ljets_ge4j_ge4t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["varname"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.53

    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["varname"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.72

    this_dict["ljets_ge4j_ge4t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    

    for l in this_dict:
        this_dict[l]["histoname"] = discrname+"_"+l
        this_dict[l]["histotitle"] = "final discriminator ({})".format(l)
        this_dict[l]["plotPreselections"] = this_dict[l]["category"][0]

    DNNPlots = init_plots(dictionary = this_dict, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_3t(data)
    discriminatorPlots += plots_ge4j_ge4t(data)
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def init_plots(dictionary, data = None):
    plots = [] #init list of plotClasses objects to return
    for label in dictionary:
        subdict     = dictionary[label] #for easy access
        varname     = subdict["varname"] # load discriminator name
        sel         = subdict["plotPreselections"] # load selection
        histoname   = subdict["histoname"] # load histogram name
        histotitle  = subdict["histotitle"] # load histogram title
        catlabel    = subdict["catlabel"] # category label

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if "bin_edges" in subdict:
            bins  = array("f", subdict["bin_edges"])
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            subdict["nhistobins"] = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname,histotitle,nbins,bins),
                    varname,sel,catlabel))

        elif "minxval" in subdict and "maxxval" in subdict:
            nbins = subdict["nhistobins"]
            xmax  = subdict["maxxval"]
            xmin  = subdict["minxval"]
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname, histotitle,nbins,xmin, xmax),
                    varname,sel,catlabel))

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    