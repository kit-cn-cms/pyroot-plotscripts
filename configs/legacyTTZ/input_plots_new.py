
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

def plots_jtr(label, selection, jtr, data = None):
    plots = [
        plotClasses.Plot(ROOT.TH1D(jtr+"_N_PV","pile up",80,0,80),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Electron_Pt","p_{T}(electron) [GeV]",50,0,400),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Electron_E","E(electron) [GeV]",50,0,450),"Electron_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Electron_Eta","#eta(electron)",50,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Electron_Phi","#phi(electron)",50,-3.3,3.3),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Muon_Pt","p_{T}(muon) [GeV]",50,0,300),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Muon_E","E(muon) [GeV]",50,0,450),"Muon_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Muon_Eta","#eta(muon)",50,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Muon_Phi","#phi(muon)",50,-3.3,3.3),"Muon_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_TightLepton_Pt","p_{T}(lepton) [GeV]",50,0,300),"TightLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_TightLepton_E","E(lepton) [GeV]",50,0,450),"TightLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_TightLepton_Eta","#eta(lepton)",50,-2.5,2.5),"TightLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_TightLepton_Phi","#phi(lepton)",50,-3.3,3.3),"TightLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_N_BTagsM","b tag multiplicity",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_N_Jets","jet multiplicity",7,3.5,10.5),"N_Jets",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_btagValue","b tag value of all jets",30,0,1),"btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_btagValue_0","b tag value of 1st jet",30,0.0,1.0),"Jet_btagValue[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_btagValue_1","b tag value of 2nd jet",30,0.0,1.0),"Jet_btagValue[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_btagValue_2","b tag value of 3rd jet",30,0.0,1.0),"Jet_btagValue[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_btagValue_3","b tag value of 4th jet",30,0.0,1.0),"Jet_btagValue[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_btagValue_4","b tag value of 5th jet",30,0.0,1.0),"Jet_btagValue[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_btagValue_5","b tag value of 6th jet",30,0.0,1.0),"Jet_btagValue[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_btagValue_0","1st b tag value",30,0.3,1.0),"btagValue[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_btagValue_1","2nd b tag value",30,0.3,1.0),"btagValue[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_btagValue_2","3rd b tag value",30,0.3,1.0),"btagValue[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_btagValue_3","4th b tag value",30,0.0,1.0),"btagValue[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_btagValue_4","5th b tag value",30,0.0,1.0),"btagValue[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_btagValue_5","6th b tag value",30,0.0,1.0),"btagValue[5]",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsL","c tag value (vs. light flavor)",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsL",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsL_1","c tag value (vs. light flavor) of 1st jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsL[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsL_2","c tag value (vs. light flavor) of 2nd jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsL[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsL_3","c tag value (vs. light flavor) of 3rd jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsL[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsL_4","c tag value (vs. light flavor) of 4th jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsL[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsL_5","c tag value (vs. light flavor) of 5th jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsL[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsL_6","c tag value (vs. light flavor) of 6th jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsL[5]",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsB","c tag value (vs. b flavor)",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsB",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsB_1","c tag value (vs. b flavor) of 1st jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsB[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsB_2","c tag value (vs. b flavor) of 2nd jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsB[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsB_3","c tag value (vs. b flavor) of 3rd jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsB[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsB_4","c tag value (vs. b flavor) of 4th jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsB[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsB_5","c tag value (vs. b flavor) of 5th jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsB[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_Jet_DeepJet_CvsB_6","c tag value (vs. b flavor) of 6th jet",30,0.0,1.0),"ctag_ft_Jet_DeepJet_CvsB[5]",selection,label),
        ]


    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def plots_ge6j_ge3t(data = None):
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)&&(1.)"
    jtr = "ljets_ge6j_ge3t"

    plots = plots_jtr(label, selection, jtr, data)
    return plots

def plots_ge4j_ge3t(data = None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&(1.)"
    jtr = "ljets_ge4j_ge3t"

    plots = plots_jtr(label, selection, jtr, data)
    return plots

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge3t(data)
    discriminatorPlots += plots_ge6j_ge3t(data)

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
    
