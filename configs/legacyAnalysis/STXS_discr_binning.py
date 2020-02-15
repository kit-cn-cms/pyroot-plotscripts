
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

    ndefaultbins = 50
    interfaces = []
    ############
    ### HTXS ###
    ############
    TTHpredicted43 = "(DNNPredictedClass_ge4j_3t_classification==0)"
    TTHpredicted44 = "(DNNPredictedClass_ge4j_ge4t_classification==0)"

    # THpredicted43 = "(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6)"
    # THpredicted44 = "(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6)"

    # THorTTH43 = "(" + TTHpredicted43 + " && " + THpredicted43 +")"
    # THorTTH44 = "(" + TTHpredicted44 + " && " + THpredicted44 +")"
    ############################
    # plots for ge4j_3t_HTXS #
    ############################

    # only ttH node 
    interf_ljets_ge4j_3t_STXS_ttH_Bin_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_0",
                                            label          = "ljets_ge4j_3t_STXS_ttH_Bin_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==0)&& " + TTHpredicted43 +")")
    interf_ljets_ge4j_3t_STXS_ttH_Bin_0_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==0)&& " + TTHpredicted43 +")","ljets_ge4j_3t_STXS_ttH_Bin_0_node","")
    interf_ljets_ge4j_3t_STXS_ttH_Bin_0_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_Bin_0_node.bin_edges = [ 
				0.2,
				0.2487,
				0.2973,
				0.346,
				0.3947,
				0.4433,
				0.492,
				0.5407,
				0.5893,
				0.638,
				0.6867,
				0.7353,
				0.784,
				0.8327,
				0.93
				]
    interf_ljets_ge4j_3t_STXS_ttH_Bin_0_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_Bin_0_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_Bin_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_1",
                                            label          = "ljets_ge4j_3t_STXS_ttH_Bin_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==1)&& " + TTHpredicted43 +")")
    interf_ljets_ge4j_3t_STXS_ttH_Bin_1_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==1)&& " + TTHpredicted43 +")","ljets_ge4j_3t_STXS_ttH_Bin_1_node","")
    interf_ljets_ge4j_3t_STXS_ttH_Bin_1_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_Bin_1_node.bin_edges = [ 
				0.2413,
				0.262,
				0.2827,
				0.3033,
				0.324,
				0.3447,
				0.3653,
				0.386,
				0.4067,
				0.4273,
				0.448,
				0.51
				]
    interf_ljets_ge4j_3t_STXS_ttH_Bin_1_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_Bin_1_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_Bin_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_2",
                                            label          = "ljets_ge4j_3t_STXS_ttH_Bin_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==2)&& " + TTHpredicted43 +")")
    interf_ljets_ge4j_3t_STXS_ttH_Bin_2_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==2)&& " + TTHpredicted43 +")","ljets_ge4j_3t_STXS_ttH_Bin_2_node","")
    interf_ljets_ge4j_3t_STXS_ttH_Bin_2_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_Bin_2_node.bin_edges = [ 
				0.2,
				0.2493,
				0.2987,
				0.348,
				0.3973,
				0.4467,
				0.496,
				0.5453,
				]
    interf_ljets_ge4j_3t_STXS_ttH_Bin_2_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_Bin_2_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_Bin_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_3",
                                            label          = "ljets_ge4j_3t_STXS_ttH_Bin_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==3))&& " + TTHpredicted43 +")")
    interf_ljets_ge4j_3t_STXS_ttH_Bin_3_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==3)&& " + TTHpredicted43 +")","ljets_ge4j_3t_STXS_ttH_Bin_3_node","")
    interf_ljets_ge4j_3t_STXS_ttH_Bin_3_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_Bin_3_node.bin_edges = [ 
				0.2,
				0.24,
				0.28,
				0.32,
				0.36,
				0.4,
				0.44,
				0.48,
				0.52,
				0.56,
				0.6,
				0.64,
				0.68,
				0.8
				]
    interf_ljets_ge4j_3t_STXS_ttH_Bin_3_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_Bin_3_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_Bin_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_4",
                                            label          = "ljets_ge4j_3t_STXS_ttH_Bin_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==4)&& " + TTHpredicted43 +")")
    interf_ljets_ge4j_3t_STXS_ttH_Bin_4_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==4)&& " + TTHpredicted43 +")","ljets_ge4j_3t_STXS_ttH_Bin_4_node","")
    interf_ljets_ge4j_3t_STXS_ttH_Bin_4_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_Bin_4_node.bin_edges = [ 
				0.2,
				0.2533,
				0.3067,
				0.36,
				0.4133,
				0.4667,
				0.52,
				0.5733,
				0.6267,
				0.68,
				0.7333,
				0.7867,
				0.84,
				0.8933,
				0.9467,
				1.0
				]
    interf_ljets_ge4j_3t_STXS_ttH_Bin_4_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_Bin_4_node)

    # ttH and tHq and tHW nodes 
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_0",
                                            label          = "ljets_ge4j_3t_STXS_ttH_tH_bin_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==0)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_0_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==0)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_STXS_ttH_tH_bin_0_node","")
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_0_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_0_node.minxval = 0.
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_0_node.maxxval = 1.0
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_0_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_0_node.bin_edges = [ 
				0.2,
				0.2487,
				0.2973,
				0.346,
				0.3947,
				0.4433,
				0.492,
				0.5407,
				0.5893,
				0.638,
				0.6867,
				0.7353,
				0.784,
				0.93
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_tH_bin_0_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_1",
                                            label          = "ljets_ge4j_3t_STXS_ttH_tH_bin_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==1)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_1_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==1)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_STXS_ttH_tH_bin_1_node","")
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_1_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_1_node.minxval = 0
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_1_node.maxxval = 1.0
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_1_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_1_node.bin_edges = [ 
				0.2207,
				0.2413,
				0.262,
				0.2827,
				0.3033,
				0.324,
				0.3447,
				0.3653,
				0.386,
				0.4067,
				0.4273,
				0.51
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_tH_bin_1_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_2",
                                            label          = "ljets_ge4j_3t_STXS_ttH_tH_bin_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==2)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_2_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==2)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_STXS_ttH_tH_bin_2_node","")
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_2_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_2_node.minxval = 0
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_2_node.maxxval = 1.0
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_2_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_2_node.bin_edges = [ 
				0.2,
				0.2493,
				0.2987,
				0.348,
				0.3973,
				0.4467,
				0.496,
				0.94
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_tH_bin_2_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_3",
                                            label          = "ljets_ge4j_3t_STXS_ttH_tH_bin_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==3)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_3_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==3)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_STXS_ttH_tH_bin_3_node","")
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_3_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_3_node.minxval = 0
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_3_node.maxxval = 1.0
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_3_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_3_node.bin_edges = [ 
				0.2,
				0.24,
				0.28,
				0.32,
				0.36,
				0.4,
				0.44,
				0.48,
				0.52,
				0.56,
				0.6,
				0.64,
				0.68,
				0.8
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_tH_bin_3_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_4",
                                            label          = "ljets_ge4j_3t_STXS_ttH_tH_bin_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==4)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_4_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==4)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_STXS_ttH_tH_bin_4_node","")
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_4_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_4_node.minxval = 0
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_4_node.maxxval = 1.0
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_4_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_tH_bin_4_node.bin_edges = [ 
				0.2,
				0.2533,
				0.3067,
				0.36,
				0.4133,
				0.4667,
				0.52,
				0.5733,
				0.6267,
				0.68,
				0.7333,
				0.7867,
				0.84,
				0.8933,
				0.9467,
				1.0
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_tH_bin_4_node)

    ############################
    # plots for ge4j_3t_HTXS MULTIPLIED#
    ############################

    # only ttH node 
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_0_node = vhi.variableHistoInterface(variable_name  = "((DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_0) * (DNNOutput_ge4j_3t_classification_node_ttH))",
                                            label          = "ljets_ge4j_3t_STXS_ttH_weighted_bin_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==0)&&(DNNPredictedClass_ge4j_3t_classification==0))&& " + TTHpredicted43 +")")
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_0_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==0)&& " + TTHpredicted43 +")","ljets_ge4j_3t_STXS_ttH_weighted_bin_0_node","")
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_0_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_0_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_0_node.bin_edges = [ 
				0.2,
				0.21,
				0.22,
				0.23,
				0.24,
                0.25,
                0.26,
                0.27,
                0.28,
                0.29,
                0.3,
                0.4,
				0.5
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_0_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_1_node = vhi.variableHistoInterface(variable_name  = "((DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_1) * (DNNOutput_ge4j_3t_classification_node_ttH))",
                                            label          = "ljets_ge4j_3t_STXS_ttH_weighted_bin_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==1)&&(DNNPredictedClass_ge4j_3t_classification==0))&& " + TTHpredicted43 +")")
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_1_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==1)&& " + TTHpredicted43 +")","ljets_ge4j_3t_STXS_ttH_weighted_bin_1_node","")
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_1_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_1_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_1_node.bin_edges = [ 
				0.2,
                0.205,
				0.21,
				0.22,
				0.23,
				0.24,
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_1_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_2_node = vhi.variableHistoInterface(variable_name  = "((DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_2) * (DNNOutput_ge4j_3t_classification_node_ttH))",
                                            label          = "ljets_ge4j_3t_STXS_ttH_weighted_bin_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==2)&&(DNNPredictedClass_ge4j_3t_classification==0)&& " + TTHpredicted43 +")")
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_2_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==2)&& " + TTHpredicted43 +")","ljets_ge4j_3t_STXS_ttH_weighted_bin_2_node","")
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_2_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_2_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_2_node.bin_edges = [ 
				0.2,
                0.205,
				0.21,
				0.22,
				0.23,
				0.24,
				0.5
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_2_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_3_node = vhi.variableHistoInterface(variable_name  = "((DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_3) * (DNNOutput_ge4j_3t_classification_node_ttH))",
                                            label          = "ljets_ge4j_3t_STXS_ttH_weighted_bin_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==3)&&(DNNPredictedClass_ge4j_3t_classification==0)&& " + TTHpredicted43 +")")
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_3_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==3)&& " + TTHpredicted43 +")","ljets_ge4j_3t_STXS_ttH_weighted_bin_3_node","")
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_3_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_3_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_3_node.bin_edges = [ 
				0.2,
				0.21,
				0.22,
				0.23,
				0.24,
                0.3,
				0.8
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_3_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_4_node = vhi.variableHistoInterface(variable_name  = "((DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_4) * (DNNOutput_ge4j_3t_classification_node_ttH))",
                                            label          = "ljets_ge4j_3t_STXS_ttH_weighted_bin_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==4)&&(DNNPredictedClass_ge4j_3t_classification==0)&& " + TTHpredicted43 +")")
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_4_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==4)&& " + TTHpredicted43 +")","ljets_ge4j_3t_STXS_ttH_weighted_bin_4_node","")
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_4_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_4_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_4_node.bin_edges = [ 
				0.2,
				0.21,
				0.22,
				0.23,
				0.2533,
				0.3067,
				1.0
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_weighted_bin_4_node)
    
    # ttH and tHq and tHW nodes 
    multiplikator = "( ((DNNPredictedClass_ge4j_3t_classification==0) * (DNNOutput_ge4j_3t_classification_node_ttH)) +  ((DNNPredictedClass_ge4j_3t_classification==5) * (DNNOutput_ge4j_3t_classification_node_tHq)) + ((DNNPredictedClass_ge4j_3t_classification==6) * (DNNOutput_ge4j_3t_classification_node_tHW)))"
    
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_0_node = vhi.variableHistoInterface(variable_name  = "(DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_0)*"+multiplikator,
                                            label          = "ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==0)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_0_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==0)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_0_node","")
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_0_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_0_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_0_node.bin_edges = [ 
				0.2,
				0.21,
				0.22,
				0.23,
				0.2487,
				0.2973,
				0.346,
				0.3947,
				0.4433,
				0.492,
				0.5407,
				0.5893,
				0.638,
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_0_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_1_node = vhi.variableHistoInterface(variable_name  = "(DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_1)*"+multiplikator,
                                            label          = "ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==1)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_1_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==1)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_1_node","")
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_1_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_1_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_1_node.bin_edges = [ 
				0.2,
				0.21,
				0.22,
				0.23,
				0.2413,
				0.262,
				0.2827,
				0.3033,
				0.324,
				0.3447,
				0.3653,
				0.386,
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_1_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_2_node = vhi.variableHistoInterface(variable_name  = "(DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_2)*"+multiplikator,
                                            label          = "ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==2)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_2_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==2)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_2_node","")
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_2_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_2_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_2_node.bin_edges = [ 
				0.2,
				0.21,
				0.22,
				0.23,
				0.2493,
				0.2987,
				0.348,
				0.3973,
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_2_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_3_node = vhi.variableHistoInterface(variable_name  = "(DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_3)*"+multiplikator,
                                            label          = "ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==3)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_3_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==3)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_3_node","")
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_3_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_3_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_3_node.bin_edges = [ 
				0.2,
				0.21,
				0.22,
				0.23,
				0.24,
				0.28,
				0.32,
				0.36,
				0.4,
				0.44,
				0.48,
				0.52,
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_3_node)
    
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_4_node = vhi.variableHistoInterface(variable_name  = "(DNNOutput_ge4j_3t_HTXS_node_ttH_HTXS_4)*"+multiplikator,
                                            label          = "ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==4)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_4_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_HTXS==4)&&(DNNPredictedClass_ge4j_3t_classification==0 || DNNPredictedClass_ge4j_3t_classification==5 || DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_4_node","")
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_4_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_4_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_4_node.bin_edges = [ 
				0.2,
				0.2533,
				0.3067,
				0.36,
				0.4133,
				0.4667,
				0.52,
				0.5733,
				0.6267,
				0.68,
				0.7333,
				0.7867,
				0.84,
				0.8933,
				0.9467,
				1.0
				]
    interfaces.append(interf_ljets_ge4j_3t_STXS_ttH_tH_weighted_bin_4_node)


    ############################
    # plots for ge4j_ge4t_HTXS #
    ############################

    # only ttH node 
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_0",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_Bin_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==0)&& " + TTHpredicted44 +")")
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_0_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==0)&& " + TTHpredicted44 +")","ljets_ge4j_ge4t_STXS_ttH_Bin_0_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_0_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_0_node.bin_edges = [ 
				0.2487,
				0.2973,
				0.346,
				0.3947,
				0.4433,
				0.492,
				0.5407,
				0.5893,
				0.638,
				0.6867,
				0.7353,
				0.784,
				0.8327,
				]
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_0_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_Bin_0_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_1",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_Bin_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==1)&& " + TTHpredicted44 +")")
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_1_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==1)&& " + TTHpredicted44 +")","ljets_ge4j_ge4t_STXS_ttH_Bin_1_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_1_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_1_node.bin_edges = [ 
				0.2413,
				0.262,
				0.2827,
				0.3033,
				0.324,
				0.3447,
				0.3653,
				0.386,
				0.4067,
				0.4273,
				0.448,
				0.51
				]
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_1_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_Bin_1_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_2",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_Bin_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==2)&& " + TTHpredicted44 +")")
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_2_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==2)&& " + TTHpredicted44 +")","ljets_ge4j_ge4t_STXS_ttH_Bin_2_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_2_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_2_node.bin_edges = [ 
				0.2493,
				0.2987,
				0.348,
				0.3973,
				0.4467,
				0.496,
				]
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_2_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_Bin_2_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_3",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_Bin_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==3)&& " + TTHpredicted44 +")")
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_3_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==3)&& " + TTHpredicted44 +")","ljets_ge4j_ge4t_STXS_ttH_Bin_3_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_3_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_3_node.bin_edges = [ 
				0.2,
				0.24,
				0.28,
				0.32,
				0.36,
				0.4,
				0.44,
				0.48,
				0.52,
				0.56,
				0.6,
				0.64,
				0.68,
				0.8
                ]
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_4",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_Bin_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==4)&& " + TTHpredicted44 +")")
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_4_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==4)&& " + TTHpredicted44 +")","ljets_ge4j_ge4t_STXS_ttH_Bin_4_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_4_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_4_node.bin_edges = [ 
				0.2533,
				0.3067,
				0.36,
				0.4133,
				0.4667,
				0.52,
				0.5733,
				0.6267,
				0.68,
				0.7333,
				0.7867,
				0.84,
				0.8933,
				0.9467,
				1.0
				]
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_4_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_Bin_4_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_Bin_4_node)
    
    
    # ttH and tHq and tHW nodes 
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_0",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_tH_bin_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==0)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_0_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==0)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_STXS_ttH_tH_bin_0_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_0_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_0_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_0_node.bin_edges = [ 
				0.2487,
				0.2973,
				0.346,
				0.3947,
				0.4433,
				0.492,
				0.5407,
				0.5893,
				0.638,
				0.6867,
				0.93
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_0_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_1",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_tH_bin_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==1)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_1_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==1)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_STXS_ttH_tH_bin_1_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_1_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_1_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_1_node.bin_edges = [ 
				0.262,
				0.3033,
				0.324,
				0.3447,
				0.3653,
				0.386,
				0.4067,
				0.4273,
				0.51
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_1_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_2",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_tH_bin_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==2)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_2_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==2)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_STXS_ttH_tH_bin_2_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_2_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_2_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_2_node.bin_edges = [ 
				0.2493,
				0.2987,
				0.348,
				0.3973,
				0.4467,
				0.496,
				0.5453,
				0.94
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_2_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_3",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_tH_bin_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==3)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_3_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==3)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_STXS_ttH_tH_bin_3_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_3_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_3_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_3_node.bin_edges = [ 
				0.24,
				0.28,
				0.32,
				0.36,
				0.4,
				0.44,
				0.48,
				0.52,
				0.56,
				0.6,
				0.64,
				0.8
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_3_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_4",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_tH_bin_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==4)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_4_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==4)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_STXS_ttH_tH_bin_4_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_4_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_4_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_4_node.bin_edges = [ 
				0.3067,
				0.36,
				0.4133,
				0.4667,
				0.52,
				0.5733,
				0.6267,
				0.68,
				0.7333,
				0.7867,
				0.84,
				0.8933,
				0.9467,
				1.0
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_tH_bin_4_node)

    ############################
    # plots for ge4j_ge4t_HTXS MULTIPLIED#
    ############################

    # only ttH node 
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_0_node = vhi.variableHistoInterface(variable_name  = "((DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_0) * (DNNOutput_ge4j_ge4t_classification_node_ttH))",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_weighted_bin_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==0)&&(DNNPredictedClass_ge4j_ge4t_classification==0))")
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_0_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==0))","ljets_ge4j_ge4t_STXS_ttH_weighted_bin_0_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_0_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_0_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_0_node.bin_edges = [ 
			0.2,
			0.21,
			0.22,
			0.23,
            0.2487,
            0.2973,
            0.93
            ]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_0_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_1_node = vhi.variableHistoInterface(variable_name  = "((DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_1) * (DNNOutput_ge4j_ge4t_classification_node_ttH))",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_weighted_bin_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==1)&&(DNNPredictedClass_ge4j_ge4t_classification==0))")
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_1_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==1))","ljets_ge4j_ge4t_STXS_ttH_weighted_bin_1_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_1_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_1_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_1_node.bin_edges = [ 
				0.2,
				0.21,
				0.22,
				0.23,
				0.30,
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_1_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_2_node = vhi.variableHistoInterface(variable_name  = "((DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_2) * (DNNOutput_ge4j_ge4t_classification_node_ttH))",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_weighted_bin_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==2)&&(DNNPredictedClass_ge4j_ge4t_classification==0))")
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_2_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==2))","ljets_ge4j_ge4t_STXS_ttH_weighted_bin_2_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_2_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_2_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_2_node.bin_edges = [ 
				0.2,
                0.205,
				0.21,
				0.22,
				0.23,
				0.30,
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_2_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_3_node = vhi.variableHistoInterface(variable_name  = "((DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_3) * (DNNOutput_ge4j_ge4t_classification_node_ttH))",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_weighted_bin_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==3)&&(DNNPredictedClass_ge4j_ge4t_classification==0))")
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_3_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==3))","ljets_ge4j_ge4t_STXS_ttH_weighted_bin_3_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_3_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_3_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_3_node.bin_edges = [ 
			0.2,
			0.21,
			0.22,
			0.23,
			0.30,
            0.24,
            0.8
            ]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_3_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_4_node = vhi.variableHistoInterface(variable_name  = "((DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_4) * (DNNOutput_ge4j_ge4t_classification_node_ttH))",
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_weighted_bin_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==4)&&(DNNPredictedClass_ge4j_ge4t_classification==0))")
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_4_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==4))","ljets_ge4j_ge4t_STXS_ttH_weighted_bin_4_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_4_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_4_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_4_node.bin_edges = [ 
			0.2,
			0.21,
			0.22,
			0.23,
            0.2533,
            0.3067,
            1.0
            ]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_weighted_bin_4_node)
    
    # ttH and tHq and tHW nodes 
    multiplikator = "( ((DNNPredictedClass_ge4j_ge4t_classification==0) * (DNNOutput_ge4j_ge4t_classification_node_ttH)) +  ((DNNPredictedClass_ge4j_ge4t_classification==5) * (DNNOutput_ge4j_ge4t_classification_node_tHq)) + ((DNNPredictedClass_ge4j_ge4t_classification==6) * (DNNOutput_ge4j_ge4t_classification_node_tHW)))"
    
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_0_node = vhi.variableHistoInterface(variable_name  = "(DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_0)*"+multiplikator,
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==0)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_0_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==0)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_0_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_0_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_0_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_0_node.bin_edges = [ 
				0.2,
				0.2487,
				0.2973,
				0.346,
				0.3947,
				0.93
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_0_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_1_node = vhi.variableHistoInterface(variable_name  = "(DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_1)*"+multiplikator,
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==1)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_1_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==1)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_1_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_1_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_1_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_1_node.bin_edges = [ 
				0.2,
				0.2207,
				0.2413,
				0.2827,
				0.51
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_1_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_2_node = vhi.variableHistoInterface(variable_name  = "(DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_2)*"+multiplikator,
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==2)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_2_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==2)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_2_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_2_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_2_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_2_node.bin_edges = [ 
				0.2,
				0.2493,
				0.2987,
				0.94
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_2_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_3_node = vhi.variableHistoInterface(variable_name  = "(DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_3)*"+multiplikator,
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==3)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_3_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==3)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_3_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_3_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_3_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_3_node.bin_edges = [ 
				0.2,
				0.24,
				0.28,
				0.32,
				0.4,
				0.8
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_3_node)
    
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_4_node = vhi.variableHistoInterface(variable_name  = "(DNNOutput_ge4j_ge4t_HTXS_node_ttH_HTXS_4)*"+multiplikator,
                                            label          = "ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==4)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_4_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_HTXS==4)&&(DNNPredictedClass_ge4j_ge4t_classification==0 || DNNPredictedClass_ge4j_ge4t_classification==5 || DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_4_node","")
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_4_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_4_node.nhistobins = ndefaultbins
    interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_4_node.bin_edges = [ 
				0.2,
				0.2533,
				0.3067,
				0.36,
				0.4133,
				0.4667,
				0.52,
				0.5733,
				0.68,
				0.84,
				1.0
				]
    interfaces.append(interf_ljets_ge4j_ge4t_STXS_ttH_tH_weighted_bin_4_node)










    ##################
    # CLASSIFICATION #
    ##################
    # plots for ge4j_ge4t_classification

    interf_ljets_ge4j_ge4t_classification_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_ttH",
                                            label          = "ljets_ge4j_ge4t_classification_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==0))")
    interf_ljets_ge4j_ge4t_classification_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==0))","ljets_ge4j_ge4t_classification_ttH_node","")
    interf_ljets_ge4j_ge4t_classification_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_ttH_node.bin_edges = [ 
				0.1853,
				0.2307,
				0.276,
				0.3213,
				0.3667,
				0.412,
				0.4573,
				0.5027,
				0.548,
				0.5933,
                0.7,
				0.82
				]
    interf_ljets_ge4j_ge4t_classification_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_ttH_node)
    
    interf_ljets_ge4j_ge4t_classification_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_ttbb",
                                            label          = "ljets_ge4j_ge4t_classification_ttbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==1))")
    interf_ljets_ge4j_ge4t_classification_ttbb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==1))","ljets_ge4j_ge4t_classification_ttbb_node","")
    interf_ljets_ge4j_ge4t_classification_ttbb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_ttbb_node.bin_edges = [ 
				0.178,
				0.216,
				0.254,
				0.292,
				0.33,
				0.368,
				0.406,
				0.444,
				0.482,
				0.52,
				0.558,
				0.596,
				0.672,
				]
    interf_ljets_ge4j_ge4t_classification_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_ttbb_node)
    
    interf_ljets_ge4j_ge4t_classification_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_classification_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==2))")
    interf_ljets_ge4j_ge4t_classification_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==2))","ljets_ge4j_ge4t_classification_tt2b_node","")
    interf_ljets_ge4j_ge4t_classification_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_tt2b_node.bin_edges = [ 
				0.1873,
				0.2347,
				0.282,
				0.3293,
				0.3767,
				0.424,
				0.4713,
				0.85
				]
    interf_ljets_ge4j_ge4t_classification_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_tt2b_node)
    
    interf_ljets_ge4j_ge4t_classification_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_classification_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==3))")
    interf_ljets_ge4j_ge4t_classification_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==3))","ljets_ge4j_ge4t_classification_ttcc_node","")
    interf_ljets_ge4j_ge4t_classification_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_ttcc_node.bin_edges = [ 
				0.14,
				0.46
				]
    interf_ljets_ge4j_ge4t_classification_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_ttcc_node)
    
    interf_ljets_ge4j_ge4t_classification_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_classification_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==4))")
    interf_ljets_ge4j_ge4t_classification_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==4))","ljets_ge4j_ge4t_classification_ttlf_node","")
    interf_ljets_ge4j_ge4t_classification_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_ttlf_node.bin_edges = [ 
				0.14,
				0.7
				]
    interf_ljets_ge4j_ge4t_classification_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_ttlf_node)
    
    interf_ljets_ge4j_ge4t_classification_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_tHq",
                                            label          = "ljets_ge4j_ge4t_classification_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==5))")
    interf_ljets_ge4j_ge4t_classification_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==5))","ljets_ge4j_ge4t_classification_tHq_node","")
    interf_ljets_ge4j_ge4t_classification_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_tHq_node.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_classification_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_tHq_node)
    
    interf_ljets_ge4j_ge4t_classification_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classification_node_tHW",
                                            label          = "ljets_ge4j_ge4t_classification_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==6))")
    interf_ljets_ge4j_ge4t_classification_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classification==6))","ljets_ge4j_ge4t_classification_tHW_node","")
    interf_ljets_ge4j_ge4t_classification_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classification_tHW_node.bin_edges = [ 
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
    interf_ljets_ge4j_ge4t_classification_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classification_tHW_node)
    
    # plots for ge4j_3t_classification

    interf_ljets_ge4j_3t_classification_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_ttH",
                                            label          = "ljets_ge4j_3t_classification_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==0))")
    interf_ljets_ge4j_3t_classification_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==0))","ljets_ge4j_3t_classification_ttH_node","")
    interf_ljets_ge4j_3t_classification_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_ttH_node.bin_edges = [ 
				0.14,
				0.1793,
				0.2187,
				0.258,
				0.2973,
				0.3367,
				0.376,
				0.4153,
				0.4547,
				0.494,
				0.5333,
				0.73
				]
    interf_ljets_ge4j_3t_classification_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_ttH_node)
    
    interf_ljets_ge4j_3t_classification_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_ttbb",
                                            label          = "ljets_ge4j_3t_classification_ttbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==1))")
    interf_ljets_ge4j_3t_classification_ttbb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==1))","ljets_ge4j_3t_classification_ttbb_node","")
    interf_ljets_ge4j_3t_classification_ttbb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_ttbb_node.bin_edges = [ 
				0.1633,
				0.1867,
				0.21,
				0.2333,
				0.2567,
				0.28,
				0.3033,
				0.3267,
				0.35,
				0.3733,
				0.3967,
				0.42,
				0.4667,
				0.49
				]
    interf_ljets_ge4j_3t_classification_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_ttbb_node)
    
    interf_ljets_ge4j_3t_classification_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_tt2b",
                                            label          = "ljets_ge4j_3t_classification_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==2))")
    interf_ljets_ge4j_3t_classification_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==2))","ljets_ge4j_3t_classification_tt2b_node","")
    interf_ljets_ge4j_3t_classification_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_tt2b_node.bin_edges = [ 
				0.14,
				0.1853,
				0.2307,
				0.276,
				0.3213,
				0.3667,
				0.412,
				0.4573,
				0.5027,
				0.548,
				0.5933,
				0.6387,
				0.82
				]
    interf_ljets_ge4j_3t_classification_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_tt2b_node)
    
    interf_ljets_ge4j_3t_classification_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_ttcc",
                                            label          = "ljets_ge4j_3t_classification_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==3))")
    interf_ljets_ge4j_3t_classification_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==3))","ljets_ge4j_3t_classification_ttcc_node","")
    interf_ljets_ge4j_3t_classification_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_ttcc_node.bin_edges = [ 
				0.14,
				0.44
				]
    interf_ljets_ge4j_3t_classification_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_ttcc_node)
    
    interf_ljets_ge4j_3t_classification_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_ttlf",
                                            label          = "ljets_ge4j_3t_classification_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==4))")
    interf_ljets_ge4j_3t_classification_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==4))","ljets_ge4j_3t_classification_ttlf_node","")
    interf_ljets_ge4j_3t_classification_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_ttlf_node.bin_edges = [ 
				0.14,
				0.79
				]
    interf_ljets_ge4j_3t_classification_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_ttlf_node)
    
    interf_ljets_ge4j_3t_classification_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_tHq",
                                            label          = "ljets_ge4j_3t_classification_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==5))")
    interf_ljets_ge4j_3t_classification_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==5))","ljets_ge4j_3t_classification_tHq_node","")
    interf_ljets_ge4j_3t_classification_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_tHq_node.bin_edges = [ 
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
    interf_ljets_ge4j_3t_classification_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_tHq_node)
    
    interf_ljets_ge4j_3t_classification_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classification_node_tHW",
                                            label          = "ljets_ge4j_3t_classification_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==6))")
    interf_ljets_ge4j_3t_classification_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classification==6))","ljets_ge4j_3t_classification_tHW_node","")
    interf_ljets_ge4j_3t_classification_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classification_tHW_node.bin_edges = [ 
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
    interf_ljets_ge4j_3t_classification_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classification_tHW_node)
    

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
    