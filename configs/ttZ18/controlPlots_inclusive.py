
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


def write_config(jt, plots):
    template="\"{name}\",{min},{max},{nbins},-,\"{displayname}\""
    string = ""
    string+= "variablename,minvalue,maxvalue,numberofbins,logoption,displayname\n"
    
    for p in plots:
        nbins = p.histo.GetNbinsX()
        bin_edges = []
        for i in range(1,nbins+2):
            bin_edges.append(p.histo.GetBinLowEdge(i))
        config = {
            "name":         p.variable,#p.histo.GetName().replace(jt,"").replace("ljets__","").replace("ljets_","").replace("ljets",""),
            "min":          bin_edges[0],
            "max":          bin_edges[-1],
            "nbins":        nbins,
            "displayname":  p.histo.GetTitle()
            }
        string+=template.format(**config)+"\n"

    with open("/nfs/dust/cms/user/vdlinden/legacyTTH/DNNSets/ttZ_4Node_top30_v4/{}/new_plot_config.csv".format(jt), "w") as f:
        f.write(string)

jtYieldExpression = "(N_Jets==4&&N_BTagsM==3)*1"
jtYieldExpression+="+(N_Jets==4&&N_BTagsM>=4)*2"
jtYieldExpression+="+(N_Jets==5&&N_BTagsM==3)*3"
jtYieldExpression+="+(N_Jets==5&&N_BTagsM>=4)*4"
jtYieldExpression+="+(N_Jets>=6&&N_BTagsM==3)*5"
jtYieldExpression+="+(N_Jets>=6&&N_BTagsM>=4)*6"


memexp = ""


def inclusive_plots(data=None):
    label = "\geq 4 jets, \geq 3 b-tags (inclusive)"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"


    plots = [
        plotClasses.Plot(ROOT.TH1D("inclusive_eventYields","event yields",6,0.5,6.5),jtYieldExpression,selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt_0","p_{T} of leading jet",30,30.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt","p_{T} of all jets",30,20.0,400.0),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_BTagsM","number of b-tags (medium)",3,2.5,5.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_Jets","number of reconstructed jets",8,3.5,11.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_CSV_0","highest b-tag value",30,0.7,1.),"CSV[0]",selection,label),
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

        plotClasses.Plot(ROOT.TH1D("inclusive_yield","inclusive yield",1,0,10),"N_BTagsM",selection,label),
        #plotClasses.Plot(ROOT.TH1D("inclusive_Evt_blr","b-tag likelihood ratio",40,0.,1.),"Evt_blr",selection,label),
        #plotClasses.Plot(ROOT.TH1D("inclusive_Evt_blr_transformed","transformed b-tag likelihood ratio",40,-7,15.),"Evt_blr_transformed",selection,label),

        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def sideband_plots(data=None):
    label = "\geq 4 jets, \geq 3 b-tags (sideband)"
    selection = "(N_Jets>=4&&N_BTagsM>=3)*(abs(Evt_M2_closestTo91TaggedJets-91.)>=20.)"

    

    plots = [
        plotClasses.Plot(ROOT.TH1D("sideband_eventYields","event yields",6,0.5,6.5),jtYieldExpression,selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Jet_Pt_0","p_{T} of leading jet",30,30.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Jet_Pt","p_{T} of all jets",30,20.0,400.0),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_N_BTagsM","number of b-tags (medium)",3,2.5,5.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_N_Jets","number of reconstructed jets",8,3.5,11.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_CSV_0","highest b-tag value",30,0.7,1.),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_JetCSV_0","b-tag value of leading jet",30,0.,1.),"Jet_CSV[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D("sideband_Electron_Pt","p_{T}(electron)",30,30,200),"Electron_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Electron_Eta","#eta(electron)",30,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Electron_Phi","#phi(electron)",30,-3.1416,3.1416),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Muon_Pt","p_{T}(muon)",30,25,200),"Muon_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Muon_Eta","#eta(muon)",30,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Muon_Phi","#phi(muon)",30,-3.1416,3.1416),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Lepton_Pt","p_{T}(lepton)",30,25,200),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Lepton_Eta","#eta(lepton)",30,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("sideband_Lepton_Phi","#phi(lepton)",30,-3.1416,3.1416),"LooseLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D("sideband_yield","inclusive yield",1,0,10),"N_BTagsM",selection,label),
        #plotClasses.Plot(ROOT.TH1D("sideband_Evt_blr","b-tag likelihood ratio",40,0.,1.),"Evt_blr",selection,label),
        #plotClasses.Plot(ROOT.TH1D("sideband_Evt_blr_transformed","transformed b-tag likelihood ratio",40,-7,15.),"Evt_blr_transformed",selection,label),

        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += inclusive_plots(data)
    discriminatorPlots += sideband_plots(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    
if __name__ == "__main__":
    getDiscriminatorPlots()
