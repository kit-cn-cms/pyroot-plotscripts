
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

    ndefaultbins = 14
    category_dict = {}
    this_dict = {}




    # plots for ge6j_ge3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttZ"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1715,
				0.2854,
				0.3992,
				0.5131,
				0.57,
				0.6269,
				0.6838,
				0.7408,
				0.7977,
				0.94
				]
    this_dict["ljets_ge6j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttH"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1773,
				0.3588,
				0.4496,
				0.5404,
				0.6312,
				0.79
				]
    this_dict["ljets_ge6j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttbb"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1762,
				0.3669,
				0.4623,
				0.5577,
				0.6531,
				0.82
				]
    this_dict["ljets_ge6j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttcc"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1815,
				0.68
				]
    this_dict["ljets_ge6j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttlf"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1819,
				0.67
				]
    this_dict["ljets_ge6j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 5j_ge3t

    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==0))","ljets_5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttZ"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1762,
				0.2715,
				0.3669,
				0.4623,
				0.51,
				0.5577,
				0.6054,
				0.6531,
				0.7008,
				0.82
				]
    this_dict["ljets_5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttH"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1769,
				0.3615,
				0.4538,
				0.5462,
				0.6385,
				0.8
				]
    this_dict["ljets_5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttbb"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1754,
				0.3723,
				0.4708,
				0.5692,
				0.6677,
				0.84
				]
    this_dict["ljets_5j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttcc"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1858,
				0.57
				]
    this_dict["ljets_5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttlf"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.185,
				0.59
				]
    this_dict["ljets_5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 4j_ge3t

    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==0))","ljets_4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttZ"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1781,
				0.2658,
				0.3535,
				0.4412,
				0.485,
				0.5288,
				0.5727,
				0.6165,
				0.6604,
				0.77
				]
    this_dict["ljets_4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttH"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1792,
				0.3454,
				0.4285,
				0.5115,
				0.5946,
				0.74
				]
    this_dict["ljets_4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttbb"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.175,
				0.375,
				0.475,
				0.575,
				0.675,
				0.85
				]
    this_dict["ljets_4j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttcc"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1865,
				0.55
				]
    this_dict["ljets_4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttlf"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1792,
				0.74
				]
    this_dict["ljets_4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    

    for l in this_dict:
        this_dict[l]["histoname"] = discrname+"_"+l
        this_dict[l]["histotitle"] = "ANN output ({})".format(translateName(l))
        this_dict[l]["plotPreselections"] = this_dict[l]["category"][0]

    DNNPlots = init_plots(dictionary = this_dict, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def translateName(name):
    name = name.replace("ljets_","")
    name = name.replace("ge6j_ge3t_","")
    name = name.replace("ge4j_ge3t_","")
    name = name.replace("ge4j_3t_","")
    name = name.replace("ge4j_ge4t_","")
    name = name.replace("4j_ge3t_","")
    name = name.replace("le5j_ge3t_","")
    name = name.replace("5j_ge3t_","")

    name = name.replace("ttZ_","t#bar{t}+Z ")
    name = name.replace("ttH_","t#bar{t}+H ")
    name = name.replace("ttbb_","t#bar{t}+b#bar{b} ")
    name = name.replace("ttlf_","t#bar{t}+lf ")
    name = name.replace("ttcc_","t#bar{t}+c#bar{c} ")
    return name

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
    
