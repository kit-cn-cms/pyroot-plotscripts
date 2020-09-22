
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
import unfolding_setup


memexp = ""

evtYields = "(N_Jets==4&&N_BTagsM==3)*1"
evtYields+="+(N_Jets==4&&N_BTagsM>=4)*2"
evtYields+="+(N_Jets==5&&N_BTagsM==3)*3"
evtYields+="+(N_Jets==5&&N_BTagsM>=4)*4"
evtYields+="+(N_Jets>=6&&N_BTagsM==3)*5"
evtYields+="+(N_Jets>=6&&N_BTagsM>=4)*6"


def plots_unfolding(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_0","btag value of first jet", 1000, 0., 1.),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_1","btag value of second jet", 1000, 0., 1.),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_2","btag value of third jet", 1000, 0., 1.),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_3","btag value of fourth jet", 1000, 0., 1.),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_4","btag value of fifth jet", 1000, 0., 1.),"Jet_CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_5","btag value of sixth jet", 1000, 0., 1.),"Jet_CSV[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_0","highest btag value", 1000, 0.3, 1.),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_1","second highest btag value", 1000, 0.3, 1.),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_2","third highest btag value", 1000, 0.3, 1.),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_3","fourth highest btag value", 1000, 0.3, 1.),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_4","fifth highest btag value", 1000, 0., 0.5),"CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_5","sixth highest btag value", 1000, 0., 0.3),"CSV[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_0","leading jet p_{T} [GeV]", 1000, 30.,1030.),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_1","subleading jet p_{T} [GeV]", 1000, 30.,730.),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_2","3rd highest jet p_{T} [GeV]", 1000, 30.,530.),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_3","4th highest jet p_{T} [GeV]", 1000, 30.,430.),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_4","5th highest jet p_{T} [GeV]", 1000, 30.,230.),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_5","6th highest jet p_{T} [GeV]", 1000, 30.,180.),"Jet_Pt[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_0","#eta of first jet", 1000, 0,2.5),"abs(Jet_Eta[0])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_1","#eta of second jet", 1000, 0,2.5),"abs(Jet_Eta[1])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_2","#eta of third jet", 1000, 0,2.5),"abs(Jet_Eta[2])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_3","#eta of fourth jet", 1000, 0,2.5),"abs(Jet_Eta[3])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_4","#eta of fifth jet", 1000, 0,2.5),"abs(Jet_Eta[4])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta_5","#eta of sixth jet", 1000, 0,2.5),"abs(Jet_Eta[5])",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_minDrTaggedJets","min #DeltaR(bb)", 1000, 0.,5.),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Pt_minDrTaggedJets","p_{T} of min #DeltaR(bb) [GeV]", 1000, 0.,750.),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_M2_minDrTaggedJets","inv. mass of min #DeltaR(bb) [GeV]", 1000, 0.,500.),"Evt_M2_minDrTaggedJets",selection,label),
        ]

    return plots

# unfolding region
def plots_ge6j_ge4t(data=None):
    label = "\geq 6 jets, \geq 4 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=4)"

    tag = "jt64"
    plots = plots_unfolding(tag, selection, label)    

    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    #baseline
    discriminatorPlots += plots_ge6j_ge4t(data)
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
