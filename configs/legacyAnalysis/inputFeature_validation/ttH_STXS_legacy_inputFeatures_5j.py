
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


memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'



def plots(data = None, selection="(N_Jets==5&&N_BTagsM>=4)", label = "5 jets, \geq 4 b-tags", catString = "ljets_5j_ge4t" ):
    label = label
    interfaces = []
    selection = selection
    catString = catString + "_"
    plots = [
        plotClasses.Plot(ROOT.TH1D(catString+"memDBp","MEM",50,0.,1.0),memexp,selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_tHq_h_pt","Reco_tHq_h_pt",50,0.0,600.0),"Reco_tHq_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_JABDT_tHq_log_h_pt","Reco_JABDT_tHq_log_h_pt",50,0.0,7.0),"Reco_JABDT_tHq_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",50,-1.5,6.0),"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_tHW_h_pt","Reco_tHW_h_pt",50,-1.5,600.0),"Reco_tHW_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_tHW_h_dr","Reco_tHW_h_dr",50,-1.5,4.0),"Reco_tHW_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_tHq_h_dr","Reco_tHq_h_dr",50,-1.5,4.0),"Reco_tHq_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_JABDT_tHW_log_h_pt","Reco_JABDT_tHW_log_h_pt",50,0.0,7.0),"Reco_JABDT_tHW_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_ttH_h_dr","Reco_ttH_h_dr",50,-1.5,4.0),"Reco_ttH_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_ttH_h_m","Reco_ttH_h_m",50,0.0,200),"Reco_ttH_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_JABDT_ttH_log_h_pt","Reco_JABDT_ttH_log_h_pt",50,0.0,7.0),"Reco_JABDT_ttH_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Reco_JABDT_ttH_log_toplep_m","Reco_JABDT_ttH_log_toplep_m",50,0.0,7.0),"Reco_JABDT_ttH_log_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Evt_Pt_TaggedJetsAverage","Evt_Pt_TaggedJetsAverage",50,30.0,600.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",50,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",50,0.,100),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Evt_Pt_minDrTaggedJets","Evt_Pt_minDrTaggedJets",50,0.0,800.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"Evt_Pt_JetsAverage","Evt_Pt_JetsAverage",50,0.0,800.0),"Evt_Pt_JetsAverage",selection,label),
    ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots(data = data, selection="(N_Jets==5&&N_BTagsM>=4)", label = "5 jets, \geq 4 b-tags", catString = "ljets_5j_ge4t" )
    discriminatorPlots += plots(data = data, selection="(N_Jets>=6&&N_BTagsM>=4)", label = "\geq 6 jets, \geq 4 b-tags", catString = "ljets_ge6j_ge4t" )

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
    