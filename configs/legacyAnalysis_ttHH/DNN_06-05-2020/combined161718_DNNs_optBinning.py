
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
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M_minDrLepTag","Evt_M_minDrLepTag",50,15.0,400.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1","Reco_JABDT_tHq_Jet_CSV_hdau1",50,-1.5,1.0),"Reco_JABDT_tHq_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta","Reco_JABDT_tHq_abs_ljet_eta",50,-1.5,4.5),"Reco_JABDT_tHq_abs_ljet_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2","Reco_JABDT_ttbar_Jet_CSV_whaddau2",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,80.0,500.0),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m","Reco_JABDT_tHW_log_wb_m",50,-1.5,8.5),"Reco_JABDT_tHW_log_wb_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep","Reco_JABDT_ttH_Jet_CSV_btoplep",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,80.0,500.0),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttbar_whad_m","Reco_ttbar_whad_m",50,0.0,600.0),"Reco_ttbar_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_dnn(data, discrname):

    ndefaultbins = 15
    interfaces = []


    # plots for ge4j_ge4t

    interf_ljets_ge4j_ge4t_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttHbb",
                                            label          = "ljets_ge4j_ge4t_ttHbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))")
    interf_ljets_ge4j_ge4t_ttHbb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttHbb_node","")
    interf_ljets_ge4j_ge4t_ttHbb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_ttHbb_node.bin_edges = [ 
				0.158,
				0.186,
				0.214,
				0.242,
				0.27,
				0.298,
				0.326,
				0.354,
				0.382,
				0.41,
				0.55
				]
    interf_ljets_ge4j_ge4t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttHbb_node)
    
    interf_ljets_ge4j_ge4t_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttHnonbb",
                                            label          = "ljets_ge4j_ge4t_ttHnonbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))")
    interf_ljets_ge4j_ge4t_ttHnonbb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttHnonbb_node","")
    interf_ljets_ge4j_ge4t_ttHnonbb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_ttHnonbb_node.bin_edges = [ 
				0.1473,
				0.1647,
				0.182,
				0.1993,
				0.2167,
				0.234,
				0.2513,
				0.2687,
				0.39
				]
    interf_ljets_ge4j_ge4t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttHnonbb_node)
    
    interf_ljets_ge4j_ge4t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))")
    interf_ljets_ge4j_ge4t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_ttmb_node","")
    interf_ljets_ge4j_ge4t_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_ttmb_node.bin_edges = [ 
				0.154,
				0.178,
				0.202,
				0.226,
				0.25,
				0.274,
				0.298,
				0.322,
				0.346,
				0.49
				]
    interf_ljets_ge4j_ge4t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttmb_node)
    
    interf_ljets_ge4j_ge4t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))")
    interf_ljets_ge4j_ge4t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_tt2b_node","")
    interf_ljets_ge4j_ge4t_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_tt2b_node.bin_edges = [ 
				0.1487,
				# 0.158,
				# 0.1673,
				# 0.1767,
				# 0.186,
				# 0.1953,
				# 0.2047,
				# 0.214,
				# 0.2233,
				0.27
				]
    interf_ljets_ge4j_ge4t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_tt2b_node)
    
    interf_ljets_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))")
    interf_ljets_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttcc_node","")
    interf_ljets_ge4j_ge4t_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_ttcc_node.bin_edges = [ 
				0.1533,
				# 0.1767,
				# 0.2,
				# 0.2233,
				# 0.2467,
				# 0.27,
				# 0.2933,
				# 0.3167,
				# 0.34,
				0.48
				]
    interf_ljets_ge4j_ge4t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttcc_node)
    
    interf_ljets_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==5))")
    interf_ljets_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==5))","ljets_ge4j_ge4t_ttlf_node","")
    interf_ljets_ge4j_ge4t_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_ttlf_node.bin_edges = [ 
				0.13,
				# 0.1667,
				# 0.2033,
				# 0.24,
				# 0.2767,
				# 0.3133,
				# 0.35,
				# 0.3867,
				# 0.4233,
				# 0.46,
				# 0.4967,
				# 0.5333,
				0.68
				]
    interf_ljets_ge4j_ge4t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttlf_node)
    
    interf_ljets_ge4j_ge4t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_tHq",
                                            label          = "ljets_ge4j_ge4t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==6))")
    interf_ljets_ge4j_ge4t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==6))","ljets_ge4j_ge4t_tHq_node","")
    interf_ljets_ge4j_ge4t_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_tHq_node.bin_edges = [ 
				0.13,
				0.186,
				0.242,
				0.298,
				0.354,
				0.41,
				0.466,
				0.522,
				0.578,
				0.634,
				0.746,
				0.97
				]
    interf_ljets_ge4j_ge4t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_tHq_node)
    
    interf_ljets_ge4j_ge4t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_tHW",
                                            label          = "ljets_ge4j_ge4t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==7))")
    interf_ljets_ge4j_ge4t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==7))","ljets_ge4j_ge4t_tHW_node","")
    interf_ljets_ge4j_ge4t_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_tHW_node.bin_edges = [ 
				0.13,
				0.188,
				0.246,
				0.304,
				0.362,
				0.42,
				0.536,
				1.0
				]
    interf_ljets_ge4j_ge4t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_tHW_node)
    


    # plots for ge4j_3t

    interf_ljets_ge4j_3t_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttHbb",
                                            label          = "ljets_ge4j_3t_ttHbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))")
    interf_ljets_ge4j_3t_ttHbb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttHbb_node","")
    interf_ljets_ge4j_3t_ttHbb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttHbb_node.bin_edges = [ 
				0.13,
				0.1667,
				0.2033,
				0.24,
				0.2767,
				0.3133,
				0.35,
				0.3867,
				0.4233,
				0.68
				]
    interf_ljets_ge4j_3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttHbb_node)
    
    interf_ljets_ge4j_3t_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttHnonbb",
                                            label          = "ljets_ge4j_3t_ttHnonbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))")
    interf_ljets_ge4j_3t_ttHnonbb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttHnonbb_node","")
    interf_ljets_ge4j_3t_ttHnonbb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttHnonbb_node.bin_edges = [ 
				0.13,
				0.148,
				0.166,
				0.184,
				0.202,
				0.22,
				0.238,
				0.256,
				0.274,
				0.4
				]
    interf_ljets_ge4j_3t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttHnonbb_node)
    
    interf_ljets_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttmb",
                                            label          = "ljets_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))")
    interf_ljets_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_ttmb_node","")
    interf_ljets_ge4j_3t_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttmb_node.bin_edges = [ 
				0.1427,
				0.1553,
				0.168,
				0.1807,
				0.1933,
				0.206,
				0.2187,
				0.2313,
				0.244,
				0.2567,
				0.2693,
				0.32
				]
    interf_ljets_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttmb_node)
    
    interf_ljets_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_tt2b",
                                            label          = "ljets_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))")
    interf_ljets_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_tt2b_node","")
    interf_ljets_ge4j_3t_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_tt2b_node.bin_edges = [ 
				0.13,
				# 0.1613,
				# 0.1927,
				# 0.224,
				# 0.2553,
				# 0.2867,
				# 0.318,
				0.6
				]
    interf_ljets_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_tt2b_node)
    
    interf_ljets_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttcc",
                                            label          = "ljets_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))")
    interf_ljets_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttcc_node","")
    interf_ljets_ge4j_3t_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttcc_node.bin_edges = [ 
				0.13,
				# 0.1533,
				# 0.1767,
				# 0.2,
				# 0.2233,
				# 0.2467,
				# 0.27,
				# 0.2933,
				# 0.3167,
				# 0.34,
				# 0.3633,
				# 0.3867,
				0.48
				]
    interf_ljets_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttcc_node)
    
    interf_ljets_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttlf",
                                            label          = "ljets_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==5))")
    interf_ljets_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==5))","ljets_ge4j_3t_ttlf_node","")
    interf_ljets_ge4j_3t_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttlf_node.bin_edges = [ 
				0.13,
				# 0.1667,
				# 0.2033,
				# 0.24,
				# 0.2767,
				# 0.3133,
				# 0.35,
				# 0.3867,
				# 0.4233,
				# 0.46,
				# 0.4967,
				# 0.5333,
				# 0.57,
				0.68
				]
    interf_ljets_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttlf_node)
    
    interf_ljets_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_tHq",
                                            label          = "ljets_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==6))")
    interf_ljets_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==6))","ljets_ge4j_3t_tHq_node","")
    interf_ljets_ge4j_3t_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_tHq_node.bin_edges = [ 
				0.13,
				0.184,
				0.238,
				0.292,
				0.346,
				0.4,
				0.454,
				0.508,
				0.562,
				0.616,
				0.67,
				0.724,
				0.778,
				0.94
				]
    interf_ljets_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_tHq_node)
    
    interf_ljets_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_tHW",
                                            label          = "ljets_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==7))")
    interf_ljets_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==7))","ljets_ge4j_3t_tHW_node","")
    interf_ljets_ge4j_3t_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_tHW_node.bin_edges = [ 
				0.13,
				0.188,
				0.246,
				0.304,
				0.362,
				0.42,
				0.478,
				0.536,
				0.594,
				0.652,
				0.71,
				0.768,
				0.884,
				1.0
				]
    interf_ljets_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_tHW_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge4t(data)
    discriminatorPlots += plots_ge4j_3t(data)
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
    