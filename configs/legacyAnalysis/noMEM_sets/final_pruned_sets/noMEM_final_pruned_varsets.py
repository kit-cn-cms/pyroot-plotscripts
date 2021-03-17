
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

def plots_dnn_ttH_vs_slike(data, discrname, category, selection, label):
    ndefaultbins = 50
    interfaces = []


    interf_ttH_vs_ttB = vhi.variableHistoInterface(variable_name  = "DNNOutput_{cat}_node_ttH/(DNNOutput_{cat}_node_ttH + DNNOutput_{cat}_node_ttmb + DNNOutput_{cat}_node_tt2b)".format(cat = category),
                                            label          = "ljets_{}_ttH_vs_slike_merged".format(category),
                                            selection      = "({sel}&&(1.)&&(DNNPredictedClass_{cat}==0))".format(sel = selection, cat = category))
    interf_ttH_vs_ttB.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==0 || DNNPredictedClass_{cat}==1 || DNNPredictedClass_{cat}==2))".format(cat=category, sel = selection),"ljets_{}_ttH_vs_slike_merged".format(category),"")
    interf_ttH_vs_ttB.category_label = label
    interf_ttH_vs_ttB.minxval = 0.2
    interf_ttH_vs_ttB.maxxval = 1.0
    interf_ttH_vs_ttB.nhistobins = ndefaultbins
    interfaces.append(interf_ttH_vs_ttB)

    interf_ttH_vs_slike = vhi.variableHistoInterface(variable_name  = "DNNOutput_{cat}_node_ttH/(DNNOutput_{cat}_node_ttH + DNNOutput_{cat}_node_ttmb + DNNOutput_{cat}_node_tt2b)".format(cat = category),
                                            label          = "ljets_{}_ttH_vs_slike".format(category),
                                            selection      = "({sel}&&(1.)&&(DNNPredictedClass_{cat}==0))".format(cat = category, sel = selection))
    interf_ttH_vs_slike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==0))".format(cat = category, sel = selection),"ljets_{}_ttH_vs_slike".format(category),"")
    interf_ttH_vs_slike.category_label = label
    interf_ttH_vs_slike.minxval = 0.2
    interf_ttH_vs_slike.maxxval = 1.0
    interf_ttH_vs_slike.nhistobins = ndefaultbins
    interfaces.append(interf_ttH_vs_slike)

    interf_ttmb_vs_slike = vhi.variableHistoInterface(variable_name  = "DNNOutput_{cat}_node_ttmb/(DNNOutput_{cat}_node_ttH + DNNOutput_{cat}_node_ttmb + DNNOutput_{cat}_node_tt2b)".format(cat=category),
                                            label          = "ljets_{}_ttmb_vs_slike".format(category),
                                            selection      = "({sel}&&(1.)&&(DNNPredictedClass_{cat}==1))".format(cat = category, sel = selection))
    interf_ttmb_vs_slike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==1))".format(cat = category, sel = selection),"ljets_{}_ttmb_vs_slike".format(category),"")
    interf_ttmb_vs_slike.category_label = label
    interf_ttmb_vs_slike.minxval = 0.2
    interf_ttmb_vs_slike.maxxval = 1.0
    interf_ttmb_vs_slike.nhistobins = ndefaultbins
    interfaces.append(interf_ttmb_vs_slike)

    interf_tt2b_vs_slike = vhi.variableHistoInterface(variable_name  = "DNNOutput_{cat}_node_tt2b/(DNNOutput_{cat}_node_ttH + DNNOutput_{cat}_node_ttmb + DNNOutput_{cat}_node_tt2b)".format(cat=category),
                                            label          = "ljets_{}_tt2b_vs_slike".format(category),
                                            selection      = "({sel}&&(1.)&&(DNNPredictedClass_{cat}==2))".format(cat = category, sel = selection))
    interf_tt2b_vs_slike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==2))".format(cat = category, sel = selection),"ljets_{}_tt2b_vs_slike".format(category),"")
    interf_tt2b_vs_slike.category_label = label
    interf_tt2b_vs_slike.minxval = 0.2
    interf_tt2b_vs_slike.maxxval = 1.0
    interf_tt2b_vs_slike.nhistobins = ndefaultbins
    interfaces.append(interf_tt2b_vs_slike)

    interf_ttB_vs_slike = vhi.variableHistoInterface(variable_name  = "(DNNOutput_{cat}_node_tt2b + DNNOutput_{cat}_node_ttmb)/(DNNOutput_{cat}_node_ttH + DNNOutput_{cat}_node_ttmb + DNNOutput_{cat}_node_tt2b)".format(cat=category),
                                            label          = "ljets_{}_ttB_vs_slike".format(category),
                                            selection      = "({sel}&&(1.)&&(DNNPredictedClass_{cat}==2))".format(cat = category, sel = selection))
    interf_ttB_vs_slike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==2 || DNNPredictedClass_{cat}==1))".format(cat = category, sel = selection),"ljets_{}_ttB_vs_slike".format(category),"")
    interf_ttB_vs_slike.category_label = label
    interf_ttB_vs_slike.minxval = 0.2
    interf_ttB_vs_slike.maxxval = 1.0
    interf_ttB_vs_slike.nhistobins = ndefaultbins
    interfaces.append(interf_ttB_vs_slike)

    interf_ttH_ttmb_vs_slike = vhi.variableHistoInterface(variable_name  = "DNNOutput_{cat}_node_ttH/(DNNOutput_{cat}_node_ttH + DNNOutput_{cat}_node_ttmb + DNNOutput_{cat}_node_tt2b)".format(cat = category),
                                            label          = "ljets_{}_ttH_ttmb_vs_slike".format(category),
                                            selection      = "({sel}&&(1.)&&(DNNPredictedClass_{cat}==0))".format(sel = selection, cat = category))
    interf_ttH_ttmb_vs_slike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==0 || DNNPredictedClass_{cat}==1))".format(cat=category, sel = selection),"ljets_{}_ttH_vs_slike_merged".format(category),"")
    interf_ttH_ttmb_vs_slike.category_label = label
    interf_ttH_ttmb_vs_slike.minxval = 0.2
    interf_ttH_ttmb_vs_slike.maxxval = 1.0
    interf_ttH_ttmb_vs_slike.nhistobins = ndefaultbins
    interfaces.append(interf_ttH_ttmb_vs_slike)

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots	

