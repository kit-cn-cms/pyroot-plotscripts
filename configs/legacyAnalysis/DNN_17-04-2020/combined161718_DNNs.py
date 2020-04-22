
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



def plots_ge4j_ge4t_v2(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_CSV_2","CSV[2]",50,0.277,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Evt_M_minDrLepTag","Evt_M_minDrLepTag",50,15.0,400.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_JABDT_tHW_Jet_CSV_whaddau1","Reco_JABDT_tHW_Jet_CSV_whaddau1",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_tHW_energy_fraction",50,-1.5,1.0),"Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_JABDT_tHq_Jet_CSV_hdau1","Reco_JABDT_tHq_Jet_CSV_hdau1",50,-1.5,1.0),"Reco_JABDT_tHq_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_JABDT_tHq_abs_ljet_eta","Reco_JABDT_tHq_abs_ljet_eta",50,-1.5,4.5),"Reco_JABDT_tHq_abs_ljet_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_JABDT_ttH_Jet_CSV_hdau2","Reco_JABDT_ttH_Jet_CSV_hdau2",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_JABDT_ttbar_Jet_CSV_whaddau1","Reco_JABDT_ttbar_Jet_CSV_whaddau1",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_JABDT_ttbar_Jet_CSV_whaddau2","Reco_JABDT_ttbar_Jet_CSV_whaddau2",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_tHW_bestJABDToutput","Reco_tHW_bestJABDToutput",50,-1.0,0.6),"Reco_tHW_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v2_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,80.0,500.0),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_v1_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
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
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_HT_tags","Evt_HT_tags",50,100.0,1000.0),"Evt_HT_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_JetPt_over_JetE","Evt_JetPt_over_JetE",50,0.0,1.0),"Evt_JetPt_over_JetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M_JetsAverage","Evt_M_JetsAverage",50,5.0,50.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_h1","Evt_h1",50,-0.2,0.4),"Evt_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_tHW_log_wb_m","Reco_JABDT_tHW_log_wb_m",50,-1.5,8.5),"Reco_JABDT_tHW_log_wb_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep","Reco_JABDT_ttH_Jet_CSV_btoplep",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1","Reco_JABDT_ttbar_Jet_CSV_whaddau1",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1",selection,label),
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


    # plots for ge4j_ge4t_v2

    interf_ljets_ge4j_ge4t_v2_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v2_node_ttH",
                                            label          = "ljets_ge4j_ge4t_v2_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==0))")
    interf_ljets_ge4j_ge4t_v2_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==0))","ljets_ge4j_ge4t_v2_ttH_node","")
    interf_ljets_ge4j_ge4t_v2_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v2_ttH_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v2_ttH_node.maxxval = 0.75
    interf_ljets_ge4j_ge4t_v2_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v2_ttH_node)
    
    interf_ljets_ge4j_ge4t_v2_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v2_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_v2_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==1))")
    interf_ljets_ge4j_ge4t_v2_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==1))","ljets_ge4j_ge4t_v2_ttmb_node","")
    interf_ljets_ge4j_ge4t_v2_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v2_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v2_ttmb_node.maxxval = 0.54
    interf_ljets_ge4j_ge4t_v2_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v2_ttmb_node)
    
    interf_ljets_ge4j_ge4t_v2_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v2_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_v2_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==2))")
    interf_ljets_ge4j_ge4t_v2_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==2))","ljets_ge4j_ge4t_v2_tt2b_node","")
    interf_ljets_ge4j_ge4t_v2_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v2_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v2_tt2b_node.maxxval = 0.72
    interf_ljets_ge4j_ge4t_v2_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v2_tt2b_node)
    
    interf_ljets_ge4j_ge4t_v2_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v2_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_v2_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==3))")
    interf_ljets_ge4j_ge4t_v2_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==3))","ljets_ge4j_ge4t_v2_ttcc_node","")
    interf_ljets_ge4j_ge4t_v2_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v2_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v2_ttcc_node.maxxval = 0.51
    interf_ljets_ge4j_ge4t_v2_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v2_ttcc_node)
    
    interf_ljets_ge4j_ge4t_v2_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v2_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_v2_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==4))")
    interf_ljets_ge4j_ge4t_v2_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==4))","ljets_ge4j_ge4t_v2_ttlf_node","")
    interf_ljets_ge4j_ge4t_v2_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v2_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v2_ttlf_node.maxxval = 0.59
    interf_ljets_ge4j_ge4t_v2_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v2_ttlf_node)
    
    interf_ljets_ge4j_ge4t_v2_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v2_node_tHq",
                                            label          = "ljets_ge4j_ge4t_v2_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==5))")
    interf_ljets_ge4j_ge4t_v2_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==5))","ljets_ge4j_ge4t_v2_tHq_node","")
    interf_ljets_ge4j_ge4t_v2_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v2_tHq_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v2_tHq_node.maxxval = 0.98
    interf_ljets_ge4j_ge4t_v2_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v2_tHq_node)
    
    interf_ljets_ge4j_ge4t_v2_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v2_node_tHW",
                                            label          = "ljets_ge4j_ge4t_v2_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==6))")
    interf_ljets_ge4j_ge4t_v2_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v2==6))","ljets_ge4j_ge4t_v2_tHW_node","")
    interf_ljets_ge4j_ge4t_v2_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v2_tHW_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v2_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_v2_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v2_tHW_node)
    


    # plots for ge4j_3t

    interf_ljets_ge4j_3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttH",
                                            label          = "ljets_ge4j_3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))")
    interf_ljets_ge4j_3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttH_node","")
    interf_ljets_ge4j_3t_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttH_node.minxval = 0.14
    interf_ljets_ge4j_3t_ttH_node.maxxval = 0.67
    interf_ljets_ge4j_3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_node)
    
    interf_ljets_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttmb",
                                            label          = "ljets_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))")
    interf_ljets_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttmb_node","")
    interf_ljets_ge4j_3t_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_3t_ttmb_node.maxxval = 0.39
    interf_ljets_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttmb_node)
    
    interf_ljets_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_tt2b",
                                            label          = "ljets_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))")
    interf_ljets_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tt2b_node","")
    interf_ljets_ge4j_3t_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_3t_tt2b_node.maxxval = 0.89
    interf_ljets_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_tt2b_node)
    
    interf_ljets_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttcc",
                                            label          = "ljets_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))")
    interf_ljets_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttcc_node","")
    interf_ljets_ge4j_3t_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_3t_ttcc_node.maxxval = 0.62
    interf_ljets_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttcc_node)
    
    interf_ljets_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttlf",
                                            label          = "ljets_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))")
    interf_ljets_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttlf_node","")
    interf_ljets_ge4j_3t_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_3t_ttlf_node.maxxval = 0.73
    interf_ljets_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttlf_node)
    
    interf_ljets_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_tHq",
                                            label          = "ljets_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==5))")
    interf_ljets_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==5))","ljets_ge4j_3t_tHq_node","")
    interf_ljets_ge4j_3t_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_tHq_node.minxval = 0.14
    interf_ljets_ge4j_3t_tHq_node.maxxval = 0.99
    interf_ljets_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_tHq_node)
    
    interf_ljets_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_tHW",
                                            label          = "ljets_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==6))")
    interf_ljets_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==6))","ljets_ge4j_3t_tHW_node","")
    interf_ljets_ge4j_3t_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_tHW_node.minxval = 0.14
    interf_ljets_ge4j_3t_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_tHW_node)
    


    # plots for ge4j_ge4t_v1

    interf_ljets_ge4j_ge4t_v1_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v1_node_ttH",
                                            label          = "ljets_ge4j_ge4t_v1_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==0))")
    interf_ljets_ge4j_ge4t_v1_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==0))","ljets_ge4j_ge4t_v1_ttH_node","")
    interf_ljets_ge4j_ge4t_v1_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v1_ttH_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v1_ttH_node.maxxval = 0.77
    interf_ljets_ge4j_ge4t_v1_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v1_ttH_node)
    
    interf_ljets_ge4j_ge4t_v1_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v1_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_v1_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==1))")
    interf_ljets_ge4j_ge4t_v1_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==1))","ljets_ge4j_ge4t_v1_ttmb_node","")
    interf_ljets_ge4j_ge4t_v1_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v1_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v1_ttmb_node.maxxval = 0.56
    interf_ljets_ge4j_ge4t_v1_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v1_ttmb_node)
    
    interf_ljets_ge4j_ge4t_v1_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v1_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_v1_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==2))")
    interf_ljets_ge4j_ge4t_v1_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==2))","ljets_ge4j_ge4t_v1_tt2b_node","")
    interf_ljets_ge4j_ge4t_v1_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v1_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v1_tt2b_node.maxxval = 0.59
    interf_ljets_ge4j_ge4t_v1_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v1_tt2b_node)
    
    interf_ljets_ge4j_ge4t_v1_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v1_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_v1_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==3))")
    interf_ljets_ge4j_ge4t_v1_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==3))","ljets_ge4j_ge4t_v1_ttcc_node","")
    interf_ljets_ge4j_ge4t_v1_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v1_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v1_ttcc_node.maxxval = 0.51
    interf_ljets_ge4j_ge4t_v1_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v1_ttcc_node)
    
    interf_ljets_ge4j_ge4t_v1_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v1_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_v1_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==4))")
    interf_ljets_ge4j_ge4t_v1_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==4))","ljets_ge4j_ge4t_v1_ttlf_node","")
    interf_ljets_ge4j_ge4t_v1_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v1_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v1_ttlf_node.maxxval = 0.67
    interf_ljets_ge4j_ge4t_v1_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v1_ttlf_node)
    
    interf_ljets_ge4j_ge4t_v1_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v1_node_tHq",
                                            label          = "ljets_ge4j_ge4t_v1_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==5))")
    interf_ljets_ge4j_ge4t_v1_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==5))","ljets_ge4j_ge4t_v1_tHq_node","")
    interf_ljets_ge4j_ge4t_v1_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v1_tHq_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v1_tHq_node.maxxval = 0.99
    interf_ljets_ge4j_ge4t_v1_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v1_tHq_node)
    
    interf_ljets_ge4j_ge4t_v1_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_v1_node_tHW",
                                            label          = "ljets_ge4j_ge4t_v1_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==6))")
    interf_ljets_ge4j_ge4t_v1_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_v1==6))","ljets_ge4j_ge4t_v1_tHW_node","")
    interf_ljets_ge4j_ge4t_v1_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_v1_tHW_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_v1_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_v1_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_v1_tHW_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge4t_v2(data)
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
    