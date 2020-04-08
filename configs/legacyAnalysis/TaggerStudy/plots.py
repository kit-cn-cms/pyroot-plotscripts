
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

HTbinEdges = [0,50,100,150,200,300,400,500,600,700,800,900,1000,1500]
#HTbinEdges = [0,50,100,150,200,300,400,500,1000]
#HTbinEdges = [0,100,200,300,500,1000]
nHTbins = len(HTbinEdges)-1
HTbinEdges = array("f", HTbinEdges)

#nJbinEdges = [2.5,4.5,5.5,6.5,7.5,10.5]
nJbinEdges = [2.5,4.5,5.5,6.5,7.5,10.5]
nJbins = len(nJbinEdges)-1
nJbinEdges = array("f", nJbinEdges)

pvbinEdges = [0.,10.,15.,20.,25.,30.,35.,40.,45.,50.,55.,60.,70.]
pvbins = len(pvbinEdges)-1
pvbinEdges = array("f", pvbinEdges)

def plots_control_incl(data = None):
    selection = "(1.)"
    label = "inclusive"
    plots = [
        plotClasses.Plot(ROOT.TH1D("yield_" + label, "yield_" + label, 1, 0.0, 2.0), "1.", selection, label),
        plotClasses.Plot(ROOT.TH1F("N_Jets_" + label,"N_Jets_" + label,nJbins,nJbinEdges),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM_" + label,"N_BTagsM",11,-0.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM_DeepCSV_" + label,"N_BTagsM_DeepCSV",11,-0.5,10.5),"N_BTagsM_DeepCSV",selection,label),
        plotClasses.Plot(ROOT.TH1F("Jet_Pt_" + label,"Jet_Pt_" + label,npTbins, pTbinEdges),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1F("Jet_Pt_0_" + label,"Jet_Pt_0_" + label,npTbins, pTbinEdges),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1F("HT_jets_" + label,"HT_jets_" + label,nHTbins, HTbinEdges),"Evt_HT_jets",selection,label),        
        ]

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_control_3t_DeepJet(data = None):
    selection = "(1.)*(N_BTagsM == 3)"
    label = "3t_DeepJet"
    plots = [
        plotClasses.Plot(ROOT.TH1D("yield_" + label, "yield_" + label, 1, 0.0, 2.0), "1.", selection, label),
        plotClasses.Plot(ROOT.TH1F("N_Jets_" + label,"N_Jets_" + label,nJbins,nJbinEdges),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM_" + label,"N_BTagsM",11,-0.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM_DeepCSV_" + label,"N_BTagsM_DeepCSV",11,-0.5,10.5),"N_BTagsM_DeepCSV",selection,label),plotClasses.Plot(ROOT.TH1F("Jet_Pt_" + label,"Jet_Pt_" + label,npTbins, pTbinEdges),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1F("Jet_Pt_0_" + label,"Jet_Pt_0_" + label,npTbins, pTbinEdges),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1F("HT_jets_" + label,"HT_jets_" + label,nHTbins, HTbinEdges),"Evt_HT_jets",selection,label),        
        ]

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_control_ge4t_DeepJet(data = None):
    selection = "(1.)*(N_BTagsM >= 4)"
    label = "ge4t_DeepJet"
    plots = [
        plotClasses.Plot(ROOT.TH1D("yield_" + label, "yield_" + label, 1, 0.0, 2.0), "1.", selection, label),
        plotClasses.Plot(ROOT.TH1F("N_Jets_" + label,"N_Jets_" + label,nJbins,nJbinEdges),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM_" + label,"N_BTagsM",11,-0.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM_DeepCSV_" + label,"N_BTagsM_DeepCSV",11,-0.5,10.5),"N_BTagsM_DeepCSV",selection,label),plotClasses.Plot(ROOT.TH1F("Jet_Pt_" + label,"Jet_Pt_" + label,npTbins, pTbinEdges),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1F("Jet_Pt_0_" + label,"Jet_Pt_0_" + label,npTbins, pTbinEdges),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1F("HT_jets_" + label,"HT_jets_" + label,nHTbins, HTbinEdges),"Evt_HT_jets",selection,label),        
        ]

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_control_3t_DeepCSV(data = None):
    selection = "(1.)*(N_BTagsM_DeepCSV == 3)"
    label = "3t_DeepCSV"
    plots = [
        plotClasses.Plot(ROOT.TH1D("yield_" + label, "yield_" + label, 1, 0.0, 2.0), "1.", selection, label),
        plotClasses.Plot(ROOT.TH1F("N_Jets_" + label,"N_Jets_" + label,nJbins,nJbinEdges),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM_" + label,"N_BTagsM",11,-0.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM_DeepCSV_" + label,"N_BTagsM_DeepCSV",11,-0.5,10.5),"N_BTagsM_DeepCSV",selection,label),plotClasses.Plot(ROOT.TH1F("Jet_Pt_" + label,"Jet_Pt_" + label,npTbins, pTbinEdges),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1F("Jet_Pt_0_" + label,"Jet_Pt_0_" + label,npTbins, pTbinEdges),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1F("HT_jets_" + label,"HT_jets_" + label,nHTbins, HTbinEdges),"Evt_HT_jets",selection,label),        
        ]

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_control_ge4t_DeepCSV(data = None):
    selection = "(1.)*(N_BTagsM_DeepCSV >= 4)"
    label = "ge4t_DeepCSV"
    plots = [
        plotClasses.Plot(ROOT.TH1D("yield_" + label, "yield_" + label, 1, 0.0, 2.0), "1.", selection, label),
        plotClasses.Plot(ROOT.TH1F("N_Jets_" + label,"N_Jets_" + label,nJbins,nJbinEdges),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM_" + label,"N_BTagsM",11,-0.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM_DeepCSV_" + label,"N_BTagsM_DeepCSV",11,-0.5,10.5),"N_BTagsM_DeepCSV",selection,label), plotClasses.Plot(ROOT.TH1F("Jet_Pt_" + label,"Jet_Pt_" + label,npTbins, pTbinEdges),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1F("Jet_Pt_0_" + label,"Jet_Pt_0_" + label,npTbins, pTbinEdges),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1F("HT_jets_" + label,"HT_jets_" + label,nHTbins, HTbinEdges),"Evt_HT_jets",selection,label),        
        ]

    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_control_incl(data)
    discriminatorPlots += plots_control_3t_DeepJet(data)
    discriminatorPlots += plots_control_3t_DeepCSV(data)
    discriminatorPlots += plots_control_ge4t_DeepJet(data)
    discriminatorPlots += plots_control_ge4t_DeepCSV(data)
    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
