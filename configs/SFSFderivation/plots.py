
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

def plots_control(data = None):
    selection = "(1.)"
    label = "inclusive"
    plots = [
        plotClasses.Plot(ROOT.TH1D("N_Jets","N_Jets",10,-0.5,9.5),"N_Jets",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_control(data)
    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
