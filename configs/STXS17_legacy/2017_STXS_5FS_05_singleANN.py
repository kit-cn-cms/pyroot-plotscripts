
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import util.variableHistoInterface as vhi
import ROOT
from array import array
from copy import deepcopy


memexp = ""



def plots_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_CSV_3","fourth highest b-tag value",50,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_avg","average b-tag value",50,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_dev","average deviation of b-tag value",50,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_min","minimal b-tag value",50,0.0,1.0),"Evt_CSV_min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",50,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_HT","H_{T}",50,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",50,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_sphericity_jets","sphericity of jets",50,0.0,1.0),"Evt_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_transverse_sphericity_jets","transverse sphericity of jets",50,0.00177236890886,0.999349296093),"Evt_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_N_BTagsT","number of b-tags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",20,0.0,1.0),"Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1 ","Reco_JABDT_ttbar_Jet_CSV_whaddau1 ",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1 ",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttbar_log_toplep_pt","Reco_JABDT_ttbar_log_toplep_pt",50,0.0,10.0),"Reco_JABDT_ttbar_log_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_h_eta","Reco_ttH_h_eta",50,-4.0,-4.0),"Reco_ttH_h_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_h_phi","Reco_ttH_h_phi",50,-4.0,4.0),"Reco_ttH_h_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_tophad_m","Reco_ttH_tophad_m",50,0.0,800.0),"Reco_ttH_tophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_tophad_pt","Reco_ttH_tophad_pt",50,0.0,800.0),"Reco_ttH_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_whad_dr","Reco_ttH_whad_dr",50,0.0,4.0),"Reco_ttH_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_whaddau_m2","Reco_ttH_whaddau_m2",50,0.0,50.0),"Reco_ttH_whaddau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttbar_btophad_eta","Reco_ttbar_btophad_eta",50,-4.0,4.0),"Reco_ttbar_btophad_eta",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_avg","average b-tag value",50,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_dev","average deviation of b-tag value",50,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",50,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_min","minimal b-tag value",50,0.0,1.0),"Evt_CSV_min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",50,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",50,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_HT_jets","H_{T}(jets)",50,200.0,1500.0),"Evt_HT_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_HT_wo_MET","H_{T} without MET",50,200.0,1500.0),"Evt_HT_wo_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",50,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_sphericity_jets","sphericity of jets",50,0.0,1.0),"Evt_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_transverse_sphericity_jets","transverse sphericity of jets",50,0.00177236890886,0.999349296093),"Evt_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_N_BTagsT","number of b-tags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",20,0.0,1.0),"Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        # plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1 ","Reco_JABDT_ttbar_Jet_CSV_whaddau1 ",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1 ",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_log_toplep_pt","Reco_JABDT_ttbar_log_toplep_pt",50,0.0,10.0),"Reco_JABDT_ttbar_log_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_h_eta","Reco_ttH_h_eta",50,-4.0,-4.0),"Reco_ttH_h_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_h_phi","Reco_ttH_h_phi",50,-4.0,4.0),"Reco_ttH_h_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_tophad_m","Reco_ttH_tophad_m",50,0.0,800.0),"Reco_ttH_tophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_tophad_pt","Reco_ttH_tophad_pt",50,0.0,800.0),"Reco_ttH_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_whad_dr","Reco_ttH_whad_dr",50,0.0,4.0),"Reco_ttH_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_whaddau_m2","Reco_ttH_whaddau_m2",50,0.0,50.0),"Reco_ttH_whaddau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttbar_btophad_eta","Reco_ttbar_btophad_eta",50,-4.0,4.0),"Reco_ttbar_btophad_eta",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def plots_dnn(data, discrname):

    ndefaultbins = 7
    interfaces = []


    # plots for ge4j_ge4t

    interf_ljets_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))")
    interf_ljets_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttcc_node","")
    interf_ljets_ge4j_ge4t_ttcc_node.minxval = 0.11
    interf_ljets_ge4j_ge4t_ttcc_node.maxxval = 0.52
    interf_ljets_ge4j_ge4t_ttcc_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttcc_node)
    
    interf_ljets_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))")
    interf_ljets_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttlf_node","")
    interf_ljets_ge4j_ge4t_ttlf_node.minxval = 0.11
    interf_ljets_ge4j_ge4t_ttlf_node.maxxval = 0.79
    interf_ljets_ge4j_ge4t_ttlf_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttlf_node)
    
    interf_ljets_ge4j_ge4t_old_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_old_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_old_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))")
    interf_ljets_ge4j_ge4t_old_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_old_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_old_ttb_bb_node.minxval = 0.11
    interf_ljets_ge4j_ge4t_old_ttb_bb_node.maxxval = 0.61
    interf_ljets_ge4j_ge4t_old_ttb_bb_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_old_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_old_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_old_tt2b",
                                            label          = "ljets_ge4j_ge4t_old_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))")
    interf_ljets_ge4j_ge4t_old_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_old_tt2b_node","")
    interf_ljets_ge4j_ge4t_old_tt2b_node.minxval = 0.11
    interf_ljets_ge4j_ge4t_old_tt2b_node.maxxval = 0.89
    interf_ljets_ge4j_ge4t_old_tt2b_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_old_tt2b_node)
    
    interf_ljets_ge4j_ge4t_ttH_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH_1",
                                            label          = "ljets_ge4j_ge4t_ttH_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))")
    interf_ljets_ge4j_ge4t_ttH_1_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttH_1_node","")
    interf_ljets_ge4j_ge4t_ttH_1_node.minxval = 0.11
    interf_ljets_ge4j_ge4t_ttH_1_node.maxxval = 0.6
    interf_ljets_ge4j_ge4t_ttH_1_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_1_node)
    
    interf_ljets_ge4j_ge4t_ttH_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH_2",
                                            label          = "ljets_ge4j_ge4t_ttH_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==5))")
    interf_ljets_ge4j_ge4t_ttH_2_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==5))","ljets_ge4j_ge4t_ttH_2_node","")
    interf_ljets_ge4j_ge4t_ttH_2_node.minxval = 0.15
    interf_ljets_ge4j_ge4t_ttH_2_node.maxxval = 0.35
    interf_ljets_ge4j_ge4t_ttH_2_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_2_node)
    
    interf_ljets_ge4j_ge4t_ttH_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH_3",
                                            label          = "ljets_ge4j_ge4t_ttH_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==6))")
    interf_ljets_ge4j_ge4t_ttH_3_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==6))","ljets_ge4j_ge4t_ttH_3_node","")
    interf_ljets_ge4j_ge4t_ttH_3_node.minxval = 0.15
    interf_ljets_ge4j_ge4t_ttH_3_node.maxxval = 0.45
    interf_ljets_ge4j_ge4t_ttH_3_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_3_node)
    
    interf_ljets_ge4j_ge4t_ttH_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH_4",
                                            label          = "ljets_ge4j_ge4t_ttH_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==7))")
    interf_ljets_ge4j_ge4t_ttH_4_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==7))","ljets_ge4j_ge4t_ttH_4_node","")
    interf_ljets_ge4j_ge4t_ttH_4_node.minxval = 0.11
    interf_ljets_ge4j_ge4t_ttH_4_node.maxxval = 0.6
    interf_ljets_ge4j_ge4t_ttH_4_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_4_node)
    
    interf_ljets_ge4j_ge4t_ttH_5_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH_5",
                                            label          = "ljets_ge4j_ge4t_ttH_5_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==8))")
    interf_ljets_ge4j_ge4t_ttH_5_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==8))","ljets_ge4j_ge4t_ttH_5_node","")
    interf_ljets_ge4j_ge4t_ttH_5_node.minxval = 0.11
    interf_ljets_ge4j_ge4t_ttH_5_node.maxxval = 0.98
    interf_ljets_ge4j_ge4t_ttH_5_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_5_node)
    


    # plots for ge4j_3t

    interf_ljets_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttcc",
                                            label          = "ljets_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))")
    interf_ljets_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttcc_node","")
    interf_ljets_ge4j_3t_ttcc_node.minxval = 0.11
    interf_ljets_ge4j_3t_ttcc_node.maxxval = 0.41
    interf_ljets_ge4j_3t_ttcc_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttcc_node)
    
    interf_ljets_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttlf",
                                            label          = "ljets_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))")
    interf_ljets_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttlf_node","")
    interf_ljets_ge4j_3t_ttlf_node.minxval = 0.11
    interf_ljets_ge4j_3t_ttlf_node.maxxval = 0.77
    interf_ljets_ge4j_3t_ttlf_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttlf_node)
    
    interf_ljets_ge4j_3t_old_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_old_ttb_bb",
                                            label          = "ljets_ge4j_3t_old_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))")
    interf_ljets_ge4j_3t_old_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_old_ttb_bb_node","")
    interf_ljets_ge4j_3t_old_ttb_bb_node.minxval = 0.11
    interf_ljets_ge4j_3t_old_ttb_bb_node.maxxval = 0.65
    interf_ljets_ge4j_3t_old_ttb_bb_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_old_ttb_bb_node)
    
    interf_ljets_ge4j_3t_old_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_old_tt2b",
                                            label          = "ljets_ge4j_3t_old_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))")
    interf_ljets_ge4j_3t_old_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_old_tt2b_node","")
    interf_ljets_ge4j_3t_old_tt2b_node.minxval = 0.11
    interf_ljets_ge4j_3t_old_tt2b_node.maxxval = 0.86
    interf_ljets_ge4j_3t_old_tt2b_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_old_tt2b_node)
    
    interf_ljets_ge4j_3t_ttH_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttH_1",
                                            label          = "ljets_ge4j_3t_ttH_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))")
    interf_ljets_ge4j_3t_ttH_1_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttH_1_node","")
    interf_ljets_ge4j_3t_ttH_1_node.minxval = 0.11
    interf_ljets_ge4j_3t_ttH_1_node.maxxval = 0.56
    interf_ljets_ge4j_3t_ttH_1_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_1_node)
    
    interf_ljets_ge4j_3t_ttH_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttH_2",
                                            label          = "ljets_ge4j_3t_ttH_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==5))")
    interf_ljets_ge4j_3t_ttH_2_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==5))","ljets_ge4j_3t_ttH_2_node","")
    interf_ljets_ge4j_3t_ttH_2_node.minxval = 0.15
    interf_ljets_ge4j_3t_ttH_2_node.maxxval = 0.36
    interf_ljets_ge4j_3t_ttH_2_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_2_node)
    
    interf_ljets_ge4j_3t_ttH_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttH_3",
                                            label          = "ljets_ge4j_3t_ttH_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==6))")
    interf_ljets_ge4j_3t_ttH_3_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==6))","ljets_ge4j_3t_ttH_3_node","")
    interf_ljets_ge4j_3t_ttH_3_node.minxval = 0.11
    interf_ljets_ge4j_3t_ttH_3_node.maxxval = 0.42
    interf_ljets_ge4j_3t_ttH_3_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_3_node)
    
    interf_ljets_ge4j_3t_ttH_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttH_4",
                                            label          = "ljets_ge4j_3t_ttH_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==7))")
    interf_ljets_ge4j_3t_ttH_4_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==7))","ljets_ge4j_3t_ttH_4_node","")
    interf_ljets_ge4j_3t_ttH_4_node.minxval = 0.11
    interf_ljets_ge4j_3t_ttH_4_node.maxxval = 0.66
    interf_ljets_ge4j_3t_ttH_4_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_4_node)
    
    interf_ljets_ge4j_3t_ttH_5_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttH_5",
                                            label          = "ljets_ge4j_3t_ttH_5_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==8))")
    interf_ljets_ge4j_3t_ttH_5_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==8))","ljets_ge4j_3t_ttH_5_node","")
    interf_ljets_ge4j_3t_ttH_5_node.minxval = 0.11
    interf_ljets_ge4j_3t_ttH_5_node.maxxval = 0.99
    interf_ljets_ge4j_3t_ttH_5_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_5_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def init_plots(interfaces, data = None):
    plots = [] #init list of plotClasses objects to return
    dictionary = {}
    for interf in interfaces:

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if not interf.bin_edges is None:
            bins  = array("f", interf.bin_edges)
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            interf.nhistobins = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,bins),
                    interf.varname,interf.selection,interf.category_label))

        elif not (interf.minxval is None or interf.maxxval is None):
            nbins = interf.nhistobins
            xmax  = interf.maxxval
            xmin  = interf.minxval
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,xmin, xmax),
                    interf.varname,interf.selection,interf.category_label))
        else:
            print("FATAL ERROR: Unable to load bin edges or min/max values for histogram!")
            print(interf)
            raise ValueError
        dictionary[interf.label] = interf.getDictionary()

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    
