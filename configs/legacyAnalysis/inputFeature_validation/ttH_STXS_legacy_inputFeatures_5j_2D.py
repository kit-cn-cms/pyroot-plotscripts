
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
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_tHq_h_pt",50,0.0,600.0),"Reco_tHq_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_JABDT_tHq_log_h_pt",50,0.0,7.0),"Reco_JABDT_tHq_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",50,-1.5,6.0),"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_tHW_h_pt",50,-1.5,600.0),"Reco_tHW_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_tHW_h_dr",50,-1.5,4.0),"Reco_tHW_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_tHq_h_dr",50,-1.5,4.0),"Reco_tHq_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_JABDT_tHW_log_h_pt",50,0.0,7.0),"Reco_JABDT_tHW_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_ttH_h_dr",50,-1.5,4.0),"Reco_ttH_h_dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_ttH_h_m",50,0.0,200),"Reco_ttH_h_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_JABDT_ttH_log_h_pt",50,0.0,7.0),"Reco_JABDT_ttH_log_h_pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Reco_JABDT_ttH_log_toplep_m",50,0.0,7.0),"Reco_JABDT_ttH_log_toplep_m",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Evt_Pt_TaggedJetsAverage",50,30.0,600.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","average #DeltaR(tags)",50,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Evt_M_TaggedJetsAverage",50,0.,100),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Evt_Pt_minDrTaggedJets",50,0.0,800.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D(catString+"","Evt_Pt_JetsAverage",50,0.0,800.0),"Evt_Pt_JetsAverage",selection,label),
    ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots

def plotInterfaces(data = None, selection="(N_Jets==5&&N_BTagsM>=4)", label = "5 jets, \geq 4 b-tags", catString = "ljets_5j_ge4t" ):
    catString = catString + "_"
    interfaces = []
    memDBp = vhi.variableHistoInterface(variable_name  = "memDBp", label = catString+"memDBp", selection = selection)
    memDBp.category = (selection, catString+"memDBp","")
    memDBp.category_label = label
    memDBp.histotitle = "memDBp"
    memDBp.histoname = catString+"memDBp"
    memDBp.nhistobins = 20
    memDBp.minxval = 0.
    memDBp.maxxval = 1.0
    interfaces.append(memDBp)

    Reco_tHq_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_tHq_h_pt", label = catString+"Reco_tHq_h_pt", selection      = selection)
    Reco_tHq_h_pt.category = (selection, catString+"Reco_tHq_h_pt","")
    Reco_tHq_h_pt.category_label = label
    Reco_tHq_h_pt.histotitle = "Reco_tHq_h_pt"
    Reco_tHq_h_pt.histoname = catString+"Reco_tHq_h_pt"
    Reco_tHq_h_pt.nhistobins = 20
    Reco_tHq_h_pt.minxval = 0.
    Reco_tHq_h_pt.maxxval = 600.
    interfaces.append(Reco_tHq_h_pt)

    Reco_JABDT_tHq_log_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_log_h_pt", label = catString+"Reco_JABDT_tHq_log_h_pt", selection      = selection)
    Reco_JABDT_tHq_log_h_pt.category = (selection, catString+"Reco_JABDT_tHq_log_h_pt","")
    Reco_JABDT_tHq_log_h_pt.category_label = label
    Reco_JABDT_tHq_log_h_pt.histotitle = "Reco_JABDT_tHq_log_h_pt"
    Reco_JABDT_tHq_log_h_pt.histoname = catString+"Reco_JABDT_tHq_log_h_pt"
    Reco_JABDT_tHq_log_h_pt.nhistobins = 20
    Reco_JABDT_tHq_log_h_pt.minxval = 0.
    Reco_JABDT_tHq_log_h_pt.maxxval = 7.
    interfaces.append(Reco_JABDT_tHq_log_h_pt)

    Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt", label = catString+"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt", selection      = selection)
    Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.category = (selection, catString+"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt","")
    Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.category_label = label
    Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.histotitle = "Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt"
    Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.histoname = catString+"Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt"
    Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.nhistobins = 20
    Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.minxval = -1.5
    Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt.maxxval = 6.
    interfaces.append(Reco_JABDT_tHq_log_min_hdau1_pt_hdau2_pt)

    Reco_tHW_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_tHW_h_pt", label = catString+"Reco_tHW_h_pt", selection      = selection)
    Reco_tHW_h_pt.category = (selection, catString+"Reco_tHW_h_pt","")
    Reco_tHW_h_pt.category_label = label
    Reco_tHW_h_pt.histotitle = "Reco_tHW_h_pt"
    Reco_tHW_h_pt.histoname = catString+"Reco_tHW_h_pt"
    Reco_tHW_h_pt.nhistobins = 20
    Reco_tHW_h_pt.minxval = -1.5
    Reco_tHW_h_pt.maxxval = 600.
    interfaces.append(Reco_tHW_h_pt)

    Reco_tHW_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHW_h_dr", label = catString+"Reco_tHW_h_dr", selection      = selection)
    Reco_tHW_h_dr.category = (selection, catString+"Reco_tHW_h_dr","")
    Reco_tHW_h_dr.category_label = label
    Reco_tHW_h_dr.histotitle = "Reco_tHW_h_dr"
    Reco_tHW_h_dr.histoname = catString+"Reco_tHW_h_dr"
    Reco_tHW_h_dr.nhistobins = 20
    Reco_tHW_h_dr.minxval = -1.5
    Reco_tHW_h_dr.maxxval = 4.
    interfaces.append(Reco_tHW_h_dr)

    Reco_tHq_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_tHq_h_dr", label = catString+"Reco_tHq_h_dr", selection      = selection)
    Reco_tHq_h_dr.category = (selection, catString+"Reco_tHq_h_dr","")
    Reco_tHq_h_dr.category_label = label
    Reco_tHq_h_dr.histotitle = "Reco_tHq_h_dr"
    Reco_tHq_h_dr.histoname = catString+"Reco_tHq_h_dr"
    Reco_tHq_h_dr.nhistobins = 20
    Reco_tHq_h_dr.minxval = -1.5
    Reco_tHq_h_dr.maxxval = 4.
    interfaces.append(Reco_tHq_h_dr)

    Reco_JABDT_tHW_log_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_tHW_log_h_pt", label = catString+"Reco_JABDT_tHW_log_h_pt", selection      = selection)
    Reco_JABDT_tHW_log_h_pt.category = (selection, catString+"Reco_JABDT_tHW_log_h_pt","")
    Reco_JABDT_tHW_log_h_pt.category_label = label
    Reco_JABDT_tHW_log_h_pt.histotitle = "Reco_JABDT_tHW_log_h_pt"
    Reco_JABDT_tHW_log_h_pt.histoname = catString+"Reco_JABDT_tHW_log_h_pt"
    Reco_JABDT_tHW_log_h_pt.nhistobins = 20
    Reco_JABDT_tHW_log_h_pt.minxval = 0.
    Reco_JABDT_tHW_log_h_pt.maxxval = 7.
    interfaces.append(Reco_JABDT_tHW_log_h_pt)

    Reco_ttH_h_dr = vhi.variableHistoInterface(variable_name  = "Reco_ttH_h_dr", label = catString+"Reco_ttH_h_dr", selection      = selection)
    Reco_ttH_h_dr.category = (selection, catString+"Reco_ttH_h_dr","")
    Reco_ttH_h_dr.category_label = label
    Reco_ttH_h_dr.histotitle = "Reco_ttH_h_dr"
    Reco_ttH_h_dr.histoname = catString+"Reco_ttH_h_dr"
    Reco_ttH_h_dr.nhistobins = 20
    Reco_ttH_h_dr.minxval = -1.5
    Reco_ttH_h_dr.maxxval = 4.
    interfaces.append(Reco_ttH_h_dr)

    Reco_ttH_h_m = vhi.variableHistoInterface(variable_name  = "Reco_ttH_h_m", label = catString+"Reco_ttH_h_m", selection      = selection)
    Reco_ttH_h_m.category = (selection, catString+"Reco_ttH_h_m","")
    Reco_ttH_h_m.category_label = label
    Reco_ttH_h_m.histotitle = "Reco_ttH_h_m"
    Reco_ttH_h_m.histoname = catString+"Reco_ttH_h_m"
    Reco_ttH_h_m.nhistobins = 20
    Reco_ttH_h_m.minxval = 0.
    Reco_ttH_h_m.maxxval = 200.
    interfaces.append(Reco_ttH_h_m)

    Reco_JABDT_ttH_log_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_log_h_pt", label = catString+"Reco_JABDT_ttH_log_h_pt", selection      = selection)
    Reco_JABDT_ttH_log_h_pt.category = (selection, catString+"Reco_JABDT_ttH_log_h_pt","")
    Reco_JABDT_ttH_log_h_pt.category_label = label
    Reco_JABDT_ttH_log_h_pt.histotitle = "Reco_JABDT_ttH_log_h_pt"
    Reco_JABDT_ttH_log_h_pt.histoname = catString+"Reco_JABDT_ttH_log_h_pt"
    Reco_JABDT_ttH_log_h_pt.nhistobins = 20
    Reco_JABDT_ttH_log_h_pt.minxval = 0.
    Reco_JABDT_ttH_log_h_pt.maxxval = 7.
    interfaces.append(Reco_JABDT_ttH_log_h_pt)

    Reco_JABDT_ttH_log_toplep_m = vhi.variableHistoInterface(variable_name  = "Reco_JABDT_ttH_log_toplep_m", label = catString+"Reco_JABDT_ttH_log_toplep_m", selection      = selection)
    Reco_JABDT_ttH_log_toplep_m.category = (selection, catString+"Reco_JABDT_ttH_log_toplep_m","")
    Reco_JABDT_ttH_log_toplep_m.category_label = label
    Reco_JABDT_ttH_log_toplep_m.histotitle = "Reco_JABDT_ttH_log_toplep_m"
    Reco_JABDT_ttH_log_toplep_m.histoname = catString+"Reco_JABDT_ttH_log_toplep_m"
    Reco_JABDT_ttH_log_toplep_m.nhistobins = 20
    Reco_JABDT_ttH_log_toplep_m.minxval = 0.
    Reco_JABDT_ttH_log_toplep_m.maxxval = 7.
    interfaces.append(Reco_JABDT_ttH_log_toplep_m)

    Evt_Pt_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_TaggedJetsAverage", label = catString+"Evt_Pt_TaggedJetsAverage", selection      = selection)
    Evt_Pt_TaggedJetsAverage.category = (selection, catString+"Evt_Pt_TaggedJetsAverage","")
    Evt_Pt_TaggedJetsAverage.category_label = label
    Evt_Pt_TaggedJetsAverage.histotitle = "Evt_Pt_TaggedJetsAverage"
    Evt_Pt_TaggedJetsAverage.histoname = catString+"Evt_Pt_TaggedJetsAverage"
    Evt_Pt_TaggedJetsAverage.nhistobins = 20
    Evt_Pt_TaggedJetsAverage.minxval = 30.
    Evt_Pt_TaggedJetsAverage.maxxval = 400.
    interfaces.append(Evt_Pt_TaggedJetsAverage)

    Evt_Dr_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Dr_TaggedJetsAverage", label = catString+"Evt_Dr_TaggedJetsAverage", selection      = selection)
    Evt_Dr_TaggedJetsAverage.category = (selection, catString+"Evt_Dr_TaggedJetsAverage","")
    Evt_Dr_TaggedJetsAverage.category_label = label
    Evt_Dr_TaggedJetsAverage.histotitle = "Evt_Dr_TaggedJetsAverage"
    Evt_Dr_TaggedJetsAverage.histoname = catString+"Evt_Dr_TaggedJetsAverage"
    Evt_Dr_TaggedJetsAverage.nhistobins = 20
    Evt_Dr_TaggedJetsAverage.minxval = 0.5
    Evt_Dr_TaggedJetsAverage.maxxval = 3.5
    interfaces.append(Evt_Dr_TaggedJetsAverage)

    Evt_M_TaggedJetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_M_TaggedJetsAverage", label = catString+"Evt_M_TaggedJetsAverage", selection      = selection)
    Evt_M_TaggedJetsAverage.category = (selection, catString+"Evt_M_TaggedJetsAverage","")
    Evt_M_TaggedJetsAverage.category_label = label
    Evt_M_TaggedJetsAverage.histotitle = "Evt_M_TaggedJetsAverage"
    Evt_M_TaggedJetsAverage.histoname = catString+"Evt_M_TaggedJetsAverage"
    Evt_M_TaggedJetsAverage.nhistobins = 20
    Evt_M_TaggedJetsAverage.minxval = 0.5
    Evt_M_TaggedJetsAverage.maxxval = 100
    interfaces.append(Evt_M_TaggedJetsAverage)

    Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets", label = catString+"Evt_Pt_minDrTaggedJets", selection      = selection)
    Evt_Pt_minDrTaggedJets.category = (selection, catString+"Evt_Pt_minDrTaggedJets","")
    Evt_Pt_minDrTaggedJets.category_label = label
    Evt_Pt_minDrTaggedJets.histotitle = "Evt_Pt_minDrTaggedJets"
    Evt_Pt_minDrTaggedJets.histoname = catString+"Evt_Pt_minDrTaggedJets"
    Evt_Pt_minDrTaggedJets.nhistobins = 20
    Evt_Pt_minDrTaggedJets.minxval = 0.5
    Evt_Pt_minDrTaggedJets.maxxval = 800
    interfaces.append(Evt_Pt_minDrTaggedJets)

    Evt_Pt_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Pt_JetsAverage", label = catString+"Evt_Pt_JetsAverage", selection      = selection)
    Evt_Pt_JetsAverage.category = (selection, catString+"Evt_Pt_JetsAverage","")
    Evt_Pt_JetsAverage.category_label = label
    Evt_Pt_JetsAverage.histotitle = "Evt_Pt_JetsAverage"
    Evt_Pt_JetsAverage.histoname = catString+"Evt_Pt_JetsAverage"
    Evt_Pt_JetsAverage.nhistobins = 20
    Evt_Pt_JetsAverage.minxval = 0.
    Evt_Pt_JetsAverage.maxxval = 400
    interfaces.append(Evt_Pt_JetsAverage)

    return interfaces


