
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



def plots_ge4j_ge4t_classification(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_CSV_2","CSV[2]",50,0.277,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_HT_tags","Evt_HT_tags",50,100.0,1000.0),"Evt_HT_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_Pt_TaggedJetsAverage","Evt_Pt_TaggedJetsAverage",50,30.0,600.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_tHW_energy_fraction",50,-1.5,1.0),"Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Reco_JABDT_tHq_abs_ljet_eta","Reco_JABDT_tHq_abs_ljet_eta",50,-1.5,4.5),"Reco_JABDT_tHq_abs_ljet_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Reco_ttH_bestJABDToutput","Reco_ttH_bestJABDToutput",50,-1.0,0.7),"Reco_ttH_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Reco_ttH_toplep_m","Reco_ttH_toplep_m",50,-1.5,750.0),"Reco_ttH_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_Reco_ttbar_bestJABDToutput","Reco_ttbar_bestJABDToutput",50,-0.4,0.7),"Reco_ttbar_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_classification_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots

def plots_ge4j_ge4t_STXSnet(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",50.0,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50.0,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50.0,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Evt_Pt_TaggedJetsAverage","Evt_Pt_TaggedJetsAverage",50.0,30.0,600.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50.0,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Reco_JABDT_tHW_log_h_pt","nan",nan,nan,nan),"Reco_JABDT_tHW_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Reco_JABDT_tHq_log_h_pt","nan",nan,nan,nan),"Reco_JABDT_tHq_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","nan",nan,nan,nan),"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Reco_JABDT_ttH_log_h_pt","nan",nan,nan,nan),"Reco_JABDT_ttH_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Reco_JABDT_ttH_log_toplep_m","Reco_JABDT_ttH_log_toplep_m",50.0,-1.5,7.5),"Reco_JABDT_ttH_log_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Reco_tHW_h_dr","nan",nan,nan,nan),"Reco_tHW_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Reco_tHW_h_pt","nan",nan,nan,nan),"Reco_tHW_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Reco_tHq_h_pt","nan",nan,nan,nan),"Reco_tHq_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Reco_ttH_h_dr","nan",nan,nan,nan),"Reco_ttH_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_Reco_ttH_h_m","nan",nan,nan,nan),"Reco_ttH_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_STXSnet_memDBp","MEM",50.0,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_ge4j_3t_classification(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_Evt_CSV_dev","Evt_CSV_dev",50,0.0,0.25),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_Evt_HT_jets","H_{T}(jets)",50,200.0,1500.0),"Evt_HT_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_Evt_M_JetsAverage","Evt_M_JetsAverage",50,5.0,50.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_Evt_M_Total","Evt_M_Total",50,200.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_Reco_ttH_bestJABDToutput","Reco_ttH_bestJABDToutput",50,-1.0,0.7),"Reco_ttH_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_Reco_ttbar_bestJABDToutput","Reco_ttbar_bestJABDToutput",50,-0.4,0.7),"Reco_ttbar_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_classification_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots

