
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


def plots_ge6j_ge3t():
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRJets","min #DeltaR(jet jet)",30,0.4,2.2),"Evt_Dr_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRLeptonJet","min #DeltaR(lep jet)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Eta_JetsAverage","average #eta(jets)",30,-2.0,2.0),"Evt_Eta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Eta_TaggedJetsAverage","average #eta(tags)",30,-2.0,2.0),"Evt_Eta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_HT_Jets","H_{T} of jets",30,150.0,1700.0),"Evt_HT_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_JetPtOverJetE","p_{T}(jets)/E(jets)",30,0.2,1.0),"Evt_JetPtOverJetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Jet_MaxDeta_Jets","max #Delta#eta(jet jet)",30,0.0,4.5),"Evt_Jet_MaxDeta_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M2_JetsAverage","average M_{2}(jets)",30,50.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MinDeltaRLeptonJet","mass of min #DeltaR(lep jet)",30,20.0,250.0),"Evt_M_MinDeltaRLeptonJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_MET","p_{T}(MET)",30,20.0,400.0),"Evt_Pt_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_HT","H_{T}",30,100.0,1500.0),"MVA_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_MET","MET",30,0.0,300.0),"MVA_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Mlb","Mlb",30,20.0,300.0),"MVA_Mlb",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_all_sum_pt_with_met","p_{T} sum including MET",30,200.0,1500.0),"MVA_all_sum_pt_with_met",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_aplanarity","aplanarity",30,0.0,0.5),"MVA_aplanarity",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_aplanarity_jets","aplanarity of jets",30,0.0,0.3),"MVA_aplanarity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_aplanarity_tags","aplanarity of tagged jets",30,0.0,0.15),"MVA_aplanarity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_avg_btag_disc_btags","average btag value of tagged jets",30,0.2,1.0),"MVA_avg_btag_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_avg_dr_tagged_jets","average #DeltaR of tagged jets",30,0.4,3.5),"MVA_avg_dr_tagged_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_blr","btag likelihood ratio",30,0.0,1.0),"MVA_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_blr_transformed","transformed b-tag likelihood ratio",30,-7.0,14.0),"MVA_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_cos_theta_l_bhad","cos#theta(lep b_{had})",30,-1.0,1.0),"MVA_cos_theta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_delta_phi_blep_bhad","#Delta#phi(b_{lep} b_{had})",30,0.0,6.28318530718),"MVA_delta_phi_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_delta_phi_l_bhad","#Delta#phi(lep b_{had})",30,0.0,6.28318530718),"MVA_delta_phi_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_dr_between_lep_and_closest_jet","min #DeltaR(lep jet)",30,0.4,3.0),"MVA_dr_between_lep_and_closest_jet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_h0","first fox wolfram moment",30,0.2,0.45),"MVA_h0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_h2","third fox wolfram moment",30,-0.15,0.3),"MVA_h2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_h3","fourth fox wolfram moment",30,-0.15,0.25),"MVA_h3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_lowest_btag","lowest btag",30,0.3,1.0),"MVA_lowest_btag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_max_dR_bb","max #DeltaR(tag tag)",30,2.0,5.0),"MVA_max_dR_bb",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"MVA_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_maxeta_jet_jet","max #Delta#eta(jet jet)",30,0.0,1.6),"MVA_maxeta_jet_jet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_maxeta_jet_tag","max #Delta#eta(jet tag)",30,0.0,1.6),"MVA_maxeta_jet_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_maxeta_tag_tag","max #Delta#eta(tag tag)",30,0.0,1.6),"MVA_maxeta_tag_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_pt_all_jets_over_E_all_jets","p_{T}(jets)/E(jets)",30,0.2,1.0),"MVA_pt_all_jets_over_E_all_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_pt_all_jets_over_E_all_jets_tags","p_{T}(tags)/E(tags)",30,0.2,1.0),"MVA_pt_all_jets_over_E_all_jets_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_sphericity","sphericity",30,0.0,1.0),"MVA_sphericity",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_sphericity_jets","sphericity of jets",30,0.0,1.0),"MVA_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"MVA_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_transverse_sphericity","transverse sphericity",30,0.0,1.0),"MVA_transverse_sphericity",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"MVA_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_transverse_sphericity_tags","transverse sphericity of tagged jets",30,0.0,1.0),"MVA_transverse_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_BTagsL","number of btags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_PrimaryVertices","N(PrimaryVertices)",30,0.0,60.0),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_0","highest btag value",30,0.3,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_2","DeepJet btag value of third jet",30,0.0,1.0),"Jet_DeepJetCSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_3","DeepJet btag value of fourth jet",30,0.0,1.0),"Jet_DeepJetCSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_E_0","energy of leading jet",30,20.0,1000.0),"Jet_E[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_E_1","energy of subleading jet",30,20.0,1000.0),"Jet_E[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_E_2","energy of third jet",30,20.0,500.0),"Jet_E[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_E_3","energy of fourth jet",30,20.0,500.0),"Jet_E[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Eta_0","#eta of leading jet",30,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Eta_1","#eta of subleading jet",30,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Eta_2","#eta of third jet",30,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Eta_3","#eta of fourth jet",30,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_1","mass of subleading jet",30,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Phi_0","#phi of leading jet",30,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Phi_1","#phi of subleading jet",30,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Phi_2","#phi of third jet",30,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Phi_3","#phi of fourth jet",30,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_LooseLepton_E_0","E(lep)",30,0.0,600.0),"LooseLepton_E[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_LooseLepton_Eta_0","#eta(lep)",30,-2.4,2.4),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_LooseLepton_Phi_0","#phi(lep)",30,-3.14159265359,3.14159265359),"LooseLepton_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_4","fifth highest btag value",30,0.0,1.0),"CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_4","DeepJet btag value of fifth jet",30,0.0,1.0),"Jet_DeepJetCSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_E_4","energy of fifth jet",30,20.0,400.0),"Jet_E[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Eta_4","#eta of fifth jet",30,-2.4,2.4),"Jet_Eta[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_4","mass of fifth jet",30,0.0,20.0),"Jet_M[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Phi_4","#phi of fifth jet",30,-3.14159265359,3.14159265359),"Jet_Phi[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_4","p_{T} of fifth jet",30,30.0,150.0),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_dEta_fn","#Delta#eta(fn)",30,0.0,3.0),"MVA_dEta_fn",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_best_higgs_mass","best higgs mass",30,0.0,250.0),"MVA_best_higgs_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_5","sixth highest btag value",30,0.0,1.0),"CSV[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_5","DeepJet btag value of sixth jet",30,0.0,1.0),"Jet_DeepJetCSV[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_E_5","energy of sixth jet",30,20.0,500.0),"Jet_E[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Eta_5","#eta of sixth jet",30,-2.4,2.4),"Jet_Eta[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_5","mass of sixth jet",30,0.0,20.0),"Jet_M[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Phi_5","#phi of sixth jet",30,-3.14159265359,3.14159265359),"Jet_Phi[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_5","p_{T} of sixth jet",30,30.0,100.0),"Jet_Pt[5]",selection,label),
        ]

    return plots

