
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


    # plots for classifier_ge4j_ge4t

    interf_ljets_classifier_ge4j_ge4t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_ge4t_node_ttH",
                                            label          = "ljets_classifier_ge4j_ge4t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==0))")
    interf_ljets_classifier_ge4j_ge4t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==0))","ljets_classifier_ge4j_ge4t_ttH_node","")
    interf_ljets_classifier_ge4j_ge4t_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_classifier_ge4j_ge4t_ttH_node.minxval = 0.14
    interf_ljets_classifier_ge4j_ge4t_ttH_node.maxxval = 0.93
    interf_ljets_classifier_ge4j_ge4t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_ge4t_ttH_node)
    
    interf_ljets_classifier_ge4j_ge4t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_ge4t_node_ttmb",
                                            label          = "ljets_classifier_ge4j_ge4t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==1))")
    interf_ljets_classifier_ge4j_ge4t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==1))","ljets_classifier_ge4j_ge4t_ttmb_node","")
    interf_ljets_classifier_ge4j_ge4t_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_classifier_ge4j_ge4t_ttmb_node.minxval = 0.14
    interf_ljets_classifier_ge4j_ge4t_ttmb_node.maxxval = 0.75
    interf_ljets_classifier_ge4j_ge4t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_ge4t_ttmb_node)
    
    interf_ljets_classifier_ge4j_ge4t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_classifier_ge4j_ge4t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==2))")
    interf_ljets_classifier_ge4j_ge4t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==2))","ljets_classifier_ge4j_ge4t_tt2b_node","")
    interf_ljets_classifier_ge4j_ge4t_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_classifier_ge4j_ge4t_tt2b_node.minxval = 0.14
    interf_ljets_classifier_ge4j_ge4t_tt2b_node.maxxval = 0.4
    interf_ljets_classifier_ge4j_ge4t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_ge4t_tt2b_node)
    
    interf_ljets_classifier_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_classifier_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==3))")
    interf_ljets_classifier_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==3))","ljets_classifier_ge4j_ge4t_ttcc_node","")
    interf_ljets_classifier_ge4j_ge4t_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_classifier_ge4j_ge4t_ttcc_node.minxval = 0.14
    interf_ljets_classifier_ge4j_ge4t_ttcc_node.maxxval = 0.6
    interf_ljets_classifier_ge4j_ge4t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_ge4t_ttcc_node)
    
    interf_ljets_classifier_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_classifier_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==4))")
    interf_ljets_classifier_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==4))","ljets_classifier_ge4j_ge4t_ttlf_node","")
    interf_ljets_classifier_ge4j_ge4t_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_classifier_ge4j_ge4t_ttlf_node.minxval = 0.14
    interf_ljets_classifier_ge4j_ge4t_ttlf_node.maxxval = 0.71
    interf_ljets_classifier_ge4j_ge4t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_ge4t_ttlf_node)
    
    interf_ljets_classifier_ge4j_ge4t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_ge4t_node_tHq",
                                            label          = "ljets_classifier_ge4j_ge4t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==5))")
    interf_ljets_classifier_ge4j_ge4t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==5))","ljets_classifier_ge4j_ge4t_tHq_node","")
    interf_ljets_classifier_ge4j_ge4t_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_classifier_ge4j_ge4t_tHq_node.minxval = 0.14
    interf_ljets_classifier_ge4j_ge4t_tHq_node.maxxval = 0.99
    interf_ljets_classifier_ge4j_ge4t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_ge4t_tHq_node)
    
    interf_ljets_classifier_ge4j_ge4t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_ge4t_node_tHW",
                                            label          = "ljets_classifier_ge4j_ge4t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==6))")
    interf_ljets_classifier_ge4j_ge4t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_classifier_ge4j_ge4t==6))","ljets_classifier_ge4j_ge4t_tHW_node","")
    interf_ljets_classifier_ge4j_ge4t_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_classifier_ge4j_ge4t_tHW_node.minxval = 0.14
    interf_ljets_classifier_ge4j_ge4t_tHW_node.maxxval = 1.0
    interf_ljets_classifier_ge4j_ge4t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_ge4t_tHW_node)
    


    # plots for classifier_ge4j_3t

    interf_ljets_classifier_ge4j_3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_3t_node_ttH",
                                            label          = "ljets_classifier_ge4j_3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==0))")
    interf_ljets_classifier_ge4j_3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==0))","ljets_classifier_ge4j_3t_ttH_node","")
    interf_ljets_classifier_ge4j_3t_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_classifier_ge4j_3t_ttH_node.minxval = 0.14
    interf_ljets_classifier_ge4j_3t_ttH_node.maxxval = 0.9
    interf_ljets_classifier_ge4j_3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_3t_ttH_node)
    
    interf_ljets_classifier_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_3t_node_ttmb",
                                            label          = "ljets_classifier_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==1))")
    interf_ljets_classifier_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==1))","ljets_classifier_ge4j_3t_ttmb_node","")
    interf_ljets_classifier_ge4j_3t_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_classifier_ge4j_3t_ttmb_node.minxval = 0.14
    interf_ljets_classifier_ge4j_3t_ttmb_node.maxxval = 0.54
    interf_ljets_classifier_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_3t_ttmb_node)
    
    interf_ljets_classifier_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_3t_node_tt2b",
                                            label          = "ljets_classifier_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==2))")
    interf_ljets_classifier_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==2))","ljets_classifier_ge4j_3t_tt2b_node","")
    interf_ljets_classifier_ge4j_3t_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_classifier_ge4j_3t_tt2b_node.minxval = 0.14
    interf_ljets_classifier_ge4j_3t_tt2b_node.maxxval = 0.69
    interf_ljets_classifier_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_3t_tt2b_node)
    
    interf_ljets_classifier_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_3t_node_ttcc",
                                            label          = "ljets_classifier_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==3))")
    interf_ljets_classifier_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==3))","ljets_classifier_ge4j_3t_ttcc_node","")
    interf_ljets_classifier_ge4j_3t_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_classifier_ge4j_3t_ttcc_node.minxval = 0.14
    interf_ljets_classifier_ge4j_3t_ttcc_node.maxxval = 0.68
    interf_ljets_classifier_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_3t_ttcc_node)
    
    interf_ljets_classifier_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_3t_node_ttlf",
                                            label          = "ljets_classifier_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==4))")
    interf_ljets_classifier_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==4))","ljets_classifier_ge4j_3t_ttlf_node","")
    interf_ljets_classifier_ge4j_3t_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_classifier_ge4j_3t_ttlf_node.minxval = 0.14
    interf_ljets_classifier_ge4j_3t_ttlf_node.maxxval = 0.77
    interf_ljets_classifier_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_3t_ttlf_node)
    
    interf_ljets_classifier_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_3t_node_tHq",
                                            label          = "ljets_classifier_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==5))")
    interf_ljets_classifier_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==5))","ljets_classifier_ge4j_3t_tHq_node","")
    interf_ljets_classifier_ge4j_3t_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_classifier_ge4j_3t_tHq_node.minxval = 0.14
    interf_ljets_classifier_ge4j_3t_tHq_node.maxxval = 0.93
    interf_ljets_classifier_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_3t_tHq_node)
    
    interf_ljets_classifier_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_classifier_ge4j_3t_node_tHW",
                                            label          = "ljets_classifier_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==6))")
    interf_ljets_classifier_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_classifier_ge4j_3t==6))","ljets_classifier_ge4j_3t_tHW_node","")
    interf_ljets_classifier_ge4j_3t_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_classifier_ge4j_3t_tHW_node.minxval = 0.14
    interf_ljets_classifier_ge4j_3t_tHW_node.maxxval = 1.0
    interf_ljets_classifier_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_classifier_ge4j_3t_tHW_node)
    

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
    