def plots_ge4j_3t_STXSnet(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",50.0,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50.0,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Evt_Pt_TaggedJetsAverage","Evt_Pt_TaggedJetsAverage",50.0,30.0,600.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Reco_JABDT_tHW_log_h_m","nan",nan,nan,nan),"Reco_JABDT_tHW_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Reco_JABDT_tHW_log_h_pt","nan",nan,nan,nan),"Reco_JABDT_tHW_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Reco_JABDT_tHq_log_h_m","nan",nan,nan,nan),"Reco_JABDT_tHq_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Reco_JABDT_tHq_log_h_pt","nan",nan,nan,nan),"Reco_JABDT_tHq_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","nan",nan,nan,nan),"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Reco_tHW_h_pt","nan",nan,nan,nan),"Reco_tHW_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Reco_tHq_h_pt","nan",nan,nan,nan),"Reco_tHq_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_Reco_ttH_h_dr","nan",nan,nan,nan),"Reco_ttH_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_STXSnet_memDBp","MEM",50.0,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots

def plots_dnn_ttH_vs_slike_STXS(data, discrname, cat_classifier, cat_stxs, stxsproc, index, selection, label):
    ndefaultbins = 50
    interfaces = []

    # interf_ttH_vs_slike = vhi.variableHistoInterface(variable_name  = "(DNNOutput_{cat}_node_ttH/(DNNOutput_{cat}_node_ttH + DNNOutput_{cat}_node_ttmb + DNNOutput_{cat}_node_tt2b))*DNNOutput_{cat_stxs}_node_{stxsproc}".format(cat = cat_classifier, cat_stxs = cat_stxs, stxsproc = stxsproc),
    #                                         label          = "ljets_{cat}_ttH_vs_slike_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),
    #                                         selection      = "")
    # interf_ttH_vs_slike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==0)&&(DNNPredictedClass_{cat_stxs}=={index}))".format(cat = cat_classifier, cat_stxs = cat_stxs, sel = selection, index = str(index)),"ljets_{cat}_ttH_vs_slike_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),"")
    # interf_ttH_vs_slike.category_label = label
    # interf_ttH_vs_slike.minxval = 0.2
    # interf_ttH_vs_slike.maxxval = 1.0
    # interf_ttH_vs_slike.nhistobins = ndefaultbins
    # interfaces.append(interf_ttH_vs_slike)


    interf_ttH_ttmb_vs_slike = vhi.variableHistoInterface(variable_name  = "(DNNOutput_{cat}_node_ttH/(DNNOutput_{cat}_node_ttH + DNNOutput_{cat}_node_ttmb + DNNOutput_{cat}_node_tt2b))*DNNOutput_{cat_stxs}_node_{stxsproc}".format(cat = cat_classifier, cat_stxs = cat_stxs, stxsproc = stxsproc),
                                            label          = "ljets_{cat}_ttH_ttmb_vs_slike_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),
                                            selection      = "")
    interf_ttH_ttmb_vs_slike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==0 || DNNPredictedClass_{cat}==1)&&(DNNPredictedClass_{cat_stxs}=={index}))".format(cat = cat_classifier, sel = selection, cat_stxs = cat_stxs, index = str(index)),"ljets_{cat}_ttH_ttmb_vs_slike_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),"")
    interf_ttH_ttmb_vs_slike.category_label = label
    interf_ttH_ttmb_vs_slike.minxval = 0.0
    interf_ttH_ttmb_vs_slike.maxxval = 0.8
    interf_ttH_ttmb_vs_slike.nhistobins = ndefaultbins
    interfaces.append(interf_ttH_ttmb_vs_slike)

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots	

def plots_dnn_ttH_times_STXS(data, discrname, cat_classifier, cat_stxs, stxsproc, index, selection, label):
    ndefaultbins = 50
    interfaces = []

    interf_ttH_times_STXS = vhi.variableHistoInterface(variable_name  = "(DNNOutput_{cat}_node_ttH)*DNNOutput_{cat_stxs}_node_{stxsproc}".format(cat = cat_classifier, cat_stxs = cat_stxs, stxsproc = stxsproc),
                                            label          = "ljets_{cat}_ttH_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),
                                            selection      = "")
    interf_ttH_times_STXS.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==0)&&(DNNPredictedClass_{cat_stxs}=={index}))".format(cat = cat_classifier, sel = selection, cat_stxs = cat_stxs, index = str(index)),"ljets_{cat}_ttH_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),"")
    interf_ttH_times_STXS.category_label = label
    interf_ttH_times_STXS.minxval = 0.0
    interf_ttH_times_STXS.maxxval = 0.8
    interf_ttH_times_STXS.nhistobins = ndefaultbins
    interfaces.append(interf_ttH_times_STXS)

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots	


