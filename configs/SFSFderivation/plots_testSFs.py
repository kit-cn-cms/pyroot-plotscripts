
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

htDummy = "((N_Jets>=1)*Jet_Pt[0])"
htDummy+="+((N_Jets>=2)*Jet_Pt[1])"
htDummy+="+((N_Jets>=3)*Jet_Pt[2])"
htDummy+="+((N_Jets>=4)*Jet_Pt[3])"
htDummy+="+((N_Jets>=5)*Jet_Pt[4])"
htDummy+="+((N_Jets>=6)*Jet_Pt[5])"
htDummy+="+((N_Jets>=7)*Jet_Pt[6])"
htDummy+="+((N_Jets>=8)*Jet_Pt[7])"
htDummy+="+((N_Jets>=9)*Jet_Pt[8])"
htDummy+="+((N_Jets>=10)*Jet_Pt[9])"
htDummy+="+((N_Jets>=11)*Jet_Pt[10])"
htDummy+="+((N_Jets>=12)*Jet_Pt[11])"
htDummy+="+((N_LooseLeptons>=1)*LooseLepton_Pt[0])"
htDummy+="+((N_LooseLeptons>=2)*LooseLepton_Pt[1])"
htDummy+="+(Evt_MET_Pt)"

def plots_control(data = None):
    selection = "(N_Jets>=4&&N_BTagsM>=3)"
    label = "\geq 4 jets, \geq 3 b-tags"
    plots = [
        plotClasses.Plot(ROOT.TH1D("N_Jets","N_Jets",6,3.5,9.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("Jet_Pt","Jet_Pt",50,0.,500.),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("Jet_Pt_0","Jet_Pt_0",50,0.,500.),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM","N_BTagsM",6,2.5,8.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("HT","HT",75,0.,1500.),htDummy,selection,label),
        ]
    selection = "(1.)"
    label = "inclusive"
    plots+= [
        plotClasses.Plot(ROOT.TH1D("inclusive_N_Jets","N_Jets",10,-0.5,9.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt","Jet_Pt",50,0.,500.),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt_0","Jet_Pt_0",50,0.,500.),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_BTagsM","N_BTagsM",9,-0.5,8.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_HT","HT",75,0.,1500.),htDummy,selection,label),
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
