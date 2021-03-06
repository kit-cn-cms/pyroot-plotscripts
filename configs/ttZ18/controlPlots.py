
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

def reco_plots(data=None):
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("inclusive_eventYields","event yields",6,0.5,6.5),jtYieldExpression,selection,label),

        plotClasses.Plot(ROOT.TH1D("control_Chi2_Z","#chi^{2}(Z)",40,0.0,10.0),"RecoTTZ_Chi2Z",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Z_log","log(#chi^{2}(Z))",40,-10,7),"log(RecoTTZ_Chi2Z+1e-30)",selection,label),
        #plotClasses.Plot(ROOT.TH1D("control_Chi2_Z_over_H_likelihood","#chi^{2}(Z)/#chi^{2}(H)",40,0.0,20.0),"RecoTTZ_Chi2Z/(RecoTTH_Chi2Higgs+1e-30)",selection,label),
        #plotClasses.Plot(ROOT.TH1D("control_Chi2_Z_percentage","#chi^{2}(Z)/(#chi^{2}(Z) + #chi^{2}(H))",40,0.0,1.0),"RecoTTZ_Chi2Z/(RecoTTH_Chi2Higgs+RecoTTZ_Chi2Z)",selection,label),
        #plotClasses.Plot(ROOT.TH1D("control_Chi2_Higgs","#chi^{2}(H)",40,0.0,10.0),"RecoTTH_Chi2Higgs",selection,label),
        #plotClasses.Plot(ROOT.TH1D("control_Chi2_Higgs_log","log(#chi^{2}(H))",40,-10,7),"log(RecoTTH_Chi2Higgs+1e-30)",selection,label),

        plotClasses.Plot(ROOT.TH1D("control_RecoTTZ_TopHad_M_log","log(M(t_{had}))",40,4.5,6.5),"log(RecoTTZ_TopHad_M)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_RecoTTZ_TopLep_M_log","log(M(t_{lep}))",40,4.5,6.5),"log(RecoTTZ_TopLep_M)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_RecoTTZ_Z_M_log","log(M(Z))",40,3.5,6.5),"log(RecoTTZ_Z_M)",selection,label),

        plotClasses.Plot(ROOT.TH1D("control_Evt_blr","b-tag likelihood ratio",40,0.,1.),"Evt_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Evt_blr_transformed","transformed b-tag likelihood ratio",40,-7,15.),"Evt_blr_transformed",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots



def control_plots(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    plots = [
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

        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_blr","b-tag likelihood ratio",40,0.,1.),"Evt_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Evt_blr_transformed","transformed b-tag likelihood ratio",40,-7,15.),"Evt_blr_transformed",selection,label),

        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots




def plots_ge6j_ge3t(data = None):
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_CSV_2","third highest b-tag value",30,0.275,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,0.8),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_CSV_4","fifth highest b-tag value",30,0.0,0.2),"CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_CSV_5","sixth highest b-tag value",30,0.0,0.1),"CSV[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",30,0.275,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.02,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_E_TaggedJetsAverage","average E(tags)",30,50.0,500.0),"Evt_E_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_HT_wo_MET","H_{T} without MET",30,300.0,1500.0),"Evt_HT_wo_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,30.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,30.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,40.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,20.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Pt_JetsAverage","average p_{T}(jets)",30,30.0,250.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Pt_TaggedJetsAverage","average p_{T}(tags)",30,30.0,300.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Jet_M_0","mass of leading jet",30,5.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,50.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_N_BTagsM","number of b-tags (medium)",3,2.5,5.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_RecoTTZ_Chi2Z","ttZ reconstruction #chi^{2}(Z)",30,0.0,30.0),"RecoTTZ_Chi2Z",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_RecoTTZ_Z_BJet2_Pt","ttZ reconstruction second p_{T}(b_{Z})",30,30.0,200.0),"RecoTTZ_Z_BJet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_RecoTTZ_Z_M","ttZ reconstruction M(Z)",30,30.0,250.0),"RecoTTZ_Z_M",selection,label),
        ]

    write_config("ge6j_ge3t", plots)
    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_5j_ge3t(data = None):
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_CSV_2","third highest b-tag value",30,0.275,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,0.3),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_CSV_avg","average b-tag value",30,0.25,0.8),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",30,0.35,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.275,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,1.5,3.3),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M2_JetsAverage","average M_{2}(jets)",30,50.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,20.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,20.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,20.0,350.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M3","M_{3} with highest p_{T}",30,50.0,800.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,35.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M_Total","total mass",30,300.0,2000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,20.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Pt_JetsAverage","average p_{T}(jets)",30,40.0,250.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,50.0,500.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,450.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Jet_M_0","mass of leading jet",30,5.0,70.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,40.0,500.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,150.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_RecoTTZ_Chi2WHad","ttZ reconstruction #chi^{2}(W_{had})",30,0.0,300.0),"RecoTTZ_Chi2WHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_RecoTTZ_TopHad_W_Pt","ttZ reconstruction p_{T}(W_{had})",30,0.0,500.0),"RecoTTZ_TopHad_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_RecoTTZ_TopLep_BJet_Pt","ttZ reconstruction p_{T}(b_{lep})",30,30.0,300.0),"RecoTTZ_TopLep_BJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        ]

    write_config("5j_ge3t", plots)
    if data:
        add_data_plots(plots=plots,data=data)
    return plots




def plots_4j_ge3t(data = None):
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_CSV_2","third highest b-tag value",30,0.275,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,0.3),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_CSV_avg","average b-tag value",30,0.25,0.8),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.2),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_CSV_min","minimal b-tag value",30,0.0,0.3),"Evt_CSV_min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,20.0,250.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,20.0,250.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,20.0,350.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M3","M_{3} with highest p_{T}",30,50.0,800.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_MHT","missing H_{T}",30,0.0,300.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_MTW","MTW",30,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,35.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,50.0,500.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,25.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Jet_DeepJetCSV_3","DeepJet b-tag value of fourth jet",30,0.0,1.0),"Jet_DeepJetCSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Jet_M_0","mass of leading jet",30,5.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,50.0,500.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,100.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_Chi2TopHad","ttZ reconstruction #chi^{2}(t_{had})",30,0.0,100.0),"RecoTTZ_Chi2TopHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_Chi2TopLep","ttZ reconstruction #chi^{2}(t_{lep})",30,0.0,100.0),"RecoTTZ_Chi2TopLep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_Chi2Total","ttZ reconstruction #chi^{2}",30,0.0,200.0),"RecoTTZ_Chi2Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_Chi2WHad","ttZ reconstruction #chi^{2}(W_{had})",30,0.0,100.0),"RecoTTZ_Chi2WHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_TopHad_Pt","ttZ reconstruction p_{T}(t_{had})",30,0.0,600.0),"RecoTTZ_TopHad_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        ]

    write_config("4j_ge3t", plots)
    if data:
        add_data_plots(plots=plots,data=data)
    return plots




def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge6j_ge3t(data)
    discriminatorPlots += plots_5j_ge3t(data)
    discriminatorPlots += plots_4j_ge3t(data)
    discriminatorPlots += control_plots(data)
    discriminatorPlots += reco_plots(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    
if __name__ == "__main__":
    getDiscriminatorPlots()