def plots_dnn(data, discrname):

    ndefaultbins = 50
    interfaces = []
    # plots for ge4j_ge4t_STXSnet

    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_STXSnet_node_ttHbb_STXS_0",
    #                                         label          = "ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_0_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXSnet==0))")
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_0_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXSnet==0))","ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_0_node","")
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_0_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_0_node.minxval = 0.2
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_0_node.maxxval = 0.99
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_0_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_0_node)
    
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_STXSnet_node_ttHbb_STXS_1",
    #                                         label          = "ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_1_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXSnet==1))")
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_1_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXSnet==1))","ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_1_node","")
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_1_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_1_node.minxval = 0.2
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_1_node.maxxval = 0.66
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_1_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_1_node)
    
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_STXSnet_node_ttHbb_STXS_2",
    #                                         label          = "ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_2_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXSnet==2))")
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_2_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXSnet==2))","ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_2_node","")
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_2_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_2_node.minxval = 0.2
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_2_node.maxxval = 0.85
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_2_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_2_node)
    
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_STXSnet_node_ttHbb_STXS_3",
    #                                         label          = "ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_3_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXSnet==3))")
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_3_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXSnet==3))","ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_3_node","")
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_3_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_3_node.minxval = 0.2
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_3_node.maxxval = 0.96
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_3_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_3_node)
    
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_STXSnet_node_ttHbb_STXS_4",
    #                                         label          = "ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_4_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXSnet==4))")
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_4_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_STXSnet==4))","ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_4_node","")
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_4_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_4_node.minxval = 0.2
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_4_node.maxxval = 1.0
    # interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_4_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_ge4t_STXSnet_ttHbb_STXS_4_node)



    # # plots for ge4j_3t_STXSnet

    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_STXSnet_node_ttHbb_STXS_0",
    #                                         label          = "ljets_ge4j_3t_STXSnet_ttHbb_STXS_0_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXSnet==0))")
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_0_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXSnet==0))","ljets_ge4j_3t_STXSnet_ttHbb_STXS_0_node","")
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_0_node.category_label = "\geq 4 jets, 3 b-tags"
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_0_node.minxval = 0.2
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_0_node.maxxval = 0.93
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_0_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_0_node)
    
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_STXSnet_node_ttHbb_STXS_1",
    #                                         label          = "ljets_ge4j_3t_STXSnet_ttHbb_STXS_1_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXSnet==1))")
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_1_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXSnet==1))","ljets_ge4j_3t_STXSnet_ttHbb_STXS_1_node","")
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_1_node.category_label = "\geq 4 jets, 3 b-tags"
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_1_node.minxval = 0.2
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_1_node.maxxval = 0.81
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_1_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_1_node)
    
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_STXSnet_node_ttHbb_STXS_2",
    #                                         label          = "ljets_ge4j_3t_STXSnet_ttHbb_STXS_2_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXSnet==2))")
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_2_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXSnet==2))","ljets_ge4j_3t_STXSnet_ttHbb_STXS_2_node","")
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_2_node.category_label = "\geq 4 jets, 3 b-tags"
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_2_node.minxval = 0.2
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_2_node.maxxval = 0.9
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_2_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_2_node)
    
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_STXSnet_node_ttHbb_STXS_3",
    #                                         label          = "ljets_ge4j_3t_STXSnet_ttHbb_STXS_3_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXSnet==3))")
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_3_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXSnet==3))","ljets_ge4j_3t_STXSnet_ttHbb_STXS_3_node","")
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_3_node.category_label = "\geq 4 jets, 3 b-tags"
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_3_node.minxval = 0.2
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_3_node.maxxval = 0.96
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_3_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_3_node)
    
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_STXSnet_node_ttHbb_STXS_4",
    #                                         label          = "ljets_ge4j_3t_STXSnet_ttHbb_STXS_4_node",
    #                                         selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXSnet==4))")
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_4_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_STXSnet==4))","ljets_ge4j_3t_STXSnet_ttHbb_STXS_4_node","")
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_4_node.category_label = "\geq 4 jets, 3 b-tags"
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_4_node.minxval = 0.2
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_4_node.maxxval = 0.99
    # interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_4_node.nhistobins = ndefaultbins
    # interfaces.append(interf_ljets_ge4j_3t_STXSnet_ttHbb_STXS_4_node)



    # plots for ge4j_ge4t_classification

    interf_ljets_ge4j_ge4t_classification_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_ttH",
                                            label          = "ljets_ge4j_ge4t_classification_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==0))")
    interf_ljets_ge4j_ge4t_classification_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==0))","ljets_ge4j_ge4t_classification_ttH_node","")
    interf_ljets_ge4j_ge4t_classification_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_ttH_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_classification_ttH_node.maxxval = 0.88
    interf_ljets_ge4j_ge4t_classification_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_ttH_node)
    
    interf_ljets_ge4j_ge4t_classification_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_classification_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==1))")
    interf_ljets_ge4j_ge4t_classification_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==1))","ljets_ge4j_ge4t_classification_ttmb_node","")
    interf_ljets_ge4j_ge4t_classification_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_classification_ttmb_node.maxxval = 0.79
    interf_ljets_ge4j_ge4t_classification_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_ttmb_node)
    
    interf_ljets_ge4j_ge4t_classification_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_classification_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==2))")
    interf_ljets_ge4j_ge4t_classification_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==2))","ljets_ge4j_ge4t_classification_tt2b_node","")
    interf_ljets_ge4j_ge4t_classification_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_classification_tt2b_node.maxxval = 0.71
    interf_ljets_ge4j_ge4t_classification_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_classification_tt2b_node)
    
    interf_ljets_ge4j_ge4t_classification_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_classification_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==3))")
    interf_ljets_ge4j_ge4t_classification_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==3))","ljets_ge4j_ge4t_classification_ttcc_node","")
    interf_ljets_ge4j_ge4t_classification_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_classification_ttcc_node.maxxval = 0.51
    interf_ljets_ge4j_ge4t_classification_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_classification_ttcc_node)
    
    interf_ljets_ge4j_ge4t_classification_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_classification_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==4))")
    interf_ljets_ge4j_ge4t_classification_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==4))","ljets_ge4j_ge4t_classification_ttlf_node","")
    interf_ljets_ge4j_ge4t_classification_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_classification_ttlf_node.maxxval = 0.78
    interf_ljets_ge4j_ge4t_classification_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_classification_ttlf_node)
    
    interf_ljets_ge4j_ge4t_classification_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_tHq",
                                            label          = "ljets_ge4j_ge4t_classification_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==5))")
    interf_ljets_ge4j_ge4t_classification_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==5))","ljets_ge4j_ge4t_classification_tHq_node","")
    interf_ljets_ge4j_ge4t_classification_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_tHq_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_classification_tHq_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_classification_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_tHq_node)
    
    interf_ljets_ge4j_ge4t_classification_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_tHW",
                                            label          = "ljets_ge4j_ge4t_classification_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_classification_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_classification_tHW_node","")
    interf_ljets_ge4j_ge4t_classification_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_tHW_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_classification_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_classification_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_tHW_node)
    
    # plots for ge4j_3t_classification

    interf_ljets_ge4j_3t_classification_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_ttH",
                                            label          = "ljets_ge4j_3t_classification_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==0))")
    interf_ljets_ge4j_3t_classification_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==0))","ljets_ge4j_3t_classification_ttH_node","")
    interf_ljets_ge4j_3t_classification_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_ttH_node.minxval = 0.14
    interf_ljets_ge4j_3t_classification_ttH_node.maxxval = 0.96
    interf_ljets_ge4j_3t_classification_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_ttH_node)
    
    interf_ljets_ge4j_3t_classification_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_ttmb",
                                            label          = "ljets_ge4j_3t_classification_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==1))")
    interf_ljets_ge4j_3t_classification_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==1))","ljets_ge4j_3t_classification_ttmb_node","")
    interf_ljets_ge4j_3t_classification_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_3t_classification_ttmb_node.maxxval = 0.46
    interf_ljets_ge4j_3t_classification_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_ttmb_node)
    
    interf_ljets_ge4j_3t_classification_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_tt2b",
                                            label          = "ljets_ge4j_3t_classification_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==2))")
    interf_ljets_ge4j_3t_classification_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==2))","ljets_ge4j_3t_classification_tt2b_node","")
    interf_ljets_ge4j_3t_classification_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_3t_classification_tt2b_node.maxxval = 0.62
    interf_ljets_ge4j_3t_classification_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_classification_tt2b_node)
    
    interf_ljets_ge4j_3t_classification_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_ttcc",
                                            label          = "ljets_ge4j_3t_classification_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==3))")
    interf_ljets_ge4j_3t_classification_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==3))","ljets_ge4j_3t_classification_ttcc_node","")
    interf_ljets_ge4j_3t_classification_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_3t_classification_ttcc_node.maxxval = 0.44
    interf_ljets_ge4j_3t_classification_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_classification_ttcc_node)
    
    interf_ljets_ge4j_3t_classification_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_ttlf",
                                            label          = "ljets_ge4j_3t_classification_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==4))")
    interf_ljets_ge4j_3t_classification_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==4))","ljets_ge4j_3t_classification_ttlf_node","")
    interf_ljets_ge4j_3t_classification_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_3t_classification_ttlf_node.maxxval = 0.84
    interf_ljets_ge4j_3t_classification_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_classification_ttlf_node)
    
    interf_ljets_ge4j_3t_classification_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_tHq",
                                            label          = "ljets_ge4j_3t_classification_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==5))")
    interf_ljets_ge4j_3t_classification_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==5))","ljets_ge4j_3t_classification_tHq_node","")
    interf_ljets_ge4j_3t_classification_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_tHq_node.minxval = 0.14
    interf_ljets_ge4j_3t_classification_tHq_node.maxxval = 0.98
    interf_ljets_ge4j_3t_classification_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_tHq_node)
    
    interf_ljets_ge4j_3t_classification_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_tHW",
                                            label          = "ljets_ge4j_3t_classification_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_classification_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_classification_tHW_node","")
    interf_ljets_ge4j_3t_classification_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_tHW_node.minxval = 0.14
    interf_ljets_ge4j_3t_classification_tHW_node.maxxval = 0.99
    interf_ljets_ge4j_3t_classification_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_tHW_node)
  

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    # input variables
    # discriminatorPlots += plots_ge4j_ge4t_classification(data)
    # discriminatorPlots += plots_ge4j_3t_classification(data)
    # discriminatorPlots += plots_ge4j_ge4t_STXSnet(data)
    # discriminatorPlots += plots_ge4j_3t_STXSnet(data)plots_ge4j_3t_STXSnet

    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"
    # STXS
    discriminatorPlots += plots_dnn_ttH_times_STXS(data = data, discrname=discrname, cat_classifier="ge4j_3t_classification", cat_stxs = "ge4j_3t_STXSnet", stxsproc = "ttHbb_STXS_0", index = 0, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_times_STXS(data = data, discrname=discrname, cat_classifier="ge4j_3t_classification", cat_stxs = "ge4j_3t_STXSnet", stxsproc = "ttHbb_STXS_1", index = 1, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_times_STXS(data = data, discrname=discrname, cat_classifier="ge4j_3t_classification", cat_stxs = "ge4j_3t_STXSnet", stxsproc = "ttHbb_STXS_2", index = 2, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_times_STXS(data = data, discrname=discrname, cat_classifier="ge4j_3t_classification", cat_stxs = "ge4j_3t_STXSnet", stxsproc = "ttHbb_STXS_3", index = 3, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_times_STXS(data = data, discrname=discrname, cat_classifier="ge4j_3t_classification", cat_stxs = "ge4j_3t_STXSnet", stxsproc = "ttHbb_STXS_4", index = 4, selection = selection, label = label )


    # discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge4j_3t_classification", cat_stxs = "ge4j_3t_STXSnet", stxsproc = "ttHbb_STXS_0", index = 0, selection = selection, label = label )
    # discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge4j_3t_classification", cat_stxs = "ge4j_3t_STXSnet", stxsproc = "ttHbb_STXS_1", index = 1, selection = selection, label = label )
    # discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge4j_3t_classification", cat_stxs = "ge4j_3t_STXSnet", stxsproc = "ttHbb_STXS_2", index = 2, selection = selection, label = label )
    # discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge4j_3t_classification", cat_stxs = "ge4j_3t_STXSnet", stxsproc = "ttHbb_STXS_3", index = 3, selection = selection, label = label )
    # discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge4j_3t_classification", cat_stxs = "ge4j_3t_STXSnet", stxsproc = "ttHbb_STXS_4", index = 4, selection = selection, label = label )



    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)"
    # STXS
    discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge4j_ge4t_classification", cat_stxs = "ge4j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_0", index = 0, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge4j_ge4t_classification", cat_stxs = "ge4j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_1", index = 1, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge4j_ge4t_classification", cat_stxs = "ge4j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_2", index = 2, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge4j_ge4t_classification", cat_stxs = "ge4j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_3", index = 3, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge4j_ge4t_classification", cat_stxs = "ge4j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_4", index = 4, selection = selection, label = label )


    # standard classifiers
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
    
