
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


def plots_ge4j_ge4t():
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_RecoTTZ_cosdTheta_Lep_topHad","ttZ reconstruction cos#Delta#theta(lep,t_{had})",30,-1.0,1.0),"RecoTTZ_cosdTheta_Lep_topHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_RecoTTZ_TopLep_BJet_Pt","ttZ reconstruction p_{T}(b_{lep})",30,0.0,400.0),"RecoTTZ_TopLep_BJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_min","minimal b-tag value",30,0.0,1.0),"Evt_CSV_min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Eta_1","#eta of subleading jet",30,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Phi_0","#phi of leading jet",30,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_RecoTTZ_Dphi_bLep_wLep","ttZ reconstruction #Delta#phi(b_{lep},W_{lep})",30,0.0,6.28318530718),"RecoTTZ_Dphi_bLep_wLep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_RecoTTZ_TopLep_BJet_E","ttZ reconstruction E(b_{lep})",30,0.0,600.0),"RecoTTZ_TopLep_BJet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsT","number of b-tags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_E_1","energy of subleading jet",30,20.0,1000.0),"Jet_E[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_maxDrJets","#DeltaR( max #Delta#eta(jet,jet) )",30,2.0,5.5),"Evt_Dr_maxDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_RecoTTZ_TopHad_W_Phi","ttZ reconstruction #phi(W_{had})",30,-3.14159265359,3.14159265359),"RecoTTZ_TopHad_W_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M3","M_{3} closest to 175 GeV",30,100.0,1000.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_DeepJetCSV_1","DeepJet b-tag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_RecoTTZ_Dphi_bLep_topHad","ttZ reconstruction #Delta#phi(b_{lep},t_{had})",30,0.0,6.28318530718),"RecoTTZ_Dphi_bLep_topHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Eta_0","#eta of leading jet",30,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Eta_2","#eta of third jet",30,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Phi_1","#phi of subleading jet",30,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Phi_3","#phi of fourth jet",30,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_maxDrTaggedJets","#DeltaR( max #Delta#eta(tag,tag) )",30,0.0,5.0),"Evt_Dr_maxDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_1","second highest b-tag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_MTW","MTW",30,0.0,200.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsM","number of b-tags (medium)",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_h0","first fox wolfram moment",30,0.2,0.45),"Evt_h0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsL","number of b-tags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",30,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        ]

    return plots
def plots_ge6j_ge3t():
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Z_BJet2_E","ttZ reconstruction E(b_{Z})[1]",30,0.0,400.0),"RecoTTZ_Z_BJet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_BTagsT","number of b-tags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_1","mass of subleading jet",30,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M3_oneTagged","M_{3} closest to 175 GeV with one untagged jet",30,100.0,1000.0),"Evt_M3_oneTagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_0","highest b-tag value",30,0.3,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_minDrJets","#DeltaR( min #DeltaR(jet,jet) )",30,0.4,1.8),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_4","p_{T} of fifth jet",30,30.0,150.0),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_TopLep_BJet_Pt","ttZ reconstruction p_{T}(b_{lep})",30,0.0,400.0),"RecoTTZ_TopLep_BJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_4","mass of fifth jet",30,0.0,20.0),"Jet_M[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_1","DeepJet b-tag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_cosdTheta_Z_Lep","ttZ reconstruction cos#Delta#theta(Z,lep)",30,-1.0,1.0),"RecoTTZ_cosdTheta_Z_Lep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_minDrLepJet","#DeltaR( min #DeltaR(lep,jet) )",30,0.4,3.0),"Evt_Dr_minDrLepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_1","second highest b-tag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_min","minimal b-tag value",30,0.0,1.0),"Evt_CSV_min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_4","fifth highest b-tag value",30,0.0,1.0),"CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_5","mass of sixth jet",30,0.0,20.0),"Jet_M[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_MHT","missing H_{T}",30,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M3","M_{3} closest to 175 GeV",30,100.0,1000.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_BTagsM","number of b-tags (medium)",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_5","p_{T} of sixth jet",30,30.0,100.0),"Jet_Pt[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_JetsAverage","average M(jets)",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Z_BJet2_Pt","ttZ reconstruction p_{T}(b_{Z})[1]",30,0.0,200.0),"RecoTTZ_Z_BJet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_MTW","MTW",30,0.0,200.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Z_M","ttZ reconstruction M(Z)",30,0.0,300.0),"RecoTTZ_Z_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_RecoTTZ_Chi2Z","ttZ reconstruction #chi^{2}(Z)",30,0.0,300.0),"RecoTTZ_Chi2Z",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        ]

    return plots
