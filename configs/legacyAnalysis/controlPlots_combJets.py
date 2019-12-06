
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

yieldExpression = "(N_Jets==4 && N_BTagsM==3)*1"
yieldExpression+="+(N_Jets==4 && N_BTagsM>=4)*2"
yieldExpression+="+(N_Jets==5 && N_BTagsM==3)*3"
yieldExpression+="+(N_Jets==5 && N_BTagsM>=4)*4"
yieldExpression+="+(N_Jets>=6 && N_BTagsM==3)*5"
yieldExpression+="+(N_Jets>=6 && N_BTagsM>=4)*6"



def plots_control_mem(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_memDBp","MEM",30,0.0,1.0),memexp,selection,label)
    ]
    return plots

def plots_control(cat,selection,label):
    plots = [
        # plotClasses.Plot(ROOT.TH1D(cat+"_memDBp","MEM",30,0.0,1.0),memexp,selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_evtYield","yields",6,0.5,6.5),yieldExpression,selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_N_PV","N_PrimaryVertices",80,0,80),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Pt","p_{T}(electron)",50,0,400),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_E","E(electron)",50,0,450),"Electron_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Eta","#eta(electron)",50,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Phi","#phi(electron)",50,-3.3,3.3),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Pt","p_{T}(muon)",50,0,300),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_E","E(muon)",50,0,450),"Muon_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Eta","#eta(muon)",50,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Phi","#phi(muon)",50,-3.3,3.3),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Pt","p_{T}(lepton)",50,0,300),"LooseLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_E","E(lepton)",50,0,450),"LooseLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Eta","#eta(lepton)",50,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Phi","#phi(lepton)",50,-3.3,3.3),"LooseLepton_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Pt","p_{T}(tight lepton)",50,0,300),"TightLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_E","E(tight lepton)",50,0,450),"TightLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Eta","#eta(tight lepton)",50,-2.5,2.5),"TightLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Phi","#phi(tight lepton)",50,-3.3,3.3),"TightLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_N_BTagsM","N_BTagsM",8,2.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_N_Jets","N_Jets",9,3.5,12.5),"N_Jets",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_N_ForwardJets","N_ForwardJets",6,0.5,6.5),"N_ForwardJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_ForwardJet_Pt","ForwardJet_Pt",40,20,400),"ForwardJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_ForwardJet_Eta","ForwardJet_Eta",30,-5.5,5.5),"ForwardJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_ForwardJet_M","ForwardJet_M",30,0.0,50.0),"ForwardJet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_ForwardJet_Phi","ForwardJet_Phi",30,-3.3,3.3),"ForwardJet_Phi",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_CSV","CSV",30,0,1),"CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_DeepJetCSV","Jet_DeepJetCSV",30,0.0,1.0),"Jet_DeepJetCSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV","Jet_CSV",30,0.0,1.0),"Jet_CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_0","Jet CSV[0]",30,0.3,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_1","Jet CSV[1]",30,0.3,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_2","Jet CSV[2]",30,0.3,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_0","CSV[0]",30,0.3,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_1","CSV[1]",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_2","CSV[2]",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_3","CSV[3]",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_CSV_min_tagged","min b-tag value of tagged jets",30,0.3,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_CSV_avg","average b-tag value",30,0.1,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.5),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_TaggedJetsAverage","average #DeltaR Tags",30,0.3,4.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_E_TaggedJetsAverage","average E(tags)",50,0.0,700.0),"Evt_E_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Eta_TaggedJetsAverage","average #eta of tagged Jets",50,-2.5,2.5),"Evt_Eta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT","H_{T}",50,150.0,2000.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",40,0.0,600.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_MET","MET",30,10.0,300),"Evt_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_MET_Phi","MET Phi",30,-3.3,3.3),"Evt_MET_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_M_TaggedJetsAverage","average M(tags)",30,3.0,35.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Pt_TaggedJetsAverage","average p_{T}(tags)",30,20.0,300.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_TaggedJetPt_over_TaggedJetE","p_{T}(tags)/E(tags)",30,0.2,1.0),"Evt_TaggedJetPt_over_TaggedJetE",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_M2_closestTo125TaggedJets","M2_closestTo125TaggedJets",30,0.0,300.0),"Evt_M2_closestTo125TaggedJets",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Deta_maxDetaTagTag","Evt_Deta_maxDetaTagTag",30,0.0,2.0),"Evt_Deta_maxDetaTagTag",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_sphericity_jets","Evt_sphericity_jets",30,0.0,1.0),"Evt_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_sphericity_tags","Evt_sphericity_tags",30,0.0,1.0),"Evt_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_blr","Evt_blr",30,-0.05,1.0),"Evt_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_blr_transformed","Evt_blr_transformed",30,-6.0,16.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_0","Jet_Pt[0]",30,20,500),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_1","Jet_Pt[1]",30,20,500),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_2","Jet_Pt[2]",30,20,350),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_3","Jet_Pt[3]",30,20,250),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT_tags","Evt_HT_tags",50,50.0,1200.0),"Evt_HT_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_M_minDrLepTag","Evt_M_minDrLepTag",30,0.0,350.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",30,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_maxDrJets","Evt_Dr_maxDrJets",30,1.5,6.0),"Evt_Dr_maxDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_minDrLepTag","Evt_Dr_minDrLepTag",30,0.3,3.5),"Evt_Dr_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_minDrTaggedJets","Evt_Dr_minDrTaggedJets",30,0.3,3.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT_wo_MET","Evt_HT_wo_MET",50,100.0,1600.0),"Evt_HT_wo_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Pt_minDrJets","Evt_Pt_minDrJets",40,1.0,600.0),"Evt_Pt_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",40,0.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,1.0,4.0),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Dr_minDrJets","Evt_Dr_minDrJets",30,0.3,3.2),"Evt_Dr_minDrJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_Deta_maxDetaJetJet","Evt_Deta_maxDetaJetJet",30,0.0,1.8),"Evt_Deta_maxDetaJetJet",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_transverse_sphericity_jets","Evt_transverse_sphericity_jets", 30,0.0,1.0),"Evt_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_CSV_dev_tagged","Evt_CSV_dev_tagged",30,0.0,0.12),"Evt_CSV_dev_tagged",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_E","Jet_E",60,0,800),"Jet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta","Jet_Eta",30,-2.5,2.5),"Jet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_M","Jet_M",30,0.0,50.0),"Jet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi","Jet_Phi",30,-3.3,3.3),"Jet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt","Jet_Pt",40,20,400),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_LooseJet_E","LooseJet_E",100,0,1000),"LooseJet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_LooseJet_Eta","LooseJet_Eta",40,-4,4),"LooseJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_LooseJet_M","LooseJet_M",30,0,60),"LooseJet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_LooseJet_Phi","LooseJet_Phi",30,-3.3,3.3),"LooseJet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_LooseJet_Pt","LooseJet_Pt",40,20,400),"LooseJet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TaggedJet_E","TaggedJet_E",60,0,800),"TaggedJet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TaggedJet_Eta","TaggedJet_Eta",30,-2.5,2.5),"TaggedJet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TaggedJet_M","TaggedJet_M",30,0,50),"TaggedJet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TaggedJet_Phi","TaggedJet_Phi",30,-3.3,3.3),"TaggedJet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TaggedJet_Pt","TaggedJet_Pt",30,20,400),"TaggedJet_Pt",selection,label),
        ]
    return plots

