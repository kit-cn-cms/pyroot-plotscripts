
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

def control_plots():
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_BTagsM","number of b-tags (medium)",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_Jets","number of reconstructed jets",10,1.5,11.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_CSV_0","highest b-tag value",30,0.3,1.),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_JetCSV_0","b-tag value of leading jet",30,0.,1.),"Jet_CSV[0]",selection,label),
        ]
    return plots


def plots_ge4j_ge4t():
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_h0","first fox wolfram moment",30,0.2,0.45),"Evt_h0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsM","number of b-tags (medium)",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsL","number of b-tags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",30,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        ]

    return plots
def plots_ge6j_ge3t():
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Z_BJet2_Pt","ttZ reconstruction p_{T}(b_{Z})[1]",30,0.0,200.0),"RecoTTZ_Z_BJet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_JetsAverage","average M(jets)",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Z_M","ttZ reconstruction M(Z)",30,0.0,300.0),"RecoTTZ_Z_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Chi2Z","ttZ reconstruction #chi^{2}(Z)",30,0.0,300.0),"RecoTTZ_Chi2Z",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_MTW","MTW",30,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),

        # control plots
        plotClasses.Plot(ROOT.TH1D("control_Z_over_H_Chi2LLH","LLH #chi^{2}(Z)/#chi^{2}(H)",50,0.0,10.0),"RecoTTZ_Chi2Z/(RecoTTH_Chi2Higgs+1e-30)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2Z_percentage","LLH #chi^{2}(Z)/(#chi^{2}(Z) + #chi^{2}(H))",50,0.0,1.0),"RecoTTZ_Chi2Z/(RecoTTH_Chi2Higgs+RecoTTZ_Chi2Z)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Z_vs_H_Chi2Difference","LLH #chi^{2}(Z) - #chi^{2}(H)",50,-10.,10.),"RecoTTZ_Chi2Z-RecoTTH_Chi2Higgs",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Z","LLH #chi^{2}(Z)",50,0.0,10.0),"RecoTTZ_Chi2Z",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Higgs","LLH #chi^{2}(H)",50,0.0,10.0),"RecoTTH_Chi2Higgs",selection,label),
        ]

    return plots
def plots_le5j_ge3t():
    label = "\leq 5 jets, \geq 3 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,50.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_MHT","missing H_{T}",30,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_MTW","MTW",30,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots
def plots_5j_ge3t():
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_MHT","missing H_{T}",30,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_MTW","MTW",30,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        ]

    return plots
def plots_ge4j_ge3t():
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_MTW","MTW",30,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_JetsAverage","average M(jets)",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        ]

    return plots
def plots_4j_ge3t():
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Chi2TopHad","ttZ reconstruction #chi^{2}(t_{had})",30,0.0,300.0),"RecoTTZ_Chi2TopHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Chi2WHad","ttZ reconstruction #chi^{2}(W_{had})",30,0.0,300.0),"RecoTTZ_Chi2WHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_minDrJets","M_{2}( min #DeltaR(jet,jet) )",30,0.0,200.0),"Evt_M2_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopHad_Pt","ttZ reconstruction p_{T}(t_{had})",30,0.0,700.0),"RecoTTZ_TopHad_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_MTW","MTW",30,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_MHT","missing H_{T}",30,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        ]

    return plots
def plots_ge4j_3t():
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_MTW","MTW",30,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_JetsAverage","average M(jets)",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += control_plots()
    discriminatorPlots += plots_ge4j_ge4t()
    discriminatorPlots += plots_ge6j_ge3t()
    discriminatorPlots += plots_le5j_ge3t()
    discriminatorPlots += plots_5j_ge3t()
    discriminatorPlots += plots_ge4j_ge3t()
    discriminatorPlots += plots_4j_ge3t()
    discriminatorPlots += plots_ge4j_3t()

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
    
