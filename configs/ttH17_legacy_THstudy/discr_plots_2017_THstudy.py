
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



def plots_dnn(data, discrname):

    ndefaultbins = 10
    interfaces = []


    # plots for ge4j_ge4t_07_ttH

    interf_ljets_ge4j_ge4t_07_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==0))")
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==0))","ljets_ge4j_ge4t_07_ttH_ttH_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.maxxval = 0.84
    interf_ljets_ge4j_ge4t_07_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttH_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_07_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==1))")
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==1))","ljets_ge4j_ge4t_07_ttH_tt2b_node","")
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.maxxval = 0.86
    interf_ljets_ge4j_ge4t_07_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==2))")
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==2))","ljets_ge4j_ge4t_07_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.maxxval = 0.54
    interf_ljets_ge4j_ge4t_07_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==3))")
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==3))","ljets_ge4j_ge4t_07_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.maxxval = 0.79
    interf_ljets_ge4j_ge4t_07_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttlf_node)
    
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_07_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_07_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==4))")
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_07_ttH==4))","ljets_ge4j_ge4t_07_ttH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.maxxval = 0.68
    interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_07_ttH_ttb_bb_node)
    


    # plots for ge4j_ge4t_08_t_ttH

    interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_08_t_ttH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_08_t_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==0))")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==0))","ljets_ge4j_ge4t_08_t_ttH_ttH_node","")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node.maxxval = 0.8
    interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_08_t_ttH_ttH_node)
    
    interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_08_t_ttH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_08_t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==1))")
    interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==1))","ljets_ge4j_ge4t_08_t_ttH_tt2b_node","")
    interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node.maxxval = 0.74
    interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_08_t_ttH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_08_t_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_08_t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==2))")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==2))","ljets_ge4j_ge4t_08_t_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node.maxxval = 0.55
    interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_08_t_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_08_t_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_08_t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==3))")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==3))","ljets_ge4j_ge4t_08_t_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node.maxxval = 0.76
    interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_08_t_ttH_ttlf_node)
    
    interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_08_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==4))")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_08_t_ttH==4))","ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node.maxxval = 0.73
    interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_08_t_ttH_ttb_bb_node)
    


    # plots for ge4j_ge4t_11_ttH

    interf_ljets_ge4j_ge4t_11_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_11_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==0))")
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==0))","ljets_ge4j_ge4t_11_ttH_ttH_node","")
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.maxxval = 0.82
    interf_ljets_ge4j_ge4t_11_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_ttH_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_old_tt2b",
                                            label          = "ljets_ge4j_ge4t_11_ttH_old_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==1))")
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==1))","ljets_ge4j_ge4t_11_ttH_old_tt2b_node","")
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.maxxval = 0.67
    interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_old_tt2b_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_11_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==2))")
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==2))","ljets_ge4j_ge4t_11_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.maxxval = 0.53
    interf_ljets_ge4j_ge4t_11_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_11_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==3))")
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==3))","ljets_ge4j_ge4t_11_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.maxxval = 0.73
    interf_ljets_ge4j_ge4t_11_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_ttlf_node)
    
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_11_ttH_node_old_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==4))")
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_11_ttH==4))","ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.maxxval = 0.76
    interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_11_ttH_old_ttb_bb_node)
    


    # plots for ge3j_ge3t_ge1f_04_t_ttH

    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_04_t_ttH_node_t_ttH",
                                            label          = "ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==0))")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==0))","ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node","")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node.maxxval = 0.98
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_t_ttH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_04_t_ttH_node_tt2b",
                                            label          = "ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==1))")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==1))","ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node","")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node.maxxval = 0.93
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_tt2b_node)
    
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_04_t_ttH_node_ttcc",
                                            label          = "ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==2))")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==2))","ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node","")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node.maxxval = 0.58
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttcc_node)
    
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_04_t_ttH_node_ttlf",
                                            label          = "ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==3))")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==3))","ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node","")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node.maxxval = 0.82
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttlf_node)
    
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_04_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==4))")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_04_t_ttH==4))","ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node","")
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node.maxxval = 0.78
    interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_04_t_ttH_ttb_bb_node)
    


    # plots for ge3j_ge3t_ge1f_02_ttH

    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_02_ttH_node_ttH",
                                            label          = "ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==0))")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==0))","ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node","")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node.maxxval = 0.88
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_02_ttH_node_tt2b",
                                            label          = "ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==1))")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==1))","ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node","")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node.maxxval = 0.95
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_02_ttH_tt2b_node)
    
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_02_ttH_node_ttcc",
                                            label          = "ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==2))")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==2))","ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node","")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node.maxxval = 0.57
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttcc_node)
    
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_02_ttH_node_ttlf",
                                            label          = "ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==3))")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==3))","ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node","")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node.maxxval = 0.85
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttlf_node)
    
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_02_ttH_node_ttb_bb",
                                            label          = "ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==4))")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_02_ttH==4))","ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node","")
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node.maxxval = 0.74
    interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_02_ttH_ttb_bb_node)
    


    # plots for ge3j_ge3t_ge1f_01_tH

    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_ttH",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_ttH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==0))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==0))","ljets_ge3j_ge3t_ge1f_01_tH_ttH_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node.maxxval = 0.84
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_ttH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_tH",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_tH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==1))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==1))","ljets_ge3j_ge3t_ge1f_01_tH_tH_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node.maxxval = 1.0
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_tH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_tt2b",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==2))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==2))","ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node.maxxval = 0.96
    interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_tt2b_node)
    
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_ttcc",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==3))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==3))","ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node.maxxval = 0.57
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_ttcc_node)
    
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_ttlf",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==4))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==4))","ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node.maxxval = 0.8
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_ttlf_node)
    
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_01_tH_node_ttb_bb",
                                            label          = "ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==5))")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_01_tH==5))","ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node","")
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node.minxval = 0.17
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node.maxxval = 0.7
    interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_01_tH_ttb_bb_node)
    


    # plots for ge3j_ge3t_ge1f_03_tHQtHW

    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_ttH",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==0))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==0))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node.maxxval = 0.77
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttH_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_tHQ",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==1))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==1))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node.maxxval = 0.99
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHQ_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_tHW",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==2))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==2))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node.maxxval = 1.0
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tHW_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_tt2b",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==3))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==3))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node.maxxval = 0.93
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_tt2b_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_ttcc",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==4))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==4))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node.maxxval = 0.5
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttcc_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_ttlf",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==5))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==5))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node.maxxval = 0.79
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttlf_node)
    
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge3j_ge3t_ge1f_03_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==6))")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node.category = ("((N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)&&(1.)&&(DNNPredictedClass_ge3j_ge3t_ge1f_03_tHQtHW==6))","ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node","")
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node.minxval = 0.14
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node.maxxval = 0.63
    interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge3j_ge3t_ge1f_03_tHQtHW_ttb_bb_node)
    


    # plots for ge4J_3t_09_ttH

    interf_ljets_ge4J_3t_09_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_09_ttH_node_ttH",
                                            label          = "ljets_ge4J_3t_09_ttH_ttH_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==0))")
    interf_ljets_ge4J_3t_09_ttH_ttH_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==0))","ljets_ge4J_3t_09_ttH_ttH_node","")
    interf_ljets_ge4J_3t_09_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4J_3t_09_ttH_ttH_node.maxxval = 0.92
    interf_ljets_ge4J_3t_09_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_3t_09_ttH_ttH_node)
    
    interf_ljets_ge4J_3t_09_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_09_ttH_node_tt2b",
                                            label          = "ljets_ge4J_3t_09_ttH_tt2b_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==1))")
    interf_ljets_ge4J_3t_09_ttH_tt2b_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==1))","ljets_ge4J_3t_09_ttH_tt2b_node","")
    interf_ljets_ge4J_3t_09_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4J_3t_09_ttH_tt2b_node.maxxval = 0.85
    interf_ljets_ge4J_3t_09_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_3t_09_ttH_tt2b_node)
    
    interf_ljets_ge4J_3t_09_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_09_ttH_node_ttcc",
                                            label          = "ljets_ge4J_3t_09_ttH_ttcc_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==2))")
    interf_ljets_ge4J_3t_09_ttH_ttcc_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==2))","ljets_ge4J_3t_09_ttH_ttcc_node","")
    interf_ljets_ge4J_3t_09_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4J_3t_09_ttH_ttcc_node.maxxval = 0.57
    interf_ljets_ge4J_3t_09_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_3t_09_ttH_ttcc_node)
    
    interf_ljets_ge4J_3t_09_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_09_ttH_node_ttlf",
                                            label          = "ljets_ge4J_3t_09_ttH_ttlf_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==3))")
    interf_ljets_ge4J_3t_09_ttH_ttlf_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==3))","ljets_ge4J_3t_09_ttH_ttlf_node","")
    interf_ljets_ge4J_3t_09_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4J_3t_09_ttH_ttlf_node.maxxval = 0.81
    interf_ljets_ge4J_3t_09_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_3t_09_ttH_ttlf_node)
    
    interf_ljets_ge4J_3t_09_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_09_ttH_node_ttb_bb",
                                            label          = "ljets_ge4J_3t_09_ttH_ttb_bb_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==4))")
    interf_ljets_ge4J_3t_09_ttH_ttb_bb_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_09_ttH==4))","ljets_ge4J_3t_09_ttH_ttb_bb_node","")
    interf_ljets_ge4J_3t_09_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4J_3t_09_ttH_ttb_bb_node.maxxval = 0.69
    interf_ljets_ge4J_3t_09_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_3t_09_ttH_ttb_bb_node)
    


    # plots for ge4J_3t_10_t_ttH

    interf_ljets_ge4J_3t_10_t_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_10_t_ttH_node_ttH",
                                            label          = "ljets_ge4J_3t_10_t_ttH_ttH_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==0))")
    interf_ljets_ge4J_3t_10_t_ttH_ttH_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==0))","ljets_ge4J_3t_10_t_ttH_ttH_node","")
    interf_ljets_ge4J_3t_10_t_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4J_3t_10_t_ttH_ttH_node.maxxval = 0.95
    interf_ljets_ge4J_3t_10_t_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_3t_10_t_ttH_ttH_node)
    
    interf_ljets_ge4J_3t_10_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_10_t_ttH_node_tt2b",
                                            label          = "ljets_ge4J_3t_10_t_ttH_tt2b_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==1))")
    interf_ljets_ge4J_3t_10_t_ttH_tt2b_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==1))","ljets_ge4J_3t_10_t_ttH_tt2b_node","")
    interf_ljets_ge4J_3t_10_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4J_3t_10_t_ttH_tt2b_node.maxxval = 0.85
    interf_ljets_ge4J_3t_10_t_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_3t_10_t_ttH_tt2b_node)
    
    interf_ljets_ge4J_3t_10_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_10_t_ttH_node_ttcc",
                                            label          = "ljets_ge4J_3t_10_t_ttH_ttcc_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==2))")
    interf_ljets_ge4J_3t_10_t_ttH_ttcc_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==2))","ljets_ge4J_3t_10_t_ttH_ttcc_node","")
    interf_ljets_ge4J_3t_10_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4J_3t_10_t_ttH_ttcc_node.maxxval = 0.59
    interf_ljets_ge4J_3t_10_t_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_3t_10_t_ttH_ttcc_node)
    
    interf_ljets_ge4J_3t_10_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_10_t_ttH_node_ttlf",
                                            label          = "ljets_ge4J_3t_10_t_ttH_ttlf_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==3))")
    interf_ljets_ge4J_3t_10_t_ttH_ttlf_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==3))","ljets_ge4J_3t_10_t_ttH_ttlf_node","")
    interf_ljets_ge4J_3t_10_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4J_3t_10_t_ttH_ttlf_node.maxxval = 0.84
    interf_ljets_ge4J_3t_10_t_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_3t_10_t_ttH_ttlf_node)
    
    interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_3t_10_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4J_3t_10_t_ttH_ttb_bb_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==4))")
    interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4J_3t_10_t_ttH==4))","ljets_ge4J_3t_10_t_ttH_ttb_bb_node","")
    interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node.maxxval = 0.71
    interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_3t_10_t_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_0f_04_t_ttH

    interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_04_t_ttH_node_t_ttH",
                                            label          = "ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==0))")
    interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==0))","ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node","")
    interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node.maxxval = 0.99
    interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_04_t_ttH_t_ttH_node)
    
    interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_04_t_ttH_node_tt2b",
                                            label          = "ljets_ge4j_3t_0f_04_t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==1))")
    interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==1))","ljets_ge4j_3t_0f_04_t_ttH_tt2b_node","")
    interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node.maxxval = 0.96
    interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_04_t_ttH_tt2b_node)
    
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_04_t_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_0f_04_t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==2))")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==2))","ljets_ge4j_3t_0f_04_t_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node.maxxval = 0.65
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_04_t_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_04_t_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_0f_04_t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==3))")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==3))","ljets_ge4j_3t_0f_04_t_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node.maxxval = 0.82
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_04_t_ttH_ttlf_node)
    
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_04_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==4))")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_04_t_ttH==4))","ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node","")
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node.maxxval = 0.71
    interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_04_t_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_0f_02_ttH

    interf_ljets_ge4j_3t_0f_02_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_02_ttH_node_ttH",
                                            label          = "ljets_ge4j_3t_0f_02_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==0))")
    interf_ljets_ge4j_3t_0f_02_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==0))","ljets_ge4j_3t_0f_02_ttH_ttH_node","")
    interf_ljets_ge4j_3t_0f_02_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_02_ttH_ttH_node.maxxval = 0.91
    interf_ljets_ge4j_3t_0f_02_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_02_ttH_ttH_node)
    
    interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_02_ttH_node_tt2b",
                                            label          = "ljets_ge4j_3t_0f_02_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==1))")
    interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==1))","ljets_ge4j_3t_0f_02_ttH_tt2b_node","")
    interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node.maxxval = 0.97
    interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_02_ttH_tt2b_node)
    
    interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_02_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_0f_02_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==2))")
    interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==2))","ljets_ge4j_3t_0f_02_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node.maxxval = 0.6
    interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_02_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_02_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_0f_02_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==3))")
    interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==3))","ljets_ge4j_3t_0f_02_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node.maxxval = 0.81
    interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_02_ttH_ttlf_node)
    
    interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_02_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_0f_02_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==4))")
    interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_02_ttH==4))","ljets_ge4j_3t_0f_02_ttH_ttb_bb_node","")
    interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node.maxxval = 0.73
    interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_02_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_0f_01_tH

    interf_ljets_ge4j_3t_0f_01_tH_tH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_tH",
                                            label          = "ljets_ge4j_3t_0f_01_tH_tH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==0))")
    interf_ljets_ge4j_3t_0f_01_tH_tH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==0))","ljets_ge4j_3t_0f_01_tH_tH_node","")
    interf_ljets_ge4j_3t_0f_01_tH_tH_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_tH_node.maxxval = 1.0
    interf_ljets_ge4j_3t_0f_01_tH_tH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_tH_node)
    
    interf_ljets_ge4j_3t_0f_01_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_ttH",
                                            label          = "ljets_ge4j_3t_0f_01_tH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==1))")
    interf_ljets_ge4j_3t_0f_01_tH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==1))","ljets_ge4j_3t_0f_01_tH_ttH_node","")
    interf_ljets_ge4j_3t_0f_01_tH_ttH_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_ttH_node.maxxval = 0.77
    interf_ljets_ge4j_3t_0f_01_tH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_ttH_node)
    
    interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_0f_01_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==2))")
    interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==2))","ljets_ge4j_3t_0f_01_tH_ttb_bb_node","")
    interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node.maxxval = 0.64
    interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_ttb_bb_node)
    
    interf_ljets_ge4j_3t_0f_01_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_tt2b",
                                            label          = "ljets_ge4j_3t_0f_01_tH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==3))")
    interf_ljets_ge4j_3t_0f_01_tH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==3))","ljets_ge4j_3t_0f_01_tH_tt2b_node","")
    interf_ljets_ge4j_3t_0f_01_tH_tt2b_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_tt2b_node.maxxval = 0.94
    interf_ljets_ge4j_3t_0f_01_tH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_tt2b_node)
    
    interf_ljets_ge4j_3t_0f_01_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_ttcc",
                                            label          = "ljets_ge4j_3t_0f_01_tH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==4))")
    interf_ljets_ge4j_3t_0f_01_tH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==4))","ljets_ge4j_3t_0f_01_tH_ttcc_node","")
    interf_ljets_ge4j_3t_0f_01_tH_ttcc_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_ttcc_node.maxxval = 0.51
    interf_ljets_ge4j_3t_0f_01_tH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_ttcc_node)
    
    interf_ljets_ge4j_3t_0f_01_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_01_tH_node_ttlf",
                                            label          = "ljets_ge4j_3t_0f_01_tH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==5))")
    interf_ljets_ge4j_3t_0f_01_tH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_01_tH==5))","ljets_ge4j_3t_0f_01_tH_ttlf_node","")
    interf_ljets_ge4j_3t_0f_01_tH_ttlf_node.minxval = 0.17
    interf_ljets_ge4j_3t_0f_01_tH_ttlf_node.maxxval = 0.8
    interf_ljets_ge4j_3t_0f_01_tH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_01_tH_ttlf_node)
    


    # plots for ge4j_3t_0f_03_tHQtHW

    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_tHW",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==0))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==0))","ljets_ge4j_3t_0f_03_tHQtHW_tHW_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_tHW_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_tHQ",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==1))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==1))","ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node.maxxval = 0.99
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_tHQ_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_ttH",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==2))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==2))","ljets_ge4j_3t_0f_03_tHQtHW_ttH_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node.maxxval = 0.7
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_ttH_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==3))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==3))","ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node.maxxval = 0.6
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_ttb_bb_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_tt2b",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==4))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==4))","ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node.maxxval = 0.94
    interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_tt2b_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_ttcc",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==5))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==5))","ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node.maxxval = 0.47
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_ttcc_node)
    
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_0f_03_tHQtHW_node_ttlf",
                                            label          = "ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==6))")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_3t_0f_03_tHQtHW==6))","ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node","")
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node.maxxval = 0.79
    interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_0f_03_tHQtHW_ttlf_node)
    


    # plots for ge4j_ge4t_0f_04_t_ttH

    interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_04_t_ttH_node_t_ttH",
                                            label          = "ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==0))")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==0))","ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node","")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node.maxxval = 0.81
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_04_t_ttH_t_ttH_node)
    
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_04_t_ttH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==1))")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==1))","ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node","")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node.maxxval = 0.91
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_04_t_ttH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_04_t_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==2))")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==2))","ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node.maxxval = 0.68
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_04_t_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==3))")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==3))","ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node.maxxval = 0.87
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttlf_node)
    
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_04_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==4))")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_04_t_ttH==4))","ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node.maxxval = 0.75
    interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_04_t_ttH_ttb_bb_node)
    


    # plots for ge4j_ge4t_0f_02_ttH

    interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_02_ttH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_0f_02_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==0))")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==0))","ljets_ge4j_ge4t_0f_02_ttH_ttH_node","")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node.maxxval = 0.81
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_02_ttH_ttH_node)
    
    interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_02_ttH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_0f_02_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==1))")
    interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==1))","ljets_ge4j_ge4t_0f_02_ttH_tt2b_node","")
    interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node.maxxval = 0.91
    interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_02_ttH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_02_ttH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_0f_02_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==2))")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==2))","ljets_ge4j_ge4t_0f_02_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node.maxxval = 0.6
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_02_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_02_ttH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_0f_02_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==3))")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==3))","ljets_ge4j_ge4t_0f_02_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node.maxxval = 0.84
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_02_ttH_ttlf_node)
    
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_02_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==4))")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_02_ttH==4))","ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node.maxxval = 0.77
    interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_02_ttH_ttb_bb_node)
    


    # plots for ge4j_ge4t_0f_01_tH

    interf_ljets_ge4j_ge4t_0f_01_tH_tH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_tH",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_tH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==0))")
    interf_ljets_ge4j_ge4t_0f_01_tH_tH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==0))","ljets_ge4j_ge4t_0f_01_tH_tH_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_tH_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_tH_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_0f_01_tH_tH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_tH_node)
    
    interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_ttH",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==1))")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==1))","ljets_ge4j_ge4t_0f_01_tH_ttH_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node.maxxval = 0.81
    interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_ttH_node)
    
    interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==2))")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==2))","ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node.maxxval = 0.73
    interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==3))")
    interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==3))","ljets_ge4j_ge4t_0f_01_tH_tt2b_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node.maxxval = 0.93
    interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==4))")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==4))","ljets_ge4j_ge4t_0f_01_tH_ttcc_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node.maxxval = 0.64
    interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_01_tH_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_0f_01_tH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==5))")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_01_tH==5))","ljets_ge4j_ge4t_0f_01_tH_ttlf_node","")
    interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node.minxval = 0.17
    interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node.maxxval = 0.76
    interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_01_tH_ttlf_node)
    


    # plots for ge4j_ge4t_0f_03_tHQtHW

    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_tHW",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==0))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==0))","ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHW_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_tHQ",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==1))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==1))","ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node.maxxval = 0.97
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tHQ_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_ttH",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==2))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==2))","ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node.maxxval = 0.75
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttH_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==3))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==3))","ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node.maxxval = 0.64
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==4))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==4))","ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node.maxxval = 0.91
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_tt2b_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==5))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==5))","ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node.maxxval = 0.59
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttcc_node)
    
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_0f_03_tHQtHW_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==6))")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_0f_03_tHQtHW==6))","ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node","")
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node.maxxval = 0.85
    interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_ge4t_0f_03_tHQtHW_ttlf_node)
    


    # plots for ge4J_ge4t_09_ttH

    interf_ljets_ge4J_ge4t_09_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_09_ttH_node_ttH",
                                            label          = "ljets_ge4J_ge4t_09_ttH_ttH_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==0))")
    interf_ljets_ge4J_ge4t_09_ttH_ttH_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==0))","ljets_ge4J_ge4t_09_ttH_ttH_node","")
    interf_ljets_ge4J_ge4t_09_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_09_ttH_ttH_node.maxxval = 0.83
    interf_ljets_ge4J_ge4t_09_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_ge4t_09_ttH_ttH_node)
    
    interf_ljets_ge4J_ge4t_09_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_09_ttH_node_tt2b",
                                            label          = "ljets_ge4J_ge4t_09_ttH_tt2b_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==1))")
    interf_ljets_ge4J_ge4t_09_ttH_tt2b_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==1))","ljets_ge4J_ge4t_09_ttH_tt2b_node","")
    interf_ljets_ge4J_ge4t_09_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_09_ttH_tt2b_node.maxxval = 0.79
    interf_ljets_ge4J_ge4t_09_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_ge4t_09_ttH_tt2b_node)
    
    interf_ljets_ge4J_ge4t_09_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_09_ttH_node_ttcc",
                                            label          = "ljets_ge4J_ge4t_09_ttH_ttcc_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==2))")
    interf_ljets_ge4J_ge4t_09_ttH_ttcc_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==2))","ljets_ge4J_ge4t_09_ttH_ttcc_node","")
    interf_ljets_ge4J_ge4t_09_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_09_ttH_ttcc_node.maxxval = 0.58
    interf_ljets_ge4J_ge4t_09_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_ge4t_09_ttH_ttcc_node)
    
    interf_ljets_ge4J_ge4t_09_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_09_ttH_node_ttlf",
                                            label          = "ljets_ge4J_ge4t_09_ttH_ttlf_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==3))")
    interf_ljets_ge4J_ge4t_09_ttH_ttlf_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==3))","ljets_ge4J_ge4t_09_ttH_ttlf_node","")
    interf_ljets_ge4J_ge4t_09_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_09_ttH_ttlf_node.maxxval = 0.82
    interf_ljets_ge4J_ge4t_09_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_ge4t_09_ttH_ttlf_node)
    
    interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_09_ttH_node_ttb_bb",
                                            label          = "ljets_ge4J_ge4t_09_ttH_ttb_bb_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==4))")
    interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_09_ttH==4))","ljets_ge4J_ge4t_09_ttH_ttb_bb_node","")
    interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node.maxxval = 0.79
    interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_ge4t_09_ttH_ttb_bb_node)
    


    # plots for ge4J_ge4t_10_t_ttH

    interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_10_t_ttH_node_ttH",
                                            label          = "ljets_ge4J_ge4t_10_t_ttH_ttH_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==0))")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==0))","ljets_ge4J_ge4t_10_t_ttH_ttH_node","")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node.maxxval = 0.8
    interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4J_ge4t_10_t_ttH_ttH_node)
    
    interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_10_t_ttH_node_tt2b",
                                            label          = "ljets_ge4J_ge4t_10_t_ttH_tt2b_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==1))")
    interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==1))","ljets_ge4J_ge4t_10_t_ttH_tt2b_node","")
    interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node.maxxval = 0.78
    interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_ge4t_10_t_ttH_tt2b_node)
    
    interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_10_t_ttH_node_ttcc",
                                            label          = "ljets_ge4J_ge4t_10_t_ttH_ttcc_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==2))")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==2))","ljets_ge4J_ge4t_10_t_ttH_ttcc_node","")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node.maxxval = 0.58
    interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_ge4t_10_t_ttH_ttcc_node)
    
    interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_10_t_ttH_node_ttlf",
                                            label          = "ljets_ge4J_ge4t_10_t_ttH_ttlf_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==3))")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==3))","ljets_ge4J_ge4t_10_t_ttH_ttlf_node","")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node.maxxval = 0.82
    interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_ge4t_10_t_ttH_ttlf_node)
    
    interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4J_ge4t_10_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node",
                                            selection      = "(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==4))")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node.category = ("(((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4J_ge4t_10_t_ttH==4))","ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node","")
    interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node.maxxval = 0.73
    interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4J_ge4t_10_t_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_07_ttH

    interf_ljets_ge4j_3t_07_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttH",
                                            label          = "ljets_ge4j_3t_07_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==0))")
    interf_ljets_ge4j_3t_07_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==0))","ljets_ge4j_3t_07_ttH_ttH_node","")
    interf_ljets_ge4j_3t_07_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_07_ttH_ttH_node.maxxval = 0.93
    interf_ljets_ge4j_3t_07_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttH_node)
    
    interf_ljets_ge4j_3t_07_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_tt2b",
                                            label          = "ljets_ge4j_3t_07_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==1))")
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==1))","ljets_ge4j_3t_07_ttH_tt2b_node","")
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.maxxval = 0.89
    interf_ljets_ge4j_3t_07_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_tt2b_node)
    
    interf_ljets_ge4j_3t_07_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_07_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==2))")
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==2))","ljets_ge4j_3t_07_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.maxxval = 0.66
    interf_ljets_ge4j_3t_07_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_07_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_07_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==3))")
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==3))","ljets_ge4j_3t_07_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.maxxval = 0.81
    interf_ljets_ge4j_3t_07_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttlf_node)
    
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_07_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_07_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==4))")
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_07_ttH==4))","ljets_ge4j_3t_07_ttH_ttb_bb_node","")
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.maxxval = 0.76
    interf_ljets_ge4j_3t_07_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_07_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_08_t_ttH

    interf_ljets_ge4j_3t_08_t_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_08_t_ttH_node_ttH",
                                            label          = "ljets_ge4j_3t_08_t_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==0))")
    interf_ljets_ge4j_3t_08_t_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==0))","ljets_ge4j_3t_08_t_ttH_ttH_node","")
    interf_ljets_ge4j_3t_08_t_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_08_t_ttH_ttH_node.maxxval = 0.87
    interf_ljets_ge4j_3t_08_t_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_08_t_ttH_ttH_node)
    
    interf_ljets_ge4j_3t_08_t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_08_t_ttH_node_tt2b",
                                            label          = "ljets_ge4j_3t_08_t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==1))")
    interf_ljets_ge4j_3t_08_t_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==1))","ljets_ge4j_3t_08_t_ttH_tt2b_node","")
    interf_ljets_ge4j_3t_08_t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_08_t_ttH_tt2b_node.maxxval = 0.85
    interf_ljets_ge4j_3t_08_t_ttH_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_08_t_ttH_tt2b_node)
    
    interf_ljets_ge4j_3t_08_t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_08_t_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_08_t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==2))")
    interf_ljets_ge4j_3t_08_t_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==2))","ljets_ge4j_3t_08_t_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_08_t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_08_t_ttH_ttcc_node.maxxval = 0.52
    interf_ljets_ge4j_3t_08_t_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_08_t_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_08_t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_08_t_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_08_t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==3))")
    interf_ljets_ge4j_3t_08_t_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==3))","ljets_ge4j_3t_08_t_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_08_t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_08_t_ttH_ttlf_node.maxxval = 0.82
    interf_ljets_ge4j_3t_08_t_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_08_t_ttH_ttlf_node)
    
    interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_08_t_ttH_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_08_t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==4))")
    interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_08_t_ttH==4))","ljets_ge4j_3t_08_t_ttH_ttb_bb_node","")
    interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node.maxxval = 0.66
    interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_08_t_ttH_ttb_bb_node)
    


    # plots for ge4j_3t_11_ttH

    interf_ljets_ge4j_3t_11_ttH_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_ttH",
                                            label          = "ljets_ge4j_3t_11_ttH_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==0))")
    interf_ljets_ge4j_3t_11_ttH_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==0))","ljets_ge4j_3t_11_ttH_ttH_node","")
    interf_ljets_ge4j_3t_11_ttH_ttH_node.minxval = 0.2
    interf_ljets_ge4j_3t_11_ttH_ttH_node.maxxval = 0.87
    interf_ljets_ge4j_3t_11_ttH_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_ttH_node)
    
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_old_tt2b",
                                            label          = "ljets_ge4j_3t_11_ttH_old_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==1))")
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==1))","ljets_ge4j_3t_11_ttH_old_tt2b_node","")
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.maxxval = 0.87
    interf_ljets_ge4j_3t_11_ttH_old_tt2b_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_old_tt2b_node)
    
    interf_ljets_ge4j_3t_11_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_ttcc",
                                            label          = "ljets_ge4j_3t_11_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==2))")
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==2))","ljets_ge4j_3t_11_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.maxxval = 0.55
    interf_ljets_ge4j_3t_11_ttH_ttcc_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_11_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_ttlf",
                                            label          = "ljets_ge4j_3t_11_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==3))")
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==3))","ljets_ge4j_3t_11_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.maxxval = 0.81
    interf_ljets_ge4j_3t_11_ttH_ttlf_node.nhistobins = 1
    interfaces.append(interf_ljets_ge4j_3t_11_ttH_ttlf_node)
    
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_11_ttH_node_old_ttb_bb",
                                            label          = "ljets_ge4j_3t_11_ttH_old_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==4))")
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_11_ttH==4))","ljets_ge4j_3t_11_ttH_old_ttb_bb_node","")
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node.maxxval = 0.76
    interf_ljets_ge4j_3t_11_ttH_old_ttb_bb_node.nhistobins = 1
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
    