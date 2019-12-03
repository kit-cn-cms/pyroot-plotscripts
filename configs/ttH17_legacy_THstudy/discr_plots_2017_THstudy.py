
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

    ndefaultbins = 1
    interfaces = []


    # plots for ge4j_ge4t_07_ttH

    interf_ljets_ge4j_ge4t_07_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==0))")
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==0))","ljets_ge4j_ge4t_07_ttH_ttH_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.maxxval = 0.84
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttH_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_07_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==1))")
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==1))","ljets_ge4j_ge4t_07_ttH_tt2b_node","")
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.maxxval = 0.86
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==2))")
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==2))","ljets_ge4j_ge4t_07_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.maxxval = 0.54
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==3))")
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==3))","ljets_ge4j_ge4t_07_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.maxxval = 0.79
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttlf_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==4))")
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==4))","ljets_ge4j_ge4t_07_ttH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.maxxval = 0.68
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node)
    


    # plots for ge4j_ge4t_13_tHQtHW

    interf_ljets_ge4j_ge4t_13_tHQtHW_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_13_tHQtHW_node_tHW",
                                            label          = "ljets_ge4j_ge4t_13_tHQtHW_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==0))")
    interf_ljets_ge4j_ge4t_13_tHQtHW_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==0))","ljets_ge4j_ge4t_13_tHQtHW_tHW_node","")
    interf_ljets_ge4j_ge4t_13_tHQtHW_tHW_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_13_tHQtHW_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_13_tHQtHW_tHW_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_13_tHQtHW_tHW_node)
    
    interf_ljets_ge4j_ge4t_13_tHQtHW_tHQ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_13_tHQtHW_node_tHQ",
                                            label          = "ljets_ge4j_ge4t_13_tHQtHW_tHQ_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==1))")
    interf_ljets_ge4j_ge4t_13_tHQtHW_tHQ_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==1))","ljets_ge4j_ge4t_13_tHQtHW_tHQ_node","")
    interf_ljets_ge4j_ge4t_13_tHQtHW_tHQ_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_13_tHQtHW_tHQ_node.maxxval = 0.99
    interf_ljets_ge4j_ge4t_13_tHQtHW_tHQ_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_13_tHQtHW_tHQ_node)
    
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_13_tHQtHW_node_ttH",
                                            label          = "ljets_ge4j_ge4t_13_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==2))")
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==2))","ljets_ge4j_ge4t_13_tHQtHW_ttH_node","")
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttH_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttH_node.maxxval = 0.74
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_13_tHQtHW_ttH_node)
    
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_13_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_13_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==3))")
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==3))","ljets_ge4j_ge4t_13_tHQtHW_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttb_bb_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttb_bb_node.maxxval = 0.66
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_13_tHQtHW_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_13_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_13_tHQtHW_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_13_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==4))")
    interf_ljets_ge4j_ge4t_13_tHQtHW_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==4))","ljets_ge4j_ge4t_13_tHQtHW_tt2b_node","")
    interf_ljets_ge4j_ge4t_13_tHQtHW_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_13_tHQtHW_tt2b_node.maxxval = 0.69
    interf_ljets_ge4j_ge4t_13_tHQtHW_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_13_tHQtHW_tt2b_node)
    
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_13_tHQtHW_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_13_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==5))")
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==5))","ljets_ge4j_ge4t_13_tHQtHW_ttcc_node","")
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttcc_node.maxxval = 0.51
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_13_tHQtHW_ttcc_node)
    
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_13_tHQtHW_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_13_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==6))")
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_13_tHQtHW==6))","ljets_ge4j_ge4t_13_tHQtHW_ttlf_node","")
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttlf_node.maxxval = 0.71
    interf_ljets_ge4j_ge4t_13_tHQtHW_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_13_tHQtHW_ttlf_node)
    


    # plots for ge4j_ge4t_08_t_ttH

    interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_08_t_ttH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_08_t_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==0))")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==0))","ljets_ge4j_ge4t_08_t_ttH_ttH_node","")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node.maxxval = 0.8
    interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node)
    
    interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_08_t_ttH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_08_t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==1))")
    interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==1))","ljets_ge4j_ge4t_08_t_ttH_tt2b_node","")
    interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node.maxxval = 0.74
    interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_08_t_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_08_t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==2))")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==2))","ljets_ge4j_ge4t_08_t_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node.maxxval = 0.55
    interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_08_t_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_08_t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==3))")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==3))","ljets_ge4j_ge4t_08_t_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node.maxxval = 0.76
    interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node)
    
    interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_08_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==4))")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==4))","ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node.maxxval = 0.73
    interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node)
    


    # plots for ge4j_ge4t_12_tH

    interf_ljets_ge4j_ge4t_12_tH_tH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_12_tH_node_tH",
                                            label          = "ljets_ge4j_ge4t_12_tH_tH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==0))")
    interf_ljets_ge4j_ge4t_12_tH_tH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==0))","ljets_ge4j_ge4t_12_tH_tH_node","")
    interf_ljets_ge4j_ge4t_12_tH_tH_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_12_tH_tH_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_12_tH_tH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_12_tH_tH_node)
    
    interf_ljets_ge4j_ge4t_12_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_12_tH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_12_tH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==1))")
    interf_ljets_ge4j_ge4t_12_tH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==1))","ljets_ge4j_ge4t_12_tH_ttH_node","")
    interf_ljets_ge4j_ge4t_12_tH_ttH_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_12_tH_ttH_node.maxxval = 0.74
    interf_ljets_ge4j_ge4t_12_tH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_12_tH_ttH_node)
    
    interf_ljets_ge4j_ge4t_12_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_12_tH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_12_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==2))")
    interf_ljets_ge4j_ge4t_12_tH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==2))","ljets_ge4j_ge4t_12_tH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_12_tH_ttb_bb_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_12_tH_ttb_bb_node.maxxval = 0.63
    interf_ljets_ge4j_ge4t_12_tH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_12_tH_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_12_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_12_tH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_12_tH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==3))")
    interf_ljets_ge4j_ge4t_12_tH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==3))","ljets_ge4j_ge4t_12_tH_tt2b_node","")
    interf_ljets_ge4j_ge4t_12_tH_tt2b_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_12_tH_tt2b_node.maxxval = 0.79
    interf_ljets_ge4j_ge4t_12_tH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_12_tH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_12_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_12_tH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_12_tH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==4))")
    interf_ljets_ge4j_ge4t_12_tH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==4))","ljets_ge4j_ge4t_12_tH_ttcc_node","")
    interf_ljets_ge4j_ge4t_12_tH_ttcc_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_12_tH_ttcc_node.maxxval = 0.55
    interf_ljets_ge4j_ge4t_12_tH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_12_tH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_12_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_12_tH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_12_tH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==5))")
    interf_ljets_ge4j_ge4t_12_tH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_12_tH==5))","ljets_ge4j_ge4t_12_tH_ttlf_node","")
    interf_ljets_ge4j_ge4t_12_tH_ttlf_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_12_tH_ttlf_node.maxxval = 0.77
    interf_ljets_ge4j_ge4t_12_tH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_12_tH_ttlf_node)
    


    # plots for ge4j_ge4t_11_ttH

    interf_ljets_ge4j_ge4t_11_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_11_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==0))")
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==0))","ljets_ge4j_ge4t_11_ttH_ttH_node","")
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.maxxval = 0.82
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_ttH_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_old_tt2b",
                                            label          = "ljets_ge4j_ge4t_11_ttH_old_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==1))")
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==1))","ljets_ge4j_ge4t_11_ttH_old_tt2b_node","")
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.maxxval = 0.67
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_11_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==2))")
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==2))","ljets_ge4j_ge4t_11_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.maxxval = 0.53
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_11_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==3))")
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==3))","ljets_ge4j_ge4t_11_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.maxxval = 0.73
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_ttlf_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_old_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==4))")
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==4))","ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.maxxval = 0.76
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node)
    


    # plots for ge3j_ge3t_ge1f_04_t_ttH

    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_04_t_ttH_node_t_ttH",
                                            label          = "ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==0))")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==0))","ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node","")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node.maxxval = 0.99
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_04_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==1))")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==1))","ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node","")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node.maxxval = 0.74
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node)
    
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_04_t_ttH_node_tt2b",
                                            label          = "ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==2))")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==2))","ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node","")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node.maxxval = 0.8
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node)
    
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_04_t_ttH_node_ttcc",
                                            label          = "ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==3))")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==3))","ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node","")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node.maxxval = 0.53
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node)
    
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_04_t_ttH_node_ttlf",
                                            label          = "ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==4))")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==4))","ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node","")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node.maxxval = 0.84
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node)
    


    # plots for ge3j_ge3t_ge1f_05_tH

    interf_ljets_ge3j_ge3t_ge1f_05_tH_tH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_05_tH_node_tH",
                                            label          = "ljets_ge3j_ge3t_ge1f_05_tH_tH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==0))")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_tH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==0))","ljets_ge3j_ge3t_ge1f_05_tH_tH_node","")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_tH_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_05_tH_tH_node.maxxval = 1.0
    interf_ljets_ge3j_ge3t_ge1f_05_tH_tH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_05_tH_tH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_05_tH_node_ttH",
                                            label          = "ljets_ge3j_ge3t_ge1f_05_tH_ttH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==1))")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==1))","ljets_ge3j_ge3t_ge1f_05_tH_ttH_node","")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttH_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttH_node.maxxval = 0.88
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_05_tH_ttH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_05_tH_node_ttb_bb",
                                            label          = "ljets_ge3j_ge3t_ge1f_05_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==2))")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttb_bb_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==2))","ljets_ge3j_ge3t_ge1f_05_tH_ttb_bb_node","")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttb_bb_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttb_bb_node.maxxval = 0.62
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_05_tH_ttb_bb_node)
    
    interf_ljets_ge3j_ge3t_ge1f_05_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_05_tH_node_tt2b",
                                            label          = "ljets_ge3j_ge3t_ge1f_05_tH_tt2b_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==3))")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_tt2b_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==3))","ljets_ge3j_ge3t_ge1f_05_tH_tt2b_node","")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_tt2b_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_05_tH_tt2b_node.maxxval = 0.86
    interf_ljets_ge3j_ge3t_ge1f_05_tH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_05_tH_tt2b_node)
    
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_05_tH_node_ttcc",
                                            label          = "ljets_ge3j_ge3t_ge1f_05_tH_ttcc_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==4))")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttcc_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==4))","ljets_ge3j_ge3t_ge1f_05_tH_ttcc_node","")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttcc_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttcc_node.maxxval = 0.48
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_05_tH_ttcc_node)
    
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_05_tH_node_ttlf",
                                            label          = "ljets_ge3j_ge3t_ge1f_05_tH_ttlf_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==5))")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttlf_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_05_tH==5))","ljets_ge3j_ge3t_ge1f_05_tH_ttlf_node","")
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttlf_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttlf_node.maxxval = 0.77
    interf_ljets_ge3j_ge3t_ge1f_05_tH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_05_tH_ttlf_node)
    


    # plots for ge3j_ge3t_ge1f_06_tHQtHW

    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_06_tHQtHW_node_tHW",
                                            label          = "ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHW_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==0))")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHW_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==0))","ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHW_node","")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHW_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHW_node.maxxval = 1.0
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHW_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHW_node)
    
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHQ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_06_tHQtHW_node_tHQ",
                                            label          = "ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHQ_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==1))")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHQ_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==1))","ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHQ_node","")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHQ_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHQ_node.maxxval = 0.99
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHQ_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tHQ_node)
    
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_06_tHQtHW_node_ttH",
                                            label          = "ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==2))")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==2))","ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttH_node","")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttH_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttH_node.maxxval = 0.76
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_06_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==3))")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttb_bb_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==3))","ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttb_bb_node","")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttb_bb_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttb_bb_node.maxxval = 0.59
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttb_bb_node)
    
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_06_tHQtHW_node_tt2b",
                                            label          = "ljets_ge3j_ge3t_ge1f_06_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==4))")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tt2b_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==4))","ljets_ge3j_ge3t_ge1f_06_tHQtHW_tt2b_node","")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tt2b_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tt2b_node.maxxval = 0.66
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_tt2b_node)
    
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_06_tHQtHW_node_ttcc",
                                            label          = "ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==5))")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttcc_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==5))","ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttcc_node","")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttcc_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttcc_node.maxxval = 0.45
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttcc_node)
    
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_06_tHQtHW_node_ttlf",
                                            label          = "ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==6))")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttlf_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_06_tHQtHW==6))","ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttlf_node","")
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttlf_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttlf_node.maxxval = 0.78
    interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_06_tHQtHW_ttlf_node)
    


    # plots for ge3j_ge3t_ge1f_01_tH

    interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_tH",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_tH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==0))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==0))","ljets_ge3j_ge3t_ge1f_01_tH_tH_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node.maxxval = 1.0
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_ttH",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_ttH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==1))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==1))","ljets_ge3j_ge3t_ge1f_01_tH_ttH_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node.maxxval = 0.88
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_ttb_bb",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==2))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==2))","ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node.maxxval = 0.62
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node)
    
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_tt2b",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==3))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==3))","ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node.maxxval = 0.86
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node)
    
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_ttcc",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==4))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==4))","ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node.maxxval = 0.48
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node)
    
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_ttlf",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==5))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==5))","ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node.maxxval = 0.77
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node)
    


    # plots for ge3j_ge3t_ge1f_02_ttH

    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_02_ttH_node_ttH",
                                            label          = "ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==0))")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==0))","ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node","")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node.maxxval = 0.87
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_02_ttH_node_ttb_bb",
                                            label          = "ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==1))")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==1))","ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node","")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node.maxxval = 0.69
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node)
    
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_02_ttH_node_tt2b",
                                            label          = "ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==2))")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==2))","ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node","")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node.maxxval = 0.78
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node)
    
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_02_ttH_node_ttcc",
                                            label          = "ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==3))")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==3))","ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node","")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node.maxxval = 0.57
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node)
    
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_02_ttH_node_ttlf",
                                            label          = "ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==4))")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==4))","ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node","")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node.maxxval = 0.79
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node)
    


    # plots for ge3j_ge3t_ge1f_03_tHQtHW

    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_tHW",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==0))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==0))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node.maxxval = 1.0
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_tHQ",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==1))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==1))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node.maxxval = 0.99
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_ttH",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==2))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==2))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node.maxxval = 0.76
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==3))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==3))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node.maxxval = 0.59
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_tt2b",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==4))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==4))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node.maxxval = 0.66
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_ttcc",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==5))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==5))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node.maxxval = 0.45
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_ttlf",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==6))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==6))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node.maxxval = 0.78
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node)
    


    # plots for ge4J_3t_09_ttH

    interf_ljets_ge4J_3t_09_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_09_ttH_node_ttH",
                                            label          = "ljets_ge4J_3t_09_ttH_ttH_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==0))")
    interf_ljets_ge4J_3t_09_ttH_ttH_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==0))","ljets_ge4J_3t_09_ttH_ttH_node","")
    interf_ljets_ge4J_3t_09_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4J_3t_09_ttH_ttH_node.maxxval = 0.92
    interf_ljets_ge4J_3t_09_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4J_3t_09_ttH_ttH_node)
    
    interf_ljets_ge4J_3t_09_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_09_ttH_node_tt2b",
                                            label          = "ljets_ge4J_3t_09_ttH_tt2b_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==1))")
    interf_ljets_ge4J_3t_09_ttH_tt2b_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==1))","ljets_ge4J_3t_09_ttH_tt2b_node","")
    interf_ljets_ge4J_3t_09_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4J_3t_09_ttH_tt2b_node.maxxval = 0.85
    interf_ljets_ge4J_3t_09_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_3t_09_ttH_tt2b_node)
    
    interf_ljets_ge4J_3t_09_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_09_ttH_node_ttcc",
                                            label          = "ljets_ge4J_3t_09_ttH_ttcc_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==2))")
    interf_ljets_ge4J_3t_09_ttH_ttcc_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==2))","ljets_ge4J_3t_09_ttH_ttcc_node","")
    interf_ljets_ge4J_3t_09_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4J_3t_09_ttH_ttcc_node.maxxval = 0.57
    interf_ljets_ge4J_3t_09_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_3t_09_ttH_ttcc_node)
    
    interf_ljets_ge4J_3t_09_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_09_ttH_node_ttlf",
                                            label          = "ljets_ge4J_3t_09_ttH_ttlf_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==3))")
    interf_ljets_ge4J_3t_09_ttH_ttlf_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==3))","ljets_ge4J_3t_09_ttH_ttlf_node","")
    interf_ljets_ge4J_3t_09_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4J_3t_09_ttH_ttlf_node.maxxval = 0.81
    interf_ljets_ge4J_3t_09_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_3t_09_ttH_ttlf_node)
    
    interf_ljets_ge4J_3t_09_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_09_ttH_node_ttb_bb",
                                            label          = "ljets_ge4J_3t_09_ttH_ttb_bb_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==4))")
    interf_ljets_ge4J_3t_09_ttH_ttb_bb_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==4))","ljets_ge4J_3t_09_ttH_ttb_bb_node","")
    interf_ljets_ge4J_3t_09_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4J_3t_09_ttH_ttb_bb_node.maxxval = 0.69
    interf_ljets_ge4J_3t_09_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_3t_09_ttH_ttb_bb_node)
    


    # plots for ge4J_3t_10_t_ttH

    interf_ljets_ge4J_3t_10_t_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_10_t_ttH_node_ttH",
                                            label          = "ljets_ge4J_3t_10_t_ttH_ttH_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==0))")
    interf_ljets_ge4J_3t_10_t_ttH_ttH_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==0))","ljets_ge4J_3t_10_t_ttH_ttH_node","")
    interf_ljets_ge4J_3t_10_t_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4J_3t_10_t_ttH_ttH_node.maxxval = 0.95
    interf_ljets_ge4J_3t_10_t_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4J_3t_10_t_ttH_ttH_node)
    
    interf_ljets_ge4J_3t_10_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_10_t_ttH_node_tt2b",
                                            label          = "ljets_ge4J_3t_10_t_ttH_tt2b_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==1))")
    interf_ljets_ge4J_3t_10_t_ttH_tt2b_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==1))","ljets_ge4J_3t_10_t_ttH_tt2b_node","")
    interf_ljets_ge4J_3t_10_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4J_3t_10_t_ttH_tt2b_node.maxxval = 0.85
    interf_ljets_ge4J_3t_10_t_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_3t_10_t_ttH_tt2b_node)
    
    interf_ljets_ge4J_3t_10_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_10_t_ttH_node_ttcc",
                                            label          = "ljets_ge4J_3t_10_t_ttH_ttcc_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==2))")
    interf_ljets_ge4J_3t_10_t_ttH_ttcc_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==2))","ljets_ge4J_3t_10_t_ttH_ttcc_node","")
    interf_ljets_ge4J_3t_10_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4J_3t_10_t_ttH_ttcc_node.maxxval = 0.59
    interf_ljets_ge4J_3t_10_t_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_3t_10_t_ttH_ttcc_node)
    
    interf_ljets_ge4J_3t_10_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_10_t_ttH_node_ttlf",
                                            label          = "ljets_ge4J_3t_10_t_ttH_ttlf_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==3))")
    interf_ljets_ge4J_3t_10_t_ttH_ttlf_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==3))","ljets_ge4J_3t_10_t_ttH_ttlf_node","")
    interf_ljets_ge4J_3t_10_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4J_3t_10_t_ttH_ttlf_node.maxxval = 0.84
    interf_ljets_ge4J_3t_10_t_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_3t_10_t_ttH_ttlf_node)
    
    interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_10_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4J_3t_10_t_ttH_ttb_bb_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==4))")
    interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==4))","ljets_ge4J_3t_10_t_ttH_ttb_bb_node","")
    interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node.maxxval = 0.71
    interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_0f_04_t_ttH

    interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_04_t_ttH_node_t_ttH",
                                            label          = "ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==0))")
    interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==0))","ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node","")
    interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node.maxxval = 0.98
    interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node)
    
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_04_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==1))")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==1))","ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node","")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node.maxxval = 0.6
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node)
    
    interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_04_t_ttH_node_tt2b",
                                            label          = "ljets_ge4j_3t_0f_04_t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==2))")
    interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==2))","ljets_ge4j_3t_0f_04_t_ttH_tt2b_node","")
    interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node.maxxval = 0.84
    interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node)
    
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_04_t_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_0f_04_t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==3))")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==3))","ljets_ge4j_3t_0f_04_t_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node.maxxval = 0.56
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_04_t_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_0f_04_t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==4))")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==4))","ljets_ge4j_3t_0f_04_t_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node.maxxval = 0.82
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node)
    


    # plots for ge4j_3t_0f_05_tH

    interf_ljets_ge4j_3t_0f_05_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_05_tH_node_ttH",
                                            label          = "ljets_ge4j_3t_0f_05_tH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_05_tH==0))")
    interf_ljets_ge4j_3t_0f_05_tH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_05_tH==0))","ljets_ge4j_3t_0f_05_tH_ttH_node","")
    interf_ljets_ge4j_3t_0f_05_tH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_05_tH_ttH_node.maxxval = 0.92
    interf_ljets_ge4j_3t_0f_05_tH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_0f_05_tH_ttH_node)
    
    interf_ljets_ge4j_3t_0f_05_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_05_tH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_0f_05_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_05_tH==1))")
    interf_ljets_ge4j_3t_0f_05_tH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_05_tH==1))","ljets_ge4j_3t_0f_05_tH_ttb_bb_node","")
    interf_ljets_ge4j_3t_0f_05_tH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_05_tH_ttb_bb_node.maxxval = 0.64
    interf_ljets_ge4j_3t_0f_05_tH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_05_tH_ttb_bb_node)
    
    interf_ljets_ge4j_3t_0f_05_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_05_tH_node_tt2b",
                                            label          = "ljets_ge4j_3t_0f_05_tH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_05_tH==2))")
    interf_ljets_ge4j_3t_0f_05_tH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_05_tH==2))","ljets_ge4j_3t_0f_05_tH_tt2b_node","")
    interf_ljets_ge4j_3t_0f_05_tH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_05_tH_tt2b_node.maxxval = 0.84
    interf_ljets_ge4j_3t_0f_05_tH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_05_tH_tt2b_node)
    
    interf_ljets_ge4j_3t_0f_05_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_05_tH_node_ttcc",
                                            label          = "ljets_ge4j_3t_0f_05_tH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_05_tH==3))")
    interf_ljets_ge4j_3t_0f_05_tH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_05_tH==3))","ljets_ge4j_3t_0f_05_tH_ttcc_node","")
    interf_ljets_ge4j_3t_0f_05_tH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_05_tH_ttcc_node.maxxval = 0.55
    interf_ljets_ge4j_3t_0f_05_tH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_05_tH_ttcc_node)
    
    interf_ljets_ge4j_3t_0f_05_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_05_tH_node_ttlf",
                                            label          = "ljets_ge4j_3t_0f_05_tH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_05_tH==4))")
    interf_ljets_ge4j_3t_0f_05_tH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_05_tH==4))","ljets_ge4j_3t_0f_05_tH_ttlf_node","")
    interf_ljets_ge4j_3t_0f_05_tH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_05_tH_ttlf_node.maxxval = 0.82
    interf_ljets_ge4j_3t_0f_05_tH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_05_tH_ttlf_node)
    


    # plots for ge4j_3t_0f_06_tHQtHW

    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_06_tHQtHW_node_ttH",
                                            label          = "ljets_ge4j_3t_0f_06_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_06_tHQtHW==0))")
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_06_tHQtHW==0))","ljets_ge4j_3t_0f_06_tHQtHW_ttH_node","")
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttH_node.maxxval = 0.92
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_0f_06_tHQtHW_ttH_node)
    
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_06_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_0f_06_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_06_tHQtHW==1))")
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_06_tHQtHW==1))","ljets_ge4j_3t_0f_06_tHQtHW_ttb_bb_node","")
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttb_bb_node.maxxval = 0.64
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_06_tHQtHW_ttb_bb_node)
    
    interf_ljets_ge4j_3t_0f_06_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_06_tHQtHW_node_tt2b",
                                            label          = "ljets_ge4j_3t_0f_06_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_06_tHQtHW==2))")
    interf_ljets_ge4j_3t_0f_06_tHQtHW_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_06_tHQtHW==2))","ljets_ge4j_3t_0f_06_tHQtHW_tt2b_node","")
    interf_ljets_ge4j_3t_0f_06_tHQtHW_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_06_tHQtHW_tt2b_node.maxxval = 0.84
    interf_ljets_ge4j_3t_0f_06_tHQtHW_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_06_tHQtHW_tt2b_node)
    
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_06_tHQtHW_node_ttcc",
                                            label          = "ljets_ge4j_3t_0f_06_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_06_tHQtHW==3))")
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_06_tHQtHW==3))","ljets_ge4j_3t_0f_06_tHQtHW_ttcc_node","")
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttcc_node.maxxval = 0.55
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_06_tHQtHW_ttcc_node)
    
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_06_tHQtHW_node_ttlf",
                                            label          = "ljets_ge4j_3t_0f_06_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_06_tHQtHW==4))")
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_06_tHQtHW==4))","ljets_ge4j_3t_0f_06_tHQtHW_ttlf_node","")
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttlf_node.maxxval = 0.82
    interf_ljets_ge4j_3t_0f_06_tHQtHW_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_06_tHQtHW_ttlf_node)
    


    # plots for ge4j_3t_0f_01_tH

    interf_ljets_ge4j_3t_0f_01_tH_tH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_tH",
                                            label          = "ljets_ge4j_3t_0f_01_tH_tH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==0))")
    interf_ljets_ge4j_3t_0f_01_tH_tH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==0))","ljets_ge4j_3t_0f_01_tH_tH_node","")
    interf_ljets_ge4j_3t_0f_01_tH_tH_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_tH_node.maxxval = 1.0
    interf_ljets_ge4j_3t_0f_01_tH_tH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_tH_node)
    
    interf_ljets_ge4j_3t_0f_01_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_ttH",
                                            label          = "ljets_ge4j_3t_0f_01_tH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==1))")
    interf_ljets_ge4j_3t_0f_01_tH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==1))","ljets_ge4j_3t_0f_01_tH_ttH_node","")
    interf_ljets_ge4j_3t_0f_01_tH_ttH_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_ttH_node.maxxval = 0.76
    interf_ljets_ge4j_3t_0f_01_tH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_ttH_node)
    
    interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_0f_01_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==2))")
    interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==2))","ljets_ge4j_3t_0f_01_tH_ttb_bb_node","")
    interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node.maxxval = 0.58
    interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node)
    
    interf_ljets_ge4j_3t_0f_01_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_tt2b",
                                            label          = "ljets_ge4j_3t_0f_01_tH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==3))")
    interf_ljets_ge4j_3t_0f_01_tH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==3))","ljets_ge4j_3t_0f_01_tH_tt2b_node","")
    interf_ljets_ge4j_3t_0f_01_tH_tt2b_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_tt2b_node.maxxval = 0.77
    interf_ljets_ge4j_3t_0f_01_tH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_tt2b_node)
    
    interf_ljets_ge4j_3t_0f_01_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_ttcc",
                                            label          = "ljets_ge4j_3t_0f_01_tH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==4))")
    interf_ljets_ge4j_3t_0f_01_tH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==4))","ljets_ge4j_3t_0f_01_tH_ttcc_node","")
    interf_ljets_ge4j_3t_0f_01_tH_ttcc_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_ttcc_node.maxxval = 0.5
    interf_ljets_ge4j_3t_0f_01_tH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_ttcc_node)
    
    interf_ljets_ge4j_3t_0f_01_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_ttlf",
                                            label          = "ljets_ge4j_3t_0f_01_tH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==5))")
    interf_ljets_ge4j_3t_0f_01_tH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==5))","ljets_ge4j_3t_0f_01_tH_ttlf_node","")
    interf_ljets_ge4j_3t_0f_01_tH_ttlf_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_ttlf_node.maxxval = 0.79
    interf_ljets_ge4j_3t_0f_01_tH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_ttlf_node)
    


    # plots for ge4j_3t_0f_02_ttH

    interf_ljets_ge4j_3t_0f_02_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_02_ttH_node_ttH",
                                            label          = "ljets_ge4j_3t_0f_02_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==0))")
    interf_ljets_ge4j_3t_0f_02_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==0))","ljets_ge4j_3t_0f_02_ttH_ttH_node","")
    interf_ljets_ge4j_3t_0f_02_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_02_ttH_ttH_node.maxxval = 0.92
    interf_ljets_ge4j_3t_0f_02_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_0f_02_ttH_ttH_node)
    
    interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_02_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_0f_02_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==1))")
    interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==1))","ljets_ge4j_3t_0f_02_ttH_ttb_bb_node","")
    interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node.maxxval = 0.64
    interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node)
    
    interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_02_ttH_node_tt2b",
                                            label          = "ljets_ge4j_3t_0f_02_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==2))")
    interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==2))","ljets_ge4j_3t_0f_02_ttH_tt2b_node","")
    interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node.maxxval = 0.84
    interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node)
    
    interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_02_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_0f_02_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==3))")
    interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==3))","ljets_ge4j_3t_0f_02_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node.maxxval = 0.55
    interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_02_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_0f_02_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==4))")
    interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==4))","ljets_ge4j_3t_0f_02_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node.maxxval = 0.82
    interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node)
    


    # plots for ge4j_3t_0f_03_tHQtHW

    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_tHW",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==0))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==0))","ljets_ge4j_3t_0f_03_tHQtHW_tHW_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_tHQ",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==1))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==1))","ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node.maxxval = 0.98
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_ttH",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==2))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==2))","ljets_ge4j_3t_0f_03_tHQtHW_ttH_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node.maxxval = 0.66
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==3))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==3))","ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node.maxxval = 0.52
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_tt2b",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==4))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==4))","ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node.maxxval = 0.69
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_ttcc",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==5))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==5))","ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node.maxxval = 0.47
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_ttlf",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==6))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==6))","ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node.maxxval = 0.76
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node)
    


    # plots for ge4j_ge4t_0f_04_t_ttH

    interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_04_t_ttH_node_t_ttH",
                                            label          = "ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==0))")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==0))","ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node","")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node.maxxval = 0.83
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node)
    
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_04_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==1))")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==1))","ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node.maxxval = 0.68
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_04_t_ttH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==2))")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==2))","ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node","")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node.maxxval = 0.76
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_04_t_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==3))")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==3))","ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node.maxxval = 0.65
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_04_t_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==4))")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==4))","ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node.maxxval = 0.81
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node)
    


    # plots for ge4j_ge4t_0f_05_tH

    interf_ljets_ge4j_ge4t_0f_05_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_05_tH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_0f_05_tH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_05_tH==0))")
    interf_ljets_ge4j_ge4t_0f_05_tH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_05_tH==0))","ljets_ge4j_ge4t_0f_05_tH_ttH_node","")
    interf_ljets_ge4j_ge4t_0f_05_tH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_05_tH_ttH_node.maxxval = 0.84
    interf_ljets_ge4j_ge4t_0f_05_tH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_0f_05_tH_ttH_node)
    
    interf_ljets_ge4j_ge4t_0f_05_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_05_tH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_0f_05_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_05_tH==1))")
    interf_ljets_ge4j_ge4t_0f_05_tH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_05_tH==1))","ljets_ge4j_ge4t_0f_05_tH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_0f_05_tH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_05_tH_ttb_bb_node.maxxval = 0.66
    interf_ljets_ge4j_ge4t_0f_05_tH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_05_tH_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_0f_05_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_05_tH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_0f_05_tH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_05_tH==2))")
    interf_ljets_ge4j_ge4t_0f_05_tH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_05_tH==2))","ljets_ge4j_ge4t_0f_05_tH_tt2b_node","")
    interf_ljets_ge4j_ge4t_0f_05_tH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_05_tH_tt2b_node.maxxval = 0.8
    interf_ljets_ge4j_ge4t_0f_05_tH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_05_tH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_0f_05_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_05_tH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_0f_05_tH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_05_tH==3))")
    interf_ljets_ge4j_ge4t_0f_05_tH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_05_tH==3))","ljets_ge4j_ge4t_0f_05_tH_ttcc_node","")
    interf_ljets_ge4j_ge4t_0f_05_tH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_05_tH_ttcc_node.maxxval = 0.54
    interf_ljets_ge4j_ge4t_0f_05_tH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_05_tH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_0f_05_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_05_tH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_0f_05_tH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_05_tH==4))")
    interf_ljets_ge4j_ge4t_0f_05_tH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_05_tH==4))","ljets_ge4j_ge4t_0f_05_tH_ttlf_node","")
    interf_ljets_ge4j_ge4t_0f_05_tH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_05_tH_ttlf_node.maxxval = 0.75
    interf_ljets_ge4j_ge4t_0f_05_tH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_05_tH_ttlf_node)
    


    # plots for ge4j_ge4t_0f_06_tHQtHW

    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_06_tHQtHW_node_ttH",
                                            label          = "ljets_ge4j_ge4t_0f_06_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_06_tHQtHW==0))")
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_06_tHQtHW==0))","ljets_ge4j_ge4t_0f_06_tHQtHW_ttH_node","")
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttH_node.maxxval = 0.84
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttH_node)
    
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_06_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_0f_06_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_06_tHQtHW==1))")
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_06_tHQtHW==1))","ljets_ge4j_ge4t_0f_06_tHQtHW_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttb_bb_node.maxxval = 0.66
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_06_tHQtHW_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_0f_06_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_06_tHQtHW==2))")
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_06_tHQtHW==2))","ljets_ge4j_ge4t_0f_06_tHQtHW_tt2b_node","")
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_tt2b_node.maxxval = 0.8
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_06_tHQtHW_tt2b_node)
    
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_06_tHQtHW_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_0f_06_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_06_tHQtHW==3))")
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_06_tHQtHW==3))","ljets_ge4j_ge4t_0f_06_tHQtHW_ttcc_node","")
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttcc_node.maxxval = 0.54
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttcc_node)
    
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_06_tHQtHW_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_0f_06_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_06_tHQtHW==4))")
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_06_tHQtHW==4))","ljets_ge4j_ge4t_0f_06_tHQtHW_ttlf_node","")
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttlf_node.maxxval = 0.75
    interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_06_tHQtHW_ttlf_node)
    


    # plots for ge4j_ge4t_0f_01_tH

    interf_ljets_ge4j_ge4t_0f_01_tH_tH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_tH",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_tH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==0))")
    interf_ljets_ge4j_ge4t_0f_01_tH_tH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==0))","ljets_ge4j_ge4t_0f_01_tH_tH_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_tH_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_tH_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_0f_01_tH_tH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_tH_node)
    
    interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==1))")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==1))","ljets_ge4j_ge4t_0f_01_tH_ttH_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node.maxxval = 0.8
    interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node)
    
    interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==2))")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==2))","ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node.maxxval = 0.7
    interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==3))")
    interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==3))","ljets_ge4j_ge4t_0f_01_tH_tt2b_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node.maxxval = 0.7
    interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==4))")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==4))","ljets_ge4j_ge4t_0f_01_tH_ttcc_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node.maxxval = 0.66
    interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==5))")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==5))","ljets_ge4j_ge4t_0f_01_tH_ttlf_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node.maxxval = 0.79
    interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node)
    


    # plots for ge4j_ge4t_0f_02_ttH

    interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_02_ttH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_0f_02_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==0))")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==0))","ljets_ge4j_ge4t_0f_02_ttH_ttH_node","")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node.maxxval = 0.84
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node)
    
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_02_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==1))")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==1))","ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node.maxxval = 0.66
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_02_ttH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_0f_02_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==2))")
    interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==2))","ljets_ge4j_ge4t_0f_02_ttH_tt2b_node","")
    interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node.maxxval = 0.8
    interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_02_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_0f_02_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==3))")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==3))","ljets_ge4j_ge4t_0f_02_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node.maxxval = 0.54
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_02_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_0f_02_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==4))")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==4))","ljets_ge4j_ge4t_0f_02_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node.maxxval = 0.75
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node)
    


    # plots for ge4j_ge4t_0f_03_tHQtHW

    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_tHW",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==0))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==0))","ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_tHQ",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==1))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==1))","ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node.maxxval = 0.95
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_ttH",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==2))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==2))","ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node.maxxval = 0.76
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==3))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==3))","ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node.maxxval = 0.61
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==4))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==4))","ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node.maxxval = 0.7
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==5))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==5))","ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node.maxxval = 0.6
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==6))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==6))","ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node.maxxval = 0.71
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node)
    


    # plots for ge4J_ge4t_09_ttH

    interf_ljets_ge4J_ge4t_09_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_09_ttH_node_ttH",
                                            label          = "ljets_ge4J_ge4t_09_ttH_ttH_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==0))")
    interf_ljets_ge4J_ge4t_09_ttH_ttH_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==0))","ljets_ge4J_ge4t_09_ttH_ttH_node","")
    interf_ljets_ge4J_ge4t_09_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_09_ttH_ttH_node.maxxval = 0.83
    interf_ljets_ge4J_ge4t_09_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4J_ge4t_09_ttH_ttH_node)
    
    interf_ljets_ge4J_ge4t_09_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_09_ttH_node_tt2b",
                                            label          = "ljets_ge4J_ge4t_09_ttH_tt2b_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==1))")
    interf_ljets_ge4J_ge4t_09_ttH_tt2b_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==1))","ljets_ge4J_ge4t_09_ttH_tt2b_node","")
    interf_ljets_ge4J_ge4t_09_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_09_ttH_tt2b_node.maxxval = 0.79
    interf_ljets_ge4J_ge4t_09_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_ge4t_09_ttH_tt2b_node)
    
    interf_ljets_ge4J_ge4t_09_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_09_ttH_node_ttcc",
                                            label          = "ljets_ge4J_ge4t_09_ttH_ttcc_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==2))")
    interf_ljets_ge4J_ge4t_09_ttH_ttcc_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==2))","ljets_ge4J_ge4t_09_ttH_ttcc_node","")
    interf_ljets_ge4J_ge4t_09_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_09_ttH_ttcc_node.maxxval = 0.58
    interf_ljets_ge4J_ge4t_09_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_ge4t_09_ttH_ttcc_node)
    
    interf_ljets_ge4J_ge4t_09_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_09_ttH_node_ttlf",
                                            label          = "ljets_ge4J_ge4t_09_ttH_ttlf_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==3))")
    interf_ljets_ge4J_ge4t_09_ttH_ttlf_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==3))","ljets_ge4J_ge4t_09_ttH_ttlf_node","")
    interf_ljets_ge4J_ge4t_09_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_09_ttH_ttlf_node.maxxval = 0.82
    interf_ljets_ge4J_ge4t_09_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_ge4t_09_ttH_ttlf_node)
    
    interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_09_ttH_node_ttb_bb",
                                            label          = "ljets_ge4J_ge4t_09_ttH_ttb_bb_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==4))")
    interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==4))","ljets_ge4J_ge4t_09_ttH_ttb_bb_node","")
    interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node.maxxval = 0.79
    interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node)
    


    # plots for ge4J_ge4t_10_t_ttH

    interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_10_t_ttH_node_ttH",
                                            label          = "ljets_ge4J_ge4t_10_t_ttH_ttH_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==0))")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==0))","ljets_ge4J_ge4t_10_t_ttH_ttH_node","")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node.maxxval = 0.8
    interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node)
    
    interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_10_t_ttH_node_tt2b",
                                            label          = "ljets_ge4J_ge4t_10_t_ttH_tt2b_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==1))")
    interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==1))","ljets_ge4J_ge4t_10_t_ttH_tt2b_node","")
    interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node.maxxval = 0.78
    interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node)
    
    interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_10_t_ttH_node_ttcc",
                                            label          = "ljets_ge4J_ge4t_10_t_ttH_ttcc_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==2))")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==2))","ljets_ge4J_ge4t_10_t_ttH_ttcc_node","")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node.maxxval = 0.58
    interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node)
    
    interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_10_t_ttH_node_ttlf",
                                            label          = "ljets_ge4J_ge4t_10_t_ttH_ttlf_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==3))")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==3))","ljets_ge4J_ge4t_10_t_ttH_ttlf_node","")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node.maxxval = 0.82
    interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node)
    
    interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_10_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==4))")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==4))","ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node","")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node.maxxval = 0.73
    interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_07_ttH

    interf_ljets_ge4j_3t_07_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttH",
                                            label          = "ljets_ge4j_3t_07_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==0))")
    interf_ljets_ge4j_3t_07_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==0))","ljets_ge4j_3t_07_ttH_ttH_node","")
    interf_ljets_ge4j_3t_07_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_07_ttH_ttH_node.maxxval = 0.93
    interf_ljets_ge4j_3t_07_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttH_node)
    
    interf_ljets_ge4j_3t_07_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_tt2b",
                                            label          = "ljets_ge4j_3t_07_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==1))")
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==1))","ljets_ge4j_3t_07_ttH_tt2b_node","")
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.maxxval = 0.89
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_tt2b_node)
    
    interf_ljets_ge4j_3t_07_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_07_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==2))")
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==2))","ljets_ge4j_3t_07_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.maxxval = 0.66
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_07_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_07_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==3))")
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==3))","ljets_ge4j_3t_07_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.maxxval = 0.81
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttlf_node)
    
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_07_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==4))")
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==4))","ljets_ge4j_3t_07_ttH_ttb_bb_node","")
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.maxxval = 0.76
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_13_tHQtHW

    interf_ljets_ge4j_3t_13_tHQtHW_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_13_tHQtHW_node_tHW",
                                            label          = "ljets_ge4j_3t_13_tHQtHW_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==0))")
    interf_ljets_ge4j_3t_13_tHQtHW_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==0))","ljets_ge4j_3t_13_tHQtHW_tHW_node","")
    interf_ljets_ge4j_3t_13_tHQtHW_tHW_node.minxval = 0.14
    interf_ljets_ge4j_3t_13_tHQtHW_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_3t_13_tHQtHW_tHW_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_13_tHQtHW_tHW_node)
    
    interf_ljets_ge4j_3t_13_tHQtHW_tHQ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_13_tHQtHW_node_tHQ",
                                            label          = "ljets_ge4j_3t_13_tHQtHW_tHQ_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==1))")
    interf_ljets_ge4j_3t_13_tHQtHW_tHQ_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==1))","ljets_ge4j_3t_13_tHQtHW_tHQ_node","")
    interf_ljets_ge4j_3t_13_tHQtHW_tHQ_node.minxval = 0.14
    interf_ljets_ge4j_3t_13_tHQtHW_tHQ_node.maxxval = 0.99
    interf_ljets_ge4j_3t_13_tHQtHW_tHQ_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_13_tHQtHW_tHQ_node)
    
    interf_ljets_ge4j_3t_13_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_13_tHQtHW_node_ttH",
                                            label          = "ljets_ge4j_3t_13_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==2))")
    interf_ljets_ge4j_3t_13_tHQtHW_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==2))","ljets_ge4j_3t_13_tHQtHW_ttH_node","")
    interf_ljets_ge4j_3t_13_tHQtHW_ttH_node.minxval = 0.14
    interf_ljets_ge4j_3t_13_tHQtHW_ttH_node.maxxval = 0.67
    interf_ljets_ge4j_3t_13_tHQtHW_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_13_tHQtHW_ttH_node)
    
    interf_ljets_ge4j_3t_13_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_13_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_13_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==3))")
    interf_ljets_ge4j_3t_13_tHQtHW_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==3))","ljets_ge4j_3t_13_tHQtHW_ttb_bb_node","")
    interf_ljets_ge4j_3t_13_tHQtHW_ttb_bb_node.minxval = 0.14
    interf_ljets_ge4j_3t_13_tHQtHW_ttb_bb_node.maxxval = 0.52
    interf_ljets_ge4j_3t_13_tHQtHW_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_13_tHQtHW_ttb_bb_node)
    
    interf_ljets_ge4j_3t_13_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_13_tHQtHW_node_tt2b",
                                            label          = "ljets_ge4j_3t_13_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==4))")
    interf_ljets_ge4j_3t_13_tHQtHW_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==4))","ljets_ge4j_3t_13_tHQtHW_tt2b_node","")
    interf_ljets_ge4j_3t_13_tHQtHW_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_3t_13_tHQtHW_tt2b_node.maxxval = 0.74
    interf_ljets_ge4j_3t_13_tHQtHW_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_13_tHQtHW_tt2b_node)
    
    interf_ljets_ge4j_3t_13_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_13_tHQtHW_node_ttcc",
                                            label          = "ljets_ge4j_3t_13_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==5))")
    interf_ljets_ge4j_3t_13_tHQtHW_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==5))","ljets_ge4j_3t_13_tHQtHW_ttcc_node","")
    interf_ljets_ge4j_3t_13_tHQtHW_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_3t_13_tHQtHW_ttcc_node.maxxval = 0.46
    interf_ljets_ge4j_3t_13_tHQtHW_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_13_tHQtHW_ttcc_node)
    
    interf_ljets_ge4j_3t_13_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_13_tHQtHW_node_ttlf",
                                            label          = "ljets_ge4j_3t_13_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==6))")
    interf_ljets_ge4j_3t_13_tHQtHW_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_13_tHQtHW==6))","ljets_ge4j_3t_13_tHQtHW_ttlf_node","")
    interf_ljets_ge4j_3t_13_tHQtHW_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_3t_13_tHQtHW_ttlf_node.maxxval = 0.74
    interf_ljets_ge4j_3t_13_tHQtHW_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_13_tHQtHW_ttlf_node)
    


    # plots for ge4j_3t_08_t_ttH

    interf_ljets_ge4j_3t_08_t_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_08_t_ttH_node_ttH",
                                            label          = "ljets_ge4j_3t_08_t_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==0))")
    interf_ljets_ge4j_3t_08_t_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==0))","ljets_ge4j_3t_08_t_ttH_ttH_node","")
    interf_ljets_ge4j_3t_08_t_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_08_t_ttH_ttH_node.maxxval = 0.87
    interf_ljets_ge4j_3t_08_t_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_08_t_ttH_ttH_node)
    
    interf_ljets_ge4j_3t_08_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_08_t_ttH_node_tt2b",
                                            label          = "ljets_ge4j_3t_08_t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==1))")
    interf_ljets_ge4j_3t_08_t_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==1))","ljets_ge4j_3t_08_t_ttH_tt2b_node","")
    interf_ljets_ge4j_3t_08_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_08_t_ttH_tt2b_node.maxxval = 0.85
    interf_ljets_ge4j_3t_08_t_ttH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_08_t_ttH_tt2b_node)
    
    interf_ljets_ge4j_3t_08_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_08_t_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_08_t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==2))")
    interf_ljets_ge4j_3t_08_t_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==2))","ljets_ge4j_3t_08_t_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_08_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_08_t_ttH_ttcc_node.maxxval = 0.52
    interf_ljets_ge4j_3t_08_t_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_08_t_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_08_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_08_t_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_08_t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==3))")
    interf_ljets_ge4j_3t_08_t_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==3))","ljets_ge4j_3t_08_t_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_08_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_08_t_ttH_ttlf_node.maxxval = 0.82
    interf_ljets_ge4j_3t_08_t_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_08_t_ttH_ttlf_node)
    
    interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_08_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_08_t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==4))")
    interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==4))","ljets_ge4j_3t_08_t_ttH_ttb_bb_node","")
    interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node.maxxval = 0.66
    interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_12_tH

    interf_ljets_ge4j_3t_12_tH_tH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_12_tH_node_tH",
                                            label          = "ljets_ge4j_3t_12_tH_tH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==0))")
    interf_ljets_ge4j_3t_12_tH_tH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==0))","ljets_ge4j_3t_12_tH_tH_node","")
    interf_ljets_ge4j_3t_12_tH_tH_node.minxval = 0.17
    interf_ljets_ge4j_3t_12_tH_tH_node.maxxval = 1.0
    interf_ljets_ge4j_3t_12_tH_tH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_12_tH_tH_node)
    
    interf_ljets_ge4j_3t_12_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_12_tH_node_ttH",
                                            label          = "ljets_ge4j_3t_12_tH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==1))")
    interf_ljets_ge4j_3t_12_tH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==1))","ljets_ge4j_3t_12_tH_ttH_node","")
    interf_ljets_ge4j_3t_12_tH_ttH_node.minxval = 0.17
    interf_ljets_ge4j_3t_12_tH_ttH_node.maxxval = 0.79
    interf_ljets_ge4j_3t_12_tH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_12_tH_ttH_node)
    
    interf_ljets_ge4j_3t_12_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_12_tH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_12_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==2))")
    interf_ljets_ge4j_3t_12_tH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==2))","ljets_ge4j_3t_12_tH_ttb_bb_node","")
    interf_ljets_ge4j_3t_12_tH_ttb_bb_node.minxval = 0.17
    interf_ljets_ge4j_3t_12_tH_ttb_bb_node.maxxval = 0.55
    interf_ljets_ge4j_3t_12_tH_ttb_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_12_tH_ttb_bb_node)
    
    interf_ljets_ge4j_3t_12_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_12_tH_node_tt2b",
                                            label          = "ljets_ge4j_3t_12_tH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==3))")
    interf_ljets_ge4j_3t_12_tH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==3))","ljets_ge4j_3t_12_tH_tt2b_node","")
    interf_ljets_ge4j_3t_12_tH_tt2b_node.minxval = 0.17
    interf_ljets_ge4j_3t_12_tH_tt2b_node.maxxval = 0.83
    interf_ljets_ge4j_3t_12_tH_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_12_tH_tt2b_node)
    
    interf_ljets_ge4j_3t_12_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_12_tH_node_ttcc",
                                            label          = "ljets_ge4j_3t_12_tH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==4))")
    interf_ljets_ge4j_3t_12_tH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==4))","ljets_ge4j_3t_12_tH_ttcc_node","")
    interf_ljets_ge4j_3t_12_tH_ttcc_node.minxval = 0.17
    interf_ljets_ge4j_3t_12_tH_ttcc_node.maxxval = 0.5
    interf_ljets_ge4j_3t_12_tH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_12_tH_ttcc_node)
    
    interf_ljets_ge4j_3t_12_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_12_tH_node_ttlf",
                                            label          = "ljets_ge4j_3t_12_tH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==5))")
    interf_ljets_ge4j_3t_12_tH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_12_tH==5))","ljets_ge4j_3t_12_tH_ttlf_node","")
    interf_ljets_ge4j_3t_12_tH_ttlf_node.minxval = 0.17
    interf_ljets_ge4j_3t_12_tH_ttlf_node.maxxval = 0.78
    interf_ljets_ge4j_3t_12_tH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_12_tH_ttlf_node)
    


    # plots for ge4j_3t_11_ttH

    interf_ljets_ge4j_3t_11_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_ttH",
                                            label          = "ljets_ge4j_3t_11_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==0))")
    interf_ljets_ge4j_3t_11_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==0))","ljets_ge4j_3t_11_ttH_ttH_node","")
    interf_ljets_ge4j_3t_11_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_11_ttH_ttH_node.maxxval = 0.87
    interf_ljets_ge4j_3t_11_ttH_ttH_node.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_ttH_node)
    
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_old_tt2b",
                                            label          = "ljets_ge4j_3t_11_ttH_old_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==1))")
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==1))","ljets_ge4j_3t_11_ttH_old_tt2b_node","")
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.maxxval = 0.87
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_old_tt2b_node)
    
    interf_ljets_ge4j_3t_11_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_11_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==2))")
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==2))","ljets_ge4j_3t_11_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.maxxval = 0.55
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_11_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_11_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==3))")
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==3))","ljets_ge4j_3t_11_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.maxxval = 0.81
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_ttlf_node)
    
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_old_ttb_bb",
                                            label          = "ljets_ge4j_3t_11_ttH_old_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==4))")
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==4))","ljets_ge4j_3t_11_ttH_old_ttb_bb_node","")
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node.maxxval = 0.76
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
    