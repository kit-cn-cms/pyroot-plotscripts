
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

    ndefaultbins = 15
    category_dict = {}
    this_dict = {}




    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1913,
				0.3308,
				0.3831,
				0.4179,
				0.4528,
				0.4877,
				0.5226,
				0.5574,
				0.6097,
				0.6621,
				0.8972
				]
    this_dict["ljets_ge4j_ge4t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1923,
				0.3,
				0.3462,
				0.3923,
				0.4231,
				0.4538,
				0.4846,
				0.5154,
				0.5462,
				0.5769,
				0.6077,
				0.8152
				]
    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1913,
				0.3482,
				0.4005,
				0.4528,
				0.8972
				]
    this_dict["ljets_ge4j_ge4t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1922,
				0.3017,
				0.8254
				]
    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1937,
				0.2188,
				0.3194,
				0.3822,
				0.445,
				0.5078,
				0.7024
				]
    this_dict["ljets_ge4j_ge4t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1914,
				0.2945,
				0.346,
				0.3804,
				0.4147,
				0.4491,
				0.4835,
				0.5178,
				0.5694,
				0.6209,
				0.6724,
				0.887
				]
    this_dict["ljets_ge6j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1924,
				0.2832,
				0.3135,
				0.3437,
				0.374,
				0.4042,
				0.4345,
				0.4496,
				0.4799,
				0.5101,
				0.5404,
				0.5706,
				0.8049
				]
    this_dict["ljets_ge6j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1918,
				0.2082,
				0.2903,
				0.3395,
				0.3723,
				0.4051,
				0.4379,
				0.4708,
				0.52,
				0.8562
				]
    this_dict["ljets_ge6j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1967,
				0.2767,
				0.3033,
				0.33,
				0.4666
				]
    this_dict["ljets_ge6j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1945,
				0.2827,
				0.3158,
				0.3488,
				0.3709,
				0.404,
				0.4481,
				0.6409
				]
    this_dict["ljets_ge6j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge4t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge6j_ge4t==0))","ljets_ge6j_ge4t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge4t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.3223,
				0.43,
				0.4762,
				0.5223,
				0.5838,
				0.6454,
				0.7223,
				0.9452
				]
    this_dict["ljets_ge6j_ge4t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge6j_ge4t==1))","ljets_ge6j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge4t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.3231,
				0.4062,
				0.4477,
				0.4754,
				0.5169,
				0.5585,
				0.8837
				]
    this_dict["ljets_ge6j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge6j_ge4t==2))","ljets_ge6j_ge4t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge4t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.3221,
				0.3379,
				0.4333,
				0.5128,
				0.9657
				]
    this_dict["ljets_ge6j_ge4t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==0))","ljets_le5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1905,
				0.2664,
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
				0.57,
				0.6079,
				0.6459,
				0.6838,
				0.7218,
				0.7597,
				0.7977,
				0.9587
				]
    this_dict["ljets_le5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==1))","ljets_le5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1921,
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
				0.6054,
				0.6372,
				0.8357
				]
    this_dict["ljets_le5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==2))","ljets_le5j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1922,
				0.2704,
				0.3017,
				0.3173,
				0.3329,
				0.3486,
				0.3799,
				0.3955,
				0.4112,
				0.4424,
				0.4737,
				0.505,
				0.5519,
				0.8254
				]
    this_dict["ljets_le5j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==3))","ljets_le5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1962,
				0.2577,
				0.2731,
				0.2885,
				0.3115,
				0.3269,
				0.3423,
				0.3577,
				0.3808,
				0.5076
				]
    this_dict["ljets_le5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==4))","ljets_le5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1941,
				0.2649,
				0.2885,
				0.3121,
				0.3356,
				0.3592,
				0.3828,
				0.4064,
				0.43,
				0.4536,
				0.489,
				0.5244,
				0.6716
				]
    this_dict["ljets_le5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 5j_ge3t

    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==0))","ljets_5j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1906,
				0.2842,
				0.3217,
				0.3591,
				0.3965,
				0.434,
				0.4714,
				0.5088,
				0.5463,
				0.6024,
				0.6586,
				0.7335,
				0.9485
				]
    this_dict["ljets_5j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1915,
				0.2085,
				0.2762,
				0.31,
				0.3438,
				0.3777,
				0.4115,
				0.4454,
				0.4792,
				0.5131,
				0.5469,
				0.5808,
				0.6146,
				0.8767
				]
    this_dict["ljets_5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1923,
				0.2846,
				0.3308,
				0.3615,
				0.3923,
				0.4231,
				0.4538,
				0.5,
				0.5615,
				0.8152
				]
    this_dict["ljets_5j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.196,
				0.2676,
				0.2994,
				0.3312,
				0.5178
				]
    this_dict["ljets_5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1947,
				0.2158,
				0.2788,
				0.3104,
				0.3419,
				0.3735,
				0.405,
				0.4365,
				0.6204
				]
    this_dict["ljets_5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==0))","ljets_ge4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1913,
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
				0.6795,
				0.7144,
				0.7492,
				0.8972
				]
    this_dict["ljets_ge4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==1))","ljets_ge4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1918,
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
				0.7005,
				0.8562
				]
    this_dict["ljets_ge4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==2))","ljets_ge4j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1926,
				0.2669,
				0.2818,
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
				0.4751,
				0.5049,
				0.5346,
				0.5644,
				0.7947
				]
    this_dict["ljets_ge4j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==3))","ljets_ge4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1964,
				0.2538,
				0.2682,
				0.2826,
				0.2969,
				0.3113,
				0.3256,
				0.3328,
				0.3472,
				0.3615,
				0.3759,
				0.3903,
				0.4871
				]
    this_dict["ljets_ge4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==4))","ljets_ge4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1924,
				0.2681,
				0.2983,
				0.3135,
				0.3286,
				0.3437,
				0.3588,
				0.374,
				0.3891,
				0.4042,
				0.4194,
				0.4496,
				0.4799,
				0.5101,
				0.5404,
				0.5706,
				0.616,
				0.8049
				]
    this_dict["ljets_ge4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge6j_3t==0))","ljets_ge6j_3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge6j_3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1908,
				0.3015,
				0.3569,
				0.4308,
				0.5231,
				0.9382
				]
    this_dict["ljets_ge6j_3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge6j_3t==1))","ljets_ge6j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1917,
				0.2917,
				0.3417,
				0.3917,
				0.4417,
				0.4917,
				0.8665
				]
    this_dict["ljets_ge6j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge6j_3t==2))","ljets_ge6j_3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1914,
				0.2086,
				0.3117,
				0.3804,
				0.4491,
				0.887
				]
    this_dict["ljets_ge6j_3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge6j_3t==3))","ljets_ge6j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1956,
				0.2218,
				0.2741,
				0.309,
				0.5486
				]
    this_dict["ljets_ge6j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge6j_3t==4))","ljets_ge6j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1941,
				0.2177,
				0.2885,
				0.3238,
				0.3592,
				0.3946,
				0.6716
				]
    this_dict["ljets_ge6j_3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 4j_ge3t

    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==0))","ljets_4j_ge3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1903,
				0.2877,
				0.3267,
				0.3656,
				0.4046,
				0.4631,
				0.5021,
				0.5605,
				0.619,
				0.9792
				]
    this_dict["ljets_4j_ge3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1922,
				0.2704,
				0.3017,
				0.3329,
				0.3642,
				0.3955,
				0.4268,
				0.4581,
				0.4894,
				0.5206,
				0.5519,
				0.8254
				]
    this_dict["ljets_4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1918,
				0.2903,
				0.3231,
				0.3559,
				0.3887,
				0.4215,
				0.4872,
				0.8562
				]
    this_dict["ljets_4j_ge3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1954,
				0.2138,
				0.2785,
				0.3154,
				0.3615,
				0.5691
				]
    this_dict["ljets_4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1941,
				0.2767,
				0.3121,
				0.3474,
				0.3828,
				0.4182,
				0.6716
				]
    this_dict["ljets_4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttZ_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttZ"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.191,
				0.2808,
				0.3167,
				0.3346,
				0.3526,
				0.3705,
				0.3885,
				0.4064,
				0.4244,
				0.4423,
				0.4782,
				0.5141,
				0.55,
				0.5859,
				0.6218,
				0.6756,
				0.7295,
				0.9177
				]
    this_dict["ljets_ge4j_3t_ttZ_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1933,
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
				0.5133,
				0.54,
				0.7332
				]
    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1923,
				0.2692,
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
				0.4692,
				0.5,
				0.5308,
				0.5615,
				0.6077,
				0.8152
				]
    this_dict["ljets_ge4j_3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1958,
				0.255,
				0.2719,
				0.2888,
				0.3058,
				0.3227,
				0.3396,
				0.3565,
				0.3819,
				0.5384
				]
    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1931,
				0.2069,
				0.2623,
				0.29,
				0.3038,
				0.3177,
				0.3315,
				0.3454,
				0.3592,
				0.3731,
				0.4008,
				0.4285,
				0.4562,
				0.4838,
				0.5254,
				0.7537
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
    discriminatorPlots += plots_ge4j_ge4t()
    discriminatorPlots += plots_ge6j_ge3t()
    discriminatorPlots += plots_ge6j_ge4t()
    discriminatorPlots += plots_le5j_ge3t()
    discriminatorPlots += plots_5j_ge3t()
    discriminatorPlots += plots_ge4j_ge3t()
    discriminatorPlots += plots_ge6j_3t()
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
    