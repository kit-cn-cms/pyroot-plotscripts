
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
				0.1717,
				0.2283,
				0.285,
				0.3417,
				0.3983,
				0.455,
				0.5117,
				0.5683,
				0.625,
				0.6817,
				0.71
				]
    interf_ljets_ge6j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttHbb_node)
    
    interf_ljets_ge6j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttZbb",
                                            label          = "ljets_ge6j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))")
    interf_ljets_ge6j_ge3t_ttZbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttZbb_node","")
    interf_ljets_ge6j_ge3t_ttZbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttZbb_node.bin_edges = [ 
				0.1661,
				0.2339,
				0.3017,
				0.3694,
				0.4372,
				0.505,
				0.5728,
				0.6406,
				0.7083,
				0.7761,
				0.81
				]
    interf_ljets_ge6j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttZbb_node)
    
    interf_ljets_ge6j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))")
    interf_ljets_ge6j_ge3t_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_ttbb_node","")
    interf_ljets_ge6j_ge3t_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttbb_node.bin_edges = [ 
				0.1606,
				0.2394,
				0.3183,
				0.3972,
				0.4761,
				0.555,
				0.6339,
				0.7128,
				0.7917,
				0.8706,
				0.91
				]
    interf_ljets_ge6j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttbb_node)
    
    interf_ljets_ge6j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))")
    interf_ljets_ge6j_ge3t_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttcc_node","")
    interf_ljets_ge6j_ge3t_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttcc_node.bin_edges = [ 
				0.1794,
				0.2206,
				0.2617,
				0.3028,
				0.3439,
				0.385,
				0.4261,
				0.4672,
				0.5083,
				0.5494,
				0.57
				]
    interf_ljets_ge6j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttcc_node)
    
    interf_ljets_ge6j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))")
    interf_ljets_ge6j_ge3t_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttlf_node","")
    interf_ljets_ge6j_ge3t_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttlf_node.bin_edges = [ 
				0.1739,
				0.2261,
				0.2783,
				0.3306,
				0.3828,
				0.435,
				0.4872,
				0.5394,
				0.5917,
				0.6439,
				0.67
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
				0.165,
				0.235,
				0.305,
				0.375,
				0.445,
				0.515,
				0.585,
				0.655,
				0.725,
				0.795,
				0.83
				]
    interf_ljets_4j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttHbb_node)
    
    interf_ljets_4j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttZbb",
                                            label          = "ljets_4j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))")
    interf_ljets_4j_ge3t_ttZbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttZbb_node","")
    interf_ljets_4j_ge3t_ttZbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttZbb_node.bin_edges = [ 
				0.1639,
				0.2361,
				0.3083,
				0.3806,
				0.4528,
				0.525,
				0.5972,
				0.6694,
				0.7417,
				0.8139,
				0.85
				]
    interf_ljets_4j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttZbb_node)
    
    interf_ljets_4j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttbb",
                                            label          = "ljets_4j_ge3t_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))")
    interf_ljets_4j_ge3t_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_ttbb_node","")
    interf_ljets_4j_ge3t_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttbb_node.bin_edges = [ 
				0.1606,
				0.2394,
				0.3183,
				0.3972,
				0.4761,
				0.555,
				0.6339,
				0.7128,
				0.7917,
				0.8706,
				0.91
				]
    interf_ljets_4j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttbb_node)
    
    interf_ljets_4j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttcc",
                                            label          = "ljets_4j_ge3t_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))")
    interf_ljets_4j_ge3t_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttcc_node","")
    interf_ljets_4j_ge3t_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttcc_node.bin_edges = [ 
				0.1739,
				0.2261,
				0.2783,
				0.3306,
				0.3828,
				0.435,
				0.4872,
				0.5394,
				0.5917,
				0.6439,
				0.67
				]
    interf_ljets_4j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttcc_node)
    
    interf_ljets_4j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttlf",
                                            label          = "ljets_4j_ge3t_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))")
    interf_ljets_4j_ge3t_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttlf_node","")
    interf_ljets_4j_ge3t_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttlf_node.bin_edges = [ 
				0.1744,
				0.2256,
				0.2767,
				0.3278,
				0.3789,
				0.43,
				0.4811,
				0.5322,
				0.5833,
				0.6344,
				0.66
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
				0.1672,
				0.2328,
				0.2983,
				0.3639,
				0.4294,
				0.495,
				0.5606,
				0.6261,
				0.6917,
				0.7572,
				0.79
				]
    interf_ljets_5j_ge3t_ttHbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttHbb_node)
    
    interf_ljets_5j_ge3t_ttZbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttZbb",
                                            label          = "ljets_5j_ge3t_ttZbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))")
    interf_ljets_5j_ge3t_ttZbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttZbb_node","")
    interf_ljets_5j_ge3t_ttZbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttZbb_node.bin_edges = [ 
				0.16,
				0.24,
				0.32,
				0.4,
				0.48,
				0.56,
				0.64,
				0.72,
				0.8,
				0.88,
				0.92
				]
    interf_ljets_5j_ge3t_ttZbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttZbb_node)
    
    interf_ljets_5j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttbb",
                                            label          = "ljets_5j_ge3t_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))")
    interf_ljets_5j_ge3t_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_ttbb_node","")
    interf_ljets_5j_ge3t_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttbb_node.bin_edges = [ 
				0.1644,
				0.2356,
				0.3067,
				0.3778,
				0.4489,
				0.52,
				0.5911,
				0.6622,
				0.7333,
				0.8044,
				0.84
				]
    interf_ljets_5j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttbb_node)
    
    interf_ljets_5j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttcc",
                                            label          = "ljets_5j_ge3t_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))")
    interf_ljets_5j_ge3t_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttcc_node","")
    interf_ljets_5j_ge3t_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttcc_node.bin_edges = [ 
				0.175,
				0.225,
				0.275,
				0.325,
				0.375,
				0.425,
				0.475,
				0.525,
				0.575,
				0.625,
				0.65
				]
    interf_ljets_5j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttcc_node)
    
    interf_ljets_5j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttlf",
                                            label          = "ljets_5j_ge3t_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))")
    interf_ljets_5j_ge3t_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttlf_node","")
    interf_ljets_5j_ge3t_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttlf_node.bin_edges = [ 
				0.1756,
				0.2244,
				0.2733,
				0.3222,
				0.3711,
				0.42,
				0.4689,
				0.5178,
				0.5667,
				0.6156,
				0.64
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
    