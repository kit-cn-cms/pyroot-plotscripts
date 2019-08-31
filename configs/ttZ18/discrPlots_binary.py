
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import ROOT
from array import array
from copy import deepcopy


memexp = ""



def plots_dnn(data, discrname):

    ndefaultbins = 50
    category_dict = {}
    this_dict = {}

    # plots for ge4j_ge3t_ttH_tthf_bkg

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttH_tthf_bkg==0))","ljets_ge4j_ge3t_ttH_tthf_bkg_binary_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttH_tthf_bkg"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = -1.0
    category_dict["maxxval"] = 1.0

    this_dict["ljets_ge4j_ge3t_ttH_tthf_bkg_binary_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge3t_ttH_bkg

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttH_bkg==0))","ljets_ge4j_ge3t_ttH_bkg_binary_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttH_bkg"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = -1.0
    category_dict["maxxval"] = 1.0

    this_dict["ljets_ge4j_ge3t_ttH_bkg_binary_node"] = deepcopy(category_dict)
    category_dict.clear()



    
    # plots for ge6j_ge3t_ttH_tthf_bkg

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttH_tthf_bkg==0))","ljets_ge6j_ge3t_ttH_tthf_bkg_binary_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttH_tthf_bkg"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = -1.0
    category_dict["maxxval"] = 1.0

    this_dict["ljets_ge6j_ge3t_ttH_tthf_bkg_binary_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge3t_ttH_bkg

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttH_bkg==0))","ljets_ge6j_ge3t_ttH_bkg_binary_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttH_bkg"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = -1.0
    category_dict["maxxval"] = 1.0

    this_dict["ljets_ge6j_ge3t_ttH_bkg_binary_node"] = deepcopy(category_dict)
    category_dict.clear()



    # plots for ge4j_ge4t_ttH_tthf_bkg

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttH_tthf_bkg==0))","ljets_ge4j_ge4t_ttH_tthf_bkg_binary_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttH_tthf_bkg"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = -1.0
    category_dict["maxxval"] = 1.0

    this_dict["ljets_ge4j_ge4t_ttH_tthf_bkg_binary_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge4t_ttH_bkg

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t_ttH_bkg==0))","ljets_ge4j_ge4t_ttH_bkg_binary_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_ttH_bkg"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = -1.0
    category_dict["maxxval"] = 1.0

    this_dict["ljets_ge4j_ge4t_ttH_bkg_binary_node"] = deepcopy(category_dict)
    category_dict.clear()


    for l in this_dict:
        this_dict[l]["histoname"] = discrname+"_"+l
        this_dict[l]["histotitle"] = "final discriminator ({})".format(l)
        this_dict[l]["plotPreselections"] = this_dict[l]["category"][0]

    DNNPlots = init_plots(dictionary = this_dict, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def init_plots(dictionary, data = None):
    plots = [] #init list of plotClasses objects to return
    for label in dictionary:
        subdict     = dictionary[label] #for easy access
        discr       = subdict["discr"] # load discriminator name
        sel         = subdict["plotPreselections"] # load selection
        histoname   = subdict["histoname"] # load histogram name
        histotitle  = subdict["histotitle"] # load histogram title
        catlabel    = subdict["catlabel"] # category label

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if "bin_edges" in subdict:
            bins  = array("f", subdict["bin_edges"])
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            subdict["nhistobins"] = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname,histotitle,nbins,bins),
                    discr,sel,catlabel))

        elif "minxval" in subdict and "maxxval" in subdict:
            nbins = subdict["nhistobins"]
            xmax  = subdict["maxxval"]
            xmin  = subdict["minxval"]
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname, histotitle,nbins,xmin, xmax),
                    discr,sel,catlabel))

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    
