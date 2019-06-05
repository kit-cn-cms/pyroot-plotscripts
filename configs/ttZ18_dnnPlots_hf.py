
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
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Phi_0","#phi of leading jet",30,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_E_3","energy of fourth jet",30,20.0,500.0),"Jet_E[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_LooseLepton_Eta_0","#eta(lep)",30,-2.4,2.4),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Phi_2","#phi of third jet",30,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Eta_2","#eta of third jet",30,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Eta_0","#eta of leading jet",30,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_pt_all_jets_over_E_all_jets_tags","p_{T}(tags)/E(tags)",30,0.2,1.0),"MVA_pt_all_jets_over_E_all_jets_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_blr","btag likelihood ratio",30,0.0,1.0),"MVA_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsL","number of btags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        ]

    return plots
def plots_ge6j_ge3t():
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_4","p_{T} of fifth jet",30,30.0,150.0),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_h2","third fox wolfram moment",30,-0.15,0.3),"MVA_h2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_pt_all_jets_over_E_all_jets_tags","p_{T}(tags)/E(tags)",30,0.2,1.0),"MVA_pt_all_jets_over_E_all_jets_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_4","fifth highest btag value",30,0.0,1.0),"CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_5","p_{T} of sixth jet",30,30.0,100.0),"Jet_Pt[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        ]

    return plots
def plots_ge6j_ge4t():
    label = "\geq 6 jets, \geq 4 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_CSV_4","fifth highest btag value",30,0.0,1.0),"CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_HT","H_{T}",30,100.0,1500.0),"MVA_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_best_higgs_mass","best higgs mass",30,0.0,250.0),"MVA_best_higgs_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_blr","btag likelihood ratio",30,0.0,1.0),"MVA_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_CSV_0","highest btag value",30,0.3,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_avg_dr_tagged_jets","average #DeltaR of tagged jets",30,0.4,3.5),"MVA_avg_dr_tagged_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_h2","third fox wolfram moment",30,-0.15,0.3),"MVA_h2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge4t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        ]

    return plots
def plots_le5j_ge3t():
    label = "\leq 5 jets, \geq 3 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        ]

    return plots
def plots_5j_ge3t():
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_4","p_{T} of fifth jet",30,30.0,150.0),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        ]

    return plots
def plots_ge4j_ge3t():
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_JetsAverage","average M_{2}(jets)",30,50.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        ]

    return plots
def plots_ge6j_3t():
    label = "\geq 6 jets, 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_CSV_5","sixth highest btag value",30,0.0,1.0),"CSV[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_cos_theta_l_bhad","cos#theta(lep b_{had})",30,-1.0,1.0),"MVA_cos_theta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_CSV_4","fifth highest btag value",30,0.0,1.0),"CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Jet_Pt_5","p_{T} of sixth jet",30,30.0,100.0),"Jet_Pt[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_Mlb","Mlb",30,20.0,300.0),"MVA_Mlb",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots
def plots_4j_ge3t():
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_MinDeltaRJets","min #DeltaR(jet jet)",30,0.4,2.2),"Evt_Dr_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        ]

    return plots
def plots_ge4j_3t():
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_HT","H_{T}",30,100.0,1500.0),"MVA_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_JetsAverage","average M_{2}(jets)",30,50.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots

