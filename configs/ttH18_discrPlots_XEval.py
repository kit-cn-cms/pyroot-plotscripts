
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

    ndefaultbins = 15
    category_dict = {}
    this_dict = {}




    # plots for ge6j_ge3t

    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==0))","ljets_ge6j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1489,
				0.2754,
				0.3175,
				0.3596,
				0.4018,
				0.4439,
				0.4861,
				0.5282,
				0.76 
			]
    this_dict["ljets_ge6j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==1))","ljets_ge6j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttbb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1457,
				0.2914,
				0.34,
				0.3886,
				0.4371,
				0.4857,
				0.5343,
				0.5829,
				0.85 
			]
    this_dict["ljets_ge6j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==2))","ljets_ge6j_ge3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1479,
				0.2807,
				0.325,
				0.3693,
				0.4136,
				0.4579,
				0.5021,
				0.5464,
				0.79 
			]
    this_dict["ljets_ge6j_ge3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==3))","ljets_ge6j_ge3t_ttb_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1557,
				0.2414,
				0.27,
				0.2986,
				0.3271,
				0.3557,
				0.3843,
				0.4129,
				0.57 
			]
    this_dict["ljets_ge6j_ge3t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==4))","ljets_ge6j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1607,
				0.2164,
				0.235,
				0.2536,
				0.2721,
				0.2907,
				0.3093,
				0.3279,
				0.43 
			]
    this_dict["ljets_ge6j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=6&&N_BTagsM>=3)&&(DNNPredictedClass_ge6j_ge3t==5))","ljets_ge6j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge6j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1568,
				0.2361,
				0.2625,
				0.2889,
				0.3154,
				0.3418,
				0.3682,
				0.3946,
				0.54 
			]
    this_dict["ljets_ge6j_ge3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for le5j_ge3t

    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==0))","ljets_le5j_ge3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1493,
				0.2736,
				0.315,
				0.3564,
				0.3979,
				0.4393,
				0.4807,
				0.5221,
				0.75 
			]
    this_dict["ljets_le5j_ge3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==1))","ljets_le5j_ge3t_ttbb_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttbb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1439,
				0.3004,
				0.3525,
				0.4046,
				0.4568,
				0.5089,
				0.5611,
				0.6132,
				0.9 
			]
    this_dict["ljets_le5j_ge3t_ttbb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==2))","ljets_le5j_ge3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1521,
				0.2593,
				0.295,
				0.3307,
				0.3664,
				0.4021,
				0.4379,
				0.4736,
				0.67 
			]
    this_dict["ljets_le5j_ge3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==3))","ljets_le5j_ge3t_ttb_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1571,
				0.2343,
				0.26,
				0.2857,
				0.3114,
				0.3371,
				0.3629,
				0.3886,
				0.53 
			]
    this_dict["ljets_le5j_ge3t_ttb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==4))","ljets_le5j_ge3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1614,
				0.2129,
				0.23,
				0.2471,
				0.2643,
				0.2814,
				0.2986,
				0.3157,
				0.41 
			]
    this_dict["ljets_le5j_ge3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets<=5&&N_BTagsM>=3)&&(DNNPredictedClass_le5j_ge3t==5))","ljets_le5j_ge3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_le5j_ge3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1486,
				0.2771,
				0.32,
				0.3629,
				0.4057,
				0.4486,
				0.4914,
				0.5343,
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
    