def plots_le5j_ge3t():
    label = "\leq 5 jets, \geq 3 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_JetsAverage","average M_{2}(jets)",30,50.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_Deta_bLep_wLep","ttZ reconstruction #Delta#eta(b_{lep},W_{lep})",30,0.0,3.0),"RecoTTZ_Deta_bLep_wLep",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopHad_BJet_Pt","ttZ reconstruction p_{T}(b_{had})",30,0.0,400.0),"RecoTTZ_TopHad_BJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_1","mass of subleading jet",30,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopLep_BJet_Pt","ttZ reconstruction p_{T}(b_{lep})",30,0.0,400.0),"RecoTTZ_TopLep_BJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_1","DeepJet b-tag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_HT_wo_MET","H_{T} without MET",30,200.0,1500.0),"Evt_HT_wo_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_cosdTheta_bHad_wHad","ttZ reconstruction cos#Delta#theta(b_{had},W_{had})",30,-1.0,1.0),"RecoTTZ_cosdTheta_bHad_wHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_min","minimal b-tag value",30,0.0,1.0),"Evt_CSV_min",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_Total","total mass",30,250.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_N_BTagsL","number of b-tags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_minDrJets","#DeltaR( min #DeltaR(jet,jet) )",30,0.4,1.8),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_HT_jets","H_{T}(jets)",30,200.0,1500.0),"Evt_HT_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopLep_W_Pt","ttZ reconstruction p_{T}(W_{lep})",30,0.0,500.0),"RecoTTZ_TopLep_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopHad_Pt","ttZ reconstruction p_{T}(t_{had})",30,0.0,700.0),"RecoTTZ_TopHad_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_h1","second fox wolfram moment",30,-0.2,0.35),"Evt_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_minDrJets","M_{2}( min #DeltaR(jet,jet) )",30,0.0,200.0),"Evt_M2_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M3","M_{3} closest to 175 GeV",30,100.0,1000.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopHad_W_Pt","ttZ reconstruction p_{T}(W_{had})",30,0.0,500.0),"RecoTTZ_TopHad_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_JetsAverage","average M(jets)",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_MTW","MTW",30,0.0,200.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_MHT","missing H_{T}",30,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        ]

    return plots
def plots_5j_ge3t():
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_Deta_bLep_bHad","ttZ reconstruction #Delta#eta(b_{lep},b_{had})",30,0.0,4.5),"RecoTTZ_Deta_bLep_bHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopLep_Pt","ttZ reconstruction p_{T}(t_{lep})",30,0.0,700.0),"RecoTTZ_TopLep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopLep_W_Pt","ttZ reconstruction p_{T}(W_{lep})",30,0.0,500.0),"RecoTTZ_TopLep_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_h2","third fox wolfram moment",30,-0.1,0.3),"Evt_h2",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_4","mass of fifth jet",30,0.0,20.0),"Jet_M[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_JetsAverage","average M_{2}(jets)",30,50.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_N_BTagsL","number of b-tags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_DeepJetCSV_4","DeepJet b-tag value of fifth jet",30,0.0,1.0),"Jet_DeepJetCSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_JetPt_over_JetE","p_{T}(jets)/E(jets)",30,0.3,1.0),"Evt_JetPt_over_JetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_JetsAverage","average M(jets)",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopHad_Pt","ttZ reconstruction p_{T}(t_{had})",30,0.0,700.0),"RecoTTZ_TopHad_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_minDrJets","#DeltaR( min #DeltaR(jet,jet) )",30,0.4,1.8),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopLep_BJet_Pt","ttZ reconstruction p_{T}(b_{lep})",30,0.0,400.0),"RecoTTZ_TopLep_BJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_Total","total mass",30,250.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M3","M_{3} closest to 175 GeV",30,100.0,1000.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_h1","second fox wolfram moment",30,-0.2,0.35),"Evt_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_4","p_{T} of fifth jet",30,30.0,150.0),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_MHT","missing H_{T}",30,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_minDrJets","M_{2}( min #DeltaR(jet,jet) )",30,0.0,200.0),"Evt_M2_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopHad_W_Pt","ttZ reconstruction p_{T}(W_{had})",30,0.0,500.0),"RecoTTZ_TopHad_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_MTW","MTW",30,0.0,200.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        ]

    return plots
