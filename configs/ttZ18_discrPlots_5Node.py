
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

    ndefaultbins = 20
    category_dict = {}
    this_dict = {}




    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.86

    this_dict["ljets_ge4j_ge4t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.78

    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.96

    this_dict["ljets_ge4j_ge4t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.8

    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.81

    this_dict["ljets_ge4j_ge4t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttZ"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.99

    this_dict["ljets_ge6j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttH"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.76

    this_dict["ljets_ge6j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_tthf"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.9

    this_dict["ljets_ge6j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttcc"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.63

    this_dict["ljets_ge6j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttlf"
    category_dict["catlabel"] = "\geq 6 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.61

    this_dict["ljets_ge6j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==0))","ljets_le5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttZ"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.92

    this_dict["ljets_le5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==1))","ljets_le5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttH"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.73

    this_dict["ljets_le5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==2))","ljets_le5j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_tthf"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.87

    this_dict["ljets_le5j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==3))","ljets_le5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttcc"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.55

    this_dict["ljets_le5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==4))","ljets_le5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttlf"
    category_dict["catlabel"] = "\leq 5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.71

    this_dict["ljets_le5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 5j_ge3t

    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==0))","ljets_5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttZ"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.97

    this_dict["ljets_5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttH"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.76

    this_dict["ljets_5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_tthf"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.86

    this_dict["ljets_5j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttcc"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.59

    this_dict["ljets_5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttlf"
    category_dict["catlabel"] = "5 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.67

    this_dict["ljets_5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==0))","ljets_ge4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.91

    this_dict["ljets_ge4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==1))","ljets_ge4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.73

    this_dict["ljets_ge4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==2))","ljets_ge4j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.88

    this_dict["ljets_ge4j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==3))","ljets_ge4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.57

    this_dict["ljets_ge4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==4))","ljets_ge4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.77

    this_dict["ljets_ge4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 4j_ge3t

    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==0))","ljets_4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttZ"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.95

    this_dict["ljets_4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttH"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.76

    this_dict["ljets_4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_tthf"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.94

    this_dict["ljets_4j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttcc"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.6

    this_dict["ljets_4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttlf"
    category_dict["catlabel"] = "4 jets, \geq 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.74

    this_dict["ljets_4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttZ"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.93

    this_dict["ljets_ge4j_3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.64

    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_tthf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.86

    this_dict["ljets_ge4j_3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.6

    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.72

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
    discriminatorPlots += plots_ge4j_ge4t(data)
    discriminatorPlots += plots_ge6j_ge3t(data)
    discriminatorPlots += plots_le5j_ge3t(data)
    discriminatorPlots += plots_5j_ge3t(data)
    discriminatorPlots += plots_ge4j_ge3t(data)
    discriminatorPlots += plots_4j_ge3t(data)
    discriminatorPlots += plots_ge4j_3t(data)
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
    