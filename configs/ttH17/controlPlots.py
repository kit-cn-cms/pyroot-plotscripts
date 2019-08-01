
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

def plots_ge4j_ge3t(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Pt","p_{T}(electron)",50,0,200),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Eta","#eta(electron)",50,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Electron_Phi","#phi(electron)",50,-3.1416,3.1416),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Pt","p_{T}(muon)",50,0,200),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Eta","#eta(muon)",50,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Muon_Phi","#phi(muon)",50,-3.1416,3.1416),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Pt","p_{T}(lepton)",50,0,200),"LooseLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Eta","#eta(lepton)",50,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Lepton_Phi","#phi(lepton)",50,-3.1416,3.1416),"LooseLepton_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_Jets","N_Jets",12,0,12),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_BTagsM","N_BTagsM",8,0,8),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt","Jet_Pt",50,0,800),"Jet_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt0","Leading Jet_Pt",50,0,800),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt1","Subleading Jet_Pt",50,0,800),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV","DeepCSV",50,0,1),"CSV",selection,label),
        ]

    plots_ttH=[
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whaddau_m1","Reco_ttH_whaddau_m1",50,0,50),"Reco_ttH_whaddau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whaddau_m2","Reco_ttH_whaddau_m2",50,0,50),"Reco_ttH_whaddau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_log_toplep_pt","Reco_JABDT_ttH_log_toplep_pt",50,-1.0,20),"Reco_JABDT_ttH_log_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_hdau_eta2","Reco_ttH_hdau_eta2",50,-4.2,4.2),"Reco_ttH_hdau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whad_eta","Reco_ttH_whad_eta",50,-4.2,4.2),"Reco_ttH_whad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_Jet_CSV_hdau2","Reco_JABDT_ttH_Jet_CSV_hdau2",50,0,1),"Reco_JABDT_ttH_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_hdau_eta1","Reco_ttH_hdau_eta1",50,-4.2,4.2),"Reco_ttH_hdau_eta1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btophad_m","Reco_ttH_btophad_m",50,0,200),"Reco_ttH_btophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_tophad_pt","Reco_ttH_tophad_pt",50,0,200),"Reco_ttH_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btoplep_m","Reco_ttH_btoplep_m",50,0,200),"Reco_ttH_btoplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whaddau_phi2","Reco_ttH_whaddau_phi2",50,-5.2,3.2),"Reco_ttH_whaddau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btophad_eta","Reco_ttH_btophad_eta",50,-4.2,4.2),"Reco_ttH_btophad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whaddau_phi1","Reco_ttH_whaddau_phi1",50,-5.2,3.2),"Reco_ttH_whaddau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_h_pt","Reco_ttH_h_pt",50,0,200),"Reco_ttH_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_toplep_pt","Reco_ttH_toplep_pt",50,0,200),"Reco_ttH_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btoplep_w_dr","Reco_ttH_btoplep_w_dr",50,0,4),"Reco_ttH_btoplep_w_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_Jet_CSV_hdau1","Reco_JABDT_ttH_Jet_CSV_hdau1",50,0,1),"Reco_JABDT_ttH_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_hdau_pt1","Reco_ttH_hdau_pt1",50,0,200),"Reco_ttH_hdau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_Jet_CSV_whaddau2","Reco_JABDT_ttH_Jet_CSV_whaddau2",50,0,1),"Reco_JABDT_ttH_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_hdau_pt2","Reco_ttH_hdau_pt2",50,0,200),"Reco_ttH_hdau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_toplep_m","Reco_ttH_toplep_m",50,0,200),"Reco_ttH_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_hdau_idx1","Reco_ttH_hdau_idx1",50,0,200),"Reco_ttH_hdau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_toplep_eta","Reco_ttH_toplep_eta",50,-4.2,4.2),"Reco_ttH_toplep_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_hdau_idx2","Reco_ttH_hdau_idx2",50,0,200),"Reco_ttH_hdau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",50,0,10),"Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_Jet_CSV_btoplep","Reco_JABDT_ttH_Jet_CSV_btoplep",50,0,1),"Reco_JABDT_ttH_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whad_dr","Reco_ttH_whad_dr",50,0,4),"Reco_ttH_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whad_phi","Reco_ttH_whad_phi",50,-5.2,3.2),"Reco_ttH_whad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_h_m","Reco_ttH_h_m",50,0,200),"Reco_ttH_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btoplep_phi","Reco_ttH_btoplep_phi",50,-3.2,3.2),"Reco_ttH_btoplep_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_toplep_phi","Reco_ttH_toplep_phi",50,-3.2,3.2),"Reco_ttH_toplep_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_Jet_CSV_whaddau1","Reco_JABDT_ttH_Jet_CSV_whaddau1",50,0,1),"Reco_JABDT_ttH_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_log_tophad_m__M__whad_m","Reco_JABDT_ttH_log_tophad_m__M__whad_m",50,-1.0,20),"Reco_JABDT_ttH_log_tophad_m__M__whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whaddau_eta1","Reco_ttH_whaddau_eta1",50,-4.2,4.2),"Reco_ttH_whaddau_eta1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_hdau_m2","Reco_ttH_hdau_m2",50,0,200),"Reco_ttH_hdau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_tophad_m","Reco_ttH_tophad_m",50,0,200),"Reco_ttH_tophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whaddau_eta2","Reco_ttH_whaddau_eta2",50,-4.2,4.2),"Reco_ttH_whaddau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btophad_idx","Reco_ttH_btophad_idx",50,0,200),"Reco_ttH_btophad_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whad_pt","Reco_ttH_whad_pt",50,0,200),"Reco_ttH_whad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_toplep_w_dr","Reco_ttH_toplep_w_dr",50,0,4),"Reco_ttH_toplep_w_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_log_toplep_m","Reco_JABDT_ttH_log_toplep_m",50,-1.0,20),"Reco_JABDT_ttH_log_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_hdau_phi1","Reco_ttH_hdau_phi1",50,-3.2,3.2),"Reco_ttH_hdau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_hdau_phi2","Reco_ttH_hdau_phi2",50,-3.2,3.2),"Reco_ttH_hdau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_h_eta","Reco_ttH_h_eta",50,-4.2,4.2),"Reco_ttH_h_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_tophad_eta","Reco_ttH_tophad_eta",50,-4.2,4.2),"Reco_ttH_tophad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whaddau_pt1","Reco_ttH_whaddau_pt1",50,0,200),"Reco_ttH_whaddau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btoplep_pt","Reco_ttH_btoplep_pt",50,0,200),"Reco_ttH_btoplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btophad_phi","Reco_ttH_btophad_phi",50,-3.2,3.2),"Reco_ttH_btophad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whaddau_pt2","Reco_ttH_whaddau_pt2",50,0,200),"Reco_ttH_whaddau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btoplep_eta","Reco_ttH_btoplep_eta",50,-4.2,4.2),"Reco_ttH_btoplep_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_h_dr","Reco_ttH_h_dr",50,0,4),"Reco_ttH_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_hdau_m1","Reco_ttH_hdau_m1",50,0,200),"Reco_ttH_hdau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_h_phi","Reco_ttH_h_phi",50,-3.2,3.2),"Reco_ttH_h_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whaddau_idx2","Reco_ttH_whaddau_idx2",50,0,200),"Reco_ttH_whaddau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_Jet_CSV_btophad","Reco_JABDT_ttH_Jet_CSV_btophad",50,0,1),"Reco_JABDT_ttH_Jet_CSV_btophad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_tophad_dr","Reco_ttH_tophad_dr",50,0,4),"Reco_ttH_tophad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whaddau_idx1","Reco_ttH_whaddau_idx1",50,0,200),"Reco_ttH_whaddau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_log_h_pt","Reco_JABDT_ttH_log_h_pt",50,-1.0,15),"Reco_JABDT_ttH_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btoplep_idx","Reco_ttH_btoplep_idx",50,0,200),"Reco_ttH_btoplep_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_btophad_pt","Reco_ttH_btophad_pt",50,0,200),"Reco_ttH_btophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_whad_m","Reco_ttH_whad_m",50,0,200),"Reco_ttH_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_log_h_m","Reco_JABDT_ttH_log_h_m",50,0.0,15),"Reco_JABDT_ttH_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_log_tophad_pt","Reco_JABDT_ttH_log_tophad_pt",50,-1.0,20),"Reco_JABDT_ttH_log_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttH_tophad_phi","Reco_ttH_tophad_phi",50,-3.2,3.2),"Reco_ttH_tophad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttH_log_whad_m","Reco_JABDT_ttH_log_whad_m",50,-1.0,20),"Reco_JABDT_ttH_log_whad_m",selection,label),
        ]
    plots_ttbar=[
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2","Reco_JABDT_ttbar_Jet_CSV_whaddau2",50,0,1),"Reco_JABDT_ttbar_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_btophad_pt","Reco_ttbar_btophad_pt",50,0,200),"Reco_ttbar_btophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1","Reco_JABDT_ttbar_Jet_CSV_whaddau1",50,0,1),"Reco_JABDT_ttbar_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whaddau_idx1","Reco_ttbar_whaddau_idx1",50,0,200),"Reco_ttbar_whaddau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_costheta_toplep_tophad","Reco_JABDT_ttbar_costheta_toplep_tophad",50,-1.0,2.2),"Reco_JABDT_ttbar_costheta_toplep_tophad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whaddau_idx2","Reco_ttbar_whaddau_idx2",50,0,200),"Reco_ttbar_whaddau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whaddau_phi1","Reco_ttbar_whaddau_phi1",50,-5.2,3.2),"Reco_ttbar_whaddau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_tophad_m","Reco_ttbar_tophad_m",50,0,200),"Reco_ttbar_tophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whaddau_phi2","Reco_ttbar_whaddau_phi2",50,-5.2,3.2),"Reco_ttbar_whaddau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_log_toplep_pt","Reco_JABDT_ttbar_log_toplep_pt",50,-1.0,20),"Reco_JABDT_ttbar_log_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_btophad_eta","Reco_ttbar_btophad_eta",50,-4.2,4.2),"Reco_ttbar_btophad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_btoplep_eta","Reco_ttbar_btoplep_eta",50,-4.2,4.2),"Reco_ttbar_btoplep_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_btophad_phi","Reco_ttbar_btophad_phi",50,-3.2,3.2),"Reco_ttbar_btophad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_tophad_dr","Reco_ttbar_tophad_dr",50,0,4),"Reco_ttbar_tophad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_btoplep_phi","Reco_ttbar_btoplep_phi",50,-3.2,3.2),"Reco_ttbar_btoplep_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_Jet_CSV_btoplep","Reco_JABDT_ttbar_Jet_CSV_btoplep",50,0,1),"Reco_JABDT_ttbar_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whad_m","Reco_ttbar_whad_m",50,0,200),"Reco_ttbar_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_Jet_CSV_btophad","Reco_JABDT_ttbar_Jet_CSV_btophad",50,0,1),"Reco_JABDT_ttbar_Jet_CSV_btophad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whaddau_m2","Reco_ttbar_whaddau_m2",50,0,50),"Reco_ttbar_whaddau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whaddau_m1","Reco_ttbar_whaddau_m1",50,0,50),"Reco_ttbar_whaddau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_toplep_phi","Reco_ttbar_toplep_phi",50,-3.2,3.2),"Reco_ttbar_toplep_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_log_tophad_m__M__whad_m","Reco_JABDT_ttbar_log_tophad_m__M__whad_m",50,-1.0,20),"Reco_JABDT_ttbar_log_tophad_m__M__whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_tophad_eta","Reco_ttbar_tophad_eta",50,-4.2,4.2),"Reco_ttbar_tophad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whad_dr","Reco_ttbar_whad_dr",50,0,4),"Reco_ttbar_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_tophad_pt","Reco_ttbar_tophad_pt",50,0,200),"Reco_ttbar_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_btoplep_idx","Reco_ttbar_btoplep_idx",50,0,200),"Reco_ttbar_btoplep_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_tophad_pt__P__toplep_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_ttbar_tophad_pt__P__toplep_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",50,0,10),"Reco_JABDT_ttbar_tophad_pt__P__toplep_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_toplep_pt","Reco_ttbar_toplep_pt",50,0,200),"Reco_ttbar_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whaddau_eta2","Reco_ttbar_whaddau_eta2",50,-4.2,4.2),"Reco_ttbar_whaddau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,0,200),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whaddau_eta1","Reco_ttbar_whaddau_eta1",50,-4.2,4.2),"Reco_ttbar_whaddau_eta1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_tophad_phi","Reco_ttbar_tophad_phi",50,-3.2,3.2),"Reco_ttbar_tophad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whad_pt","Reco_ttbar_whad_pt",50,0,200),"Reco_ttbar_whad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_btophad_idx","Reco_ttbar_btophad_idx",50,0,200),"Reco_ttbar_btophad_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_LeptonicW_Eta","Reco_LeptonicW_Eta",50,0,200),"Reco_LeptonicW_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_btoplep_pt","Reco_ttbar_btoplep_pt",50,0,200),"Reco_ttbar_btoplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whad_eta","Reco_ttbar_whad_eta",50,-4.2,4.2),"Reco_ttbar_whad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whaddau_pt1","Reco_ttbar_whaddau_pt1",50,0,200),"Reco_ttbar_whaddau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whaddau_pt2","Reco_ttbar_whaddau_pt2",50,0,200),"Reco_ttbar_whaddau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_LeptonicW_M","Reco_LeptonicW_M",50,0,200),"Reco_LeptonicW_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_toplep_eta","Reco_ttbar_toplep_eta",50,-4.2,4.2),"Reco_ttbar_toplep_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_btophad_m","Reco_ttbar_btophad_m",50,0,200),"Reco_ttbar_btophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_whad_phi","Reco_ttbar_whad_phi",50,-5.2,3.2),"Reco_ttbar_whad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_log_tophad_pt","Reco_JABDT_ttbar_log_tophad_pt",50,-1.0,20),"Reco_JABDT_ttbar_log_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_LeptonicW_Phi","Reco_LeptonicW_Phi",50,0,200),"Reco_LeptonicW_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_ttbar_btoplep_m","Reco_ttbar_btoplep_m",50,0,200),"Reco_ttbar_btoplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_LeptonicW_Pt","Reco_LeptonicW_Pt",50,0,200),"Reco_LeptonicW_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_log_toplep_m","Reco_JABDT_ttbar_log_toplep_m",50,-1.0,20),"Reco_JABDT_ttbar_log_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_ttbar_log_whad_m","Reco_JABDT_ttbar_log_whad_m",50,-1.0,20),"Reco_JABDT_ttbar_log_whad_m",selection,label),
    ]
    plots_tHW=[
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_abs_top_eta","Reco_JABDT_tHW_abs_top_eta",50,-1.2,4.2),"Reco_JABDT_tHW_abs_top_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whad_phi","Reco_tHW_whad_phi",50,-5.2,3.2),"Reco_tHW_whad_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_log_h_pt","Reco_JABDT_tHW_log_h_pt",50,-1.0,15),"Reco_JABDT_tHW_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_abs_btop_eta","Reco_JABDT_tHW_abs_btop_eta",50,-1.2,4.2),"Reco_JABDT_tHW_abs_btop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_log_h_m","Reco_JABDT_tHW_log_h_m",50,-0.0,15),"Reco_JABDT_tHW_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_log_whad_pt","Reco_JABDT_tHW_log_whad_pt",50,-1.0,20),"Reco_JABDT_tHW_log_whad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whaddau_idx2","Reco_tHW_whaddau_idx2",50,0,200),"Reco_tHW_whaddau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whaddau_idx1","Reco_tHW_whaddau_idx1",50,0,200),"Reco_tHW_whaddau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_wb_h_dr","Reco_tHW_wb_h_dr",50,0,4),"Reco_tHW_wb_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_btop_phi","Reco_tHW_btop_phi",50,-3.2,3.2),"Reco_tHW_btop_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_h_eta","Reco_tHW_h_eta",50,-4.2,4.2),"Reco_tHW_h_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_wtop_eta","Reco_tHW_wtop_eta",50,-4.2,4.2),"Reco_tHW_wtop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_wb_pt","Reco_tHW_wb_pt",50,0,200),"Reco_tHW_wb_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whaddau_eta1","Reco_tHW_whaddau_eta1",50,-4.2,4.2),"Reco_tHW_whaddau_eta1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whaddau_eta2","Reco_tHW_whaddau_eta2",50,-4.2,4.2),"Reco_tHW_whaddau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_top_h_dr","Reco_tHW_top_h_dr",50,0,4),"Reco_tHW_top_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whad_pt","Reco_tHW_whad_pt",50,0,200),"Reco_tHW_whad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_hdau_eta1","Reco_tHW_hdau_eta1",50,-4.2,4.2),"Reco_tHW_hdau_eta1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_btop_eta","Reco_tHW_btop_eta",50,-4.2,4.2),"Reco_tHW_btop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_btop_m","Reco_tHW_btop_m",50,0,200),"Reco_tHW_btop_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_hdau_eta2","Reco_tHW_hdau_eta2",50,-4.2,4.2),"Reco_tHW_hdau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_h_pt","Reco_tHW_h_pt",50,0,200),"Reco_tHW_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_log_whad_m","Reco_JABDT_tHW_log_whad_m",50,-1.0,20),"Reco_JABDT_tHW_log_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_abs_top_eta__M__wb_eta","Reco_JABDT_tHW_abs_top_eta__M__wb_eta",50,-1.2,5.2),"Reco_JABDT_tHW_abs_top_eta__M__wb_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_wtop_pt","Reco_tHW_wtop_pt",50,0,200),"Reco_tHW_wtop_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_Jet_CSV_hdau2","Reco_JABDT_tHW_Jet_CSV_hdau2",50,0,1),"Reco_JABDT_tHW_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_hdau_pt1","Reco_tHW_hdau_pt1",50,0,200),"Reco_tHW_hdau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_hdau_pt2","Reco_tHW_hdau_pt2",50,0,200),"Reco_tHW_hdau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_abs_top_eta__M__higg_eta","Reco_JABDT_tHW_abs_top_eta__M__higg_eta",50,-1.2,5.2),"Reco_JABDT_tHW_abs_top_eta__M__higg_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_btop_idx","Reco_tHW_btop_idx",50,0,200),"Reco_tHW_btop_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_hdau_m2","Reco_tHW_hdau_m2",50,0,200),"Reco_tHW_hdau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_h_phi","Reco_tHW_h_phi",50,-3.2,3.2),"Reco_tHW_h_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_wb_m","Reco_tHW_wb_m",50,0,200),"Reco_tHW_wb_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",50,0,10),"Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_wtop_m","Reco_tHW_wtop_m",50,0,200),"Reco_tHW_wtop_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_wtop_h_dr","Reco_tHW_wtop_h_dr",50,0,4),"Reco_tHW_wtop_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_log_top_m","Reco_JABDT_tHW_log_top_m",50,-0.0,10),"Reco_JABDT_tHW_log_top_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_abs_wlep_eta__M__whad_eta","Reco_JABDT_tHW_abs_wlep_eta__M__whad_eta",50,-4.2,4.2),"Reco_JABDT_tHW_abs_wlep_eta__M__whad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_log_top_pt","Reco_JABDT_tHW_log_top_pt",50,-0.0,10),"Reco_JABDT_tHW_log_top_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whaddau_m1","Reco_tHW_whaddau_m1",50,0,50),"Reco_tHW_whaddau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_top_pt","Reco_tHW_top_pt",50,0,200),"Reco_tHW_top_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_Jet_CSV_hdau1","Reco_JABDT_tHW_Jet_CSV_hdau1",50,0,1),"Reco_JABDT_tHW_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whaddau_m2","Reco_tHW_whaddau_m2",50,0,50),"Reco_tHW_whaddau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_wb_phi","Reco_tHW_wb_phi",50,-3.2,3.2),"Reco_tHW_wb_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,0,1),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_h_m","Reco_tHW_h_m",50,0,200),"Reco_tHW_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_log_wb_m","Reco_JABDT_tHW_log_wb_m",50,-1.0,20),"Reco_JABDT_tHW_log_wb_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_hdau_phi2","Reco_tHW_hdau_phi2",50,-3.2,3.2),"Reco_tHW_hdau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whad_dr","Reco_tHW_whad_dr",50,0,4),"Reco_tHW_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_btop_lepw_dr","Reco_tHW_btop_lepw_dr",50,0,4),"Reco_tHW_btop_lepw_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_wtop_phi","Reco_tHW_wtop_phi",50,-3.2,3.2),"Reco_tHW_wtop_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_abs_wb_eta","Reco_JABDT_tHW_abs_wb_eta",50,-1.2,4.2),"Reco_JABDT_tHW_abs_wb_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_wb_eta","Reco_tHW_wb_eta",50,-4.2,4.2),"Reco_tHW_wb_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_hdau_m1","Reco_tHW_hdau_m1",50,0,200),"Reco_tHW_hdau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_h_dr","Reco_tHW_h_dr",50,0,4),"Reco_tHW_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_top_phi","Reco_tHW_top_phi",50,-3.2,3.2),"Reco_tHW_top_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whaddau_phi2","Reco_tHW_whaddau_phi2",50,-5.2,3.2),"Reco_tHW_whaddau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whaddau_phi1","Reco_tHW_whaddau_phi1",50,-5.2,3.2),"Reco_tHW_whaddau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_log_wb_pt","Reco_JABDT_tHW_log_wb_pt",50,-1.0,20),"Reco_JABDT_tHW_log_wb_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_top_eta","Reco_tHW_top_eta",50,-4.2,4.2),"Reco_tHW_top_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_hdau_idx2","Reco_tHW_hdau_idx2",50,0,200),"Reco_tHW_hdau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_hdau_idx1","Reco_tHW_hdau_idx1",50,0,200),"Reco_tHW_hdau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whad_eta","Reco_tHW_whad_eta",50,-1.2,4.2),"Reco_tHW_whad_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_wlep_pt__M__whad_pt","Reco_JABDT_tHW_wlep_pt__M__whad_pt",50,0,200),"Reco_JABDT_tHW_wlep_pt__M__whad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_hdau_phi1","Reco_tHW_hdau_phi1",50,-3.2,3.2),"Reco_tHW_hdau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_btop_pt","Reco_tHW_btop_pt",50,0,200),"Reco_tHW_btop_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_leptonictop","Reco_tHW_leptonictop",50,0,200),"Reco_tHW_leptonictop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHW_costheta_btop_lep","Reco_JABDT_tHW_costheta_btop_lep",50,-1.0,1.2),"Reco_JABDT_tHW_costheta_btop_lep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_top_m","Reco_tHW_top_m",50,0,200),"Reco_tHW_top_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whad_m","Reco_tHW_whad_m",50,0,200),"Reco_tHW_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whaddau_pt2","Reco_tHW_whaddau_pt2",50,0,200),"Reco_tHW_whaddau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHW_whaddau_pt1","Reco_tHW_whaddau_pt1",50,0,200),"Reco_tHW_whaddau_pt1",selection,label),
    ]
    plots_THQ=[
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_top_phi","Reco_tHq_top_phi",50,-3.2,3.2),"Reco_tHq_top_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_btop_idx","Reco_tHq_btop_idx",50,0,200),"Reco_tHq_btop_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_top_pt__P__h_pt__P__ljet_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_tHq_top_pt__P__h_pt__P__ljet_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",50,0,10),"Reco_JABDT_tHq_top_pt__P__h_pt__P__ljet_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_abs_btop_eta","Reco_JABDT_tHq_abs_btop_eta",50,-1.2,4.2),"Reco_JABDT_tHq_abs_btop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_abs_ljet_eta","Reco_JABDT_tHq_abs_ljet_eta",50,-1.2,4.2),"Reco_JABDT_tHq_abs_ljet_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_hdau_phi1","Reco_tHq_hdau_phi1",50,-3.2,3.2),"Reco_tHq_hdau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_hdau_phi2","Reco_tHq_hdau_phi2",50,-3.2,3.2),"Reco_tHq_hdau_phi2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_h_eta","Reco_tHq_h_eta",50,-4.2,4.2),"Reco_tHq_h_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_hdau_pt2","Reco_tHq_hdau_pt2",50,0,200),"Reco_tHq_hdau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_h_m","Reco_tHq_h_m",50,0,200),"Reco_tHq_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_ljet_idx","Reco_tHq_ljet_idx",50,0,200),"Reco_tHq_ljet_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_hdau_pt1","Reco_tHq_hdau_pt1",50,0,200),"Reco_tHq_hdau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_log_h_m","Reco_JABDT_tHq_log_h_m",50,-0.0,15),"Reco_JABDT_tHq_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_ljet_phi","Reco_tHq_ljet_phi",50,-3.2,3.2),"Reco_tHq_ljet_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_abs_ljet_eta__M__btop_eta","Reco_JABDT_tHq_abs_ljet_eta__M__btop_eta",50,-1.2,5.2),"Reco_JABDT_tHq_abs_ljet_eta__M__btop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_h_pt","Reco_tHq_h_pt",50,0,200),"Reco_tHq_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_log_ljet_pt","Reco_JABDT_tHq_log_ljet_pt",50,-1.0,15),"Reco_JABDT_tHq_log_ljet_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_hdau_idx1","Reco_tHq_hdau_idx1",50,0,200),"Reco_tHq_hdau_idx1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_hdau_idx2","Reco_tHq_hdau_idx2",50,0,200),"Reco_tHq_hdau_idx2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_btop_w_dr","Reco_tHq_btop_w_dr",50,0,4),"Reco_tHq_btop_w_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_abs_top_eta","Reco_JABDT_tHq_abs_top_eta",50,-1.2,4.2),"Reco_JABDT_tHq_abs_top_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_btop_pt","Reco_tHq_btop_pt",50,0,200),"Reco_tHq_btop_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_top_pt","Reco_tHq_top_pt",50,0,200),"Reco_tHq_top_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_hdau_eta2","Reco_tHq_hdau_eta2",50,-4.2,4.2),"Reco_tHq_hdau_eta2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_h_phi","Reco_tHq_h_phi",50,-3.2,3.2),"Reco_tHq_h_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_costheta_btop_lep","Reco_JABDT_tHq_costheta_btop_lep",50,-1.0,1.2),"Reco_JABDT_tHq_costheta_btop_lep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_top_h_dr","Reco_tHq_top_h_dr",50,0,4),"Reco_tHq_top_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_log_top_m","Reco_JABDT_tHq_log_top_m",50,-0.0,10),"Reco_JABDT_tHq_log_top_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_log_top_pt","Reco_JABDT_tHq_log_top_pt",50,-0.0,10),"Reco_JABDT_tHq_log_top_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_ljet_pt","Reco_tHq_ljet_pt",50,0,200),"Reco_tHq_ljet_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_costhetastar","Reco_tHq_costhetastar",50,-1.0,1.2),"Reco_tHq_costhetastar",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",50,-0.0,10),"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_ljet_e__M__btop_e","Reco_JABDT_tHq_ljet_e__M__btop_e",50,-2,400),"Reco_JABDT_tHq_ljet_e__M__btop_e",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_Jet_CSV_ljet","Reco_JABDT_tHq_Jet_CSV_ljet",50,0,1),"Reco_JABDT_tHq_Jet_CSV_ljet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_top_eta","Reco_tHq_top_eta",50,-4.2,4.2),"Reco_tHq_top_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_top_m","Reco_tHq_top_m",50,0,200),"Reco_tHq_top_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_btop_m","Reco_tHq_btop_m",50,0,200),"Reco_tHq_btop_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_btop_phi","Reco_tHq_btop_phi",50,-3.2,3.2),"Reco_tHq_btop_phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_btop_eta","Reco_tHq_btop_eta",50,-4.2,4.2),"Reco_tHq_btop_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_abs_h_eta","Reco_JABDT_tHq_abs_h_eta",50,-1.2,4.2),"Reco_JABDT_tHq_abs_h_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_log_h_pt","Reco_JABDT_tHq_log_h_pt",50,-1.0,15),"Reco_JABDT_tHq_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_Jet_CSV_hdau1","Reco_JABDT_tHq_Jet_CSV_hdau1",50,0,1),"Reco_JABDT_tHq_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_abs_top_eta__M__higg_eta","Reco_JABDT_tHq_abs_top_eta__M__higg_eta",50,-1.2,5.2),"Reco_JABDT_tHq_abs_top_eta__M__higg_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_Jet_CSV_hdau2","Reco_JABDT_tHq_Jet_CSV_hdau2",50,0,1),"Reco_JABDT_tHq_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_hdau_m2","Reco_tHq_hdau_m2",50,0,200),"Reco_tHq_hdau_m2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_JABDT_tHq_Jet_CSV_btop","Reco_JABDT_tHq_Jet_CSV_btop",50,0,1),"Reco_JABDT_tHq_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_btop_lep_dr","Reco_tHq_btop_lep_dr",50,0,4),"Reco_tHq_btop_lep_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_hdau_m1","Reco_tHq_hdau_m1",50,0,200),"Reco_tHq_hdau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_h_dr","Reco_tHq_h_dr",50,0,4),"Reco_tHq_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_ljet_eta","Reco_tHq_ljet_eta",50,-4.2,4.2),"Reco_tHq_ljet_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_ljet_m","Reco_tHq_ljet_m",50,0,200),"Reco_tHq_ljet_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Reco_tHq_hdau_eta1","Reco_tHq_hdau_eta1",50,-4.2,4.2),"Reco_tHq_hdau_eta1",selection,label),
    ]


    plots += plots_ttH
    plots += plots_ttbar
    plots += plots_tHW
    plots += plots_THQ

    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge3t(data)

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








