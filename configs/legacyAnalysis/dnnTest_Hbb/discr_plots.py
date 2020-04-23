
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

    ndefaultbins = 15
    interfaces = []


    # plots for ge4j_ge4t_Hbb

    interf_ljets_ge4j_ge4t_Hbb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_ttHbb",
                                            label          = "ljets_ge4j_ge4t_Hbb_ttHbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==0))")
    interf_ljets_ge4j_ge4t_Hbb_ttHbb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==0))","ljets_ge4j_ge4t_Hbb_ttHbb_node","")
    interf_ljets_ge4j_ge4t_Hbb_ttHbb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_ttHbb_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hbb_ttHbb_node.maxxval = 0.88
    interf_ljets_ge4j_ge4t_Hbb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_ttHbb_node)
    
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_Hbb_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==1))")
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==1))","ljets_ge4j_ge4t_Hbb_ttmb_node","")
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node.maxxval = 0.76
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_ttmb_node)
    
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_Hbb_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==2))")
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==2))","ljets_ge4j_ge4t_Hbb_tt2b_node","")
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node.maxxval = 0.7
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_tt2b_node)
    
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_Hbb_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==3))")
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==3))","ljets_ge4j_ge4t_Hbb_ttcc_node","")
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node.maxxval = 0.62
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_ttcc_node)
    
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_Hbb_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==4))")
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==4))","ljets_ge4j_ge4t_Hbb_ttlf_node","")
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node.maxxval = 0.77
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_ttlf_node)
    
    interf_ljets_ge4j_ge4t_Hbb_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_tHq",
                                            label          = "ljets_ge4j_ge4t_Hbb_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==5))")
    interf_ljets_ge4j_ge4t_Hbb_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==5))","ljets_ge4j_ge4t_Hbb_tHq_node","")
    interf_ljets_ge4j_ge4t_Hbb_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_tHq_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hbb_tHq_node.maxxval = 0.99
    interf_ljets_ge4j_ge4t_Hbb_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_tHq_node)
    
    interf_ljets_ge4j_ge4t_Hbb_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_tHW",
                                            label          = "ljets_ge4j_ge4t_Hbb_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==6))")
    interf_ljets_ge4j_ge4t_Hbb_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==6))","ljets_ge4j_ge4t_Hbb_tHW_node","")
    interf_ljets_ge4j_ge4t_Hbb_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_tHW_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hbb_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_Hbb_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_tHW_node)
    


    # plots for ge4j_ge4t_Hincl

    interf_ljets_ge4j_ge4t_Hincl_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_ttH",
                                            label          = "ljets_ge4j_ge4t_Hincl_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==0))")
    interf_ljets_ge4j_ge4t_Hincl_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==0))","ljets_ge4j_ge4t_Hincl_ttH_node","")
    interf_ljets_ge4j_ge4t_Hincl_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_ttH_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hincl_ttH_node.maxxval = 0.83
    interf_ljets_ge4j_ge4t_Hincl_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_ttH_node)
    
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_Hincl_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==1))")
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==1))","ljets_ge4j_ge4t_Hincl_ttmb_node","")
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node.maxxval = 0.67
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_ttmb_node)
    
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_Hincl_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==2))")
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==2))","ljets_ge4j_ge4t_Hincl_tt2b_node","")
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node.maxxval = 0.69
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_tt2b_node)
    
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_Hincl_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==3))")
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==3))","ljets_ge4j_ge4t_Hincl_ttcc_node","")
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node.maxxval = 0.62
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_ttcc_node)
    
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_Hincl_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==4))")
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==4))","ljets_ge4j_ge4t_Hincl_ttlf_node","")
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node.maxxval = 0.79
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_ttlf_node)
    
    interf_ljets_ge4j_ge4t_Hincl_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_tHq",
                                            label          = "ljets_ge4j_ge4t_Hincl_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==5))")
    interf_ljets_ge4j_ge4t_Hincl_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==5))","ljets_ge4j_ge4t_Hincl_tHq_node","")
    interf_ljets_ge4j_ge4t_Hincl_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_tHq_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hincl_tHq_node.maxxval = 0.99
    interf_ljets_ge4j_ge4t_Hincl_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_tHq_node)
    
    interf_ljets_ge4j_ge4t_Hincl_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_tHW",
                                            label          = "ljets_ge4j_ge4t_Hincl_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==6))")
    interf_ljets_ge4j_ge4t_Hincl_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==6))","ljets_ge4j_ge4t_Hincl_tHW_node","")
    interf_ljets_ge4j_ge4t_Hincl_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_tHW_node.minxval = 0.14
    interf_ljets_ge4j_ge4t_Hincl_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_ge4t_Hincl_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_tHW_node)
    


    # plots for ge4j_3t_Hbb

    interf_ljets_ge4j_3t_Hbb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_ttHbb",
                                            label          = "ljets_ge4j_3t_Hbb_ttHbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==0))")
    interf_ljets_ge4j_3t_Hbb_ttHbb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==0))","ljets_ge4j_3t_Hbb_ttHbb_node","")
    interf_ljets_ge4j_3t_Hbb_ttHbb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_ttHbb_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hbb_ttHbb_node.maxxval = 0.86
    interf_ljets_ge4j_3t_Hbb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_ttHbb_node)
    
    interf_ljets_ge4j_3t_Hbb_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_ttmb",
                                            label          = "ljets_ge4j_3t_Hbb_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==1))")
    interf_ljets_ge4j_3t_Hbb_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==1))","ljets_ge4j_3t_Hbb_ttmb_node","")
    interf_ljets_ge4j_3t_Hbb_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hbb_ttmb_node.maxxval = 0.52
    interf_ljets_ge4j_3t_Hbb_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_ttmb_node)
    
    interf_ljets_ge4j_3t_Hbb_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_tt2b",
                                            label          = "ljets_ge4j_3t_Hbb_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==2))")
    interf_ljets_ge4j_3t_Hbb_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==2))","ljets_ge4j_3t_Hbb_tt2b_node","")
    interf_ljets_ge4j_3t_Hbb_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hbb_tt2b_node.maxxval = 0.8
    interf_ljets_ge4j_3t_Hbb_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_tt2b_node)
    
    interf_ljets_ge4j_3t_Hbb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_ttcc",
                                            label          = "ljets_ge4j_3t_Hbb_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==3))")
    interf_ljets_ge4j_3t_Hbb_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==3))","ljets_ge4j_3t_Hbb_ttcc_node","")
    interf_ljets_ge4j_3t_Hbb_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hbb_ttcc_node.maxxval = 0.84
    interf_ljets_ge4j_3t_Hbb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_ttcc_node)
    
    interf_ljets_ge4j_3t_Hbb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_ttlf",
                                            label          = "ljets_ge4j_3t_Hbb_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==4))")
    interf_ljets_ge4j_3t_Hbb_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==4))","ljets_ge4j_3t_Hbb_ttlf_node","")
    interf_ljets_ge4j_3t_Hbb_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hbb_ttlf_node.maxxval = 0.84
    interf_ljets_ge4j_3t_Hbb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_ttlf_node)
    
    interf_ljets_ge4j_3t_Hbb_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_tHq",
                                            label          = "ljets_ge4j_3t_Hbb_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==5))")
    interf_ljets_ge4j_3t_Hbb_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==5))","ljets_ge4j_3t_Hbb_tHq_node","")
    interf_ljets_ge4j_3t_Hbb_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_tHq_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hbb_tHq_node.maxxval = 0.99
    interf_ljets_ge4j_3t_Hbb_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_tHq_node)
    
    interf_ljets_ge4j_3t_Hbb_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_tHW",
                                            label          = "ljets_ge4j_3t_Hbb_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==6))")
    interf_ljets_ge4j_3t_Hbb_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==6))","ljets_ge4j_3t_Hbb_tHW_node","")
    interf_ljets_ge4j_3t_Hbb_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_tHW_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hbb_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_3t_Hbb_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_tHW_node)
    


    # plots for ge4j_3t_Hincl

    interf_ljets_ge4j_3t_Hincl_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_ttH",
                                            label          = "ljets_ge4j_3t_Hincl_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==0))")
    interf_ljets_ge4j_3t_Hincl_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==0))","ljets_ge4j_3t_Hincl_ttH_node","")
    interf_ljets_ge4j_3t_Hincl_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_ttH_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hincl_ttH_node.maxxval = 0.77
    interf_ljets_ge4j_3t_Hincl_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_ttH_node)
    
    interf_ljets_ge4j_3t_Hincl_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_ttmb",
                                            label          = "ljets_ge4j_3t_Hincl_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==1))")
    interf_ljets_ge4j_3t_Hincl_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==1))","ljets_ge4j_3t_Hincl_ttmb_node","")
    interf_ljets_ge4j_3t_Hincl_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hincl_ttmb_node.maxxval = 0.56
    interf_ljets_ge4j_3t_Hincl_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_ttmb_node)
    
    interf_ljets_ge4j_3t_Hincl_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_tt2b",
                                            label          = "ljets_ge4j_3t_Hincl_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==2))")
    interf_ljets_ge4j_3t_Hincl_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==2))","ljets_ge4j_3t_Hincl_tt2b_node","")
    interf_ljets_ge4j_3t_Hincl_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hincl_tt2b_node.maxxval = 0.8
    interf_ljets_ge4j_3t_Hincl_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_tt2b_node)
    
    interf_ljets_ge4j_3t_Hincl_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_ttcc",
                                            label          = "ljets_ge4j_3t_Hincl_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==3))")
    interf_ljets_ge4j_3t_Hincl_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==3))","ljets_ge4j_3t_Hincl_ttcc_node","")
    interf_ljets_ge4j_3t_Hincl_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hincl_ttcc_node.maxxval = 0.81
    interf_ljets_ge4j_3t_Hincl_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_ttcc_node)
    
    interf_ljets_ge4j_3t_Hincl_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_ttlf",
                                            label          = "ljets_ge4j_3t_Hincl_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==4))")
    interf_ljets_ge4j_3t_Hincl_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==4))","ljets_ge4j_3t_Hincl_ttlf_node","")
    interf_ljets_ge4j_3t_Hincl_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hincl_ttlf_node.maxxval = 0.86
    interf_ljets_ge4j_3t_Hincl_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_ttlf_node)
    
    interf_ljets_ge4j_3t_Hincl_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_tHq",
                                            label          = "ljets_ge4j_3t_Hincl_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==5))")
    interf_ljets_ge4j_3t_Hincl_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==5))","ljets_ge4j_3t_Hincl_tHq_node","")
    interf_ljets_ge4j_3t_Hincl_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_tHq_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hincl_tHq_node.maxxval = 0.99
    interf_ljets_ge4j_3t_Hincl_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_tHq_node)
    
    interf_ljets_ge4j_3t_Hincl_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_tHW",
                                            label          = "ljets_ge4j_3t_Hincl_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==6))")
    interf_ljets_ge4j_3t_Hincl_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==6))","ljets_ge4j_3t_Hincl_tHW_node","")
    interf_ljets_ge4j_3t_Hincl_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_tHW_node.minxval = 0.14
    interf_ljets_ge4j_3t_Hincl_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_3t_Hincl_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_tHW_node)
    

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
    