def plots_ttHReco(cat,selection,label):
    plots_ttH=[
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whaddau_m1","Reco_ttH_whaddau_m1",50,0,50),"Reco_ttH_whaddau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whaddau_m2","Reco_ttH_whaddau_m2",50,0,50),"Reco_ttH_whaddau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_log_toplep_pt","Reco_JABDT_ttH_log_toplep_pt",50,0,10),"Reco_JABDT_ttH_log_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_hdau_eta2","Reco_ttH_hdau_eta2",50,-2.5,2.5),"Reco_ttH_hdau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whad_eta","Reco_ttH_whad_eta",50,-4.2,4.2),"Reco_ttH_whad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_Jet_CSV_hdau2","Reco_JABDT_ttH_Jet_CSV_hdau2",50,0,1),"Reco_JABDT_ttH_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_hdau_eta1","Reco_ttH_hdau_eta1",50,-2.5,2.5),"Reco_ttH_hdau_eta1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btophad_m","Reco_ttH_btophad_m",50,0,60),"Reco_ttH_btophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_tophad_pt","Reco_ttH_tophad_pt",50,0,800),"Reco_ttH_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btoplep_m","Reco_ttH_btoplep_m",50,0,60),"Reco_ttH_btoplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whaddau_phi2","Reco_ttH_whaddau_phi2",50,-3.1416,3.1416),"Reco_ttH_whaddau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btophad_eta","Reco_ttH_btophad_eta",50,-2.5,2.5),"Reco_ttH_btophad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whaddau_phi1","Reco_ttH_whaddau_phi1",50,-3.1416,3.1416),"Reco_ttH_whaddau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_h_pt","Reco_ttH_h_pt",50,0,800),"Reco_ttH_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_toplep_pt","Reco_ttH_toplep_pt",50,0,800),"Reco_ttH_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btoplep_w_dr","Reco_ttH_btoplep_w_dr",50,0,4),"Reco_ttH_btoplep_w_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_Jet_CSV_hdau1","Reco_JABDT_ttH_Jet_CSV_hdau1",50,0,1),"Reco_JABDT_ttH_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_hdau_pt1","Reco_ttH_hdau_pt1",50,0,400),"Reco_ttH_hdau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_Jet_CSV_whaddau2","Reco_JABDT_ttH_Jet_CSV_whaddau2",50,0,1),"Reco_JABDT_ttH_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_hdau_pt2","Reco_ttH_hdau_pt2",50,0,400),"Reco_ttH_hdau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_toplep_m","Reco_ttH_toplep_m",50,0,800),"Reco_ttH_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_hdau_idx1","Reco_ttH_hdau_idx1",10,0,10),"Reco_ttH_hdau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_toplep_eta","Reco_ttH_toplep_eta",50,-4.2,4.2),"Reco_ttH_toplep_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_hdau_idx2","Reco_ttH_hdau_idx2",10,0,10),"Reco_ttH_hdau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",50,0,1),"Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_Jet_CSV_btoplep","Reco_JABDT_ttH_Jet_CSV_btoplep",50,0,1),"Reco_JABDT_ttH_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whad_dr","Reco_ttH_whad_dr",50,0,4),"Reco_ttH_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whad_phi","Reco_ttH_whad_phi",50,-3.1416,3.1416),"Reco_ttH_whad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_h_m","Reco_ttH_h_m",50,0,250),"Reco_ttH_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btoplep_phi","Reco_ttH_btoplep_phi",50,-3.1416,3.1416),"Reco_ttH_btoplep_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_toplep_phi","Reco_ttH_toplep_phi",50,-3.1416,3.1416),"Reco_ttH_toplep_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_Jet_CSV_whaddau1","Reco_JABDT_ttH_Jet_CSV_whaddau1",50,0,1),"Reco_JABDT_ttH_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_log_tophad_m__M__whad_m","Reco_JABDT_ttH_log_tophad_m__M__whad_m",50,0,10),"Reco_JABDT_ttH_log_tophad_m__M__whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whaddau_eta1","Reco_ttH_whaddau_eta1",50,-4.2,4.2),"Reco_ttH_whaddau_eta1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_hdau_m2","Reco_ttH_hdau_m2",50,0,60),"Reco_ttH_hdau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_tophad_m","Reco_ttH_tophad_m",50,0,400),"Reco_ttH_tophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whaddau_eta2","Reco_ttH_whaddau_eta2",50,-4.2,4.2),"Reco_ttH_whaddau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btophad_idx","Reco_ttH_btophad_idx",10,0,10),"Reco_ttH_btophad_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whad_pt","Reco_ttH_whad_pt",50,0,800),"Reco_ttH_whad_pt",selection,label),
        # plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_toplep_w_dr","Reco_ttH_toplep_w_dr",50,0,4),"Reco_ttH_toplep_w_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_log_toplep_m","Reco_JABDT_ttH_log_toplep_m",50,0,10),"Reco_JABDT_ttH_log_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_hdau_phi1","Reco_ttH_hdau_phi1",50,-3.1416,3.1416),"Reco_ttH_hdau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_hdau_phi2","Reco_ttH_hdau_phi2",50,-3.1416,3.1416),"Reco_ttH_hdau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_h_eta","Reco_ttH_h_eta",50,-4.2,4.2),"Reco_ttH_h_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_tophad_eta","Reco_ttH_tophad_eta",50,-4.2,4.2),"Reco_ttH_tophad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whaddau_pt1","Reco_ttH_whaddau_pt1",50,0,400),"Reco_ttH_whaddau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btoplep_pt","Reco_ttH_btoplep_pt",50,0,400),"Reco_ttH_btoplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btophad_phi","Reco_ttH_btophad_phi",50,-3.1416,3.1416),"Reco_ttH_btophad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whaddau_pt2","Reco_ttH_whaddau_pt2",50,0,400),"Reco_ttH_whaddau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btoplep_eta","Reco_ttH_btoplep_eta",50,-2.5,2.5),"Reco_ttH_btoplep_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_h_dr","Reco_ttH_h_dr",50,0,4),"Reco_ttH_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_hdau_m1","Reco_ttH_hdau_m1",50,0,60),"Reco_ttH_hdau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_h_phi","Reco_ttH_h_phi",50,-3.1416,3.1416),"Reco_ttH_h_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whaddau_idx2","Reco_ttH_whaddau_idx2",10,0,10),"Reco_ttH_whaddau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_Jet_CSV_btophad","Reco_JABDT_ttH_Jet_CSV_btophad",50,0,1),"Reco_JABDT_ttH_Jet_CSV_btophad",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_tophad_dr","Reco_ttH_tophad_dr",50,0,4),"Reco_ttH_tophad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whaddau_idx1","Reco_ttH_whaddau_idx1",10,0,10),"Reco_ttH_whaddau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_log_h_pt","Reco_JABDT_ttH_log_h_pt",50,0,10),"Reco_JABDT_ttH_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btoplep_idx","Reco_ttH_btoplep_idx",10,0,10),"Reco_ttH_btoplep_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_btophad_pt","Reco_ttH_btophad_pt",50,0,400),"Reco_ttH_btophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_whad_m","Reco_ttH_whad_m",50,0,300),"Reco_ttH_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_log_h_m","Reco_JABDT_ttH_log_h_m",50,0,10),"Reco_JABDT_ttH_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_log_tophad_pt","Reco_JABDT_ttH_log_tophad_pt",50,0,10),"Reco_JABDT_ttH_log_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_tophad_phi","Reco_ttH_tophad_phi",50,-3.1416,3.1416),"Reco_ttH_tophad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttH_log_whad_m","Reco_JABDT_ttH_log_whad_m",50,0,10),"Reco_JABDT_ttH_log_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttH_bestJABDToutput","Reco_ttH_bestJABDToutput",50,-1,1),"Reco_ttH_bestJABDToutput",selection,label),
        ]
    return plots_ttH

