
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



def plots_ljets_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"


    interf_ljets_ge4j_ge4t_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            label          = "ljets_ge4j_ge4t_Evt_HT_jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_HT_jets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_HT_jets","")
    interf_ljets_ge4j_ge4t_Evt_HT_jets.category_label = label
    interf_ljets_ge4j_ge4t_Evt_HT_jets.bin_edges = [ 
                150.0,
                187.0,
                224.0,
                261.0,
                298.0,
                335.0,
                372.0,
                409.0,
                446.0,
                483.0,
                520.0,
                557.0,
                594.0,
                631.0,
                668.0,
                705.0,
                742.0,
                779.0,
                816.0,
                853.0,
                890.0,
                927.0,
                964.0,
                1001.0,
                1038.0,
                1075.0,
                1112.0,
                1186.0,
                1260.0,
                1334.0,
                1445.0,
                1556.0,
                1778.0,
                2000.0
                ]
    interf_ljets_ge4j_ge4t_Evt_HT_jets.histotitle = "H_{T} (jets)"
    interf_ljets_ge4j_ge4t_Evt_HT_jets.histoname = "ljets_ge4j_ge4t_Evt_HT_jets"
    interf_ljets_ge4j_ge4t_Evt_HT_jets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_HT_jets)
    
    interf_ljets_ge4j_ge4t_Jet_CSV_0 = vhi.variableHistoInterface(variable_name  = "Jet_CSV[0]",
                                            label          = "ljets_ge4j_ge4t_Jet_CSV_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_CSV_0.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_CSV_0","")
    interf_ljets_ge4j_ge4t_Jet_CSV_0.category_label = label
    interf_ljets_ge4j_ge4t_Jet_CSV_0.bin_edges = [ 
                0.3,
                0.3233,
                0.3467,
                0.37,
                0.3933,
                0.4167,
                0.44,
                0.4633,
                0.4867,
                0.51,
                0.5333,
                0.5567,
                0.58,
                0.6033,
                0.6267,
                0.65,
                0.6733,
                0.6967,
                0.72,
                0.7433,
                0.7667,
                0.79,
                0.8133,
                0.8367,
                0.86,
                0.8833,
                0.9067,
                0.93,
                0.9533,
                0.9767,
                1.0
                ]
    interf_ljets_ge4j_ge4t_Jet_CSV_0.histotitle = "Jet CSV[0]"
    interf_ljets_ge4j_ge4t_Jet_CSV_0.histoname = "ljets_ge4j_ge4t_Jet_CSV_0"
    interf_ljets_ge4j_ge4t_Jet_CSV_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_CSV_0)
    
    interf_ljets_ge4j_ge4t_Jet_Pt_0 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[0]",
                                            label          = "ljets_ge4j_ge4t_Jet_Pt_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Jet_Pt_0.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Jet_Pt_0","")
    interf_ljets_ge4j_ge4t_Jet_Pt_0.category_label = label
    interf_ljets_ge4j_ge4t_Jet_Pt_0.bin_edges = [ 
                36.0,
                52.0,
                68.0,
                84.0,
                100.0,
                116.0,
                132.0,
                148.0,
                164.0,
                180.0,
                196.0,
                212.0,
                228.0,
                244.0,
                260.0,
                276.0,
                292.0,
                308.0,
                324.0,
                340.0,
                356.0,
                372.0,
                388.0,
                404.0,
                420.0,
                436.0,
                452.0,
                484.0,
                500.0
                ]
    interf_ljets_ge4j_ge4t_Jet_Pt_0.histotitle = "hardest jet p_{T}"
    interf_ljets_ge4j_ge4t_Jet_Pt_0.histoname = "ljets_ge4j_ge4t_Jet_Pt_0"
    interf_ljets_ge4j_ge4t_Jet_Pt_0.nhistobins = 30
    interfaces.append(interf_ljets_ge4j_ge4t_Jet_Pt_0)

    interf_ljets_ge4j_ge4t_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_ge4t_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_N_Jets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_N_Jets","")
    interf_ljets_ge4j_ge4t_N_Jets.category_label = label
    interf_ljets_ge4j_ge4t_N_Jets.minxval = -0.5
    interf_ljets_ge4j_ge4t_N_Jets.maxxval = 9.5

    interf_ljets_ge4j_ge4t_N_Jets.histotitle = "N(Jets)"
    interf_ljets_ge4j_ge4t_N_Jets.histoname = "ljets_ge4j_ge4t_N_Jets"
    interf_ljets_ge4j_ge4t_N_Jets.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_ge4t_N_Jets)

    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets",
                                            selection      = selection)
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.category = (selection,"ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.bin_edges = [ 
                36.0,
                52.0,
                68.0,
                84.0,
                100.0,
                116.0,
                132.0,
                148.0,
                164.0,
                180.0,
                196.0,
                212.0,
                228.0,
                244.0,
                260.0,
                276.0,
                292.0,
                308.0,
                324.0,
                340.0,
                356.0,
                372.0,
                388.0,
                404.0,
                420.0,
                436.0,
                452.0,
                468.0,
                484.0,
                500.0
                ]
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.histotitle = "p_{T}^{tagged} (min #Delta R)"
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets.nhistobins = 30
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Pt_minDrTaggedJets)

    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_ttH_h_pt",
                                            label          = "ljets_ge4j_ge4t_Reco_ttH_h_pt",
                                            selection      = selection)
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.category = (selection,"ljets_ge4j_ge4t_Reco_ttH_h_pt","")
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.category_label = label
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.bin_edges = [ 
                36.0,
                52.0,
                68.0,
                84.0,
                100.0,
                116.0,
                132.0,
                148.0,
                164.0,
                180.0,
                196.0,
                212.0,
                228.0,
                244.0,
                260.0,
                276.0,
                292.0,
                308.0,
                324.0,
                340.0,
                356.0,
                372.0,
                388.0,
                404.0,
                420.0,
                436.0,
                452.0,
                468.0,
                484.0,
                500.0
                ]
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.histotitle = "p_{T}^{H} (ttH Reco)"
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.histoname = "ljets_ge4j_ge4t_Reco_ttH_h_pt"
    interf_ljets_ge4j_ge4t_Reco_ttH_h_pt.nhistobins = 30
    interfaces.append(interf_ljets_ge4j_ge4t_Reco_ttH_h_pt)

    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Dr_minDrTaggedJets",
                                            label          = "ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets",
                                            selection      = selection)
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.category = (selection,"ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets","")
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.minxval = 0
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.maxxval = 4

    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.histotitle = "#Delta R_{bb}^{min}"
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.histoname = "ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets"
    interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets.nhistobins = 40
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_Dr_minDrTaggedJets)
    
    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_ljets_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    interf_ljets_ge4j_3t_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_3t_N_Jets",
                                            selection      = selection)
    interf_ljets_ge4j_3t_N_Jets.category = (selection,"ljets_ge4j_3t_N_Jets","")
    interf_ljets_ge4j_3t_N_Jets.category_label = label
    interf_ljets_ge4j_3t_N_Jets.minxval = -0.5
    interf_ljets_ge4j_3t_N_Jets.maxxval = 9.5

    interf_ljets_ge4j_3t_N_Jets.histotitle = "N(Jets)"
    interf_ljets_ge4j_3t_N_Jets.histoname = "ljets_ge4j_3t_N_Jets"
    interf_ljets_ge4j_3t_N_Jets.nhistobins = 10
    interfaces.append(interf_ljets_ge4j_3t_N_Jets)

    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Dr_minDrTaggedJets",
                                            label          = "ljets_ge4j_3t_Evt_Dr_minDrTaggedJets",
                                            selection      = selection)
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.category = (selection,"ljets_ge4j_3t_Evt_Dr_minDrTaggedJets","")
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.minxval = 0
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.maxxval = 4

    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.histotitle = "#Delta R_{bb}^{min}"
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.histoname = "ljets_ge4j_3t_Evt_Dr_minDrTaggedJets"
    interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets.nhistobins = 40
    interfaces.append(interf_ljets_ge4j_3t_Evt_Dr_minDrTaggedJets)

    interf_ljets_ge4j_3t_Evt_HT_jets = vhi.variableHistoInterface(variable_name  = "Evt_HT_jets",
                                            label          = "ljets_ge4j_3t_Evt_HT_jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_HT_jets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_HT_jets","")
    interf_ljets_ge4j_3t_Evt_HT_jets.category_label = label
    interf_ljets_ge4j_3t_Evt_HT_jets.bin_edges = [ 
                150.0,
                187.0,
                224.0,
                261.0,
                298.0,
                335.0,
                372.0,
                409.0,
                446.0,
                483.0,
                520.0,
                557.0,
                594.0,
                631.0,
                668.0,
                705.0,
                742.0,
                779.0,
                816.0,
                853.0,
                890.0,
                927.0,
                964.0,
                1001.0,
                1038.0,
                1075.0,
                1112.0,
                1149.0,
                1186.0,
                1223.0,
                1260.0,
                1297.0,
                1334.0,
                1371.0,
                1408.0,
                1445.0,
                1482.0,
                1519.0,
                1556.0,
                1593.0,
                1630.0,
                1667.0,
                1741.0,
                1815.0,
                1889.0,
                1963.0,
                2000.0
                ]
    interf_ljets_ge4j_3t_Evt_HT_jets.histotitle = "H_{T} (jets)"
    interf_ljets_ge4j_3t_Evt_HT_jets.histoname = "ljets_ge4j_3t_Evt_HT_jets"
    interf_ljets_ge4j_3t_Evt_HT_jets.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_HT_jets)
    
    interf_ljets_ge4j_3t_Jet_CSV_0 = vhi.variableHistoInterface(variable_name  = "Jet_CSV[0]",
                                            label          = "ljets_ge4j_3t_Jet_CSV_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_CSV_0.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_CSV_0","")
    interf_ljets_ge4j_3t_Jet_CSV_0.category_label = label
    interf_ljets_ge4j_3t_Jet_CSV_0.bin_edges = [ 
                0.3,
                0.3233,
                0.3467,
                0.37,
                0.3933,
                0.4167,
                0.44,
                0.4633,
                0.4867,
                0.51,
                0.5333,
                0.5567,
                0.58,
                0.6033,
                0.6267,
                0.65,
                0.6733,
                0.6967,
                0.72,
                0.7433,
                0.7667,
                0.79,
                0.8133,
                0.8367,
                0.86,
                0.8833,
                0.9067,
                0.93,
                0.9533,
                0.9767,
                1.0
                ]
    interf_ljets_ge4j_3t_Jet_CSV_0.histotitle = "Jet CSV[0]"
    interf_ljets_ge4j_3t_Jet_CSV_0.histoname = "ljets_ge4j_3t_Jet_CSV_0"
    interf_ljets_ge4j_3t_Jet_CSV_0.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Jet_CSV_0)
    
    interf_ljets_ge4j_3t_Jet_Pt_0 = vhi.variableHistoInterface(variable_name  = "Jet_Pt[0]",
                                            label          = "ljets_ge4j_3t_Jet_Pt_0",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Jet_Pt_0.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Jet_Pt_0","")
    interf_ljets_ge4j_3t_Jet_Pt_0.category_label = label
    interf_ljets_ge4j_3t_Jet_Pt_0.bin_edges = [ 
                36.0,
                52.0,
                68.0,
                84.0,
                100.0,
                116.0,
                132.0,
                148.0,
                164.0,
                180.0,
                196.0,
                212.0,
                228.0,
                244.0,
                260.0,
                276.0,
                292.0,
                308.0,
                324.0,
                340.0,
                356.0,
                372.0,
                388.0,
                404.0,
                420.0,
                436.0,
                452.0,
                468.0,
                484.0,
                500.0
                ]
    interf_ljets_ge4j_3t_Jet_Pt_0.histotitle = "hardest jet p_{T}"
    interf_ljets_ge4j_3t_Jet_Pt_0.histoname = "ljets_ge4j_3t_Jet_Pt_0"
    interf_ljets_ge4j_3t_Jet_Pt_0.nhistobins = 30
    interfaces.append(interf_ljets_ge4j_3t_Jet_Pt_0)
    
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets = vhi.variableHistoInterface(variable_name  = "Evt_Pt_minDrTaggedJets",
                                            label          = "ljets_ge4j_3t_Evt_Pt_minDrTaggedJets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Pt_minDrTaggedJets","")
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.category_label = label
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.bin_edges = [ 
                36.0,
                52.0,
                68.0,
                84.0,
                100.0,
                116.0,
                132.0,
                148.0,
                164.0,
                180.0,
                196.0,
                212.0,
                228.0,
                244.0,
                260.0,
                276.0,
                292.0,
                308.0,
                324.0,
                340.0,
                356.0,
                372.0,
                388.0,
                404.0,
                420.0,
                436.0,
                452.0,
                468.0,
                484.0,
                500.0
                ]
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.histotitle = "p_{T}^{tagged} (min #Delta R)"
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.histoname = "ljets_ge4j_3t_Evt_Pt_minDrTaggedJets"
    interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets.nhistobins = 30
    interfaces.append(interf_ljets_ge4j_3t_Evt_Pt_minDrTaggedJets)

    interf_ljets_ge4j_3t_Reco_ttH_h_pt = vhi.variableHistoInterface(variable_name  = "Reco_ttH_h_pt",
                                            label          = "ljets_ge4j_3t_Reco_ttH_h_pt",
                                            selection      = selection)
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.category = (selection,"ljets_ge4j_3t_Reco_ttH_h_pt","")
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.category_label = label
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.bin_edges = [ 
                36.0,
                52.0,
                68.0,
                84.0,
                100.0,
                116.0,
                132.0,
                148.0,
                164.0,
                180.0,
                196.0,
                212.0,
                228.0,
                244.0,
                260.0,
                276.0,
                292.0,
                308.0,
                324.0,
                340.0,
                356.0,
                372.0,
                388.0,
                404.0,
                420.0,
                436.0,
                452.0,
                468.0,
                484.0,
                500.0
                ]
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.histotitle = "p_{T}^{H} (ttH Reco)"
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.histoname = "ljets_ge4j_3t_Reco_ttH_h_pt"
    interf_ljets_ge4j_3t_Reco_ttH_h_pt.nhistobins = 30
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttH_h_pt)

    plots = init_plots(interfaces = interfaces)    
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ljets_ge4j_ge4t(data)
    discriminatorPlots += plots_ljets_ge4j_3t(data)

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
    