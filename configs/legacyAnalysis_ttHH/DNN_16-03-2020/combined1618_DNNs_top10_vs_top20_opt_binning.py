
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import util.variableHistoInterface as vhi
import ROOT
from array import array
from copy import deepcopy


memexp = ""



def plots_top20_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_CSV_1","CSV[1]",50,0.277,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_CSV_2","CSV[2]",50,0.277,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_Dr_minDrTaggedJets","Evt_Dr_minDrTaggedJets",50,0.35,2.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_M2_JetsAverage","Evt_M2_JetsAverage",50,50.0,600.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",50,40.0,1000.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_M_JetsAverage","Evt_M_JetsAverage",50,5.0,50.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_M_minDrLepTag","Evt_M_minDrLepTag",50,15.0,400.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_N_BTagsM","N_BTagsM",5,3.5,8.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_hdau2","Reco_JABDT_tHW_Jet_CSV_hdau2",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1","Reco_JABDT_tHW_Jet_CSV_whaddau1",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_tHW_energy_fraction",50,-1.5,1.0),"Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop","Reco_JABDT_tHq_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHq_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1","Reco_JABDT_tHq_Jet_CSV_hdau1",50,-1.5,1.0),"Reco_JABDT_tHq_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta","Reco_JABDT_tHq_abs_ljet_eta",50,-1.5,4.5),"Reco_JABDT_tHq_abs_ljet_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_tHq_ljet_e__M__btop_e","Reco_JABDT_tHq_ljet_e__M__btop_e",50,-1000.0,2000.0),"Reco_JABDT_tHq_ljet_e__M__btop_e",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_btoplep","Reco_JABDT_ttH_Jet_CSV_btoplep",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2","Reco_JABDT_ttH_Jet_CSV_hdau2",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_m","Reco_JABDT_ttH_log_toplep_m",50,-1.5,7.5),"Reco_JABDT_ttH_log_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep","Reco_JABDT_ttbar_Jet_CSV_btoplep",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1","Reco_JABDT_ttbar_Jet_CSV_whaddau1",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2","Reco_JABDT_ttbar_Jet_CSV_whaddau2",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_tHW_bestJABDToutput","Reco_tHW_bestJABDToutput",50,-1.0,0.6),"Reco_tHW_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_tHW_top_h_dr","Reco_tHW_top_h_dr",50,-1.5,8.0),"Reco_tHW_top_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_tHW_whad_dr","Reco_tHW_whad_dr",50,-1.5,5.0),"Reco_tHW_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_tHW_whaddau_m1","Reco_tHW_whaddau_m1",50,-1.5,100.0),"Reco_tHW_whaddau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_tHq_costhetastar","Reco_tHq_costhetastar",50,-5.0,1.0),"Reco_tHq_costhetastar",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_ttH_bestJABDToutput","Reco_ttH_bestJABDToutput",50,-1.0,0.7),"Reco_ttH_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_ttH_toplep_m","Reco_ttH_toplep_m",50,-1.5,750.0),"Reco_ttH_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_ttbar_bestJABDToutput","Reco_ttbar_bestJABDToutput",50,-0.4,0.7),"Reco_ttbar_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,80.0,500.0),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_TaggedJet_M_0","TaggedJet_M[0]",50,0.0,200.0),"TaggedJet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_ge4t_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_top20_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_CSV_1","CSV[1]",50,0.277,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_CSV_dev","Evt_CSV_dev",50,0.0,0.25),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_CSV_min_tagged","Evt_CSV_min_tagged",50,0.277,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",50,0.5,4.0),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_HT_tags","Evt_HT_tags",50,100.0,1000.0),"Evt_HT_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_JetPt_over_JetE","Evt_JetPt_over_JetE",50,0.0,1.0),"Evt_JetPt_over_JetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_M2_JetsAverage","Evt_M2_JetsAverage",50,50.0,600.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_M_JetsAverage","Evt_M_JetsAverage",50,5.0,50.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_M_Total","Evt_M_Total",50,200.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Evt_h1","Evt_h1",50,-0.2,0.4),"Evt_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1","Reco_JABDT_tHW_Jet_CSV_whaddau1",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_tHW_log_top_m","Reco_JABDT_tHW_log_top_m",50,-1.5,8.0),"Reco_JABDT_tHW_log_top_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_tHW_log_wb_m","Reco_JABDT_tHW_log_wb_m",50,-1.5,8.5),"Reco_JABDT_tHW_log_wb_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_tHq_log_ljet_pt","Reco_JABDT_tHq_log_ljet_pt",50,3.0,7.5),"Reco_JABDT_tHq_log_ljet_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep","Reco_JABDT_ttH_Jet_CSV_btoplep",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2","Reco_JABDT_ttH_Jet_CSV_hdau2",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad","Reco_JABDT_ttbar_Jet_CSV_btophad",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_btophad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep","Reco_JABDT_ttbar_Jet_CSV_btoplep",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1","Reco_JABDT_ttbar_Jet_CSV_whaddau1",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2","Reco_JABDT_ttbar_Jet_CSV_whaddau2",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m","Reco_JABDT_ttbar_log_tophad_m",50,4.0,8.0),"Reco_JABDT_ttbar_log_tophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_JABDT_ttbar_log_whad_m","Reco_JABDT_ttbar_log_whad_m",50,3.0,8.0),"Reco_JABDT_ttbar_log_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_tHW_bestJABDToutput","Reco_tHW_bestJABDToutput",50,-1.0,0.6),"Reco_tHW_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_tHW_whad_dr","Reco_tHW_whad_dr",50,-1.5,5.0),"Reco_tHW_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_tHq_ljet_m","Reco_tHq_ljet_m",50,10.0,75.0),"Reco_tHq_ljet_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_ttH_bestJABDToutput","Reco_ttH_bestJABDToutput",50,-1.0,0.7),"Reco_ttH_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_ttbar_bestJABDToutput","Reco_ttbar_bestJABDToutput",50,-0.4,0.7),"Reco_ttbar_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,80.0,500.0),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_Reco_ttbar_whad_m","Reco_ttbar_whad_m",50,0.0,600.0),"Reco_ttbar_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top20_ge4j_3t_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_top10_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_CSV_2","CSV[2]",50,0.277,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_M_JetsAverage","Evt_M_JetsAverage",50,5.0,50.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_M_minDrLepTag","Evt_M_minDrLepTag",50,15.0,400.0),"Evt_M_minDrLepTag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50,30.0,500.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_whaddau1","Reco_JABDT_tHW_Jet_CSV_whaddau1",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_tHW_energy_fraction",50,-1.5,1.0),"Reco_JABDT_tHW_top_pt__P__h_pt__P__wb_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1","Reco_JABDT_tHq_Jet_CSV_hdau1",50,-1.5,1.0),"Reco_JABDT_tHq_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_JABDT_tHq_abs_ljet_eta","Reco_JABDT_tHq_abs_ljet_eta",50,-1.5,4.5),"Reco_JABDT_tHq_abs_ljet_eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_JABDT_ttH_Jet_CSV_hdau2","Reco_JABDT_ttH_Jet_CSV_hdau2",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1","Reco_JABDT_ttbar_Jet_CSV_whaddau1",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2","Reco_JABDT_ttbar_Jet_CSV_whaddau2",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_tHW_bestJABDToutput","Reco_tHW_bestJABDToutput",50,-1.0,0.6),"Reco_tHW_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_ttH_bestJABDToutput","Reco_ttH_bestJABDToutput",50,-1.0,0.7),"Reco_ttH_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_ttH_toplep_m","Reco_ttH_toplep_m",50,-1.5,750.0),"Reco_ttH_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_ttbar_bestJABDToutput","Reco_ttbar_bestJABDToutput",50,-0.4,0.7),"Reco_ttbar_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,80.0,500.0),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_ge4t_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_top10_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_CSV_dev","Evt_CSV_dev",50,0.0,0.25),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_HT_tags","Evt_HT_tags",50,100.0,1000.0),"Evt_HT_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_JetPt_over_JetE","Evt_JetPt_over_JetE",50,0.0,1.0),"Evt_JetPt_over_JetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_M_JetsAverage","Evt_M_JetsAverage",50,5.0,50.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,5.0,70.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_M_Total","Evt_M_Total",50,200.0,3000.0),"Evt_M_Total",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,600.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Evt_h1","Evt_h1",50,-0.2,0.4),"Evt_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1","Reco_JABDT_tHW_Jet_CSV_whaddau1",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_JABDT_tHW_log_wb_m","Reco_JABDT_tHW_log_wb_m",50,-1.5,8.5),"Reco_JABDT_tHW_log_wb_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_btoplep","Reco_JABDT_ttH_Jet_CSV_btoplep",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad","Reco_JABDT_ttbar_Jet_CSV_btophad",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_btophad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep","Reco_JABDT_ttbar_Jet_CSV_btoplep",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1","Reco_JABDT_ttbar_Jet_CSV_whaddau1",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_tHW_bestJABDToutput","Reco_tHW_bestJABDToutput",50,-1.0,0.6),"Reco_tHW_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_tHW_whad_dr","Reco_tHW_whad_dr",50,-1.5,5.0),"Reco_tHW_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_ttH_bestJABDToutput","Reco_ttH_bestJABDToutput",50,-1.0,0.7),"Reco_ttH_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_ttbar_bestJABDToutput","Reco_ttbar_bestJABDToutput",50,-0.4,0.7),"Reco_ttbar_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,80.0,500.0),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_Reco_ttbar_whad_m","Reco_ttbar_whad_m",50,0.0,600.0),"Reco_ttbar_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_top10_ge4j_3t_memDBp","MEM",50,0.0,1.0),memexp,selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_dnn(data, discrname):

    ndefaultbins = 15
    interfaces = []


    # plots for top20_ge4j_ge4t

    interf_ljets_top20_ge4j_ge4t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_ge4t_node_ttH",
                                            label          = "ljets_top20_ge4j_ge4t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==0))")
    interf_ljets_top20_ge4j_ge4t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==0))","ljets_top20_ge4j_ge4t_ttH_node","")
    interf_ljets_top20_ge4j_ge4t_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top20_ge4j_ge4t_ttH_node.bin_edges = [ 
                0.21,
                0.2333,
                0.2567,
                0.28,
                0.3033,
                0.3267,
                0.35,
                0.3733,
                0.3967,
                0.42,
                0.4433,
                0.4667,
                0.49,
                0.5133,
                0.5367,
                0.56,
                0.5833,
                0.63,
                0.6767,
                0.84
                ]
    interf_ljets_top20_ge4j_ge4t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_ge4t_ttH_node)
    
    interf_ljets_top20_ge4j_ge4t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_ge4t_node_ttmb",
                                            label          = "ljets_top20_ge4j_ge4t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==1))")
    interf_ljets_top20_ge4j_ge4t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==1))","ljets_top20_ge4j_ge4t_ttmb_node","")
    interf_ljets_top20_ge4j_ge4t_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top20_ge4j_ge4t_ttmb_node.bin_edges = [ 
                0.159,
                0.216,
                0.235,
                0.254,
                0.273,
                0.292,
                0.311,
                0.33,
                0.349,
                0.368,
                0.387,
                0.406,
                0.425,
                0.444,
                0.463,
                0.482,
                0.501,
                0.539,
                0.71
                ]
    interf_ljets_top20_ge4j_ge4t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_ge4t_ttmb_node)
    
    interf_ljets_top20_ge4j_ge4t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_top20_ge4j_ge4t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==2))")
    interf_ljets_top20_ge4j_ge4t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==2))","ljets_top20_ge4j_ge4t_tt2b_node","")
    interf_ljets_top20_ge4j_ge4t_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top20_ge4j_ge4t_tt2b_node.bin_edges = [ 
                0.204,
                # 0.2253,
                # 0.2467,
                # 0.268,
                # 0.2893,
                # 0.3107,
                # 0.332,
                # 0.3533,
                # 0.3747,
                # 0.396,
                # 0.4173,
                # 0.4387,
                # 0.4813,
                0.78
                ]
    interf_ljets_top20_ge4j_ge4t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_ge4t_tt2b_node)
    
    interf_ljets_top20_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_top20_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==3))")
    interf_ljets_top20_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==3))","ljets_top20_ge4j_ge4t_ttcc_node","")
    interf_ljets_top20_ge4j_ge4t_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top20_ge4j_ge4t_ttcc_node.bin_edges = [ 
                0.21,
                # 0.2217,
                # 0.2333,
                # 0.245,
                # 0.2567,
                # 0.2683,
                # 0.28,
                # 0.2917,
                # 0.3033,
                # 0.315,
                # 0.3267,
                # 0.3383,
                # 0.35,
                # 0.3617,
                # 0.3733,
                # 0.385,
                # 0.3967,
                # 0.4083,
                # 0.42,
                # 0.4317,
                0.49
                ]
    interf_ljets_top20_ge4j_ge4t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_ge4t_ttcc_node)
    
    interf_ljets_top20_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_top20_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==4))")
    interf_ljets_top20_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==4))","ljets_top20_ge4j_ge4t_ttlf_node","")
    interf_ljets_top20_ge4j_ge4t_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top20_ge4j_ge4t_ttlf_node.bin_edges = [ 
                0.2147,
                # 0.2333,
                # 0.252,
                # 0.2707,
                # 0.2893,
                # 0.308,
                # 0.3267,
                # 0.3453,
                # 0.364,
                # 0.3827,
                # 0.4013,
                # 0.42,
                # 0.4387,
                # 0.4573,
                # 0.476,
                # 0.4947,
                # 0.5133,
                # 0.532,
                # 0.5507,
                # 0.5693,
                # 0.588,
                # 0.6067,
                # 0.644,
                0.7
                ]
    interf_ljets_top20_ge4j_ge4t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_ge4t_ttlf_node)
    
    interf_ljets_top20_ge4j_ge4t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_ge4t_node_tHq",
                                            label          = "ljets_top20_ge4j_ge4t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==5))")
    interf_ljets_top20_ge4j_ge4t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==5))","ljets_top20_ge4j_ge4t_tHq_node","")
    interf_ljets_top20_ge4j_ge4t_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top20_ge4j_ge4t_tHq_node.bin_edges = [ 
                0.226,
                0.2547,
                0.2833,
                0.312,
                0.3407,
                0.3693,
                0.398,
                0.4267,
                0.4553,
                0.484,
                0.5127,
                0.5413,
                0.57,
                0.5987,
                0.6273,
                0.656,
                0.6847,
                0.7133,
                0.742,
                0.7993,
                0.8567,
                1.0
                ]
    interf_ljets_top20_ge4j_ge4t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_ge4t_tHq_node)
    
    interf_ljets_top20_ge4j_ge4t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_ge4t_node_tHW",
                                            label          = "ljets_top20_ge4j_ge4t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==6))")
    interf_ljets_top20_ge4j_ge4t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top20_ge4j_ge4t==6))","ljets_top20_ge4j_ge4t_tHW_node","")
    interf_ljets_top20_ge4j_ge4t_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top20_ge4j_ge4t_tHW_node.bin_edges = [ 
                0.226,
                0.2547,
                0.2833,
                0.312,
                0.3407,
                0.3693,
                0.398,
                0.4267,
                0.4553,
                0.484,
                0.5127,
                0.57,
                0.6273,
                0.6847,
                0.7707,
                0.8853,
                1.0
                ]
    interf_ljets_top20_ge4j_ge4t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_ge4t_tHW_node)
    


    # plots for top20_ge4j_3t

    interf_ljets_top20_ge4j_3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_3t_node_ttH",
                                            label          = "ljets_top20_ge4j_3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==0))")
    interf_ljets_top20_ge4j_3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==0))","ljets_top20_ge4j_3t_ttH_node","")
    interf_ljets_top20_ge4j_3t_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top20_ge4j_3t_ttH_node.bin_edges = [ 
                0.1603,
                0.1807,
                0.201,
                0.2213,
                0.2417,
                0.262,
                0.2823,
                0.3027,
                0.323,
                0.3433,
                0.3637,
                0.384,
                0.4043,
                0.4247,
                0.445,
                0.4653,
                0.4857,
                0.506,
                0.5263,
                0.5467,
                0.567,
                0.6077,
                0.75
                ]
    interf_ljets_top20_ge4j_3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_3t_ttH_node)
    
    interf_ljets_top20_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_3t_node_ttmb",
                                            label          = "ljets_top20_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==1))")
    interf_ljets_top20_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==1))","ljets_top20_ge4j_3t_ttmb_node","")
    interf_ljets_top20_ge4j_3t_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top20_ge4j_3t_ttmb_node.bin_edges = [ 
                0.173,
                0.184,
                0.195,
                0.206,
                0.217,
                0.228,
                0.239,
                0.25,
                0.261,
                0.272,
                0.283,
                0.294,
                0.305,
                0.316,
                0.327,
                0.338,
                0.349,
                0.36,
                0.371,
                0.382,
                0.393,
                0.404,
                0.415,
                0.47
                ]
    interf_ljets_top20_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_3t_ttmb_node)
    
    interf_ljets_top20_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_3t_node_tt2b",
                                            label          = "ljets_top20_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==2))")
    interf_ljets_top20_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==2))","ljets_top20_ge4j_3t_tt2b_node","")
    interf_ljets_top20_ge4j_3t_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top20_ge4j_3t_tt2b_node.bin_edges = [ 
                0.1807,
                # 0.201,
                # 0.2213,
                # 0.2417,
                # 0.262,
                # 0.2823,
                # 0.3027,
                # 0.323,
                # 0.3433,
                # 0.3637,
                # 0.384,
                # 0.4043,
                # 0.4247,
                # 0.445,
                # 0.4653,
                # 0.4857,
                # 0.506,
                # 0.5263,
                # 0.5467,
                # 0.567,
                # 0.5873,
                # 0.6077,
                # 0.6483,
                0.75
                ]
    interf_ljets_top20_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_3t_tt2b_node)
    
    interf_ljets_top20_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_3t_node_ttcc",
                                            label          = "ljets_top20_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==3))")
    interf_ljets_top20_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==3))","ljets_top20_ge4j_3t_ttcc_node","")
    interf_ljets_top20_ge4j_3t_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top20_ge4j_3t_ttcc_node.bin_edges = [ 
                0.175,
                # 0.1867,
                # 0.1983,
                # 0.21,
                # 0.2217,
                # 0.2333,
                # 0.245,
                # 0.2567,
                # 0.2683,
                # 0.28,
                # 0.2917,
                # 0.3033,
                # 0.315,
                # 0.3267,
                # 0.3383,
                # 0.35,
                # 0.3617,
                # 0.3733,
                # 0.385,
                # 0.3967,
                # 0.4083,
                # 0.42,
                # 0.4317,
                # 0.4433,
                0.49
                ]
    interf_ljets_top20_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_3t_ttcc_node)
    
    interf_ljets_top20_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_3t_node_ttlf",
                                            label          = "ljets_top20_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==4))")
    interf_ljets_top20_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==4))","ljets_top20_ge4j_3t_ttlf_node","")
    interf_ljets_top20_ge4j_3t_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top20_ge4j_3t_ttlf_node.bin_edges = [ 
                0.1623,
                # 0.1847,
                # 0.207,
                # 0.2293,
                # 0.2517,
                # 0.274,
                # 0.2963,
                # 0.3187,
                # 0.341,
                # 0.3633,
                # 0.3857,
                # 0.408,
                # 0.4303,
                # 0.4527,
                # 0.475,
                # 0.4973,
                # 0.5197,
                # 0.542,
                # 0.5643,
                # 0.5867,
                # 0.609,
                # 0.6313,
                # 0.6537,
                # 0.676,
                # 0.6983,
                # 0.7207,
                # 0.743,
                0.81
                ]
    interf_ljets_top20_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_3t_ttlf_node)
    
    interf_ljets_top20_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_3t_node_tHq",
                                            label          = "ljets_top20_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==5))")
    interf_ljets_top20_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==5))","ljets_top20_ge4j_3t_tHq_node","")
    interf_ljets_top20_ge4j_3t_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top20_ge4j_3t_tHq_node.bin_edges = [ 
                0.1677,
                0.1953,
                0.223,
                0.2507,
                0.2783,
                0.306,
                0.3337,
                0.3613,
                0.389,
                0.4167,
                0.4443,
                0.472,
                0.4997,
                0.5273,
                0.555,
                0.5827,
                0.6103,
                0.638,
                0.6657,
                0.6933,
                0.721,
                0.7487,
                0.7763,
                0.804,
                0.8317,
                0.8593,
                0.887,
                0.97
                ]
    interf_ljets_top20_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_3t_tHq_node)
    
    interf_ljets_top20_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top20_ge4j_3t_node_tHW",
                                            label          = "ljets_top20_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==6))")
    interf_ljets_top20_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top20_ge4j_3t==6))","ljets_top20_ge4j_3t_tHW_node","")
    interf_ljets_top20_ge4j_3t_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top20_ge4j_3t_tHW_node.bin_edges = [ 
                0.1687,
                0.1973,
                0.226,
                0.2547,
                0.2833,
                0.312,
                0.3407,
                0.3693,
                0.398,
                0.4267,
                0.4553,
                0.484,
                0.5127,
                0.5413,
                0.57,
                0.5987,
                0.6273,
                0.656,
                0.6847,
                0.7133,
                0.742,
                0.7707,
                0.7993,
                0.828,
                0.8567,
                0.8853,
                0.914,
                0.9427,
                1.0
                ]
    interf_ljets_top20_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top20_ge4j_3t_tHW_node)
    


    # plots for top10_ge4j_ge4t

    interf_ljets_top10_ge4j_ge4t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttH",
                                            label          = "ljets_top10_ge4j_ge4t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0))")
    interf_ljets_top10_ge4j_ge4t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==0))","ljets_top10_ge4j_ge4t_ttH_node","")
    interf_ljets_top10_ge4j_ge4t_ttH_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttH_node.bin_edges = [ 
                0.207,
                0.2293,
                0.2517,
                0.274,
                0.2963,
                0.3187,
                0.341,
                0.3633,
                0.3857,
                0.408,
                0.4303,
                0.4527,
                0.475,
                0.4973,
                0.5197,
                0.542,
                0.5643,
                0.5867,
                0.609,
                0.6537,
                0.81
                ]
    interf_ljets_top10_ge4j_ge4t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttH_node)
    
    interf_ljets_top10_ge4j_ge4t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttmb",
                                            label          = "ljets_top10_ge4j_ge4t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==1))")
    interf_ljets_top10_ge4j_ge4t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==1))","ljets_top10_ge4j_ge4t_ttmb_node","")
    interf_ljets_top10_ge4j_ge4t_ttmb_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttmb_node.bin_edges = [ 
                0.2133,
                0.2317,
                0.25,
                0.2683,
                0.2867,
                0.305,
                0.3233,
                0.3417,
                0.36,
                0.3783,
                0.3967,
                0.415,
                0.4333,
                0.4517,
                0.47,
                0.4883,
                0.525,
                0.69
                ]
    interf_ljets_top10_ge4j_ge4t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttmb_node)
    
    interf_ljets_top10_ge4j_ge4t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_top10_ge4j_ge4t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==2))")
    interf_ljets_top10_ge4j_ge4t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==2))","ljets_top10_ge4j_ge4t_tt2b_node","")
    interf_ljets_top10_ge4j_ge4t_tt2b_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_tt2b_node.bin_edges = [ 
                0.198,
                # 0.2173,
                # 0.2367,
                # 0.256,
                # 0.2753,
                # 0.2947,
                # 0.314,
                # 0.3333,
                # 0.3527,
                # 0.372,
                # 0.3913,
                # 0.43,
                # 0.4687,
                0.72
                ]
    interf_ljets_top10_ge4j_ge4t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_tt2b_node)
    
    interf_ljets_top10_ge4j_ge4t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_top10_ge4j_ge4t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==3))")
    interf_ljets_top10_ge4j_ge4t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==3))","ljets_top10_ge4j_ge4t_ttcc_node","")
    interf_ljets_top10_ge4j_ge4t_ttcc_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttcc_node.bin_edges = [ 
                0.1933,
                # 0.2147,
                # 0.2253,
                # 0.236,
                # 0.2467,
                # 0.2573,
                # 0.268,
                # 0.2787,
                # 0.2893,
                # 0.3,
                # 0.3107,
                # 0.3213,
                # 0.332,
                # 0.3427,
                # 0.3533,
                # 0.364,
                # 0.3747,
                # 0.3853,
                # 0.4067,
                0.46
                ]
    interf_ljets_top10_ge4j_ge4t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttcc_node)
    
    interf_ljets_top10_ge4j_ge4t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_top10_ge4j_ge4t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==4))")
    interf_ljets_top10_ge4j_ge4t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==4))","ljets_top10_ge4j_ge4t_ttlf_node","")
    interf_ljets_top10_ge4j_ge4t_ttlf_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_ttlf_node.bin_edges = [ 
                0.199,
                # 0.2187,
                # 0.2383,
                # 0.258,
                # 0.2777,
                # 0.2973,
                # 0.317,
                # 0.3367,
                # 0.3563,
                # 0.376,
                # 0.3957,
                # 0.4153,
                # 0.435,
                # 0.4547,
                # 0.4743,
                # 0.494,
                # 0.5137,
                # 0.5333,
                # 0.553,
                # 0.5727,
                # 0.5923,
                # 0.612,
                # 0.6513,
                0.73
                ]
    interf_ljets_top10_ge4j_ge4t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_ttlf_node)
    
    interf_ljets_top10_ge4j_ge4t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_tHq",
                                            label          = "ljets_top10_ge4j_ge4t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==5))")
    interf_ljets_top10_ge4j_ge4t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==5))","ljets_top10_ge4j_ge4t_tHq_node","")
    interf_ljets_top10_ge4j_ge4t_tHq_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_tHq_node.bin_edges = [ 
                0.225,
                0.2533,
                0.2817,
                0.31,
                0.3383,
                0.3667,
                0.395,
                0.4233,
                0.4517,
                0.48,
                0.5083,
                0.5367,
                0.565,
                0.5933,
                0.6217,
                0.65,
                0.6783,
                0.7067,
                0.735,
                0.7917,
                0.8483,
                0.99
                ]
    interf_ljets_top10_ge4j_ge4t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_tHq_node)
    
    interf_ljets_top10_ge4j_ge4t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_ge4t_node_tHW",
                                            label          = "ljets_top10_ge4j_ge4t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==6))")
    interf_ljets_top10_ge4j_ge4t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_top10_ge4j_ge4t==6))","ljets_top10_ge4j_ge4t_tHW_node","")
    interf_ljets_top10_ge4j_ge4t_tHW_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_top10_ge4j_ge4t_tHW_node.bin_edges = [ 
                0.226,
                0.2547,
                0.2833,
                0.312,
                0.3407,
                0.3693,
                0.398,
                0.4267,
                0.4553,
                0.484,
                0.5127,
                0.5413,
                0.57,
                0.6273,
                0.6847,
                0.7707,
                0.8853,
                1.0
                ]
    interf_ljets_top10_ge4j_ge4t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_ge4t_tHW_node)
    


    # plots for top10_ge4j_3t

    interf_ljets_top10_ge4j_3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttH",
                                            label          = "ljets_top10_ge4j_3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0))")
    interf_ljets_top10_ge4j_3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==0))","ljets_top10_ge4j_3t_ttH_node","")
    interf_ljets_top10_ge4j_3t_ttH_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttH_node.bin_edges = [ 
                0.178,
                0.197,
                0.216,
                0.235,
                0.254,
                0.273,
                0.292,
                0.311,
                0.33,
                0.349,
                0.368,
                0.387,
                0.406,
                0.425,
                0.444,
                0.463,
                0.482,
                0.501,
                0.52,
                0.539,
                0.558,
                0.577,
                0.596,
                0.71
                ]
    interf_ljets_top10_ge4j_3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttH_node)
    
    interf_ljets_top10_ge4j_3t_ttmb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttmb",
                                            label          = "ljets_top10_ge4j_3t_ttmb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==1))")
    interf_ljets_top10_ge4j_3t_ttmb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==1))","ljets_top10_ge4j_3t_ttmb_node","")
    interf_ljets_top10_ge4j_3t_ttmb_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttmb_node.bin_edges = [ 
                0.172,
                0.1827,
                0.1933,
                0.204,
                0.2147,
                0.2253,
                0.236,
                0.2467,
                0.2573,
                0.268,
                0.2787,
                0.2893,
                0.3,
                0.3107,
                0.3213,
                0.332,
                0.3427,
                0.3533,
                0.364,
                0.3747,
                0.3853,
                0.396,
                0.4173,
                0.46
                ]
    interf_ljets_top10_ge4j_3t_ttmb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttmb_node)
    
    interf_ljets_top10_ge4j_3t_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_tt2b",
                                            label          = "ljets_top10_ge4j_3t_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==2))")
    interf_ljets_top10_ge4j_3t_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==2))","ljets_top10_ge4j_3t_tt2b_node","")
    interf_ljets_top10_ge4j_3t_tt2b_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_tt2b_node.bin_edges = [ 
                0.1793,
                # 0.199,
                # 0.2187,
                # 0.2383,
                # 0.258,
                # 0.2777,
                # 0.2973,
                # 0.317,
                # 0.3367,
                # 0.3563,
                # 0.376,
                # 0.3957,
                # 0.4153,
                # 0.435,
                # 0.4547,
                # 0.4743,
                # 0.494,
                # 0.5137,
                # 0.5333,
                # 0.553,
                # 0.5727,
                # 0.5923,
                # 0.612,
                0.73
                ]
    interf_ljets_top10_ge4j_3t_tt2b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_tt2b_node)
    
    interf_ljets_top10_ge4j_3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttcc",
                                            label          = "ljets_top10_ge4j_3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==3))")
    interf_ljets_top10_ge4j_3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==3))","ljets_top10_ge4j_3t_ttcc_node","")
    interf_ljets_top10_ge4j_3t_ttcc_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttcc_node.bin_edges = [ 
                0.176,
                # 0.188,
                # 0.2,
                # 0.212,
                # 0.224,
                # 0.236,
                # 0.248,
                # 0.26,
                # 0.272,
                # 0.284,
                # 0.296,
                # 0.308,
                # 0.32,
                # 0.332,
                # 0.344,
                # 0.356,
                # 0.368,
                # 0.38,
                # 0.392,
                # 0.404,
                # 0.416,
                # 0.428,
                # 0.44,
                0.5
                ]
    interf_ljets_top10_ge4j_3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttcc_node)
    
    interf_ljets_top10_ge4j_3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_ttlf",
                                            label          = "ljets_top10_ge4j_3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==4))")
    interf_ljets_top10_ge4j_3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==4))","ljets_top10_ge4j_3t_ttlf_node","")
    interf_ljets_top10_ge4j_3t_ttlf_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_ttlf_node.bin_edges = [ 
                0.1613,
                # 0.1827,
                # 0.204,
                # 0.2253,
                # 0.2467,
                # 0.268,
                # 0.2893,
                # 0.3107,
                # 0.332,
                # 0.3533,
                # 0.3747,
                # 0.396,
                # 0.4173,
                # 0.4387,
                # 0.46,
                # 0.4813,
                # 0.5027,
                # 0.524,
                # 0.5453,
                # 0.5667,
                # 0.588,
                # 0.6093,
                # 0.6307,
                # 0.652,
                # 0.6733,
                # 0.6947,
                # 0.716,
                # 0.7373,
                0.78
                ]
    interf_ljets_top10_ge4j_3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_ttlf_node)
    
    interf_ljets_top10_ge4j_3t_tHq_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_tHq",
                                            label          = "ljets_top10_ge4j_3t_tHq_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==5))")
    interf_ljets_top10_ge4j_3t_tHq_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==5))","ljets_top10_ge4j_3t_tHq_node","")
    interf_ljets_top10_ge4j_3t_tHq_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_tHq_node.bin_edges = [ 
                0.1683,
                0.1967,
                0.225,
                0.2533,
                0.2817,
                0.31,
                0.3383,
                0.3667,
                0.395,
                0.4233,
                0.4517,
                0.48,
                0.5083,
                0.5367,
                0.565,
                0.5933,
                0.6217,
                0.65,
                0.6783,
                0.7067,
                0.735,
                0.7633,
                0.7917,
                0.82,
                0.8483,
                0.8767,
                0.99
                ]
    interf_ljets_top10_ge4j_3t_tHq_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_tHq_node)
    
    interf_ljets_top10_ge4j_3t_tHW_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_top10_ge4j_3t_node_tHW",
                                            label          = "ljets_top10_ge4j_3t_tHW_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==6))")
    interf_ljets_top10_ge4j_3t_tHW_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_top10_ge4j_3t==6))","ljets_top10_ge4j_3t_tHW_node","")
    interf_ljets_top10_ge4j_3t_tHW_node.category_label = "\geq 4 jets, 3 b-tags"
    interf_ljets_top10_ge4j_3t_tHW_node.bin_edges = [ 
                0.1687,
                0.1973,
                0.226,
                0.2547,
                0.2833,
                0.312,
                0.3407,
                0.3693,
                0.398,
                0.4267,
                0.4553,
                0.484,
                0.5127,
                0.5413,
                0.57,
                0.5987,
                0.6273,
                0.656,
                0.6847,
                0.7133,
                0.742,
                0.7707,
                0.7993,
                0.828,
                0.8567,
                0.8853,
                0.914,
                0.9427,
                1.0
                ]
    interf_ljets_top10_ge4j_3t_tHW_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_top10_ge4j_3t_tHW_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    # discriminatorPlots += plots_top20_ge4j_ge4t(data)
    # discriminatorPlots += plots_top20_ge4j_3t(data)
    # discriminatorPlots += plots_top10_ge4j_ge4t(data)
    # discriminatorPlots += plots_top10_ge4j_3t(data)
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def init_plots(interfaces, data = None):
    plots = [] #init list of plotClasses objects to return
    dictionary = {}
    for interf in interfaces:

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if not interf.bin_edges is None:
            bins  = array("f", interf.bin_edges)
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            interf.nhistobins = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,bins),
                    interf.varname,interf.selection,interf.category_label))

        elif not (interf.minxval is None or interf.maxxval is None):
            nbins = interf.nhistobins
            xmax  = interf.maxxval
            xmin  = interf.minxval
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,xmin, xmax),
                    interf.varname,interf.selection,interf.category_label))
        else:
            print("FATAL ERROR: Unable to load bin edges or min/max values for histogram!")
            print(interf)
            raise ValueError
        dictionary[interf.label] = interf.getDictionary()

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    