
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



def plots_ge4j_ge4t_classifier(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Evt_M_minDrLepTag","Evt_M_minDrLepTag",50,15.0,400.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Reco_JABDT_tHq_Jet_CSV_hdau1","Reco_JABDT_tHq_Jet_CSV_hdau1",50,-1.5,1.0),"Reco_JABDT_tHq_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Reco_JABDT_tHq_abs_ljet_eta","Reco_JABDT_tHq_abs_ljet_eta",50,-1.5,4.5),"Reco_JABDT_tHq_abs_ljet_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Reco_JABDT_ttbar_Jet_CSV_whaddau2","Reco_JABDT_ttbar_Jet_CSV_whaddau2",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,80.0,500.0),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classifier_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_ge4j_ge4t_STXS(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",50.0,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50.0,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50.0,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Evt_Pt_TaggedJetsAverage","Evt_Pt_TaggedJetsAverage",50.0,30.0,600.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50.0,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Reco_JABDT_tHW_log_h_pt","nan",nan,nan,nan),"Reco_JABDT_tHW_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Reco_JABDT_tHq_log_h_pt","nan",nan,nan,nan),"Reco_JABDT_tHq_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","nan",nan,nan,nan),"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Reco_JABDT_ttH_log_h_pt","nan",nan,nan,nan),"Reco_JABDT_ttH_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Reco_JABDT_ttH_log_toplep_m","Reco_JABDT_ttH_log_toplep_m",50.0,-1.5,7.5),"Reco_JABDT_ttH_log_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Reco_tHW_h_dr","nan",nan,nan,nan),"Reco_tHW_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Reco_tHW_h_pt","nan",nan,nan,nan),"Reco_tHW_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Reco_tHq_h_pt","nan",nan,nan,nan),"Reco_tHq_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Reco_ttH_h_dr","nan",nan,nan,nan),"Reco_ttH_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXS_Reco_ttH_h_m","nan",nan,nan,nan),"Reco_ttH_h_m",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_ge4j_3t_classifier(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classifier_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classifier_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classifier_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classifier_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classifier_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classifier_Reco_JABDT_tHW_log_wb_m","Reco_JABDT_tHW_log_wb_m",50,-1.5,8.5),"Reco_JABDT_tHW_log_wb_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classifier_Reco_JABDT_ttH_Jet_CSV_btoplep","Reco_JABDT_ttH_Jet_CSV_btoplep",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classifier_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,80.0,500.0),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classifier_Reco_ttbar_whad_m","Reco_ttbar_whad_m",50,0.0,600.0),"Reco_ttbar_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classifier_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_ge4j_3t_STXS(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",50.0,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50.0,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Evt_Pt_TaggedJetsAverage","Evt_Pt_TaggedJetsAverage",50.0,30.0,600.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Reco_JABDT_tHW_log_h_m","nan",nan,nan,nan),"Reco_JABDT_tHW_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Reco_JABDT_tHW_log_h_pt","nan",nan,nan,nan),"Reco_JABDT_tHW_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Reco_JABDT_tHq_log_h_m","nan",nan,nan,nan),"Reco_JABDT_tHq_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Reco_JABDT_tHq_log_h_pt","nan",nan,nan,nan),"Reco_JABDT_tHq_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","nan",nan,nan,nan),"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Reco_tHW_h_dr","nan",nan,nan,nan),"Reco_tHW_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Reco_tHW_h_pt","nan",nan,nan,nan),"Reco_tHW_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Reco_tHq_h_pt","nan",nan,nan,nan),"Reco_tHq_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_Reco_ttH_h_dr","nan",nan,nan,nan),"Reco_ttH_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXS_TaggedJet_Pt_0","nan",nan,nan,nan),"TaggedJet_Pt[0]",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_dnn(data, discrname):

    ndefaultbins = 50
    interfaces = []


    # plots for ge4j_ge4t_classifier

    interf_ljets_ge4j_ge4t_classifier_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_ttH",
                                            label          = "ljets_ge4j_ge4t_classifier_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==0))")
    interf_ljets_ge4j_ge4t_classifier_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==0))","ljets_ge4j_ge4t_classifier_ttH_node","")
    interf_ljets_ge4j_ge4t_classifier_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_ttH_node.bin_edges = [ 
				0.2032,
				0.219,
				0.2348,
				0.2506,
				0.2664,
				0.2822,
				0.298,
				0.3138,
				0.3296,
				0.3454,
				0.3612,
				0.377,
				0.3928,
				0.4086,
				0.4244,
				0.4402,
				0.456,
				0.4718,
				0.4876,
				0.5034,
				0.5192,
				0.5508,
				0.5824,
				0.614,
				0.6614,
				0.93
				]
    interf_ljets_ge4j_ge4t_classifier_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_ttH_node)
    
    interf_ljets_ge4j_ge4t_classifier_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_classifier_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==1))")
    interf_ljets_ge4j_ge4t_classifier_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==1))","ljets_ge4j_ge4t_classifier_ttmb_node","")
    interf_ljets_ge4j_ge4t_classifier_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_ttmb_node.bin_edges = [ 
				0.2108,
				0.2344,
				0.2462,
				0.258,
				0.2698,
				0.2816,
				0.2934,
				0.3052,
				0.317,
				0.3288,
				0.3406,
				0.3524,
				0.3642,
				0.376,
				0.3878,
				0.3996,
				0.4114,
				0.4232,
				0.435,
				0.4468,
				0.4586,
				0.4822,
				0.494,
				0.5176,
				0.5412,
				0.5648,
				0.612,
				0.73
				]
    interf_ljets_ge4j_ge4t_classifier_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_ttmb_node)
    
    interf_ljets_ge4j_ge4t_classifier_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_classifier_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==2))")
    interf_ljets_ge4j_ge4t_classifier_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==2))","ljets_ge4j_ge4t_classifier_tt2b_node","")
    interf_ljets_ge4j_ge4t_classifier_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_tt2b_node.bin_edges = [ 
				0.1976,
				# 0.2104,
				# 0.2168,
				# 0.2232,
				# 0.2296,
				# 0.236,
				# 0.2424,
				# 0.2488,
				# 0.2552,
				# 0.2616,
				# 0.268,
				# 0.2744,
				# 0.2808,
				# 0.2872,
				# 0.2936,
				# 0.3,
				# 0.3064,
				# 0.3128,
				# 0.3192,
				# 0.3256,
				# 0.332,
				# 0.3448,
				# 0.3576,
				# 0.3768,
				0.46
				]
    interf_ljets_ge4j_ge4t_classifier_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_tt2b_node)
    
    interf_ljets_ge4j_ge4t_classifier_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_classifier_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==3))")
    interf_ljets_ge4j_ge4t_classifier_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==3))","ljets_ge4j_ge4t_classifier_ttcc_node","")
    interf_ljets_ge4j_ge4t_classifier_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_ttcc_node.bin_edges = [ 
				0.1712,
				# 0.2024,
				# 0.2128,
				# 0.2232,
				# 0.2336,
				# 0.244,
				# 0.2544,
				# 0.2648,
				# 0.2752,
				# 0.2856,
				# 0.296,
				# 0.3064,
				# 0.3168,
				# 0.3272,
				# 0.3376,
				# 0.348,
				# 0.3584,
				# 0.3688,
				# 0.3792,
				# 0.3896,
				# 0.4104,
				0.66
				]
    interf_ljets_ge4j_ge4t_classifier_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_ttcc_node)
    
    interf_ljets_ge4j_ge4t_classifier_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_classifier_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==4))")
    interf_ljets_ge4j_ge4t_classifier_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==4))","ljets_ge4j_ge4t_classifier_ttlf_node","")
    interf_ljets_ge4j_ge4t_classifier_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_ttlf_node.bin_edges = [ 
				0.193,
				# 0.2142,
				# 0.2248,
				# 0.2354,
				# 0.246,
				# 0.2566,
				# 0.2672,
				# 0.2778,
				# 0.2884,
				# 0.299,
				# 0.3096,
				# 0.3202,
				# 0.3308,
				# 0.3414,
				# 0.352,
				# 0.3626,
				# 0.3732,
				# 0.3838,
				# 0.3944,
				# 0.405,
				# 0.4156,
				# 0.4262,
				# 0.4368,
				# 0.4474,
				# 0.458,
				# 0.4686,
				# 0.4792,
				# 0.4898,
				# 0.5004,
				# 0.511,
				# 0.5322,
				# 0.5534,
				# 0.5746,
				# 0.6064,
				0.67
				]
    interf_ljets_ge4j_ge4t_classifier_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_ttlf_node)
    
    interf_ljets_ge4j_ge4t_classifier_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_tHq",
                                            label          = "ljets_ge4j_ge4t_classifier_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==5))")
    interf_ljets_ge4j_ge4t_classifier_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==5))","ljets_ge4j_ge4t_classifier_tHq_node","")
    interf_ljets_ge4j_ge4t_classifier_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_tHq_node.bin_edges = [ 
				0.224,
				0.2408,
				0.2576,
				0.2744,
				0.2912,
				0.308,
				0.3248,
				0.3416,
				0.3584,
				0.3752,
				0.392,
				0.4088,
				0.4256,
				0.4592,
				0.4928,
				0.5264,
				0.56,
				0.5936,
				0.6272,
				0.6608,
				0.6944,
				0.7448,
				0.8288,
				0.98
				]
    interf_ljets_ge4j_ge4t_classifier_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_tHq_node)
    
    interf_ljets_ge4j_ge4t_classifier_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_tHW",
                                            label          = "ljets_ge4j_ge4t_classifier_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==6))")
    interf_ljets_ge4j_ge4t_classifier_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==6))","ljets_ge4j_ge4t_classifier_tHW_node","")
    interf_ljets_ge4j_ge4t_classifier_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_tHW_node.bin_edges = [ 
				0.2088,
				0.2432,
				0.2604,
				0.2776,
				0.2948,
				0.312,
				0.3292,
				0.3464,
				0.3636,
				0.3808,
				0.4152,
				0.4324,
				0.4668,
				0.5012,
				0.5528,
				0.6388,
				0.7592,
				1.0
				]
    interf_ljets_ge4j_ge4t_classifier_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_tHW_node)
    


    # plots for ge4j_ge4t_STXS

    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_STXS_node_ttHbb_STXS_0",
    #                                         label          = "ljets_ge4j_ge4t_STXS_ttHbb_STXS_0_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXS==0))")
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_0_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXS==0))","ljets_ge4j_ge4t_STXS_ttHbb_STXS_0_node","")
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_0_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_0_node.bin_edges = [ 
	# 			0.276,
	# 			0.3064,
	# 			0.3216,
	# 			0.3368,
	# 			0.352,
	# 			0.3672,
	# 			0.3824,
	# 			0.3976,
	# 			0.4128,
	# 			0.428,
	# 			0.4432,
	# 			0.4584,
	# 			0.4736,
	# 			0.4888,
	# 			0.504,
	# 			0.5192,
	# 			0.5344,
	# 			0.5496,
	# 			0.5648,
	# 			0.58,
	# 			0.5952,
	# 			0.6104,
	# 			0.6256,
	# 			0.6408,
	# 			0.656,
	# 			0.6712,
	# 			0.6864,
	# 			0.7016,
	# 			0.7168,
	# 			0.732,
	# 			0.7472,
	# 			0.7624,
	# 			0.7776,
	# 			0.7928,
	# 			0.808,
	# 			0.8384,
	# 			0.884,
	# 			0.96
	# 			]
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_0_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_0_node)
    
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_STXS_node_ttHbb_STXS_1",
    #                                         label          = "ljets_ge4j_ge4t_STXS_ttHbb_STXS_1_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXS==1))")
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_1_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXS==1))","ljets_ge4j_ge4t_STXS_ttHbb_STXS_1_node","")
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_1_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_1_node.bin_edges = [ 
	# 			0.238,
	# 			0.2836,
	# 			0.314,
	# 			0.3292,
	# 			0.3368,
	# 			0.3444,
	# 			0.352,
	# 			0.3596,
	# 			0.3672,
	# 			0.3748,
	# 			0.3824,
	# 			0.39,
	# 			0.3976,
	# 			0.4052,
	# 			0.4128,
	# 			0.4204,
	# 			0.428,
	# 			0.4356,
	# 			0.4432,
	# 			0.4508,
	# 			0.4584,
	# 			0.466,
	# 			0.4736,
	# 			0.4812,
	# 			0.4888,
	# 			0.4964,
	# 			0.5116,
	# 			0.58
	# 			]
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_1_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_1_node)
    
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_STXS_node_ttHbb_STXS_2",
    #                                         label          = "ljets_ge4j_ge4t_STXS_ttHbb_STXS_2_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXS==2))")
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_2_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXS==2))","ljets_ge4j_ge4t_STXS_ttHbb_STXS_2_node","")
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_2_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_2_node.bin_edges = [ 
	# 			0.288,
	# 			0.31,
	# 			0.321,
	# 			0.332,
	# 			0.343,
	# 			0.354,
	# 			0.365,
	# 			0.376,
	# 			0.387,
	# 			0.398,
	# 			0.409,
	# 			0.42,
	# 			0.431,
	# 			0.442,
	# 			0.453,
	# 			0.464,
	# 			0.475,
	# 			0.486,
	# 			0.497,
	# 			0.508,
	# 			0.519,
	# 			0.53,
	# 			0.541,
	# 			0.552,
	# 			0.563,
	# 			0.574,
	# 			0.585,
	# 			0.596,
	# 			0.607,
	# 			0.618,
	# 			0.629,
	# 			0.651,
	# 			0.673,
	# 			0.75
	# 			]
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_2_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_2_node)
    
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_STXS_node_ttHbb_STXS_3",
    #                                         label          = "ljets_ge4j_ge4t_STXS_ttHbb_STXS_3_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXS==3))")
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_3_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXS==3))","ljets_ge4j_ge4t_STXS_ttHbb_STXS_3_node","")
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_3_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_3_node.bin_edges = [ 
	# 			0.2552,
	# 			0.2828,
	# 			0.3104,
	# 			0.338,
	# 			0.3656,
	# 			0.3794,
	# 			0.3932,
	# 			0.407,
	# 			0.4208,
	# 			0.4346,
	# 			0.4484,
	# 			0.4622,
	# 			0.476,
	# 			0.4898,
	# 			0.5036,
	# 			0.5174,
	# 			0.5312,
	# 			0.545,
	# 			0.5588,
	# 			0.5726,
	# 			0.5864,
	# 			0.6002,
	# 			0.614,
	# 			0.6278,
	# 			0.6416,
	# 			0.6554,
	# 			0.6692,
	# 			0.683,
	# 			0.6968,
	# 			0.7106,
	# 			0.7244,
	# 			0.7382,
	# 			0.752,
	# 			0.7658,
	# 			0.7934,
	# 			0.821,
	# 			0.89
	# 			]
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_3_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_3_node)
    
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_STXS_node_ttHbb_STXS_4",
    #                                         label          = "ljets_ge4j_ge4t_STXS_ttHbb_STXS_4_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXS==4))")
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_4_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXS==4))","ljets_ge4j_ge4t_STXS_ttHbb_STXS_4_node","")
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_4_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_4_node.bin_edges = [ 
	# 			0.264,
	# 			0.36,
	# 			0.408,
	# 			0.456,
	# 			0.488,
	# 			0.52,
	# 			0.568,
	# 			0.6,
	# 			0.632,
	# 			0.664,
	# 			0.696,
	# 			0.728,
	# 			0.76,
	# 			0.792,
	# 			0.824,
	# 			0.856,
	# 			0.888,
	# 			0.904,
	# 			0.936,
	# 			0.952,
	# 			0.968,
	# 			0.984,
	# 			1.0
	# 			]
    # interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_4_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttHbb_STXS_4_node)
    


    # plots for ge4j_3t_classifier

    interf_ljets_ge4j_3t_classifier_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_ttH",
                                            label          = "ljets_ge4j_3t_classifier_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==0))")
    interf_ljets_ge4j_3t_classifier_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==0))","ljets_ge4j_3t_classifier_ttH_node","")
    interf_ljets_ge4j_3t_classifier_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_ttH_node.bin_edges = [ 
				0.17,
				0.185,
				0.2,
				0.215,
				0.23,
				0.245,
				0.26,
				0.275,
				0.29,
				0.305,
				0.32,
				0.335,
				0.35,
				0.365,
				0.38,
				0.395,
				0.41,
				0.425,
				0.44,
				0.455,
				0.47,
				0.485,
				0.5,
				0.515,
				0.53,
				0.56,
				0.89
				]
    interf_ljets_ge4j_3t_classifier_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_ttH_node)
    
    interf_ljets_ge4j_3t_classifier_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_ttmb",
                                            label          = "ljets_ge4j_3t_classifier_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==1))")
    interf_ljets_ge4j_3t_classifier_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==1))","ljets_ge4j_3t_classifier_ttmb_node","")
    interf_ljets_ge4j_3t_classifier_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_ttmb_node.bin_edges = [ 
				0.172,
				0.18,
				0.188,
				0.196,
				0.204,
				0.212,
				0.22,
				0.228,
				0.236,
				0.244,
				0.252,
				0.26,
				0.268,
				0.276,
				0.284,
				0.292,
				0.3,
				0.308,
				0.316,
				0.324,
				0.332,
				0.34,
				0.348,
				0.356,
				0.364,
				0.372,
				0.38,
				0.388,
				0.404,
				0.42,
				0.54
				]
    interf_ljets_ge4j_3t_classifier_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_ttmb_node)
    
    interf_ljets_ge4j_3t_classifier_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_tt2b",
                                            label          = "ljets_ge4j_3t_classifier_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==2))")
    interf_ljets_ge4j_3t_classifier_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==2))","ljets_ge4j_3t_classifier_tt2b_node","")
    interf_ljets_ge4j_3t_classifier_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_tt2b_node.bin_edges = [ 
				0.1608,
				# 0.1712,
				# 0.1816,
				# 0.192,
				# 0.2024,
				# 0.2128,
				# 0.2232,
				# 0.2336,
				# 0.244,
				# 0.2544,
				# 0.2648,
				# 0.2752,
				# 0.2856,
				# 0.296,
				# 0.3064,
				# 0.3168,
				# 0.3272,
				# 0.3376,
				# 0.348,
				# 0.3584,
				# 0.3688,
				# 0.3792,
				# 0.3896,
				# 0.4,
				# 0.4104,
				# 0.4208,
				# 0.4312,
				# 0.4416,
				# 0.452,
				# 0.4728,
				# 0.504,
				0.66
				]
    interf_ljets_ge4j_3t_classifier_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_tt2b_node)
    
    interf_ljets_ge4j_3t_classifier_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_ttcc",
                                            label          = "ljets_ge4j_3t_classifier_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==3))")
    interf_ljets_ge4j_3t_classifier_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==3))","ljets_ge4j_3t_classifier_ttcc_node","")
    interf_ljets_ge4j_3t_classifier_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_ttcc_node.bin_edges = [ 
				0.1604,
				# 0.1706,
				# 0.1808,
				# 0.191,
				# 0.2012,
				# 0.2114,
				# 0.2216,
				# 0.2318,
				# 0.242,
				# 0.2522,
				# 0.2624,
				# 0.2726,
				# 0.2828,
				# 0.293,
				# 0.3032,
				# 0.3134,
				# 0.3236,
				# 0.3338,
				# 0.344,
				# 0.3542,
				# 0.3644,
				# 0.3746,
				# 0.3848,
				# 0.395,
				# 0.4052,
				# 0.4358,
				# 0.4562,
				# 0.4766,
				# 0.497,
				# 0.5174,
				# 0.5378,
				0.65
				]
    interf_ljets_ge4j_3t_classifier_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_ttcc_node)
    
    interf_ljets_ge4j_3t_classifier_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_ttlf",
                                            label          = "ljets_ge4j_3t_classifier_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==4))")
    interf_ljets_ge4j_3t_classifier_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==4))","ljets_ge4j_3t_classifier_ttlf_node","")
    interf_ljets_ge4j_3t_classifier_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_ttlf_node.bin_edges = [ 
				0.1656,
				# 0.1784,
				# 0.1912,
				# 0.204,
				# 0.2168,
				# 0.2296,
				# 0.2424,
				# 0.2552,
				# 0.268,
				# 0.2808,
				# 0.2936,
				# 0.3064,
				# 0.3192,
				# 0.332,
				# 0.3448,
				# 0.3576,
				# 0.3704,
				# 0.3832,
				# 0.396,
				# 0.4088,
				# 0.4216,
				# 0.4344,
				# 0.4472,
				# 0.46,
				# 0.4728,
				# 0.4856,
				# 0.4984,
				# 0.5112,
				# 0.524,
				# 0.5368,
				# 0.5496,
				# 0.5624,
				# 0.5752,
				# 0.588,
				# 0.6008,
				# 0.6136,
				# 0.6264,
				# 0.6392,
				# 0.652,
				# 0.6776,
				# 0.7032,
				0.78
				]
    interf_ljets_ge4j_3t_classifier_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_ttlf_node)
    
    interf_ljets_ge4j_3t_classifier_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_tHq",
                                            label          = "ljets_ge4j_3t_classifier_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==5))")
    interf_ljets_ge4j_3t_classifier_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==5))","ljets_ge4j_3t_classifier_tHq_node","")
    interf_ljets_ge4j_3t_classifier_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_tHq_node.bin_edges = [ 
				0.156,
				0.172,
				0.188,
				0.204,
				0.22,
				0.236,
				0.252,
				0.268,
				0.284,
				0.3,
				0.316,
				0.332,
				0.348,
				0.364,
				0.38,
				0.396,
				0.412,
				0.428,
				0.444,
				0.46,
				0.476,
				0.492,
				0.508,
				0.524,
				0.54,
				0.556,
				0.572,
				0.588,
				0.604,
				0.62,
				0.636,
				0.652,
				0.668,
				0.684,
				0.7,
				0.716,
				0.732,
				0.748,
				0.764,
				0.78,
				0.812,
				0.94
				]
    interf_ljets_ge4j_3t_classifier_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_tHq_node)
    
    interf_ljets_ge4j_3t_classifier_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_tHW",
                                            label          = "ljets_ge4j_3t_classifier_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==6))")
    interf_ljets_ge4j_3t_classifier_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==6))","ljets_ge4j_3t_classifier_tHW_node","")
    interf_ljets_ge4j_3t_classifier_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_tHW_node.bin_edges = [ 
				0.1572,
				0.1744,
				0.1916,
				0.2088,
				0.226,
				0.2432,
				0.2604,
				0.2776,
				0.2948,
				0.312,
				0.3292,
				0.3464,
				0.3636,
				0.3808,
				0.398,
				0.4152,
				0.4324,
				0.4496,
				0.4668,
				0.484,
				0.5012,
				0.5184,
				0.5356,
				0.5528,
				0.57,
				0.5872,
				0.6044,
				0.6216,
				0.6388,
				0.656,
				0.6732,
				0.6904,
				0.7076,
				0.7248,
				0.742,
				0.7592,
				0.7764,
				0.8108,
				0.8452,
				0.8796,
				0.914,
				1.0
				]
    interf_ljets_ge4j_3t_classifier_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_tHW_node)
    


    # plots for ge4j_3t_STXS

    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_STXS_node_ttHbb_STXS_0",
    #                                         label          = "ljets_ge4j_3t_STXS_ttHbb_STXS_0_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXS==0))")
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_0_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXS==0))","ljets_ge4j_3t_STXS_ttHbb_STXS_0_node","")
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_0_node.category_label = "\geq 4 jets, 3 b-tags"
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_0_node.bin_edges = [ 
	# 			0.2156,
	# 			0.2312,
	# 			0.2468,
	# 			0.2624,
	# 			0.278,
	# 			0.2936,
	# 			0.3092,
	# 			0.3248,
	# 			0.3404,
	# 			0.356,
	# 			0.3716,
	# 			0.3872,
	# 			0.4028,
	# 			0.4184,
	# 			0.434,
	# 			0.4496,
	# 			0.4652,
	# 			0.4808,
	# 			0.4964,
	# 			0.512,
	# 			0.5276,
	# 			0.5432,
	# 			0.5588,
	# 			0.5744,
	# 			0.59,
	# 			0.6056,
	# 			0.6212,
	# 			0.6368,
	# 			0.6524,
	# 			0.668,
	# 			0.6836,
	# 			0.6992,
	# 			0.7148,
	# 			0.7304,
	# 			0.746,
	# 			0.7616,
	# 			0.7772,
	# 			0.7928,
	# 			0.8084,
	# 			0.824,
	# 			0.8396,
	# 			0.8552,
	# 			0.8708,
	# 			0.8864,
	# 			0.902,
	# 			0.9176,
	# 			0.9332,
	# 			0.9488,
	# 			0.98
	# 			]
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_0_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_3t_STXS_ttHbb_STXS_0_node)
    
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_STXS_node_ttHbb_STXS_1",
    #                                         label          = "ljets_ge4j_3t_STXS_ttHbb_STXS_1_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXS==1))")
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_1_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXS==1))","ljets_ge4j_3t_STXS_ttHbb_STXS_1_node","")
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_1_node.category_label = "\geq 4 jets, 3 b-tags"
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_1_node.bin_edges = [ 
	# 			0.2204,
	# 			0.2306,
	# 			0.2408,
	# 			0.251,
	# 			0.2612,
	# 			0.2714,
	# 			0.2816,
	# 			0.2918,
	# 			0.302,
	# 			0.3122,
	# 			0.3224,
	# 			0.3326,
	# 			0.3428,
	# 			0.353,
	# 			0.3632,
	# 			0.3734,
	# 			0.3836,
	# 			0.3938,
	# 			0.404,
	# 			0.4142,
	# 			0.4244,
	# 			0.4346,
	# 			0.4448,
	# 			0.455,
	# 			0.4652,
	# 			0.4754,
	# 			0.4856,
	# 			0.4958,
	# 			0.506,
	# 			0.5162,
	# 			0.5264,
	# 			0.5366,
	# 			0.5468,
	# 			0.557,
	# 			0.5672,
	# 			0.5774,
	# 			0.5876,
	# 			0.5978,
	# 			0.608,
	# 			0.6182,
	# 			0.6284,
	# 			0.6386,
	# 			0.6488,
	# 			0.659,
	# 			0.6692,
	# 			0.6794,
	# 			0.6896,
	# 			0.71
	# 			]
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_1_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_3t_STXS_ttHbb_STXS_1_node)
    
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_STXS_node_ttHbb_STXS_2",
    #                                         label          = "ljets_ge4j_3t_STXS_ttHbb_STXS_2_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXS==2))")
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_2_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXS==2))","ljets_ge4j_3t_STXS_ttHbb_STXS_2_node","")
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_2_node.category_label = "\geq 4 jets, 3 b-tags"
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_2_node.bin_edges = [ 
	# 			0.2272,
	# 			0.2408,
	# 			0.2544,
	# 			0.268,
	# 			0.2816,
	# 			0.2952,
	# 			0.3088,
	# 			0.3224,
	# 			0.336,
	# 			0.3496,
	# 			0.3632,
	# 			0.3768,
	# 			0.3904,
	# 			0.404,
	# 			0.4176,
	# 			0.4312,
	# 			0.4448,
	# 			0.4584,
	# 			0.472,
	# 			0.4856,
	# 			0.4992,
	# 			0.5128,
	# 			0.5264,
	# 			0.54,
	# 			0.5536,
	# 			0.5672,
	# 			0.5808,
	# 			0.5944,
	# 			0.608,
	# 			0.6216,
	# 			0.6352,
	# 			0.6488,
	# 			0.6624,
	# 			0.676,
	# 			0.6896,
	# 			0.7032,
	# 			0.7168,
	# 			0.7304,
	# 			0.744,
	# 			0.7576,
	# 			0.7712,
	# 			0.7848,
	# 			0.7984,
	# 			0.812,
	# 			0.8256,
	# 			0.8392,
	# 			0.88
	# 			]
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_2_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_3t_STXS_ttHbb_STXS_2_node)
    
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_STXS_node_ttHbb_STXS_3",
    #                                         label          = "ljets_ge4j_3t_STXS_ttHbb_STXS_3_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXS==3))")
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_3_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXS==3))","ljets_ge4j_3t_STXS_ttHbb_STXS_3_node","")
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_3_node.category_label = "\geq 4 jets, 3 b-tags"
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_3_node.bin_edges = [ 
	# 			0.2152,
	# 			0.2304,
	# 			0.2456,
	# 			0.2608,
	# 			0.276,
	# 			0.2912,
	# 			0.3064,
	# 			0.3216,
	# 			0.3368,
	# 			0.352,
	# 			0.3672,
	# 			0.3824,
	# 			0.3976,
	# 			0.4128,
	# 			0.428,
	# 			0.4432,
	# 			0.4584,
	# 			0.4736,
	# 			0.4888,
	# 			0.504,
	# 			0.5192,
	# 			0.5344,
	# 			0.5496,
	# 			0.5648,
	# 			0.58,
	# 			0.5952,
	# 			0.6104,
	# 			0.6256,
	# 			0.6408,
	# 			0.656,
	# 			0.6712,
	# 			0.6864,
	# 			0.7016,
	# 			0.7168,
	# 			0.732,
	# 			0.7472,
	# 			0.7624,
	# 			0.7776,
	# 			0.7928,
	# 			0.808,
	# 			0.8232,
	# 			0.8384,
	# 			0.8536,
	# 			0.8688,
	# 			0.884,
	# 			0.8992,
	# 			0.9144,
	# 			0.9296,
	# 			0.9448,
	# 			0.96
	# 			]
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_3_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_3t_STXS_ttHbb_STXS_3_node)
    
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_STXS_node_ttHbb_STXS_4",
    #                                         label          = "ljets_ge4j_3t_STXS_ttHbb_STXS_4_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXS==4))")
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_4_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXS==4))","ljets_ge4j_3t_STXS_ttHbb_STXS_4_node","")
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_4_node.category_label = "\geq 4 jets, 3 b-tags"
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_4_node.bin_edges = [ 
	# 			0.2158,
	# 			0.2316,
	# 			0.2474,
	# 			0.2632,
	# 			0.279,
	# 			0.2948,
	# 			0.3106,
	# 			0.3264,
	# 			0.3422,
	# 			0.358,
	# 			0.3738,
	# 			0.3896,
	# 			0.4054,
	# 			0.4212,
	# 			0.437,
	# 			0.4528,
	# 			0.4686,
	# 			0.4844,
	# 			0.5002,
	# 			0.516,
	# 			0.5318,
	# 			0.5476,
	# 			0.5634,
	# 			0.5792,
	# 			0.595,
	# 			0.6108,
	# 			0.6266,
	# 			0.6424,
	# 			0.6582,
	# 			0.674,
	# 			0.6898,
	# 			0.7056,
	# 			0.7214,
	# 			0.7372,
	# 			0.753,
	# 			0.7688,
	# 			0.7846,
	# 			0.8004,
	# 			0.8162,
	# 			0.832,
	# 			0.8478,
	# 			0.8636,
	# 			0.8794,
	# 			0.8952,
	# 			0.911,
	# 			0.9268,
	# 			0.9426,
	# 			0.9584,
	# 			0.9742,
	# 			0.99
	# 			]
    # interf_ljets_ge4j_3t_STXS_ttHbb_STXS_4_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_3t_STXS_ttHbb_STXS_4_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    # discriminatorPlots += plots_ge4j_ge4t_classifier(data)
    # discriminatorPlots += plots_ge4j_ge4t_STXS(data)
    # discriminatorPlots += plots_ge4j_3t_classifier(data)
    # discriminatorPlots += plots_ge4j_3t_STXS(data)
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
    