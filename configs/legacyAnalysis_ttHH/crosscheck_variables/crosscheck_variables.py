
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



def evtYieldCategories():
    return [
    ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
    ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
    ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
    ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
    ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
    ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
    ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
    ]

memexp = ""

yieldExpression = "(N_Jets==4 && N_BTagsM==3)*1"
yieldExpression+="+(N_Jets==4 && N_BTagsM>=4)*2"
yieldExpression+="+(N_Jets==5 && N_BTagsM==3)*3"
yieldExpression+="+(N_Jets==5 && N_BTagsM>=4)*4"
yieldExpression+="+(N_Jets>=6 && N_BTagsM==3)*5"
yieldExpression+="+(N_Jets>=6 && N_BTagsM>=4)*6"



def plots_control(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_0","Jet CSV[0]",30,0.3,1.0),"Jet_CSV[0]",selection,label),
        
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT_jets","H_{T}",50,150.0,2000.0),"Evt_HT_jets",selection,label),
        
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_0","Jet_Pt[0]",30,20,500),"Jet_Pt[0]",selection,label),
        
        ]
    return plots

#baseline
def plots_ge4j_ge3t(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    tag = "ge4j_ge3t"
    plots = plots_control(tag, selection, label)    
    # plots += plots_ttHReco(tag, selection, label)
    # plots += plots_ttbarReco(tag, selection, label)
    # plots += plots_tHWReco(tag, selection, label)
    # plots += plots_tHQReco(tag, selection, label) 

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

#analysis categories w/o forward stuff
def plots_ge4j_3t(data=None):
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"

    tag = "ge4j_3t"
    plots = plots_control(tag, selection, label)    
    # plots += plots_ttHReco(tag, selection, label)
    # plots += plots_ttbarReco(tag, selection, label)
    # plots += plots_tHWReco(tag, selection, label)
    # plots += plots_tHQReco(tag, selection, label) 

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge4j_ge4t(data=None):
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)"

    tag = "ge4j_ge4t"
    plots = plots_control(tag, selection, label)    
    # plots += plots_ttHReco(tag, selection, label)
    # plots += plots_ttbarReco(tag, selection, label)
    # plots += plots_tHWReco(tag, selection, label)
    # plots += plots_tHQReco(tag, selection, label)  

    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    #baseline
    # discriminatorPlots += plots_ge4j_ge3t(data)

    #analysis categories w/o forward stuff
    discriminatorPlots += plots_ge4j_3t(data)
    discriminatorPlots += plots_ge4j_ge4t(data)
    return discriminatorPlots


def init_plots(dictionary, data = None):
    plots = [] #init list of plotClasses objects to return
    for label in dictionary:
        subdict = dictionary[label] #for easy access
        discr = subdict["discr"] # load discriminator name
        sel = subdict["plotPreselections"] # load selection
        histoname = subdict["histoname"] # load histogram name
        histotitle = subdict["histotitle"] # load histogram title

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used
        if "bin_edges" in subdict:
            bins = array("f", subdict["bin_edges"])
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            subdict["nhistobins"] = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname,histotitle,nbins,bins),
                    discr,sel,label))
        elif "minxval" in subdict and "maxxval" in subdict:
            nbins = subdict["nhistobins"]
            xmax  = subdict["maxxval"]
            xmin  = subdict["minxval"]
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname, histotitle,nbins,xmin, xmax),
                    discr,sel,label))
    if not data is None:
        data.categories.update(dictionary)
    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
