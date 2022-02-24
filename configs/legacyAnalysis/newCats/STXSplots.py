
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


memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'

def getDNNclass(cla):
    return "((N_Jets==5&&N_BTagsM>=4)*(DNNPredictedClass_5j_ge4t_classification=={}) + ((N_Jets>=6&&N_BTagsM>=4)*(DNNPredictedClass_ge6j_ge4t_classification=={})) )".format(cla, cla)

def getDNNoutput(cla):
    return "((N_Jets==5&&N_BTagsM>=4)*(DNNOutput_5j_ge4t_classification_node_{}) + ((N_Jets>=6&&N_BTagsM>=4)*(DNNOutput_ge6j_ge4t_classification_node_{})) )".format(cla, cla)

def plots_dnn_ttH_vs_slike_STXS(data, discrname, cat_classifier, cat_stxs, stxsproc, index, selection, label):
    ndefaultbins = 50
    interfaces = []

    # interf_ttH_vs_slike = vhi.variableHistoInterface(variable_name  = "(DNNOutput_{cat}_node_ttH/(DNNOutput_{cat}_node_ttH + DNNOutput_{cat}_node_ttmb + DNNOutput_{cat}_node_tt2b))*DNNOutput_{cat_stxs}_node_{stxsproc}".format(cat = cat_classifier, cat_stxs = cat_stxs, stxsproc = stxsproc),
    #                                         label          = "ljets_{cat}_ttH_vs_slike_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),
    #                                         selection      = "")
    # interf_ttH_vs_slike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==0)&&(DNNPredictedClass_{cat_stxs}=={index}))".format(cat = cat_classifier, cat_stxs = cat_stxs, sel = selection, index = str(index)),"ljets_{cat}_ttH_vs_slike_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),"")
    # interf_ttH_vs_slike.category_label = label
    # interf_ttH_vs_slike.minxval = 0.2
    # interf_ttH_vs_slike.maxxval = 1.0
    # interf_ttH_vs_slike.nhistobins = ndefaultbins
    # interfaces.append(interf_ttH_vs_slike)


    interf_ttH_ttmb_vs_slike = vhi.variableHistoInterface(variable_name  = "(DNNOutput_{cat}_node_ttH/(DNNOutput_{cat}_node_ttH + DNNOutput_{cat}_node_ttmb + DNNOutput_{cat}_node_tt2b))*DNNOutput_{cat_stxs}_node_{stxsproc}".format(cat = cat_classifier, cat_stxs = cat_stxs, stxsproc = stxsproc),
                                            label          = "ljets_{cat}_ttH_ttmb_vs_slike_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),
                                            selection      = "")
    interf_ttH_ttmb_vs_slike.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==0 || DNNPredictedClass_{cat}==1)&&(DNNPredictedClass_{cat_stxs}=={index}))".format(cat = cat_classifier, sel = selection, cat_stxs = cat_stxs, index = str(index)),"ljets_{cat}_ttH_ttmb_vs_slike_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),"")
    interf_ttH_ttmb_vs_slike.category_label = label
    interf_ttH_ttmb_vs_slike.minxval = 0.0
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

def plots_dnn_ttH_times_STXS(data, discrname, cat_classifier, cat_stxs, stxsproc, index, selection, label):
    ndefaultbins = 50
    interfaces = []

    interf_ttH_times_STXS = vhi.variableHistoInterface(variable_name  = "(DNNOutput_{cat}_node_ttH)*DNNOutput_{cat_stxs}_node_{stxsproc}".format(cat = cat_classifier, cat_stxs = cat_stxs, stxsproc = stxsproc),
                                            label          = "ljets_{cat}_ttH_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),
                                            selection      = "")
    interf_ttH_times_STXS.category = ("({sel}&&(1.)&&(DNNPredictedClass_{cat}==0)&&(DNNPredictedClass_{cat_stxs}=={index}))".format(cat = cat_classifier, sel = selection, cat_stxs = cat_stxs, index = str(index)),"ljets_{cat}_ttH_times_{stxsproc}".format(cat = cat_classifier, stxsproc = stxsproc),"")
    interf_ttH_times_STXS.category_label = label
    interf_ttH_times_STXS.minxval = 0.0
    interf_ttH_times_STXS.maxxval = 1.0
    interf_ttH_times_STXS.nhistobins = ndefaultbins
    interfaces.append(interf_ttH_times_STXS)

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots	