def plots_STXS_ljets_5j_ge4t(data = None):
    interfaces = plotInterfaces(data = data, selection="(N_Jets==5&&N_BTagsM>=4)", label = "5 jets, \geq 4 b-tags", catString = "ljets_5j_ge4t" )
    for i in interfaces:
        i.category_label = "5 jets, \geq 4 b-tags"
    plots = init_plots_2D(interfaces = interfaces)
    if data:
        add_data_plots(plots = plots, data = data)
    return plots

def plots_STXS_ljets_ge6j_ge4t(data = None):
    interfaces = plotInterfaces(data = data, selection="(N_Jets>=6&&N_BTagsM>=4)", label = "\geq 6 jets, \geq 4 b-tags", catString = "ljets_ge6j_ge4t" )
    for i in interfaces:
        i.category_label = "\geq 6 jets, \geq 4 b-tags"
    plots = init_plots_2D(interfaces = interfaces)
    if data:
        add_data_plots(plots = plots, data = data)
    return plots

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_STXS_ljets_5j_ge4t(data)
    discriminatorPlots += plots_STXS_ljets_ge6j_ge4t(data)

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
            maxxval  = interf.maxxval
            minxval  = interf.minxval
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,minxval, maxxval),
                    interf.varname,interf.selection,interf.category_label))
        else:
            print("FATAL ERROR: Unable to load bin edges or min/max values for histogram!")
            print(interf)
            raise ValueError
        dictionary[interf.label] = interf.getDictionary()

    if not data is None:
        data.categories.update(dictionary)

    return plots


