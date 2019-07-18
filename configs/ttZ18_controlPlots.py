
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
        plotClasses.Plot(ROOT.TH1D("inclusive_Jet_Pt_0","p_{T} of leading jet",50,30.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_BTagsM","number of b-tags (medium)",5,2.5,5.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_N_Jets","number of reconstructed jets",10,3.5,13.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_CSV_0","highest b-tag value",50,0.3,1.),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_JetCSV_0","b-tag value of leading jet",50,0.,1.),"Jet_CSV[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Pt","p_{T}(electron)",40,20,200),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Eta","#eta(electron)",40,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Electron_Phi","#phi(electron)",40,-3.1416,3.1416),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Pt","p_{T}(muon)",40,20,200),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Eta","#eta(muon)",40,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Muon_Phi","#phi(muon)",40,-3.1416,3.1416),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Pt","p_{T}(lepton)",40,20,200),"LooseLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Eta","#eta(lepton)",40,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("inclusive_Lepton_Phi","#phi(lepton)",40,-3.1416,3.1416),"LooseLepton_Phi[0]",selection,label),

        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge4j_ge4t(data=None):
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_M_0","mass of leading jet",50,10.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",50,1.0,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,30.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",50,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",50,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_avg","average b-tag value",50,0.2,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,30.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,30.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_h0","first fox wolfram moment",50,0.2,0.43),"Evt_h0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_dev","average deviation of b-tag value",50,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_3","fourth highest b-tag value",50,0.3,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_0","p_{T} of leading jet",50,30.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsM","number of b-tags (medium)",3,3.5,6.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,2.5),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsL","number of b-tags (loose)",5,3.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,30.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",50,0.4,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,30.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots
def plots_ge6j_ge3t(data=None):
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Z_BJet2_Pt","ttZ reconstruction p_{T}(b_{Z})[1]",50,30.0,200.0),"RecoTTZ_Z_BJet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,30.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_0","mass of leading jet",50,10.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,30.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Z_M","ttZ reconstruction M(Z)",50,30.0,300.0),"RecoTTZ_Z_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",50,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Chi2Z","ttZ reconstruction #chi^{2}(Z)",50,0.0,300.0),"RecoTTZ_Chi2Z",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",50,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,30.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_dev","average deviation of b-tag value",50,0.02,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_3","fourth highest b-tag value",50,0.0,1.0),"CSV[3]",selection,label),

        # control plots
        plotClasses.Plot(ROOT.TH1D("control_Z_over_H_Chi2LLH","#chi^{2}(Z)/#chi^{2}(H)",50,0.0,10.0),"RecoTTZ_Chi2Z/(RecoTTH_Chi2Higgs+1e-30)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2Z_percentage","#chi^{2}(Z)/(#chi^{2}(Z) + #chi^{2}(H))",50,0.0,1.0),"RecoTTZ_Chi2Z/(RecoTTH_Chi2Higgs+RecoTTZ_Chi2Z)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Z_vs_H_Chi2Difference","#chi^{2}(Z) - #chi^{2}(H)",50,-10.,10.),"RecoTTZ_Chi2Z-RecoTTH_Chi2Higgs",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Z","#chi^{2}(Z)",50,0.0,10.0),"RecoTTZ_Chi2Z",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Higgs","#chi^{2}(H)",50,0.0,10.0),"RecoTTH_Chi2Higgs",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Higgs_log","log(#chi^{2}(H))",50,-20,20),"log(RecoTTH_Chi2Higgs+1e-30)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Z_log","log(#chi^{2}(Z))",50,-20,20),"log(RecoTTZ_Chi2Z+1e-30)",selection,label),

        plotClasses.Plot(ROOT.TH1D("control_Z_over_H_Chi2LLH_mirrored","#chi^{2}(Z)/#chi^{2}(H)",50,0.0,10.0),"Chi2Z_mirror/(Chi2Higgs_mirror+1e-30)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2Z_percentage_mirrored","#chi^{2}(Z)/(#chi^{2}(Z) + #chi^{2}(H))",50,0.0,1.0),"Chi2Z_mirror/(Chi2Higgs_mirror+Chi2Z_mirror)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Z_vs_H_Chi2Difference_mirrored","#chi^{2}(Z) - #chi^{2}(H)",50,-1,1),"Chi2Z_mirror-Chi2Higgs_mirror",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Z_mirrored","#chi^{2}(Z)_mirrored",50,0.0,1.),"Chi2Z_mirror",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Higgs_mirrored","#chi^{2}(H)_mirrired",50,0.0,1.),"Chi2Higgs_mirror",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Higgs_log_mirrored","log(#chi^{2}(H))",50,-50.,0.),"log(Chi2Higgs_mirror+1e-30)",selection,label),
        plotClasses.Plot(ROOT.TH1D("control_Chi2_Z_log_mirrored","log(#chi^{2}(Z))",50,-50.,0.),"log(Chi2Z_mirror+1e-30)",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots
def plots_le5j_ge3t(data=None):
    label = "\leq 5 jets, \geq 3 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",50,30.0,140.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",50,30.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_0","p_{T} of leading jet",50,30.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",50,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_0","mass of leading jet",50,10.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_MHT","missing H_{T}",50,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,30.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,30.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,30.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",50,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_avg","average b-tag value",50,0.2,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_3","fourth highest b-tag value",50,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots
def plots_5j_ge3t(data=None):
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",50,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",50,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_0","mass of leading jet",50,10.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,20.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_MHT","missing H_{T}",50,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_avg","average b-tag value",50,0.2,0.8),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",50,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,30.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_dev","average deviation of b-tag value",50,0.02,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,30.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,30.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_3","fourth highest b-tag value",50,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots
def plots_ge4j_ge3t(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",50,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,30.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",50,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,30.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,30.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_M_0","mass of leading jet",50,10.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",50,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_0","p_{T} of leading jet",50,30.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_avg","average b-tag value",50,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,30.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_3","fourth highest b-tag value",50,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots
def plots_4j_ge3t(data=None):
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Chi2TopHad","ttZ reconstruction #chi^{2}(t_{had})",50,0.0,300.0),"RecoTTZ_Chi2TopHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,30.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_0","mass of leading jet",50,10.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,30.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Chi2WHad","ttZ reconstruction #chi^{2}(W_{had})",50,0.0,300.0),"RecoTTZ_Chi2WHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_minDrJets","M_{2}( min #DeltaR(jet,jet) )",50,30.0,300.0),"Evt_M2_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",50,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",50,20.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",50,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,30.,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_dev","average deviation of b-tag value",50,0.0,0.2),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopHad_Pt","ttZ reconstruction p_{T}(t_{had})",50,0.0,700.0),"RecoTTZ_TopHad_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_MHT","missing H_{T}",50,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,20.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots
def plots_ge4j_3t(data=None):
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_2","third highest b-tag value",50,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",50,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",50,30.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",50,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",50,30.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",50,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",50,20.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",50,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_MTW","MTW",50,0.0,300.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",50,30.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_0","mass of leading jet",50,10.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_JetsAverage","average M(jets)",50,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",50,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_0","p_{T} of leading jet",50,30.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_avg","average b-tag value",50,0.1,0.8),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",50,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",50,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",50,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_TaggedJetsAverage","average M(tags)",50,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]
    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += control_plots(data)
    discriminatorPlots += plots_ge4j_ge4t(data)
    discriminatorPlots += plots_ge6j_ge3t(data)
    discriminatorPlots += plots_le5j_ge3t(data)
    #discriminatorPlots += plots_5j_ge3t(data)
    discriminatorPlots += plots_ge4j_ge3t(data)
    #discriminatorPlots += plots_4j_ge3t(data)
    discriminatorPlots += plots_ge4j_3t(data)

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