def plots_dnn_X_vs_ttLF(data, discrname, category, selection, label):
    ndefaultbins = 50
    interfaces = []
    interf_ttcc_vs_ttLFlike = vhi.variableHistoInterface(variable_name  = "DNNOutput_{cat}_node_ttcc/(DNNOutput_{cat}_node_ttcc + DNNOutput_{cat}_node_ttlf)".format(cat = category),
                                            label          = "ljets_{}_ttcc_vs_ttLFlike".format(category),
                                            selection      = "({sel}&&(1.)&&(DNNPredictedClass_{cat}==0))".format(sel = selection, cat = category))
    interf_ttcc_vs_ttLFlike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==3 || DNNPredictedClass_{cat}==4))".format(cat=category, sel = selection),"ljets_{}_ttcc_vs_ttLFlike".format(category),"")
    interf_ttcc_vs_ttLFlike.category_label = label
    interf_ttcc_vs_ttLFlike.minxval = 0.2
    interf_ttcc_vs_ttLFlike.maxxval = 1.0
    interf_ttcc_vs_ttLFlike.nhistobins = ndefaultbins
    interfaces.append(interf_ttcc_vs_ttLFlike)

    interf_ttlf_vs_ttLFlike = vhi.variableHistoInterface(variable_name  = "DNNOutput_{cat}_node_ttlf/(DNNOutput_{cat}_node_ttcc + DNNOutput_{cat}_node_ttlf)".format(cat = category),
                                            label          = "ljets_{}_ttlf_vs_ttLFlike".format(category),
                                            selection      = "({sel}&&(1.)&&(DNNPredictedClass_{cat}==0))".format(sel = selection, cat = category))
    interf_ttlf_vs_ttLFlike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==3 || DNNPredictedClass_{cat}==4))".format(cat=category, sel = selection),"ljets_{}_ttlf_vs_ttLFlike".format(category),"")
    interf_ttlf_vs_ttLFlike.category_label = label
    interf_ttlf_vs_ttLFlike.minxval = 0.2
    interf_ttlf_vs_ttLFlike.maxxval = 1.0
    interf_ttlf_vs_ttLFlike.nhistobins = ndefaultbins
    interfaces.append(interf_ttlf_vs_ttLFlike)

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots	

