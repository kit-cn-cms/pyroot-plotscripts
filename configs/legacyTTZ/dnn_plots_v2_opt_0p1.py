
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


    # plots for ge6j_ge3t_Xnonbb_merged

    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_merged_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==0))")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==0))","ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node.bin_edges = [ 
				0.2,
				0.262,
				0.324,
				0.386,
				0.448,
				0.51,
				0.572,
				0.634,
				0.82
				]
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_merged_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==1))")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==1))","ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node.bin_edges = [ 
				0.2,
				0.27,
				0.34,
				0.41,
				0.48,
				0.55,
				0.62,
				0.69,
				0.9
				]
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_merged_node_ttXnonbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==2))")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==2))","ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node.bin_edges = [ 
				0.2,
				0.261,
				0.322,
				0.383,
				0.444,
				0.505,
				0.566,
				0.81
				]
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_merged_node_ttnonbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==3))")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==3))","ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node.bin_edges = [ 
				0.2,
				0.265,
				0.33,
				0.395,
				0.46,
				0.525,
				0.59,
				0.655,
				0.72,
				0.785,
				0.85
				]
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_merged_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==4))")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==4))","ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node.bin_edges = [ 
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
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node)
    


    # plots for ge6j_ge3t_Xnonbb_ttbar

    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_ttbar_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==0))")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==0))","ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node.bin_edges = [ 
				0.25,
				0.31,
				0.37,
				0.43,
				0.49,
				0.55,
				0.61,
				0.67,
				0.85
				]
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_ttbar_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==1))")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==1))","ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node.bin_edges = [ 
				0.25,
				0.317,
				0.384,
				0.451,
				0.518,
				0.585,
				0.652,
				0.719,
				0.92
				]
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_ttbar_node_ttXnonbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==2))")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==2))","ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node.bin_edges = [ 
				0.25,
				0.321,
				0.392,
				0.463,
				0.534,
				0.605,
				0.676,
				0.96
				]
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_ttbar_node_ttbar",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==3))")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==3))","ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node.bin_edges = [ 
				0.25,
				0.316,
				0.382,
				0.448,
				0.514,
				0.58,
				0.646,
				0.712,
				0.778,
				0.844,
				0.91
				]
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node)
    


    # plots for ge6j_ge3t_bb

    interf_ljets_ge6j_ge3t_bb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_bb_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==0))")
    interf_ljets_ge6j_ge3t_bb_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==0))","ljets_ge6j_ge3t_bb_ttHbb_node","")
    interf_ljets_ge6j_ge3t_bb_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttHbb_node.bin_edges = [ 
				0.2,
				0.264,
				0.328,
				0.392,
				0.456,
				0.52,
				0.584,
				0.648,
				0.84
				]
    interf_ljets_ge6j_ge3t_bb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_bb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_bb_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==1))")
    interf_ljets_ge6j_ge3t_bb_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==1))","ljets_ge6j_ge3t_bb_ttZbb_node","")
    interf_ljets_ge6j_ge3t_bb_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttZbb_node.bin_edges = [ 
				0.2,
				0.272,
				0.344,
				0.416,
				0.488,
				0.56,
				0.632,
				0.704,
				0.92
				]
    interf_ljets_ge6j_ge3t_bb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_bb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_bb_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==2))")
    interf_ljets_ge6j_ge3t_bb_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==2))","ljets_ge6j_ge3t_bb_ttbb_node","")
    interf_ljets_ge6j_ge3t_bb_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttbb_node.bin_edges = [ 
				0.2,
				0.277,
				0.354,
				0.431,
				0.508,
				0.585,
				0.662,
				0.739,
				0.816,
				0.97
				]
    interf_ljets_ge6j_ge3t_bb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttbb_node)
    
    interf_ljets_ge6j_ge3t_bb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_bb_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==3))")
    interf_ljets_ge6j_ge3t_bb_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==3))","ljets_ge6j_ge3t_bb_ttcc_node","")
    interf_ljets_ge6j_ge3t_bb_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttcc_node.bin_edges = [ 
				0.2,
				0.249,
				0.298,
				0.347,
				0.396,
				0.445,
				0.494,
				0.543,
				0.592,
				0.69
				]
    interf_ljets_ge6j_ge3t_bb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttcc_node)
    
    interf_ljets_ge6j_ge3t_bb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_bb_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==4))")
    interf_ljets_ge6j_ge3t_bb_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==4))","ljets_ge6j_ge3t_bb_ttlf_node","")
    interf_ljets_ge6j_ge3t_bb_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttlf_node.bin_edges = [ 
				0.2,
				0.258,
				0.316,
				0.374,
				0.432,
				0.49,
				0.548,
				0.606,
				0.664,
				0.722,
				0.78
				]
    interf_ljets_ge6j_ge3t_bb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttlf_node)
    


    # plots for ge6j_ge3t_bb_merged

    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_merged_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_bb_merged_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==0))")
    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==0))","ljets_ge6j_ge3t_bb_merged_ttHbb_node","")
    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node.bin_edges = [ 
				0.25,
				0.31,
				0.37,
				0.43,
				0.49,
				0.55,
				0.61,
				0.67,
				0.85
				]
    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_merged_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_bb_merged_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==1))")
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==1))","ljets_ge6j_ge3t_bb_merged_ttZbb_node","")
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node.bin_edges = [ 
				0.25,
				0.316,
				0.382,
				0.448,
				0.514,
				0.58,
				0.646,
				0.712,
				0.91
				]
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_merged_node_ttnonbb",
                                            label          = "ljets_ge6j_ge3t_bb_merged_ttnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==2))")
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==2))","ljets_ge6j_ge3t_bb_merged_ttnonbb_node","")
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node.bin_edges = [ 
				0.25,
				0.317,
				0.384,
				0.451,
				0.518,
				0.585,
				0.652,
				0.719,
				0.786,
				0.853,
				0.92
				]
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node)
    
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_merged_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_bb_merged_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==3))")
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==3))","ljets_ge6j_ge3t_bb_merged_ttbb_node","")
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node.bin_edges = [ 
				0.25,
				0.32,
				0.39,
				0.46,
				0.53,
				0.6,
				0.67,
				0.74,
				0.81,
				0.88,
				0.95
				]
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_merged_ttbb_node)
    


    # plots for ge6j_ge3t_bb_ttbar

    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_ttbar_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_bb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==0))")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==0))","ljets_ge6j_ge3t_bb_ttbar_ttHbb_node","")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node.bin_edges = [ 
				0.33,
				0.39,
				0.45,
				0.51,
				0.57,
				0.63,
				0.69,
				0.75,
				0.93
				]
    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_ttbar_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_bb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==1))")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==1))","ljets_ge6j_ge3t_bb_ttbar_ttZbb_node","")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node.bin_edges = [ 
				0.33,
				0.393,
				0.456,
				0.519,
				0.582,
				0.645,
				0.708,
				0.771,
				0.834,
				0.96
				]
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_ttbar_node_ttbar",
                                            label          = "ljets_ge6j_ge3t_bb_ttbar_ttbar_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==2))")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==2))","ljets_ge6j_ge3t_bb_ttbar_ttbar_node","")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node.bin_edges = [ 
				0.33,
				0.396,
				0.462,
				0.528,
				0.594,
				0.66,
				0.726,
				0.792,
				0.858,
				0.924,
				0.99
				]
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node)
    


    # plots for ge6j_ge3t_comb

    interf_ljets_ge6j_ge3t_comb_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_comb_node_ttH",
                                            label          = "ljets_ge6j_ge3t_comb_ttH_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==0))")
    interf_ljets_ge6j_ge3t_comb_ttH_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==0))","ljets_ge6j_ge3t_comb_ttH_node","")
    interf_ljets_ge6j_ge3t_comb_ttH_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_comb_ttH_node.bin_edges = [ 
				0.2,
				0.258,
				0.316,
				0.374,
				0.432,
				0.49,
				0.548,
				0.606,
				0.78
				]
    interf_ljets_ge6j_ge3t_comb_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_comb_ttH_node)
    
    interf_ljets_ge6j_ge3t_comb_ttZ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_comb_node_ttZ",
                                            label          = "ljets_ge6j_ge3t_comb_ttZ_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==1))")
    interf_ljets_ge6j_ge3t_comb_ttZ_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==1))","ljets_ge6j_ge3t_comb_ttZ_node","")
    interf_ljets_ge6j_ge3t_comb_ttZ_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_comb_ttZ_node.bin_edges = [ 
				0.2,
				0.261,
				0.322,
				0.383,
				0.444,
				0.505,
				0.81
				]
    interf_ljets_ge6j_ge3t_comb_ttZ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_comb_ttZ_node)
    
    interf_ljets_ge6j_ge3t_comb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_comb_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_comb_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==2))")
    interf_ljets_ge6j_ge3t_comb_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==2))","ljets_ge6j_ge3t_comb_ttbb_node","")
    interf_ljets_ge6j_ge3t_comb_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_comb_ttbb_node.bin_edges = [ 
				0.2,
				0.268,
				0.336,
				0.404,
				0.472,
				0.54,
				0.608,
				0.676,
				0.744,
				0.88
				]
    interf_ljets_ge6j_ge3t_comb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_comb_ttbb_node)
    
    interf_ljets_ge6j_ge3t_comb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_comb_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_comb_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==3))")
    interf_ljets_ge6j_ge3t_comb_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==3))","ljets_ge6j_ge3t_comb_ttcc_node","")
    interf_ljets_ge6j_ge3t_comb_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_comb_ttcc_node.bin_edges = [ 
				0.2,
				0.237,
				0.274,
				0.311,
				0.348,
				0.385,
				0.422,
				0.459,
				0.496,
				0.57
				]
    interf_ljets_ge6j_ge3t_comb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_comb_ttcc_node)
    
    interf_ljets_ge6j_ge3t_comb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_comb_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_comb_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==4))")
    interf_ljets_ge6j_ge3t_comb_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==4))","ljets_ge6j_ge3t_comb_ttlf_node","")
    interf_ljets_ge6j_ge3t_comb_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_comb_ttlf_node.bin_edges = [ 
				0.2,
				0.253,
				0.306,
				0.359,
				0.412,
				0.465,
				0.518,
				0.571,
				0.624,
				0.73
				]
    interf_ljets_ge6j_ge3t_comb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_comb_ttlf_node)
    


    # plots for ge6j_ge3t_split

    interf_ljets_ge6j_ge3t_split_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_split_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==0))")
    interf_ljets_ge6j_ge3t_split_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==0))","ljets_ge6j_ge3t_split_ttHbb_node","")
    interf_ljets_ge6j_ge3t_split_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttHbb_node.bin_edges = [ 
				0.14,
				0.2,
				0.26,
				0.32,
				0.38,
				0.44,
				0.5,
				0.56,
				0.74
				]
    interf_ljets_ge6j_ge3t_split_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttHnonbb",
                                            label          = "ljets_ge6j_ge3t_split_ttHnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==1))")
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==1))","ljets_ge6j_ge3t_split_ttHnonbb_node","")
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node.bin_edges = [ 
				0.166,
				0.192,
				0.218,
				0.244,
				0.27,
				0.296,
				0.4
				]
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttHnonbb_node)
    
    interf_ljets_ge6j_ge3t_split_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_split_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==2))")
    interf_ljets_ge6j_ge3t_split_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==2))","ljets_ge6j_ge3t_split_ttZbb_node","")
    interf_ljets_ge6j_ge3t_split_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttZbb_node.bin_edges = [ 
				0.14,
				0.212,
				0.284,
				0.356,
				0.428,
				0.5,
				0.572,
				0.644,
				0.86
				]
    interf_ljets_ge6j_ge3t_split_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttZnonbb",
                                            label          = "ljets_ge6j_ge3t_split_ttZnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==3))")
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==3))","ljets_ge6j_ge3t_split_ttZnonbb_node","")
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node.bin_edges = [ 
				0.14,
				0.196,
				0.252,
				0.308,
				0.364,
				0.42,
				0.7
				]
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttZnonbb_node)
    
    interf_ljets_ge6j_ge3t_split_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_split_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==4))")
    interf_ljets_ge6j_ge3t_split_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==4))","ljets_ge6j_ge3t_split_ttbb_node","")
    interf_ljets_ge6j_ge3t_split_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttbb_node.bin_edges = [ 
				0.14,
				0.207,
				0.274,
				0.341,
				0.408,
				0.475,
				0.542,
				0.609,
				0.81
				]
    interf_ljets_ge6j_ge3t_split_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttbb_node)
    
    interf_ljets_ge6j_ge3t_split_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_split_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==5))")
    interf_ljets_ge6j_ge3t_split_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==5))","ljets_ge6j_ge3t_split_ttcc_node","")
    interf_ljets_ge6j_ge3t_split_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttcc_node.bin_edges = [ 
				0.178,
				0.216,
				0.254,
				0.292,
				0.33,
				0.368,
				0.406,
				0.52
				]
    interf_ljets_ge6j_ge3t_split_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttcc_node)
    
    interf_ljets_ge6j_ge3t_split_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_split_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==6))")
    interf_ljets_ge6j_ge3t_split_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==6))","ljets_ge6j_ge3t_split_ttlf_node","")
    interf_ljets_ge6j_ge3t_split_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttlf_node.bin_edges = [ 
				0.14,
				0.201,
				0.262,
				0.323,
				0.384,
				0.445,
				0.506,
				0.567,
				0.628,
				0.75
				]
    interf_ljets_ge6j_ge3t_split_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttlf_node)
    


    # plots for ge6j_ge3t_ttX

    interf_ljets_ge6j_ge3t_ttX_ttXbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttX_node_ttXbb",
                                            label          = "ljets_ge6j_ge3t_ttX_ttXbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==0))")
    interf_ljets_ge6j_ge3t_ttX_ttXbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==0))","ljets_ge6j_ge3t_ttX_ttXbb_node","")
    interf_ljets_ge6j_ge3t_ttX_ttXbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttX_ttXbb_node.bin_edges = [ 
				0.2,
				0.275,
				0.35,
				0.425,
				0.5,
				0.575,
				0.65,
				0.725,
				0.8,
				0.95
				]
    interf_ljets_ge6j_ge3t_ttX_ttXbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttX_ttXbb_node)
    
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttX_node_ttXnonbb",
                                            label          = "ljets_ge6j_ge3t_ttX_ttXnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==1))")
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==1))","ljets_ge6j_ge3t_ttX_ttXnonbb_node","")
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node.bin_edges = [ 
				0.2,
				0.265,
				0.33,
				0.395,
				0.46,
				0.85
				]
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node)
    
    interf_ljets_ge6j_ge3t_ttX_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttX_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_ttX_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==2))")
    interf_ljets_ge6j_ge3t_ttX_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==2))","ljets_ge6j_ge3t_ttX_ttbb_node","")
    interf_ljets_ge6j_ge3t_ttX_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttX_ttbb_node.bin_edges = [ 
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
    interf_ljets_ge6j_ge3t_ttX_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttX_ttbb_node)
    
    interf_ljets_ge6j_ge3t_ttX_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttX_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_ttX_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==3))")
    interf_ljets_ge6j_ge3t_ttX_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==3))","ljets_ge6j_ge3t_ttX_ttcc_node","")
    interf_ljets_ge6j_ge3t_ttX_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttX_ttcc_node.bin_edges = [ 
				0.2,
				0.248,
				0.296,
				0.344,
				0.392,
				0.44,
				0.488,
				0.68
				]
    interf_ljets_ge6j_ge3t_ttX_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttX_ttcc_node)
    
    interf_ljets_ge6j_ge3t_ttX_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttX_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_ttX_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==4))")
    interf_ljets_ge6j_ge3t_ttX_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==4))","ljets_ge6j_ge3t_ttX_ttlf_node","")
    interf_ljets_ge6j_ge3t_ttX_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttX_ttlf_node.bin_edges = [ 
				0.2,
				0.254,
				0.308,
				0.362,
				0.416,
				0.47,
				0.524,
				0.578,
				0.632,
				0.686,
				0.74
				]
    interf_ljets_ge6j_ge3t_ttX_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttX_ttlf_node)
    


    # plots for ge6j_ge3t_ttXnonbb

    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==0))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==0))","ljets_ge6j_ge3t_ttXnonbb_ttHbb_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node.bin_edges = [ 
				0.17,
				0.234,
				0.298,
				0.362,
				0.426,
				0.49,
				0.554,
				0.618,
				0.81
				]
    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==1))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==1))","ljets_ge6j_ge3t_ttXnonbb_ttZbb_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node.bin_edges = [ 
				0.17,
				0.242,
				0.314,
				0.386,
				0.458,
				0.53,
				0.602,
				0.674,
				0.89
				]
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttXnonbb",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==2))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==2))","ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node.bin_edges = [ 
				0.17,
				0.237,
				0.304,
				0.371,
				0.438,
				0.84
				]
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node)
    
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==3))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==3))","ljets_ge6j_ge3t_ttXnonbb_ttbb_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node.bin_edges = [ 
				0.17,
				0.247,
				0.324,
				0.401,
				0.478,
				0.555,
				0.632,
				0.709,
				0.94
				]
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node)
    
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==4))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==4))","ljets_ge6j_ge3t_ttXnonbb_ttcc_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node.bin_edges = [ 
				0.17,
				0.211,
				0.252,
				0.293,
				0.334,
				0.375,
				0.416,
				0.457,
				0.498,
				0.58
				]
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node)
    
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==5))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==5))","ljets_ge6j_ge3t_ttXnonbb_ttlf_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node.bin_edges = [ 
				0.17,
				0.223,
				0.276,
				0.329,
				0.382,
				0.435,
				0.488,
				0.541,
				0.594,
				0.647,
				0.7
				]
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node)
    


    # plots for 4j_ge3t_Xnonbb_merged

    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_merged_node_ttHbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_merged_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==0))")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==0))","ljets_4j_ge3t_Xnonbb_merged_ttHbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node.bin_edges = [ 
				0.2,
				0.262,
				0.324,
				0.386,
				0.448,
				0.51,
				0.572,
				0.82
				]
    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_merged_node_ttZbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_merged_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==1))")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==1))","ljets_4j_ge3t_Xnonbb_merged_ttZbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node.bin_edges = [ 
				0.2,
				0.267,
				0.334,
				0.401,
				0.468,
				0.535,
				0.602,
				0.669,
				0.87
				]
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_merged_node_ttXnonbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==2))")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==2))","ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node.bin_edges = [ 
				0.2,
				0.276,
				0.352,
				0.428,
				0.504,
				0.58,
				0.656,
				0.96
				]
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_merged_node_ttnonbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==3))")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==3))","ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node.bin_edges = [ 
				0.2,
				0.264,
				0.328,
				0.392,
				0.456,
				0.52,
				0.584,
				0.648,
				0.712,
				0.776,
				0.84
				]
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_merged_node_ttbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_merged_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==4))")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==4))","ljets_4j_ge3t_Xnonbb_merged_ttbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node.bin_edges = [ 
				0.2,
				0.271,
				0.342,
				0.413,
				0.484,
				0.555,
				0.626,
				0.697,
				0.768,
				0.91
				]
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node)
    


    # plots for 4j_ge3t_Xnonbb_ttbar

    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_ttbar_node_ttHbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==0))")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==0))","ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node.bin_edges = [ 
				0.25,
				0.311,
				0.372,
				0.433,
				0.494,
				0.555,
				0.616,
				0.86
				]
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_ttbar_node_ttZbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==1))")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==1))","ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node.bin_edges = [ 
				0.25,
				0.32,
				0.39,
				0.46,
				0.53,
				0.6,
				0.67,
				0.74,
				0.95
				]
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_ttbar_node_ttXnonbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==2))")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==2))","ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node.bin_edges = [ 
				0.25,
				0.322,
				0.394,
				0.466,
				0.538,
				0.61,
				0.682,
				0.754,
				0.826,
				0.97
				]
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_ttbar_node_ttbar",
                                            label          = "ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==3))")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==3))","ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node","")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node.bin_edges = [ 
				0.25,
				0.316,
				0.382,
				0.448,
				0.514,
				0.58,
				0.646,
				0.712,
				0.778,
				0.844,
				0.91
				]
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node)
    


    # plots for 4j_ge3t_bb

    interf_ljets_4j_ge3t_bb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_node_ttHbb",
                                            label          = "ljets_4j_ge3t_bb_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==0))")
    interf_ljets_4j_ge3t_bb_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==0))","ljets_4j_ge3t_bb_ttHbb_node","")
    interf_ljets_4j_ge3t_bb_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttHbb_node.bin_edges = [ 
				0.2,
				0.269,
				0.338,
				0.407,
				0.476,
				0.545,
				0.614,
				0.89
				]
    interf_ljets_4j_ge3t_bb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttHbb_node)
    
    interf_ljets_4j_ge3t_bb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_node_ttZbb",
                                            label          = "ljets_4j_ge3t_bb_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==1))")
    interf_ljets_4j_ge3t_bb_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==1))","ljets_4j_ge3t_bb_ttZbb_node","")
    interf_ljets_4j_ge3t_bb_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttZbb_node.bin_edges = [ 
				0.2,
				0.274,
				0.348,
				0.422,
				0.496,
				0.57,
				0.644,
				0.718,
				0.94
				]
    interf_ljets_4j_ge3t_bb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttZbb_node)
    
    interf_ljets_4j_ge3t_bb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_node_ttbb",
                                            label          = "ljets_4j_ge3t_bb_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==2))")
    interf_ljets_4j_ge3t_bb_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==2))","ljets_4j_ge3t_bb_ttbb_node","")
    interf_ljets_4j_ge3t_bb_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttbb_node.bin_edges = [ 
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
    interf_ljets_4j_ge3t_bb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttbb_node)
    
    interf_ljets_4j_ge3t_bb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_node_ttcc",
                                            label          = "ljets_4j_ge3t_bb_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==3))")
    interf_ljets_4j_ge3t_bb_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==3))","ljets_4j_ge3t_bb_ttcc_node","")
    interf_ljets_4j_ge3t_bb_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttcc_node.bin_edges = [ 
				0.2,
				0.254,
				0.308,
				0.362,
				0.416,
				0.47,
				0.524,
				0.578,
				0.632,
				0.74
				]
    interf_ljets_4j_ge3t_bb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttcc_node)
    
    interf_ljets_4j_ge3t_bb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_node_ttlf",
                                            label          = "ljets_4j_ge3t_bb_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==4))")
    interf_ljets_4j_ge3t_bb_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==4))","ljets_4j_ge3t_bb_ttlf_node","")
    interf_ljets_4j_ge3t_bb_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttlf_node.bin_edges = [ 
				0.2,
				0.254,
				0.308,
				0.362,
				0.416,
				0.47,
				0.524,
				0.578,
				0.632,
				0.686,
				0.74
				]
    interf_ljets_4j_ge3t_bb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttlf_node)
    


    # plots for 4j_ge3t_bb_merged

    interf_ljets_4j_ge3t_bb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_merged_node_ttHbb",
                                            label          = "ljets_4j_ge3t_bb_merged_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==0))")
    interf_ljets_4j_ge3t_bb_merged_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==0))","ljets_4j_ge3t_bb_merged_ttHbb_node","")
    interf_ljets_4j_ge3t_bb_merged_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_merged_ttHbb_node.bin_edges = [ 
				0.25,
				0.311,
				0.372,
				0.433,
				0.494,
				0.555,
				0.616,
				0.677,
				0.86
				]
    interf_ljets_4j_ge3t_bb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_merged_ttHbb_node)
    
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_merged_node_ttZbb",
                                            label          = "ljets_4j_ge3t_bb_merged_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==1))")
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==1))","ljets_4j_ge3t_bb_merged_ttZbb_node","")
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node.bin_edges = [ 
				0.25,
				0.318,
				0.386,
				0.454,
				0.522,
				0.59,
				0.658,
				0.726,
				0.794,
				0.93
				]
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_merged_ttZbb_node)
    
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_merged_node_ttnonbb",
                                            label          = "ljets_4j_ge3t_bb_merged_ttnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==2))")
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==2))","ljets_4j_ge3t_bb_merged_ttnonbb_node","")
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node.bin_edges = [ 
				0.25,
				0.315,
				0.38,
				0.445,
				0.51,
				0.575,
				0.64,
				0.705,
				0.77,
				0.835,
				0.9
				]
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_merged_ttnonbb_node)
    
    interf_ljets_4j_ge3t_bb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_merged_node_ttbb",
                                            label          = "ljets_4j_ge3t_bb_merged_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==3))")
    interf_ljets_4j_ge3t_bb_merged_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==3))","ljets_4j_ge3t_bb_merged_ttbb_node","")
    interf_ljets_4j_ge3t_bb_merged_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_merged_ttbb_node.bin_edges = [ 
				0.25,
				0.321,
				0.392,
				0.463,
				0.534,
				0.605,
				0.676,
				0.747,
				0.818,
				0.889,
				0.96
				]
    interf_ljets_4j_ge3t_bb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_merged_ttbb_node)
    


    # plots for 4j_ge3t_bb_ttbar

    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_ttbar_node_ttHbb",
                                            label          = "ljets_4j_ge3t_bb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==0))")
    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==0))","ljets_4j_ge3t_bb_ttbar_ttHbb_node","")
    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node.bin_edges = [ 
				0.33,
				0.391,
				0.452,
				0.513,
				0.574,
				0.635,
				0.696,
				0.757,
				0.94
				]
    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node)
    
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_ttbar_node_ttZbb",
                                            label          = "ljets_4j_ge3t_bb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==1))")
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==1))","ljets_4j_ge3t_bb_ttbar_ttZbb_node","")
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node.bin_edges = [ 
				0.33,
				0.395,
				0.46,
				0.525,
				0.59,
				0.655,
				0.72,
				0.785,
				0.85,
				0.98
				]
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node)
    
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_ttbar_node_ttbar",
                                            label          = "ljets_4j_ge3t_bb_ttbar_ttbar_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==2))")
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==2))","ljets_4j_ge3t_bb_ttbar_ttbar_node","")
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node.bin_edges = [ 
				0.33,
				0.396,
				0.462,
				0.528,
				0.594,
				0.66,
				0.726,
				0.792,
				0.858,
				0.924,
				0.99
				]
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttbar_ttbar_node)
    


    # plots for 4j_ge3t_comb

    interf_ljets_4j_ge3t_comb_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_comb_node_ttH",
                                            label          = "ljets_4j_ge3t_comb_ttH_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==0))")
    interf_ljets_4j_ge3t_comb_ttH_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==0))","ljets_4j_ge3t_comb_ttH_node","")
    interf_ljets_4j_ge3t_comb_ttH_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_comb_ttH_node.bin_edges = [ 
				0.2,
				0.257,
				0.314,
				0.371,
				0.428,
				0.485,
				0.542,
				0.599,
				0.77
				]
    interf_ljets_4j_ge3t_comb_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_comb_ttH_node)
    
    interf_ljets_4j_ge3t_comb_ttZ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_comb_node_ttZ",
                                            label          = "ljets_4j_ge3t_comb_ttZ_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==1))")
    interf_ljets_4j_ge3t_comb_ttZ_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==1))","ljets_4j_ge3t_comb_ttZ_node","")
    interf_ljets_4j_ge3t_comb_ttZ_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_comb_ttZ_node.bin_edges = [ 
				0.2,
				0.272,
				0.344,
				0.416,
				0.488,
				0.56,
				0.92
				]
    interf_ljets_4j_ge3t_comb_ttZ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_comb_ttZ_node)
    
    interf_ljets_4j_ge3t_comb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_comb_node_ttbb",
                                            label          = "ljets_4j_ge3t_comb_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==2))")
    interf_ljets_4j_ge3t_comb_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==2))","ljets_4j_ge3t_comb_ttbb_node","")
    interf_ljets_4j_ge3t_comb_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_comb_ttbb_node.bin_edges = [ 
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
    interf_ljets_4j_ge3t_comb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_comb_ttbb_node)
    
    interf_ljets_4j_ge3t_comb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_comb_node_ttcc",
                                            label          = "ljets_4j_ge3t_comb_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==3))")
    interf_ljets_4j_ge3t_comb_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==3))","ljets_4j_ge3t_comb_ttcc_node","")
    interf_ljets_4j_ge3t_comb_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_comb_ttcc_node.bin_edges = [ 
				0.2,
				0.24,
				0.28,
				0.32,
				0.36,
				0.4,
				0.44,
				0.48,
				0.52,
				0.6
				]
    interf_ljets_4j_ge3t_comb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_comb_ttcc_node)
    
    interf_ljets_4j_ge3t_comb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_comb_node_ttlf",
                                            label          = "ljets_4j_ge3t_comb_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==4))")
    interf_ljets_4j_ge3t_comb_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==4))","ljets_4j_ge3t_comb_ttlf_node","")
    interf_ljets_4j_ge3t_comb_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_comb_ttlf_node.bin_edges = [ 
				0.2,
				0.249,
				0.298,
				0.347,
				0.396,
				0.445,
				0.494,
				0.543,
				0.592,
				0.641,
				0.69
				]
    interf_ljets_4j_ge3t_comb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_comb_ttlf_node)
    


    # plots for 4j_ge3t_split

    interf_ljets_4j_ge3t_split_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttHbb",
                                            label          = "ljets_4j_ge3t_split_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==0))")
    interf_ljets_4j_ge3t_split_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==0))","ljets_4j_ge3t_split_ttHbb_node","")
    interf_ljets_4j_ge3t_split_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttHbb_node.bin_edges = [ 
				0.14,
				0.201,
				0.262,
				0.323,
				0.384,
				0.445,
				0.506,
				0.75
				]
    interf_ljets_4j_ge3t_split_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttHbb_node)
    
    interf_ljets_4j_ge3t_split_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttHnonbb",
                                            label          = "ljets_4j_ge3t_split_ttHnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==1))")
    interf_ljets_4j_ge3t_split_ttHnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==1))","ljets_4j_ge3t_split_ttHnonbb_node","")
    interf_ljets_4j_ge3t_split_ttHnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttHnonbb_node.bin_edges = [ 
				0.14,
				0.179,
				0.218,
				0.257,
				0.296,
				0.335,
				0.53
				]
    interf_ljets_4j_ge3t_split_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttHnonbb_node)
    
    interf_ljets_4j_ge3t_split_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttZbb",
                                            label          = "ljets_4j_ge3t_split_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==2))")
    interf_ljets_4j_ge3t_split_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==2))","ljets_4j_ge3t_split_ttZbb_node","")
    interf_ljets_4j_ge3t_split_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttZbb_node.bin_edges = [ 
				0.14,
				0.211,
				0.282,
				0.353,
				0.424,
				0.495,
				0.566,
				0.85
				]
    interf_ljets_4j_ge3t_split_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttZbb_node)
    
    interf_ljets_4j_ge3t_split_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttZnonbb",
                                            label          = "ljets_4j_ge3t_split_ttZnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==3))")
    interf_ljets_4j_ge3t_split_ttZnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==3))","ljets_4j_ge3t_split_ttZnonbb_node","")
    interf_ljets_4j_ge3t_split_ttZnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttZnonbb_node.bin_edges = [ 
				0.14,
				0.208,
				0.276,
				0.344,
				0.412,
				0.48,
				0.82
				]
    interf_ljets_4j_ge3t_split_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttZnonbb_node)
    
    interf_ljets_4j_ge3t_split_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttbb",
                                            label          = "ljets_4j_ge3t_split_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==4))")
    interf_ljets_4j_ge3t_split_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==4))","ljets_4j_ge3t_split_ttbb_node","")
    interf_ljets_4j_ge3t_split_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttbb_node.bin_edges = [ 
				0.14,
				0.211,
				0.282,
				0.353,
				0.424,
				0.495,
				0.566,
				0.637,
				0.85
				]
    interf_ljets_4j_ge3t_split_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttbb_node)
    
    interf_ljets_4j_ge3t_split_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttcc",
                                            label          = "ljets_4j_ge3t_split_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==5))")
    interf_ljets_4j_ge3t_split_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==5))","ljets_4j_ge3t_split_ttcc_node","")
    interf_ljets_4j_ge3t_split_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttcc_node.bin_edges = [ 
				0.14,
				0.175,
				0.21,
				0.245,
				0.28,
				0.315,
				0.35,
				0.385,
				0.42,
				0.49
				]
    interf_ljets_4j_ge3t_split_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttcc_node)
    
    interf_ljets_4j_ge3t_split_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttlf",
                                            label          = "ljets_4j_ge3t_split_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==6))")
    interf_ljets_4j_ge3t_split_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==6))","ljets_4j_ge3t_split_ttlf_node","")
    interf_ljets_4j_ge3t_split_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttlf_node.bin_edges = [ 
				0.14,
				0.191,
				0.242,
				0.293,
				0.344,
				0.395,
				0.446,
				0.497,
				0.548,
				0.599,
				0.65
				]
    interf_ljets_4j_ge3t_split_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttlf_node)
    


    # plots for 4j_ge3t_ttX

    interf_ljets_4j_ge3t_ttX_ttXbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttX_node_ttXbb",
                                            label          = "ljets_4j_ge3t_ttX_ttXbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==0))")
    interf_ljets_4j_ge3t_ttX_ttXbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==0))","ljets_4j_ge3t_ttX_ttXbb_node","")
    interf_ljets_4j_ge3t_ttX_ttXbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttX_ttXbb_node.bin_edges = [ 
				0.2,
				0.275,
				0.35,
				0.425,
				0.5,
				0.575,
				0.65,
				0.725,
				0.8,
				0.95
				]
    interf_ljets_4j_ge3t_ttX_ttXbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttX_ttXbb_node)
    
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttX_node_ttXnonbb",
                                            label          = "ljets_4j_ge3t_ttX_ttXnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==1))")
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==1))","ljets_4j_ge3t_ttX_ttXnonbb_node","")
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node.bin_edges = [ 
				0.2,
				0.273,
				0.346,
				0.419,
				0.492,
				0.565,
				0.93
				]
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttX_ttXnonbb_node)
    
    interf_ljets_4j_ge3t_ttX_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttX_node_ttbb",
                                            label          = "ljets_4j_ge3t_ttX_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==2))")
    interf_ljets_4j_ge3t_ttX_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==2))","ljets_4j_ge3t_ttX_ttbb_node","")
    interf_ljets_4j_ge3t_ttX_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttX_ttbb_node.bin_edges = [ 
				0.2,
				0.27,
				0.34,
				0.41,
				0.48,
				0.55,
				0.62,
				0.69,
				0.76,
				0.9
				]
    interf_ljets_4j_ge3t_ttX_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttX_ttbb_node)
    
    interf_ljets_4j_ge3t_ttX_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttX_node_ttcc",
                                            label          = "ljets_4j_ge3t_ttX_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==3))")
    interf_ljets_4j_ge3t_ttX_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==3))","ljets_4j_ge3t_ttX_ttcc_node","")
    interf_ljets_4j_ge3t_ttX_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttX_ttcc_node.bin_edges = [ 
				0.2,
				0.239,
				0.278,
				0.317,
				0.356,
				0.395,
				0.434,
				0.473,
				0.512,
				0.59
				]
    interf_ljets_4j_ge3t_ttX_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttX_ttcc_node)
    
    interf_ljets_4j_ge3t_ttX_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttX_node_ttlf",
                                            label          = "ljets_4j_ge3t_ttX_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==4))")
    interf_ljets_4j_ge3t_ttX_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==4))","ljets_4j_ge3t_ttX_ttlf_node","")
    interf_ljets_4j_ge3t_ttX_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttX_ttlf_node.bin_edges = [ 
				0.2,
				0.253,
				0.306,
				0.359,
				0.412,
				0.465,
				0.518,
				0.571,
				0.624,
				0.73
				]
    interf_ljets_4j_ge3t_ttX_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttX_ttlf_node)
    


    # plots for 4j_ge3t_ttXnonbb

    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttHbb",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==0))")
    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==0))","ljets_4j_ge3t_ttXnonbb_ttHbb_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node.bin_edges = [ 
				0.17,
				0.24,
				0.31,
				0.38,
				0.45,
				0.52,
				0.87
				]
    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node)
    
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttZbb",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==1))")
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==1))","ljets_4j_ge3t_ttXnonbb_ttZbb_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node.bin_edges = [ 
				0.17,
				0.247,
				0.324,
				0.401,
				0.478,
				0.555,
				0.632,
				0.94
				]
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node)
    
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttXnonbb",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttXnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==2))")
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==2))","ljets_4j_ge3t_ttXnonbb_ttXnonbb_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node.bin_edges = [ 
				0.17,
				0.248,
				0.326,
				0.404,
				0.482,
				0.56,
				0.95
				]
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node)
    
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttbb",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==3))")
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==3))","ljets_4j_ge3t_ttXnonbb_ttbb_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node.bin_edges = [ 
				0.17,
				0.247,
				0.324,
				0.401,
				0.478,
				0.555,
				0.632,
				0.709,
				0.94
				]
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttbb_node)
    
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttcc",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==4))")
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==4))","ljets_4j_ge3t_ttXnonbb_ttcc_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node.bin_edges = [ 
				0.17,
				0.207,
				0.244,
				0.281,
				0.318,
				0.355,
				0.392,
				0.429,
				0.466,
				0.54
				]
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttcc_node)
    
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttlf",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==5))")
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==5))","ljets_4j_ge3t_ttXnonbb_ttlf_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node.bin_edges = [ 
				0.17,
				0.219,
				0.268,
				0.317,
				0.366,
				0.415,
				0.464,
				0.513,
				0.562,
				0.611,
				0.66
				]
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttlf_node)
    


    # plots for 5j_ge3t_Xnonbb_merged

    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_merged_node_ttHbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_merged_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==0))")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==0))","ljets_5j_ge3t_Xnonbb_merged_ttHbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node.bin_edges = [ 
				0.2,
				0.262,
				0.324,
				0.386,
				0.448,
				0.51,
				0.572,
				0.82
				]
    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_merged_node_ttZbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_merged_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==1))")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==1))","ljets_5j_ge3t_Xnonbb_merged_ttZbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node.bin_edges = [ 
				0.2,
				0.269,
				0.338,
				0.407,
				0.476,
				0.545,
				0.614,
				0.683,
				0.89
				]
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_merged_node_ttXnonbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==2))")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==2))","ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node.bin_edges = [ 
				0.2,
				0.274,
				0.348,
				0.422,
				0.496,
				0.57,
				0.94
				]
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_merged_node_ttnonbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==3))")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==3))","ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node.bin_edges = [ 
				0.2,
				0.266,
				0.332,
				0.398,
				0.464,
				0.53,
				0.596,
				0.662,
				0.728,
				0.794,
				0.86
				]
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_merged_node_ttbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_merged_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==4))")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==4))","ljets_5j_ge3t_Xnonbb_merged_ttbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node.bin_edges = [ 
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
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node)
    


    # plots for 5j_ge3t_Xnonbb_ttbar

    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_ttbar_node_ttHbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==0))")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==0))","ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node.bin_edges = [ 
				0.25,
				0.309,
				0.368,
				0.427,
				0.486,
				0.545,
				0.604,
				0.663,
				0.84
				]
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_ttbar_node_ttZbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==1))")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==1))","ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node.bin_edges = [ 
				0.25,
				0.318,
				0.386,
				0.454,
				0.522,
				0.59,
				0.658,
				0.726,
				0.93
				]
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_ttbar_node_ttXnonbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==2))")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==2))","ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node.bin_edges = [ 
				0.25,
				0.319,
				0.388,
				0.457,
				0.526,
				0.595,
				0.664,
				0.94
				]
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_ttbar_node_ttbar",
                                            label          = "ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==3))")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==3))","ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node","")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node.bin_edges = [ 
				0.25,
				0.312,
				0.374,
				0.436,
				0.498,
				0.56,
				0.622,
				0.684,
				0.746,
				0.808,
				0.87
				]
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node)
    


    # plots for 5j_ge3t_bb

    interf_ljets_5j_ge3t_bb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_node_ttHbb",
                                            label          = "ljets_5j_ge3t_bb_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==0))")
    interf_ljets_5j_ge3t_bb_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==0))","ljets_5j_ge3t_bb_ttHbb_node","")
    interf_ljets_5j_ge3t_bb_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttHbb_node.bin_edges = [ 
				0.2,
				0.266,
				0.332,
				0.398,
				0.464,
				0.53,
				0.596,
				0.662,
				0.86
				]
    interf_ljets_5j_ge3t_bb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttHbb_node)
    
    interf_ljets_5j_ge3t_bb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_node_ttZbb",
                                            label          = "ljets_5j_ge3t_bb_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==1))")
    interf_ljets_5j_ge3t_bb_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==1))","ljets_5j_ge3t_bb_ttZbb_node","")
    interf_ljets_5j_ge3t_bb_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttZbb_node.bin_edges = [ 
				0.2,
				0.27,
				0.34,
				0.41,
				0.48,
				0.55,
				0.62,
				0.69,
				0.9
				]
    interf_ljets_5j_ge3t_bb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttZbb_node)
    
    interf_ljets_5j_ge3t_bb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_node_ttbb",
                                            label          = "ljets_5j_ge3t_bb_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==2))")
    interf_ljets_5j_ge3t_bb_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==2))","ljets_5j_ge3t_bb_ttbb_node","")
    interf_ljets_5j_ge3t_bb_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttbb_node.bin_edges = [ 
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
    interf_ljets_5j_ge3t_bb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttbb_node)
    
    interf_ljets_5j_ge3t_bb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_node_ttcc",
                                            label          = "ljets_5j_ge3t_bb_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==3))")
    interf_ljets_5j_ge3t_bb_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==3))","ljets_5j_ge3t_bb_ttcc_node","")
    interf_ljets_5j_ge3t_bb_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttcc_node.bin_edges = [ 
				0.2,
				0.249,
				0.298,
				0.347,
				0.396,
				0.445,
				0.494,
				0.543,
				0.69
				]
    interf_ljets_5j_ge3t_bb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttcc_node)
    
    interf_ljets_5j_ge3t_bb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_node_ttlf",
                                            label          = "ljets_5j_ge3t_bb_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==4))")
    interf_ljets_5j_ge3t_bb_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==4))","ljets_5j_ge3t_bb_ttlf_node","")
    interf_ljets_5j_ge3t_bb_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttlf_node.bin_edges = [ 
				0.2,
				0.253,
				0.306,
				0.359,
				0.412,
				0.465,
				0.518,
				0.571,
				0.624,
				0.73
				]
    interf_ljets_5j_ge3t_bb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttlf_node)
    


    # plots for 5j_ge3t_bb_merged

    interf_ljets_5j_ge3t_bb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_merged_node_ttHbb",
                                            label          = "ljets_5j_ge3t_bb_merged_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==0))")
    interf_ljets_5j_ge3t_bb_merged_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==0))","ljets_5j_ge3t_bb_merged_ttHbb_node","")
    interf_ljets_5j_ge3t_bb_merged_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_merged_ttHbb_node.bin_edges = [ 
				0.25,
				0.312,
				0.374,
				0.436,
				0.498,
				0.56,
				0.622,
				0.684,
				0.87
				]
    interf_ljets_5j_ge3t_bb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_merged_ttHbb_node)
    
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_merged_node_ttZbb",
                                            label          = "ljets_5j_ge3t_bb_merged_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==1))")
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==1))","ljets_5j_ge3t_bb_merged_ttZbb_node","")
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node.bin_edges = [ 
				0.25,
				0.317,
				0.384,
				0.451,
				0.518,
				0.585,
				0.652,
				0.719,
				0.92
				]
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_merged_ttZbb_node)
    
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_merged_node_ttnonbb",
                                            label          = "ljets_5j_ge3t_bb_merged_ttnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==2))")
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==2))","ljets_5j_ge3t_bb_merged_ttnonbb_node","")
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node.bin_edges = [ 
				0.25,
				0.318,
				0.386,
				0.454,
				0.522,
				0.59,
				0.658,
				0.726,
				0.794,
				0.862,
				0.93
				]
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_merged_ttnonbb_node)
    
    interf_ljets_5j_ge3t_bb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_merged_node_ttbb",
                                            label          = "ljets_5j_ge3t_bb_merged_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==3))")
    interf_ljets_5j_ge3t_bb_merged_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==3))","ljets_5j_ge3t_bb_merged_ttbb_node","")
    interf_ljets_5j_ge3t_bb_merged_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_merged_ttbb_node.bin_edges = [ 
				0.25,
				0.322,
				0.394,
				0.466,
				0.538,
				0.61,
				0.682,
				0.754,
				0.826,
				0.97
				]
    interf_ljets_5j_ge3t_bb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_merged_ttbb_node)
    


    # plots for 5j_ge3t_bb_ttbar

    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_ttbar_node_ttHbb",
                                            label          = "ljets_5j_ge3t_bb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==0))")
    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==0))","ljets_5j_ge3t_bb_ttbar_ttHbb_node","")
    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node.bin_edges = [ 
				0.33,
				0.388,
				0.446,
				0.504,
				0.562,
				0.62,
				0.678,
				0.736,
				0.794,
				0.91
				]
    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node)
    
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_ttbar_node_ttZbb",
                                            label          = "ljets_5j_ge3t_bb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==1))")
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==1))","ljets_5j_ge3t_bb_ttbar_ttZbb_node","")
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node.bin_edges = [ 
				0.33,
				0.393,
				0.456,
				0.519,
				0.582,
				0.645,
				0.708,
				0.771,
				0.834,
				0.96
				]
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node)
    
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_ttbar_node_ttbar",
                                            label          = "ljets_5j_ge3t_bb_ttbar_ttbar_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==2))")
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==2))","ljets_5j_ge3t_bb_ttbar_ttbar_node","")
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node.bin_edges = [ 
				0.33,
				0.395,
				0.46,
				0.525,
				0.59,
				0.655,
				0.72,
				0.785,
				0.85,
				0.915,
				0.98
				]
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttbar_ttbar_node)
    


    # plots for 5j_ge3t_comb

    interf_ljets_5j_ge3t_comb_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_comb_node_ttH",
                                            label          = "ljets_5j_ge3t_comb_ttH_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==0))")
    interf_ljets_5j_ge3t_comb_ttH_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==0))","ljets_5j_ge3t_comb_ttH_node","")
    interf_ljets_5j_ge3t_comb_ttH_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_comb_ttH_node.bin_edges = [ 
				0.2,
				0.258,
				0.316,
				0.374,
				0.432,
				0.49,
				0.548,
				0.606,
				0.78
				]
    interf_ljets_5j_ge3t_comb_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_comb_ttH_node)
    
    interf_ljets_5j_ge3t_comb_ttZ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_comb_node_ttZ",
                                            label          = "ljets_5j_ge3t_comb_ttZ_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==1))")
    interf_ljets_5j_ge3t_comb_ttZ_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==1))","ljets_5j_ge3t_comb_ttZ_node","")
    interf_ljets_5j_ge3t_comb_ttZ_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_comb_ttZ_node.bin_edges = [ 
				0.2,
				0.268,
				0.336,
				0.404,
				0.472,
				0.54,
				0.88
				]
    interf_ljets_5j_ge3t_comb_ttZ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_comb_ttZ_node)
    
    interf_ljets_5j_ge3t_comb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_comb_node_ttbb",
                                            label          = "ljets_5j_ge3t_comb_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==2))")
    interf_ljets_5j_ge3t_comb_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==2))","ljets_5j_ge3t_comb_ttbb_node","")
    interf_ljets_5j_ge3t_comb_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_comb_ttbb_node.bin_edges = [ 
				0.2,
				0.271,
				0.342,
				0.413,
				0.484,
				0.555,
				0.626,
				0.697,
				0.91
				]
    interf_ljets_5j_ge3t_comb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_comb_ttbb_node)
    
    interf_ljets_5j_ge3t_comb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_comb_node_ttcc",
                                            label          = "ljets_5j_ge3t_comb_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==3))")
    interf_ljets_5j_ge3t_comb_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==3))","ljets_5j_ge3t_comb_ttcc_node","")
    interf_ljets_5j_ge3t_comb_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_comb_ttcc_node.bin_edges = [ 
				0.2,
				0.236,
				0.272,
				0.308,
				0.344,
				0.38,
				0.416,
				0.452,
				0.488,
				0.56
				]
    interf_ljets_5j_ge3t_comb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_comb_ttcc_node)
    
    interf_ljets_5j_ge3t_comb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_comb_node_ttlf",
                                            label          = "ljets_5j_ge3t_comb_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==4))")
    interf_ljets_5j_ge3t_comb_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==4))","ljets_5j_ge3t_comb_ttlf_node","")
    interf_ljets_5j_ge3t_comb_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_comb_ttlf_node.bin_edges = [ 
				0.2,
				0.249,
				0.298,
				0.347,
				0.396,
				0.445,
				0.494,
				0.543,
				0.592,
				0.69
				]
    interf_ljets_5j_ge3t_comb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_comb_ttlf_node)
    


    # plots for 5j_ge3t_split

    interf_ljets_5j_ge3t_split_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttHbb",
                                            label          = "ljets_5j_ge3t_split_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==0))")
    interf_ljets_5j_ge3t_split_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==0))","ljets_5j_ge3t_split_ttHbb_node","")
    interf_ljets_5j_ge3t_split_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttHbb_node.bin_edges = [ 
				0.14,
				0.199,
				0.258,
				0.317,
				0.376,
				0.435,
				0.494,
				0.73
				]
    interf_ljets_5j_ge3t_split_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttHbb_node)
    
    interf_ljets_5j_ge3t_split_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttHnonbb",
                                            label          = "ljets_5j_ge3t_split_ttHnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==1))")
    interf_ljets_5j_ge3t_split_ttHnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==1))","ljets_5j_ge3t_split_ttHnonbb_node","")
    interf_ljets_5j_ge3t_split_ttHnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttHnonbb_node.bin_edges = [ 
				0.14,
				0.173,
				0.206,
				0.239,
				0.272,
				0.305,
				0.338,
				0.47
				]
    interf_ljets_5j_ge3t_split_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttHnonbb_node)
    
    interf_ljets_5j_ge3t_split_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttZbb",
                                            label          = "ljets_5j_ge3t_split_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==2))")
    interf_ljets_5j_ge3t_split_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==2))","ljets_5j_ge3t_split_ttZbb_node","")
    interf_ljets_5j_ge3t_split_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttZbb_node.bin_edges = [ 
				0.14,
				0.217,
				0.294,
				0.371,
				0.448,
				0.525,
				0.602,
				0.91
				]
    interf_ljets_5j_ge3t_split_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttZbb_node)
    
    interf_ljets_5j_ge3t_split_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttZnonbb",
                                            label          = "ljets_5j_ge3t_split_ttZnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==3))")
    interf_ljets_5j_ge3t_split_ttZnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==3))","ljets_5j_ge3t_split_ttZnonbb_node","")
    interf_ljets_5j_ge3t_split_ttZnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttZnonbb_node.bin_edges = [ 
				0.14,
				0.212,
				0.284,
				0.356,
				0.428,
				0.5,
				0.86
				]
    interf_ljets_5j_ge3t_split_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttZnonbb_node)
    
    interf_ljets_5j_ge3t_split_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttbb",
                                            label          = "ljets_5j_ge3t_split_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==4))")
    interf_ljets_5j_ge3t_split_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==4))","ljets_5j_ge3t_split_ttbb_node","")
    interf_ljets_5j_ge3t_split_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttbb_node.bin_edges = [ 
				0.14,
				0.202,
				0.264,
				0.326,
				0.388,
				0.45,
				0.512,
				0.574,
				0.636,
				0.76
				]
    interf_ljets_5j_ge3t_split_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttbb_node)
    
    interf_ljets_5j_ge3t_split_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttcc",
                                            label          = "ljets_5j_ge3t_split_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==5))")
    interf_ljets_5j_ge3t_split_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==5))","ljets_5j_ge3t_split_ttcc_node","")
    interf_ljets_5j_ge3t_split_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttcc_node.bin_edges = [ 
				0.174,
				0.208,
				0.242,
				0.276,
				0.31,
				0.344,
				0.378,
				0.412,
				0.48
				]
    interf_ljets_5j_ge3t_split_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttcc_node)
    
    interf_ljets_5j_ge3t_split_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttlf",
                                            label          = "ljets_5j_ge3t_split_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==6))")
    interf_ljets_5j_ge3t_split_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==6))","ljets_5j_ge3t_split_ttlf_node","")
    interf_ljets_5j_ge3t_split_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttlf_node.bin_edges = [ 
				0.14,
				0.195,
				0.25,
				0.305,
				0.36,
				0.415,
				0.47,
				0.525,
				0.58,
				0.69
				]
    interf_ljets_5j_ge3t_split_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttlf_node)
    


    # plots for 5j_ge3t_ttX

    interf_ljets_5j_ge3t_ttX_ttXbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttX_node_ttXbb",
                                            label          = "ljets_5j_ge3t_ttX_ttXbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==0))")
    interf_ljets_5j_ge3t_ttX_ttXbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==0))","ljets_5j_ge3t_ttX_ttXbb_node","")
    interf_ljets_5j_ge3t_ttX_ttXbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttX_ttXbb_node.bin_edges = [ 
				0.2,
				0.274,
				0.348,
				0.422,
				0.496,
				0.57,
				0.644,
				0.718,
				0.792,
				0.94
				]
    interf_ljets_5j_ge3t_ttX_ttXbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttX_ttXbb_node)
    
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttX_node_ttXnonbb",
                                            label          = "ljets_5j_ge3t_ttX_ttXnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==1))")
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==1))","ljets_5j_ge3t_ttX_ttXnonbb_node","")
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node.bin_edges = [ 
				0.2,
				0.271,
				0.342,
				0.413,
				0.484,
				0.91
				]
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttX_ttXnonbb_node)
    
    interf_ljets_5j_ge3t_ttX_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttX_node_ttbb",
                                            label          = "ljets_5j_ge3t_ttX_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==2))")
    interf_ljets_5j_ge3t_ttX_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==2))","ljets_5j_ge3t_ttX_ttbb_node","")
    interf_ljets_5j_ge3t_ttX_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttX_ttbb_node.bin_edges = [ 
				0.2,
				0.27,
				0.34,
				0.41,
				0.48,
				0.55,
				0.62,
				0.69,
				0.76,
				0.9
				]
    interf_ljets_5j_ge3t_ttX_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttX_ttbb_node)
    
    interf_ljets_5j_ge3t_ttX_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttX_node_ttcc",
                                            label          = "ljets_5j_ge3t_ttX_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==3))")
    interf_ljets_5j_ge3t_ttX_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==3))","ljets_5j_ge3t_ttX_ttcc_node","")
    interf_ljets_5j_ge3t_ttX_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttX_ttcc_node.bin_edges = [ 
				0.2,
				0.238,
				0.276,
				0.314,
				0.352,
				0.39,
				0.428,
				0.466,
				0.58
				]
    interf_ljets_5j_ge3t_ttX_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttX_ttcc_node)
    
    interf_ljets_5j_ge3t_ttX_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttX_node_ttlf",
                                            label          = "ljets_5j_ge3t_ttX_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==4))")
    interf_ljets_5j_ge3t_ttX_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==4))","ljets_5j_ge3t_ttX_ttlf_node","")
    interf_ljets_5j_ge3t_ttX_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttX_ttlf_node.bin_edges = [ 
				0.2,
				0.252,
				0.304,
				0.356,
				0.408,
				0.46,
				0.512,
				0.564,
				0.616,
				0.72
				]
    interf_ljets_5j_ge3t_ttX_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttX_ttlf_node)
    


    # plots for 5j_ge3t_ttXnonbb

    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttHbb",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==0))")
    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==0))","ljets_5j_ge3t_ttXnonbb_ttHbb_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node.bin_edges = [ 
				0.17,
				0.233,
				0.296,
				0.359,
				0.422,
				0.485,
				0.548,
				0.8
				]
    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node)
    
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttZbb",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==1))")
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==1))","ljets_5j_ge3t_ttXnonbb_ttZbb_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node.bin_edges = [ 
				0.17,
				0.243,
				0.316,
				0.389,
				0.462,
				0.535,
				0.608,
				0.681,
				0.9
				]
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node)
    
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttXnonbb",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttXnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==2))")
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==2))","ljets_5j_ge3t_ttXnonbb_ttXnonbb_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node.bin_edges = [ 
				0.17,
				0.237,
				0.304,
				0.371,
				0.438,
				0.505,
				0.84
				]
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node)
    
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttbb",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==3))")
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==3))","ljets_5j_ge3t_ttXnonbb_ttbb_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node.bin_edges = [ 
				0.17,
				0.237,
				0.304,
				0.371,
				0.438,
				0.505,
				0.572,
				0.639,
				0.706,
				0.84
				]
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttbb_node)
    
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttcc",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==4))")
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==4))","ljets_5j_ge3t_ttXnonbb_ttcc_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node.bin_edges = [ 
				0.17,
				0.21,
				0.25,
				0.29,
				0.33,
				0.37,
				0.41,
				0.45,
				0.57
				]
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttcc_node)
    
    interf_ljets_5j_ge3t_ttXnonbb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttlf",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==5))")
    interf_ljets_5j_ge3t_ttXnonbb_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==5))","ljets_5j_ge3t_ttXnonbb_ttlf_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttlf_node.bin_edges = [ 
				0.17,
				0.222,
				0.274,
				0.326,
				0.378,
				0.43,
				0.482,
				0.534,
				0.586,
				0.69
				]
    interf_ljets_5j_ge3t_ttXnonbb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttlf_node)
    

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
    