def plots_ttbarReco(cat,selection,label):
    plots_ttbar=[
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_Jet_CSV_whaddau2","Reco_JABDT_ttbar_Jet_CSV_whaddau2",50,0,1),"Reco_JABDT_ttbar_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_btophad_pt","Reco_ttbar_btophad_pt",50,0,400),"Reco_ttbar_btophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_Jet_CSV_whaddau1","Reco_JABDT_ttbar_Jet_CSV_whaddau1",50,0,1),"Reco_JABDT_ttbar_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whaddau_idx1","Reco_ttbar_whaddau_idx1",10,0,10),"Reco_ttbar_whaddau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_costheta_toplep_tophad","Reco_JABDT_ttbar_costheta_toplep_tophad",50,-1.0,1.0),"Reco_JABDT_ttbar_costheta_toplep_tophad",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whaddau_idx2","Reco_ttbar_whaddau_idx2",10,0,10),"Reco_ttbar_whaddau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whaddau_phi1","Reco_ttbar_whaddau_phi1",50,-3.1416,3.1416),"Reco_ttbar_whaddau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_tophad_m","Reco_ttbar_tophad_m",50,40,400),"Reco_ttbar_tophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whaddau_phi2","Reco_ttbar_whaddau_phi2",50,-3.1416,3.1416),"Reco_ttbar_whaddau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_log_toplep_pt","Reco_JABDT_ttbar_log_toplep_pt",50,0,10),"Reco_JABDT_ttbar_log_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_btophad_eta","Reco_ttbar_btophad_eta",50,-2.5,2.5),"Reco_ttbar_btophad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_btoplep_eta","Reco_ttbar_btoplep_eta",50,-2.5,2.5),"Reco_ttbar_btoplep_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_btophad_phi","Reco_ttbar_btophad_phi",50,-3.1416,3.1416),"Reco_ttbar_btophad_phi",selection,label),
        # plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_tophad_dr","Reco_ttbar_tophad_dr",50,0,4),"Reco_ttbar_tophad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_btoplep_phi","Reco_ttbar_btoplep_phi",50,-3.1416,3.1416),"Reco_ttbar_btoplep_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_Jet_CSV_btoplep","Reco_JABDT_ttbar_Jet_CSV_btoplep",50,0,1),"Reco_JABDT_ttbar_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whad_m","Reco_ttbar_whad_m",50,0,300),"Reco_ttbar_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_Jet_CSV_btophad","Reco_JABDT_ttbar_Jet_CSV_btophad",50,0,1),"Reco_JABDT_ttbar_Jet_CSV_btophad",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whaddau_m2","Reco_ttbar_whaddau_m2",50,0,50),"Reco_ttbar_whaddau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whaddau_m1","Reco_ttbar_whaddau_m1",50,0,50),"Reco_ttbar_whaddau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_toplep_phi","Reco_ttbar_toplep_phi",50,-3.1416,3.1416),"Reco_ttbar_toplep_phi",selection,label),
        # plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_log_tophad_m__M__whad_m","Reco_JABDT_ttbar_log_tophad_m__M__whad_m",50,0,10),"Reco_JABDT_ttbar_log_tophad_m__M__whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_tophad_eta","Reco_ttbar_tophad_eta",50,-4.2,4.2),"Reco_ttbar_tophad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whad_dr","Reco_ttbar_whad_dr",50,0,4),"Reco_ttbar_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_tophad_pt","Reco_ttbar_tophad_pt",50,0,800),"Reco_ttbar_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_btoplep_idx","Reco_ttbar_btoplep_idx",10,0,10),"Reco_ttbar_btoplep_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_tophad_pt__P__toplep_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_ttbar_tophad_pt__P__toplep_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",50,0,1),"Reco_JABDT_ttbar_tophad_pt__P__toplep_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_toplep_pt","Reco_ttbar_toplep_pt",50,0,800),"Reco_ttbar_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whaddau_eta2","Reco_ttbar_whaddau_eta2",50,-4.2,4.2),"Reco_ttbar_whaddau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,0,800),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whaddau_eta1","Reco_ttbar_whaddau_eta1",50,-4.2,4.2),"Reco_ttbar_whaddau_eta1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_tophad_phi","Reco_ttbar_tophad_phi",50,-3.1416,3.1416),"Reco_ttbar_tophad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whad_pt","Reco_ttbar_whad_pt",50,0,800),"Reco_ttbar_whad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_btophad_idx","Reco_ttbar_btophad_idx",10,0,10),"Reco_ttbar_btophad_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_LeptonicW_Eta","Reco_LeptonicW_Eta",50,-4.2,4.2),"Reco_LeptonicW_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_btoplep_pt","Reco_ttbar_btoplep_pt",50,0,400),"Reco_ttbar_btoplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whad_eta","Reco_ttbar_whad_eta",50,-4.2,4.2),"Reco_ttbar_whad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whaddau_pt1","Reco_ttbar_whaddau_pt1",50,0,400),"Reco_ttbar_whaddau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whaddau_pt2","Reco_ttbar_whaddau_pt2",50,0,400),"Reco_ttbar_whaddau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_LeptonicW_M","Reco_LeptonicW_M",50,0,400),"Reco_LeptonicW_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_toplep_eta","Reco_ttbar_toplep_eta",50,-4.2,4.2),"Reco_ttbar_toplep_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_btophad_m","Reco_ttbar_btophad_m",50,0,60),"Reco_ttbar_btophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_whad_phi","Reco_ttbar_whad_phi",50,-3.1416,3.1416),"Reco_ttbar_whad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_log_tophad_pt","Reco_JABDT_ttbar_log_tophad_pt",50,0,10),"Reco_JABDT_ttbar_log_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_LeptonicW_Phi","Reco_LeptonicW_Phi",50,-3.1416,3.1416),"Reco_LeptonicW_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_btoplep_m","Reco_ttbar_btoplep_m",50,0,60),"Reco_ttbar_btoplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_LeptonicW_Pt","Reco_LeptonicW_Pt",50,0,400),"Reco_LeptonicW_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_log_toplep_m","Reco_JABDT_ttbar_log_toplep_m",50,0,10),"Reco_JABDT_ttbar_log_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_ttbar_log_whad_m","Reco_JABDT_ttbar_log_whad_m",50,0,10),"Reco_JABDT_ttbar_log_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_ttbar_bestJABDToutput","Reco_ttbar_bestJABDToutput",50,-1,1),"Reco_ttbar_bestJABDToutput",selection,label),
    ]
    return plots_ttbar