def plots_dnn(data, discrname):

    ndefaultbins = 50
    interfaces = []


    # plots for ge4j_3t_v1

    interf_ljets_ge4j_3t_v1_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v1_node_ttH",
                                            label          = "ljets_ge4j_3t_v1_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==0))")
    interf_ljets_ge4j_3t_v1_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==0))","ljets_ge4j_3t_v1_ttH_node","")
    interf_ljets_ge4j_3t_v1_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v1_ttH_node.minxval = 0.14
    interf_ljets_ge4j_3t_v1_ttH_node.maxxval = 0.75
    interf_ljets_ge4j_3t_v1_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v1_ttH_node)
    
    interf_ljets_ge4j_3t_v1_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v1_node_ttmb",
                                            label          = "ljets_ge4j_3t_v1_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==1))")
    interf_ljets_ge4j_3t_v1_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==1))","ljets_ge4j_3t_v1_ttmb_node","")
    interf_ljets_ge4j_3t_v1_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v1_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_3t_v1_ttmb_node.maxxval = 0.5
    interf_ljets_ge4j_3t_v1_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v1_ttmb_node)
    
    interf_ljets_ge4j_3t_v1_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v1_node_tt2b",
                                            label          = "ljets_ge4j_3t_v1_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==2))")
    interf_ljets_ge4j_3t_v1_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==2))","ljets_ge4j_3t_v1_tt2b_node","")
    interf_ljets_ge4j_3t_v1_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v1_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_3t_v1_tt2b_node.maxxval = 0.8
    interf_ljets_ge4j_3t_v1_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v1_tt2b_node)
    
    interf_ljets_ge4j_3t_v1_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v1_node_ttcc",
                                            label          = "ljets_ge4j_3t_v1_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==3))")
    interf_ljets_ge4j_3t_v1_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==3))","ljets_ge4j_3t_v1_ttcc_node","")
    interf_ljets_ge4j_3t_v1_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v1_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_3t_v1_ttcc_node.maxxval = 0.47
    interf_ljets_ge4j_3t_v1_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v1_ttcc_node)
    
    interf_ljets_ge4j_3t_v1_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v1_node_ttlf",
                                            label          = "ljets_ge4j_3t_v1_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==4))")
    interf_ljets_ge4j_3t_v1_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==4))","ljets_ge4j_3t_v1_ttlf_node","")
    interf_ljets_ge4j_3t_v1_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v1_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_3t_v1_ttlf_node.maxxval = 0.84
    interf_ljets_ge4j_3t_v1_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v1_ttlf_node)
    
    interf_ljets_ge4j_3t_v1_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v1_node_tHq",
                                            label          = "ljets_ge4j_3t_v1_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==5))")
    interf_ljets_ge4j_3t_v1_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==5))","ljets_ge4j_3t_v1_tHq_node","")
    interf_ljets_ge4j_3t_v1_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v1_tHq_node.minxval = 0.14
    interf_ljets_ge4j_3t_v1_tHq_node.maxxval = 0.96
    interf_ljets_ge4j_3t_v1_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v1_tHq_node)
    
    interf_ljets_ge4j_3t_v1_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v1_node_tHW",
                                            label          = "ljets_ge4j_3t_v1_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==6))")
    interf_ljets_ge4j_3t_v1_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v1==6))","ljets_ge4j_3t_v1_tHW_node","")
    interf_ljets_ge4j_3t_v1_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v1_tHW_node.minxval = 0.14
    interf_ljets_ge4j_3t_v1_tHW_node.maxxval = 1.0
    interf_ljets_ge4j_3t_v1_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v1_tHW_node)
    


    # plots for ge4j_3t_v2

    interf_ljets_ge4j_3t_v2_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v2_node_ttH",
                                            label          = "ljets_ge4j_3t_v2_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==0))")
    interf_ljets_ge4j_3t_v2_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==0))","ljets_ge4j_3t_v2_ttH_node","")
    interf_ljets_ge4j_3t_v2_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v2_ttH_node.minxval = 0.14
    interf_ljets_ge4j_3t_v2_ttH_node.maxxval = 0.73
    interf_ljets_ge4j_3t_v2_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v2_ttH_node)
    
    interf_ljets_ge4j_3t_v2_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v2_node_ttmb",
                                            label          = "ljets_ge4j_3t_v2_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==1))")
    interf_ljets_ge4j_3t_v2_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==1))","ljets_ge4j_3t_v2_ttmb_node","")
    interf_ljets_ge4j_3t_v2_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v2_ttmb_node.minxval = 0.14
    interf_ljets_ge4j_3t_v2_ttmb_node.maxxval = 0.46
    interf_ljets_ge4j_3t_v2_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v2_ttmb_node)
    
    interf_ljets_ge4j_3t_v2_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v2_node_tt2b",
                                            label          = "ljets_ge4j_3t_v2_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==2))")
    interf_ljets_ge4j_3t_v2_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==2))","ljets_ge4j_3t_v2_tt2b_node","")
    interf_ljets_ge4j_3t_v2_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v2_tt2b_node.minxval = 0.14
    interf_ljets_ge4j_3t_v2_tt2b_node.maxxval = 0.61
    interf_ljets_ge4j_3t_v2_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v2_tt2b_node)
    
    interf_ljets_ge4j_3t_v2_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v2_node_ttcc",
                                            label          = "ljets_ge4j_3t_v2_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==3))")
    interf_ljets_ge4j_3t_v2_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==3))","ljets_ge4j_3t_v2_ttcc_node","")
    interf_ljets_ge4j_3t_v2_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v2_ttcc_node.minxval = 0.14
    interf_ljets_ge4j_3t_v2_ttcc_node.maxxval = 0.45
    interf_ljets_ge4j_3t_v2_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v2_ttcc_node)
    
    interf_ljets_ge4j_3t_v2_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v2_node_ttlf",
                                            label          = "ljets_ge4j_3t_v2_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==4))")
    interf_ljets_ge4j_3t_v2_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==4))","ljets_ge4j_3t_v2_ttlf_node","")
    interf_ljets_ge4j_3t_v2_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v2_ttlf_node.minxval = 0.14
    interf_ljets_ge4j_3t_v2_ttlf_node.maxxval = 0.85
    interf_ljets_ge4j_3t_v2_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v2_ttlf_node)
    
    interf_ljets_ge4j_3t_v2_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v2_node_tHq",
                                            label          = "ljets_ge4j_3t_v2_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==5))")
    interf_ljets_ge4j_3t_v2_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==5))","ljets_ge4j_3t_v2_tHq_node","")
    interf_ljets_ge4j_3t_v2_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v2_tHq_node.minxval = 0.14
    interf_ljets_ge4j_3t_v2_tHq_node.maxxval = 0.98
    interf_ljets_ge4j_3t_v2_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v2_tHq_node)
    
    interf_ljets_ge4j_3t_v2_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_v2_node_tHW",
                                            label          = "ljets_ge4j_3t_v2_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==6))")
    interf_ljets_ge4j_3t_v2_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_v2==6))","ljets_ge4j_3t_v2_tHW_node","")
    interf_ljets_ge4j_3t_v2_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_v2_tHW_node.minxval = 0.14
    interf_ljets_ge4j_3t_v2_tHW_node.maxxval = 0.99
    interf_ljets_ge4j_3t_v2_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_v2_tHW_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_dnn(data, discrname)
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"
    discriminatorPlots += plots_dnn_ttH_vs_slike(data = data, discrname=discrname, category="ge4j_3t_v1", selection= selection, label = label )
    discriminatorPlots += plots_dnn_ttH_vs_slike(data = data, discrname=discrname, category="ge4j_3t_v2", selection= selection, label = label )
    discriminatorPlots += plots_dnn_X_vs_ttLF(data = data, discrname=discrname, category="ge4j_3t_v1", selection= selection, label = label )
    discriminatorPlots += plots_dnn_X_vs_ttLF(data = data, discrname=discrname, category="ge4j_3t_v2", selection= selection, label = label )
    

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
    