
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
				0.1267,
				0.1533,
				0.18,
				0.2067,
				0.2333,
				0.26,
				0.2867,
				0.3133,
				0.34,
				0.3667,
				0.38
				]
    interf_ljets_ge6j_ge3t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttHnonbb_node)
    
    interf_ljets_ge6j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))")
    interf_ljets_ge6j_ge3t_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_ttZbb_node","")
    interf_ljets_ge6j_ge3t_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttZbb_node.bin_edges = [ 
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
    interf_ljets_ge6j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttZnonbb",
                                            label          = "ljets_ge6j_ge3t_ttZnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))")
    interf_ljets_ge6j_ge3t_ttZnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttZnonbb_node","")
    interf_ljets_ge6j_ge3t_ttZnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttZnonbb_node.bin_edges = [ 
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
    interf_ljets_ge6j_ge3t_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttZnonbb_node)
    
    interf_ljets_ge6j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))")
    interf_ljets_ge6j_ge3t_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttbb_node","")
    interf_ljets_ge6j_ge3t_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttbb_node.bin_edges = [ 
				0.1128,
				0.1672,
				0.2217,
				0.2761,
				0.3306,
				0.385,
				0.4394,
				0.4939,
				0.5483,
				0.6028,
				0.63
				]
    interf_ljets_ge6j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttbb_node)
    
    interf_ljets_ge6j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==5))")
    interf_ljets_ge6j_ge3t_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==5))","ljets_ge6j_ge3t_ttcc_node","")
    interf_ljets_ge6j_ge3t_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttcc_node.bin_edges = [ 
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
    interf_ljets_ge6j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttcc_node)
    
    interf_ljets_ge6j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==6))")
    interf_ljets_ge6j_ge3t_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==6))","ljets_ge6j_ge3t_ttlf_node","")
    interf_ljets_ge6j_ge3t_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttlf_node.bin_edges = [ 
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
    interf_ljets_ge6j_ge3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttlf_node)
    


    # plots for 4j_ge3t

    interf_ljets_4j_ge3t_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttHbb",
                                            label          = "ljets_4j_ge3t_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==0))")
    interf_ljets_4j_ge3t_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==0))","ljets_4j_ge3t_ttHbb_node","")
    interf_ljets_4j_ge3t_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttHbb_node.bin_edges = [ 
				0.1133,
				0.1667,
				0.22,
				0.2733,
				0.3267,
				0.38,
				0.4333,
				0.4867,
				0.54,
				0.5933,
				0.62
				]
    interf_ljets_4j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttHbb_node)
    
    interf_ljets_4j_ge3t_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttHnonbb",
                                            label          = "ljets_4j_ge3t_ttHnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))")
    interf_ljets_4j_ge3t_ttHnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttHnonbb_node","")
    interf_ljets_4j_ge3t_ttHnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttHnonbb_node.bin_edges = [ 
				0.1233,
				0.1567,
				0.19,
				0.2233,
				0.2567,
				0.29,
				0.3233,
				0.3567,
				0.39,
				0.4233,
				0.44
				]
    interf_ljets_4j_ge3t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttHnonbb_node)
    
    interf_ljets_4j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttZbb",
                                            label          = "ljets_4j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))")
    interf_ljets_4j_ge3t_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_ttZbb_node","")
    interf_ljets_4j_ge3t_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttZbb_node.bin_edges = [ 
				0.1017,
				0.1783,
				0.255,
				0.3317,
				0.4083,
				0.485,
				0.5617,
				0.6383,
				0.715,
				0.7917,
				0.83
				]
    interf_ljets_4j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttZbb_node)
    
    interf_ljets_4j_ge3t_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttZnonbb",
                                            label          = "ljets_4j_ge3t_ttZnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))")
    interf_ljets_4j_ge3t_ttZnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttZnonbb_node","")
    interf_ljets_4j_ge3t_ttZnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttZnonbb_node.bin_edges = [ 
				0.0928,
				0.1872,
				0.2817,
				0.3761,
				0.4706,
				0.565,
				0.6594,
				0.7539,
				0.8483,
				0.9428,
				0.99
				]
    interf_ljets_4j_ge3t_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttZnonbb_node)
    
    interf_ljets_4j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttbb",
                                            label          = "ljets_4j_ge3t_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))")
    interf_ljets_4j_ge3t_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttbb_node","")
    interf_ljets_4j_ge3t_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttbb_node.bin_edges = [ 
				0.1156,
				0.1644,
				0.2133,
				0.2622,
				0.3111,
				0.36,
				0.4089,
				0.4578,
				0.5067,
				0.5556,
				0.58
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
    interf_ljets_4j_ge3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttlf_node)
    


    # plots for 5j_ge3t

    interf_ljets_5j_ge3t_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttHbb",
                                            label          = "ljets_5j_ge3t_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==0))")
    interf_ljets_5j_ge3t_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==0))","ljets_5j_ge3t_ttHbb_node","")
    interf_ljets_5j_ge3t_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttHbb_node.bin_edges = [ 
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
    interf_ljets_5j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttHbb_node)
    
    interf_ljets_5j_ge3t_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttHnonbb",
                                            label          = "ljets_5j_ge3t_ttHnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))")
    interf_ljets_5j_ge3t_ttHnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttHnonbb_node","")
    interf_ljets_5j_ge3t_ttHnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttHnonbb_node.bin_edges = [ 
				0.1272,
				0.1528,
				0.1783,
				0.2039,
				0.2294,
				0.255,
				0.2806,
				0.3061,
				0.3317,
				0.3572,
				0.37
				]
    interf_ljets_5j_ge3t_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttHnonbb_node)
    
    interf_ljets_5j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttZbb",
                                            label          = "ljets_5j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))")
    interf_ljets_5j_ge3t_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_ttZbb_node","")
    interf_ljets_5j_ge3t_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttZbb_node.bin_edges = [ 
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
    interf_ljets_5j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttZbb_node)
    
    interf_ljets_5j_ge3t_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttZnonbb",
                                            label          = "ljets_5j_ge3t_ttZnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))")
    interf_ljets_5j_ge3t_ttZnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttZnonbb_node","")
    interf_ljets_5j_ge3t_ttZnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttZnonbb_node.bin_edges = [ 
				0.095,
				0.185,
				0.275,
				0.365,
				0.455,
				0.545,
				0.635,
				0.725,
				0.815,
				0.905,
				0.95
				]
    interf_ljets_5j_ge3t_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttZnonbb_node)
    
    interf_ljets_5j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttbb",
                                            label          = "ljets_5j_ge3t_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))")
    interf_ljets_5j_ge3t_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttbb_node","")
    interf_ljets_5j_ge3t_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttbb_node.bin_edges = [ 
				0.1156,
				0.1644,
				0.2133,
				0.2622,
				0.3111,
				0.36,
				0.4089,
				0.4578,
				0.5067,
				0.5556,
				0.58
				]
    interf_ljets_5j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttbb_node)
    
    interf_ljets_5j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttcc",
                                            label          = "ljets_5j_ge3t_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==5))")
    interf_ljets_5j_ge3t_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==5))","ljets_5j_ge3t_ttcc_node","")
    interf_ljets_5j_ge3t_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttcc_node.bin_edges = [ 
				0.1244,
				0.1556,
				0.1867,
				0.2178,
				0.2489,
				0.28,
				0.3111,
				0.3422,
				0.3733,
				0.4044,
				0.42
				]
    interf_ljets_5j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttcc_node)
    
    interf_ljets_5j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttlf",
                                            label          = "ljets_5j_ge3t_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==6))")
    interf_ljets_5j_ge3t_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==6))","ljets_5j_ge3t_ttlf_node","")
    interf_ljets_5j_ge3t_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttlf_node.bin_edges = [ 
				0.1172,
				0.1628,
				0.2083,
				0.2539,
				0.2994,
				0.345,
				0.3906,
				0.4361,
				0.4817,
				0.5272,
				0.55
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
    