def plots_tHWReco(cat,selection,label):
    plots_tHW=[
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_bestJABDToutput","Reco_tHW_bestJABDToutput",20,-1,1),"Reco_tHW_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_abs_top_eta","Reco_JABDT_tHW_abs_top_eta",40,0.0,4.0),"Reco_JABDT_tHW_abs_top_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whad_phi","Reco_tHW_whad_phi",34,-3.14,3.14),"Reco_tHW_whad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_log_h_pt","Reco_JABDT_tHW_log_h_pt",37,0.0,7.4),"Reco_JABDT_tHW_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_abs_btop_eta","Reco_JABDT_tHW_abs_btop_eta",25,0.0,2.5),"Reco_JABDT_tHW_abs_btop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_log_h_m","Reco_JABDT_tHW_log_h_m",22,3.0,7.2),"Reco_JABDT_tHW_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_log_whad_pt","Reco_JABDT_tHW_log_whad_pt",36,0.0,7.2),"Reco_JABDT_tHW_log_whad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whaddau_idx2","Reco_tHW_whaddau_idx2",15,0,15),"Reco_tHW_whaddau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whaddau_idx1","Reco_tHW_whaddau_idx1",15,0,15),"Reco_tHW_whaddau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_wb_h_dr","Reco_tHW_wb_h_dr",45,0,4.5),"Reco_tHW_wb_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_btop_phi","Reco_tHW_btop_phi",34,-3.14,3.14),"Reco_tHW_btop_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_h_eta","Reco_tHW_h_eta",40,-4.0,4.0),"Reco_tHW_h_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_wtop_eta","Reco_tHW_wtop_eta",42,-4.2,4.2),"Reco_tHW_wtop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_wb_pt","Reco_tHW_wb_pt",55,0,550),"Reco_tHW_wb_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whaddau_eta1","Reco_tHW_whaddau_eta1",40,-4.0,4.0),"Reco_tHW_whaddau_eta1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whaddau_eta2","Reco_tHW_whaddau_eta2",40,-4.0,4.0),"Reco_tHW_whaddau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_top_h_dr","Reco_tHW_top_h_dr",50,0,5),"Reco_tHW_top_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whad_pt","Reco_tHW_whad_pt",45,0,450),"Reco_tHW_whad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_hdau_eta1","Reco_tHW_hdau_eta1",50,-2.5,2.5),"Reco_tHW_hdau_eta1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_btop_eta","Reco_tHW_btop_eta",50,-2.5,2.5),"Reco_tHW_btop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_btop_m","Reco_tHW_btop_m",45,0,90),"Reco_tHW_btop_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_hdau_eta2","Reco_tHW_hdau_eta2",50,-2.5,2.5),"Reco_tHW_hdau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_h_pt","Reco_tHW_h_pt",75,0,750),"Reco_tHW_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_log_whad_m","Reco_JABDT_tHW_log_whad_m",25,3.0,8),"Reco_JABDT_tHW_log_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_abs_top_eta__M__wb_eta","Reco_JABDT_tHW_abs_top_eta__M__wb_eta",55,0.0,5.5),"Reco_JABDT_tHW_abs_top_eta__M__wb_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_wtop_pt","Reco_tHW_wtop_pt",45,0,450),"Reco_tHW_wtop_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_Jet_CSV_hdau2","Reco_JABDT_tHW_Jet_CSV_hdau2",50,0,1),"Reco_JABDT_tHW_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_hdau_pt1","Reco_tHW_hdau_pt1",35,0,350),"Reco_tHW_hdau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_hdau_pt2","Reco_tHW_hdau_pt2",35,0,350),"Reco_tHW_hdau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_abs_top_eta__M__higg_eta","Reco_JABDT_tHW_abs_top_eta__M__higg_eta",55,0.0,5.5),"Reco_JABDT_tHW_abs_top_eta__M__higg_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_btop_idx","Reco_tHW_btop_idx",15,0,15),"Reco_tHW_btop_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_hdau_m2","Reco_tHW_hdau_m2",45,0,90),"Reco_tHW_hdau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_h_phi","Reco_tHW_h_phi",34,-3.14,3.14),"Reco_tHW_h_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_wb_m","Reco_tHW_wb_m",35,0,350),"Reco_tHW_wb_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",50,0,1),"Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_wtop_m","Reco_tHW_wtop_m",40,0,400),"Reco_tHW_wtop_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_wtop_h_dr","Reco_tHW_wtop_h_dr",50,0,5.0),"Reco_tHW_wtop_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_log_top_m","Reco_JABDT_tHW_log_top_m",35,4.0,7.5),"Reco_JABDT_tHW_log_top_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_abs_wlep_eta__M__whad_eta","Reco_JABDT_tHW_abs_wlep_eta__M__whad_eta",55,0.0,5.5),"Reco_JABDT_tHW_abs_wlep_eta__M__whad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_log_top_pt","Reco_JABDT_tHW_log_top_pt",31,1.0,7.2),"Reco_JABDT_tHW_log_top_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whaddau_m1","Reco_tHW_whaddau_m1",60,0,60),"Reco_tHW_whaddau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_top_pt","Reco_tHW_top_pt",70,0,700),"Reco_tHW_top_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_Jet_CSV_hdau1","Reco_JABDT_tHW_Jet_CSV_hdau1",50,0,1),"Reco_JABDT_tHW_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whaddau_m2","Reco_tHW_whaddau_m2",40,0,40),"Reco_tHW_whaddau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_wb_phi","Reco_tHW_wb_phi",34,-3.14,3.14),"Reco_tHW_wb_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,0,1),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_h_m","Reco_tHW_h_m",30,0,300),"Reco_tHW_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_log_wb_m","Reco_JABDT_tHW_log_wb_m",25,3.0,8),"Reco_JABDT_tHW_log_wb_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_hdau_phi2","Reco_tHW_hdau_phi2",34,-3.14,3.14),"Reco_tHW_hdau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whad_dr","Reco_tHW_whad_dr",52,0,5.2),"Reco_tHW_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_btop_lepw_dr","Reco_tHW_btop_lepw_dr",45,0,4.5),"Reco_tHW_btop_lepw_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_wtop_phi","Reco_tHW_wtop_phi",34,-3.14,3.14),"Reco_tHW_wtop_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_abs_wb_eta","Reco_JABDT_tHW_abs_wb_eta",42,0.0,4.2),"Reco_JABDT_tHW_abs_wb_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_wb_eta","Reco_tHW_wb_eta",42,-4.2,4.2),"Reco_tHW_wb_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_hdau_m1","Reco_tHW_hdau_m1",45,0,90),"Reco_tHW_hdau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_h_dr","Reco_tHW_h_dr",40,0,4),"Reco_tHW_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_top_phi","Reco_tHW_top_phi",34,-3.14,3.14),"Reco_tHW_top_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whaddau_phi2","Reco_tHW_whaddau_phi2",34,-3.14,3.14),"Reco_tHW_whaddau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whaddau_phi1","Reco_tHW_whaddau_phi1",34,-3.14,3.14),"Reco_tHW_whaddau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_log_wb_pt","Reco_JABDT_tHW_log_wb_pt",50,0.0,7.5),"Reco_JABDT_tHW_log_wb_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_top_eta","Reco_tHW_top_eta",42,-4.2,4.2),"Reco_tHW_top_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_hdau_idx2","Reco_tHW_hdau_idx2",15,0,15),"Reco_tHW_hdau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_hdau_idx1","Reco_tHW_hdau_idx1",15,0,15),"Reco_tHW_hdau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whad_eta","Reco_tHW_whad_eta",40,-4.0,4.0),"Reco_tHW_whad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_wlep_pt__M__whad_pt","Reco_JABDT_tHW_wlep_pt__M__whad_pt",35,0,350),"Reco_JABDT_tHW_wlep_pt__M__whad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_hdau_phi1","Reco_tHW_hdau_phi1",34,-3.14,3.14),"Reco_tHW_hdau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_btop_pt","Reco_tHW_btop_pt",30,0,300),"Reco_tHW_btop_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_leptonictop","Reco_tHW_leptonictop",10,0,1),"Reco_tHW_leptonictop",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHW_costheta_btop_lep","Reco_JABDT_tHW_costheta_btop_lep",50,-1.0,1.0),"Reco_JABDT_tHW_costheta_btop_lep",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_top_m","Reco_tHW_top_m",70,0,700),"Reco_tHW_top_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whad_m","Reco_tHW_whad_m",40,0,400),"Reco_tHW_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whaddau_pt2","Reco_tHW_whaddau_pt2",20,0,200),"Reco_tHW_whaddau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHW_whaddau_pt1","Reco_tHW_whaddau_pt1",40,0,400),"Reco_tHW_whaddau_pt1",selection,label),
    ]
    return plots_tHW

