
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
				0.1094,
				0.1706,
				0.2317,
				0.2928,
				0.3539,
				0.415,
				0.4761,
				0.5372,
				0.5983,
				0.6594,
				0.69
				]
    interf_ljets_ge6j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttHnonbb",
                                            label          = "ljets_ge6j_ge3t_ttHnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))")
    interf_ljets_ge6j_ge3t_ttHnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttHnonbb_node","")
    interf_ljets_ge6j_ge3t_ttHnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttHnonbb_node.bin_edges = [ 
				0.1289,
				0.1511,
				0.1733,
				0.1956,
				0.2178,
				0.24,
				0.2622,
				0.2844,
				0.3067,
				0.3289,
				0.34
				]
    interf_ljets_ge6j_ge3t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttHnonbb_node)
    
    interf_ljets_ge6j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))")
    interf_ljets_ge6j_ge3t_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_ttZbb_node","")
    interf_ljets_ge6j_ge3t_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttZbb_node.bin_edges = [ 
				0.1056,
				0.1744,
				0.2433,
				0.3122,
				0.3811,
				0.45,
				0.5189,
				0.5878,
				0.6567,
				0.7256,
				0.76
				]
    interf_ljets_ge6j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttZnonbb",
                                            label          = "ljets_ge6j_ge3t_ttZnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))")
    interf_ljets_ge6j_ge3t_ttZnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttZnonbb_node","")
    interf_ljets_ge6j_ge3t_ttZnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttZnonbb_node.bin_edges = [ 
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
    interf_ljets_ge6j_ge3t_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttZnonbb_node)
    
    interf_ljets_ge6j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))")
    interf_ljets_ge6j_ge3t_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttbb_node","")
    interf_ljets_ge6j_ge3t_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttbb_node.bin_edges = [ 
				0.1206,
				0.1594,
				0.1983,
				0.2372,
				0.2761,
				0.315,
				0.3539,
				0.3928,
				0.4317,
				0.4706,
				0.49
				]
    interf_ljets_ge6j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttbb_node)
    
    interf_ljets_ge6j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==5))")
    interf_ljets_ge6j_ge3t_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==5))","ljets_ge6j_ge3t_ttcc_node","")
    interf_ljets_ge6j_ge3t_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttcc_node.bin_edges = [ 
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
    interf_ljets_ge6j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttcc_node)
    
    interf_ljets_ge6j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==6))")
    interf_ljets_ge6j_ge3t_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==6))","ljets_ge6j_ge3t_ttlf_node","")
    interf_ljets_ge6j_ge3t_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttlf_node.bin_edges = [ 
				0.1139,
				0.1661,
				0.2183,
				0.2706,
				0.3228,
				0.375,
				0.4272,
				0.4794,
				0.5317,
				0.5839,
				0.61
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
				0.1028,
				0.1772,
				0.2517,
				0.3261,
				0.4006,
				0.475,
				0.5494,
				0.6239,
				0.6983,
				0.7728,
				0.81
				]
    interf_ljets_4j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttHbb_node)
    
    interf_ljets_4j_ge3t_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttHnonbb",
                                            label          = "ljets_4j_ge3t_ttHnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))")
    interf_ljets_4j_ge3t_ttHnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttHnonbb_node","")
    interf_ljets_4j_ge3t_ttHnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttHnonbb_node.bin_edges = [ 
				0.1256,
				0.1544,
				0.1833,
				0.2122,
				0.2411,
				0.27,
				0.2989,
				0.3278,
				0.3567,
				0.3856,
				0.4
				]
    interf_ljets_4j_ge3t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttHnonbb_node)
    
    interf_ljets_4j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttZbb",
                                            label          = "ljets_4j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))")
    interf_ljets_4j_ge3t_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_ttZbb_node","")
    interf_ljets_4j_ge3t_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttZbb_node.bin_edges = [ 
				0.1028,
				0.1772,
				0.2517,
				0.3261,
				0.4006,
				0.475,
				0.5494,
				0.6239,
				0.6983,
				0.7728,
				0.81
				]
    interf_ljets_4j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttZbb_node)
    
    interf_ljets_4j_ge3t_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttZnonbb",
                                            label          = "ljets_4j_ge3t_ttZnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))")
    interf_ljets_4j_ge3t_ttZnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttZnonbb_node","")
    interf_ljets_4j_ge3t_ttZnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttZnonbb_node.bin_edges = [ 
				0.0961,
				0.1839,
				0.2717,
				0.3594,
				0.4472,
				0.535,
				0.6228,
				0.7106,
				0.7983,
				0.8861,
				0.93
				]
    interf_ljets_4j_ge3t_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttZnonbb_node)
    
    interf_ljets_4j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttbb",
                                            label          = "ljets_4j_ge3t_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))")
    interf_ljets_4j_ge3t_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttbb_node","")
    interf_ljets_4j_ge3t_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttbb_node.bin_edges = [ 
				0.1106,
				0.1694,
				0.2283,
				0.2872,
				0.3461,
				0.405,
				0.4639,
				0.5228,
				0.5817,
				0.6406,
				0.67
				]
    interf_ljets_4j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttbb_node)
    
    interf_ljets_4j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttcc",
                                            label          = "ljets_4j_ge3t_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==5))")
    interf_ljets_4j_ge3t_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==5))","ljets_4j_ge3t_ttcc_node","")
    interf_ljets_4j_ge3t_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttcc_node.bin_edges = [ 
				0.1239,
				0.1561,
				0.1883,
				0.2206,
				0.2528,
				0.285,
				0.3172,
				0.3494,
				0.3817,
				0.4139,
				0.43
				]
    interf_ljets_4j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttcc_node)
    
    interf_ljets_4j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttlf",
                                            label          = "ljets_4j_ge3t_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==6))")
    interf_ljets_4j_ge3t_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==6))","ljets_4j_ge3t_ttlf_node","")
    interf_ljets_4j_ge3t_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttlf_node.bin_edges = [ 
				0.1144,
				0.1656,
				0.2167,
				0.2678,
				0.3189,
				0.37,
				0.4211,
				0.4722,
				0.5233,
				0.5744,
				0.6
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
				0.105,
				0.175,
				0.245,
				0.315,
				0.385,
				0.455,
				0.525,
				0.595,
				0.665,
				0.735,
				0.77
				]
    interf_ljets_5j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttHbb_node)
    
    interf_ljets_5j_ge3t_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttHnonbb",
                                            label          = "ljets_5j_ge3t_ttHnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))")
    interf_ljets_5j_ge3t_ttHnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttHnonbb_node","")
    interf_ljets_5j_ge3t_ttHnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttHnonbb_node.bin_edges = [ 
				0.1283,
				0.1517,
				0.175,
				0.1983,
				0.2217,
				0.245,
				0.2683,
				0.2917,
				0.315,
				0.3383,
				0.35
				]
    interf_ljets_5j_ge3t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttHnonbb_node)
    
    interf_ljets_5j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttZbb",
                                            label          = "ljets_5j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))")
    interf_ljets_5j_ge3t_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_ttZbb_node","")
    interf_ljets_5j_ge3t_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttZbb_node.bin_edges = [ 
				0.1056,
				0.1744,
				0.2433,
				0.3122,
				0.3811,
				0.45,
				0.5189,
				0.5878,
				0.6567,
				0.7256,
				0.76
				]
    interf_ljets_5j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttZbb_node)
    
    interf_ljets_5j_ge3t_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttZnonbb",
                                            label          = "ljets_5j_ge3t_ttZnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))")
    interf_ljets_5j_ge3t_ttZnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttZnonbb_node","")
    interf_ljets_5j_ge3t_ttZnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttZnonbb_node.bin_edges = [ 
				0.0967,
				0.1833,
				0.27,
				0.3567,
				0.4433,
				0.53,
				0.6167,
				0.7033,
				0.79,
				0.8767,
				0.92
				]
    interf_ljets_5j_ge3t_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttZnonbb_node)
    
    interf_ljets_5j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttbb",
                                            label          = "ljets_5j_ge3t_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))")
    interf_ljets_5j_ge3t_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttbb_node","")
    interf_ljets_5j_ge3t_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttbb_node.bin_edges = [ 
				0.1139,
				0.1661,
				0.2183,
				0.2706,
				0.3228,
				0.375,
				0.4272,
				0.4794,
				0.5317,
				0.5839,
				0.61
				]
    interf_ljets_5j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttbb_node)
    
    interf_ljets_5j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttcc",
                                            label          = "ljets_5j_ge3t_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==5))")
    interf_ljets_5j_ge3t_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==5))","ljets_5j_ge3t_ttcc_node","")
    interf_ljets_5j_ge3t_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttcc_node.bin_edges = [ 
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
    interf_ljets_5j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttcc_node)
    
    interf_ljets_5j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttlf",
                                            label          = "ljets_5j_ge3t_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==6))")
    interf_ljets_5j_ge3t_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==6))","ljets_5j_ge3t_ttlf_node","")
    interf_ljets_5j_ge3t_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttlf_node.bin_edges = [ 
				0.1144,
				0.1656,
				0.2167,
				0.2678,
				0.3189,
				0.37,
				0.4211,
				0.4722,
				0.5233,
				0.5744,
				0.6
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
    