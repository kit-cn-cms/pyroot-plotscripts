
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

memexp = ''

yieldExpression = "(N_Jets==4 && N_BTagsM==3)*1"
yieldExpression+="+(N_Jets==5 && N_BTagsM==3)*2"
yieldExpression+="+(N_Jets>=6 && N_BTagsM==3)*3"
yieldExpression+="+(N_Jets==4 && N_BTagsM>=4)*4"
yieldExpression+="+(N_Jets==5 && N_BTagsM>=4)*5"
yieldExpression+="+(N_Jets>=6 && N_BTagsM>=4)*6"

def plots_control(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_diffYield","yield per jet-tag bin",6,0.5,6.5),yieldExpression,selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_totYield","total yield",1,-1,1),"0.",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_N_PV","N_PrimaryVertices",80,0,80),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Pt","p_{T}(electron)",50,0,400),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_E","E(electron)",50,0,450),"Electron_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Eta","#eta(electron)",50,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Phi","#phi(electron)",50,-3.3,3.3),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Pt","p_{T}(muon)",50,0,300),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_E","E(muon)",50,0,450),"Muon_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Eta","#eta(muon)",50,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Phi","#phi(muon)",50,-3.3,3.3),"Muon_Phi[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Pt","p_{T}(lepton)",50,0,300),"LooseLepton_Pt",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_E","E(lepton)",50,0,450),"LooseLepton_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Eta","#eta(lepton)",50,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Phi","#phi(lepton)",50,-3.3,3.3),"LooseLepton_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Pt","p_{T}(tight lepton)",50,0,300),"TightLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_E","E(tight lepton)",50,0,450),"TightLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Eta","#eta(tight lepton)",50,-2.5,2.5),"TightLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Phi","#phi(tight lepton)",50,-3.3,3.3),"TightLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_N_BTagsM","b-tagged jet multiplicity",8,2.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_N_Jets","jet multiplicity",9,3.5,12.5),"N_Jets",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_btagValue","deepJet b-tagging value",30,0,1),"btagValue",selection,label),
  
        ]
    if cat == "ge4j_ge3t":
        plots += [
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_btagValue_0","b-tagging value of jet No. 0",30,0.0,1.0),"Jet_btagValue[0]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_btagValue_1","b-tagging value of jet No. 1",30,0.0,1.0),"Jet_btagValue[1]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_btagValue_2","b-tagging value of jet No. 2",30,0.0,1.0),"Jet_btagValue[2]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_btagValue_3","b-tagging value of jet No. 3",30,0.0,1.0),"Jet_btagValue[3]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_btagValue_4","b-tagging value of jet No. 4",30,0.0,1.0),"Jet_btagValue[4]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_btagValue_5","b-tagging value of jet No. 5",30,0.0,1.0),"Jet_btagValue[5]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_btagValue_0","b-tagging value No. 0",30,0.3,1.0),"btagValue[0]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_btagValue_1","b-tagging value No. 1",30,0.3,1.0),"btagValue[1]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_btagValue_2","b-tagging value No. 2",30,0.3,1.0),"btagValue[2]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_btagValue_3","b-tagging value No. 3",30,0.0,1.0),"btagValue[3]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_btagValue_4","b-tagging value No. 4",30,0.0,1.0),"btagValue[4]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_btagValue_5","b-tagging value No. 5",30,0.0,1.0),"btagValue[5]",selection,label),

            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_0","p_{T} of jet No. 0 [GeV]",30,20,500),"Jet_Pt[0]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_1","p_{T} of jet No. 1 [GeV]",30,20,500),"Jet_Pt[1]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_2","p_{T} of jet No. 2 [GeV]",30,20,350),"Jet_Pt[2]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_3","p_{T} of jet No. 3 [GeV]",30,20,250),"Jet_Pt[3]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_4","p_{T} of jet No. 4 [GeV]",30,20,250),"Jet_Pt[4]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_5","p_{T} of jet No. 5 [GeV]",30,20,250),"Jet_Pt[5]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_0","#eta of jet No. 0",30,-2.5,2.5),"Jet_Eta[0]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_1","#eta of jet No. 1",30,-2.5,2.5),"Jet_Eta[1]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_2","#eta of jet No. 2",30,-2.5,2.5),"Jet_Eta[2]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_3","#eta of jet No. 3",30,-2.5,2.5),"Jet_Eta[3]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_4","#eta of jet No. 4",30,-2.5,2.5),"Jet_Eta[4]",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_5","#eta of jet No. 5",30,-2.5,2.5),"Jet_Eta[5]",selection,label),

            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_E","energy of all jets [GeV]",60,0,800),"Jet_E",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta","#eta of all jets",30,-2.5,2.5),"Jet_Eta",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_M","mass of all jets [GeV]",30,0.0,50.0),"Jet_M",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi","#phi of all jets",30,-3.3,3.3),"Jet_Phi",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt","p_{T} of all jets [GeV]",40,20,400),"Jet_Pt",selection,label),

            plotClasses.Plot(ROOT.TH1D(cat+"_Evt_MET","missing transverse energy [GeV]",30,10.0,300),"Evt_MET",selection,label),
            plotClasses.Plot(ROOT.TH1D(cat+"_Evt_MET_Phi","#phi of missing transverse energy",30,-3.3,3.3),"Evt_MET_Phi",selection,label),
        ]
    return plots


#baseline
def plots_ge4j_ge3t(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    tag = "ge4j_ge3t"
    plots = plots_control(tag, selection, label)   
    #plots += plots_crossCheck(tag, selection, label)   
     
    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_4j_ge3t(data=None):
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)"

    tag = "4j_ge3t"
    plots = plots_control(tag, selection, label)    

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_5j_ge3t(data=None):
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)"

    tag = "5j_ge3t"
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



def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    #baseline
    discriminatorPlots += plots_ge4j_ge3t(data)
    discriminatorPlots += plots_4j_ge3t(data)
    discriminatorPlots += plots_5j_ge3t(data)
    discriminatorPlots += plots_ge6j_ge3t(data)

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

def init_plots_vhi(interfaces, data = None):
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
