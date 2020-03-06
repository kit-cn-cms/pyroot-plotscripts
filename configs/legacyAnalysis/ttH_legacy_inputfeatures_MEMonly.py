
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
import numpy as np

memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'

def plots_ljets_ge4j_ge4t():
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    interf_ljets_ge4j_ge4t_memDBp = vhi.variableHistoInterface(variable_name  = memexp,
                                            label          = "ljets_ge4j_ge4t_memDBp",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_memDBp.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ge4j_ge4t_memDBp","")
    interf_ljets_ge4j_ge4t_memDBp.category_label = label
    interf_ljets_ge4j_ge4t_memDBp.bin_edges = [ 
                0.0,
                0.0333,
                0.0667,
                0.1,
                0.1333,
                0.1667,
                0.2,
                0.2333,
                0.2667,
                0.3,
                0.3333,
                0.3667,
                0.4,
                0.4333,
                0.4667,
                0.5,
                0.5333,
                0.5667,
                0.6,
                0.6333,
                0.6667,
                0.7,
                0.7333,
                0.7667,
                0.8,
                0.8333,
                0.8667,
                0.9,
                0.9333,
                0.9667,
                1.0
                ]
    interf_ljets_ge4j_ge4t_memDBp.histotitle = "MEM"
    interf_ljets_ge4j_ge4t_memDBp.histoname = "ljets_ge4j_ge4t_memDBp"
    interf_ljets_ge4j_ge4t_memDBp.nhistobins = 30
    interfaces.append(interf_ljets_ge4j_ge4t_memDBp)
    for i in interfaces:
        i.category_label = label
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def plots_ljets_ge4j_3t():
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"
    interf_ljets_ge4j_3t_memDBp = vhi.variableHistoInterface(variable_name  = memexp,
                                            label          = "ljets_ge4j_3t_memDBp",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_memDBp.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ge4j_3t_memDBp","")
    interf_ljets_ge4j_3t_memDBp.category_label = label
    interf_ljets_ge4j_3t_memDBp.bin_edges = [ 
                0.0,
                0.0333,
                0.0667,
                0.1,
                0.1333,
                0.1667,
                0.2,
                0.2333,
                0.2667,
                0.3,
                0.3333,
                0.3667,
                0.4,
                0.4333,
                0.4667,
                0.5,
                0.5333,
                0.5667,
                0.6,
                0.6333,
                0.6667,
                0.7,
                0.7333,
                0.7667,
                0.8,
                0.8333,
                0.8667,
                0.9,
                0.9333,
                0.9667,
                1.0
                ]
    interf_ljets_ge4j_3t_memDBp.histotitle = "MEM"
    interf_ljets_ge4j_3t_memDBp.histoname = "ljets_ge4j_3t_memDBp"
    interf_ljets_ge4j_3t_memDBp.nhistobins = 30
    interfaces.append(interf_ljets_ge4j_3t_memDBp)
    
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ljets_ge4j_ge4t(data)
    discriminatorPlots += plots_ljets_ge4j_3t(data)

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

def init_plots_2D(interfaces):
    plots = [] #init list of plotClasses objects to return
    dictionary = {}
    for i, interf in enumerate(interfaces):
        for interf2 in interfaces[i+1:]:
            binsX = None
            nbinsX = None
            xmin = None
            xmax = None
            binsY = None
            nbinsY = None
            ymin = None
            ymax = None
            
            # check if initialization uses bin edges or min/max vals
            # if 'subdict' contains the keyword 'bin_edges', an array
            # of type float is created from the corresponding python list.
            # Else, the min/maxvals are used 
            if not interf.bin_edges is None:
                binsX  = array("f", interf.bin_edges)
                nbinsX = len(binsX)-1 # last bin edge in array is overflow bin => subtract for nbins
                interf.nhistobins = nbinsX # update number of bins

            elif not (interf.minxval is None or interf.maxxval is None):
                nbinsX = interf.nhistobins
                xmax  = interf.maxxval
                xmin  = interf.minxval
            
            if not interf2.bin_edges is None:
                binsY  = array("f", interf2.bin_edges)
                nbinsY = len(binsY)-1 # last bin edge in array is overflow bin => subtract for nbins
                interf2.nhistobins = nbinsY # update number of bins
            elif not (interf2.minxval is None or interf2.maxxval is None):
                nbinsY = interf2.nhistobins
                ymax  = interf2.maxxval
                ymin  = interf2.minxval

            hname_2D = "{}_{}".format(interf.histoname, interf2.histoname)
            htitle_2D = "{}_{}".format(interf.histotitle, intef2.histotitle)
            if not binsX is None:
                if not binsY is None:
                    plots.append(
                            plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,binsX, nbinsY,binsY),
                                variable1 = interf.varname,
                                variable2 = interf2.varname,
                                selection = interf.selection,
                                label = interf.category_label))
                else: 
                    plots.append(
                            plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,binsX, nbinsY,ymin, ymax),
                                variable1 = interf.varname,
                                variable2 = interf2.varname,
                                selection = interf.selection,
                                label = interf.category_label))
            elif not (xmin is None or xmax is None):
                if not binsY is None:
                    plots.append(
                            plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,xmin, xmax, nbinsY,binsY),
                                variable1 = interf.varname,
                                variable2 = interf2.varname,
                                selection = interf.selection,
                                label = interf.category_label))
                else: 
                    plots.append(
                            plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,xmin, xmax, nbinsY,ymin, ymax),
                                variable1 = interf.varname,
                                variable2 = interf2.varname,
                                selection = interf.selection,
                                label = interf.category_label))
            else:
                s = "FATAL ERROR: Unable to load bin edges or min/max values for histogram!\n"
                s += "interface 1:\n{}".format(interf)
                s += "interface 2:\n{}".format(interf2)
                raise ValueError(s)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    