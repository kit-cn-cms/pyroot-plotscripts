
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

def getDNNclass(cla):
    return "((N_Jets>=4&&N_BTagsM>=4)*(DNNPredictedClass_ge4j_ge4t_classification=={}) + ((N_Jets>=4&&N_BTagsM==3)*(DNNPredictedClass_ge4j_3t_classification=={})) )".format(cla, cla)

def getDNNoutput(cla):
    return "((N_Jets>=4&&N_BTagsM>=4)*(DNNOutput_ge4j_ge4t_classification_node_{}) + ((N_Jets>=4&&N_BTagsM==3)*(DNNOutput_ge4j_3t_classification_node_{})) )".format(cla, cla)


def plots_dnn_v2(data, discrname, jt_selection, jt_label):

    ndefaultbins = 50
    interfaces = []

    interf_classification_ttH_ttmb_node = vhi.variableHistoInterface(variable_name  = "(" + getDNNoutput("ttH") + "/ (" + getDNNoutput("ttH") + "+" + getDNNoutput("ttmb") + "+" + getDNNoutput("tt2b") + "))" ,
                                            label          = "ljets_"+jt_label+"_classification_ttH_ttmb_vs_slike",
                                            selection      = "()" )
    interf_classification_ttH_ttmb_node.category = ("((" + getDNNclass(0) + "||" + getDNNclass(1) + ")" + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttH_ttmb_node","")
    interf_classification_ttH_ttmb_node.category_label = jt_label
    interf_classification_ttH_ttmb_node.minxval = 0.2
    interf_classification_ttH_ttmb_node.maxxval = 1.0
    interf_classification_ttH_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_ttH_ttmb_node)

    interf_classification_ttH_node = vhi.variableHistoInterface(variable_name  =  getDNNoutput("ttH") ,
                                            label          = "ljets_"+jt_label+"_classification_ttH_vs_slike",
                                            selection      = "()" )
    interf_classification_ttH_node.category = ("((" + getDNNclass(0) + ")" + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttH__node","")
    interf_classification_ttH_node.category_label = jt_label
    interf_classification_ttH_node.minxval = 0.14
    interf_classification_ttH_node.maxxval = 0.88
    interf_classification_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_ttH_node)

    interf_classification_ttmb_node = vhi.variableHistoInterface(variable_name  =  getDNNoutput("ttH") ,
                                            label          = "ljets_"+jt_label+"_classification_ttH_vs_slike",
                                            selection      = "()" )
    interf_classification_ttmb_node.category = ("((" + getDNNclass(1) + ")" + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttH__node","")
    interf_classification_ttmb_node.category_label = jt_label
    interf_classification_ttmb_node.minxval = 0.14
    interf_classification_ttmb_node.maxxval = 0.79
    interf_classification_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_ttmb_node)

    interf_classification_tt2b_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("tt2b"),
                                            label          = "ljets_"+jt_label+"_classification_tt2b_node",
                                            selection      = "()" )
    interf_classification_tt2b_node.category = ("(" + getDNNclass(2) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_tt2b_node","")
    interf_classification_tt2b_node.category_label = jt_label
    interf_classification_tt2b_node.minxval = 0.14
    interf_classification_tt2b_node.maxxval = 0.71
    interf_classification_tt2b_node.nhistobins = 1
    interfaces.append(interf_classification_tt2b_node)


    interf_classification_ttcc_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("ttcc"),
                                            label          = "ljets_"+jt_label+"_classification_ttcc_node",
                                            selection      = "()" )
    interf_classification_ttcc_node.category = ("(" + getDNNclass(3) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttcc_node","")
    interf_classification_ttcc_node.category_label = jt_label
    interf_classification_ttcc_node.minxval = 0.14
    interf_classification_ttcc_node.maxxval = 0.51
    interf_classification_ttcc_node.nhistobins = 1
    interfaces.append(interf_classification_ttcc_node)


    interf_classification_ttlf_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("ttlf"),
                                            label          = "ljets_"+jt_label+"_classification_ttlf_node",
                                            selection      = "()" )
    interf_classification_ttlf_node.category = ("(" + getDNNclass(4) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttlf_node","")
    interf_classification_ttlf_node.category_label = jt_label
    interf_classification_ttlf_node.minxval = 0.14
    interf_classification_ttlf_node.maxxval = 0.78
    interf_classification_ttlf_node.nhistobins = 1
    interfaces.append(interf_classification_ttlf_node)

    interf_classification_tHq_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("tHq"),
                                            label          = "ljets_"+jt_label+"_classification_tHq_node",
                                            selection      = "()" )
    interf_classification_tHq_node.category = ("(" + getDNNclass(5) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_tHq_node","")
    interf_classification_tHq_node.category_label = jt_label
    interf_classification_tHq_node.minxval = 0.14
    interf_classification_tHq_node.maxxval = 1.0
    interf_classification_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_tHq_node)

    interf_classification_tHW_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("tHW"),
                                            label          = "ljets_"+jt_label+"_classification_tHW_node",
                                            selection      = "()" )
    interf_classification_tHW_node.category = ("(" + getDNNclass(6) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_tHW_node","")
    interf_classification_tHW_node.category_label = jt_label
    interf_classification_tHW_node.minxval = 0.14
    interf_classification_tHW_node.maxxval = 1.0
    interf_classification_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_tHW_node)

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0] 

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots














def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_dnn_v2(data, discrname, "(N_Jets>=5&&N_BTagsM==3)", "ge5j_3t")
    discriminatorPlots += plots_dnn_v2(data, discrname, "(N_Jets>=5&&N_BTagsM>=4)", "ge5j_ge3t")
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
    