def plots_tHQReco(cat,selection,label):
    plots_THQ=[
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",20,-1,1),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_top_phi","Reco_tHq_top_phi",34,-3.14,3.14),"Reco_tHq_top_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_btop_idx","Reco_tHq_btop_idx",15,0,15),"Reco_tHq_btop_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_top_pt__P__h_pt__P__ljet_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_tHq_top_pt__P__h_pt__P__ljet_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",50,0,1),"Reco_JABDT_tHq_top_pt__P__h_pt__P__ljet_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_abs_btop_eta","Reco_JABDT_tHq_abs_btop_eta",25,0.0,2.5),"Reco_JABDT_tHq_abs_btop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_abs_ljet_eta","Reco_JABDT_tHq_abs_ljet_eta",33,0.0,3.3),"Reco_JABDT_tHq_abs_ljet_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_hdau_phi1","Reco_tHq_hdau_phi1",34,-3.14,3.14),"Reco_tHq_hdau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_hdau_phi2","Reco_tHq_hdau_phi2",34,-3.14,3.14),"Reco_tHq_hdau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_h_eta","Reco_tHq_h_eta",45,-4.5,4.5),"Reco_tHq_h_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_hdau_pt2","Reco_tHq_hdau_pt2",35,0,350),"Reco_tHq_hdau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_h_m","Reco_tHq_h_m",50,0,250),"Reco_tHq_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_ljet_idx","Reco_tHq_ljet_idx",15,0,15),"Reco_tHq_ljet_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_hdau_pt1","Reco_tHq_hdau_pt1",35,0,350),"Reco_tHq_hdau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_log_h_m","Reco_JABDT_tHq_log_h_m",21,3.0,7.2),"Reco_JABDT_tHq_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_ljet_phi","Reco_tHq_ljet_phi",34,-3.14,3.14),"Reco_tHq_ljet_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_abs_ljet_eta__M__btop_eta","Reco_JABDT_tHq_abs_ljet_eta__M__btop_eta",50,0.0,5.0),"Reco_JABDT_tHq_abs_ljet_eta__M__btop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_h_pt","Reco_tHq_h_pt",60,0,600),"Reco_tHq_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_log_ljet_pt","Reco_JABDT_tHq_log_ljet_pt",21,3.0,7.2),"Reco_JABDT_tHq_log_ljet_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_hdau_idx1","Reco_tHq_hdau_idx1",15,0,15),"Reco_tHq_hdau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_hdau_idx2","Reco_tHq_hdau_idx2",15,0,15),"Reco_tHq_hdau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_btop_w_dr","Reco_tHq_btop_w_dr",42,0,4.2),"Reco_tHq_btop_w_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_abs_top_eta","Reco_JABDT_tHq_abs_top_eta",45,0.0,4.5),"Reco_JABDT_tHq_abs_top_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_btop_pt","Reco_tHq_btop_pt",35,0,350),"Reco_tHq_btop_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_top_pt","Reco_tHq_top_pt",80,0,800),"Reco_tHq_top_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_hdau_eta2","Reco_tHq_hdau_eta2",50,-2.5,2.5),"Reco_tHq_hdau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_h_phi","Reco_tHq_h_phi",34,-3.14,3.14),"Reco_tHq_h_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_costheta_btop_lep","Reco_JABDT_tHq_costheta_btop_lep",50,-1.0,1.0),"Reco_JABDT_tHq_costheta_btop_lep",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_top_h_dr","Reco_tHq_top_h_dr",50,0,5),"Reco_tHq_top_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_log_top_m","Reco_JABDT_tHq_log_top_m",30,4.2,7.2),"Reco_JABDT_tHq_log_top_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_log_top_pt","Reco_JABDT_tHq_log_top_pt",41,-1.0,7.2),"Reco_JABDT_tHq_log_top_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_ljet_pt","Reco_tHq_ljet_pt",60,0,600),"Reco_tHq_ljet_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_costhetastar","Reco_tHq_costhetastar",50,-1.0,1.0),"Reco_tHq_costhetastar",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",21,3.0,7.2),"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_ljet_e__M__btop_e","Reco_JABDT_tHq_ljet_e__M__btop_e",60,0,600),"Reco_JABDT_tHq_ljet_e__M__btop_e",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_Jet_CSV_ljet","Reco_JABDT_tHq_Jet_CSV_ljet",50,0,1),"Reco_JABDT_tHq_Jet_CSV_ljet",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_top_eta","Reco_tHq_top_eta",45,-4.5,4.5),"Reco_tHq_top_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_top_m","Reco_tHq_top_m",70,50,750),"Reco_tHq_top_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_btop_m","Reco_tHq_btop_m",40,0,100),"Reco_tHq_btop_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_btop_phi","Reco_tHq_btop_phi",34,-3.14,3.14),"Reco_tHq_btop_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_btop_eta","Reco_tHq_btop_eta",50,-2.5,2.5),"Reco_tHq_btop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_abs_h_eta","Reco_JABDT_tHq_abs_h_eta",45,0.0,4.5),"Reco_JABDT_tHq_abs_h_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_log_h_pt","Reco_JABDT_tHq_log_h_pt",41,-1.0,7.2),"Reco_JABDT_tHq_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_Jet_CSV_hdau1","Reco_JABDT_tHq_Jet_CSV_hdau1",50,0,1),"Reco_JABDT_tHq_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_abs_top_eta__M__higg_eta","Reco_JABDT_tHq_abs_top_eta__M__higg_eta",60,0.0,6.0),"Reco_JABDT_tHq_abs_top_eta__M__higg_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_Jet_CSV_hdau2","Reco_JABDT_tHq_Jet_CSV_hdau2",50,0,1),"Reco_JABDT_tHq_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_hdau_m2","Reco_tHq_hdau_m2",50,0,125),"Reco_tHq_hdau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_JABDT_tHq_Jet_CSV_btop","Reco_JABDT_tHq_Jet_CSV_btop",50,0,1),"Reco_JABDT_tHq_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_btop_lep_dr","Reco_tHq_btop_lep_dr",42,0,4.2),"Reco_tHq_btop_lep_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_hdau_m1","Reco_tHq_hdau_m1",50,0,125),"Reco_tHq_hdau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_h_dr","Reco_tHq_h_dr",40,0,4),"Reco_tHq_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_ljet_eta","Reco_tHq_ljet_eta",40,-4.0,4.0),"Reco_tHq_ljet_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_ljet_m","Reco_tHq_ljet_m",55,0,110),"Reco_tHq_ljet_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Reco_tHq_hdau_eta1","Reco_tHq_hdau_eta1",50,-2.5,2.5),"Reco_tHq_hdau_eta1",selection,label),
    ]
    return plots_THQ