def plots_ge4j_ge3t():
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopHad_Pt","ttZ reconstruction p_{T}(t_{had})",30,0.0,700.0),"RecoTTZ_TopHad_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_min","minimal b-tag value",30,0.0,1.0),"Evt_CSV_min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_JetsAverage","average M_{2}(jets)",30,50.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrLepJet","#DeltaR( min #DeltaR(lep,jet) )",30,0.4,3.0),"Evt_Dr_minDrLepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrJets","#DeltaR( min #DeltaR(jet,jet) )",30,0.4,1.8),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_TaggedJetsAverage","average p_{T}(tags)",30,0.0,300.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_HT_tags","H_{T}(tags)",30,100.0,1000.0),"Evt_HT_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_BTagsL","number of b-tags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_1","second highest b-tag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_h1","second fox wolfram moment",30,-0.2,0.35),"Evt_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_Total","total mass",30,250.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",30,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopLep_W_Pt","ttZ reconstruction p_{T}(W_{lep})",30,0.0,500.0),"RecoTTZ_TopLep_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_DeepJetCSV_1","DeepJet b-tag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopHad_W_Pt","ttZ reconstruction p_{T}(W_{had})",30,0.0,500.0),"RecoTTZ_TopHad_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_HT_wo_MET","H_{T} without MET",30,200.0,1500.0),"Evt_HT_wo_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M3","M_{3} closest to 175 GeV",30,100.0,1000.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_BTagsM","number of b-tags (medium)",5,2.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_HT_jets","H_{T}(jets)",30,200.0,1500.0),"Evt_HT_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_MHT","missing H_{T}",30,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_MTW","MTW",30,0.0,200.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_JetsAverage","average M(jets)",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        ]

    return plots
def plots_4j_ge3t():
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_cosdTheta_Lep_bHad","ttZ reconstruction cos#Delta#theta(lep,b_{had})",30,-1.0,1.0),"RecoTTZ_cosdTheta_Lep_bHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_cosdTheta_Lep_topHad","ttZ reconstruction cos#Delta#theta(lep,t_{had})",30,-1.0,1.0),"RecoTTZ_cosdTheta_Lep_topHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Dphi_topLep_topHad","ttZ reconstruction #Delta#phi(t_{lep},t_{had})",30,0.0,6.28318530718),"RecoTTZ_Dphi_topLep_topHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_h1","second fox wolfram moment",30,-0.2,0.35),"Evt_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_cosdTheta_bLep_wLep","ttZ reconstruction cos#Delta#theta(b_{lep},W_{lep})",30,-1.0,1.0),"RecoTTZ_cosdTheta_bLep_wLep",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_N_BTagsT","number of b-tags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Deta_Lep_bHad","ttZ reconstruction #Delta#eta(lep,b_{had})",30,0.0,4.0),"RecoTTZ_Deta_Lep_bHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Deta_Lep_topHad","ttZ reconstruction #Delta#eta(lep,t_{had})",30,0.0,5.0),"RecoTTZ_Deta_Lep_topHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Deta_bLep_wLep","ttZ reconstruction #Delta#eta(b_{lep},W_{lep})",30,0.0,3.0),"RecoTTZ_Deta_bLep_wLep",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_JetsAverage","average M(jets)",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M3","M_{3} closest to 175 GeV",30,100.0,1000.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_min","minimal b-tag value",30,0.0,1.0),"Evt_CSV_min",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_cosdTheta_bHad_wHad","ttZ reconstruction cos#Delta#theta(b_{had},W_{had})",30,-1.0,1.0),"RecoTTZ_cosdTheta_bHad_wHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopLep_W_Pt","ttZ reconstruction p_{T}(W_{lep})",30,0.0,500.0),"RecoTTZ_TopLep_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_DeepJetCSV_3","DeepJet b-tag value of fourth jet",30,0.0,1.0),"Jet_DeepJetCSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Chi2WHad","ttZ reconstruction #chi^{2}(W_{had})",30,0.0,300.0),"RecoTTZ_Chi2WHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_Chi2TopHad","ttZ reconstruction #chi^{2}(t_{had})",30,0.0,300.0),"RecoTTZ_Chi2TopHad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_minDrJets","#DeltaR( min #DeltaR(jet,jet) )",30,0.4,1.8),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopHad_Pt","ttZ reconstruction p_{T}(t_{had})",30,0.0,700.0),"RecoTTZ_TopHad_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_MTW","MTW",30,0.0,200.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_minDrJets","M_{2}( min #DeltaR(jet,jet) )",30,0.0,200.0),"Evt_M2_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_MHT","missing H_{T}",30,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        ]

    return plots
