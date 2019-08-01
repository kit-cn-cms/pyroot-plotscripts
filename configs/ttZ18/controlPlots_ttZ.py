
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

def control_plots(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt_0","p_{T} of leading jet",30,30.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt","p_{T} of all jets",30,20.0,600.0),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_BTagsM","number of b-tags (medium)",3,2.5,5.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_Jets","number of reconstructed jets",8,3.5,11.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_CSV_0","highest b-tag value",30,0.275,1.),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_JetCSV_0","b-tag value of leading jet",30,0.,1.),"Jet_CSV[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Pt","p_{T}(electron)",30,30,200),"Electron_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Eta","#eta(electron)",30,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Phi","#phi(electron)",30,-3.1416,3.1416),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Pt","p_{T}(muon)",30,25,200),"Muon_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Eta","#eta(muon)",30,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Phi","#phi(muon)",30,-3.1416,3.1416),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Pt","p_{T}(lepton)",30,25,200),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Eta","#eta(lepton)",30,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Phi","#phi(lepton)",30,-3.1416,3.1416),"LooseLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D("inclusive_N_GenJets","number of generator jets",14,3.5,17.5),"N_GenJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_GenJet_Pt","p_{T} of all generator jets",80,0.,400.),"GenJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_LowGenJet_Pt","p_{T} of all generator jets",50,0.,50.),"GenJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_GenJet_Eta","#eta of all generator jets",50,-4.5,4.5),"GenJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_GenJet_Phi","#phi of all generator jets",50,-3.141,3.141),"GenJet_Phi",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += control_plots(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    
