
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



def plots_ge4j_ge3t(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Pt","p_{T}(electron)",50,0,200),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Eta","#eta(electron)",50,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Phi","#phi(electron)",50,-3.1416,3.1416),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Pt","p_{T}(muon)",50,0,200),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Eta","#eta(muon)",50,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Phi","#phi(muon)",50,-3.1416,3.1416),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Pt","p_{T}(lepton)",50,0,200),"LooseLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Eta","#eta(lepton)",50,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Phi","#phi(lepton)",50,-3.1416,3.1416),"LooseLepton_Phi[0]",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_mtw_cut(data=None):
    label = "\geq 4 jets, \geq 3 b-tags, MTW \geq 50 GeV"
    selection = "(N_Jets>=4&&N_BTagsM>=3&&Evt_MTW>=50.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("mtw_control_Electron_Pt","p_{T}(electron)",50,0,200),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("mtw_control_Electron_Eta","#eta(electron)",50,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("mtw_control_Electron_Phi","#phi(electron)",50,-3.1416,3.1416),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("mtw_control_Muon_Pt","p_{T}(muon)",50,0,200),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("mtw_control_Muon_Eta","#eta(muon)",50,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("mtw_control_Muon_Phi","#phi(muon)",50,-3.1416,3.1416),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("mtw_control_Lepton_Pt","p_{T}(lepton)",50,0,200),"LooseLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("mtw_control_Lepton_Eta","#eta(lepton)",50,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("mtw_control_Lepton_Phi","#phi(lepton)",50,-3.1416,3.1416),"LooseLepton_Phi[0]",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge3t(data)
    discriminatorPlots += plots_mtw_cut(data)

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
