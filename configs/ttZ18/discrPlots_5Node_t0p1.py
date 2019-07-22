
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(os.path.dirname(filedir))
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


def plots_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_RecoTTZ_cosdTheta_Lep_bHad","ttZ reconstruction cos#Delta#theta(lep,b_{had})",50,-1.0,1.0),"RecoTTZ_cosdTheta_Lep_bHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_1","p_{T} of subleading jet",50,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_minDrJets","M_{2}( min #DeltaR(jet,jet) )",50,0.0,200.0),"Evt_M2_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsL","number of b-tags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_E_TaggedJetsAverage","average E(tags)",50,0.0,800.0),"Evt_E_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_3","p_{T} of fourth jet",30,50.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",50,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",50,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M3","M_{3} with highest p_{T}",50,50.0,1000.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_ge6j_ge3t(data = None):
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_0","mass of leading jet",50,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_E_TaggedJetsAverage","average E(tags)",50,0.0,800.0),"Evt_E_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",50,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_dev","average deviation of b-tag value",50,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",50,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Z_M","ttZ reconstruction M(Z)",50,0.0,300.0),"RecoTTZ_Z_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_3","fourth highest b-tag value",50,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Chi2Z","ttZ reconstruction #chi^{2}(Z)",50,0.0,300.0),"RecoTTZ_Chi2Z",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_le5j_ge3t(data = None):
    label = "\leq 5 jets, \geq 3 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_0","mass of leading jet",50,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",50,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_Total","total mass",50,250.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_avg","average b-tag value",50,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_3","fourth highest b-tag value",50,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_5j_ge3t(data = None):
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_MHT","missing H_{T}",50,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M3","M_{3} with highest p_{T}",50,50.0,1000.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_0","mass of leading jet",50,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",50,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_dev","average deviation of b-tag value",50,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_Total","total mass",50,250.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_avg","average b-tag value",50,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_ge4j_ge3t(data = None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",50,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_Total","total mass",50,250.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",50,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",50,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_avg","average b-tag value",50,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_3","fourth highest b-tag value",50,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_4j_ge3t(data = None):
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",50,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_dev","average deviation of b-tag value",50,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Chi2WHad","ttZ reconstruction #chi^{2}(W_{had})",50,0.0,300.0),"RecoTTZ_Chi2WHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopLep_W_Pt","ttZ reconstruction p_{T}(W_{lep})",50,0.0,500.0),"RecoTTZ_TopLep_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_MHT","missing H_{T}",50,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",50,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_0","mass of leading jet",50,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_avg","average b-tag value",50,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_minDrJets","M_{2}( min #DeltaR(jet,jet) )",50,0.0,200.0),"Evt_M2_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",50,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_0","p_{T} of leading jet",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_dev","average deviation of b-tag value",50,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_Total","total mass",50,250.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_3","fourth highest b-tag value",50,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",50,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",50,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_avg","average b-tag value",50,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots




def plots_dnn(data, discrname):

    ndefaultbins = 15
    category_dict = {}
    this_dict = {}




    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.266,
				0.299,
				0.332,
				0.365,
				0.398,
				0.431,
				0.464,
				0.497,
				0.53,
				0.596,
				0.86
				]
    this_dict["ljets_ge4j_ge4t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.258,
				0.287,
				0.316,
				0.345,
				0.374,
				0.403,
				0.432,
				0.461,
				0.49,
				0.519,
				0.548,
				0.606,
				0.78
				]
    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.276,
				0.314,
				0.352,
				0.39,
				0.428,
				0.466,
				0.504,
				0.542,
				0.58,
				0.618,
				0.656,
				0.694,
				0.732,
				0.808,
				0.96
				]
    this_dict["ljets_ge4j_ge4t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.26,
				0.29,
				0.32,
				0.35,
				0.38,
				0.41,
				0.44,
				0.47,
				0.5,
				0.8
				]
    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.261,
				0.2915,
				0.322,
				0.3525,
				0.383,
				0.4135,
				0.444,
				0.4745,
				0.505,
				0.5355,
				0.566,
				0.5965,
				0.627,
				0.81
				]
    this_dict["ljets_ge4j_ge4t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttZ"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2395,
				0.279,
				0.3185,
				0.358,
				0.3975,
				0.437,
				0.4765,
				0.516,
				0.5555,
				0.595,
				0.99
				]
    this_dict["ljets_ge6j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttH"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.256,
				0.284,
				0.312,
				0.34,
				0.368,
				0.396,
				0.424,
				0.452,
				0.48,
				0.508,
				0.536,
				0.564,
				0.592,
				0.76
				]
    this_dict["ljets_ge6j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_tthf"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.235,
				0.27,
				0.305,
				0.34,
				0.375,
				0.41,
				0.445,
				0.48,
				0.515,
				0.55,
				0.585,
				0.62,
				0.655,
				0.69,
				0.9
				]
    this_dict["ljets_ge6j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttcc"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.243,
				0.2645,
				0.286,
				0.3075,
				0.329,
				0.3505,
				0.372,
				0.3935,
				0.415,
				0.4365,
				0.63
				]
    this_dict["ljets_ge6j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttlf"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.241,
				0.2615,
				0.282,
				0.3025,
				0.323,
				0.3435,
				0.364,
				0.3845,
				0.405,
				0.4255,
				0.446,
				0.4665,
				0.487,
				0.5075,
				0.528,
				0.61
				]
    this_dict["ljets_ge6j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==0))","ljets_le5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttZ"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.236,
				0.272,
				0.308,
				0.344,
				0.38,
				0.416,
				0.452,
				0.488,
				0.524,
				0.56,
				0.596,
				0.92
				]
    this_dict["ljets_le5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==1))","ljets_le5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttH"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2265,
				0.253,
				0.2795,
				0.306,
				0.3325,
				0.359,
				0.3855,
				0.412,
				0.4385,
				0.465,
				0.4915,
				0.518,
				0.5445,
				0.571,
				0.5975,
				0.73
				]
    this_dict["ljets_le5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==2))","ljets_le5j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_tthf"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2335,
				0.267,
				0.3005,
				0.334,
				0.3675,
				0.401,
				0.4345,
				0.468,
				0.5015,
				0.535,
				0.5685,
				0.602,
				0.6355,
				0.669,
				0.7025,
				0.736,
				0.87
				]
    this_dict["ljets_le5j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==3))","ljets_le5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttcc"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.235,
				0.2525,
				0.27,
				0.2875,
				0.305,
				0.3225,
				0.34,
				0.3575,
				0.375,
				0.3925,
				0.41,
				0.4275,
				0.445,
				0.4625,
				0.48,
				0.55
				]
    this_dict["ljets_le5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==4))","ljets_le5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttlf"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2255,
				0.251,
				0.2765,
				0.302,
				0.3275,
				0.353,
				0.3785,
				0.404,
				0.4295,
				0.455,
				0.4805,
				0.506,
				0.5315,
				0.557,
				0.5825,
				0.608,
				0.6335,
				0.71
				]
    this_dict["ljets_le5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 5j_ge3t

    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==0))","ljets_5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttZ"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2385,
				0.277,
				0.3155,
				0.354,
				0.3925,
				0.431,
				0.4695,
				0.508,
				0.5465,
				0.6235,
				0.97
				]
    this_dict["ljets_5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttH"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.228,
				0.256,
				0.284,
				0.312,
				0.34,
				0.368,
				0.396,
				0.424,
				0.452,
				0.48,
				0.508,
				0.536,
				0.564,
				0.76
				]
    this_dict["ljets_5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_tthf"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.233,
				0.266,
				0.299,
				0.332,
				0.365,
				0.398,
				0.431,
				0.464,
				0.497,
				0.53,
				0.563,
				0.596,
				0.629,
				0.662,
				0.695,
				0.728,
				0.86
				]
    this_dict["ljets_5j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttcc"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.239,
				0.2585,
				0.278,
				0.2975,
				0.317,
				0.3365,
				0.356,
				0.3755,
				0.395,
				0.4145,
				0.434,
				0.4535,
				0.59
				]
    this_dict["ljets_5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttlf"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.247,
				0.2705,
				0.294,
				0.3175,
				0.341,
				0.3645,
				0.388,
				0.4115,
				0.435,
				0.4585,
				0.482,
				0.5055,
				0.529,
				0.5525,
				0.576,
				0.67
				]
    this_dict["ljets_5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==0))","ljets_ge4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2355,
				0.271,
				0.3065,
				0.342,
				0.3775,
				0.413,
				0.4485,
				0.484,
				0.5195,
				0.555,
				0.5905,
				0.626,
				0.91
				]
    this_dict["ljets_ge4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==1))","ljets_ge4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2265,
				0.253,
				0.2795,
				0.306,
				0.3325,
				0.359,
				0.3855,
				0.412,
				0.4385,
				0.465,
				0.4915,
				0.518,
				0.5445,
				0.571,
				0.5975,
				0.73
				]
    this_dict["ljets_ge4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==2))","ljets_ge4j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.234,
				0.268,
				0.302,
				0.336,
				0.37,
				0.404,
				0.438,
				0.472,
				0.506,
				0.54,
				0.574,
				0.608,
				0.642,
				0.676,
				0.71,
				0.744,
				0.88
				]
    this_dict["ljets_ge4j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==3))","ljets_ge4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2185,
				0.237,
				0.2555,
				0.274,
				0.2925,
				0.311,
				0.3295,
				0.348,
				0.3665,
				0.385,
				0.4035,
				0.422,
				0.4405,
				0.459,
				0.4775,
				0.496,
				0.57
				]
    this_dict["ljets_ge4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==4))","ljets_ge4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2285,
				0.257,
				0.2855,
				0.314,
				0.3425,
				0.371,
				0.3995,
				0.428,
				0.4565,
				0.485,
				0.5135,
				0.542,
				0.5705,
				0.599,
				0.6275,
				0.656,
				0.6845,
				0.713,
				0.7415,
				0.77
				]
    this_dict["ljets_ge4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 4j_ge3t

    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==0))","ljets_4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttZ"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2375,
				0.275,
				0.3125,
				0.35,
				0.3875,
				0.425,
				0.4625,
				0.5,
				0.5375,
				0.575,
				0.65,
				0.95
				]
    this_dict["ljets_4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttH"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.228,
				0.256,
				0.284,
				0.312,
				0.34,
				0.368,
				0.396,
				0.424,
				0.452,
				0.48,
				0.508,
				0.536,
				0.564,
				0.76
				]
    this_dict["ljets_4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_tthf"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.237,
				0.274,
				0.311,
				0.348,
				0.385,
				0.422,
				0.459,
				0.496,
				0.533,
				0.57,
				0.607,
				0.644,
				0.681,
				0.718,
				0.94
				]
    this_dict["ljets_4j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttcc"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.24,
				0.26,
				0.28,
				0.3,
				0.32,
				0.34,
				0.36,
				0.38,
				0.4,
				0.42,
				0.44,
				0.46,
				0.6
				]
    this_dict["ljets_4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttlf"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.227,
				0.254,
				0.281,
				0.308,
				0.335,
				0.362,
				0.389,
				0.416,
				0.443,
				0.47,
				0.497,
				0.524,
				0.551,
				0.578,
				0.605,
				0.74
				]
    this_dict["ljets_4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2365,
				0.273,
				0.3095,
				0.346,
				0.3825,
				0.419,
				0.4555,
				0.492,
				0.5285,
				0.565,
				0.6015,
				0.93
				]
    this_dict["ljets_ge4j_3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.222,
				0.244,
				0.266,
				0.288,
				0.31,
				0.332,
				0.354,
				0.376,
				0.398,
				0.42,
				0.442,
				0.464,
				0.486,
				0.508,
				0.53,
				0.64
				]
    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.233,
				0.266,
				0.299,
				0.332,
				0.365,
				0.398,
				0.431,
				0.464,
				0.497,
				0.53,
				0.563,
				0.596,
				0.629,
				0.662,
				0.695,
				0.728,
				0.86
				]
    this_dict["ljets_ge4j_3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.22,
				0.24,
				0.26,
				0.28,
				0.3,
				0.32,
				0.34,
				0.36,
				0.38,
				0.4,
				0.42,
				0.44,
				0.46,
				0.6
				]
    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.226,
				0.252,
				0.278,
				0.304,
				0.33,
				0.356,
				0.382,
				0.408,
				0.434,
				0.46,
				0.486,
				0.512,
				0.538,
				0.564,
				0.59,
				0.616,
				0.642,
				0.668,
				0.694,
				0.72
				]
    this_dict["ljets_ge4j_3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    

    for l in this_dict:
        this_dict[l]["histoname"] = discrname+"_"+l
        this_dict[l]["histotitle"] = "final discriminator ({})".format(l)
        this_dict[l]["plotPreselections"] = this_dict[l]["category"][0]

    DNNPlots = init_plots(dictionary = this_dict, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    #discriminatorPlots += plots_ge4j_ge4t(data)
    #discriminatorPlots += plots_ge6j_ge3t(data)
    #discriminatorPlots += plots_le5j_ge3t(data)
    #discriminatorPlots += plots_5j_ge3t(data)
    #discriminatorPlots += plots_ge4j_ge3t(data)
    #discriminatorPlots += plots_4j_ge3t(data)
    #discriminatorPlots += plots_ge4j_3t(data)
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def init_plots(dictionary, data = None):
    plots = [] #init list of plotClasses objects to return
    for label in dictionary:
        subdict     = dictionary[label] #for easy access
        discr       = subdict["discr"] # load discriminator name
        sel         = subdict["plotPreselections"] # load selection
        histoname   = subdict["histoname"] # load histogram name
        histotitle  = subdict["histotitle"] # load histogram title
        catlabel    = subdict["catlabel"] # category label

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if "bin_edges" in subdict:
            bins  = array("f", subdict["bin_edges"])
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            subdict["nhistobins"] = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname,histotitle,nbins,bins),
                    discr,sel,catlabel))

        elif "minxval" in subdict and "maxxval" in subdict:
            nbins = subdict["nhistobins"]
            xmax  = subdict["maxxval"]
            xmin  = subdict["minxval"]
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname, histotitle,nbins,xmin, xmax),
                    discr,sel,catlabel))

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    
