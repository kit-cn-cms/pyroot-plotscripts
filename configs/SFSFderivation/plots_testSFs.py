
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

nJbinEdges = [-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,10.5]
nJbins = len(nJbinEdges)-1
nJbinEdges = array("f", nJbinEdges)

pvbinEdges = [0.,10.,15.,20.,25.,30.,35.,40.,45.,50.,55.,60.,70.]
pvbins = len(pvbinEdges)-1
pvbinEdges = array("f", pvbinEdges)

def plots_control(data = None):
    selection = "(N_BTagsM>=3)"
    label = "\geq 3 b-tags"
    plots = [
        plotClasses.Plot(ROOT.TH1D("N_Jets","N_Jets",nJbins,nJbinEdges),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("Jet_Pt","Jet_Pt",50,0.,500.),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("Jet_Pt_0","Jet_Pt_0",npTbins, pTbinEdges),"Jet_Pt[0]",selection,label),
        #plotClasses.Plot(ROOT.TH1D("Jet_Pt_0","Jet_Pt_0",50,0.,500.),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM","N_BTagsM",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("Jet_Eta","Jet_Eta",30,-2.5,2.5),"Jet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("CSV","CSV",50,0.,1.),"CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D("HT","HT",75,0.,1500.),htDummy,selection,label),
        plotClasses.Plot(ROOT.TH1D("N_PV","PV",pvbins,pvbinEdges),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_GenPV","GenPV",pvbins,pvbinEdges),"N_GenPVs",selection,label),
        ]
    selection = "(1.)"
    label = "inclusive"
    plots+= [
        plotClasses.Plot(ROOT.TH1D("inclusive_N_Jets","N_Jets",nJbins,nJbinEdges),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt","Jet_Pt",50,0.,500.),"Jet_Pt",selection,label),
        #plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt_0","Jet_Pt_0",50,0.,500.),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt_0","Jet_Pt_0",npTbins, pTbinEdges),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_BTagsM","N_BTagsM",9,-0.5,8.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Eta","Jet_Eta",30,-2.5,2.5),"Jet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_CSV","CSV",50,0.,1.),"CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D("inclusive_HT","HT",75,0.,1500.),htDummy,selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_PV","PV",pvbins,pvbinEdges),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_GenPV","GenPV",pvbins,pvbinEdges),"N_GenPVs",selection,label),
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
