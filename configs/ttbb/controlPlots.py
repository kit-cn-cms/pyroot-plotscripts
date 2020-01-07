
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

evtYields = "(N_Jets==4&&N_BTagsM==3)*1"
evtYields+="+(N_Jets==4&&N_BTagsM>=4)*2"
evtYields+="+(N_Jets==5&&N_BTagsM==3)*3"
evtYields+="+(N_Jets==5&&N_BTagsM>=4)*4"
evtYields+="+(N_Jets>=6&&N_BTagsM==3)*5"
evtYields+="+(N_Jets>=6&&N_BTagsM>=4)*6"

def plots_control(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_yields","yield",6,0.5,6.5),evtYields,selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_N_PV","N_PrimaryVertices",80,0,80),"N_PrimaryVertices",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Pt","p_{T}(electron)",30,30,530),"Electron_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Eta","#eta(electron)",25,-2.4,2.4),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Phi","#phi(electron)",25,-3.1416,3.1416),"Electron_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Pt","p_{T}(muon)",30,30,530),"Muon_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Eta","#eta(muon)",25,-2.4,2.4),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Phi","#phi(muon)",25,-3.1416,3.1416),"Muon_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Pt","p_{T}(lepton)",30,30,530),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Eta","#eta(lepton)",25,-2.4,2.4),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Phi","#phi(lepton)",25,-3.1416,3.1416),"LooseLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta","Jet_Eta",25,-2.4,2.4),"Jet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi","Jet_Phi",25,-3.1416,3.1416),"Jet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt","Jet_Pt",30, 30., 730),"Jet_Pt",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_N_BTagsM","N_BTagsM",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_N_Jets","N_Jets",5,3.5,8.5),"N_Jets",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_CSV","CSV",60,0.0,1.0),"CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV","Jet_CSV",30,0.0,1.0),"Jet_CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_0","Jet CSV[0]",60,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_1","Jet CSV[1]",60,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_2","Jet CSV[2]",60,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_3","Jet CSV[3]",60,0.0,1.0),"Jet_CSV[3]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_0","CSV[0]",60,0.0,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_1","CSV[1]",60,0.0,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_2","CSV[2]",60,0.0,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_3","CSV[3]",60,0.0,1.0),"CSV[3]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT","H_{T} [GeV]",50,0.0,2000.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT_tags","H_{T}(b-tagged jets) [GeV]",50,0.0,1000.0),"Evt_HT_tags",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_MET","MET",30,10.0,300),"Evt_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_MET_Phi","MET Phi",30,-3.3,3.3),"Evt_MET_Phi",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_0","Jet_Pt[0]",30,30.,730.),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_1","Jet_Pt[1]",30,30.,530.),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_2","Jet_Pt[2]",30,30.,430.),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_3","Jet_Pt[3]",30,30.,300.),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_4","Jet_Pt[4]",30,30.,300.),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_5","Jet_Pt[5]",30,30.,300.),"Jet_Pt[5]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_0","Jet_Eta[0]",25,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_1","Jet_Eta[1]",25,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_2","Jet_Eta[2]",25,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_3","Jet_Eta[3]",25,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_4","Jet_Eta[4]",25,-2.4,2.4),"Jet_Eta[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_5","Jet_Eta[5]",25,-2.4,2.4),"Jet_Eta[5]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_0","Jet_Phi[0]",25,-3.1416,3.1416),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_1","Jet_Phi[1]",25,-3.1416,3.1416),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_2","Jet_Phi[2]",25,-3.1416,3.1416),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_3","Jet_Phi[3]",25,-3.1416,3.1416),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_4","Jet_Phi[4]",25,-3.1416,3.1416),"Jet_Phi[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi_5","Jet_Phi[5]",25,-3.1416,3.1416),"Jet_Phi[5]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_minDrLepJet","Evt_Dr_minDrLepJet",30,0.0,4.0),"Evt_Dr_minDrLepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_minDrTaggedJets","Evt_Dr_minDrTaggedJets",30,0.3,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",40,0.0,400.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_M2_minDrTaggedJets","Evt_M2_minDrTaggedJets",40,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        ]
    return plots

#baseline
def plots_ge4j_ge3t(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    tag = "ge4j_ge3t"
    plots = plots_control(tag, selection, label)    

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge6j_ge3t(data=None):
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)"

    tag = "ge6j_ge3t"
    plots = plots_control(tag, selection, label)    

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge6j_ge4t(data=None):
    label = "\geq 6 jets, \geq 4 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=4)"

    tag = "ge6j_ge4t"
    plots = plots_control(tag, selection, label)    

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge6j_ge4t_mu(data=None):
    label = "mu, \geq 6 jets, \geq 4 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=4&&N_TightMuons==1)"

    tag = "mu_ge6j_ge4t"
    plots = plots_control(tag, selection, label)    

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge6j_ge4t_el(data=None):
    label = "el, \geq 6 jets, \geq 4 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=4&&N_TightElectrons==1)"

    tag = "el_ge6j_ge4t"
    plots = plots_control(tag, selection, label)    

    if data:
        add_data_plots(plots=plots,data=data)

    return plots



def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    #baseline
    discriminatorPlots += plots_ge4j_ge3t(data)
    #discriminatorPlots += plots_ge6j_ge3t(data)
    discriminatorPlots += plots_ge6j_ge4t(data)
    discriminatorPlots += plots_ge6j_ge4t_mu(data)
    discriminatorPlots += plots_ge6j_ge4t_el(data)

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
