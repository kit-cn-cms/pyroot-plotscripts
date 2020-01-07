
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



def plots_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_CSV_1","CSV[1]",50,0.277,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_CSV_2","CSV[2]",50,0.277,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_CSV_3","CSV[3]",50,0.277,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_dev","Evt_CSV_dev",50,0.0,0.25),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_CSV_min_tagged","Evt_CSV_min_tagged",50,0.277,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets","Evt_Dr_minDrTaggedJets",50,0.35,2.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_E_JetsAverage","Evt_E_JetsAverage",50,40.0,1000.0),"Evt_E_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",50,40.0,1500.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M_JetsAverage","Evt_M_JetsAverage",50,5.0,100.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,4.5,100.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50,30.0,800.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,1500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_h0","Evt_h0",50,0.1,0.45),"Evt_h0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Jet_M_0","Jet_M[0]",50,2.7,240.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Jet_Pt_1","Jet_Pt[1]",50,30.0,1000.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_N_BTagsL","N_BTagsL",50,4.0,9.0),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_N_BTagsM","N_BTagsM",50,4.0,8.0),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_tHW_Jet_CSV_btop","Reco_JABDT_tHW_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_btop","Reco_JABDT_tHq_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHq_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_tHq_Jet_CSV_hdau1","Reco_JABDT_tHq_Jet_CSV_hdau1",50,-1.5,1.0),"Reco_JABDT_tHq_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_tHq_log_top_m","Reco_JABDT_tHq_log_top_m",50,-1.5,7.0),"Reco_JABDT_tHq_log_top_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttH_log_toplep_pt","Reco_JABDT_ttH_log_toplep_pt",50,-1.5,7.0),"Reco_JABDT_ttH_log_toplep_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_btoplep","Reco_JABDT_ttbar_Jet_CSV_btoplep",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau1","Reco_JABDT_ttbar_Jet_CSV_whaddau1",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_ttbar_Jet_CSV_whaddau2","Reco_JABDT_ttbar_Jet_CSV_whaddau2",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_tHW_bestJABDToutput","Reco_tHW_bestJABDToutput",50,-1.0,0.6),"Reco_tHW_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_tHW_hdau_m1","Reco_tHW_hdau_m1",50,-1.5,200.0),"Reco_tHW_hdau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_tHW_hdau_phi1","Reco_tHW_hdau_phi1",50,-5.0,3.1416),"Reco_tHW_hdau_phi1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_tHW_top_h_dr","Reco_tHW_top_h_dr",50,-1.5,10.0),"Reco_tHW_top_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_tHW_whad_dr","Reco_tHW_whad_dr",50,-1.5,8.0),"Reco_tHW_whad_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_tHq_h_m","Reco_tHq_h_m",50,-1.5,2000.0),"Reco_tHq_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_bestJABDToutput","Reco_ttH_bestJABDToutput",50,-1.0,0.7),"Reco_ttH_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_tophad_pt","Reco_ttH_tophad_pt",50,-1.5,2000.0),"Reco_ttH_tophad_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttbar_bestJABDToutput","Reco_ttbar_bestJABDToutput",50,-0.4,0.7),"Reco_ttbar_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_TaggedJet_CSV_0","TaggedJet_CSV[0]",50,0.277,1.0),"TaggedJet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_TaggedJet_CSV_3","TaggedJet_CSV[3]",50,0.277,1.0),"TaggedJet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_TaggedJet_M_3","TaggedJet_M[3]",50,1.5,50.0),"TaggedJet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_TaggedJet_Pt_3","TaggedJet_Pt[3]",50,30.0,400.0),"TaggedJet_Pt[3]",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_CSV_1","CSV[1]",50,0.277,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_CSV_2","CSV[2]",50,0.277,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_CSV_3","CSV[3]",50,0.277,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_avg","Evt_CSV_avg",50,0.15,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_avg_tagged","Evt_CSV_avg_tagged",50,0.3,1.0),"Evt_CSV_avg_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_dev","Evt_CSV_dev",50,0.0,0.25),"Evt_CSV_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_CSV_min_tagged","Evt_CSV_min_tagged",50,0.277,1.0),"Evt_CSV_min_tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",50,0.0,3.0),"Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",50,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_JetPt_over_JetE","Evt_JetPt_over_JetE",50,0.0,1.0),"Evt_JetPt_over_JetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",50,40.0,1500.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,4.5,100.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50,30.0,800.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage","Evt_Pt_TaggedJetsAverage",50,30.0,1000.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,20.0,1500.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_blr_transformed","Evt_blr_transformed",50,-2.5,15.0),"Evt_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_h1","Evt_h1",50,-0.2,0.4),"Evt_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_N_Jets","N_Jets",7,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_hdau2","Reco_JABDT_tHW_Jet_CSV_hdau2",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_tHW_Jet_CSV_whaddau1","Reco_JABDT_tHW_Jet_CSV_whaddau1",50,-1.5,1.0),"Reco_JABDT_tHW_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_tHq_Jet_CSV_btop","Reco_JABDT_tHq_Jet_CSV_btop",50,-1.5,1.0),"Reco_JABDT_tHq_Jet_CSV_btop",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau1","Reco_JABDT_ttH_Jet_CSV_hdau1",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_hdau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttH_Jet_CSV_hdau2","Reco_JABDT_ttH_Jet_CSV_hdau2",50,-1.5,1.0),"Reco_JABDT_ttH_Jet_CSV_hdau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btophad","Reco_JABDT_ttbar_Jet_CSV_btophad",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_btophad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_btoplep","Reco_JABDT_ttbar_Jet_CSV_btoplep",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_btoplep",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau1","Reco_JABDT_ttbar_Jet_CSV_whaddau1",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_Jet_CSV_whaddau2","Reco_JABDT_ttbar_Jet_CSV_whaddau2",50,0.0,1.0),"Reco_JABDT_ttbar_Jet_CSV_whaddau2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_log_tophad_m","Reco_JABDT_ttbar_log_tophad_m",50,0.0,8.0),"Reco_JABDT_ttbar_log_tophad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttbar_log_whad_m","Reco_JABDT_ttbar_log_whad_m",50,0.0,8.0),"Reco_JABDT_ttbar_log_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_tHW_bestJABDToutput","Reco_tHW_bestJABDToutput",50,-1.0,0.6),"Reco_tHW_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_tHW_top_h_dr","Reco_tHW_top_h_dr",50,-1.5,10.0),"Reco_tHW_top_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_tHW_wb_h_dr","Reco_tHW_wb_h_dr",50,-1.5,10.0),"Reco_tHW_wb_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_tHq_bestJABDToutput","Reco_tHq_bestJABDToutput",50,-1.0,0.7),"Reco_tHq_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_bestJABDToutput","Reco_ttH_bestJABDToutput",50,-1.0,0.7),"Reco_ttH_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttbar_bestJABDToutput","Reco_ttbar_bestJABDToutput",50,-0.4,0.7),"Reco_ttbar_bestJABDToutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttbar_toplep_m","Reco_ttbar_toplep_m",50,80.0,2000.0),"Reco_ttbar_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttbar_whad_m","Reco_ttbar_whad_m",50,0.0,2000.0),"Reco_ttbar_whad_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttbar_whaddau_m1","Reco_ttbar_whaddau_m1",50,0.0,250.0),"Reco_ttbar_whaddau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_TaggedJet_M_0","TaggedJet_M[0]",50,0.0,250.0),"TaggedJet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_TaggedJet_M_1","TaggedJet_M[1]",50,0.0,200.0),"TaggedJet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_TaggedJet_M_2","TaggedJet_M[2]",50,0.0,80.0),"TaggedJet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_TaggedJet_Pt_1","TaggedJet_Pt[1]",50,30.0,1000.0),"TaggedJet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_TaggedJet_Pt_2","TaggedJet_Pt[2]",50,30.0,800.0),"TaggedJet_Pt[2]",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge4t(data)
    discriminatorPlots += plots_ge4j_3t(data)

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
    
