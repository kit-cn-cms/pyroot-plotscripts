
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

jtYieldExpression = "(N_Jets==4&&N_BTagsM==3)*1"
jtYieldExpression+="+(N_Jets==4&&N_BTagsM>=4)*2"
jtYieldExpression+="+(N_Jets==5&&N_BTagsM==3)*3"
jtYieldExpression+="+(N_Jets==5&&N_BTagsM>=4)*4"
jtYieldExpression+="+(N_Jets>=6&&N_BTagsM==3)*5"
jtYieldExpression+="+(N_Jets>=6&&N_BTagsM>=4)*6"


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

def recogen_plots(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"
    label6 = "\geq 6 jets, \geq 3 b-tags"
    selection6 = "(N_Jets>=6&&N_BTagsM>=3)"

    plots = [
        # delta etas
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_topLep_topHad","#Delta#eta(t_{lep},t_{had})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenTopLep_Eta[0]-GenTopHad_Eta[0])",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_Lep_bHad","#Delta#eta(lep,b_{had})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenTopLep_Lep_Eta[0]-GenTopHad_B_Eta[0])",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_Lep_topHad","#Delta#eta(lep,t_{had})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenTopLep_Lep_Eta[0]-GenTopHad_Eta[0])",selection,label),

        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_bHad_wHad","#Delta#eta(b_{had},W_{had})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenTopHad_B_Eta[0]-GenTopHad_W_Eta[0])",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_bLep_bHad","#Delta#eta(b_{lep},b_{had})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenTopLep_B_Eta[0]-GenTopHad_B_Eta[0])",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_bLep_topHad","#Delta#eta(b_{lep},t_{had})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenTopLep_B_Eta[0]-GenTopHad_Eta[0])",selection,label),

        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_bLep_wLep","#Delta#eta(b_{lep},W_{lep})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenTopLep_B_Eta[0]-GenTopLep_W_Eta[0])",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_topHad_wLep","#Delta#eta(t_{had},W_{lep})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenTopHad_Eta[0]-GenTopLep_W_Eta[0])",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_topLep_bHad","#Delta#eta(t_{lep},b_{had})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenTopLep_Eta[0]-GenTopHad_B_Eta[0])",selection,label),

        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_Z_Lep","#Delta#eta(Z,lep)",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenZ_Eta-GenTopLep_Lep_Eta[0])",selection6,label6),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_Z_bHad","#Delta#eta(Z,b_{had})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenZ_Eta-GenTopHad_B_Eta[0])",selection6,label6),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_Z_bLep","#Delta#eta(Z,b_{lep})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenZ_Eta-GenTopLep_B_Eta[0])",selection6,label6),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_Z_topHad","#Delta#eta(Z,t_{had})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenZ_Eta-GenTopHad_Eta[0])",selection6,label6),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Deta_Z_topLep","#Delta#eta(Z,t_{lep})",40,0,5,40,0,5),
            "RecoTTZ_Deta_topLep_topHad","abs(GenZ_Eta-GenTopLep_Eta[0])",selection6,label6),

        # eta
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopHad_Eta","#eta(t_{had})",40,-2.5,2.5,40,-2.5,2.5),
            "RecoTTZ_TopHad_Eta","GenTopHad_Eta[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopHad_B_Eta","#eta(b_{had})",40,-2.5,2.5,40,-2.5,2.5),
            "RecoTTZ_TopHad_BJet_Eta","GenTopHad_B_Eta[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopHad_W_Eta","#eta(W_{had})",40,-2.5,2.5,40,-2.5,2.5),
            "RecoTTZ_TopHad_W_Eta","GenTopHad_W_Eta[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopLep_Eta","#eta(t_{lep})",40,-2.5,2.5,40,-2.5,2.5),
            "RecoTTZ_TopLep_Eta","GenTopLep_Eta[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopLep_B_Eta","#eta(b_{lep})",40,-2.5,2.5,40,-2.5,2.5),
            "RecoTTZ_TopLep_BJet_Eta","GenTopLep_B_Eta[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopLep_W_Eta","#eta(W_{lep})",40,-2.5,2.5,40,-2.5,2.5),
            "RecoTTZ_TopLep_W_Eta","GenTopLep_W_Eta[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Z_Eta","#eta(Z)",40,-2.5,2.5,40,-2.5,2.5),
            "RecoTTZ_Z_Eta","GenZ_Eta",selection6,label6),
        
        # phi
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopHad_Phi","#phi(t_{had})",40,-3.141,3.141,40,-3.141,3.141),
            "RecoTTZ_TopHad_Phi","GenTopHad_Phi[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopHad_B_Phi","#phi(b_{had})",40,-3.141,3.141,40,-3.141,3.141),
            "RecoTTZ_TopHad_BJet_Phi","GenTopHad_B_Phi[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopHad_W_Phi","#phi(W_{had})",40,-3.141,3.141,40,-3.141,3.141),
            "RecoTTZ_TopHad_W_Phi","GenTopHad_W_Phi[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopLep_Phi","#phi(t_{lep})",40,-3.141,3.141,40,-3.141,3.141),
            "RecoTTZ_TopLep_Phi","GenTopLep_Phi[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopLep_B_Phi","#phi(b_{lep})",40,-3.141,3.141,40,-3.141,3.141),
            "RecoTTZ_TopLep_BJet_Phi","GenTopLep_B_Phi[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopLep_W_Phi","#phi(W_{lep})",40,-3.141,3.141,40,-3.141,3.141),
            "RecoTTZ_TopLep_W_Phi","GenTopLep_W_Phi[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Z_Phi","#phi(Z)",40,-3.141,3.141,40,-3.141,3.141),
            "RecoTTZ_Z_Phi","GenZ_Phi",selection6,label6),
    
        # pt
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopHad_Pt","p_{T}(t_{had})",40,0.,500.,40,0.,500.),
            "RecoTTZ_TopHad_Pt","GenTopHad_Pt[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopHad_B_Pt","p_{T}(b_{had})",40,0.,500.,40,0.,500.),
            "RecoTTZ_TopHad_BJet_Pt","GenTopHad_B_Pt[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopHad_W_Pt","p_{T}(W_{had})",40,0.,500.,40,0.,500.),
            "RecoTTZ_TopHad_W_Pt","GenTopHad_W_Pt[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopLep_Pt","p_{T}(t_{lep})",40,0.,500.,40,0.,500.),
            "RecoTTZ_TopLep_Pt","GenTopLep_Pt[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopLep_B_Pt","p_{T}(b_{lep})",40,0.,500.,40,0.,500.),
            "RecoTTZ_TopLep_BJet_Pt","GenTopLep_B_Pt[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_TopLep_W_Pt","p_{T}(W_{lep})",40,0.,500.,40,0.,500.),
            "RecoTTZ_TopLep_W_Pt","GenTopLep_W_Pt[0]",selection,label),
        plotClasses.TwoDimPlot(
            ROOT.TH2D("recoVSgen_Z_Pt","p_{T}(Z)",40,0.,500.,40,0.,500.),
            "RecoTTZ_Z_Pt","GenZ_Pt",selection6,label6),
        ]

    return plots




def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += recogen_plots(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    
if __name__ == "__main__":
    getDiscriminatorPlots()
