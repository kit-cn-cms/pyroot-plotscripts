
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



def plots_top10_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_HT_jets","Evt_HT_jets",50,0.0,2000.0),"Evt_HT_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_N_BTagsM","N_BTagsM",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_Dr_minDrTaggedJets","Evt_Dr_minDrTaggedJets",50,0.,4.),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_CSV","CSV",50,0.,1.0),"CSV",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_top10_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_HT_jets","Evt_HT_jets",50,0.0,2000.0),"Evt_HT_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_N_BTagsM","N_BTagsM",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_Dr_minDrTaggedJets","Evt_Dr_minDrTaggedJets",50,0.,4.),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_CSV","CSV",50,0.,1.0),"CSV",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_dnn(data, discrname):

    ndefaultbins = 15
    interfaces = []

    # plots for top10_ge4j_ge4t

    interf_ljets_top10_ge4j_ge4t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttH",
                                            label          = "ljets_top10_ge4j_ge4t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0))")
    interf_ljets_top10_ge4j_ge4t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0))","ljets_top10_ge4j_ge4t_ttH_node","")
    interf_ljets_top10_ge4j_ge4t_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttH_node.bin_edges = [ 
                0.207,
                0.2517,
                0.2963,
                0.341,
                0.3857,
                0.4303,
                0.475,
                0.5197,
                0.5643,
                0.609,
                0.81
                ]
    interf_ljets_top10_ge4j_ge4t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttH_node)
    
    interf_ljets_top10_ge4j_ge4t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttmb",
                                            label          = "ljets_top10_ge4j_ge4t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==1))")
    interf_ljets_top10_ge4j_ge4t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==1))","ljets_top10_ge4j_ge4t_ttmb_node","")
    interf_ljets_top10_ge4j_ge4t_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttmb_node.bin_edges = [ 
                0.2133,
                0.25,
                0.2867,
                0.3233,
                0.36,
                0.3967,
                0.4333,
                0.47,
                0.69
                ]
    interf_ljets_top10_ge4j_ge4t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttmb_node)
    
    interf_ljets_top10_ge4j_ge4t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_top10_ge4j_ge4t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==2))")
    interf_ljets_top10_ge4j_ge4t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==2))","ljets_top10_ge4j_ge4t_tt2b_node","")
    interf_ljets_top10_ge4j_ge4t_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_tt2b_node.bin_edges = [ 
                0.198,
                # 0.2173,
                # 0.2367,
                # 0.256,
                # 0.2753,
                # 0.2947,
                # 0.314,
                # 0.3333,
                # 0.3527,
                # 0.372,
                # 0.3913,
                # 0.43,
                # 0.4687,
                0.72
                ]
    interf_ljets_top10_ge4j_ge4t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_tt2b_node)
    
    interf_ljets_top10_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_top10_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==3))")
    interf_ljets_top10_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==3))","ljets_top10_ge4j_ge4t_ttcc_node","")
    interf_ljets_top10_ge4j_ge4t_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttcc_node.bin_edges = [ 
                0.1933,
                # 0.2147,
                # 0.2253,
                # 0.236,
                # 0.2467,
                # 0.2573,
                # 0.268,
                # 0.2787,
                # 0.2893,
                # 0.3,
                # 0.3107,
                # 0.3213,
                # 0.332,
                # 0.3427,
                # 0.3533,
                # 0.364,
                # 0.3747,
                # 0.3853,
                # 0.4067,
                0.46
                ]
    interf_ljets_top10_ge4j_ge4t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttcc_node)
    
    interf_ljets_top10_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_top10_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==4))")
    interf_ljets_top10_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==4))","ljets_top10_ge4j_ge4t_ttlf_node","")
    interf_ljets_top10_ge4j_ge4t_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttlf_node.bin_edges = [ 
                0.199,
                # 0.2187,
                # 0.2383,
                # 0.258,
                # 0.2777,
                # 0.2973,
                # 0.317,
                # 0.3367,
                # 0.3563,
                # 0.376,
                # 0.3957,
                # 0.4153,
                # 0.435,
                # 0.4547,
                # 0.4743,
                # 0.494,
                # 0.5137,
                # 0.5333,
                # 0.553,
                # 0.5727,
                # 0.5923,
                # 0.612,
                # 0.6513,
                0.73
                ]
    interf_ljets_top10_ge4j_ge4t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttlf_node)
    
    interf_ljets_top10_ge4j_ge4t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_tHq",
                                            label          = "ljets_top10_ge4j_ge4t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==5))")
    interf_ljets_top10_ge4j_ge4t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==5))","ljets_top10_ge4j_ge4t_tHq_node","")
    interf_ljets_top10_ge4j_ge4t_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_tHq_node.bin_edges = [ 
                0.225,
                0.2817,
                0.3383,
                0.395,
                0.4517,
                0.5083,
                0.565,
                0.6217,
                0.6783,
                0.735,
                0.99
                ]
    interf_ljets_top10_ge4j_ge4t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_tHq_node)
    
    interf_ljets_top10_ge4j_ge4t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_tHW",
                                            label          = "ljets_top10_ge4j_ge4t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==6))")
    interf_ljets_top10_ge4j_ge4t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==6))","ljets_top10_ge4j_ge4t_tHW_node","")
    interf_ljets_top10_ge4j_ge4t_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_tHW_node.bin_edges = [ 
                0.226,
                0.2833,
                0.3407,
                0.398,
                0.4553,
                0.5127,
                0.57,
                0.6847,
                1.0
                ]
    interf_ljets_top10_ge4j_ge4t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_tHW_node)
    


    # plots for top10_ge4j_3t

    interf_ljets_top10_ge4j_3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttH",
                                            label          = "ljets_top10_ge4j_3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0))")
    interf_ljets_top10_ge4j_3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0))","ljets_top10_ge4j_3t_ttH_node","")
    interf_ljets_top10_ge4j_3t_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttH_node.bin_edges = [ 
                0.178,
                0.216,
                0.254,
                0.292,
                0.33,
                0.368,
                0.406,
                0.444,
                0.482,
                0.52,
                0.558,
                0.71
                ]
    interf_ljets_top10_ge4j_3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttH_node)
    
    interf_ljets_top10_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttmb",
                                            label          = "ljets_top10_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==1))")
    interf_ljets_top10_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==1))","ljets_top10_ge4j_3t_ttmb_node","")
    interf_ljets_top10_ge4j_3t_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttmb_node.bin_edges = [ 
                0.172,
                0.1933,
                0.2147,
                0.236,
                0.2573,
                0.2787,
                0.3,
                0.3213,
                0.3427,
                0.364,
                0.3853,
                0.46
                ]
    interf_ljets_top10_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttmb_node)
    
    interf_ljets_top10_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_tt2b",
                                            label          = "ljets_top10_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==2))")
    interf_ljets_top10_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==2))","ljets_top10_ge4j_3t_tt2b_node","")
    interf_ljets_top10_ge4j_3t_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_tt2b_node.bin_edges = [ 
                0.1793,
                # 0.199,
                # 0.2187,
                # 0.2383,
                # 0.258,
                # 0.2777,
                # 0.2973,
                # 0.317,
                # 0.3367,
                # 0.3563,
                # 0.376,
                # 0.3957,
                # 0.4153,
                # 0.435,
                # 0.4547,
                # 0.4743,
                # 0.494,
                # 0.5137,
                # 0.5333,
                # 0.553,
                # 0.5727,
                # 0.5923,
                # 0.612,
                0.73
                ]
    interf_ljets_top10_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_tt2b_node)
    
    interf_ljets_top10_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttcc",
                                            label          = "ljets_top10_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==3))")
    interf_ljets_top10_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==3))","ljets_top10_ge4j_3t_ttcc_node","")
    interf_ljets_top10_ge4j_3t_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttcc_node.bin_edges = [ 
                0.176,
                # 0.188,
                # 0.2,
                # 0.212,
                # 0.224,
                # 0.236,
                # 0.248,
                # 0.26,
                # 0.272,
                # 0.284,
                # 0.296,
                # 0.308,
                # 0.32,
                # 0.332,
                # 0.344,
                # 0.356,
                # 0.368,
                # 0.38,
                # 0.392,
                # 0.404,
                # 0.416,
                # 0.428,
                # 0.44,
                0.5
                ]
    interf_ljets_top10_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttcc_node)
    
    interf_ljets_top10_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttlf",
                                            label          = "ljets_top10_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==4))")
    interf_ljets_top10_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==4))","ljets_top10_ge4j_3t_ttlf_node","")
    interf_ljets_top10_ge4j_3t_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttlf_node.bin_edges = [ 
                0.1613,
                # 0.1827,
                # 0.204,
                # 0.2253,
                # 0.2467,
                # 0.268,
                # 0.2893,
                # 0.3107,
                # 0.332,
                # 0.3533,
                # 0.3747,
                # 0.396,
                # 0.4173,
                # 0.4387,
                # 0.46,
                # 0.4813,
                # 0.5027,
                # 0.524,
                # 0.5453,
                # 0.5667,
                # 0.588,
                # 0.6093,
                # 0.6307,
                # 0.652,
                # 0.6733,
                # 0.6947,
                # 0.716,
                # 0.7373,
                0.78
                ]
    interf_ljets_top10_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttlf_node)
    
    interf_ljets_top10_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_tHq",
                                            label          = "ljets_top10_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==5))")
    interf_ljets_top10_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==5))","ljets_top10_ge4j_3t_tHq_node","")
    interf_ljets_top10_ge4j_3t_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_tHq_node.bin_edges = [ 
                0.1683,
                0.225,
                0.2817,
                0.3383,
                0.395,
                0.4517,
                0.5083,
                0.565,
                0.6217,
                0.6783,
                0.735,
                0.7917,
                0.8483,
                0.99
                ]
    interf_ljets_top10_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_tHq_node)
    
    interf_ljets_top10_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_tHW",
                                            label          = "ljets_top10_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==6))")
    interf_ljets_top10_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==6))","ljets_top10_ge4j_3t_tHW_node","")
    interf_ljets_top10_ge4j_3t_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_tHW_node.bin_edges = [ 
                0.1687,
                0.226,
                0.2833,
                0.3407,
                0.398,
                0.4553,
                0.5127,
                0.57,
                0.6273,
                0.6847,
                0.742,
                0.7993,
                0.8567,
                0.914,
                1.0
                ]
    interf_ljets_top10_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_tHW_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    # discriminatorPlots += plots_top20_ge4j_ge4t(data)
    # discriminatorPlots += plots_top20_ge4j_3t(data)
    # discriminatorPlots += plots_top10_ge4j_ge4t(data)
    # discriminatorPlots += plots_top10_ge4j_3t(data)
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
    