def plots_le5j_ge3t():
    label = "\leq 5 jets, \geq 3 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRJets","min #DeltaR(jet jet)",30,0.4,2.2),"Evt_Dr_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRLeptonJet","min #DeltaR(lep jet)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Eta_JetsAverage","average #eta(jets)",30,-2.0,2.0),"Evt_Eta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Eta_TaggedJetsAverage","average #eta(tags)",30,-2.0,2.0),"Evt_Eta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_HT_Jets","H_{T} of jets",30,150.0,1700.0),"Evt_HT_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_JetPtOverJetE","p_{T}(jets)/E(jets)",30,0.2,1.0),"Evt_JetPtOverJetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Jet_MaxDeta_Jets","max #Delta#eta(jet jet)",30,0.0,4.5),"Evt_Jet_MaxDeta_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_JetsAverage","average M_{2}(jets)",30,50.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MinDeltaRLeptonJet","mass of min #DeltaR(lep jet)",30,20.0,250.0),"Evt_M_MinDeltaRLeptonJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_MET","p_{T}(MET)",30,20.0,400.0),"Evt_Pt_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_HT","H_{T}",30,100.0,1500.0),"MVA_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_MET","MET",30,0.0,300.0),"MVA_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Mlb","Mlb",30,20.0,300.0),"MVA_Mlb",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_all_sum_pt_with_met","p_{T} sum including MET",30,200.0,1500.0),"MVA_all_sum_pt_with_met",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_aplanarity","aplanarity",30,0.0,0.5),"MVA_aplanarity",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_aplanarity_jets","aplanarity of jets",30,0.0,0.3),"MVA_aplanarity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_aplanarity_tags","aplanarity of tagged jets",30,0.0,0.15),"MVA_aplanarity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_avg_btag_disc_btags","average btag value of tagged jets",30,0.2,1.0),"MVA_avg_btag_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_avg_dr_tagged_jets","average #DeltaR of tagged jets",30,0.4,3.5),"MVA_avg_dr_tagged_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_blr","btag likelihood ratio",30,0.0,1.0),"MVA_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_blr_transformed","transformed b-tag likelihood ratio",30,-7.0,14.0),"MVA_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_cos_theta_l_bhad","cos#theta(lep b_{had})",30,-1.0,1.0),"MVA_cos_theta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_delta_phi_blep_bhad","#Delta#phi(b_{lep} b_{had})",30,0.0,6.28318530718),"MVA_delta_phi_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_delta_phi_l_bhad","#Delta#phi(lep b_{had})",30,0.0,6.28318530718),"MVA_delta_phi_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_dr_between_lep_and_closest_jet","min #DeltaR(lep jet)",30,0.4,3.0),"MVA_dr_between_lep_and_closest_jet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_h0","first fox wolfram moment",30,0.2,0.45),"MVA_h0",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_h2","third fox wolfram moment",30,-0.15,0.3),"MVA_h2",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_h3","fourth fox wolfram moment",30,-0.15,0.25),"MVA_h3",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_lowest_btag","lowest btag",30,0.3,1.0),"MVA_lowest_btag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_max_dR_bb","max #DeltaR(tag tag)",30,2.0,5.0),"MVA_max_dR_bb",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"MVA_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_maxeta_jet_jet","max #Delta#eta(jet jet)",30,0.0,1.6),"MVA_maxeta_jet_jet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_maxeta_jet_tag","max #Delta#eta(jet tag)",30,0.0,1.6),"MVA_maxeta_jet_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_maxeta_tag_tag","max #Delta#eta(tag tag)",30,0.0,1.6),"MVA_maxeta_tag_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_pt_all_jets_over_E_all_jets","p_{T}(jets)/E(jets)",30,0.2,1.0),"MVA_pt_all_jets_over_E_all_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_pt_all_jets_over_E_all_jets_tags","p_{T}(tags)/E(tags)",30,0.2,1.0),"MVA_pt_all_jets_over_E_all_jets_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_sphericity","sphericity",30,0.0,1.0),"MVA_sphericity",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_sphericity_jets","sphericity of jets",30,0.0,1.0),"MVA_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"MVA_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_transverse_sphericity","transverse sphericity",30,0.0,1.0),"MVA_transverse_sphericity",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"MVA_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_transverse_sphericity_tags","transverse sphericity of tagged jets",30,0.0,1.0),"MVA_transverse_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_N_BTagsL","number of btags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_N_PrimaryVertices","N(PrimaryVertices)",30,0.0,60.0),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_0","highest btag value",30,0.3,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_2","DeepJet btag value of third jet",30,0.0,1.0),"Jet_DeepJetCSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_3","DeepJet btag value of fourth jet",30,0.0,1.0),"Jet_DeepJetCSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_E_0","energy of leading jet",30,20.0,1000.0),"Jet_E[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_E_1","energy of subleading jet",30,20.0,1000.0),"Jet_E[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_E_2","energy of third jet",30,20.0,500.0),"Jet_E[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_E_3","energy of fourth jet",30,20.0,500.0),"Jet_E[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Eta_0","#eta of leading jet",30,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Eta_1","#eta of subleading jet",30,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Eta_2","#eta of third jet",30,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Eta_3","#eta of fourth jet",30,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_1","mass of subleading jet",30,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_2","mass of third jet",30,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Phi_0","#phi of leading jet",30,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Phi_1","#phi of subleading jet",30,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Phi_2","#phi of third jet",30,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Phi_3","#phi of fourth jet",30,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_LooseLepton_E_0","E(lep)",30,0.0,600.0),"LooseLepton_E[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_LooseLepton_Eta_0","#eta(lep)",30,-2.4,2.4),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_LooseLepton_Phi_0","#phi(lep)",30,-3.14159265359,3.14159265359),"LooseLepton_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        ]

    return plots