def plots_ge4j_3t():
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_1","second highest b-tag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_minDrLepJet","#DeltaR( min #DeltaR(lep,jet) )",30,0.4,3.0),"Evt_Dr_minDrLepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_minDrJets","#DeltaR( min #DeltaR(jet,jet) )",30,0.4,1.8),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopHad_Pt","ttZ reconstruction p_{T}(t_{had})",30,0.0,700.0),"RecoTTZ_TopHad_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_JetPt_over_JetE","p_{T}(jets)/E(jets)",30,0.3,1.0),"Evt_JetPt_over_JetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_Total","total mass",30,250.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_dev","average deviation of b-tag value",30,0.0,0.24),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_1","mass of subleading jet",30,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_minDrJets","M_{2}( min #DeltaR(jet,jet) )",30,0.0,200.0),"Evt_M2_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopLep_W_Pt","ttZ reconstruction p_{T}(W_{lep})",30,0.0,500.0),"RecoTTZ_TopLep_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_avg_tagged","average b-tag value of tagged jets",30,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_HT_wo_MET","H_{T} without MET",30,200.0,1500.0),"Evt_HT_wo_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_dev_tagged","average deviation of b-tag value of tagged jets",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_h1","second fox wolfram moment",30,-0.2,0.35),"Evt_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopHad_W_Pt","ttZ reconstruction p_{T}(W_{had})",30,0.0,500.0),"RecoTTZ_TopHad_W_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M3","M_{3} closest to 175 GeV",30,100.0,1000.0),"Evt_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_HT_jets","H_{T}(jets)",30,200.0,1500.0),"Evt_HT_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_DeepJetCSV_1","DeepJet b-tag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_minDrJets","p_{T}( min #DeltaR(jet,jet) )",30,0.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_min_tagged","minimal b-tag value of tagged jets",30,0.28,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_2","third highest b-tag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_3","fourth highest b-tag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_MHT","missing H_{T}",30,0.0,400.0),"Evt_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_closestTo125TaggedJets","M_{2}(tag,tag) closest to 125 GeV",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_minDrLepTag","#DeltaR( min #DeltaR(lep,tag) )",30,0.4,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_avg","average b-tag value",30,0.1,0.9),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopLep_M","ttZ reconstruction M(t_{lep})",30,100.0,500.0),"RecoTTZ_TopLep_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_minDrTaggedJets","#DeltaR( min #DeltaR(tag,tag) )",30,0.4,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_MTW","MTW",30,0.0,200.0),"Evt_MTW",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_closestTo91TaggedJets","M_{2}(tag,tag) closest to 91 GeV",30,0.0,300.0),"Evt_M2_closestTo91TaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_minDrLepTag","M_{2}( min #DeltaR(lep,tag) )",30,0.0,250.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_DeepJetCSV_0","DeepJet b-tag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_JetsAverage","average M(jets)",30,5.0,30.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_RecoTTZ_TopHad_M","ttZ reconstruction M(t_{had})",30,100.0,500.0),"RecoTTZ_TopHad_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_minDrTaggedJets","M_{2}( min #DeltaR(tag,tag) )",30,0.0,400.0),"Evt_M2_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_minDrTaggedJets","p_{T}( min #DeltaR(tag,tag) )",30,0.0,500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots

def plots_dnn(data, discrname):

    ndefaultbins = 100
    category_dict = {}
    this_dict = {}




    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.87

    this_dict["ljets_ge4j_ge4t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.76

    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.86

    this_dict["ljets_ge4j_ge4t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.74

    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.77

    this_dict["ljets_ge4j_ge4t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.93

    this_dict["ljets_ge6j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.75

    this_dict["ljets_ge6j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.84

    this_dict["ljets_ge6j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.5

    this_dict["ljets_ge6j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.69

    this_dict["ljets_ge6j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==0))","ljets_le5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.99

    this_dict["ljets_le5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==1))","ljets_le5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.79

    this_dict["ljets_le5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==2))","ljets_le5j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.79

    this_dict["ljets_le5j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==3))","ljets_le5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.5

    this_dict["ljets_le5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_le5j_ge3t==4))","ljets_le5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.73

    this_dict["ljets_le5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 5j_ge3t

    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==0))","ljets_5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.99

    this_dict["ljets_5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.74

    this_dict["ljets_5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.79

    this_dict["ljets_5j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.53

    this_dict["ljets_5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.62

    this_dict["ljets_5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==0))","ljets_ge4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.98

    this_dict["ljets_ge4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==1))","ljets_ge4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.85

    this_dict["ljets_ge4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==2))","ljets_ge4j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.85

    this_dict["ljets_ge4j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==3))","ljets_ge4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.5

    this_dict["ljets_ge4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_ge3t==4))","ljets_ge4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.79

    this_dict["ljets_ge4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 4j_ge3t

    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==0))","ljets_4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.97

    this_dict["ljets_4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.77

    this_dict["ljets_4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.86

    this_dict["ljets_4j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.52

    this_dict["ljets_4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&((Evt_Odd==0))&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.73

    this_dict["ljets_4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.97

    this_dict["ljets_ge4j_3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.78

    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.8

    this_dict["ljets_ge4j_3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.46

    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&((Evt_Odd==0))&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.81

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
    discriminatorPlots += plots_ge4j_ge4t()
    discriminatorPlots += plots_ge6j_ge3t()
    discriminatorPlots += plots_le5j_ge3t()
    discriminatorPlots += plots_5j_ge3t()
    discriminatorPlots += plots_ge4j_ge3t()
    discriminatorPlots += plots_4j_ge3t()
    discriminatorPlots += plots_ge4j_3t()
    discriminatorPlots += plots_dnn(data, discrname)

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
    