
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


    # plots for ge6j_ge3t

    interf_ljets_ge6j_ge3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttH",
                                            label          = "ljets_ge6j_ge3t_ttH_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==0))")
    interf_ljets_ge6j_ge3t_ttH_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttH_node","")
    interf_ljets_ge6j_ge3t_ttH_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttH_node.bin_edges = [ 
				0.1754,
				0.3725,
				0.4711,
				0.5696,
				0.6682,
				0.8654
				]
    interf_ljets_ge6j_ge3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttH_node)
    
    interf_ljets_ge6j_ge3t_ttZ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttZ",
                                            label          = "ljets_ge6j_ge3t_ttZ_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))")
    interf_ljets_ge6j_ge3t_ttZ_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttZ_node","")
    interf_ljets_ge6j_ge3t_ttZ_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttZ_node.bin_edges = [ 
				0.1789,
				0.2632,
				0.3475,
				0.4318,
				0.4739,
				0.5161,
				0.5582,
				0.6004,
				0.6425,
				0.7689
				]
    interf_ljets_ge6j_ge3t_ttZ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttZ_node)
    
    interf_ljets_ge6j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttbb",
                                            label          = "ljets_ge6j_ge3t_ttbb_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))")
    interf_ljets_ge6j_ge3t_ttbb_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_ttbb_node","")
    interf_ljets_ge6j_ge3t_ttbb_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttbb_node.bin_edges = [ 
				0.1814,
				0.33,
				0.4043,
				0.4786,
				0.5529,
				0.7014
				]
    interf_ljets_ge6j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttbb_node)
    
    interf_ljets_ge6j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttcc",
                                            label          = "ljets_ge6j_ge3t_ttcc_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))")
    interf_ljets_ge6j_ge3t_ttcc_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttcc_node","")
    interf_ljets_ge6j_ge3t_ttcc_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttcc_node.bin_edges = [ 
				0.1871,
				0.5471
				]
    interf_ljets_ge6j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttcc_node)
    
    interf_ljets_ge6j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge6j_ge3t_node_ttlf",
                                            label          = "ljets_ge6j_ge3t_ttlf_node",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))")
    interf_ljets_ge6j_ge3t_ttlf_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttlf_node","")
    interf_ljets_ge6j_ge3t_ttlf_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_ttlf_node.bin_edges = [ 
				0.1814,
				0.7014
				]
    interf_ljets_ge6j_ge3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_ttlf_node)
    


    # plots for 4j_ge3t

    interf_ljets_4j_ge3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttH",
                                            label          = "ljets_4j_ge3t_ttH_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==0))")
    interf_ljets_4j_ge3t_ttH_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==0))","ljets_4j_ge3t_ttH_node","")
    interf_ljets_4j_ge3t_ttH_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttH_node.bin_edges = [ 
				0.1779,
				0.355,
				0.4436,
				0.5321,
				0.6207,
				0.7979
				]
    interf_ljets_4j_ge3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttH_node)
    
    interf_ljets_4j_ge3t_ttZ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttZ",
                                            label          = "ljets_4j_ge3t_ttZ_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))")
    interf_ljets_4j_ge3t_ttZ_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttZ_node","")
    interf_ljets_4j_ge3t_ttZ_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttZ_node.bin_edges = [ 
				0.1714,
				0.2857,
				0.4,
				0.5143,
				0.5714,
				0.6286,
				0.6857,
				0.7429,
				0.8,
				0.9714
				]
    interf_ljets_4j_ge3t_ttZ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttZ_node)
    
    interf_ljets_4j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttbb",
                                            label          = "ljets_4j_ge3t_ttbb_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))")
    interf_ljets_4j_ge3t_ttbb_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_ttbb_node","")
    interf_ljets_4j_ge3t_ttbb_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttbb_node.bin_edges = [ 
				0.1779,
				0.355,
				0.4436,
				0.5321,
				0.6207,
				0.7979
				]
    interf_ljets_4j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttbb_node)
    
    interf_ljets_4j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttcc",
                                            label          = "ljets_4j_ge3t_ttcc_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))")
    interf_ljets_4j_ge3t_ttcc_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttcc_node","")
    interf_ljets_4j_ge3t_ttcc_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttcc_node.bin_edges = [ 
				0.1879,
				0.5279
				]
    interf_ljets_4j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttcc_node)
    
    interf_ljets_4j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_4j_ge3t_node_ttlf",
                                            label          = "ljets_4j_ge3t_ttlf_node",
                                            selection      = "((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))")
    interf_ljets_4j_ge3t_ttlf_node.category = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttlf_node","")
    interf_ljets_4j_ge3t_ttlf_node.category_label = "4 jets, \geq 3 b-tags"
    interf_ljets_4j_ge3t_ttlf_node.bin_edges = [ 
				0.1832,
				0.6532
				]
    interf_ljets_4j_ge3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_4j_ge3t_ttlf_node)
    


    # plots for 5j_ge3t

    interf_ljets_5j_ge3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttH",
                                            label          = "ljets_5j_ge3t_ttH_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==0))")
    interf_ljets_5j_ge3t_ttH_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==0))","ljets_5j_ge3t_ttH_node","")
    interf_ljets_5j_ge3t_ttH_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttH_node.bin_edges = [ 
				0.1786,
				0.35,
				0.4357,
				0.5214,
				0.6071,
				0.7786
				]
    interf_ljets_5j_ge3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttH_node)
    
    interf_ljets_5j_ge3t_ttZ_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttZ",
                                            label          = "ljets_5j_ge3t_ttZ_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))")
    interf_ljets_5j_ge3t_ttZ_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttZ_node","")
    interf_ljets_5j_ge3t_ttZ_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttZ_node.bin_edges = [ 
				0.1732,
				0.2804,
				0.3875,
				0.4946,
				0.5482,
				0.6018,
				0.6554,
				0.7089,
				0.7625,
				0.9232
				]
    interf_ljets_5j_ge3t_ttZ_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttZ_node)
    
    interf_ljets_5j_ge3t_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttbb",
                                            label          = "ljets_5j_ge3t_ttbb_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))")
    interf_ljets_5j_ge3t_ttbb_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_ttbb_node","")
    interf_ljets_5j_ge3t_ttbb_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttbb_node.bin_edges = [ 
				0.1793,
				0.345,
				0.4279,
				0.5107,
				0.5936,
				0.7593
				]
    interf_ljets_5j_ge3t_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttbb_node)
    
    interf_ljets_5j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttcc",
                                            label          = "ljets_5j_ge3t_ttcc_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))")
    interf_ljets_5j_ge3t_ttcc_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttcc_node","")
    interf_ljets_5j_ge3t_ttcc_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttcc_node.bin_edges = [ 
				0.1879,
				0.5279
				]
    interf_ljets_5j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_5j_ge3t_ttcc_node)
    
    interf_ljets_5j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_5j_ge3t_node_ttlf",
                                            label          = "ljets_5j_ge3t_ttlf_node",
                                            selection      = "((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))")
    interf_ljets_5j_ge3t_ttlf_node.category = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttlf_node","")
    interf_ljets_5j_ge3t_ttlf_node.category_label = "5 jets, \geq 3 b-tags"
    interf_ljets_5j_ge3t_ttlf_node.bin_edges = [ 
				0.1814,
				0.7014
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
    