
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
    interf_ljets_ge4j_ge4t_Hbb_ttHbb_node.bin_edges = [ 
				0.1893,
				0.2387,
				0.288,
				0.3373,
				0.3867,
				0.436,
				0.4853,
				0.5347,
				0.584,
				0.6333,
				0.6827,
				0.88
				]
    interf_ljets_ge4j_ge4t_Hbb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_ttHbb_node)
    
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_Hbb_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==1))")
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==1))","ljets_ge4j_ge4t_Hbb_ttmb_node","")
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node.bin_edges = [ 
				0.1813,
				0.2227,
				0.264,
				0.3053,
				0.3467,
				0.388,
				0.4293,
				0.4707,
				0.512,
				0.5533,
				0.76
				]
    interf_ljets_ge4j_ge4t_Hbb_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_ttmb_node)
    
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_Hbb_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==2))")
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==2))","ljets_ge4j_ge4t_Hbb_tt2b_node","")
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node.bin_edges = [ 
				0.2147,
				0.252,
				0.2893,
				0.3267,
				0.364,
				0.4013,
				0.476,
				0.7
				]
    interf_ljets_ge4j_ge4t_Hbb_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_tt2b_node)
    
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_Hbb_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==3))")
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==3))","ljets_ge4j_ge4t_Hbb_ttcc_node","")
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node.bin_edges = [ 
				0.204,
				0.236,
				0.268,
				0.3,
				0.332,
				0.364,
				0.396,
				0.428,
				0.62
				]
    interf_ljets_ge4j_ge4t_Hbb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_ttcc_node)
    
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_Hbb_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==4))")
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==4))","ljets_ge4j_ge4t_Hbb_ttlf_node","")
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node.bin_edges = [ 
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
				0.644,
				0.77
				]
    interf_ljets_ge4j_ge4t_Hbb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_ttlf_node)
    
    interf_ljets_ge4j_ge4t_Hbb_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_tHq",
                                            label          = "ljets_ge4j_ge4t_Hbb_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==5))")
    interf_ljets_ge4j_ge4t_Hbb_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==5))","ljets_ge4j_ge4t_Hbb_tHq_node","")
    interf_ljets_ge4j_ge4t_Hbb_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_tHq_node.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_Hbb_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_tHq_node)
    
    interf_ljets_ge4j_ge4t_Hbb_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hbb_node_tHW",
                                            label          = "ljets_ge4j_ge4t_Hbb_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==6))")
    interf_ljets_ge4j_ge4t_Hbb_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hbb==6))","ljets_ge4j_ge4t_Hbb_tHW_node","")
    interf_ljets_ge4j_ge4t_Hbb_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hbb_tHW_node.bin_edges = [ 
				0.1973,
				0.2547,
				0.312,
				0.3693,
				0.4267,
				0.484,
				0.5413,
				0.5987,
				0.656,
				0.7707,
				1.0
				]
    interf_ljets_ge4j_ge4t_Hbb_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hbb_tHW_node)
    


    # plots for ge4j_ge4t_Hincl

    interf_ljets_ge4j_ge4t_Hincl_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_ttH",
                                            label          = "ljets_ge4j_ge4t_Hincl_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==0))")
    interf_ljets_ge4j_ge4t_Hincl_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==0))","ljets_ge4j_ge4t_Hincl_ttH_node","")
    interf_ljets_ge4j_ge4t_Hincl_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_ttH_node.bin_edges = [ 
				0.186,
				0.232,
				0.278,
				0.324,
				0.37,
				0.416,
				0.462,
				0.508,
				0.554,
				0.6,
				0.646,
				0.83
				]
    interf_ljets_ge4j_ge4t_Hincl_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_ttH_node)
    
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_Hincl_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==1))")
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==1))","ljets_ge4j_ge4t_Hincl_ttmb_node","")
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node.bin_edges = [ 
				0.2107,
				0.246,
				0.2813,
				0.3167,
				0.352,
				0.3873,
				0.4227,
				0.458,
				0.4933,
				0.5287,
				0.67
				]
    interf_ljets_ge4j_ge4t_Hincl_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_ttmb_node)
    
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_Hincl_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==2))")
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==2))","ljets_ge4j_ge4t_Hincl_tt2b_node","")
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node.bin_edges = [ 
				0.2133,
				0.25,
				0.2867,
				0.3233,
				0.36,
				0.3967,
				0.47,
				0.69
				]
    interf_ljets_ge4j_ge4t_Hincl_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_tt2b_node)
    
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_Hincl_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==3))")
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==3))","ljets_ge4j_ge4t_Hincl_ttcc_node","")
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node.bin_edges = [ 
				0.204,
				0.236,
				0.268,
				0.3,
				0.332,
				0.364,
				0.396,
				0.428,
				0.46,
				0.62
				]
    interf_ljets_ge4j_ge4t_Hincl_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_ttcc_node)
    
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_Hincl_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==4))")
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==4))","ljets_ge4j_ge4t_Hincl_ttlf_node","")
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node.bin_edges = [ 
				0.1833,
				0.2267,
				0.27,
				0.3133,
				0.3567,
				0.4,
				0.4433,
				0.4867,
				0.53,
				0.5733,
				0.6167,
				0.66,
				0.79
				]
    interf_ljets_ge4j_ge4t_Hincl_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_ttlf_node)
    
    interf_ljets_ge4j_ge4t_Hincl_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_tHq",
                                            label          = "ljets_ge4j_ge4t_Hincl_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==5))")
    interf_ljets_ge4j_ge4t_Hincl_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==5))","ljets_ge4j_ge4t_Hincl_tHq_node","")
    interf_ljets_ge4j_ge4t_Hincl_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_tHq_node.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_Hincl_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_tHq_node)
    
    interf_ljets_ge4j_ge4t_Hincl_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_Hincl_node_tHW",
                                            label          = "ljets_ge4j_ge4t_Hincl_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==6))")
    interf_ljets_ge4j_ge4t_Hincl_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_Hincl==6))","ljets_ge4j_ge4t_Hincl_tHW_node","")
    interf_ljets_ge4j_ge4t_Hincl_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_Hincl_tHW_node.bin_edges = [ 
				0.1973,
				0.2547,
				0.312,
				0.3693,
				0.4267,
				0.484,
				0.5413,
				0.5987,
				0.656,
				0.7707,
				1.0
				]
    interf_ljets_ge4j_ge4t_Hincl_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_Hincl_tHW_node)
    


    # plots for ge4j_3t_Hbb

    interf_ljets_ge4j_3t_Hbb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_ttHbb",
                                            label          = "ljets_ge4j_3t_Hbb_ttHbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==0))")
    interf_ljets_ge4j_3t_Hbb_ttHbb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==0))","ljets_ge4j_3t_Hbb_ttHbb_node","")
    interf_ljets_ge4j_3t_Hbb_ttHbb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_ttHbb_node.bin_edges = [ 
				0.14,
				0.188,
				0.236,
				0.284,
				0.332,
				0.38,
				0.428,
				0.476,
				0.524,
				0.572,
				0.62,
				0.668,
				0.86
				]
    interf_ljets_ge4j_3t_Hbb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_ttHbb_node)
    
    interf_ljets_ge4j_3t_Hbb_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_ttmb",
                                            label          = "ljets_ge4j_3t_Hbb_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==1))")
    interf_ljets_ge4j_3t_Hbb_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==1))","ljets_ge4j_3t_Hbb_ttmb_node","")
    interf_ljets_ge4j_3t_Hbb_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_ttmb_node.bin_edges = [ 
				0.1653,
				0.1907,
				0.216,
				0.2413,
				0.2667,
				0.292,
				0.3173,
				0.3427,
				0.368,
				0.3933,
				0.4187,
				0.444,
				0.4693,
				0.52
				]
    interf_ljets_ge4j_3t_Hbb_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_ttmb_node)
    
    interf_ljets_ge4j_3t_Hbb_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_tt2b",
                                            label          = "ljets_ge4j_3t_Hbb_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==2))")
    interf_ljets_ge4j_3t_Hbb_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==2))","ljets_ge4j_3t_Hbb_tt2b_node","")
    interf_ljets_ge4j_3t_Hbb_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_tt2b_node.bin_edges = [ 
				0.14,
				0.184,
				0.228,
				0.272,
				0.316,
				0.36,
				0.404,
				0.448,
				0.492,
				0.536,
				0.58,
				0.624,
				0.668,
				0.8
				]
    interf_ljets_ge4j_3t_Hbb_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_tt2b_node)
    
    interf_ljets_ge4j_3t_Hbb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_ttcc",
                                            label          = "ljets_ge4j_3t_Hbb_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==3))")
    interf_ljets_ge4j_3t_Hbb_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==3))","ljets_ge4j_3t_Hbb_ttcc_node","")
    interf_ljets_ge4j_3t_Hbb_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_ttcc_node.bin_edges = [ 
				0.14,
				0.1867,
				0.2333,
				0.28,
				0.3267,
				0.3733,
				0.42,
				0.4667,
				0.5133,
				0.56,
				0.6067,
				0.6533,
				0.7,
				0.84
				]
    interf_ljets_ge4j_3t_Hbb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_ttcc_node)
    
    interf_ljets_ge4j_3t_Hbb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_ttlf",
                                            label          = "ljets_ge4j_3t_Hbb_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==4))")
    interf_ljets_ge4j_3t_Hbb_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==4))","ljets_ge4j_3t_Hbb_ttlf_node","")
    interf_ljets_ge4j_3t_Hbb_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_ttlf_node.bin_edges = [ 
				0.14,
				0.1867,
				0.2333,
				0.28,
				0.3267,
				0.3733,
				0.42,
				0.4667,
				0.5133,
				0.56,
				0.6067,
				0.6533,
				0.7,
				0.7467,
				0.84
				]
    interf_ljets_ge4j_3t_Hbb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_ttlf_node)
    
    interf_ljets_ge4j_3t_Hbb_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_tHq",
                                            label          = "ljets_ge4j_3t_Hbb_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==5))")
    interf_ljets_ge4j_3t_Hbb_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==5))","ljets_ge4j_3t_Hbb_tHq_node","")
    interf_ljets_ge4j_3t_Hbb_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_tHq_node.bin_edges = [ 
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
				0.9333,
				0.99
				]
    interf_ljets_ge4j_3t_Hbb_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_tHq_node)
    
    interf_ljets_ge4j_3t_Hbb_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hbb_node_tHW",
                                            label          = "ljets_ge4j_3t_Hbb_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==6))")
    interf_ljets_ge4j_3t_Hbb_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hbb==6))","ljets_ge4j_3t_Hbb_tHW_node","")
    interf_ljets_ge4j_3t_Hbb_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hbb_tHW_node.bin_edges = [ 
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
				1.0
				]
    interf_ljets_ge4j_3t_Hbb_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hbb_tHW_node)
    


    # plots for ge4j_3t_Hincl

    interf_ljets_ge4j_3t_Hincl_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_ttH",
                                            label          = "ljets_ge4j_3t_Hincl_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==0))")
    interf_ljets_ge4j_3t_Hincl_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==0))","ljets_ge4j_3t_Hincl_ttH_node","")
    interf_ljets_ge4j_3t_Hincl_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_ttH_node.bin_edges = [ 
				0.14,
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
    interf_ljets_ge4j_3t_Hincl_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_ttH_node)
    
    interf_ljets_ge4j_3t_Hincl_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_ttmb",
                                            label          = "ljets_ge4j_3t_Hincl_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==1))")
    interf_ljets_ge4j_3t_Hincl_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==1))","ljets_ge4j_3t_Hincl_ttmb_node","")
    interf_ljets_ge4j_3t_Hincl_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_ttmb_node.bin_edges = [ 
				0.168,
				0.196,
				0.224,
				0.252,
				0.28,
				0.308,
				0.336,
				0.364,
				0.392,
				0.42,
				0.448,
				0.476,
				0.56
				]
    interf_ljets_ge4j_3t_Hincl_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_ttmb_node)
    
    interf_ljets_ge4j_3t_Hincl_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_tt2b",
                                            label          = "ljets_ge4j_3t_Hincl_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==2))")
    interf_ljets_ge4j_3t_Hincl_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==2))","ljets_ge4j_3t_Hincl_tt2b_node","")
    interf_ljets_ge4j_3t_Hincl_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_tt2b_node.bin_edges = [ 
				0.14,
				0.184,
				0.228,
				0.272,
				0.316,
				0.36,
				0.404,
				0.448,
				0.492,
				0.536,
				0.58,
				0.624,
				0.668,
				0.8
				]
    interf_ljets_ge4j_3t_Hincl_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_tt2b_node)
    
    interf_ljets_ge4j_3t_Hincl_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_ttcc",
                                            label          = "ljets_ge4j_3t_Hincl_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==3))")
    interf_ljets_ge4j_3t_Hincl_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==3))","ljets_ge4j_3t_Hincl_ttcc_node","")
    interf_ljets_ge4j_3t_Hincl_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_ttcc_node.bin_edges = [ 
				0.14,
				0.1847,
				0.2293,
				0.274,
				0.3187,
				0.3633,
				0.408,
				0.4527,
				0.4973,
				0.542,
				0.5867,
				0.6313,
				0.676,
				0.7207,
				0.81
				]
    interf_ljets_ge4j_3t_Hincl_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_ttcc_node)
    
    interf_ljets_ge4j_3t_Hincl_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_ttlf",
                                            label          = "ljets_ge4j_3t_Hincl_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==4))")
    interf_ljets_ge4j_3t_Hincl_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==4))","ljets_ge4j_3t_Hincl_ttlf_node","")
    interf_ljets_ge4j_3t_Hincl_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_ttlf_node.bin_edges = [ 
				0.14,
				0.188,
				0.236,
				0.284,
				0.332,
				0.38,
				0.428,
				0.476,
				0.524,
				0.572,
				0.62,
				0.668,
				0.716,
				0.86
				]
    interf_ljets_ge4j_3t_Hincl_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_ttlf_node)
    
    interf_ljets_ge4j_3t_Hincl_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_tHq",
                                            label          = "ljets_ge4j_3t_Hincl_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==5))")
    interf_ljets_ge4j_3t_Hincl_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==5))","ljets_ge4j_3t_Hincl_tHq_node","")
    interf_ljets_ge4j_3t_Hincl_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_tHq_node.bin_edges = [ 
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
				0.9333,
				0.99
				]
    interf_ljets_ge4j_3t_Hincl_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_Hincl_tHq_node)
    
    interf_ljets_ge4j_3t_Hincl_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_Hincl_node_tHW",
                                            label          = "ljets_ge4j_3t_Hincl_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==6))")
    interf_ljets_ge4j_3t_Hincl_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_Hincl==6))","ljets_ge4j_3t_Hincl_tHW_node","")
    interf_ljets_ge4j_3t_Hincl_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_Hincl_tHW_node.bin_edges = [ 
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
				1.0
				]
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
    