def plots_dnn(data, discrname):

    ndefaultbins = 40
    category_dict = {}
    this_dict = {}




    # plots for ge6j_ge3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1624,
				0.1776,
				0.1927,
				0.2078,
				0.2229,
				0.2381,
				0.2532,
				0.2683,
				0.2835,
				0.2986,
				0.3137,
				0.3288,
				0.344,
				0.3591,
				0.3742,
				0.3894,
				0.4045,
				0.4196,
				0.4347,
				0.4499,
				0.465,
				0.4801,
				0.4953,
				0.5104,
				0.5255,
				0.5406,
				0.5558,
				0.5709,
				0.586,
				0.6012,
				0.6163,
				0.6314,
				0.6465,
				0.6617,
				0.6768,
				0.6919,
				0.7071,
				0.7222,
				0.7373,
				0.7524,
				0.76
				]
    this_dict["ljets_ge6j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttbb_node","")
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
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_tt2b"
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
    this_dict["ljets_ge6j_ge3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttb_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1649,
				0.1751,
				0.1854,
				0.1956,
				0.2059,
				0.2162,
				0.2264,
				0.2367,
				0.2469,
				0.2572,
				0.2674,
				0.2777,
				0.2879,
				0.2982,
				0.3085,
				0.3187,
				0.329,
				0.3392,
				0.3495,
				0.3597,
				0.37,
				0.3803,
				0.3905,
				0.4008,
				0.411,
				0.4213,
				0.4315,
				0.4418,
				0.4521,
				0.4623,
				0.4726,
				0.4828,
				0.4931,
				0.5033,
				0.5136,
				0.5238,
				0.5341,
				0.5444,
				0.5546,
				0.5649,
				0.57
				]
    this_dict["ljets_ge6j_ge3t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttcc_node","")
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
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==5))","ljets_ge6j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1653,
				0.1747,
				0.1842,
				0.1937,
				0.2032,
				0.2127,
				0.2222,
				0.2317,
				0.2412,
				0.2506,
				0.2601,
				0.2696,
				0.2791,
				0.2886,
				0.2981,
				0.3076,
				0.3171,
				0.3265,
				0.336,
				0.3455,
				0.355,
				0.3645,
				0.374,
				0.3835,
				0.3929,
				0.4024,
				0.4119,
				0.4214,
				0.4309,
				0.4404,
				0.4499,
				0.4594,
				0.4688,
				0.4783,
				0.4878,
				0.4973,
				0.5068,
				0.5163,
				0.5258,
				0.5353,
				0.54
				]
    this_dict["ljets_ge6j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==0))","ljets_le5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttH"
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
    this_dict["ljets_le5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==1))","ljets_le5j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttbb"
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
    this_dict["ljets_le5j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==2))","ljets_le5j_ge3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1636,
				0.1764,
				0.1892,
				0.2021,
				0.2149,
				0.2277,
				0.2405,
				0.2533,
				0.2662,
				0.279,
				0.2918,
				0.3046,
				0.3174,
				0.3303,
				0.3431,
				0.3559,
				0.3687,
				0.3815,
				0.3944,
				0.4072,
				0.42,
				0.4328,
				0.4456,
				0.4585,
				0.4713,
				0.4841,
				0.4969,
				0.5097,
				0.5226,
				0.5354,
				0.5482,
				0.561,
				0.5738,
				0.5867,
				0.5995,
				0.6123,
				0.6251,
				0.6379,
				0.6508,
				0.6636,
				0.67
				]
    this_dict["ljets_le5j_ge3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==3))","ljets_le5j_ge3t_ttb_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttb"
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
    this_dict["ljets_le5j_ge3t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==4))","ljets_le5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttcc"
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
    this_dict["ljets_le5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==5))","ljets_le5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttlf"
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
    this_dict["ljets_le5j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    

    for l in this_dict:
        this_dict[l]["histoname"] = discrname+"_"+l
        this_dict[l]["histotitle"] = "final discriminator ({})".format(l)
        this_dict[l]["plotPreselections"] = this_dict[l]["category"][0]

    DNNPlots = init_plots(dictionary = this_dict, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge6j_ge3t()
    discriminatorPlots += plots_le5j_ge3t()
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
    