
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


    # plots for top10_ge4j_ge4t

    interf_ljets_top10_ge4j_ge4t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttH",
                                            label          = "ljets_top10_ge4j_ge4t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0))")
    interf_ljets_top10_ge4j_ge4t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0))","ljets_top10_ge4j_ge4t_ttH_node","")
    interf_ljets_top10_ge4j_ge4t_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttH_node.bin_edges = [ 
				0.14,
				0.2238,
				0.3075,
				0.3913,
				0.475,
				0.5588,
				0.6425,
				0.81
				]
    interf_ljets_top10_ge4j_ge4t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttH_node)
    
    interf_ljets_top10_ge4j_ge4t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttmb",
                                            label          = "ljets_top10_ge4j_ge4t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==1))")
    interf_ljets_top10_ge4j_ge4t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==1))","ljets_top10_ge4j_ge4t_ttmb_node","")
    interf_ljets_top10_ge4j_ge4t_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttmb_node.bin_edges = [ 
				0.2087,
				0.2775,
				0.3463,
				0.415,
				0.4837,
				0.5525,
				0.69
				]
    interf_ljets_top10_ge4j_ge4t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttmb_node)
    
    interf_ljets_top10_ge4j_ge4t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_top10_ge4j_ge4t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==2))")
    interf_ljets_top10_ge4j_ge4t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==2))","ljets_top10_ge4j_ge4t_tt2b_node","")
    interf_ljets_top10_ge4j_ge4t_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_tt2b_node.bin_edges = [ 
				0.14,
				0.2125,
				0.285,
				0.3575,
				0.43,
				0.72
				]
    interf_ljets_top10_ge4j_ge4t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_tt2b_node)
    
    interf_ljets_top10_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_top10_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==3))")
    interf_ljets_top10_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==3))","ljets_top10_ge4j_ge4t_ttcc_node","")
    interf_ljets_top10_ge4j_ge4t_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttcc_node.bin_edges = [ 
				0.18,
				0.22,
				0.26,
				0.3,
				0.34,
				0.38,
				0.42,
				0.46
				]
    interf_ljets_top10_ge4j_ge4t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttcc_node)
    
    interf_ljets_top10_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_top10_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==4))")
    interf_ljets_top10_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==4))","ljets_top10_ge4j_ge4t_ttlf_node","")
    interf_ljets_top10_ge4j_ge4t_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttlf_node.bin_edges = [ 
				0.2137,
				0.2875,
				0.3613,
				0.435,
				0.5088,
				0.5825,
				0.6563,
				0.73
				]
    interf_ljets_top10_ge4j_ge4t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttlf_node)
    
    interf_ljets_top10_ge4j_ge4t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_tHq",
                                            label          = "ljets_top10_ge4j_ge4t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==5))")
    interf_ljets_top10_ge4j_ge4t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==5))","ljets_top10_ge4j_ge4t_tHq_node","")
    interf_ljets_top10_ge4j_ge4t_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_tHq_node.bin_edges = [ 
				0.14,
				0.2463,
				0.3525,
				0.4587,
				0.565,
				0.6713,
				0.7775,
				0.99
				]
    interf_ljets_top10_ge4j_ge4t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_tHq_node)
    
    interf_ljets_top10_ge4j_ge4t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_tHW",
                                            label          = "ljets_top10_ge4j_ge4t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==6))")
    interf_ljets_top10_ge4j_ge4t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==6))","ljets_top10_ge4j_ge4t_tHW_node","")
    interf_ljets_top10_ge4j_ge4t_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_tHW_node.bin_edges = [ 
				0.14,
				0.2475,
				0.355,
				0.4625,
				0.57,
				0.6775,
				0.785,
				0.8925,
				1.0
				]
    interf_ljets_top10_ge4j_ge4t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_tHW_node)
    


    # plots for STXS_Top10_ge4j_ge4t

    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10_ge4j_ge4t_node_ttH_HTXS_0",
                                            label          = "ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_ge4t==0))")
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_0_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_ge4t==0))","ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_0_node","")
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_0_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_0_node.bin_edges = [ 
				0.3575,
				0.4362,
				0.515,
				0.5938,
				0.83
				]
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_0_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_0_node)
    
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10_ge4j_ge4t_node_ttH_HTXS_1",
                                            label          = "ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_ge4t==1))")
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_1_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_ge4t==1))","ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_1_node","")
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_1_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_1_node.bin_edges = [ 
				0.31,
				0.3375,
				0.365,
				0.42
				]
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_1_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_1_node)
    
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10_ge4j_ge4t_node_ttH_HTXS_2",
                                            label          = "ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_ge4t==2))")
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_2_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_ge4t==2))","ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_2_node","")
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_2_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_2_node.bin_edges = [ 
				0.2725,
				0.3087,
				0.345,
				0.3812,
				0.49
				]
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_2_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_2_node)
    
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10_ge4j_ge4t_node_ttH_HTXS_3",
                                            label          = "ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_ge4t==3))")
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_3_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_ge4t==3))","ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_3_node","")
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_3_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_3_node.bin_edges = [ 
				0.295,
				0.3425,
				0.39,
				0.4375,
				0.58
				]
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_3_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_3_node)
    
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10_ge4j_ge4t_node_ttH_HTXS_4",
                                            label          = "ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_ge4t==4))")
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_4_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_ge4t==4))","ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_4_node","")
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_4_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_4_node.bin_edges = [ 
				0.4,
				0.5,
				0.7,
				1.0
				]
    interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_4_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10_ge4j_ge4t_ttH_HTXS_4_node)
    


    # plots for STXS_Top10wClass_ge4j_ge4t

    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10wClass_ge4j_ge4t_node_ttH_HTXS_0",
                                            label          = "ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_ge4t==0))")
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_0_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_ge4t==0))","ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_0_node","")
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_0_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_0_node.bin_edges = [ 
				0.3575,
				0.4362,
				0.515,
				0.5938,
				0.83
				]
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_0_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_0_node)
    
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10wClass_ge4j_ge4t_node_ttH_HTXS_1",
                                            label          = "ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_ge4t==1))")
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_1_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_ge4t==1))","ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_1_node","")
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_1_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_1_node.bin_edges = [ 
				0.2938,
				0.325,
				0.3563,
				0.3875,
				0.45
				]
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_1_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_1_node)
    
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10wClass_ge4j_ge4t_node_ttH_HTXS_2",
                                            label          = "ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_ge4t==2))")
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_2_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_ge4t==2))","ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_2_node","")
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_2_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_2_node.bin_edges = [ 
				0.2563,
				0.3125,
				0.3688,
				0.65
				]
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_2_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_2_node)
    
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10wClass_ge4j_ge4t_node_ttH_HTXS_3",
                                            label          = "ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_ge4t==3))")
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_3_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_ge4t==3))","ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_3_node","")
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_3_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_3_node.bin_edges = [ 
				0.3,
				0.35,
				0.4,
				0.45,
				0.6
				]
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_3_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_3_node)
    
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10wClass_ge4j_ge4t_node_ttH_HTXS_4",
                                            label          = "ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_ge4t==4))")
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_4_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_ge4t==4))","ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_4_node","")
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_4_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_4_node.bin_edges = [ 
				0.4,
				0.5,
				0.7,
				1.0
				]
    interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_4_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10wClass_ge4j_ge4t_ttH_HTXS_4_node)
    


    # plots for top10_ge4j_3t

    interf_ljets_top10_ge4j_3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttH",
                                            label          = "ljets_top10_ge4j_3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0))")
    interf_ljets_top10_ge4j_3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0))","ljets_top10_ge4j_3t_ttH_node","")
    interf_ljets_top10_ge4j_3t_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttH_node.bin_edges = [ 
				0.14,
				0.2112,
				0.2825,
				0.3538,
				0.425,
				0.4962,
				0.5675,
				0.71
				]
    interf_ljets_top10_ge4j_3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttH_node)
    
    interf_ljets_top10_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttmb",
                                            label          = "ljets_top10_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==1))")
    interf_ljets_top10_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==1))","ljets_top10_ge4j_3t_ttmb_node","")
    interf_ljets_top10_ge4j_3t_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttmb_node.bin_edges = [ 
				0.14,
				0.18,
				0.22,
				0.26,
				0.3,
				0.34,
				0.38,
				0.42,
				0.46
				]
    interf_ljets_top10_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttmb_node)
    
    interf_ljets_top10_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_tt2b",
                                            label          = "ljets_top10_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==2))")
    interf_ljets_top10_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==2))","ljets_top10_ge4j_3t_tt2b_node","")
    interf_ljets_top10_ge4j_3t_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_tt2b_node.bin_edges = [ 
				0.14,
				0.2137,
				0.2875,
				0.3613,
				0.435,
				0.5088,
				0.5825,
				0.73
				]
    interf_ljets_top10_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_tt2b_node)
    
    interf_ljets_top10_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttcc",
                                            label          = "ljets_top10_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==3))")
    interf_ljets_top10_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==3))","ljets_top10_ge4j_3t_ttcc_node","")
    interf_ljets_top10_ge4j_3t_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttcc_node.bin_edges = [ 
				0.14,
				0.185,
				0.23,
				0.275,
				0.32,
				0.365,
				0.41,
				0.455,
				0.5
				]
    interf_ljets_top10_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttcc_node)
    
    interf_ljets_top10_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttlf",
                                            label          = "ljets_top10_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==4))")
    interf_ljets_top10_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==4))","ljets_top10_ge4j_3t_ttlf_node","")
    interf_ljets_top10_ge4j_3t_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttlf_node.bin_edges = [ 
				0.14,
				0.22,
				0.3,
				0.38,
				0.46,
				0.54,
				0.62,
				0.7,
				0.78
				]
    interf_ljets_top10_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttlf_node)
    
    interf_ljets_top10_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_tHq",
                                            label          = "ljets_top10_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==5))")
    interf_ljets_top10_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==5))","ljets_top10_ge4j_3t_tHq_node","")
    interf_ljets_top10_ge4j_3t_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_tHq_node.bin_edges = [ 
				0.14,
				0.2463,
				0.3525,
				0.4587,
				0.565,
				0.6713,
				0.7775,
				0.8838,
				0.99
				]
    interf_ljets_top10_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_tHq_node)
    
    interf_ljets_top10_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_tHW",
                                            label          = "ljets_top10_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==6))")
    interf_ljets_top10_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==6))","ljets_top10_ge4j_3t_tHW_node","")
    interf_ljets_top10_ge4j_3t_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_tHW_node.bin_edges = [ 
				0.14,
				0.2475,
				0.355,
				0.4625,
				0.57,
				0.6775,
				0.785,
				0.8925,
				1.0
				]
    interf_ljets_top10_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_tHW_node)
    


    # plots for STXS_Top10_ge4j_3t

    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10_ge4j_3t_node_ttH_HTXS_0",
                                            label          = "ljets_STXS_Top10_ge4j_3t_ttH_HTXS_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_3t==0))")
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_0_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_3t==0))","ljets_STXS_Top10_ge4j_3t_ttH_HTXS_0_node","")
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_0_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_0_node.bin_edges = [ 
				0.2,
				0.29,
				0.38,
				0.47,
				0.56,
				0.65,
				0.74,
				0.92
				]
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_0_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_0_node)
    
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10_ge4j_3t_node_ttH_HTXS_1",
                                            label          = "ljets_STXS_Top10_ge4j_3t_ttH_HTXS_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_3t==1))")
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_1_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_3t==1))","ljets_STXS_Top10_ge4j_3t_ttH_HTXS_1_node","")
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_1_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_1_node.bin_edges = [ 
				0.2825,
				0.31,
				0.3375,
				0.365,
				0.3925,
				0.42
				]
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_1_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_1_node)
    
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10_ge4j_3t_node_ttH_HTXS_2",
                                            label          = "ljets_STXS_Top10_ge4j_3t_ttH_HTXS_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_3t==2))")
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_2_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_3t==2))","ljets_STXS_Top10_ge4j_3t_ttH_HTXS_2_node","")
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_2_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_2_node.bin_edges = [ 
				0.2338,
				0.2675,
				0.3013,
				0.335,
				0.3688,
				0.4025,
				0.47
				]
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_2_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_2_node)
    
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10_ge4j_3t_node_ttH_HTXS_3",
                                            label          = "ljets_STXS_Top10_ge4j_3t_ttH_HTXS_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_3t==3))")
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_3_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_3t==3))","ljets_STXS_Top10_ge4j_3t_ttH_HTXS_3_node","")
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_3_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_3_node.bin_edges = [ 
				0.2487,
				0.2975,
				0.3463,
				0.395,
				0.4437,
				0.4925,
				0.59
				]
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_3_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_3_node)
    
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10_ge4j_3t_node_ttH_HTXS_4",
                                            label          = "ljets_STXS_Top10_ge4j_3t_ttH_HTXS_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_3t==4))")
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_4_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10_ge4j_3t==4))","ljets_STXS_Top10_ge4j_3t_ttH_HTXS_4_node","")
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_4_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_4_node.bin_edges = [ 
				0.3,
				0.4,
				0.5,
				0.6,
				0.7,
				0.8,
				0.9,
				1.0
				]
    interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_4_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10_ge4j_3t_ttH_HTXS_4_node)
    


    # plots for STXS_Top10wClass_ge4j_3t

    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_0_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10wClass_ge4j_3t_node_ttH_HTXS_0",
                                            label          = "ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_0_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_3t==0))")
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_0_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_3t==0))","ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_0_node","")
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_0_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_0_node.bin_edges = [ 
				0.2,
				0.2825,
				0.365,
				0.4475,
				0.53,
				0.6125,
				0.695,
				0.86
				]
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_0_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_0_node)
    
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10wClass_ge4j_3t_node_ttH_HTXS_1",
                                            label          = "ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_3t==1))")
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_1_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_3t==1))","ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_1_node","")
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_1_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_1_node.bin_edges = [ 
				0.2787,
				0.305,
				0.3312,
				0.3575,
				0.3837,
				0.41
				]
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_1_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_1_node)
    
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10wClass_ge4j_3t_node_ttH_HTXS_2",
                                            label          = "ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_3t==2))")
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_2_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_3t==2))","ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_2_node","")
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_2_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_2_node.bin_edges = [ 
				0.2325,
				0.265,
				0.2975,
				0.33,
				0.3625,
				0.395,
				0.46
				]
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_2_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_2_node)
    
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10wClass_ge4j_3t_node_ttH_HTXS_3",
                                            label          = "ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_3t==3))")
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_3_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_3t==3))","ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_3_node","")
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_3_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_3_node.bin_edges = [ 
				0.2462,
				0.2925,
				0.3387,
				0.385,
				0.4312,
				0.4775,
				0.57
				]
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_3_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_3_node)
    
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_STXS_Top10wClass_ge4j_3t_node_ttH_HTXS_4",
                                            label          = "ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_3t==4))")
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_4_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0)&&(DNNPredictedClass_STXS_Top10wClass_ge4j_3t==4))","ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_4_node","")
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_4_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_4_node.bin_edges = [ 
				0.3,
				0.4,
				0.5,
				0.6,
				0.7,
				0.8,
				0.9,
				1.0
				]
    interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_4_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_STXS_Top10wClass_ge4j_3t_ttH_HTXS_4_node)
    

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
    