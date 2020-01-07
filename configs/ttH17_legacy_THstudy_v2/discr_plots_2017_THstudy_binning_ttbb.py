
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

def plots_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"
    ndefaultbins = 50
    interfaces = []


    interf_ljets_ge4j_3t_Evt_HT = vhi.variableHistoInterface(variable_name  = "Evt_HT",
                                            category_label = label,
                                            label          = "ljets_ge4j_3t_Evt_HT")
    interf_ljets_ge4j_3t_Evt_HT.category = (selection,"ljets_ge4j_3t_Evt_HT","")

    interf_ljets_ge4j_3t_Evt_HT.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_Evt_HT.bin_edges = [200.0,230.0,260.0,290.0,320.0,350.0,380.0,410.0,440.0,470.0,500.0,530.0,560.0,590.0,620.0,650.0,680.0,710.0,740.0,770.0,800.0,830.0,860.0,890.0,920.0,950.0,980.0,1010.0,1040.0,1070.0,1100.0,1130.0,1160.0,1190.0,1220.0,1250.0,1280.0,1310.0,1340.0,1370.0,1400.0,1430.0,1460.0,1490.0,1520.0,1550.0,1580.0,1610.0,1640.0,1670.0,1700.0]
    interf_ljets_ge4j_3t_Evt_HT.histoname = "ljets_ge4j_3t_Evt_HT"
    interf_ljets_ge4j_3t_Evt_HT.histotitle = "H_{T}"
    interf_ljets_ge4j_3t_Evt_HT.selection = interf_ljets_ge4j_3t_Evt_HT.category[0]

    interfaces.append(interf_ljets_ge4j_3t_Evt_HT)

    interf_ljets_ge4j_3t_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            category_label = label,
                                            label          = "ljets_ge4j_3t_Evt_HT_jets")
    interf_ljets_ge4j_3t_Evt_HT_jets.category = (selection,"ljets_ge4j_3t_Evt_HT_jets","")

    interf_ljets_ge4j_3t_Evt_HT_jets.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_Evt_HT_jets.bin_edges = [200.0,226.0,252.0,278.0,304.0,330.0,356.0,382.0,408.0,434.0,460.0,486.0,512.0,538.0,564.0,590.0,616.0,642.0,668.0,694.0,720.0,746.0,772.0,798.0,824.0,850.0,876.0,902.0,928.0,954.0,980.0,1006.0,1032.0,1058.0,1084.0,1110.0,1136.0,1162.0,1188.0,1214.0,1240.0,1266.0,1292.0,1318.0,1344.0,1370.0,1396.0,1422.0,1448.0,1474.0,1500.0]
    interf_ljets_ge4j_3t_Evt_HT_jets.histoname = "ljets_ge4j_3t_Evt_HT_jets"
    interf_ljets_ge4j_3t_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge4j_3t_Evt_HT_jets.selection = interf_ljets_ge4j_3t_Evt_HT.category[0]

    interfaces.append(interf_ljets_ge4j_3t_Evt_HT_jets)

    interf_ljets_ge4j_3t_Evt_HT_wo_MET = vhi.variableHistoInterface(variable_name  = "Evt_HT_wo_MET",
                                            category_label = label,
                                            label          = "ljets_ge4j_3t_Evt_HT_wo_MET")
    interf_ljets_ge4j_3t_Evt_HT_wo_MET.category = (selection,"ljets_ge4j_3t_Evt_HT_wo_MET","")
    interf_ljets_ge4j_3t_Evt_HT_wo_MET.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_Evt_HT_wo_MET.bin_edges = [200.0,226.0,252.0,278.0,304.0,330.0,356.0,382.0,408.0,434.0,460.0,486.0,512.0,538.0,564.0,590.0,616.0,642.0,668.0,694.0,720.0,746.0,772.0,798.0,824.0,850.0,876.0,902.0,928.0,954.0,980.0,1006.0,1032.0,1058.0,1084.0,1110.0,1136.0,1162.0,1188.0,1214.0,1240.0,1266.0,1292.0,1318.0,1344.0,1370.0,1396.0,1422.0,1448.0,1474.0,1500.0]
    interf_ljets_ge4j_3t_Evt_HT_wo_MET.histoname = "ljets_ge4j_3t_Evt_HT_wo_MET"
    interf_ljets_ge4j_3t_Evt_HT_wo_MET.histotitle = "H_{T} without MET"
    interf_ljets_ge4j_3t_Evt_HT_wo_MET.selection = interf_ljets_ge4j_3t_Evt_HT_wo_MET.category[0]

    interfaces.append(interf_ljets_ge4j_3t_Evt_HT_wo_MET)
    
    plots = init_plots(interfaces = interfaces)
    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"
    ndefaultbins = 50
    interfaces = []


    interf_ljets_ge4j_ge4t_Evt_HT = vhi.variableHistoInterface(variable_name  = "Evt_HT",
                                            category_label = label,
                                            label          = "ljets_ge4j_ge4t_Evt_HT")
    interf_ljets_ge4j_ge4t_Evt_HT.category = (selection,"ljets_ge4j_ge4t_Evt_HT","")

    interf_ljets_ge4j_ge4t_Evt_HT.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_Evt_HT.bin_edges = [200.0,230.0,260.0,290.0,320.0,350.0,380.0,410.0,440.0,470.0,500.0,530.0,560.0,590.0,620.0,650.0,680.0,710.0,740.0,770.0,800.0,830.0,860.0,890.0,920.0,950.0,980.0,1010.0,1040.0,1070.0,1100.0,1130.0,1160.0,1190.0,1220.0,1250.0,1280.0,1310.0,1340.0,1370.0,1400.0,1430.0,1460.0,1490.0,1520.0,1550.0,1580.0,1610.0,1640.0,1670.0,1700.0]
    interf_ljets_ge4j_ge4t_Evt_HT.histoname = "ljets_ge4j_ge4t_Evt_HT"
    interf_ljets_ge4j_ge4t_Evt_HT.histotitle = "H_{T}"
    interf_ljets_ge4j_ge4t_Evt_HT.selection = interf_ljets_ge4j_ge4t_Evt_HT.category[0]

    interfaces.append(interf_ljets_ge4j_ge4t_Evt_HT)

    interf_ljets_ge4j_ge4t_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            category_label = label,
                                            label          = "ljets_ge4j_ge4t_Evt_HT_jets")
    interf_ljets_ge4j_ge4t_Evt_HT_jets.category = (selection,"ljets_ge4j_ge4t_Evt_HT_jets","")

    interf_ljets_ge4j_ge4t_Evt_HT_jets.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_Evt_HT_jets.bin_edges = [200.0,226.0,252.0,278.0,304.0,330.0,356.0,382.0,408.0,434.0,460.0,486.0,512.0,538.0,564.0,590.0,616.0,642.0,668.0,694.0,720.0,746.0,772.0,798.0,824.0,850.0,876.0,902.0,928.0,954.0,980.0,1006.0,1032.0,1058.0,1084.0,1110.0,1136.0,1162.0,1188.0,1214.0,1240.0,1266.0,1292.0,1318.0,1344.0,1370.0,1396.0,1422.0,1448.0,1474.0,1500.0]
    interf_ljets_ge4j_ge4t_Evt_HT_jets.histoname = "ljets_ge4j_ge4t_Evt_HT_jets"
    interf_ljets_ge4j_ge4t_Evt_HT_jets.histotitle = "H_{T}(jets)"
    interf_ljets_ge4j_ge4t_Evt_HT_jets.selection = interf_ljets_ge4j_ge4t_Evt_HT.category[0]

    interfaces.append(interf_ljets_ge4j_ge4t_Evt_HT_jets)

    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET = vhi.variableHistoInterface(variable_name  = "Evt_HT_wo_MET",
                                            category_label = label,
                                            label          = "ljets_ge4j_ge4t_Evt_HT_wo_MET")
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.category = (selection,"ljets_ge4j_ge4t_Evt_HT_wo_MET","")
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.bin_edges = [200.0,226.0,252.0,278.0,304.0,330.0,356.0,382.0,408.0,434.0,460.0,486.0,512.0,538.0,564.0,590.0,616.0,642.0,668.0,694.0,720.0,746.0,772.0,798.0,824.0,850.0,876.0,902.0,928.0,954.0,980.0,1006.0,1032.0,1058.0,1084.0,1110.0,1136.0,1162.0,1188.0,1214.0,1240.0,1266.0,1292.0,1318.0,1344.0,1370.0,1396.0,1422.0,1448.0,1474.0,1500.0]
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.histoname = "ljets_ge4j_ge4t_Evt_HT_wo_MET"
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.histotitle = "H_{T} without MET"
    interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.selection = interf_ljets_ge4j_ge4t_Evt_HT_wo_MET.category[0]

    interfaces.append(interf_ljets_ge4j_ge4t_Evt_HT_wo_MET)
    
    plots = init_plots(interfaces = interfaces)
    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def plots_dnn(data, discrname):

    ndefaultbins = 10
    interfaces = []


    # plots for ge4j_ge4t_07_ttH

    interf_ljets_ge4j_ge4t_07_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==0))")
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==0))","ljets_ge4j_ge4t_07_ttH_ttH_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.bin_edges = [ 
				0.2,
				0.264,
				0.328,
				0.392,
				0.456,
				0.52,
				0.584,
				0.648,
				0.712,
				0.84
				]
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttH_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_07_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==1))")
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==1))","ljets_ge4j_ge4t_07_ttH_tt2b_node","")
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.maxxval = 0.86

    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.nhistobins = 4
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==2))")
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==2))","ljets_ge4j_ge4t_07_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.bin_edges = [ 
				0.2,
				0.54
				]
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==3))")
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==3))","ljets_ge4j_ge4t_07_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.bin_edges = [ 
				0.2,
				0.79
				]
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttlf_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==4))")
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==4))","ljets_ge4j_ge4t_07_ttH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.maxxval = 0.68

    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.nhistobins = 4
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node)
    


    # plots for ge4j_ge4t_11_ttH

    interf_ljets_ge4j_ge4t_11_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_11_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==0))")
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==0))","ljets_ge4j_ge4t_11_ttH_ttH_node","")
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.bin_edges = [ 
				0.2,
				0.262,
				0.324,
				0.386,
				0.448,
				0.51,
				0.572,
				0.634,
				0.696,
				0.82
				]
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_ttH_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_old_tt2b",
                                            label          = "ljets_ge4j_ge4t_11_ttH_old_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==1))")
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==1))","ljets_ge4j_ge4t_11_ttH_old_tt2b_node","")
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.bin_edges = [ 
				0.2,
				0.67
				]
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_11_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==2))")
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==2))","ljets_ge4j_ge4t_11_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.bin_edges = [ 
				0.2,
				0.53
				]
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_11_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==3))")
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==3))","ljets_ge4j_ge4t_11_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.bin_edges = [ 
				0.2,
				0.73
				]
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_ttlf_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_old_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==4))")
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==4))","ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.bin_edges = [ 
				0.2,
				0.76
				]
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node)
    


   

    # plots for ge4j_3t_07_ttH

    interf_ljets_ge4j_3t_07_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttH",
                                            label          = "ljets_ge4j_3t_07_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==0))")
    interf_ljets_ge4j_3t_07_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==0))","ljets_ge4j_3t_07_ttH_ttH_node","")
    interf_ljets_ge4j_3t_07_ttH_ttH_node.bin_edges = [ 
				0.2,
				0.273,
				0.346,
				0.419,
				0.492,
				0.565,
				0.638,
				0.711,
				0.784,
				0.93
				]
    interf_ljets_ge4j_3t_07_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttH_node)
    
    interf_ljets_ge4j_3t_07_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_tt2b",
                                            label          = "ljets_ge4j_3t_07_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==1))")
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==1))","ljets_ge4j_3t_07_ttH_tt2b_node","")
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.bin_edges = [ 
				0.2,
				0.89
				]
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_tt2b_node)
    
    interf_ljets_ge4j_3t_07_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_07_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==2))")
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==2))","ljets_ge4j_3t_07_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.bin_edges = [ 
				0.2,
				0.66
				]
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_07_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_07_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==3))")
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==3))","ljets_ge4j_3t_07_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.bin_edges = [ 
				0.2,
				0.81
				]
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttlf_node)
    
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_07_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==4))")
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==4))","ljets_ge4j_3t_07_ttH_ttb_bb_node","")
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.bin_edges = [ 
				0.2,
				0.76
				]
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_11_ttH

    interf_ljets_ge4j_3t_11_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_ttH",
                                            label          = "ljets_ge4j_3t_11_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==0))")
    interf_ljets_ge4j_3t_11_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==0))","ljets_ge4j_3t_11_ttH_ttH_node","")
    interf_ljets_ge4j_3t_11_ttH_ttH_node.bin_edges = [ 
				0.2,
				0.267,
				0.334,
				0.401,
				0.468,
				0.535,
				0.602,
				0.669,
				0.736,
				0.87
				]
    interf_ljets_ge4j_3t_11_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_ttH_node)
    
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_old_tt2b",
                                            label          = "ljets_ge4j_3t_11_ttH_old_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==1))")
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==1))","ljets_ge4j_3t_11_ttH_old_tt2b_node","")
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.bin_edges = [ 
				0.2,
				0.87
				]
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_old_tt2b_node)
    
    interf_ljets_ge4j_3t_11_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_11_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==2))")
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==2))","ljets_ge4j_3t_11_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.bin_edges = [ 
				0.2,
				0.55
				]
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_11_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_11_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==3))")
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==3))","ljets_ge4j_3t_11_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.bin_edges = [ 
				0.2,
				0.81
				]
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_ttlf_node)
    
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_old_ttb_bb",
                                            label          = "ljets_ge4j_3t_11_ttH_old_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==4))")
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==4))","ljets_ge4j_3t_11_ttH_old_ttb_bb_node","")
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node.bin_edges = [ 
				0.2,
				0.76
				]
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots



def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_3t(data)
    discriminatorPlots += plots_ge4j_ge4t(data)
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
    