
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


    # plots for ge4j_ge4t_classifier

    interf_ljets_ge4j_ge4t_classifier_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_ttH",
                                            label          = "ljets_ge4j_ge4t_classifier_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==0))")
    interf_ljets_ge4j_ge4t_classifier_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==0))","ljets_ge4j_ge4t_classifier_ttH_node","")
    interf_ljets_ge4j_ge4t_classifier_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_ttH_node.bin_edges = [ 
				0.1927,
				0.2453,
				0.298,
				0.3507,
				0.4033,
				0.456,
				0.5087,
				0.5613,
				0.614,
				0.93
				]
    interf_ljets_ge4j_ge4t_classifier_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_ttH_node)
    
    interf_ljets_ge4j_ge4t_classifier_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_ttmb",
                                            label          = "ljets_ge4j_ge4t_classifier_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==1))")
    interf_ljets_ge4j_ge4t_classifier_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==1))","ljets_ge4j_ge4t_classifier_ttmb_node","")
    interf_ljets_ge4j_ge4t_classifier_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_ttmb_node.bin_edges = [ 
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
				0.5727,
				0.73
				]
    interf_ljets_ge4j_ge4t_classifier_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_ttmb_node)
    
    interf_ljets_ge4j_ge4t_classifier_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_classifier_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==2))")
    interf_ljets_ge4j_ge4t_classifier_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==2))","ljets_ge4j_ge4t_classifier_tt2b_node","")
    interf_ljets_ge4j_ge4t_classifier_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_tt2b_node.bin_edges = [ 
				0.1827,
				# 0.204,
				# 0.2253,
				# 0.2467,
				# 0.268,
				# 0.2893,
				# 0.3107,
				# 0.332,
				# 0.3533,
				# 0.3747,
				0.46
				]
    interf_ljets_ge4j_ge4t_classifier_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_tt2b_node)
    
    interf_ljets_ge4j_ge4t_classifier_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_classifier_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==3))")
    interf_ljets_ge4j_ge4t_classifier_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==3))","ljets_ge4j_ge4t_classifier_ttcc_node","")
    interf_ljets_ge4j_ge4t_classifier_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_ttcc_node.bin_edges = [ 
				0.1747,
				# 0.2093,
				# 0.244,
				# 0.2787,
				# 0.3133,
				# 0.348,
				# 0.3827,
				0.66
				]
    interf_ljets_ge4j_ge4t_classifier_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_ttcc_node)
    
    interf_ljets_ge4j_ge4t_classifier_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_classifier_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==4))")
    interf_ljets_ge4j_ge4t_classifier_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==4))","ljets_ge4j_ge4t_classifier_ttlf_node","")
    interf_ljets_ge4j_ge4t_classifier_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_ttlf_node.bin_edges = [ 
				0.1753,
				# 0.2107,
				# 0.246,
				# 0.2813,
				# 0.3167,
				# 0.352,
				# 0.3873,
				# 0.4227,
				# 0.458,
				# 0.4933,
				# 0.5287,
				# 0.564,
				0.67
				]
    interf_ljets_ge4j_ge4t_classifier_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_ttlf_node)
    
    interf_ljets_ge4j_ge4t_classifier_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_tHq",
                                            label          = "ljets_ge4j_ge4t_classifier_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==5))")
    interf_ljets_ge4j_ge4t_classifier_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==5))","ljets_ge4j_ge4t_classifier_tHq_node","")
    interf_ljets_ge4j_ge4t_classifier_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_tHq_node.bin_edges = [ 
				0.196,
				0.252,
				0.308,
				0.364,
				0.42,
				0.476,
				0.532,
				0.588,
				0.644,
				0.7,
				0.756,
				0.98
				]
    interf_ljets_ge4j_ge4t_classifier_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_tHq_node)
    
    interf_ljets_ge4j_ge4t_classifier_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_classifier_node_tHW",
                                            label          = "ljets_ge4j_ge4t_classifier_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==6))")
    interf_ljets_ge4j_ge4t_classifier_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t_classifier==6))","ljets_ge4j_ge4t_classifier_tHW_node","")
    interf_ljets_ge4j_ge4t_classifier_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_classifier_tHW_node.bin_edges = [ 
				0.1973,
				0.2547,
				0.312,
				0.3693,
				0.4267,
				0.484,
				0.5413,
				0.5987,
				0.7133,
				1.0
				]
    interf_ljets_ge4j_ge4t_classifier_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_classifier_tHW_node)
    

    # plots for ge4j_3t_classifier

    interf_ljets_ge4j_3t_classifier_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_ttH",
                                            label          = "ljets_ge4j_3t_classifier_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==0))")
    interf_ljets_ge4j_3t_classifier_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==0))","ljets_ge4j_3t_classifier_ttH_node","")
    interf_ljets_ge4j_3t_classifier_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_ttH_node.bin_edges = [ 
				0.14,
				0.19,
				0.24,
				0.29,
				0.34,
				0.39,
				0.44,
				0.49,
				0.54,
				0.89
				]
    interf_ljets_ge4j_3t_classifier_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_ttH_node)
    
    interf_ljets_ge4j_3t_classifier_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_ttmb",
                                            label          = "ljets_ge4j_3t_classifier_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==1))")
    interf_ljets_ge4j_3t_classifier_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==1))","ljets_ge4j_3t_classifier_ttmb_node","")
    interf_ljets_ge4j_3t_classifier_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_ttmb_node.bin_edges = [ 
				0.1667,
				0.1933,
				0.22,
				0.2467,
				0.2733,
				0.3,
				0.3267,
				0.3533,
				0.38,
				0.4067,
				0.54
				]
    interf_ljets_ge4j_3t_classifier_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_ttmb_node)
    
    interf_ljets_ge4j_3t_classifier_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_tt2b",
                                            label          = "ljets_ge4j_3t_classifier_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==2))")
    interf_ljets_ge4j_3t_classifier_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==2))","ljets_ge4j_3t_classifier_tt2b_node","")
    interf_ljets_ge4j_3t_classifier_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_tt2b_node.bin_edges = [ 
				0.14,
				# 0.1747,
				# 0.2093,
				# 0.244,
				# 0.2787,
				# 0.3133,
				# 0.348,
				# 0.3827,
				# 0.4173,
				# 0.452,
				# 0.4867,
				0.66
				]
    interf_ljets_ge4j_3t_classifier_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_tt2b_node)
    
    interf_ljets_ge4j_3t_classifier_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_ttcc",
                                            label          = "ljets_ge4j_3t_classifier_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==3))")
    interf_ljets_ge4j_3t_classifier_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==3))","ljets_ge4j_3t_classifier_ttcc_node","")
    interf_ljets_ge4j_3t_classifier_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_ttcc_node.bin_edges = [ 
				0.14,
				# 0.174,
				# 0.208,
				# 0.242,
				# 0.276,
				# 0.31,
				# 0.344,
				# 0.378,
				# 0.412,
				# 0.446,
				# 0.48,
				# 0.514,
				0.65
				]
    interf_ljets_ge4j_3t_classifier_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_ttcc_node)
    
    interf_ljets_ge4j_3t_classifier_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_ttlf",
                                            label          = "ljets_ge4j_3t_classifier_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==4))")
    interf_ljets_ge4j_3t_classifier_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==4))","ljets_ge4j_3t_classifier_ttlf_node","")
    interf_ljets_ge4j_3t_classifier_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_ttlf_node.bin_edges = [ 
				0.14,
				# 0.1827,
				# 0.2253,
				# 0.268,
				# 0.3107,
				# 0.3533,
				# 0.396,
				# 0.4387,
				# 0.4813,
				# 0.524,
				# 0.5667,
				# 0.6093,
				# 0.652,
				# 0.6947,
				0.78
				]
    interf_ljets_ge4j_3t_classifier_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_ttlf_node)
    
    interf_ljets_ge4j_3t_classifier_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_tHq",
                                            label          = "ljets_ge4j_3t_classifier_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==5))")
    interf_ljets_ge4j_3t_classifier_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==5))","ljets_ge4j_3t_classifier_tHq_node","")
    interf_ljets_ge4j_3t_classifier_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_tHq_node.bin_edges = [ 
				0.14,
				0.1933,
				0.2467,
				0.3,
				0.3533,
				0.4067,
				0.46,
				0.5133,
				0.5667,
				0.62,
				0.6733,
				0.7267,
				0.78,
				0.94
				]
    interf_ljets_ge4j_3t_classifier_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_tHq_node)
    
    interf_ljets_ge4j_3t_classifier_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_classifier_node_tHW",
                                            label          = "ljets_ge4j_3t_classifier_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==6))")
    interf_ljets_ge4j_3t_classifier_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t_classifier==6))","ljets_ge4j_3t_classifier_tHW_node","")
    interf_ljets_ge4j_3t_classifier_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_ge4j_3t_classifier_tHW_node.bin_edges = [ 
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
				1.0
				]
    interf_ljets_ge4j_3t_classifier_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_classifier_tHW_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots_CPScan(interfaces = interfaces, data = data, discrname = discrname)
    return DNNPlots

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots

def init_plots_CPScan(interfaces, data = None, discrname = ''):
    plots = [] #init list of plotClasses objects to return
    for interf in interfaces:
        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used
        # Kappa Scan 
        # points = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,20,21,23,24,26,27,29,30,32,34,35,37,47,49,50]
        # CP SCAN
        points = range (50,70) + [0,12]
        for i in points:
            histoname = "P"+str(i)+'_'+discrname+"_"+interf.label
            histotitle = interf.histotitle
            if i !=0:
                weight = "*(Weight_rwgt_{}/Weight_GEN_nom)".format(i)
            else:
                weight = "*(1)"

            if not interf.bin_edges is None:
                bins  = array("f", interf.bin_edges)
                nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
                interf.nhistobins = nbins # update number of bins
                plots.append(
                    plotClasses.Plot(
                        histo = ROOT.TH1F(histoname,histotitle,nbins,bins),
                        variable = interf.varname,
                        selection = interf.selection + weight,
                        label= interf.category_label))
            elif not (interf.minxval is None or interf.maxxval is None):
                nbins = interf.nhistobins
                xmax  = interf.maxxval
                xmin  = interf.minxval
                plots.append(
                    plotClasses.Plot(
                        histo = ROOT.TH1F(histoname,histotitle,nbins,xmin, xmax),
                        variable = interf.varname,
                        selection = interf.selection + weight,
                        label = interf.category_label))
            else:
                print("FATAL ERROR: Unable to load bin edges or min/max values for histogram!")
                print(interf)
                raise ValueError
    return plots
	
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
    