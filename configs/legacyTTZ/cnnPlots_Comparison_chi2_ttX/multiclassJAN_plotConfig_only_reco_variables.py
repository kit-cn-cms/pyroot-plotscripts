
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


    # plots for ge6j_ge3t

    interf_ljets_ge6j_ge3t_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==0))")
    interf_ljets_ge6j_ge3t_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttHbb_node","")
    interf_ljets_ge6j_ge3t_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttHbb_node.bin_edges = [ 
				0.1122,
				0.1678,
				0.2233,
				0.2789,
				0.3344,
				0.39,
				0.4456,
				0.5011,
				0.5567,
				0.6122,
				0.64
				]
    interf_ljets_ge6j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttHnonbb",
                                            label          = "ljets_ge6j_ge3t_ttHnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))")
    interf_ljets_ge6j_ge3t_ttHnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttHnonbb_node","")
    interf_ljets_ge6j_ge3t_ttHnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttHnonbb_node.bin_edges = [ 
				0.1322,
				0.1478,
				0.1633,
				0.1789,
				0.1944,
				0.21,
				0.2256,
				0.2411,
				0.2567,
				0.2722,
				0.28
				]
    interf_ljets_ge6j_ge3t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttHnonbb_node)
    
    interf_ljets_ge6j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))")
    interf_ljets_ge6j_ge3t_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_ttZbb_node","")
    interf_ljets_ge6j_ge3t_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttZbb_node.bin_edges = [ 
				0.1067,
				0.1733,
				0.24,
				0.3067,
				0.3733,
				0.44,
				0.5067,
				0.5733,
				0.64,
				0.7067,
				0.74
				]
    interf_ljets_ge6j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttZnonbb",
                                            label          = "ljets_ge6j_ge3t_ttZnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))")
    interf_ljets_ge6j_ge3t_ttZnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttZnonbb_node","")
    interf_ljets_ge6j_ge3t_ttZnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttZnonbb_node.bin_edges = [ 
				0.1189,
				0.1611,
				0.2033,
				0.2456,
				0.2878,
				0.33,
				0.3722,
				0.4144,
				0.4567,
				0.4989,
				0.52
				]
    interf_ljets_ge6j_ge3t_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttZnonbb_node)
    
    interf_ljets_ge6j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))")
    interf_ljets_ge6j_ge3t_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttbb_node","")
    interf_ljets_ge6j_ge3t_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttbb_node.bin_edges = [ 
				0.1211,
				0.1589,
				0.1967,
				0.2344,
				0.2722,
				0.31,
				0.3478,
				0.3856,
				0.4233,
				0.4611,
				0.48
				]
    interf_ljets_ge6j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttbb_node)
    
    interf_ljets_ge6j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==5))")
    interf_ljets_ge6j_ge3t_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==5))","ljets_ge6j_ge3t_ttcc_node","")
    interf_ljets_ge6j_ge3t_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttcc_node.bin_edges = [ 
				0.125,
				0.155,
				0.185,
				0.215,
				0.245,
				0.275,
				0.305,
				0.335,
				0.365,
				0.395,
				0.41
				]
    interf_ljets_ge6j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttcc_node)
    
    interf_ljets_ge6j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==6))")
    interf_ljets_ge6j_ge3t_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==6))","ljets_ge6j_ge3t_ttlf_node","")
    interf_ljets_ge6j_ge3t_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttlf_node.bin_edges = [ 
				0.12,
				0.16,
				0.2,
				0.24,
				0.28,
				0.32,
				0.36,
				0.4,
				0.44,
				0.48,
				0.5
				]
    interf_ljets_ge6j_ge3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttlf_node)
    


    # plots for 4j_ge3t

    interf_ljets_4j_ge3t_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttHbb",
                                            label          = "ljets_4j_ge3t_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==0))")
    interf_ljets_4j_ge3t_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==0))","ljets_4j_ge3t_ttHbb_node","")
    interf_ljets_4j_ge3t_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttHbb_node.bin_edges = [ 
				0.1089,
				0.1711,
				0.2333,
				0.2956,
				0.3578,
				0.42,
				0.4822,
				0.5444,
				0.6067,
				0.6689,
				0.7
				]
    interf_ljets_4j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttHbb_node)
    
    interf_ljets_4j_ge3t_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttHnonbb",
                                            label          = "ljets_4j_ge3t_ttHnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))")
    interf_ljets_4j_ge3t_ttHnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttHnonbb_node","")
    interf_ljets_4j_ge3t_ttHnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttHnonbb_node.bin_edges = [ 
				0.1261,
				0.1539,
				0.1817,
				0.2094,
				0.2372,
				0.265,
				0.2928,
				0.3206,
				0.3483,
				0.3761,
				0.39
				]
    interf_ljets_4j_ge3t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttHnonbb_node)
    
    interf_ljets_4j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttZbb",
                                            label          = "ljets_4j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))")
    interf_ljets_4j_ge3t_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_ttZbb_node","")
    interf_ljets_4j_ge3t_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttZbb_node.bin_edges = [ 
				0.1061,
				0.1739,
				0.2417,
				0.3094,
				0.3772,
				0.445,
				0.5128,
				0.5806,
				0.6483,
				0.7161,
				0.75
				]
    interf_ljets_4j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttZbb_node)
    
    interf_ljets_4j_ge3t_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttZnonbb",
                                            label          = "ljets_4j_ge3t_ttZnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))")
    interf_ljets_4j_ge3t_ttZnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttZnonbb_node","")
    interf_ljets_4j_ge3t_ttZnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttZnonbb_node.bin_edges = [ 
				0.1117,
				0.1683,
				0.225,
				0.2817,
				0.3383,
				0.395,
				0.4517,
				0.5083,
				0.565,
				0.6217,
				0.65
				]
    interf_ljets_4j_ge3t_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttZnonbb_node)
    
    interf_ljets_4j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttbb",
                                            label          = "ljets_4j_ge3t_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))")
    interf_ljets_4j_ge3t_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttbb_node","")
    interf_ljets_4j_ge3t_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttbb_node.bin_edges = [ 
				0.1122,
				0.1678,
				0.2233,
				0.2789,
				0.3344,
				0.39,
				0.4456,
				0.5011,
				0.5567,
				0.6122,
				0.64
				]
    interf_ljets_4j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttbb_node)
    
    interf_ljets_4j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttcc",
                                            label          = "ljets_4j_ge3t_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==5))")
    interf_ljets_4j_ge3t_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==5))","ljets_4j_ge3t_ttcc_node","")
    interf_ljets_4j_ge3t_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttcc_node.bin_edges = [ 
				0.125,
				0.155,
				0.185,
				0.215,
				0.245,
				0.275,
				0.305,
				0.335,
				0.365,
				0.395,
				0.41
				]
    interf_ljets_4j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttcc_node)
    
    interf_ljets_4j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttlf",
                                            label          = "ljets_4j_ge3t_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==6))")
    interf_ljets_4j_ge3t_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==6))","ljets_4j_ge3t_ttlf_node","")
    interf_ljets_4j_ge3t_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttlf_node.bin_edges = [ 
				0.1167,
				0.1633,
				0.21,
				0.2567,
				0.3033,
				0.35,
				0.3967,
				0.4433,
				0.49,
				0.5367,
				0.56
				]
    interf_ljets_4j_ge3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttlf_node)
    


    # plots for 5j_ge3t

    interf_ljets_5j_ge3t_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttHbb",
                                            label          = "ljets_5j_ge3t_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==0))")
    interf_ljets_5j_ge3t_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==0))","ljets_5j_ge3t_ttHbb_node","")
    interf_ljets_5j_ge3t_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttHbb_node.bin_edges = [ 
				0.1083,
				0.1717,
				0.235,
				0.2983,
				0.3617,
				0.425,
				0.4883,
				0.5517,
				0.615,
				0.6783,
				0.71
				]
    interf_ljets_5j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttHbb_node)
    
    interf_ljets_5j_ge3t_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttHnonbb",
                                            label          = "ljets_5j_ge3t_ttHnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))")
    interf_ljets_5j_ge3t_ttHnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttHnonbb_node","")
    interf_ljets_5j_ge3t_ttHnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttHnonbb_node.bin_edges = [ 
				0.1278,
				0.1522,
				0.1767,
				0.2011,
				0.2256,
				0.25,
				0.2744,
				0.2989,
				0.3233,
				0.3478,
				0.36
				]
    interf_ljets_5j_ge3t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttHnonbb_node)
    
    interf_ljets_5j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttZbb",
                                            label          = "ljets_5j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))")
    interf_ljets_5j_ge3t_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_ttZbb_node","")
    interf_ljets_5j_ge3t_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttZbb_node.bin_edges = [ 
				0.1044,
				0.1756,
				0.2467,
				0.3178,
				0.3889,
				0.46,
				0.5311,
				0.6022,
				0.6733,
				0.7444,
				0.78
				]
    interf_ljets_5j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttZbb_node)
    
    interf_ljets_5j_ge3t_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttZnonbb",
                                            label          = "ljets_5j_ge3t_ttZnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))")
    interf_ljets_5j_ge3t_ttZnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttZnonbb_node","")
    interf_ljets_5j_ge3t_ttZnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttZnonbb_node.bin_edges = [ 
				0.0989,
				0.1811,
				0.2633,
				0.3456,
				0.4278,
				0.51,
				0.5922,
				0.6744,
				0.7567,
				0.8389,
				0.88
				]
    interf_ljets_5j_ge3t_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttZnonbb_node)
    
    interf_ljets_5j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttbb",
                                            label          = "ljets_5j_ge3t_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))")
    interf_ljets_5j_ge3t_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttbb_node","")
    interf_ljets_5j_ge3t_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttbb_node.bin_edges = [ 
				0.1183,
				0.1617,
				0.205,
				0.2483,
				0.2917,
				0.335,
				0.3783,
				0.4217,
				0.465,
				0.5083,
				0.53
				]
    interf_ljets_5j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttbb_node)
    
    interf_ljets_5j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttcc",
                                            label          = "ljets_5j_ge3t_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==5))")
    interf_ljets_5j_ge3t_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==5))","ljets_5j_ge3t_ttcc_node","")
    interf_ljets_5j_ge3t_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttcc_node.bin_edges = [ 
				0.1228,
				0.1572,
				0.1917,
				0.2261,
				0.2606,
				0.295,
				0.3294,
				0.3639,
				0.3983,
				0.4328,
				0.45
				]
    interf_ljets_5j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttcc_node)
    
    interf_ljets_5j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttlf",
                                            label          = "ljets_5j_ge3t_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==6))")
    interf_ljets_5j_ge3t_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==6))","ljets_5j_ge3t_ttlf_node","")
    interf_ljets_5j_ge3t_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttlf_node.bin_edges = [ 
				0.1222,
				0.1578,
				0.1933,
				0.2289,
				0.2644,
				0.3,
				0.3356,
				0.3711,
				0.4067,
				0.4422,
				0.46
				]
    interf_ljets_5j_ge3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttlf_node)
    

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
    