#baseline
def plots_ge4j_ge3t(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    tag = "ge4j_ge3t"
    # plots = plots_control_mem(tag, selection, label)    
    plots = plots_control(tag, selection, label)    
    plots += plots_ttHReco(tag, selection, label)
    plots += plots_ttbarReco(tag, selection, label)
    plots += plots_tHWReco(tag, selection, label)
    plots += plots_tHQReco(tag, selection, label) 

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

#analysis categories w/o forward stuff
def plots_ge4j_3t(data=None):
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"

    tag = "ge4j_3t"
    # plots = plots_control_mem(tag, selection, label)    
    plots = plots_control(tag, selection, label)    
    plots += plots_ttHReco(tag, selection, label)
    plots += plots_ttbarReco(tag, selection, label)
    plots += plots_tHWReco(tag, selection, label)
    plots += plots_tHQReco(tag, selection, label) 

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge4j_ge4t(data=None):
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)"

    tag = "ge4j_ge4t"
    # plots = plots_control_mem(tag, selection, label)    
    plots = plots_control(tag, selection, label)    
    plots += plots_ttHReco(tag, selection, label)
    plots += plots_ttbarReco(tag, selection, label)
    plots += plots_tHWReco(tag, selection, label)
    plots += plots_tHQReco(tag, selection, label)  

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

