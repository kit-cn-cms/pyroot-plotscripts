
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
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsL","number of btags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRJets","min #DeltaR(jet jet)",30,0.4,2.2),"Evt_Dr_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_M_1","mass of subleading jet",30,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"MVA_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_blr","btag likelihood ratio",30,0.0,1.0),"MVA_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_h0","first fox wolfram moment",30,0.2,0.45),"MVA_h0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_avg_btag_disc_btags","average btag value of tagged jets",30,0.2,1.0),"MVA_avg_btag_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_blr_transformed","transformed b-tag likelihood ratio",30,-7.0,14.0),"MVA_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots
def plots_ge6j_ge3t():
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_dEta_fn","#Delta#eta(fn)",30,0.0,3.0),"MVA_dEta_fn",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_5","sixth highest btag value",30,0.0,1.0),"CSV[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_BTagsL","number of btags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_blr_transformed","transformed b-tag likelihood ratio",30,-7.0,14.0),"MVA_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots
def plots_le5j_ge3t():
    label = "\leq 5 jets, \geq 3 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_cos_theta_l_bhad","cos#theta(lep b_{had})",30,-1.0,1.0),"MVA_cos_theta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots
def plots_5j_ge3t():
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_N_BTagsL","number of btags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_cos_theta_l_bhad","cos#theta(lep b_{had})",30,-1.0,1.0),"MVA_cos_theta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Mlb","Mlb",30,20.0,300.0),"MVA_Mlb",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_4","p_{T} of fifth jet",30,30.0,150.0),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots
def plots_ge4j_ge3t():
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_BTagsL","number of btags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots
def plots_4j_ge3t():
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_MinDeltaRJets","min #DeltaR(jet jet)",30,0.4,2.2),"Evt_Dr_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_DeepJetCSV_3","DeepJet btag value of fourth jet",30,0.0,1.0),"Jet_DeepJetCSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Mlb","Mlb",30,20.0,300.0),"MVA_Mlb",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_E_0","energy of leading jet",30,20.0,1000.0),"Jet_E[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_cos_theta_l_bhad","cos#theta(lep b_{had})",30,-1.0,1.0),"MVA_cos_theta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots
def plots_ge4j_3t():
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_cos_theta_l_bhad","cos#theta(lep b_{had})",30,-1.0,1.0),"MVA_cos_theta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_N_BTagsL","number of btags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots

def plots_dnn(data, discrname):

    ndefaultbins = 40
    category_dict = {}
    this_dict = {}




    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1627,
				0.1773,
				0.1919,
				0.2065,
				0.2212,
				0.2358,
				0.2504,
				0.265,
				0.2796,
				0.2942,
				0.3088,
				0.3235,
				0.3381,
				0.3527,
				0.3673,
				0.3819,
				0.3965,
				0.4112,
				0.4258,
				0.4404,
				0.455,
				0.4696,
				0.4842,
				0.4988,
				0.5135,
				0.5281,
				0.5427,
				0.5573,
				0.5719,
				0.5865,
				0.6012,
				0.6158,
				0.6304,
				0.645,
				0.6596,
				0.6742,
				0.6888,
				0.7035,
				0.7181,
				0.7327,
				0.74
				]
    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttbb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1608,
				0.1792,
				0.1977,
				0.2162,
				0.2346,
				0.2531,
				0.2715,
				0.29,
				0.3085,
				0.3269,
				0.3454,
				0.3638,
				0.3823,
				0.4008,
				0.4192,
				0.4377,
				0.4562,
				0.4746,
				0.4931,
				0.5115,
				0.53,
				0.5485,
				0.5669,
				0.5854,
				0.6038,
				0.6223,
				0.6408,
				0.6592,
				0.6777,
				0.6962,
				0.7146,
				0.7331,
				0.7515,
				0.77,
				0.7885,
				0.8069,
				0.8254,
				0.8438,
				0.8623,
				0.8808,
				0.89
				]
    this_dict["ljets_ge4j_ge4t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1632,
				0.1768,
				0.1904,
				0.204,
				0.2176,
				0.2312,
				0.2447,
				0.2583,
				0.2719,
				0.2855,
				0.2991,
				0.3127,
				0.3263,
				0.3399,
				0.3535,
				0.3671,
				0.3806,
				0.3942,
				0.4078,
				0.4214,
				0.435,
				0.4486,
				0.4622,
				0.4758,
				0.4894,
				0.5029,
				0.5165,
				0.5301,
				0.5437,
				0.5573,
				0.5709,
				0.5845,
				0.5981,
				0.6117,
				0.6253,
				0.6388,
				0.6524,
				0.666,
				0.6796,
				0.6932,
				0.7
				]
    this_dict["ljets_ge4j_ge4t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1656,
				0.1744,
				0.1831,
				0.1918,
				0.2005,
				0.2092,
				0.2179,
				0.2267,
				0.2354,
				0.2441,
				0.2528,
				0.2615,
				0.2703,
				0.279,
				0.2877,
				0.2964,
				0.3051,
				0.3138,
				0.3226,
				0.3313,
				0.34,
				0.3487,
				0.3574,
				0.3662,
				0.3749,
				0.3836,
				0.3923,
				0.401,
				0.4097,
				0.4185,
				0.4272,
				0.4359,
				0.4446,
				0.4533,
				0.4621,
				0.4708,
				0.4795,
				0.4882,
				0.4969,
				0.5056,
				0.51
				]
    this_dict["ljets_ge4j_ge4t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1644,
				0.1756,
				0.1869,
				0.1982,
				0.2095,
				0.2208,
				0.2321,
				0.2433,
				0.2546,
				0.2659,
				0.2772,
				0.2885,
				0.2997,
				0.311,
				0.3223,
				0.3336,
				0.3449,
				0.3562,
				0.3674,
				0.3787,
				0.39,
				0.4013,
				0.4126,
				0.4238,
				0.4351,
				0.4464,
				0.4577,
				0.469,
				0.4803,
				0.4915,
				0.5028,
				0.5141,
				0.5254,
				0.5367,
				0.5479,
				0.5592,
				0.5705,
				0.5818,
				0.5931,
				0.6044,
				0.61
				]
    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==5))","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1631,
				0.1769,
				0.1908,
				0.2046,
				0.2185,
				0.2323,
				0.2462,
				0.26,
				0.2738,
				0.2877,
				0.3015,
				0.3154,
				0.3292,
				0.3431,
				0.3569,
				0.3708,
				0.3846,
				0.3985,
				0.4123,
				0.4262,
				0.44,
				0.4538,
				0.4677,
				0.4815,
				0.4954,
				0.5092,
				0.5231,
				0.5369,
				0.5508,
				0.5646,
				0.5785,
				0.5923,
				0.6062,
				0.62,
				0.6338,
				0.6477,
				0.6615,
				0.6754,
				0.6892,
				0.7031,
				0.71
				]
    this_dict["ljets_ge4j_ge4t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge6j_ge3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1626,
				0.1774,
				0.1923,
				0.2072,
				0.2221,
				0.2369,
				0.2518,
				0.2667,
				0.2815,
				0.2964,
				0.3113,
				0.3262,
				0.341,
				0.3559,
				0.3708,
				0.3856,
				0.4005,
				0.4154,
				0.4303,
				0.4451,
				0.46,
				0.4749,
				0.4897,
				0.5046,
				0.5195,
				0.5344,
				0.5492,
				0.5641,
				0.579,
				0.5938,
				0.6087,
				0.6236,
				0.6385,
				0.6533,
				0.6682,
				0.6831,
				0.6979,
				0.7128,
				0.7277,
				0.7426,
				0.75
				]
    this_dict["ljets_ge6j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttbb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1613,
				0.1787,
				0.1962,
				0.2136,
				0.231,
				0.2485,
				0.2659,
				0.2833,
				0.3008,
				0.3182,
				0.3356,
				0.3531,
				0.3705,
				0.3879,
				0.4054,
				0.4228,
				0.4403,
				0.4577,
				0.4751,
				0.4926,
				0.51,
				0.5274,
				0.5449,
				0.5623,
				0.5797,
				0.5972,
				0.6146,
				0.6321,
				0.6495,
				0.6669,
				0.6844,
				0.7018,
				0.7192,
				0.7367,
				0.7541,
				0.7715,
				0.789,
				0.8064,
				0.8238,
				0.8413,
				0.85
				]
    this_dict["ljets_ge6j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1627,
				0.1773,
				0.1919,
				0.2065,
				0.2212,
				0.2358,
				0.2504,
				0.265,
				0.2796,
				0.2942,
				0.3088,
				0.3235,
				0.3381,
				0.3527,
				0.3673,
				0.3819,
				0.3965,
				0.4112,
				0.4258,
				0.4404,
				0.455,
				0.4696,
				0.4842,
				0.4988,
				0.5135,
				0.5281,
				0.5427,
				0.5573,
				0.5719,
				0.5865,
				0.6012,
				0.6158,
				0.6304,
				0.645,
				0.6596,
				0.6742,
				0.6888,
				0.7035,
				0.7181,
				0.7327,
				0.74
				]
    this_dict["ljets_ge6j_ge3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttb_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1635,
				0.1765,
				0.1896,
				0.2027,
				0.2158,
				0.2288,
				0.2419,
				0.255,
				0.2681,
				0.2812,
				0.2942,
				0.3073,
				0.3204,
				0.3335,
				0.3465,
				0.3596,
				0.3727,
				0.3858,
				0.3988,
				0.4119,
				0.425,
				0.4381,
				0.4512,
				0.4642,
				0.4773,
				0.4904,
				0.5035,
				0.5165,
				0.5296,
				0.5427,
				0.5558,
				0.5688,
				0.5819,
				0.595,
				0.6081,
				0.6212,
				0.6342,
				0.6473,
				0.6604,
				0.6735,
				0.68
				]
    this_dict["ljets_ge6j_ge3t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1667,
				0.1733,
				0.18,
				0.1867,
				0.1933,
				0.2,
				0.2067,
				0.2133,
				0.22,
				0.2267,
				0.2333,
				0.24,
				0.2467,
				0.2533,
				0.26,
				0.2667,
				0.2733,
				0.28,
				0.2867,
				0.2933,
				0.3,
				0.3067,
				0.3133,
				0.32,
				0.3267,
				0.3333,
				0.34,
				0.3467,
				0.3533,
				0.36,
				0.3667,
				0.3733,
				0.38,
				0.3867,
				0.3933,
				0.4,
				0.4067,
				0.4133,
				0.42,
				0.4267,
				0.43
				]
    this_dict["ljets_ge6j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge6j_ge3t==5))","ljets_ge6j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1641,
				0.1759,
				0.1877,
				0.1995,
				0.2113,
				0.2231,
				0.2349,
				0.2467,
				0.2585,
				0.2703,
				0.2821,
				0.2938,
				0.3056,
				0.3174,
				0.3292,
				0.341,
				0.3528,
				0.3646,
				0.3764,
				0.3882,
				0.4,
				0.4118,
				0.4236,
				0.4354,
				0.4472,
				0.459,
				0.4708,
				0.4826,
				0.4944,
				0.5062,
				0.5179,
				0.5297,
				0.5415,
				0.5533,
				0.5651,
				0.5769,
				0.5887,
				0.6005,
				0.6123,
				0.6241,
				0.63
				]
    this_dict["ljets_ge6j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==0))","ljets_le5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1623,
				0.1777,
				0.1931,
				0.2085,
				0.2238,
				0.2392,
				0.2546,
				0.27,
				0.2854,
				0.3008,
				0.3162,
				0.3315,
				0.3469,
				0.3623,
				0.3777,
				0.3931,
				0.4085,
				0.4238,
				0.4392,
				0.4546,
				0.47,
				0.4854,
				0.5008,
				0.5162,
				0.5315,
				0.5469,
				0.5623,
				0.5777,
				0.5931,
				0.6085,
				0.6238,
				0.6392,
				0.6546,
				0.67,
				0.6854,
				0.7008,
				0.7162,
				0.7315,
				0.7469,
				0.7623,
				0.77
				]
    this_dict["ljets_le5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==1))","ljets_le5j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttbb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1603,
				0.1797,
				0.1992,
				0.2187,
				0.2382,
				0.2577,
				0.2772,
				0.2967,
				0.3162,
				0.3356,
				0.3551,
				0.3746,
				0.3941,
				0.4136,
				0.4331,
				0.4526,
				0.4721,
				0.4915,
				0.511,
				0.5305,
				0.55,
				0.5695,
				0.589,
				0.6085,
				0.6279,
				0.6474,
				0.6669,
				0.6864,
				0.7059,
				0.7254,
				0.7449,
				0.7644,
				0.7838,
				0.8033,
				0.8228,
				0.8423,
				0.8618,
				0.8813,
				0.9008,
				0.9203,
				0.93
				]
    this_dict["ljets_le5j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==2))","ljets_le5j_ge3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1614,
				0.1786,
				0.1958,
				0.2129,
				0.2301,
				0.2473,
				0.2645,
				0.2817,
				0.2988,
				0.316,
				0.3332,
				0.3504,
				0.3676,
				0.3847,
				0.4019,
				0.4191,
				0.4363,
				0.4535,
				0.4706,
				0.4878,
				0.505,
				0.5222,
				0.5394,
				0.5565,
				0.5737,
				0.5909,
				0.6081,
				0.6253,
				0.6424,
				0.6596,
				0.6768,
				0.694,
				0.7112,
				0.7283,
				0.7455,
				0.7627,
				0.7799,
				0.7971,
				0.8142,
				0.8314,
				0.84
				]
    this_dict["ljets_le5j_ge3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==3))","ljets_le5j_ge3t_ttb_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1651,
				0.1749,
				0.1846,
				0.1944,
				0.2041,
				0.2138,
				0.2236,
				0.2333,
				0.2431,
				0.2528,
				0.2626,
				0.2723,
				0.2821,
				0.2918,
				0.3015,
				0.3113,
				0.321,
				0.3308,
				0.3405,
				0.3503,
				0.36,
				0.3697,
				0.3795,
				0.3892,
				0.399,
				0.4087,
				0.4185,
				0.4282,
				0.4379,
				0.4477,
				0.4574,
				0.4672,
				0.4769,
				0.4867,
				0.4964,
				0.5062,
				0.5159,
				0.5256,
				0.5354,
				0.5451,
				0.55
				]
    this_dict["ljets_le5j_ge3t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==4))","ljets_le5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1665,
				0.1735,
				0.1804,
				0.1873,
				0.1942,
				0.2012,
				0.2081,
				0.215,
				0.2219,
				0.2288,
				0.2358,
				0.2427,
				0.2496,
				0.2565,
				0.2635,
				0.2704,
				0.2773,
				0.2842,
				0.2912,
				0.2981,
				0.305,
				0.3119,
				0.3188,
				0.3258,
				0.3327,
				0.3396,
				0.3465,
				0.3535,
				0.3604,
				0.3673,
				0.3742,
				0.3812,
				0.3881,
				0.395,
				0.4019,
				0.4088,
				0.4158,
				0.4227,
				0.4296,
				0.4365,
				0.44
				]
    this_dict["ljets_le5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_le5j_ge3t==5))","ljets_le5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1638,
				0.1762,
				0.1885,
				0.2008,
				0.2131,
				0.2254,
				0.2377,
				0.25,
				0.2623,
				0.2746,
				0.2869,
				0.2992,
				0.3115,
				0.3238,
				0.3362,
				0.3485,
				0.3608,
				0.3731,
				0.3854,
				0.3977,
				0.41,
				0.4223,
				0.4346,
				0.4469,
				0.4592,
				0.4715,
				0.4838,
				0.4962,
				0.5085,
				0.5208,
				0.5331,
				0.5454,
				0.5577,
				0.57,
				0.5823,
				0.5946,
				0.6069,
				0.6192,
				0.6315,
				0.6438,
				0.65
				]
    this_dict["ljets_le5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 5j_ge3t

    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==0))","ljets_5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1627,
				0.1773,
				0.1919,
				0.2065,
				0.2212,
				0.2358,
				0.2504,
				0.265,
				0.2796,
				0.2942,
				0.3088,
				0.3235,
				0.3381,
				0.3527,
				0.3673,
				0.3819,
				0.3965,
				0.4112,
				0.4258,
				0.4404,
				0.455,
				0.4696,
				0.4842,
				0.4988,
				0.5135,
				0.5281,
				0.5427,
				0.5573,
				0.5719,
				0.5865,
				0.6012,
				0.6158,
				0.6304,
				0.645,
				0.6596,
				0.6742,
				0.6888,
				0.7035,
				0.7181,
				0.7327,
				0.74
				]
    this_dict["ljets_5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==1))","ljets_5j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttbb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1606,
				0.1794,
				0.1981,
				0.2168,
				0.2355,
				0.2542,
				0.2729,
				0.2917,
				0.3104,
				0.3291,
				0.3478,
				0.3665,
				0.3853,
				0.404,
				0.4227,
				0.4414,
				0.4601,
				0.4788,
				0.4976,
				0.5163,
				0.535,
				0.5537,
				0.5724,
				0.5912,
				0.6099,
				0.6286,
				0.6473,
				0.666,
				0.6847,
				0.7035,
				0.7222,
				0.7409,
				0.7596,
				0.7783,
				0.7971,
				0.8158,
				0.8345,
				0.8532,
				0.8719,
				0.8906,
				0.9
				]
    this_dict["ljets_5j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==2))","ljets_5j_ge3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1615,
				0.1785,
				0.1954,
				0.2123,
				0.2292,
				0.2462,
				0.2631,
				0.28,
				0.2969,
				0.3138,
				0.3308,
				0.3477,
				0.3646,
				0.3815,
				0.3985,
				0.4154,
				0.4323,
				0.4492,
				0.4662,
				0.4831,
				0.5,
				0.5169,
				0.5338,
				0.5508,
				0.5677,
				0.5846,
				0.6015,
				0.6185,
				0.6354,
				0.6523,
				0.6692,
				0.6862,
				0.7031,
				0.72,
				0.7369,
				0.7538,
				0.7708,
				0.7877,
				0.8046,
				0.8215,
				0.83
				]
    this_dict["ljets_5j_ge3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==3))","ljets_5j_ge3t_ttb_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1642,
				0.1758,
				0.1873,
				0.1988,
				0.2104,
				0.2219,
				0.2335,
				0.245,
				0.2565,
				0.2681,
				0.2796,
				0.2912,
				0.3027,
				0.3142,
				0.3258,
				0.3373,
				0.3488,
				0.3604,
				0.3719,
				0.3835,
				0.395,
				0.4065,
				0.4181,
				0.4296,
				0.4412,
				0.4527,
				0.4642,
				0.4758,
				0.4873,
				0.4988,
				0.5104,
				0.5219,
				0.5335,
				0.545,
				0.5565,
				0.5681,
				0.5796,
				0.5912,
				0.6027,
				0.6142,
				0.62
				]
    this_dict["ljets_5j_ge3t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==4))","ljets_5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1671,
				0.1729,
				0.1788,
				0.1847,
				0.1906,
				0.1965,
				0.2024,
				0.2083,
				0.2142,
				0.2201,
				0.226,
				0.2319,
				0.2378,
				0.2437,
				0.2496,
				0.2555,
				0.2614,
				0.2673,
				0.2732,
				0.2791,
				0.285,
				0.2909,
				0.2968,
				0.3027,
				0.3086,
				0.3145,
				0.3204,
				0.3263,
				0.3322,
				0.3381,
				0.344,
				0.3499,
				0.3558,
				0.3617,
				0.3676,
				0.3735,
				0.3794,
				0.3853,
				0.3912,
				0.3971,
				0.4
				]
    this_dict["ljets_5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==5&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_5j_ge3t==5))","ljets_5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_5j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1644,
				0.1756,
				0.1869,
				0.1982,
				0.2095,
				0.2208,
				0.2321,
				0.2433,
				0.2546,
				0.2659,
				0.2772,
				0.2885,
				0.2997,
				0.311,
				0.3223,
				0.3336,
				0.3449,
				0.3562,
				0.3674,
				0.3787,
				0.39,
				0.4013,
				0.4126,
				0.4238,
				0.4351,
				0.4464,
				0.4577,
				0.469,
				0.4803,
				0.4915,
				0.5028,
				0.5141,
				0.5254,
				0.5367,
				0.5479,
				0.5592,
				0.5705,
				0.5818,
				0.5931,
				0.6044,
				0.61
				]
    this_dict["ljets_5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==0))","ljets_ge4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1626,
				0.1774,
				0.1923,
				0.2072,
				0.2221,
				0.2369,
				0.2518,
				0.2667,
				0.2815,
				0.2964,
				0.3113,
				0.3262,
				0.341,
				0.3559,
				0.3708,
				0.3856,
				0.4005,
				0.4154,
				0.4303,
				0.4451,
				0.46,
				0.4749,
				0.4897,
				0.5046,
				0.5195,
				0.5344,
				0.5492,
				0.5641,
				0.579,
				0.5938,
				0.6087,
				0.6236,
				0.6385,
				0.6533,
				0.6682,
				0.6831,
				0.6979,
				0.7128,
				0.7277,
				0.7426,
				0.75
				]
    this_dict["ljets_ge4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==1))","ljets_ge4j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttbb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1605,
				0.1795,
				0.1985,
				0.2174,
				0.2364,
				0.2554,
				0.2744,
				0.2933,
				0.3123,
				0.3313,
				0.3503,
				0.3692,
				0.3882,
				0.4072,
				0.4262,
				0.4451,
				0.4641,
				0.4831,
				0.5021,
				0.521,
				0.54,
				0.559,
				0.5779,
				0.5969,
				0.6159,
				0.6349,
				0.6538,
				0.6728,
				0.6918,
				0.7108,
				0.7297,
				0.7487,
				0.7677,
				0.7867,
				0.8056,
				0.8246,
				0.8436,
				0.8626,
				0.8815,
				0.9005,
				0.91
				]
    this_dict["ljets_ge4j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==2))","ljets_ge4j_ge3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1627,
				0.1773,
				0.1919,
				0.2065,
				0.2212,
				0.2358,
				0.2504,
				0.265,
				0.2796,
				0.2942,
				0.3088,
				0.3235,
				0.3381,
				0.3527,
				0.3673,
				0.3819,
				0.3965,
				0.4112,
				0.4258,
				0.4404,
				0.455,
				0.4696,
				0.4842,
				0.4988,
				0.5135,
				0.5281,
				0.5427,
				0.5573,
				0.5719,
				0.5865,
				0.6012,
				0.6158,
				0.6304,
				0.645,
				0.6596,
				0.6742,
				0.6888,
				0.7035,
				0.7181,
				0.7327,
				0.74
				]
    this_dict["ljets_ge4j_ge3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==3))","ljets_ge4j_ge3t_ttb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1646,
				0.1754,
				0.1862,
				0.1969,
				0.2077,
				0.2185,
				0.2292,
				0.24,
				0.2508,
				0.2615,
				0.2723,
				0.2831,
				0.2938,
				0.3046,
				0.3154,
				0.3262,
				0.3369,
				0.3477,
				0.3585,
				0.3692,
				0.38,
				0.3908,
				0.4015,
				0.4123,
				0.4231,
				0.4338,
				0.4446,
				0.4554,
				0.4662,
				0.4769,
				0.4877,
				0.4985,
				0.5092,
				0.52,
				0.5308,
				0.5415,
				0.5523,
				0.5631,
				0.5738,
				0.5846,
				0.59
				]
    this_dict["ljets_ge4j_ge3t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==4))","ljets_ge4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1669,
				0.1731,
				0.1792,
				0.1854,
				0.1915,
				0.1977,
				0.2038,
				0.21,
				0.2162,
				0.2223,
				0.2285,
				0.2346,
				0.2408,
				0.2469,
				0.2531,
				0.2592,
				0.2654,
				0.2715,
				0.2777,
				0.2838,
				0.29,
				0.2962,
				0.3023,
				0.3085,
				0.3146,
				0.3208,
				0.3269,
				0.3331,
				0.3392,
				0.3454,
				0.3515,
				0.3577,
				0.3638,
				0.37,
				0.3762,
				0.3823,
				0.3885,
				0.3946,
				0.4008,
				0.4069,
				0.41
				]
    this_dict["ljets_ge4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==5))","ljets_ge4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1626,
				0.1774,
				0.1923,
				0.2072,
				0.2221,
				0.2369,
				0.2518,
				0.2667,
				0.2815,
				0.2964,
				0.3113,
				0.3262,
				0.341,
				0.3559,
				0.3708,
				0.3856,
				0.4005,
				0.4154,
				0.4303,
				0.4451,
				0.46,
				0.4749,
				0.4897,
				0.5046,
				0.5195,
				0.5344,
				0.5492,
				0.5641,
				0.579,
				0.5938,
				0.6087,
				0.6236,
				0.6385,
				0.6533,
				0.6682,
				0.6831,
				0.6979,
				0.7128,
				0.7277,
				0.7426,
				0.75
				]
    this_dict["ljets_ge4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for 4j_ge3t

    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==0))","ljets_4j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1613,
				0.1787,
				0.1962,
				0.2136,
				0.231,
				0.2485,
				0.2659,
				0.2833,
				0.3008,
				0.3182,
				0.3356,
				0.3531,
				0.3705,
				0.3879,
				0.4054,
				0.4228,
				0.4403,
				0.4577,
				0.4751,
				0.4926,
				0.51,
				0.5274,
				0.5449,
				0.5623,
				0.5797,
				0.5972,
				0.6146,
				0.6321,
				0.6495,
				0.6669,
				0.6844,
				0.7018,
				0.7192,
				0.7367,
				0.7541,
				0.7715,
				0.789,
				0.8064,
				0.8238,
				0.8413,
				0.85
				]
    this_dict["ljets_4j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==1))","ljets_4j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttbb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1604,
				0.1796,
				0.1988,
				0.2181,
				0.2373,
				0.2565,
				0.2758,
				0.295,
				0.3142,
				0.3335,
				0.3527,
				0.3719,
				0.3912,
				0.4104,
				0.4296,
				0.4488,
				0.4681,
				0.4873,
				0.5065,
				0.5258,
				0.545,
				0.5642,
				0.5835,
				0.6027,
				0.6219,
				0.6412,
				0.6604,
				0.6796,
				0.6988,
				0.7181,
				0.7373,
				0.7565,
				0.7758,
				0.795,
				0.8142,
				0.8335,
				0.8527,
				0.8719,
				0.8912,
				0.9104,
				0.92
				]
    this_dict["ljets_4j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==2))","ljets_4j_ge3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1632,
				0.1768,
				0.1904,
				0.204,
				0.2176,
				0.2312,
				0.2447,
				0.2583,
				0.2719,
				0.2855,
				0.2991,
				0.3127,
				0.3263,
				0.3399,
				0.3535,
				0.3671,
				0.3806,
				0.3942,
				0.4078,
				0.4214,
				0.435,
				0.4486,
				0.4622,
				0.4758,
				0.4894,
				0.5029,
				0.5165,
				0.5301,
				0.5437,
				0.5573,
				0.5709,
				0.5845,
				0.5981,
				0.6117,
				0.6253,
				0.6388,
				0.6524,
				0.666,
				0.6796,
				0.6932,
				0.7
				]
    this_dict["ljets_4j_ge3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==3))","ljets_4j_ge3t_ttb_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1664,
				0.1736,
				0.1808,
				0.1879,
				0.1951,
				0.2023,
				0.2095,
				0.2167,
				0.2238,
				0.231,
				0.2382,
				0.2454,
				0.2526,
				0.2597,
				0.2669,
				0.2741,
				0.2813,
				0.2885,
				0.2956,
				0.3028,
				0.31,
				0.3172,
				0.3244,
				0.3315,
				0.3387,
				0.3459,
				0.3531,
				0.3603,
				0.3674,
				0.3746,
				0.3818,
				0.389,
				0.3962,
				0.4033,
				0.4105,
				0.4177,
				0.4249,
				0.4321,
				0.4392,
				0.4464,
				0.45
				]
    this_dict["ljets_4j_ge3t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==4))","ljets_4j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.166,
				0.174,
				0.1819,
				0.1899,
				0.1978,
				0.2058,
				0.2137,
				0.2217,
				0.2296,
				0.2376,
				0.2455,
				0.2535,
				0.2614,
				0.2694,
				0.2773,
				0.2853,
				0.2932,
				0.3012,
				0.3091,
				0.3171,
				0.325,
				0.3329,
				0.3409,
				0.3488,
				0.3568,
				0.3647,
				0.3727,
				0.3806,
				0.3886,
				0.3965,
				0.4045,
				0.4124,
				0.4204,
				0.4283,
				0.4363,
				0.4442,
				0.4522,
				0.4601,
				0.4681,
				0.476,
				0.48
				]
    this_dict["ljets_4j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets==4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_4j_ge3t==5))","ljets_4j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_4j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1633,
				0.1767,
				0.19,
				0.2033,
				0.2167,
				0.23,
				0.2433,
				0.2567,
				0.27,
				0.2833,
				0.2967,
				0.31,
				0.3233,
				0.3367,
				0.35,
				0.3633,
				0.3767,
				0.39,
				0.4033,
				0.4167,
				0.43,
				0.4433,
				0.4567,
				0.47,
				0.4833,
				0.4967,
				0.51,
				0.5233,
				0.5367,
				0.55,
				0.5633,
				0.5767,
				0.59,
				0.6033,
				0.6167,
				0.63,
				0.6433,
				0.6567,
				0.67,
				0.6833,
				0.69
				]
    this_dict["ljets_4j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1621,
				0.1779,
				0.1938,
				0.2097,
				0.2256,
				0.2415,
				0.2574,
				0.2733,
				0.2892,
				0.3051,
				0.321,
				0.3369,
				0.3528,
				0.3687,
				0.3846,
				0.4005,
				0.4164,
				0.4323,
				0.4482,
				0.4641,
				0.48,
				0.4959,
				0.5118,
				0.5277,
				0.5436,
				0.5595,
				0.5754,
				0.5913,
				0.6072,
				0.6231,
				0.639,
				0.6549,
				0.6708,
				0.6867,
				0.7026,
				0.7185,
				0.7344,
				0.7503,
				0.7662,
				0.7821,
				0.79
				]
    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttbb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1631,
				0.1769,
				0.1908,
				0.2046,
				0.2185,
				0.2323,
				0.2462,
				0.26,
				0.2738,
				0.2877,
				0.3015,
				0.3154,
				0.3292,
				0.3431,
				0.3569,
				0.3708,
				0.3846,
				0.3985,
				0.4123,
				0.4262,
				0.44,
				0.4538,
				0.4677,
				0.4815,
				0.4954,
				0.5092,
				0.5231,
				0.5369,
				0.5508,
				0.5646,
				0.5785,
				0.5923,
				0.6062,
				0.62,
				0.6338,
				0.6477,
				0.6615,
				0.6754,
				0.6892,
				0.7031,
				0.71
				]
    this_dict["ljets_ge4j_3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1619,
				0.1781,
				0.1942,
				0.2104,
				0.2265,
				0.2427,
				0.2588,
				0.275,
				0.2912,
				0.3073,
				0.3235,
				0.3396,
				0.3558,
				0.3719,
				0.3881,
				0.4042,
				0.4204,
				0.4365,
				0.4527,
				0.4688,
				0.485,
				0.5012,
				0.5173,
				0.5335,
				0.5496,
				0.5658,
				0.5819,
				0.5981,
				0.6142,
				0.6304,
				0.6465,
				0.6627,
				0.6788,
				0.695,
				0.7112,
				0.7273,
				0.7435,
				0.7596,
				0.7758,
				0.7919,
				0.8
				]
    this_dict["ljets_ge4j_3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1654,
				0.1746,
				0.1838,
				0.1931,
				0.2023,
				0.2115,
				0.2208,
				0.23,
				0.2392,
				0.2485,
				0.2577,
				0.2669,
				0.2762,
				0.2854,
				0.2946,
				0.3038,
				0.3131,
				0.3223,
				0.3315,
				0.3408,
				0.35,
				0.3592,
				0.3685,
				0.3777,
				0.3869,
				0.3962,
				0.4054,
				0.4146,
				0.4238,
				0.4331,
				0.4423,
				0.4515,
				0.4608,
				0.47,
				0.4792,
				0.4885,
				0.4977,
				0.5069,
				0.5162,
				0.5254,
				0.53
				]
    this_dict["ljets_ge4j_3t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1676,
				0.1724,
				0.1773,
				0.1822,
				0.1871,
				0.1919,
				0.1968,
				0.2017,
				0.2065,
				0.2114,
				0.2163,
				0.2212,
				0.226,
				0.2309,
				0.2358,
				0.2406,
				0.2455,
				0.2504,
				0.2553,
				0.2601,
				0.265,
				0.2699,
				0.2747,
				0.2796,
				0.2845,
				0.2894,
				0.2942,
				0.2991,
				0.304,
				0.3088,
				0.3137,
				0.3186,
				0.3235,
				0.3283,
				0.3332,
				0.3381,
				0.3429,
				0.3478,
				0.3527,
				0.3576,
				0.36
				]
    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==5))","ljets_ge4j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1627,
				0.1773,
				0.1919,
				0.2065,
				0.2212,
				0.2358,
				0.2504,
				0.265,
				0.2796,
				0.2942,
				0.3088,
				0.3235,
				0.3381,
				0.3527,
				0.3673,
				0.3819,
				0.3965,
				0.4112,
				0.4258,
				0.4404,
				0.455,
				0.4696,
				0.4842,
				0.4988,
				0.5135,
				0.5281,
				0.5427,
				0.5573,
				0.5719,
				0.5865,
				0.6012,
				0.6158,
				0.6304,
				0.645,
				0.6596,
				0.6742,
				0.6888,
				0.7035,
				0.7181,
				0.7327,
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
    