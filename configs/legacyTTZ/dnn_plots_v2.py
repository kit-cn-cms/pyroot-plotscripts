
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
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node.maxxval = 0.82
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_merged_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_merged_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==1))")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==1))","ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node.maxxval = 0.9
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_merged_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_merged_node_ttXnonbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==2))")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==2))","ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node.maxxval = 0.81
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_merged_ttXnonbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_merged_node_ttnonbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==3))")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==3))","ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node.maxxval = 0.85
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_merged_ttnonbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_merged_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==4))")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_merged==4))","ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node.maxxval = 0.87
    interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_merged_ttbb_node)
    


    # plots for ge6j_ge3t_Xnonbb_ttbar

    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_ttbar_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==0))")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==0))","ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node.minxval = 0.25
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node.maxxval = 0.85
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_ttbar_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==1))")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==1))","ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node.minxval = 0.25
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node.maxxval = 0.92
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_ttbar_node_ttXnonbb",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==2))")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==2))","ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node.minxval = 0.25
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node.maxxval = 0.96
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttXnonbb_node)
    
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_Xnonbb_ttbar_node_ttbar",
                                            label          = "ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==3))")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_Xnonbb_ttbar==3))","ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node","")
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node.minxval = 0.25
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node.maxxval = 0.91
    interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_Xnonbb_ttbar_ttbar_node)
    


    # plots for ge6j_ge3t_bb

    interf_ljets_ge6j_ge3t_bb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_bb_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==0))")
    interf_ljets_ge6j_ge3t_bb_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==0))","ljets_ge6j_ge3t_bb_ttHbb_node","")
    interf_ljets_ge6j_ge3t_bb_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttHbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_bb_ttHbb_node.maxxval = 0.84
    interf_ljets_ge6j_ge3t_bb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_bb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_bb_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==1))")
    interf_ljets_ge6j_ge3t_bb_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==1))","ljets_ge6j_ge3t_bb_ttZbb_node","")
    interf_ljets_ge6j_ge3t_bb_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttZbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_bb_ttZbb_node.maxxval = 0.92
    interf_ljets_ge6j_ge3t_bb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_bb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_bb_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==2))")
    interf_ljets_ge6j_ge3t_bb_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==2))","ljets_ge6j_ge3t_bb_ttbb_node","")
    interf_ljets_ge6j_ge3t_bb_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_bb_ttbb_node.maxxval = 0.97
    interf_ljets_ge6j_ge3t_bb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttbb_node)
    
    interf_ljets_ge6j_ge3t_bb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_bb_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==3))")
    interf_ljets_ge6j_ge3t_bb_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==3))","ljets_ge6j_ge3t_bb_ttcc_node","")
    interf_ljets_ge6j_ge3t_bb_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttcc_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_bb_ttcc_node.maxxval = 0.69
    interf_ljets_ge6j_ge3t_bb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttcc_node)
    
    interf_ljets_ge6j_ge3t_bb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_bb_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==4))")
    interf_ljets_ge6j_ge3t_bb_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb==4))","ljets_ge6j_ge3t_bb_ttlf_node","")
    interf_ljets_ge6j_ge3t_bb_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttlf_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_bb_ttlf_node.maxxval = 0.78
    interf_ljets_ge6j_ge3t_bb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttlf_node)
    


    # plots for ge6j_ge3t_bb_merged

    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_merged_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_bb_merged_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==0))")
    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==0))","ljets_ge6j_ge3t_bb_merged_ttHbb_node","")
    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node.minxval = 0.25
    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node.maxxval = 0.85
    interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_merged_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_merged_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_bb_merged_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==1))")
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==1))","ljets_ge6j_ge3t_bb_merged_ttZbb_node","")
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node.minxval = 0.25
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node.maxxval = 0.91
    interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_merged_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_merged_node_ttnonbb",
                                            label          = "ljets_ge6j_ge3t_bb_merged_ttnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==2))")
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==2))","ljets_ge6j_ge3t_bb_merged_ttnonbb_node","")
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node.minxval = 0.25
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node.maxxval = 0.92
    interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_merged_ttnonbb_node)
    
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_merged_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_bb_merged_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==3))")
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_merged==3))","ljets_ge6j_ge3t_bb_merged_ttbb_node","")
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node.minxval = 0.25
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node.maxxval = 0.95
    interf_ljets_ge6j_ge3t_bb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_merged_ttbb_node)
    


    # plots for ge6j_ge3t_bb_ttbar

    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_ttbar_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_bb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==0))")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==0))","ljets_ge6j_ge3t_bb_ttbar_ttHbb_node","")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node.minxval = 0.33
    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node.maxxval = 0.93
    interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttbar_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_ttbar_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_bb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==1))")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==1))","ljets_ge6j_ge3t_bb_ttbar_ttZbb_node","")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node.minxval = 0.33
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node.maxxval = 0.96
    interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttbar_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_bb_ttbar_node_ttbar",
                                            label          = "ljets_ge6j_ge3t_bb_ttbar_ttbar_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==2))")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_bb_ttbar==2))","ljets_ge6j_ge3t_bb_ttbar_ttbar_node","")
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node.minxval = 0.33
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node.maxxval = 0.99
    interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_bb_ttbar_ttbar_node)
    


    # plots for ge6j_ge3t_comb

    interf_ljets_ge6j_ge3t_comb_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_comb_node_ttH",
                                            label          = "ljets_ge6j_ge3t_comb_ttH_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==0))")
    interf_ljets_ge6j_ge3t_comb_ttH_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==0))","ljets_ge6j_ge3t_comb_ttH_node","")
    interf_ljets_ge6j_ge3t_comb_ttH_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_comb_ttH_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_comb_ttH_node.maxxval = 0.78
    interf_ljets_ge6j_ge3t_comb_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_comb_ttH_node)
    
    interf_ljets_ge6j_ge3t_comb_ttZ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_comb_node_ttZ",
                                            label          = "ljets_ge6j_ge3t_comb_ttZ_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==1))")
    interf_ljets_ge6j_ge3t_comb_ttZ_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==1))","ljets_ge6j_ge3t_comb_ttZ_node","")
    interf_ljets_ge6j_ge3t_comb_ttZ_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_comb_ttZ_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_comb_ttZ_node.maxxval = 0.81
    interf_ljets_ge6j_ge3t_comb_ttZ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_comb_ttZ_node)
    
    interf_ljets_ge6j_ge3t_comb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_comb_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_comb_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==2))")
    interf_ljets_ge6j_ge3t_comb_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==2))","ljets_ge6j_ge3t_comb_ttbb_node","")
    interf_ljets_ge6j_ge3t_comb_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_comb_ttbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_comb_ttbb_node.maxxval = 0.88
    interf_ljets_ge6j_ge3t_comb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_comb_ttbb_node)
    
    interf_ljets_ge6j_ge3t_comb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_comb_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_comb_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==3))")
    interf_ljets_ge6j_ge3t_comb_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==3))","ljets_ge6j_ge3t_comb_ttcc_node","")
    interf_ljets_ge6j_ge3t_comb_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_comb_ttcc_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_comb_ttcc_node.maxxval = 0.57
    interf_ljets_ge6j_ge3t_comb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_comb_ttcc_node)
    
    interf_ljets_ge6j_ge3t_comb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_comb_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_comb_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==4))")
    interf_ljets_ge6j_ge3t_comb_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_comb==4))","ljets_ge6j_ge3t_comb_ttlf_node","")
    interf_ljets_ge6j_ge3t_comb_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_comb_ttlf_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_comb_ttlf_node.maxxval = 0.73
    interf_ljets_ge6j_ge3t_comb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_comb_ttlf_node)
    


    # plots for ge6j_ge3t_split

    interf_ljets_ge6j_ge3t_split_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_split_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==0))")
    interf_ljets_ge6j_ge3t_split_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==0))","ljets_ge6j_ge3t_split_ttHbb_node","")
    interf_ljets_ge6j_ge3t_split_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttHbb_node.minxval = 0.14
    interf_ljets_ge6j_ge3t_split_ttHbb_node.maxxval = 0.74
    interf_ljets_ge6j_ge3t_split_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttHnonbb",
                                            label          = "ljets_ge6j_ge3t_split_ttHnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==1))")
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==1))","ljets_ge6j_ge3t_split_ttHnonbb_node","")
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node.minxval = 0.14
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node.maxxval = 0.4
    interf_ljets_ge6j_ge3t_split_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttHnonbb_node)
    
    interf_ljets_ge6j_ge3t_split_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_split_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==2))")
    interf_ljets_ge6j_ge3t_split_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==2))","ljets_ge6j_ge3t_split_ttZbb_node","")
    interf_ljets_ge6j_ge3t_split_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttZbb_node.minxval = 0.14
    interf_ljets_ge6j_ge3t_split_ttZbb_node.maxxval = 0.86
    interf_ljets_ge6j_ge3t_split_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttZnonbb",
                                            label          = "ljets_ge6j_ge3t_split_ttZnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==3))")
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==3))","ljets_ge6j_ge3t_split_ttZnonbb_node","")
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node.minxval = 0.14
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node.maxxval = 0.7
    interf_ljets_ge6j_ge3t_split_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttZnonbb_node)
    
    interf_ljets_ge6j_ge3t_split_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_split_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==4))")
    interf_ljets_ge6j_ge3t_split_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==4))","ljets_ge6j_ge3t_split_ttbb_node","")
    interf_ljets_ge6j_ge3t_split_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttbb_node.minxval = 0.14
    interf_ljets_ge6j_ge3t_split_ttbb_node.maxxval = 0.81
    interf_ljets_ge6j_ge3t_split_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttbb_node)
    
    interf_ljets_ge6j_ge3t_split_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_split_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==5))")
    interf_ljets_ge6j_ge3t_split_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==5))","ljets_ge6j_ge3t_split_ttcc_node","")
    interf_ljets_ge6j_ge3t_split_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttcc_node.minxval = 0.14
    interf_ljets_ge6j_ge3t_split_ttcc_node.maxxval = 0.52
    interf_ljets_ge6j_ge3t_split_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttcc_node)
    
    interf_ljets_ge6j_ge3t_split_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_split_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_split_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==6))")
    interf_ljets_ge6j_ge3t_split_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_split==6))","ljets_ge6j_ge3t_split_ttlf_node","")
    interf_ljets_ge6j_ge3t_split_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_split_ttlf_node.minxval = 0.14
    interf_ljets_ge6j_ge3t_split_ttlf_node.maxxval = 0.75
    interf_ljets_ge6j_ge3t_split_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_split_ttlf_node)
    


    # plots for ge6j_ge3t_ttX

    interf_ljets_ge6j_ge3t_ttX_ttXbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttX_node_ttXbb",
                                            label          = "ljets_ge6j_ge3t_ttX_ttXbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==0))")
    interf_ljets_ge6j_ge3t_ttX_ttXbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==0))","ljets_ge6j_ge3t_ttX_ttXbb_node","")
    interf_ljets_ge6j_ge3t_ttX_ttXbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttX_ttXbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_ttX_ttXbb_node.maxxval = 0.95
    interf_ljets_ge6j_ge3t_ttX_ttXbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttX_ttXbb_node)
    
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttX_node_ttXnonbb",
                                            label          = "ljets_ge6j_ge3t_ttX_ttXnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==1))")
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==1))","ljets_ge6j_ge3t_ttX_ttXnonbb_node","")
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node.maxxval = 0.85
    interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttX_ttXnonbb_node)
    
    interf_ljets_ge6j_ge3t_ttX_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttX_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_ttX_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==2))")
    interf_ljets_ge6j_ge3t_ttX_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==2))","ljets_ge6j_ge3t_ttX_ttbb_node","")
    interf_ljets_ge6j_ge3t_ttX_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttX_ttbb_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_ttX_ttbb_node.maxxval = 0.84
    interf_ljets_ge6j_ge3t_ttX_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttX_ttbb_node)
    
    interf_ljets_ge6j_ge3t_ttX_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttX_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_ttX_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==3))")
    interf_ljets_ge6j_ge3t_ttX_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==3))","ljets_ge6j_ge3t_ttX_ttcc_node","")
    interf_ljets_ge6j_ge3t_ttX_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttX_ttcc_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_ttX_ttcc_node.maxxval = 0.68
    interf_ljets_ge6j_ge3t_ttX_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttX_ttcc_node)
    
    interf_ljets_ge6j_ge3t_ttX_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttX_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_ttX_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==4))")
    interf_ljets_ge6j_ge3t_ttX_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttX==4))","ljets_ge6j_ge3t_ttX_ttlf_node","")
    interf_ljets_ge6j_ge3t_ttX_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttX_ttlf_node.minxval = 0.2
    interf_ljets_ge6j_ge3t_ttX_ttlf_node.maxxval = 0.74
    interf_ljets_ge6j_ge3t_ttX_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttX_ttlf_node)
    


    # plots for ge6j_ge3t_ttXnonbb

    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttHbb",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttHbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==0))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==0))","ljets_ge6j_ge3t_ttXnonbb_ttHbb_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node.minxval = 0.17
    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node.maxxval = 0.81
    interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==1))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==1))","ljets_ge6j_ge3t_ttXnonbb_ttZbb_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node.minxval = 0.17
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node.maxxval = 0.89
    interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttXnonbb",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==2))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==2))","ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node.minxval = 0.17
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node.maxxval = 0.84
    interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttXnonbb_node)
    
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==3))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==3))","ljets_ge6j_ge3t_ttXnonbb_ttbb_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node.minxval = 0.17
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node.maxxval = 0.94
    interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttbb_node)
    
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==4))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==4))","ljets_ge6j_ge3t_ttXnonbb_ttcc_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node.minxval = 0.17
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node.maxxval = 0.58
    interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttcc_node)
    
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_ttXnonbb_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_ttXnonbb_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==5))")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t_ttXnonbb==5))","ljets_ge6j_ge3t_ttXnonbb_ttlf_node","")
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node.minxval = 0.17
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node.maxxval = 0.7
    interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttXnonbb_ttlf_node)
    


    # plots for 4j_ge3t_Xnonbb_merged

    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_merged_node_ttHbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_merged_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==0))")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==0))","ljets_4j_ge3t_Xnonbb_merged_ttHbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node.maxxval = 0.82
    interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_merged_ttHbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_merged_node_ttZbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_merged_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==1))")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==1))","ljets_4j_ge3t_Xnonbb_merged_ttZbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node.maxxval = 0.87
    interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_merged_ttZbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_merged_node_ttXnonbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==2))")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==2))","ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node.maxxval = 0.96
    interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_merged_ttXnonbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_merged_node_ttnonbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==3))")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==3))","ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node.maxxval = 0.84
    interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_merged_ttnonbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_merged_node_ttbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_merged_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==4))")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_merged==4))","ljets_4j_ge3t_Xnonbb_merged_ttbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node.maxxval = 0.91
    interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_merged_ttbb_node)
    


    # plots for 4j_ge3t_Xnonbb_ttbar

    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_ttbar_node_ttHbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==0))")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==0))","ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node.minxval = 0.25
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node.maxxval = 0.86
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_ttbar_ttHbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_ttbar_node_ttZbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==1))")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==1))","ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node.minxval = 0.25
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node.maxxval = 0.95
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_ttbar_ttZbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_ttbar_node_ttXnonbb",
                                            label          = "ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==2))")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==2))","ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node","")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node.minxval = 0.25
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node.maxxval = 0.97
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_ttbar_ttXnonbb_node)
    
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_Xnonbb_ttbar_node_ttbar",
                                            label          = "ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==3))")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_Xnonbb_ttbar==3))","ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node","")
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node.minxval = 0.25
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node.maxxval = 0.91
    interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_Xnonbb_ttbar_ttbar_node)
    


    # plots for 4j_ge3t_bb

    interf_ljets_4j_ge3t_bb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_node_ttHbb",
                                            label          = "ljets_4j_ge3t_bb_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==0))")
    interf_ljets_4j_ge3t_bb_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==0))","ljets_4j_ge3t_bb_ttHbb_node","")
    interf_ljets_4j_ge3t_bb_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttHbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_bb_ttHbb_node.maxxval = 0.89
    interf_ljets_4j_ge3t_bb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttHbb_node)
    
    interf_ljets_4j_ge3t_bb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_node_ttZbb",
                                            label          = "ljets_4j_ge3t_bb_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==1))")
    interf_ljets_4j_ge3t_bb_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==1))","ljets_4j_ge3t_bb_ttZbb_node","")
    interf_ljets_4j_ge3t_bb_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttZbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_bb_ttZbb_node.maxxval = 0.94
    interf_ljets_4j_ge3t_bb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttZbb_node)
    
    interf_ljets_4j_ge3t_bb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_node_ttbb",
                                            label          = "ljets_4j_ge3t_bb_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==2))")
    interf_ljets_4j_ge3t_bb_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==2))","ljets_4j_ge3t_bb_ttbb_node","")
    interf_ljets_4j_ge3t_bb_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_bb_ttbb_node.maxxval = 0.93
    interf_ljets_4j_ge3t_bb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttbb_node)
    
    interf_ljets_4j_ge3t_bb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_node_ttcc",
                                            label          = "ljets_4j_ge3t_bb_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==3))")
    interf_ljets_4j_ge3t_bb_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==3))","ljets_4j_ge3t_bb_ttcc_node","")
    interf_ljets_4j_ge3t_bb_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttcc_node.minxval = 0.2
    interf_ljets_4j_ge3t_bb_ttcc_node.maxxval = 0.74
    interf_ljets_4j_ge3t_bb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttcc_node)
    
    interf_ljets_4j_ge3t_bb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_node_ttlf",
                                            label          = "ljets_4j_ge3t_bb_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==4))")
    interf_ljets_4j_ge3t_bb_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb==4))","ljets_4j_ge3t_bb_ttlf_node","")
    interf_ljets_4j_ge3t_bb_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttlf_node.minxval = 0.2
    interf_ljets_4j_ge3t_bb_ttlf_node.maxxval = 0.74
    interf_ljets_4j_ge3t_bb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttlf_node)
    


    # plots for 4j_ge3t_bb_merged

    interf_ljets_4j_ge3t_bb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_merged_node_ttHbb",
                                            label          = "ljets_4j_ge3t_bb_merged_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==0))")
    interf_ljets_4j_ge3t_bb_merged_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==0))","ljets_4j_ge3t_bb_merged_ttHbb_node","")
    interf_ljets_4j_ge3t_bb_merged_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_merged_ttHbb_node.minxval = 0.25
    interf_ljets_4j_ge3t_bb_merged_ttHbb_node.maxxval = 0.86
    interf_ljets_4j_ge3t_bb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_merged_ttHbb_node)
    
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_merged_node_ttZbb",
                                            label          = "ljets_4j_ge3t_bb_merged_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==1))")
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==1))","ljets_4j_ge3t_bb_merged_ttZbb_node","")
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node.minxval = 0.25
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node.maxxval = 0.93
    interf_ljets_4j_ge3t_bb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_merged_ttZbb_node)
    
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_merged_node_ttnonbb",
                                            label          = "ljets_4j_ge3t_bb_merged_ttnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==2))")
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==2))","ljets_4j_ge3t_bb_merged_ttnonbb_node","")
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node.minxval = 0.25
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node.maxxval = 0.9
    interf_ljets_4j_ge3t_bb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_merged_ttnonbb_node)
    
    interf_ljets_4j_ge3t_bb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_merged_node_ttbb",
                                            label          = "ljets_4j_ge3t_bb_merged_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==3))")
    interf_ljets_4j_ge3t_bb_merged_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_merged==3))","ljets_4j_ge3t_bb_merged_ttbb_node","")
    interf_ljets_4j_ge3t_bb_merged_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_merged_ttbb_node.minxval = 0.25
    interf_ljets_4j_ge3t_bb_merged_ttbb_node.maxxval = 0.96
    interf_ljets_4j_ge3t_bb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_merged_ttbb_node)
    


    # plots for 4j_ge3t_bb_ttbar

    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_ttbar_node_ttHbb",
                                            label          = "ljets_4j_ge3t_bb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==0))")
    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==0))","ljets_4j_ge3t_bb_ttbar_ttHbb_node","")
    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node.minxval = 0.33
    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node.maxxval = 0.94
    interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttbar_ttHbb_node)
    
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_ttbar_node_ttZbb",
                                            label          = "ljets_4j_ge3t_bb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==1))")
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==1))","ljets_4j_ge3t_bb_ttbar_ttZbb_node","")
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node.minxval = 0.33
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node.maxxval = 0.98
    interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttbar_ttZbb_node)
    
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_bb_ttbar_node_ttbar",
                                            label          = "ljets_4j_ge3t_bb_ttbar_ttbar_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==2))")
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_bb_ttbar==2))","ljets_4j_ge3t_bb_ttbar_ttbar_node","")
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node.minxval = 0.33
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node.maxxval = 0.99
    interf_ljets_4j_ge3t_bb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_bb_ttbar_ttbar_node)
    


    # plots for 4j_ge3t_comb

    interf_ljets_4j_ge3t_comb_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_comb_node_ttH",
                                            label          = "ljets_4j_ge3t_comb_ttH_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==0))")
    interf_ljets_4j_ge3t_comb_ttH_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==0))","ljets_4j_ge3t_comb_ttH_node","")
    interf_ljets_4j_ge3t_comb_ttH_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_comb_ttH_node.minxval = 0.2
    interf_ljets_4j_ge3t_comb_ttH_node.maxxval = 0.77
    interf_ljets_4j_ge3t_comb_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_comb_ttH_node)
    
    interf_ljets_4j_ge3t_comb_ttZ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_comb_node_ttZ",
                                            label          = "ljets_4j_ge3t_comb_ttZ_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==1))")
    interf_ljets_4j_ge3t_comb_ttZ_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==1))","ljets_4j_ge3t_comb_ttZ_node","")
    interf_ljets_4j_ge3t_comb_ttZ_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_comb_ttZ_node.minxval = 0.2
    interf_ljets_4j_ge3t_comb_ttZ_node.maxxval = 0.92
    interf_ljets_4j_ge3t_comb_ttZ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_comb_ttZ_node)
    
    interf_ljets_4j_ge3t_comb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_comb_node_ttbb",
                                            label          = "ljets_4j_ge3t_comb_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==2))")
    interf_ljets_4j_ge3t_comb_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==2))","ljets_4j_ge3t_comb_ttbb_node","")
    interf_ljets_4j_ge3t_comb_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_comb_ttbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_comb_ttbb_node.maxxval = 0.87
    interf_ljets_4j_ge3t_comb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_comb_ttbb_node)
    
    interf_ljets_4j_ge3t_comb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_comb_node_ttcc",
                                            label          = "ljets_4j_ge3t_comb_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==3))")
    interf_ljets_4j_ge3t_comb_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==3))","ljets_4j_ge3t_comb_ttcc_node","")
    interf_ljets_4j_ge3t_comb_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_comb_ttcc_node.minxval = 0.2
    interf_ljets_4j_ge3t_comb_ttcc_node.maxxval = 0.6
    interf_ljets_4j_ge3t_comb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_comb_ttcc_node)
    
    interf_ljets_4j_ge3t_comb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_comb_node_ttlf",
                                            label          = "ljets_4j_ge3t_comb_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==4))")
    interf_ljets_4j_ge3t_comb_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_comb==4))","ljets_4j_ge3t_comb_ttlf_node","")
    interf_ljets_4j_ge3t_comb_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_comb_ttlf_node.minxval = 0.2
    interf_ljets_4j_ge3t_comb_ttlf_node.maxxval = 0.69
    interf_ljets_4j_ge3t_comb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_comb_ttlf_node)
    


    # plots for 4j_ge3t_split

    interf_ljets_4j_ge3t_split_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttHbb",
                                            label          = "ljets_4j_ge3t_split_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==0))")
    interf_ljets_4j_ge3t_split_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==0))","ljets_4j_ge3t_split_ttHbb_node","")
    interf_ljets_4j_ge3t_split_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttHbb_node.minxval = 0.14
    interf_ljets_4j_ge3t_split_ttHbb_node.maxxval = 0.75
    interf_ljets_4j_ge3t_split_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttHbb_node)
    
    interf_ljets_4j_ge3t_split_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttHnonbb",
                                            label          = "ljets_4j_ge3t_split_ttHnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==1))")
    interf_ljets_4j_ge3t_split_ttHnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==1))","ljets_4j_ge3t_split_ttHnonbb_node","")
    interf_ljets_4j_ge3t_split_ttHnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttHnonbb_node.minxval = 0.14
    interf_ljets_4j_ge3t_split_ttHnonbb_node.maxxval = 0.53
    interf_ljets_4j_ge3t_split_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttHnonbb_node)
    
    interf_ljets_4j_ge3t_split_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttZbb",
                                            label          = "ljets_4j_ge3t_split_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==2))")
    interf_ljets_4j_ge3t_split_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==2))","ljets_4j_ge3t_split_ttZbb_node","")
    interf_ljets_4j_ge3t_split_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttZbb_node.minxval = 0.14
    interf_ljets_4j_ge3t_split_ttZbb_node.maxxval = 0.85
    interf_ljets_4j_ge3t_split_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttZbb_node)
    
    interf_ljets_4j_ge3t_split_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttZnonbb",
                                            label          = "ljets_4j_ge3t_split_ttZnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==3))")
    interf_ljets_4j_ge3t_split_ttZnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==3))","ljets_4j_ge3t_split_ttZnonbb_node","")
    interf_ljets_4j_ge3t_split_ttZnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttZnonbb_node.minxval = 0.14
    interf_ljets_4j_ge3t_split_ttZnonbb_node.maxxval = 0.82
    interf_ljets_4j_ge3t_split_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttZnonbb_node)
    
    interf_ljets_4j_ge3t_split_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttbb",
                                            label          = "ljets_4j_ge3t_split_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==4))")
    interf_ljets_4j_ge3t_split_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==4))","ljets_4j_ge3t_split_ttbb_node","")
    interf_ljets_4j_ge3t_split_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttbb_node.minxval = 0.14
    interf_ljets_4j_ge3t_split_ttbb_node.maxxval = 0.85
    interf_ljets_4j_ge3t_split_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttbb_node)
    
    interf_ljets_4j_ge3t_split_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttcc",
                                            label          = "ljets_4j_ge3t_split_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==5))")
    interf_ljets_4j_ge3t_split_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==5))","ljets_4j_ge3t_split_ttcc_node","")
    interf_ljets_4j_ge3t_split_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttcc_node.minxval = 0.14
    interf_ljets_4j_ge3t_split_ttcc_node.maxxval = 0.49
    interf_ljets_4j_ge3t_split_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttcc_node)
    
    interf_ljets_4j_ge3t_split_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_split_node_ttlf",
                                            label          = "ljets_4j_ge3t_split_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==6))")
    interf_ljets_4j_ge3t_split_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_split==6))","ljets_4j_ge3t_split_ttlf_node","")
    interf_ljets_4j_ge3t_split_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_split_ttlf_node.minxval = 0.14
    interf_ljets_4j_ge3t_split_ttlf_node.maxxval = 0.65
    interf_ljets_4j_ge3t_split_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_split_ttlf_node)
    


    # plots for 4j_ge3t_ttX

    interf_ljets_4j_ge3t_ttX_ttXbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttX_node_ttXbb",
                                            label          = "ljets_4j_ge3t_ttX_ttXbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==0))")
    interf_ljets_4j_ge3t_ttX_ttXbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==0))","ljets_4j_ge3t_ttX_ttXbb_node","")
    interf_ljets_4j_ge3t_ttX_ttXbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttX_ttXbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_ttX_ttXbb_node.maxxval = 0.95
    interf_ljets_4j_ge3t_ttX_ttXbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttX_ttXbb_node)
    
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttX_node_ttXnonbb",
                                            label          = "ljets_4j_ge3t_ttX_ttXnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==1))")
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==1))","ljets_4j_ge3t_ttX_ttXnonbb_node","")
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node.maxxval = 0.93
    interf_ljets_4j_ge3t_ttX_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttX_ttXnonbb_node)
    
    interf_ljets_4j_ge3t_ttX_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttX_node_ttbb",
                                            label          = "ljets_4j_ge3t_ttX_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==2))")
    interf_ljets_4j_ge3t_ttX_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==2))","ljets_4j_ge3t_ttX_ttbb_node","")
    interf_ljets_4j_ge3t_ttX_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttX_ttbb_node.minxval = 0.2
    interf_ljets_4j_ge3t_ttX_ttbb_node.maxxval = 0.9
    interf_ljets_4j_ge3t_ttX_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttX_ttbb_node)
    
    interf_ljets_4j_ge3t_ttX_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttX_node_ttcc",
                                            label          = "ljets_4j_ge3t_ttX_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==3))")
    interf_ljets_4j_ge3t_ttX_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==3))","ljets_4j_ge3t_ttX_ttcc_node","")
    interf_ljets_4j_ge3t_ttX_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttX_ttcc_node.minxval = 0.2
    interf_ljets_4j_ge3t_ttX_ttcc_node.maxxval = 0.59
    interf_ljets_4j_ge3t_ttX_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttX_ttcc_node)
    
    interf_ljets_4j_ge3t_ttX_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttX_node_ttlf",
                                            label          = "ljets_4j_ge3t_ttX_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==4))")
    interf_ljets_4j_ge3t_ttX_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttX==4))","ljets_4j_ge3t_ttX_ttlf_node","")
    interf_ljets_4j_ge3t_ttX_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttX_ttlf_node.minxval = 0.2
    interf_ljets_4j_ge3t_ttX_ttlf_node.maxxval = 0.73
    interf_ljets_4j_ge3t_ttX_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttX_ttlf_node)
    


    # plots for 4j_ge3t_ttXnonbb

    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttHbb",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttHbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==0))")
    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==0))","ljets_4j_ge3t_ttXnonbb_ttHbb_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node.minxval = 0.17
    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node.maxxval = 0.87
    interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttHbb_node)
    
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttZbb",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==1))")
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==1))","ljets_4j_ge3t_ttXnonbb_ttZbb_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node.minxval = 0.17
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node.maxxval = 0.94
    interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttZbb_node)
    
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttXnonbb",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttXnonbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==2))")
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==2))","ljets_4j_ge3t_ttXnonbb_ttXnonbb_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node.minxval = 0.17
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node.maxxval = 0.95
    interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttXnonbb_node)
    
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttbb",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==3))")
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==3))","ljets_4j_ge3t_ttXnonbb_ttbb_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node.minxval = 0.17
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node.maxxval = 0.94
    interf_ljets_4j_ge3t_ttXnonbb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttbb_node)
    
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttcc",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==4))")
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==4))","ljets_4j_ge3t_ttXnonbb_ttcc_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node.minxval = 0.17
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node.maxxval = 0.54
    interf_ljets_4j_ge3t_ttXnonbb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttcc_node)
    
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_ttXnonbb_node_ttlf",
                                            label          = "ljets_4j_ge3t_ttXnonbb_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==5))")
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t_ttXnonbb==5))","ljets_4j_ge3t_ttXnonbb_ttlf_node","")
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node.minxval = 0.17
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node.maxxval = 0.66
    interf_ljets_4j_ge3t_ttXnonbb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttXnonbb_ttlf_node)
    


    # plots for 5j_ge3t_Xnonbb_merged

    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_merged_node_ttHbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_merged_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==0))")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==0))","ljets_5j_ge3t_Xnonbb_merged_ttHbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node.maxxval = 0.82
    interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_merged_ttHbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_merged_node_ttZbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_merged_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==1))")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==1))","ljets_5j_ge3t_Xnonbb_merged_ttZbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node.maxxval = 0.89
    interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_merged_ttZbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_merged_node_ttXnonbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==2))")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==2))","ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node.maxxval = 0.94
    interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_merged_ttXnonbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_merged_node_ttnonbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==3))")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==3))","ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node.maxxval = 0.86
    interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_merged_ttnonbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_merged_node_ttbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_merged_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==4))")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_merged==4))","ljets_5j_ge3t_Xnonbb_merged_ttbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node.maxxval = 0.87
    interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_merged_ttbb_node)
    


    # plots for 5j_ge3t_Xnonbb_ttbar

    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_ttbar_node_ttHbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==0))")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==0))","ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node.minxval = 0.25
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node.maxxval = 0.84
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_ttbar_ttHbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_ttbar_node_ttZbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==1))")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==1))","ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node.minxval = 0.25
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node.maxxval = 0.93
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_ttbar_ttZbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_ttbar_node_ttXnonbb",
                                            label          = "ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==2))")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==2))","ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node","")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node.minxval = 0.25
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node.maxxval = 0.94
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_ttbar_ttXnonbb_node)
    
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_Xnonbb_ttbar_node_ttbar",
                                            label          = "ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==3))")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_Xnonbb_ttbar==3))","ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node","")
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node.minxval = 0.25
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node.maxxval = 0.87
    interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_Xnonbb_ttbar_ttbar_node)
    


    # plots for 5j_ge3t_bb

    interf_ljets_5j_ge3t_bb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_node_ttHbb",
                                            label          = "ljets_5j_ge3t_bb_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==0))")
    interf_ljets_5j_ge3t_bb_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==0))","ljets_5j_ge3t_bb_ttHbb_node","")
    interf_ljets_5j_ge3t_bb_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttHbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_bb_ttHbb_node.maxxval = 0.86
    interf_ljets_5j_ge3t_bb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttHbb_node)
    
    interf_ljets_5j_ge3t_bb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_node_ttZbb",
                                            label          = "ljets_5j_ge3t_bb_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==1))")
    interf_ljets_5j_ge3t_bb_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==1))","ljets_5j_ge3t_bb_ttZbb_node","")
    interf_ljets_5j_ge3t_bb_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttZbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_bb_ttZbb_node.maxxval = 0.9
    interf_ljets_5j_ge3t_bb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttZbb_node)
    
    interf_ljets_5j_ge3t_bb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_node_ttbb",
                                            label          = "ljets_5j_ge3t_bb_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==2))")
    interf_ljets_5j_ge3t_bb_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==2))","ljets_5j_ge3t_bb_ttbb_node","")
    interf_ljets_5j_ge3t_bb_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_bb_ttbb_node.maxxval = 0.93
    interf_ljets_5j_ge3t_bb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttbb_node)
    
    interf_ljets_5j_ge3t_bb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_node_ttcc",
                                            label          = "ljets_5j_ge3t_bb_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==3))")
    interf_ljets_5j_ge3t_bb_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==3))","ljets_5j_ge3t_bb_ttcc_node","")
    interf_ljets_5j_ge3t_bb_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttcc_node.minxval = 0.2
    interf_ljets_5j_ge3t_bb_ttcc_node.maxxval = 0.69
    interf_ljets_5j_ge3t_bb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttcc_node)
    
    interf_ljets_5j_ge3t_bb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_node_ttlf",
                                            label          = "ljets_5j_ge3t_bb_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==4))")
    interf_ljets_5j_ge3t_bb_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb==4))","ljets_5j_ge3t_bb_ttlf_node","")
    interf_ljets_5j_ge3t_bb_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttlf_node.minxval = 0.2
    interf_ljets_5j_ge3t_bb_ttlf_node.maxxval = 0.73
    interf_ljets_5j_ge3t_bb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttlf_node)
    


    # plots for 5j_ge3t_bb_merged

    interf_ljets_5j_ge3t_bb_merged_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_merged_node_ttHbb",
                                            label          = "ljets_5j_ge3t_bb_merged_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==0))")
    interf_ljets_5j_ge3t_bb_merged_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==0))","ljets_5j_ge3t_bb_merged_ttHbb_node","")
    interf_ljets_5j_ge3t_bb_merged_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_merged_ttHbb_node.minxval = 0.25
    interf_ljets_5j_ge3t_bb_merged_ttHbb_node.maxxval = 0.87
    interf_ljets_5j_ge3t_bb_merged_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_merged_ttHbb_node)
    
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_merged_node_ttZbb",
                                            label          = "ljets_5j_ge3t_bb_merged_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==1))")
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==1))","ljets_5j_ge3t_bb_merged_ttZbb_node","")
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node.minxval = 0.25
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node.maxxval = 0.92
    interf_ljets_5j_ge3t_bb_merged_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_merged_ttZbb_node)
    
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_merged_node_ttnonbb",
                                            label          = "ljets_5j_ge3t_bb_merged_ttnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==2))")
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==2))","ljets_5j_ge3t_bb_merged_ttnonbb_node","")
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node.minxval = 0.25
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node.maxxval = 0.93
    interf_ljets_5j_ge3t_bb_merged_ttnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_merged_ttnonbb_node)
    
    interf_ljets_5j_ge3t_bb_merged_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_merged_node_ttbb",
                                            label          = "ljets_5j_ge3t_bb_merged_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==3))")
    interf_ljets_5j_ge3t_bb_merged_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_merged==3))","ljets_5j_ge3t_bb_merged_ttbb_node","")
    interf_ljets_5j_ge3t_bb_merged_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_merged_ttbb_node.minxval = 0.25
    interf_ljets_5j_ge3t_bb_merged_ttbb_node.maxxval = 0.97
    interf_ljets_5j_ge3t_bb_merged_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_merged_ttbb_node)
    


    # plots for 5j_ge3t_bb_ttbar

    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_ttbar_node_ttHbb",
                                            label          = "ljets_5j_ge3t_bb_ttbar_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==0))")
    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==0))","ljets_5j_ge3t_bb_ttbar_ttHbb_node","")
    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node.minxval = 0.33
    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node.maxxval = 0.91
    interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttbar_ttHbb_node)
    
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_ttbar_node_ttZbb",
                                            label          = "ljets_5j_ge3t_bb_ttbar_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==1))")
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==1))","ljets_5j_ge3t_bb_ttbar_ttZbb_node","")
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node.minxval = 0.33
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node.maxxval = 0.96
    interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttbar_ttZbb_node)
    
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_bb_ttbar_node_ttbar",
                                            label          = "ljets_5j_ge3t_bb_ttbar_ttbar_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==2))")
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_bb_ttbar==2))","ljets_5j_ge3t_bb_ttbar_ttbar_node","")
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node.minxval = 0.33
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node.maxxval = 0.98
    interf_ljets_5j_ge3t_bb_ttbar_ttbar_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_bb_ttbar_ttbar_node)
    


    # plots for 5j_ge3t_comb

    interf_ljets_5j_ge3t_comb_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_comb_node_ttH",
                                            label          = "ljets_5j_ge3t_comb_ttH_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==0))")
    interf_ljets_5j_ge3t_comb_ttH_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==0))","ljets_5j_ge3t_comb_ttH_node","")
    interf_ljets_5j_ge3t_comb_ttH_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_comb_ttH_node.minxval = 0.2
    interf_ljets_5j_ge3t_comb_ttH_node.maxxval = 0.78
    interf_ljets_5j_ge3t_comb_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_comb_ttH_node)
    
    interf_ljets_5j_ge3t_comb_ttZ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_comb_node_ttZ",
                                            label          = "ljets_5j_ge3t_comb_ttZ_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==1))")
    interf_ljets_5j_ge3t_comb_ttZ_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==1))","ljets_5j_ge3t_comb_ttZ_node","")
    interf_ljets_5j_ge3t_comb_ttZ_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_comb_ttZ_node.minxval = 0.2
    interf_ljets_5j_ge3t_comb_ttZ_node.maxxval = 0.88
    interf_ljets_5j_ge3t_comb_ttZ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_comb_ttZ_node)
    
    interf_ljets_5j_ge3t_comb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_comb_node_ttbb",
                                            label          = "ljets_5j_ge3t_comb_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==2))")
    interf_ljets_5j_ge3t_comb_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==2))","ljets_5j_ge3t_comb_ttbb_node","")
    interf_ljets_5j_ge3t_comb_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_comb_ttbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_comb_ttbb_node.maxxval = 0.91
    interf_ljets_5j_ge3t_comb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_comb_ttbb_node)
    
    interf_ljets_5j_ge3t_comb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_comb_node_ttcc",
                                            label          = "ljets_5j_ge3t_comb_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==3))")
    interf_ljets_5j_ge3t_comb_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==3))","ljets_5j_ge3t_comb_ttcc_node","")
    interf_ljets_5j_ge3t_comb_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_comb_ttcc_node.minxval = 0.2
    interf_ljets_5j_ge3t_comb_ttcc_node.maxxval = 0.56
    interf_ljets_5j_ge3t_comb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_comb_ttcc_node)
    
    interf_ljets_5j_ge3t_comb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_comb_node_ttlf",
                                            label          = "ljets_5j_ge3t_comb_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==4))")
    interf_ljets_5j_ge3t_comb_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_comb==4))","ljets_5j_ge3t_comb_ttlf_node","")
    interf_ljets_5j_ge3t_comb_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_comb_ttlf_node.minxval = 0.2
    interf_ljets_5j_ge3t_comb_ttlf_node.maxxval = 0.69
    interf_ljets_5j_ge3t_comb_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_comb_ttlf_node)
    


    # plots for 5j_ge3t_split

    interf_ljets_5j_ge3t_split_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttHbb",
                                            label          = "ljets_5j_ge3t_split_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==0))")
    interf_ljets_5j_ge3t_split_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==0))","ljets_5j_ge3t_split_ttHbb_node","")
    interf_ljets_5j_ge3t_split_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttHbb_node.minxval = 0.14
    interf_ljets_5j_ge3t_split_ttHbb_node.maxxval = 0.73
    interf_ljets_5j_ge3t_split_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttHbb_node)
    
    interf_ljets_5j_ge3t_split_ttHnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttHnonbb",
                                            label          = "ljets_5j_ge3t_split_ttHnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==1))")
    interf_ljets_5j_ge3t_split_ttHnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==1))","ljets_5j_ge3t_split_ttHnonbb_node","")
    interf_ljets_5j_ge3t_split_ttHnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttHnonbb_node.minxval = 0.14
    interf_ljets_5j_ge3t_split_ttHnonbb_node.maxxval = 0.47
    interf_ljets_5j_ge3t_split_ttHnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttHnonbb_node)
    
    interf_ljets_5j_ge3t_split_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttZbb",
                                            label          = "ljets_5j_ge3t_split_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==2))")
    interf_ljets_5j_ge3t_split_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==2))","ljets_5j_ge3t_split_ttZbb_node","")
    interf_ljets_5j_ge3t_split_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttZbb_node.minxval = 0.14
    interf_ljets_5j_ge3t_split_ttZbb_node.maxxval = 0.91
    interf_ljets_5j_ge3t_split_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttZbb_node)
    
    interf_ljets_5j_ge3t_split_ttZnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttZnonbb",
                                            label          = "ljets_5j_ge3t_split_ttZnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==3))")
    interf_ljets_5j_ge3t_split_ttZnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==3))","ljets_5j_ge3t_split_ttZnonbb_node","")
    interf_ljets_5j_ge3t_split_ttZnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttZnonbb_node.minxval = 0.14
    interf_ljets_5j_ge3t_split_ttZnonbb_node.maxxval = 0.86
    interf_ljets_5j_ge3t_split_ttZnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttZnonbb_node)
    
    interf_ljets_5j_ge3t_split_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttbb",
                                            label          = "ljets_5j_ge3t_split_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==4))")
    interf_ljets_5j_ge3t_split_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==4))","ljets_5j_ge3t_split_ttbb_node","")
    interf_ljets_5j_ge3t_split_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttbb_node.minxval = 0.14
    interf_ljets_5j_ge3t_split_ttbb_node.maxxval = 0.76
    interf_ljets_5j_ge3t_split_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttbb_node)
    
    interf_ljets_5j_ge3t_split_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttcc",
                                            label          = "ljets_5j_ge3t_split_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==5))")
    interf_ljets_5j_ge3t_split_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==5))","ljets_5j_ge3t_split_ttcc_node","")
    interf_ljets_5j_ge3t_split_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttcc_node.minxval = 0.14
    interf_ljets_5j_ge3t_split_ttcc_node.maxxval = 0.48
    interf_ljets_5j_ge3t_split_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttcc_node)
    
    interf_ljets_5j_ge3t_split_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_split_node_ttlf",
                                            label          = "ljets_5j_ge3t_split_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==6))")
    interf_ljets_5j_ge3t_split_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_split==6))","ljets_5j_ge3t_split_ttlf_node","")
    interf_ljets_5j_ge3t_split_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_split_ttlf_node.minxval = 0.14
    interf_ljets_5j_ge3t_split_ttlf_node.maxxval = 0.69
    interf_ljets_5j_ge3t_split_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_split_ttlf_node)
    


    # plots for 5j_ge3t_ttX

    interf_ljets_5j_ge3t_ttX_ttXbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttX_node_ttXbb",
                                            label          = "ljets_5j_ge3t_ttX_ttXbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==0))")
    interf_ljets_5j_ge3t_ttX_ttXbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==0))","ljets_5j_ge3t_ttX_ttXbb_node","")
    interf_ljets_5j_ge3t_ttX_ttXbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttX_ttXbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_ttX_ttXbb_node.maxxval = 0.94
    interf_ljets_5j_ge3t_ttX_ttXbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttX_ttXbb_node)
    
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttX_node_ttXnonbb",
                                            label          = "ljets_5j_ge3t_ttX_ttXnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==1))")
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==1))","ljets_5j_ge3t_ttX_ttXnonbb_node","")
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node.maxxval = 0.91
    interf_ljets_5j_ge3t_ttX_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttX_ttXnonbb_node)
    
    interf_ljets_5j_ge3t_ttX_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttX_node_ttbb",
                                            label          = "ljets_5j_ge3t_ttX_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==2))")
    interf_ljets_5j_ge3t_ttX_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==2))","ljets_5j_ge3t_ttX_ttbb_node","")
    interf_ljets_5j_ge3t_ttX_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttX_ttbb_node.minxval = 0.2
    interf_ljets_5j_ge3t_ttX_ttbb_node.maxxval = 0.9
    interf_ljets_5j_ge3t_ttX_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttX_ttbb_node)
    
    interf_ljets_5j_ge3t_ttX_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttX_node_ttcc",
                                            label          = "ljets_5j_ge3t_ttX_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==3))")
    interf_ljets_5j_ge3t_ttX_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==3))","ljets_5j_ge3t_ttX_ttcc_node","")
    interf_ljets_5j_ge3t_ttX_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttX_ttcc_node.minxval = 0.2
    interf_ljets_5j_ge3t_ttX_ttcc_node.maxxval = 0.58
    interf_ljets_5j_ge3t_ttX_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttX_ttcc_node)
    
    interf_ljets_5j_ge3t_ttX_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttX_node_ttlf",
                                            label          = "ljets_5j_ge3t_ttX_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==4))")
    interf_ljets_5j_ge3t_ttX_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttX==4))","ljets_5j_ge3t_ttX_ttlf_node","")
    interf_ljets_5j_ge3t_ttX_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttX_ttlf_node.minxval = 0.2
    interf_ljets_5j_ge3t_ttX_ttlf_node.maxxval = 0.72
    interf_ljets_5j_ge3t_ttX_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttX_ttlf_node)
    


    # plots for 5j_ge3t_ttXnonbb

    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttHbb",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttHbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==0))")
    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==0))","ljets_5j_ge3t_ttXnonbb_ttHbb_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node.minxval = 0.17
    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node.maxxval = 0.8
    interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttHbb_node)
    
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttZbb",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==1))")
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==1))","ljets_5j_ge3t_ttXnonbb_ttZbb_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node.minxval = 0.17
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node.maxxval = 0.9
    interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttZbb_node)
    
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttXnonbb",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttXnonbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==2))")
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==2))","ljets_5j_ge3t_ttXnonbb_ttXnonbb_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node.minxval = 0.17
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node.maxxval = 0.84
    interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttXnonbb_node)
    
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttbb",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==3))")
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==3))","ljets_5j_ge3t_ttXnonbb_ttbb_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node.minxval = 0.17
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node.maxxval = 0.84
    interf_ljets_5j_ge3t_ttXnonbb_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttbb_node)
    
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttcc",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==4))")
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==4))","ljets_5j_ge3t_ttXnonbb_ttcc_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node.minxval = 0.17
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node.maxxval = 0.57
    interf_ljets_5j_ge3t_ttXnonbb_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttXnonbb_ttcc_node)
    
    interf_ljets_5j_ge3t_ttXnonbb_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_ttXnonbb_node_ttlf",
                                            label          = "ljets_5j_ge3t_ttXnonbb_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==5))")
    interf_ljets_5j_ge3t_ttXnonbb_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t_ttXnonbb==5))","ljets_5j_ge3t_ttXnonbb_ttlf_node","")
    interf_ljets_5j_ge3t_ttXnonbb_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttXnonbb_ttlf_node.minxval = 0.17
    interf_ljets_5j_ge3t_ttXnonbb_ttlf_node.maxxval = 0.69
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
    