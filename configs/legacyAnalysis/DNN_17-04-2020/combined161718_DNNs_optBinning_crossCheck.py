
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


    # plots for preValidation_ge4j_3t

    interf_ljets_preValidation_ge4j_3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_3t_node_ttH",
                                            label          = "ljets_preValidation_ge4j_3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==0))")
    interf_ljets_preValidation_ge4j_3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==0))","ljets_preValidation_ge4j_3t_ttH_node","")
    interf_ljets_preValidation_ge4j_3t_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_preValidation_ge4j_3t_ttH_node.bin_edges = [ 
				0.14,
				0.176,
				0.212,
				0.248,
				0.284,
				0.32,
				0.356,
				0.392,
				0.428,
				0.464,
				0.5,
				0.68
				]
    interf_ljets_preValidation_ge4j_3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_3t_ttH_node)
    
    interf_ljets_preValidation_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_3t_node_ttmb",
                                            label          = "ljets_preValidation_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==1))")
    interf_ljets_preValidation_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==1))","ljets_preValidation_ge4j_3t_ttmb_node","")
    interf_ljets_preValidation_ge4j_3t_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_preValidation_ge4j_3t_ttmb_node.bin_edges = [ 
				0.1587,
				0.1773,
				0.196,
				0.2147,
				0.2333,
				0.252,
				0.2707,
				0.2893,
				0.308,
				0.3267,
				0.42
				]
    interf_ljets_preValidation_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_3t_ttmb_node)
    
    interf_ljets_preValidation_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_3t_node_tt2b",
                                            label          = "ljets_preValidation_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==2))")
    interf_ljets_preValidation_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==2))","ljets_preValidation_ge4j_3t_tt2b_node","")
    interf_ljets_preValidation_ge4j_3t_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_preValidation_ge4j_3t_tt2b_node.bin_edges = [ 
				0.14,
				# 0.194,
				# 0.248,
				# 0.302,
				# 0.356,
				# 0.41,
				# 0.464,
				# 0.518,
				# 0.572,
				0.95
				]
    interf_ljets_preValidation_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_3t_tt2b_node)
    
    interf_ljets_preValidation_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_3t_node_ttcc",
                                            label          = "ljets_preValidation_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==3))")
    interf_ljets_preValidation_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==3))","ljets_preValidation_ge4j_3t_ttcc_node","")
    interf_ljets_preValidation_ge4j_3t_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_preValidation_ge4j_3t_ttcc_node.bin_edges = [ 
				0.14,
				# 0.1693,
				# 0.1987,
				# 0.228,
				# 0.2573,
				# 0.2867,
				# 0.316,
				# 0.3453,
				# 0.3747,
				# 0.404,
				# 0.4333,
				# 0.4627,
				# 0.492,
				0.58
				]
    interf_ljets_preValidation_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_3t_ttcc_node)
    
    interf_ljets_preValidation_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_3t_node_ttlf",
                                            label          = "ljets_preValidation_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==4))")
    interf_ljets_preValidation_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==4))","ljets_preValidation_ge4j_3t_ttlf_node","")
    interf_ljets_preValidation_ge4j_3t_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_preValidation_ge4j_3t_ttlf_node.bin_edges = [ 
				0.14,
				# 0.1847,
				# 0.2293,
				# 0.274,
				# 0.3187,
				# 0.3633,
				# 0.408,
				# 0.4527,
				# 0.4973,
				# 0.542,
				# 0.5867,
				# 0.6313,
				# 0.676,
				0.81
				]
    interf_ljets_preValidation_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_3t_ttlf_node)
    
    interf_ljets_preValidation_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_3t_node_tHq",
                                            label          = "ljets_preValidation_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==5))")
    interf_ljets_preValidation_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==5))","ljets_preValidation_ge4j_3t_tHq_node","")
    interf_ljets_preValidation_ge4j_3t_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_preValidation_ge4j_3t_tHq_node.bin_edges = [ 
				0.14,
				0.1967,
				0.2533,
				0.31,
				0.3667,
				0.4233,
				0.48,
				0.5367,
				0.5933,
				0.65,
				0.7067,
				0.7633,
				0.82,
				0.8767,
				0.99
				]
    interf_ljets_preValidation_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_3t_tHq_node)
    
    interf_ljets_preValidation_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_3t_node_tHW",
                                            label          = "ljets_preValidation_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==6))")
    interf_ljets_preValidation_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_3t==6))","ljets_preValidation_ge4j_3t_tHW_node","")
    interf_ljets_preValidation_ge4j_3t_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_preValidation_ge4j_3t_tHW_node.bin_edges = [ 
				0.14,
				0.1973,
				0.2547,
				0.312,
				0.3693,
				0.4267,
				0.484,
				0.5413,
				0.5987,
				0.656,
				0.7133,
				0.7707,
				0.828,
				0.8853,
				0.9427,
				1.0
				]
    interf_ljets_preValidation_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_3t_tHW_node)
    


    # plots for preValidation_ge4j_ge4t

    interf_ljets_preValidation_ge4j_ge4t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_ge4t_node_ttH",
                                            label          = "ljets_preValidation_ge4j_ge4t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==0))")
    interf_ljets_preValidation_ge4j_ge4t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==0))","ljets_preValidation_ge4j_ge4t_ttH_node","")
    interf_ljets_preValidation_ge4j_ge4t_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_preValidation_ge4j_ge4t_ttH_node.bin_edges = [ 
				0.182,
				0.224,
				0.266,
				0.308,
				0.35,
				0.392,
				0.434,
				0.476,
				0.518,
				0.56,
				0.602,
				0.77
				]
    interf_ljets_preValidation_ge4j_ge4t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_ge4t_ttH_node)
    
    interf_ljets_preValidation_ge4j_ge4t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_ge4t_node_ttmb",
                                            label          = "ljets_preValidation_ge4j_ge4t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==1))")
    interf_ljets_preValidation_ge4j_ge4t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==1))","ljets_preValidation_ge4j_ge4t_ttmb_node","")
    interf_ljets_preValidation_ge4j_ge4t_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_preValidation_ge4j_ge4t_ttmb_node.bin_edges = [ 
				0.2,
				0.23,
				0.26,
				0.29,
				0.32,
				0.35,
				0.38,
				0.41,
				0.59
				]
    interf_ljets_preValidation_ge4j_ge4t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_ge4t_ttmb_node)
    
    interf_ljets_preValidation_ge4j_ge4t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_preValidation_ge4j_ge4t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==2))")
    interf_ljets_preValidation_ge4j_ge4t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==2))","ljets_preValidation_ge4j_ge4t_tt2b_node","")
    interf_ljets_preValidation_ge4j_ge4t_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_preValidation_ge4j_ge4t_tt2b_node.bin_edges = [ 
				0.1813,
				# 0.2227,
				# 0.264,
				# 0.3053,
				# 0.3467,
				0.76
				]
    interf_ljets_preValidation_ge4j_ge4t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_ge4t_tt2b_node)
    
    interf_ljets_preValidation_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_preValidation_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==3))")
    interf_ljets_preValidation_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==3))","ljets_preValidation_ge4j_ge4t_ttcc_node","")
    interf_ljets_preValidation_ge4j_ge4t_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_preValidation_ge4j_ge4t_ttcc_node.bin_edges = [ 
				0.14,
				# 0.1867,
				# 0.21,
				# 0.2333,
				# 0.2567,
				# 0.28,
				# 0.3033,
				# 0.3267,
				# 0.35,
				# 0.3733,
				# 0.3967,
				0.49
				]
    interf_ljets_preValidation_ge4j_ge4t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_ge4t_ttcc_node)
    
    interf_ljets_preValidation_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_preValidation_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==4))")
    interf_ljets_preValidation_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==4))","ljets_preValidation_ge4j_ge4t_ttlf_node","")
    interf_ljets_preValidation_ge4j_ge4t_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_preValidation_ge4j_ge4t_ttlf_node.bin_edges = [ 
				0.1767,
				# 0.2133,
				# 0.25,
				# 0.2867,
				# 0.3233,
				# 0.36,
				# 0.3967,
				# 0.4333,
				# 0.47,
				# 0.5067,
				# 0.5433,
				0.69
				]
    interf_ljets_preValidation_ge4j_ge4t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_ge4t_ttlf_node)
    
    interf_ljets_preValidation_ge4j_ge4t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_ge4t_node_tHq",
                                            label          = "ljets_preValidation_ge4j_ge4t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==5))")
    interf_ljets_preValidation_ge4j_ge4t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==5))","ljets_preValidation_ge4j_ge4t_tHq_node","")
    interf_ljets_preValidation_ge4j_ge4t_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_preValidation_ge4j_ge4t_tHq_node.bin_edges = [ 
				0.1967,
				0.2533,
				0.31,
				0.3667,
				0.4233,
				0.48,
				0.5367,
				0.5933,
				0.65,
				0.7067,
				0.7633,
				0.82,
				0.99
				]
    interf_ljets_preValidation_ge4j_ge4t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_ge4t_tHq_node)
    
    interf_ljets_preValidation_ge4j_ge4t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_preValidation_ge4j_ge4t_node_tHW",
                                            label          = "ljets_preValidation_ge4j_ge4t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==6))")
    interf_ljets_preValidation_ge4j_ge4t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_preValidation_ge4j_ge4t==6))","ljets_preValidation_ge4j_ge4t_tHW_node","")
    interf_ljets_preValidation_ge4j_ge4t_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_preValidation_ge4j_ge4t_tHW_node.bin_edges = [ 
				0.1973,
				0.2547,
				0.312,
				0.3693,
				0.4267,
				0.484,
				0.5413,
				0.5987,
				0.7133,
				0.8853,
				1.0
				]
    interf_ljets_preValidation_ge4j_ge4t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_preValidation_ge4j_ge4t_tHW_node)
    


    # plots for v1_ge4j_3t

    interf_ljets_v1_ge4j_3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v1_ge4j_3t_node_ttH",
                                            label          = "ljets_v1_ge4j_3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==0))")
    interf_ljets_v1_ge4j_3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==0))","ljets_v1_ge4j_3t_ttH_node","")
    interf_ljets_v1_ge4j_3t_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_v1_ge4j_3t_ttH_node.bin_edges = [ 
				0.14,
				0.1753,
				0.2107,
				0.246,
				0.2813,
				0.3167,
				0.352,
				0.3873,
				0.4227,
				0.458,
				0.4933,
				0.67
				]
    interf_ljets_v1_ge4j_3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v1_ge4j_3t_ttH_node)
    
    interf_ljets_v1_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v1_ge4j_3t_node_ttmb",
                                            label          = "ljets_v1_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==1))")
    interf_ljets_v1_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==1))","ljets_v1_ge4j_3t_ttmb_node","")
    interf_ljets_v1_ge4j_3t_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_v1_ge4j_3t_ttmb_node.bin_edges = [ 
				0.1567,
				0.1733,
				0.19,
				0.2067,
				0.2233,
				0.24,
				0.2567,
				0.2733,
				0.29,
				0.3067,
				0.3233,
				0.34,
				0.39
				]
    interf_ljets_v1_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v1_ge4j_3t_ttmb_node)
    
    interf_ljets_v1_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v1_ge4j_3t_node_tt2b",
                                            label          = "ljets_v1_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==2))")
    interf_ljets_v1_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==2))","ljets_v1_ge4j_3t_tt2b_node","")
    interf_ljets_v1_ge4j_3t_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_v1_ge4j_3t_tt2b_node.bin_edges = [ 
				0.14,
				# 0.19,
				# 0.24,
				# 0.29,
				# 0.34,
				# 0.39,
				# 0.44,
				# 0.49,
				# 0.54,
				0.89
				]
    interf_ljets_v1_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v1_ge4j_3t_tt2b_node)
    
    interf_ljets_v1_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v1_ge4j_3t_node_ttcc",
                                            label          = "ljets_v1_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==3))")
    interf_ljets_v1_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==3))","ljets_v1_ge4j_3t_ttcc_node","")
    interf_ljets_v1_ge4j_3t_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_v1_ge4j_3t_ttcc_node.bin_edges = [ 
				0.14,
				# 0.172,
				# 0.204,
				# 0.236,
				# 0.268,
				# 0.3,
				# 0.332,
				# 0.364,
				# 0.396,
				# 0.428,
				# 0.46,
				# 0.492,
				0.62
				]
    interf_ljets_v1_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v1_ge4j_3t_ttcc_node)
    
    interf_ljets_v1_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v1_ge4j_3t_node_ttlf",
                                            label          = "ljets_v1_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==4))")
    interf_ljets_v1_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==4))","ljets_v1_ge4j_3t_ttlf_node","")
    interf_ljets_v1_ge4j_3t_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_v1_ge4j_3t_ttlf_node.bin_edges = [ 
				0.14,
				# 0.1793,
				# 0.2187,
				# 0.258,
				# 0.2973,
				# 0.3367,
				# 0.376,
				# 0.4153,
				# 0.4547,
				# 0.494,
				# 0.5333,
				# 0.5727,
				# 0.612,
				0.73
				]
    interf_ljets_v1_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v1_ge4j_3t_ttlf_node)
    
    interf_ljets_v1_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v1_ge4j_3t_node_tHq",
                                            label          = "ljets_v1_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==5))")
    interf_ljets_v1_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==5))","ljets_v1_ge4j_3t_tHq_node","")
    interf_ljets_v1_ge4j_3t_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_v1_ge4j_3t_tHq_node.bin_edges = [ 
				0.14,
				0.1967,
				0.2533,
				0.31,
				0.3667,
				0.4233,
				0.48,
				0.5367,
				0.5933,
				0.65,
				0.7067,
				0.7633,
				0.82,
				0.8767,
				0.99
				]
    interf_ljets_v1_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v1_ge4j_3t_tHq_node)
    
    interf_ljets_v1_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v1_ge4j_3t_node_tHW",
                                            label          = "ljets_v1_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==6))")
    interf_ljets_v1_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_v1_ge4j_3t==6))","ljets_v1_ge4j_3t_tHW_node","")
    interf_ljets_v1_ge4j_3t_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_v1_ge4j_3t_tHW_node.bin_edges = [ 
				0.14,
				0.1973,
				0.2547,
				0.312,
				0.3693,
				0.4267,
				0.484,
				0.5413,
				0.5987,
				0.656,
				0.7133,
				0.7707,
				0.828,
				0.8853,
				0.9427,
				1.0
				]
    interf_ljets_v1_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v1_ge4j_3t_tHW_node)
    


    # plots for v3_ge4j_ge4t

    interf_ljets_v3_ge4j_ge4t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v3_ge4j_ge4t_node_ttH",
                                            label          = "ljets_v3_ge4j_ge4t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==0))")
    interf_ljets_v3_ge4j_ge4t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==0))","ljets_v3_ge4j_ge4t_ttH_node","")
    interf_ljets_v3_ge4j_ge4t_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_v3_ge4j_ge4t_ttH_node.bin_edges = [ 
				0.1827,
				0.2253,
				0.268,
				0.3107,
				0.3533,
				0.396,
				0.4387,
				0.4813,
				0.524,
				0.5667,
				0.6093,
				0.78
				]
    interf_ljets_v3_ge4j_ge4t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v3_ge4j_ge4t_ttH_node)
    
    interf_ljets_v3_ge4j_ge4t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v3_ge4j_ge4t_node_ttmb",
                                            label          = "ljets_v3_ge4j_ge4t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==1))")
    interf_ljets_v3_ge4j_ge4t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==1))","ljets_v3_ge4j_ge4t_ttmb_node","")
    interf_ljets_v3_ge4j_ge4t_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_v3_ge4j_ge4t_ttmb_node.bin_edges = [ 
				0.1693,
				0.1987,
				0.228,
				0.2573,
				0.2867,
				0.316,
				0.3453,
				0.3747,
				0.404,
				0.58
				]
    interf_ljets_v3_ge4j_ge4t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v3_ge4j_ge4t_ttmb_node)
    
    interf_ljets_v3_ge4j_ge4t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v3_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_v3_ge4j_ge4t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==2))")
    interf_ljets_v3_ge4j_ge4t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==2))","ljets_v3_ge4j_ge4t_tt2b_node","")
    interf_ljets_v3_ge4j_ge4t_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_v3_ge4j_ge4t_tt2b_node.bin_edges = [ 
				0.1747,
				# 0.2093,
				# 0.244,
				# 0.2787,
				# 0.3133,
				# 0.348,
				0.66
				]
    interf_ljets_v3_ge4j_ge4t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v3_ge4j_ge4t_tt2b_node)
    
    interf_ljets_v3_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v3_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_v3_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==3))")
    interf_ljets_v3_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==3))","ljets_v3_ge4j_ge4t_ttcc_node","")
    interf_ljets_v3_ge4j_ge4t_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_v3_ge4j_ge4t_ttcc_node.bin_edges = [ 
				0.188,
				# 0.212,
				# 0.236,
				# 0.26,
				# 0.284,
				# 0.308,
				# 0.332,
				# 0.356,
				# 0.38,
				0.5
				]
    interf_ljets_v3_ge4j_ge4t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v3_ge4j_ge4t_ttcc_node)
    
    interf_ljets_v3_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v3_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_v3_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==4))")
    interf_ljets_v3_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==4))","ljets_v3_ge4j_ge4t_ttlf_node","")
    interf_ljets_v3_ge4j_ge4t_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_v3_ge4j_ge4t_ttlf_node.bin_edges = [ 
				0.174,
				# 0.208,
				# 0.242,
				# 0.276,
				# 0.31,
				# 0.344,
				# 0.378,
				# 0.412,
				# 0.446,
				# 0.48,
				# 0.514,
				0.65
				]
    interf_ljets_v3_ge4j_ge4t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v3_ge4j_ge4t_ttlf_node)
    
    interf_ljets_v3_ge4j_ge4t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v3_ge4j_ge4t_node_tHq",
                                            label          = "ljets_v3_ge4j_ge4t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==5))")
    interf_ljets_v3_ge4j_ge4t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==5))","ljets_v3_ge4j_ge4t_tHq_node","")
    interf_ljets_v3_ge4j_ge4t_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_v3_ge4j_ge4t_tHq_node.bin_edges = [ 
				0.1967,
				0.2533,
				0.31,
				0.3667,
				0.4233,
				0.48,
				0.5367,
				0.5933,
				0.65,
				0.7067,
				0.82,
				0.99
				]
    interf_ljets_v3_ge4j_ge4t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v3_ge4j_ge4t_tHq_node)
    
    interf_ljets_v3_ge4j_ge4t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_v3_ge4j_ge4t_node_tHW",
                                            label          = "ljets_v3_ge4j_ge4t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==6))")
    interf_ljets_v3_ge4j_ge4t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_v3_ge4j_ge4t==6))","ljets_v3_ge4j_ge4t_tHW_node","")
    interf_ljets_v3_ge4j_ge4t_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_v3_ge4j_ge4t_tHW_node.bin_edges = [ 
				0.1973,
				0.2547,
				0.312,
				0.3693,
				0.4267,
				0.484,
				0.5413,
				0.656,
				0.828,
				1.0
				]
    interf_ljets_v3_ge4j_ge4t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_v3_ge4j_ge4t_tHW_node)
    

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
    