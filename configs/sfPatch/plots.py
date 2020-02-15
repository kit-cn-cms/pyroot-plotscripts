
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

pTbinEdges = [30.,50.,75.,100.,150.,250.,350.,500.,1000.]
npTbins = len(pTbinEdges)-1
pTbinEdges = array("f", pTbinEdges)

HTbinEdges = [0,50,100,150,200,300,400,500,750,1000,1500]
#HTbinEdges = [0,50,100,150,200,300,400,500,1000]
#HTbinEdges = [0,100,200,300,500,1000]
nHTbins = len(HTbinEdges)-1
HTbinEdges = array("f", HTbinEdges)

#nJbinEdges = [2.5,4.5,5.5,6.5,7.5,10.5]
nJbinEdges = [2.5,4.5,5.5,6.5,10.5]
nJbins = len(nJbinEdges)-1
nJbinEdges = array("f", nJbinEdges)

pvbinEdges = [0.,10.,15.,20.,25.,30.,35.,40.,45.,50.,55.,60.,70.]
pvbins = len(pvbinEdges)-1
pvbinEdges = array("f", pvbinEdges)

def plots_control(data = None):
    selection = "(1.)"
    label = "inclusive"
    plots = [
        plotClasses.Plot(ROOT.TH1F("N_Jets","N_Jets",nJbins,nJbinEdges),"N_Jets",selection,label),
        #plotClasses.Plot(ROOT.TH1F("Jet_Pt_0","Jet_Pt_0",npTbins, pTbinEdges),"Jet_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1F("N_GenPVs","N_GenPVs",pvbins, pvbinEdges),"N_GenPVs",selection,label),
        #plotClasses.Plot(ROOT.TH1F("HT_jets","HT_jets",nHTbins, HTbinEdges),"Evt_HT_jets",selection,label),

        #plotClasses.TwoDimPlot(
        #    ROOT.TH2F("Jet_Pt_0_vs_N_Jets","hardest jet pt vs number of jets",npTbins,pTbinEdges,nJbins,nJbinEdges),
        #    "Jet_Pt[0]","N_Jets",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2F("Evt_HT_jets_vs_N_Jets","HT vs number of jets",nHTbins,HTbinEdges,nJbins,nJbinEdges),
            "Evt_HT_jets","N_Jets",selection,label),
        #plotClasses.TwoDimPlot(
        #    ROOT.TH2F("N_GenPVs_vs_N_Jets","number of gen PVs vs number of jets",pvbins,pvbinEdges,nJbins,nJbinEdges),
        #    "N_GenPVs", "N_Jets",selection,label),
        
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