#analysis categories w/ N_Jets=Normal+Fwd Jets
def plots_ge4j_fwd_3t(data=None):
    label = "\geq 4 (jets+fwd-jets), 3 b-tags"
    selection = "((N_Jets+N_ForwardJets)>=4&&N_BTagsM==3)"

    tag = "ge4j_fwd_3t"
    plots = plots_control(tag, selection, label)    
    plots += plots_ttHReco(tag, selection, label)
    plots += plots_ttbarReco(tag, selection, label)
    plots += plots_tHWReco(tag, selection, label)
    plots += plots_tHQReco(tag, selection, label) 

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge4j_fwd_ge4t(data=None):
    label = "\geq 4 (jets+fwd-jets), \geq 4 b-tags"
    selection = "((N_Jets+N_ForwardJets)>=4&&N_BTagsM>=4)"

    tag = "ge4j_fwd_ge4t"
    plots = plots_control(tag, selection, label)    
    plots += plots_ttHReco(tag, selection, label)
    plots += plots_ttbarReco(tag, selection, label)
    plots += plots_tHWReco(tag, selection, label)
    plots += plots_tHQReco(tag, selection, label)  

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

#analysis categories w/ explicit forward requirement
def plots_ge4j_3t_0fwd(data=None):
    label = "\geq 4 jets, 3 b-tags, = 0 fwd-jets"
    selection = "(N_Jets>=4&&N_BTagsM==3&&N_ForwardJets==0)"

    tag = "ge4j_3t_0fwd"
    plots = plots_control(tag, selection, label)    
    plots += plots_ttHReco(tag, selection, label)
    plots += plots_ttbarReco(tag, selection, label)
    plots += plots_tHWReco(tag, selection, label)
    plots += plots_tHQReco(tag, selection, label)  

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge4j_ge4t_0fwd(data=None):
    label = "\geq 4 jets, \geq 4 b-tags, = 0 fwd-jets"
    selection = "(N_Jets>=4&&N_BTagsM>=4&&N_ForwardJets==0)"

    tag = "ge4j_ge4t_0fwd"
    plots = plots_control(tag, selection, label)    
    plots += plots_ttHReco(tag, selection, label)
    plots += plots_ttbarReco(tag, selection, label)
    plots += plots_tHWReco(tag, selection, label)
    plots += plots_tHQReco(tag, selection, label)  

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge3j_ge3t_ge1fwd(data=None):
    label = "\geq 3 jets, \geq 3 b-tags, \geq 1 fwd-jets"
    selection = "(N_Jets>=3&&N_BTagsM>=3&&N_ForwardJets>=1)"

    tag = "ge3j_ge3t_1fwd"
    plots = plots_control(tag, selection, label)    
    plots += plots_ttHReco(tag, selection, label)
    plots += plots_ttbarReco(tag, selection, label)
    plots += plots_tHWReco(tag, selection, label)
    plots += plots_tHQReco(tag, selection, label)  

    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    #baseline
    #discriminatorPlots += plots_ge4j_ge3t(data)

    #analysis categories w/o forward stuff
    #discriminatorPlots += plots_ge4j_3t(data)
    #discriminatorPlots += plots_ge4j_ge4t(data)

    #analysis categories w/ N_Jets=Normal+Fwd Jets
    discriminatorPlots += plots_ge4j_fwd_3t(data)
    discriminatorPlots += plots_ge4j_fwd_ge4t(data)

    #analysis categories w/ explicit forward requirement
    #discriminatorPlots += plots_ge4j_3t_0fwd(data)
    #discriminatorPlots += plots_ge4j_ge4t_0fwd(data)
    #discriminatorPlots += plots_ge3j_ge3t_ge1fwd(data)

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
