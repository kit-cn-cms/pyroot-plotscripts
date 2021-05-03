
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
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",50,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_HT","H_{T}",50,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_HT_wo_MET","H_{T} without MET",50,200.0,1500.0),"Evt_HT_wo_MET",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Evt_Pt_TaggedJetsAverage","Evt_Pt_TaggedJetsAverage",50,30.0,600.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_tHW_log_h_m","Reco_JABDT_tHW_log_h_m",50,-1.5,6.5),"Reco_JABDT_tHW_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_tHW_log_wb_m","Reco_JABDT_tHW_log_wb_m",50,-1.5,8.5),"Reco_JABDT_tHW_log_wb_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",50,-1.5,6.0),"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_tHW_h_dr","Reco_tHW_h_dr",50,-1.5,4.0),"Reco_tHW_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_tHW_h_pt","Reco_tHW_h_pt",50,-1.5,600.0),"Reco_tHW_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_h_pt","Reco_ttH_h_pt",50,-1.5,600.0),"Reco_ttH_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Reco_ttH_hdau_m1","Reco_ttH_hdau_m1",50,-1.5,75.0),"Reco_ttH_hdau_m1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_TaggedJet_Pt_1","TaggedJet_Pt[1]",50,30.0,700.0),"TaggedJet_Pt[1]",selection,label),
        
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Pt_0","Jet_Pt[0]",50,30.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Pt_1","Jet_Pt[1]",50,30.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Pt_2","Jet_Pt[2]",50,30.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Pt_3","Jet_Pt[3]",50,30.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Pt_4","Jet_Pt[4]",50,30.0,600.0),"Jet_Pt[4]",selection+"&&(N_Jets>=5)","\geq 5 jets, \geq 4 b-tags"),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge4t_Pt_5","Jet_Pt[5]",50,30.0,600.0),"Jet_Pt[5]",selection+"&&(N_Jets>=6)","\geq 6 jets, \geq 4 b-tags"),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",50,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Dr_minDrTaggedJets","Evt_Dr_minDrTaggedJets",50,0.35,2.5),"Evt_Dr_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_HT","H_{T}",50,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Evt_Pt_TaggedJetsAverage","Evt_Pt_TaggedJetsAverage",50,30.0,600.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_tHq_log_h_pt","Reco_JABDT_tHq_log_h_pt",50,0.0,7.0),"Reco_JABDT_tHq_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttH_log_h_m","Reco_JABDT_ttH_log_h_m",50,-1.5,6.0),"Reco_JABDT_ttH_log_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt","Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",20,0.0,1.0),"Reco_JABDT_ttH_tophad_pt__P__toplep_pt__P__h_pt__DIV__Evt_HT__P__Evt_Pt_MET__P__Lep_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_tHW_h_pt","Reco_tHW_h_pt",50,-1.5,600.0),"Reco_tHW_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_tHW_hdau_pt1","Reco_tHW_hdau_pt1",50,-1.5,600.0),"Reco_tHW_hdau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_tHq_h_dr","Reco_tHq_h_dr",50,0.0,5.0),"Reco_tHq_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_tHq_h_pt","Reco_tHq_h_pt",50,0.0,600.0),"Reco_tHq_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_tHq_hdau_pt1","Reco_tHq_hdau_pt1",50,30.0,500.0),"Reco_tHq_hdau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_h_pt","Reco_ttH_h_pt",50,-1.5,600.0),"Reco_ttH_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_hdau_pt1","Reco_ttH_hdau_pt1",50,-1.5,500.0),"Reco_ttH_hdau_pt1",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Reco_ttH_hdau_pt2","Reco_ttH_hdau_pt2",50,-1.5,200.0),"Reco_ttH_hdau_pt2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_TaggedJet_M_0","TaggedJet_M[0]",50,0.0,200.0),"TaggedJet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_TaggedJet_Pt_0","TaggedJet_Pt[0]",50,30.0,600.0),"TaggedJet_Pt[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Pt_0","Jet_Pt[0]",50,30.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Pt_1","Jet_Pt[1]",50,30.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Pt_2","Jet_Pt[2]",50,30.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Pt_3","Jet_Pt[3]",50,30.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Pt_4","Jet_Pt[4]",50,30.0,600.0),"Jet_Pt[4]",selection+"&&(N_Jets>=5)","\geq 5 jets, \geq 4 b-tags"),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_3t_Pt_5","Jet_Pt[5]",50,30.0,600.0),"Jet_Pt[5]",selection+"&&(N_Jets>=6)","\geq 6 jets, \geq 4 b-tags"),
        
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
    