def plots_dnn(data, discrname, jt_selection, jt_label):

    ndefaultbins = 50
    interfaces = []

    interf_classification_ttH_ttmb_node = vhi.variableHistoInterface(variable_name  = "(" + getDNNoutput("ttH") + "/ (" + getDNNoutput("ttH") + "+" + getDNNoutput("ttmb") + "+" + getDNNoutput("tt2b") + "))" ,
                                            label          = "ljets_"+jt_label+"_classification_ttH_ttmb_vs_slike",
                                            selection      = "()" )
    interf_classification_ttH_ttmb_node.category = ("((" + getDNNclass(0) + "||" + getDNNclass(1) + ")" + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttH_ttmb_node","")
    interf_classification_ttH_ttmb_node.category_label = jt_label
    interf_classification_ttH_ttmb_node.minxval = 0.0
    interf_classification_ttH_ttmb_node.maxxval = 1.0
    interf_classification_ttH_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_ttH_ttmb_node)

    interf_classification_ttH_node = vhi.variableHistoInterface(variable_name  =  getDNNoutput("ttH") ,
                                            label          = "ljets_"+jt_label+"_classification_ttH_node",
                                            selection      = "()" )
    interf_classification_ttH_node.category = ("((" + getDNNclass(0) + ")" + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttH__node","")
    interf_classification_ttH_node.category_label = jt_label
    interf_classification_ttH_node.minxval = 0.0
    interf_classification_ttH_node.maxxval = 1.0
    interf_classification_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_ttH_node)

    interf_classification_ttmb_node = vhi.variableHistoInterface(variable_name  =  getDNNoutput("ttmb") ,
                                            label          = "ljets_"+jt_label+"_classification_ttmb_node",
                                            selection      = "()" )
    interf_classification_ttmb_node.category = ("((" + getDNNclass(1) + ")" + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttH__node","")
    interf_classification_ttmb_node.category_label = jt_label
    interf_classification_ttmb_node.minxval = 0.0
    interf_classification_ttmb_node.maxxval = 1.0
    interf_classification_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_ttmb_node)

    interf_classification_tt2b_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("tt2b"),
                                            label          = "ljets_"+jt_label+"_classification_tt2b_node",
                                            selection      = "()" )
    interf_classification_tt2b_node.category = ("(" + getDNNclass(2) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_tt2b_node","")
    interf_classification_tt2b_node.category_label = jt_label
    interf_classification_tt2b_node.minxval = 0.0
    interf_classification_tt2b_node.maxxval = 1.0
    interf_classification_tt2b_node.nhistobins = 1
    interfaces.append(interf_classification_tt2b_node)


    interf_classification_ttcc_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("ttcc"),
                                            label          = "ljets_"+jt_label+"_classification_ttcc_node",
                                            selection      = "()" )
    interf_classification_ttcc_node.category = ("(" + getDNNclass(3) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttcc_node","")
    interf_classification_ttcc_node.category_label = jt_label
    interf_classification_ttcc_node.minxval = 0.0
    interf_classification_ttcc_node.maxxval = 1.0
    interf_classification_ttcc_node.nhistobins = 1
    interfaces.append(interf_classification_ttcc_node)


    interf_classification_ttlf_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("ttlf"),
                                            label          = "ljets_"+jt_label+"_classification_ttlf_node",
                                            selection      = "()" )
    interf_classification_ttlf_node.category = ("(" + getDNNclass(4) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_ttlf_node","")
    interf_classification_ttlf_node.category_label = jt_label
    interf_classification_ttlf_node.minxval = 0.0
    interf_classification_ttlf_node.maxxval = 1.0
    interf_classification_ttlf_node.nhistobins = 1
    interfaces.append(interf_classification_ttlf_node)

    interf_classification_tHq_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("tHq"),
                                            label          = "ljets_"+jt_label+"_classification_tHq_node",
                                            selection      = "()" )
    interf_classification_tHq_node.category = ("(" + getDNNclass(5) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_tHq_node","")
    interf_classification_tHq_node.category_label = jt_label
    interf_classification_tHq_node.minxval = 0.0
    interf_classification_tHq_node.maxxval = 1.0
    interf_classification_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_classification_tHq_node)

    interf_classification_tHW_node = vhi.variableHistoInterface(variable_name  = getDNNoutput("tHW"),
                                            label          = "ljets_"+jt_label+"_classification_tHW_node",
                                            selection      = "()" )
    interf_classification_tHW_node.category = ("(" + getDNNclass(6) + "&&(" + jt_selection +"))","ljets_"+jt_label+"_classification_tHW_node","")
    interf_classification_tHW_node.category_label = jt_label
    interf_classification_tHW_node.minxval = 0.0
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
    # input variables
    label = "5 jets, \geq 4 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=4)"
    # STXS
    discriminatorPlots += plots_dnn_ttH_times_STXS(data = data, discrname=discrname, cat_classifier="5j_ge4t_classification", cat_stxs = "5j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_0", index = 0, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_times_STXS(data = data, discrname=discrname, cat_classifier="5j_ge4t_classification", cat_stxs = "5j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_1", index = 1, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_times_STXS(data = data, discrname=discrname, cat_classifier="5j_ge4t_classification", cat_stxs = "5j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_2", index = 2, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_times_STXS(data = data, discrname=discrname, cat_classifier="5j_ge4t_classification", cat_stxs = "5j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_3", index = 3, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_times_STXS(data = data, discrname=discrname, cat_classifier="5j_ge4t_classification", cat_stxs = "5j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_4", index = 4, selection = selection, label = label )

    label = "\geq 6 jets, \geq 4 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=4)"
    # STXS
    discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge6j_ge4t_classification", cat_stxs = "ge6j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_0", index = 0, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge6j_ge4t_classification", cat_stxs = "ge6j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_1", index = 1, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge6j_ge4t_classification", cat_stxs = "ge6j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_2", index = 2, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge6j_ge4t_classification", cat_stxs = "ge6j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_3", index = 3, selection = selection, label = label )
    discriminatorPlots += plots_dnn_ttH_vs_slike_STXS(data = data, discrname=discrname, cat_classifier="ge6j_ge4t_classification", cat_stxs = "ge6j_ge4t_STXSnet", stxsproc = "ttHbb_STXS_4", index = 4, selection = selection, label = label )


    # standard classifiers
    discriminatorPlots += plots_dnn(data, discrname, "(N_Jets==5&&N_BTagsM>=4)", "5j_ge4t")
    discriminatorPlots += plots_dnn(data, discrname, "(N_Jets>=6&&N_BTagsM>=4)", "ge6j_ge4t")

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
    