def plots_dnn(data, discrname):

    ndefaultbins = 40
    category_dict = {}
    this_dict = {}




    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1913,
				0.2087,
				0.2262,
				0.2436,
				0.261,
				0.2785,
				0.2959,
				0.3133,
				0.3308,
				0.3482,
				0.3656,
				0.3831,
				0.4005,
				0.4179,
				0.4354,
				0.4528,
				0.4703,
				0.4877,
				0.5051,
				0.5226,
				0.54,
				0.5574,
				0.5749,
				0.5923,
				0.6097,
				0.6272,
				0.6446,
				0.6621,
				0.6795,
				0.6969,
				0.7144,
				0.7318,
				0.7492,
				0.7667,
				0.7841,
				0.8015,
				0.819,
				0.8364,
				0.8538,
				0.8713,
				0.88
				]
    this_dict["ljets_ge4j_ge4t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1923,
				0.2077,
				0.2231,
				0.2385,
				0.2538,
				0.2692,
				0.2846,
				0.3,
				0.3154,
				0.3308,
				0.3462,
				0.3615,
				0.3769,
				0.3923,
				0.4077,
				0.4231,
				0.4385,
				0.4538,
				0.4692,
				0.4846,
				0.5,
				0.5154,
				0.5308,
				0.5462,
				0.5615,
				0.5769,
				0.5923,
				0.6077,
				0.6231,
				0.6385,
				0.6538,
				0.6692,
				0.6846,
				0.7,
				0.7154,
				0.7308,
				0.7462,
				0.7615,
				0.7769,
				0.7923,
				0.8
				]
    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1913,
				0.2087,
				0.2262,
				0.2436,
				0.261,
				0.2785,
				0.2959,
				0.3133,
				0.3308,
				0.3482,
				0.3656,
				0.3831,
				0.4005,
				0.4179,
				0.4354,
				0.4528,
				0.4703,
				0.4877,
				0.5051,
				0.5226,
				0.54,
				0.5574,
				0.5749,
				0.5923,
				0.6097,
				0.6272,
				0.6446,
				0.6621,
				0.6795,
				0.6969,
				0.7144,
				0.7318,
				0.7492,
				0.7667,
				0.7841,
				0.8015,
				0.819,
				0.8364,
				0.8538,
				0.8713,
				0.88
				]
    this_dict["ljets_ge4j_ge4t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1922,
				0.2078,
				0.2235,
				0.2391,
				0.2547,
				0.2704,
				0.286,
				0.3017,
				0.3173,
				0.3329,
				0.3486,
				0.3642,
				0.3799,
				0.3955,
				0.4112,
				0.4268,
				0.4424,
				0.4581,
				0.4737,
				0.4894,
				0.505,
				0.5206,
				0.5363,
				0.5519,
				0.5676,
				0.5832,
				0.5988,
				0.6145,
				0.6301,
				0.6458,
				0.6614,
				0.6771,
				0.6927,
				0.7083,
				0.724,
				0.7396,
				0.7553,
				0.7709,
				0.7865,
				0.8022,
				0.81
				]
    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1937,
				0.2063,
				0.2188,
				0.2314,
				0.244,
				0.2565,
				0.2691,
				0.2817,
				0.2942,
				0.3068,
				0.3194,
				0.3319,
				0.3445,
				0.3571,
				0.3696,
				0.3822,
				0.3947,
				0.4073,
				0.4199,
				0.4324,
				0.445,
				0.4576,
				0.4701,
				0.4827,
				0.4953,
				0.5078,
				0.5204,
				0.5329,
				0.5455,
				0.5581,
				0.5706,
				0.5832,
				0.5958,
				0.6083,
				0.6209,
				0.6335,
				0.646,
				0.6586,
				0.6712,
				0.6837,
				0.69
				]
    this_dict["ljets_ge4j_ge4t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1914,
				0.2086,
				0.2258,
				0.2429,
				0.2601,
				0.2773,
				0.2945,
				0.3117,
				0.3288,
				0.346,
				0.3632,
				0.3804,
				0.3976,
				0.4147,
				0.4319,
				0.4491,
				0.4663,
				0.4835,
				0.5006,
				0.5178,
				0.535,
				0.5522,
				0.5694,
				0.5865,
				0.6037,
				0.6209,
				0.6381,
				0.6553,
				0.6724,
				0.6896,
				0.7068,
				0.724,
				0.7412,
				0.7583,
				0.7755,
				0.7927,
				0.8099,
				0.8271,
				0.8442,
				0.8614,
				0.87
				]
    this_dict["ljets_ge6j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1924,
				0.2076,
				0.2227,
				0.2378,
				0.2529,
				0.2681,
				0.2832,
				0.2983,
				0.3135,
				0.3286,
				0.3437,
				0.3588,
				0.374,
				0.3891,
				0.4042,
				0.4194,
				0.4345,
				0.4496,
				0.4647,
				0.4799,
				0.495,
				0.5101,
				0.5253,
				0.5404,
				0.5555,
				0.5706,
				0.5858,
				0.6009,
				0.616,
				0.6312,
				0.6463,
				0.6614,
				0.6765,
				0.6917,
				0.7068,
				0.7219,
				0.7371,
				0.7522,
				0.7673,
				0.7824,
				0.79
				]
    this_dict["ljets_ge6j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1918,
				0.2082,
				0.2246,
				0.241,
				0.2574,
				0.2738,
				0.2903,
				0.3067,
				0.3231,
				0.3395,
				0.3559,
				0.3723,
				0.3887,
				0.4051,
				0.4215,
				0.4379,
				0.4544,
				0.4708,
				0.4872,
				0.5036,
				0.52,
				0.5364,
				0.5528,
				0.5692,
				0.5856,
				0.6021,
				0.6185,
				0.6349,
				0.6513,
				0.6677,
				0.6841,
				0.7005,
				0.7169,
				0.7333,
				0.7497,
				0.7662,
				0.7826,
				0.799,
				0.8154,
				0.8318,
				0.84
				]
    this_dict["ljets_ge6j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1967,
				0.2033,
				0.21,
				0.2167,
				0.2233,
				0.23,
				0.2367,
				0.2433,
				0.25,
				0.2567,
				0.2633,
				0.27,
				0.2767,
				0.2833,
				0.29,
				0.2967,
				0.3033,
				0.31,
				0.3167,
				0.3233,
				0.33,
				0.3367,
				0.3433,
				0.35,
				0.3567,
				0.3633,
				0.37,
				0.3767,
				0.3833,
				0.39,
				0.3967,
				0.4033,
				0.41,
				0.4167,
				0.4233,
				0.43,
				0.4367,
				0.4433,
				0.45,
				0.4567,
				0.46
				]
    this_dict["ljets_ge6j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1945,
				0.2055,
				0.2165,
				0.2276,
				0.2386,
				0.2496,
				0.2606,
				0.2717,
				0.2827,
				0.2937,
				0.3047,
				0.3158,
				0.3268,
				0.3378,
				0.3488,
				0.3599,
				0.3709,
				0.3819,
				0.3929,
				0.404,
				0.415,
				0.426,
				0.4371,
				0.4481,
				0.4591,
				0.4701,
				0.4812,
				0.4922,
				0.5032,
				0.5142,
				0.5253,
				0.5363,
				0.5473,
				0.5583,
				0.5694,
				0.5804,
				0.5914,
				0.6024,
				0.6135,
				0.6245,
				0.63
				]
    this_dict["ljets_ge6j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge4t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge6j_ge4t==0))","ljets_ge6j_ge4t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge4t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.3223,
				0.3377,
				0.3531,
				0.3685,
				0.3838,
				0.3992,
				0.4146,
				0.43,
				0.4454,
				0.4608,
				0.4762,
				0.4915,
				0.5069,
				0.5223,
				0.5377,
				0.5531,
				0.5685,
				0.5838,
				0.5992,
				0.6146,
				0.63,
				0.6454,
				0.6608,
				0.6762,
				0.6915,
				0.7069,
				0.7223,
				0.7377,
				0.7531,
				0.7685,
				0.7838,
				0.7992,
				0.8146,
				0.83,
				0.8454,
				0.8608,
				0.8762,
				0.8915,
				0.9069,
				0.9223,
				0.93
				]
    this_dict["ljets_ge6j_ge4t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge6j_ge4t==1))","ljets_ge6j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge4t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.3231,
				0.3369,
				0.3508,
				0.3646,
				0.3785,
				0.3923,
				0.4062,
				0.42,
				0.4338,
				0.4477,
				0.4615,
				0.4754,
				0.4892,
				0.5031,
				0.5169,
				0.5308,
				0.5446,
				0.5585,
				0.5723,
				0.5862,
				0.6,
				0.6138,
				0.6277,
				0.6415,
				0.6554,
				0.6692,
				0.6831,
				0.6969,
				0.7108,
				0.7246,
				0.7385,
				0.7523,
				0.7662,
				0.78,
				0.7938,
				0.8077,
				0.8215,
				0.8354,
				0.8492,
				0.8631,
				0.87
				]
    this_dict["ljets_ge6j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge6j_ge4t==2))","ljets_ge6j_ge4t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge4t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.3221,
				0.3379,
				0.3538,
				0.3697,
				0.3856,
				0.4015,
				0.4174,
				0.4333,
				0.4492,
				0.4651,
				0.481,
				0.4969,
				0.5128,
				0.5287,
				0.5446,
				0.5605,
				0.5764,
				0.5923,
				0.6082,
				0.6241,
				0.64,
				0.6559,
				0.6718,
				0.6877,
				0.7036,
				0.7195,
				0.7354,
				0.7513,
				0.7672,
				0.7831,
				0.799,
				0.8149,
				0.8308,
				0.8467,
				0.8626,
				0.8785,
				0.8944,
				0.9103,
				0.9262,
				0.9421,
				0.95
				]
    this_dict["ljets_ge6j_ge4t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==0))","ljets_le5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1905,
				0.2095,
				0.2285,
				0.2474,
				0.2664,
				0.2854,
				0.3044,
				0.3233,
				0.3423,
				0.3613,
				0.3803,
				0.3992,
				0.4182,
				0.4372,
				0.4562,
				0.4751,
				0.4941,
				0.5131,
				0.5321,
				0.551,
				0.57,
				0.589,
				0.6079,
				0.6269,
				0.6459,
				0.6649,
				0.6838,
				0.7028,
				0.7218,
				0.7408,
				0.7597,
				0.7787,
				0.7977,
				0.8167,
				0.8356,
				0.8546,
				0.8736,
				0.8926,
				0.9115,
				0.9305,
				0.94
				]
    this_dict["ljets_le5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==1))","ljets_le5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1921,
				0.2079,
				0.2238,
				0.2397,
				0.2556,
				0.2715,
				0.2874,
				0.3033,
				0.3192,
				0.3351,
				0.351,
				0.3669,
				0.3828,
				0.3987,
				0.4146,
				0.4305,
				0.4464,
				0.4623,
				0.4782,
				0.4941,
				0.51,
				0.5259,
				0.5418,
				0.5577,
				0.5736,
				0.5895,
				0.6054,
				0.6213,
				0.6372,
				0.6531,
				0.669,
				0.6849,
				0.7008,
				0.7167,
				0.7326,
				0.7485,
				0.7644,
				0.7803,
				0.7962,
				0.8121,
				0.82
				]
    this_dict["ljets_le5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==2))","ljets_le5j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1922,
				0.2078,
				0.2235,
				0.2391,
				0.2547,
				0.2704,
				0.286,
				0.3017,
				0.3173,
				0.3329,
				0.3486,
				0.3642,
				0.3799,
				0.3955,
				0.4112,
				0.4268,
				0.4424,
				0.4581,
				0.4737,
				0.4894,
				0.505,
				0.5206,
				0.5363,
				0.5519,
				0.5676,
				0.5832,
				0.5988,
				0.6145,
				0.6301,
				0.6458,
				0.6614,
				0.6771,
				0.6927,
				0.7083,
				0.724,
				0.7396,
				0.7553,
				0.7709,
				0.7865,
				0.8022,
				0.81
				]
    this_dict["ljets_le5j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==3))","ljets_le5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1962,
				0.2038,
				0.2115,
				0.2192,
				0.2269,
				0.2346,
				0.2423,
				0.25,
				0.2577,
				0.2654,
				0.2731,
				0.2808,
				0.2885,
				0.2962,
				0.3038,
				0.3115,
				0.3192,
				0.3269,
				0.3346,
				0.3423,
				0.35,
				0.3577,
				0.3654,
				0.3731,
				0.3808,
				0.3885,
				0.3962,
				0.4038,
				0.4115,
				0.4192,
				0.4269,
				0.4346,
				0.4423,
				0.45,
				0.4577,
				0.4654,
				0.4731,
				0.4808,
				0.4885,
				0.4962,
				0.5
				]
    this_dict["ljets_le5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==4))","ljets_le5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1941,
				0.2059,
				0.2177,
				0.2295,
				0.2413,
				0.2531,
				0.2649,
				0.2767,
				0.2885,
				0.3003,
				0.3121,
				0.3238,
				0.3356,
				0.3474,
				0.3592,
				0.371,
				0.3828,
				0.3946,
				0.4064,
				0.4182,
				0.43,
				0.4418,
				0.4536,
				0.4654,
				0.4772,
				0.489,
				0.5008,
				0.5126,
				0.5244,
				0.5362,
				0.5479,
				0.5597,
				0.5715,
				0.5833,
				0.5951,
				0.6069,
				0.6187,
				0.6305,
				0.6423,
				0.6541,
				0.66
				]
    this_dict["ljets_le5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 5j_ge3t

    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==0))","ljets_5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1906,
				0.2094,
				0.2281,
				0.2468,
				0.2655,
				0.2842,
				0.3029,
				0.3217,
				0.3404,
				0.3591,
				0.3778,
				0.3965,
				0.4153,
				0.434,
				0.4527,
				0.4714,
				0.4901,
				0.5088,
				0.5276,
				0.5463,
				0.565,
				0.5837,
				0.6024,
				0.6212,
				0.6399,
				0.6586,
				0.6773,
				0.696,
				0.7147,
				0.7335,
				0.7522,
				0.7709,
				0.7896,
				0.8083,
				0.8271,
				0.8458,
				0.8645,
				0.8832,
				0.9019,
				0.9206,
				0.93
				]
    this_dict["ljets_5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1915,
				0.2085,
				0.2254,
				0.2423,
				0.2592,
				0.2762,
				0.2931,
				0.31,
				0.3269,
				0.3438,
				0.3608,
				0.3777,
				0.3946,
				0.4115,
				0.4285,
				0.4454,
				0.4623,
				0.4792,
				0.4962,
				0.5131,
				0.53,
				0.5469,
				0.5638,
				0.5808,
				0.5977,
				0.6146,
				0.6315,
				0.6485,
				0.6654,
				0.6823,
				0.6992,
				0.7162,
				0.7331,
				0.75,
				0.7669,
				0.7838,
				0.8008,
				0.8177,
				0.8346,
				0.8515,
				0.86
				]
    this_dict["ljets_5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1923,
				0.2077,
				0.2231,
				0.2385,
				0.2538,
				0.2692,
				0.2846,
				0.3,
				0.3154,
				0.3308,
				0.3462,
				0.3615,
				0.3769,
				0.3923,
				0.4077,
				0.4231,
				0.4385,
				0.4538,
				0.4692,
				0.4846,
				0.5,
				0.5154,
				0.5308,
				0.5462,
				0.5615,
				0.5769,
				0.5923,
				0.6077,
				0.6231,
				0.6385,
				0.6538,
				0.6692,
				0.6846,
				0.7,
				0.7154,
				0.7308,
				0.7462,
				0.7615,
				0.7769,
				0.7923,
				0.8
				]
    this_dict["ljets_5j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.196,
				0.204,
				0.2119,
				0.2199,
				0.2278,
				0.2358,
				0.2437,
				0.2517,
				0.2596,
				0.2676,
				0.2755,
				0.2835,
				0.2914,
				0.2994,
				0.3073,
				0.3153,
				0.3232,
				0.3312,
				0.3391,
				0.3471,
				0.355,
				0.3629,
				0.3709,
				0.3788,
				0.3868,
				0.3947,
				0.4027,
				0.4106,
				0.4186,
				0.4265,
				0.4345,
				0.4424,
				0.4504,
				0.4583,
				0.4663,
				0.4742,
				0.4822,
				0.4901,
				0.4981,
				0.506,
				0.51
				]
    this_dict["ljets_5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1947,
				0.2053,
				0.2158,
				0.2263,
				0.2368,
				0.2473,
				0.2578,
				0.2683,
				0.2788,
				0.2894,
				0.2999,
				0.3104,
				0.3209,
				0.3314,
				0.3419,
				0.3524,
				0.3629,
				0.3735,
				0.384,
				0.3945,
				0.405,
				0.4155,
				0.426,
				0.4365,
				0.4471,
				0.4576,
				0.4681,
				0.4786,
				0.4891,
				0.4996,
				0.5101,
				0.5206,
				0.5312,
				0.5417,
				0.5522,
				0.5627,
				0.5732,
				0.5837,
				0.5942,
				0.6047,
				0.61
				]
    this_dict["ljets_5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==0))","ljets_ge4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1913,
				0.2087,
				0.2262,
				0.2436,
				0.261,
				0.2785,
				0.2959,
				0.3133,
				0.3308,
				0.3482,
				0.3656,
				0.3831,
				0.4005,
				0.4179,
				0.4354,
				0.4528,
				0.4703,
				0.4877,
				0.5051,
				0.5226,
				0.54,
				0.5574,
				0.5749,
				0.5923,
				0.6097,
				0.6272,
				0.6446,
				0.6621,
				0.6795,
				0.6969,
				0.7144,
				0.7318,
				0.7492,
				0.7667,
				0.7841,
				0.8015,
				0.819,
				0.8364,
				0.8538,
				0.8713,
				0.88
				]
    this_dict["ljets_ge4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==1))","ljets_ge4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1918,
				0.2082,
				0.2246,
				0.241,
				0.2574,
				0.2738,
				0.2903,
				0.3067,
				0.3231,
				0.3395,
				0.3559,
				0.3723,
				0.3887,
				0.4051,
				0.4215,
				0.4379,
				0.4544,
				0.4708,
				0.4872,
				0.5036,
				0.52,
				0.5364,
				0.5528,
				0.5692,
				0.5856,
				0.6021,
				0.6185,
				0.6349,
				0.6513,
				0.6677,
				0.6841,
				0.7005,
				0.7169,
				0.7333,
				0.7497,
				0.7662,
				0.7826,
				0.799,
				0.8154,
				0.8318,
				0.84
				]
    this_dict["ljets_ge4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==2))","ljets_ge4j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1926,
				0.2074,
				0.2223,
				0.2372,
				0.2521,
				0.2669,
				0.2818,
				0.2967,
				0.3115,
				0.3264,
				0.3413,
				0.3562,
				0.371,
				0.3859,
				0.4008,
				0.4156,
				0.4305,
				0.4454,
				0.4603,
				0.4751,
				0.49,
				0.5049,
				0.5197,
				0.5346,
				0.5495,
				0.5644,
				0.5792,
				0.5941,
				0.609,
				0.6238,
				0.6387,
				0.6536,
				0.6685,
				0.6833,
				0.6982,
				0.7131,
				0.7279,
				0.7428,
				0.7577,
				0.7726,
				0.78
				]
    this_dict["ljets_ge4j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==3))","ljets_ge4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1964,
				0.2036,
				0.2108,
				0.2179,
				0.2251,
				0.2323,
				0.2395,
				0.2467,
				0.2538,
				0.261,
				0.2682,
				0.2754,
				0.2826,
				0.2897,
				0.2969,
				0.3041,
				0.3113,
				0.3185,
				0.3256,
				0.3328,
				0.34,
				0.3472,
				0.3544,
				0.3615,
				0.3687,
				0.3759,
				0.3831,
				0.3903,
				0.3974,
				0.4046,
				0.4118,
				0.419,
				0.4262,
				0.4333,
				0.4405,
				0.4477,
				0.4549,
				0.4621,
				0.4692,
				0.4764,
				0.48
				]
    this_dict["ljets_ge4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==4))","ljets_ge4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1924,
				0.2076,
				0.2227,
				0.2378,
				0.2529,
				0.2681,
				0.2832,
				0.2983,
				0.3135,
				0.3286,
				0.3437,
				0.3588,
				0.374,
				0.3891,
				0.4042,
				0.4194,
				0.4345,
				0.4496,
				0.4647,
				0.4799,
				0.495,
				0.5101,
				0.5253,
				0.5404,
				0.5555,
				0.5706,
				0.5858,
				0.6009,
				0.616,
				0.6312,
				0.6463,
				0.6614,
				0.6765,
				0.6917,
				0.7068,
				0.7219,
				0.7371,
				0.7522,
				0.7673,
				0.7824,
				0.79
				]
    this_dict["ljets_ge4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge6j_3t==0))","ljets_ge6j_3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1908,
				0.2092,
				0.2277,
				0.2462,
				0.2646,
				0.2831,
				0.3015,
				0.32,
				0.3385,
				0.3569,
				0.3754,
				0.3938,
				0.4123,
				0.4308,
				0.4492,
				0.4677,
				0.4862,
				0.5046,
				0.5231,
				0.5415,
				0.56,
				0.5785,
				0.5969,
				0.6154,
				0.6338,
				0.6523,
				0.6708,
				0.6892,
				0.7077,
				0.7262,
				0.7446,
				0.7631,
				0.7815,
				0.8,
				0.8185,
				0.8369,
				0.8554,
				0.8738,
				0.8923,
				0.9108,
				0.92
				]
    this_dict["ljets_ge6j_3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge6j_3t==1))","ljets_ge6j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1917,
				0.2083,
				0.225,
				0.2417,
				0.2583,
				0.275,
				0.2917,
				0.3083,
				0.325,
				0.3417,
				0.3583,
				0.375,
				0.3917,
				0.4083,
				0.425,
				0.4417,
				0.4583,
				0.475,
				0.4917,
				0.5083,
				0.525,
				0.5417,
				0.5583,
				0.575,
				0.5917,
				0.6083,
				0.625,
				0.6417,
				0.6583,
				0.675,
				0.6917,
				0.7083,
				0.725,
				0.7417,
				0.7583,
				0.775,
				0.7917,
				0.8083,
				0.825,
				0.8417,
				0.85
				]
    this_dict["ljets_ge6j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge6j_3t==2))","ljets_ge6j_3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1914,
				0.2086,
				0.2258,
				0.2429,
				0.2601,
				0.2773,
				0.2945,
				0.3117,
				0.3288,
				0.346,
				0.3632,
				0.3804,
				0.3976,
				0.4147,
				0.4319,
				0.4491,
				0.4663,
				0.4835,
				0.5006,
				0.5178,
				0.535,
				0.5522,
				0.5694,
				0.5865,
				0.6037,
				0.6209,
				0.6381,
				0.6553,
				0.6724,
				0.6896,
				0.7068,
				0.724,
				0.7412,
				0.7583,
				0.7755,
				0.7927,
				0.8099,
				0.8271,
				0.8442,
				0.8614,
				0.87
				]
    this_dict["ljets_ge6j_3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge6j_3t==3))","ljets_ge6j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1956,
				0.2044,
				0.2131,
				0.2218,
				0.2305,
				0.2392,
				0.2479,
				0.2567,
				0.2654,
				0.2741,
				0.2828,
				0.2915,
				0.3003,
				0.309,
				0.3177,
				0.3264,
				0.3351,
				0.3438,
				0.3526,
				0.3613,
				0.37,
				0.3787,
				0.3874,
				0.3962,
				0.4049,
				0.4136,
				0.4223,
				0.431,
				0.4397,
				0.4485,
				0.4572,
				0.4659,
				0.4746,
				0.4833,
				0.4921,
				0.5008,
				0.5095,
				0.5182,
				0.5269,
				0.5356,
				0.54
				]
    this_dict["ljets_ge6j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge6j_3t==4))","ljets_ge6j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1941,
				0.2059,
				0.2177,
				0.2295,
				0.2413,
				0.2531,
				0.2649,
				0.2767,
				0.2885,
				0.3003,
				0.3121,
				0.3238,
				0.3356,
				0.3474,
				0.3592,
				0.371,
				0.3828,
				0.3946,
				0.4064,
				0.4182,
				0.43,
				0.4418,
				0.4536,
				0.4654,
				0.4772,
				0.489,
				0.5008,
				0.5126,
				0.5244,
				0.5362,
				0.5479,
				0.5597,
				0.5715,
				0.5833,
				0.5951,
				0.6069,
				0.6187,
				0.6305,
				0.6423,
				0.6541,
				0.66
				]
    this_dict["ljets_ge6j_3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 4j_ge3t

    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==0))","ljets_4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1903,
				0.2097,
				0.2292,
				0.2487,
				0.2682,
				0.2877,
				0.3072,
				0.3267,
				0.3462,
				0.3656,
				0.3851,
				0.4046,
				0.4241,
				0.4436,
				0.4631,
				0.4826,
				0.5021,
				0.5215,
				0.541,
				0.5605,
				0.58,
				0.5995,
				0.619,
				0.6385,
				0.6579,
				0.6774,
				0.6969,
				0.7164,
				0.7359,
				0.7554,
				0.7749,
				0.7944,
				0.8138,
				0.8333,
				0.8528,
				0.8723,
				0.8918,
				0.9113,
				0.9308,
				0.9503,
				0.96
				]
    this_dict["ljets_4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1922,
				0.2078,
				0.2235,
				0.2391,
				0.2547,
				0.2704,
				0.286,
				0.3017,
				0.3173,
				0.3329,
				0.3486,
				0.3642,
				0.3799,
				0.3955,
				0.4112,
				0.4268,
				0.4424,
				0.4581,
				0.4737,
				0.4894,
				0.505,
				0.5206,
				0.5363,
				0.5519,
				0.5676,
				0.5832,
				0.5988,
				0.6145,
				0.6301,
				0.6458,
				0.6614,
				0.6771,
				0.6927,
				0.7083,
				0.724,
				0.7396,
				0.7553,
				0.7709,
				0.7865,
				0.8022,
				0.81
				]
    this_dict["ljets_4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1918,
				0.2082,
				0.2246,
				0.241,
				0.2574,
				0.2738,
				0.2903,
				0.3067,
				0.3231,
				0.3395,
				0.3559,
				0.3723,
				0.3887,
				0.4051,
				0.4215,
				0.4379,
				0.4544,
				0.4708,
				0.4872,
				0.5036,
				0.52,
				0.5364,
				0.5528,
				0.5692,
				0.5856,
				0.6021,
				0.6185,
				0.6349,
				0.6513,
				0.6677,
				0.6841,
				0.7005,
				0.7169,
				0.7333,
				0.7497,
				0.7662,
				0.7826,
				0.799,
				0.8154,
				0.8318,
				0.84
				]
    this_dict["ljets_4j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1954,
				0.2046,
				0.2138,
				0.2231,
				0.2323,
				0.2415,
				0.2508,
				0.26,
				0.2692,
				0.2785,
				0.2877,
				0.2969,
				0.3062,
				0.3154,
				0.3246,
				0.3338,
				0.3431,
				0.3523,
				0.3615,
				0.3708,
				0.38,
				0.3892,
				0.3985,
				0.4077,
				0.4169,
				0.4262,
				0.4354,
				0.4446,
				0.4538,
				0.4631,
				0.4723,
				0.4815,
				0.4908,
				0.5,
				0.5092,
				0.5185,
				0.5277,
				0.5369,
				0.5462,
				0.5554,
				0.56
				]
    this_dict["ljets_4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1941,
				0.2059,
				0.2177,
				0.2295,
				0.2413,
				0.2531,
				0.2649,
				0.2767,
				0.2885,
				0.3003,
				0.3121,
				0.3238,
				0.3356,
				0.3474,
				0.3592,
				0.371,
				0.3828,
				0.3946,
				0.4064,
				0.4182,
				0.43,
				0.4418,
				0.4536,
				0.4654,
				0.4772,
				0.489,
				0.5008,
				0.5126,
				0.5244,
				0.5362,
				0.5479,
				0.5597,
				0.5715,
				0.5833,
				0.5951,
				0.6069,
				0.6187,
				0.6305,
				0.6423,
				0.6541,
				0.66
				]
    this_dict["ljets_4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.191,
				0.209,
				0.2269,
				0.2449,
				0.2628,
				0.2808,
				0.2987,
				0.3167,
				0.3346,
				0.3526,
				0.3705,
				0.3885,
				0.4064,
				0.4244,
				0.4423,
				0.4603,
				0.4782,
				0.4962,
				0.5141,
				0.5321,
				0.55,
				0.5679,
				0.5859,
				0.6038,
				0.6218,
				0.6397,
				0.6577,
				0.6756,
				0.6936,
				0.7115,
				0.7295,
				0.7474,
				0.7654,
				0.7833,
				0.8013,
				0.8192,
				0.8372,
				0.8551,
				0.8731,
				0.891,
				0.9
				]
    this_dict["ljets_ge4j_3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1933,
				0.2067,
				0.22,
				0.2333,
				0.2467,
				0.26,
				0.2733,
				0.2867,
				0.3,
				0.3133,
				0.3267,
				0.34,
				0.3533,
				0.3667,
				0.38,
				0.3933,
				0.4067,
				0.42,
				0.4333,
				0.4467,
				0.46,
				0.4733,
				0.4867,
				0.5,
				0.5133,
				0.5267,
				0.54,
				0.5533,
				0.5667,
				0.58,
				0.5933,
				0.6067,
				0.62,
				0.6333,
				0.6467,
				0.66,
				0.6733,
				0.6867,
				0.7,
				0.7133,
				0.72
				]
    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1923,
				0.2077,
				0.2231,
				0.2385,
				0.2538,
				0.2692,
				0.2846,
				0.3,
				0.3154,
				0.3308,
				0.3462,
				0.3615,
				0.3769,
				0.3923,
				0.4077,
				0.4231,
				0.4385,
				0.4538,
				0.4692,
				0.4846,
				0.5,
				0.5154,
				0.5308,
				0.5462,
				0.5615,
				0.5769,
				0.5923,
				0.6077,
				0.6231,
				0.6385,
				0.6538,
				0.6692,
				0.6846,
				0.7,
				0.7154,
				0.7308,
				0.7462,
				0.7615,
				0.7769,
				0.7923,
				0.8
				]
    this_dict["ljets_ge4j_3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1958,
				0.2042,
				0.2127,
				0.2212,
				0.2296,
				0.2381,
				0.2465,
				0.255,
				0.2635,
				0.2719,
				0.2804,
				0.2888,
				0.2973,
				0.3058,
				0.3142,
				0.3227,
				0.3312,
				0.3396,
				0.3481,
				0.3565,
				0.365,
				0.3735,
				0.3819,
				0.3904,
				0.3988,
				0.4073,
				0.4158,
				0.4242,
				0.4327,
				0.4412,
				0.4496,
				0.4581,
				0.4665,
				0.475,
				0.4835,
				0.4919,
				0.5004,
				0.5088,
				0.5173,
				0.5258,
				0.53
				]
    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1931,
				0.2069,
				0.2208,
				0.2346,
				0.2485,
				0.2623,
				0.2762,
				0.29,
				0.3038,
				0.3177,
				0.3315,
				0.3454,
				0.3592,
				0.3731,
				0.3869,
				0.4008,
				0.4146,
				0.4285,
				0.4423,
				0.4562,
				0.47,
				0.4838,
				0.4977,
				0.5115,
				0.5254,
				0.5392,
				0.5531,
				0.5669,
				0.5808,
				0.5946,
				0.6085,
				0.6223,
				0.6362,
				0.65,
				0.6638,
				0.6777,
				0.6915,
				0.7054,
				0.7192,
				0.7331,
				0.74
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
    #discriminatorPlots += plots_ge4j_ge4t()
    #discriminatorPlots += plots_ge6j_ge3t()
    #discriminatorPlots += plots_ge6j_ge4t()
    #discriminatorPlots += plots_le5j_ge3t()
    #discriminatorPlots += plots_5j_ge3t()
    #discriminatorPlots += plots_ge4j_ge3t()
    #discriminatorPlots += plots_ge6j_3t()
    #discriminatorPlots += plots_4j_ge3t()
    #discriminatorPlots += plots_ge4j_3t()
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
    