def create_plot_2D(interf, interf2):
    binsX = None
    nbinsX = None
    minxval = None
    maxxval = None
    binsY = None
    nbinsY = None
    ymin = None
    ymax = None
    plot = None
    
    # check if initialization uses bin edges or min/max vals
    # if 'subdict' contains the keyword 'bin_edges', an array
    # of type float is created from the corresponding python list.
    # Else, the min/maxvals are used 
    if not interf.bin_edges is None:
        binsX  = array("f", interf.bin_edges)
        nbinsX = len(binsX)-1 # last bin edge in array is overflow bin => subtract for nbins
        interf.nhistobins = nbinsX # update number of bins

    elif not (interf.minxval is None or interf.maxxval is None):
        nbinsX = interf.nhistobins
        maxxval  = interf.maxxval
        minxval  = interf.minxval
    
    if not interf2.bin_edges is None:
        binsY  = array("f", interf2.bin_edges)
        nbinsY = len(binsY)-1 # last bin edge in array is overflow bin => subtract for nbins
        interf2.nhistobins = nbinsY # update number of bins
    elif not (interf2.minxval is None or interf2.maxxval is None):
        nbinsY = interf2.nhistobins
        ymax  = interf2.maxxval
        ymin  = interf2.minxval

    hname_2D = "{}_{}".format(interf.histoname, interf2.histoname)
    htitle_2D = "{}_{}".format(interf.histotitle, interf2.histotitle)
    if not binsX is None:
        if not binsY is None:
            plot = plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,binsX, nbinsY,binsY),
                        variable1 = interf.varname,
                        variable2 = interf2.varname,
                        selection = interf.selection,
                        label = interf.category_label)
        else: 
            plot = plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,binsX, nbinsY,ymin, ymax),
                        variable1 = interf.varname,
                        variable2 = interf2.varname,
                        selection = interf.selection,
                        label = interf.category_label)
    elif not (minxval is None or maxxval is None):
        if not binsY is None:
            plot = plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,minxval, maxxval, nbinsY,binsY),
                        variable1 = interf.varname,
                        variable2 = interf2.varname,
                        selection = interf.selection,
                        label = interf.category_label)
        else: 
            plot = plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,minxval, maxxval, nbinsY,ymin, ymax),
                        variable1 = interf.varname,
                        variable2 = interf2.varname,
                        selection = interf.selection,
                        label = interf.category_label)
    else:
        s = "FATAL ERROR: Unable to load bin edges or min/max values for histogram!\n"
        s += "interface 1:\n{}".format(interf)
        s += "interface 2:\n{}".format(interf2)
        raise ValueError(s)
    return plot

def init_plots_2D(interfaces, filter_for = None):
    plots = [] #init list of plotClasses objects to return
    dictionary = {}
    if filter_for:
        current_interfaces = [x for x in interfaces \
                                if x.histotitle == filter_for]
        for interf in current_interfaces:
            for interf2 in interfaces:
                if interf2 in current_interfaces:
                    print("skipping {}".format(interf2.histotitle))
                    continue
                # print("doing {} vs {}".format(interf.histotitle, interf2.histotitle))
                plots.append(create_plot_2D(interf, interf2))
    else:
        for i, interf in enumerate(interfaces):
            for interf2 in interfaces[i+1:]:
                plots.append(create_plot_2D(interf, interf2))
    # exit(0)
    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    