
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


def plots_dnn_vs_inputs_ge4j_3t(data, discrname):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    interf_ljets_ge4j_3t_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_3t_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_N_Jets.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_N_Jets","")
    interf_ljets_ge4j_3t_N_Jets.bin_edges = [ 
                3.5,
                4.5,
                5.5,
                6.5,
                7.5,
                8.5,
                9.5,
                10.5
                ]
    interf_ljets_ge4j_3t_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge4j_3t_N_Jets.histoname = "ljets_ge4j_3t_N_Jets"
    interf_ljets_ge4j_3t_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge4j_3t_N_Jets)

    interf_ljets_ge4j_3t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_3t_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_CSV_avg","")
    interf_ljets_ge4j_3t_Evt_CSV_avg.bin_edges = [ 
                0.15,
                0.167,
                0.184,
                0.201,
                0.218,
                0.235,
                0.252,
                0.269,
                0.286,
                0.303,
                0.32,
                0.337,
                0.354,
                0.371,
                0.388,
                0.405,
                0.422,
                0.439,
                0.456,
                0.473,
                0.49,
                0.507,
                0.524,
                0.541,
                0.558,
                0.575,
                0.592,
                0.609,
                0.626,
                0.643,
                0.66,
                0.677,
                0.694,
                0.711,
                0.728,
                0.745,
                0.762,
                0.779,
                # 1.0
                ]
    interf_ljets_ge4j_3t_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge4j_3t_Evt_CSV_avg.histoname = "ljets_ge4j_3t_Evt_CSV_avg"
    interf_ljets_ge4j_3t_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_CSV_avg)

    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage = vhi.variableHistoInterface(variable_name  = "Evt_Deta_JetsAverage",
                                            label          = "ljets_ge4j_3t_Evt_Deta_JetsAverage",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Evt_Deta_JetsAverage","")
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.bin_edges = [ 
                0.0,
                0.12,
                0.18,
                0.24,
                0.3,
                0.36,
                0.42,
                0.48,
                0.54,
                0.6,
                0.66,
                0.72,
                0.78,
                0.84,
                0.9,
                0.96,
                1.02,
                1.08,
                1.14,
                1.2,
                1.26,
                1.32,
                1.38,
                1.44,
                1.5,
                1.56,
                1.62,
                1.68,
                1.74,
                1.8,
                1.86,
                1.92,
                1.98,
                2.04,
                2.1,
                2.16,
                2.22,
                2.28,
                2.34,
                2.4,
                2.46,
                2.52,
                2.58,
                2.64,
                2.7,
                3.0
                ]
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.histotitle = "Evt_Deta_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.histoname = "ljets_ge4j_3t_Evt_Deta_JetsAverage"
    interf_ljets_ge4j_3t_Evt_Deta_JetsAverage.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Evt_Deta_JetsAverage)

    interf_ljets_ge4j_3t_Reco_ttbar_whad_m = vhi.variableHistoInterface(variable_name  = "Reco_ttbar_whad_m",
                                            label          = "ljets_ge4j_3t_Reco_ttbar_whad_m",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_Reco_ttbar_whad_m","")
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.bin_edges = [ 
                0.0,
                40.0,
                80.0,
                120.0,
                160.0,
                200.0,
                240.0,
                280.0,
                320.0,
                360.0,
                400.0,
                440.0,
                480.0,
                520.0,
                560.0,
                600.0,
                640.0,
                680.0,
                720.0,
                760.0,
                800.0,
                840.0,
                880.0,
                920.0,
                960.0,
                1000.0,
                1040.0,
                1080.0,
                1120.0,
                1200.0,
                1280.0,
                1360.0,
                1440.0,
                1560.0,
                1720.0,
                1960.0,
                2000.0
                ]
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.histotitle = "Reco_ttbar_whad_m"
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.histoname = "ljets_ge4j_3t_Reco_ttbar_whad_m"
    interf_ljets_ge4j_3t_Reco_ttbar_whad_m.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_3t_Reco_ttbar_whad_m)

    interf_ljets_ge4j_3t_DNNPred = vhi.variableHistoInterface(variable_name  = "DNNPredictedClass_ge4j_3t_classifier",
                                            label          = "ljets_ge4j_3t_DNNPred",
                                            selection      = "(N_Jets>=4&&N_BTagsM==3)&&(1.)")
    interf_ljets_ge4j_3t_DNNPred.category = ("(N_Jets>=4&&N_BTagsM==3)&&(1.)","ljets_ge4j_3t_DNNPred","")
    interf_ljets_ge4j_3t_DNNPred.bin_edges = [-0.5,  0.5,  1.5,  2.5,  3.5,  4.5,  5.5,  6.5]
    interf_ljets_ge4j_3t_DNNPred.nhistobins = 7
    interf_ljets_ge4j_3t_DNNPred.histotitle = "DNNPred"
    interf_ljets_ge4j_3t_DNNPred.histoname = "ljets_ge4j_3t_DNNPred"

    plots = [build_2D_plot(interf = i, interf2 = interf_ljets_ge4j_3t_DNNPred)\
                for i in interfaces]

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_dnn_vs_inputs_ge4j_ge4t(data, discrname):
    label = "\geq 4 jets, 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    interf_ljets_ge4j_ge4t_N_Jets = vhi.variableHistoInterface(variable_name  = "N_Jets",
                                            label          = "ljets_ge4j_ge4t_N_Jets",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_N_Jets.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_N_Jets","")
    interf_ljets_ge4j_ge4t_N_Jets.bin_edges = [ 
                3.5,
                4.5,
                5.5,
                6.5,
                7.5,
                8.5,
                9.5,
                10.5
                ]
    interf_ljets_ge4j_ge4t_N_Jets.histotitle = "N_Jets"
    interf_ljets_ge4j_ge4t_N_Jets.histoname = "ljets_ge4j_ge4t_N_Jets"
    interf_ljets_ge4j_ge4t_N_Jets.nhistobins = 7
    interfaces.append(interf_ljets_ge4j_ge4t_N_Jets)

    interf_ljets_ge4j_ge4t_Evt_CSV_avg = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg",
                                            label          = "ljets_ge4j_ge4t_Evt_CSV_avg",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_CSV_avg","")
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.bin_edges = [ 
                # 0.15,
                0.252,
                0.269,
                0.286,
                0.303,
                0.32,
                0.337,
                0.354,
                0.371,
                0.388,
                0.405,
                0.422,
                0.439,
                0.456,
                0.473,
                0.49,
                0.507,
                0.524,
                0.541,
                0.558,
                0.575,
                0.592,
                0.609,
                0.626,
                0.643,
                0.66,
                0.677,
                0.694,
                0.711,
                0.728,
                0.745,
                0.762,
                0.779,
                0.796,
                0.813,
                0.83,
                0.847,
                0.898,
                1.0
                ]
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.histotitle = "Evt_CSV_avg"
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.histoname = "ljets_ge4j_ge4t_Evt_CSV_avg"
    interf_ljets_ge4j_ge4t_Evt_CSV_avg.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_CSV_avg)

    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged = vhi.variableHistoInterface(variable_name  = "Evt_CSV_avg_tagged",
                                            label          = "ljets_ge4j_ge4t_Evt_CSV_avg_tagged",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ljets_ge4j_ge4t_Evt_CSV_avg_tagged","")
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.bin_edges = [ 
                # 0.3,
                0.412,
                0.44,
                0.454,
                0.468,
                0.482,
                0.496,
                0.51,
                0.524,
                0.538,
                0.552,
                0.566,
                0.58,
                0.594,
                0.608,
                0.622,
                0.636,
                0.65,
                0.664,
                0.678,
                0.692,
                0.706,
                0.72,
                0.734,
                0.748,
                0.762,
                0.776,
                0.79,
                0.804,
                0.818,
                0.832,
                0.846,
                0.86,
                0.874,
                0.888,
                0.902,
                0.916,
                0.944,
                0.972,
                1.0
                ]
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.histotitle = "Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.histoname = "ljets_ge4j_ge4t_Evt_CSV_avg_tagged"
    interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged.nhistobins = 50
    interfaces.append(interf_ljets_ge4j_ge4t_Evt_CSV_avg_tagged)

    interf_ljets_ge4j_ge4t_memDBp = vhi.variableHistoInterface(variable_name  = memexp,
                                            label          = "ljets_ge4j_ge4t_memDBp",
                                            selection      = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)")
    interf_ljets_ge4j_ge4t_memDBp.category = ("(N_Jets>=4&&N_BTagsM>=4)&&(1.)","ge4j_ge4t_memDBp","")
    interf_ljets_ge4j_ge4t_memDBp.category_label = label
    interf_ljets_ge4j_ge4t_memDBp.bin_edges = [ 
                0.0,
                0.0333,
                0.0667,
                0.1,
                0.1333,
                0.1667,
                0.2,
                0.2333,
                0.2667,
                0.3,
                0.3333,
                0.3667,
                0.4,
                0.4333,
                0.4667,
                0.5,
                0.5333,
                0.5667,
                0.6,
                0.6333,
                0.6667,
                0.7,
                0.7333,
                0.7667,
                0.8,
                0.8333,
                0.8667,
                0.9,
                0.9333,
                0.9667,
                1.0
                ]
    interf_ljets_ge4j_ge4t_memDBp.histotitle = "MEM"
    interf_ljets_ge4j_ge4t_memDBp.histoname = "ljets_ge4j_ge4t_memDBp"
    interf_ljets_ge4j_ge4t_memDBp.nhistobins = 30
    interfaces.append(interf_ljets_ge4j_ge4t_memDBp)

    interf_ljets_ge4j_ge4t_DNNPred = vhi.variableHistoInterface(variable_name  = "DNNPredictedClass_ge4j_ge4t_classifier",
                                            label          = "ljets_ge4j_ge4t_DNNPred",
                                            selection      = selection)
    interf_ljets_ge4j_ge4t_DNNPred.category = (selection,"ljets_ge4j_ge4t_DNNPred","")
    interf_ljets_ge4j_ge4t_DNNPred.bin_edges = [-0.5,  0.5,  1.5,  2.5,  3.5,  4.5,  5.5,  6.5]
    interf_ljets_ge4j_ge4t_DNNPred.nhistobins = 7
    interf_ljets_ge4j_ge4t_DNNPred.histotitle = "DNNPred"
    interf_ljets_ge4j_ge4t_DNNPred.histoname = "ljets_ge4j_ge4t_DNNPred"

    plots = [build_2D_plot(interf = i, interf2 = interf_ljets_ge4j_ge4t_DNNPred)\
                for i in interfaces]

    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    # discriminatorPlots += plots_ge4j_ge4t_classifier(data)
    # discriminatorPlots += plots_ge4j_ge4t_STXS(data)
    # discriminatorPlots += plots_ge4j_3t_classifier(data)
    # discriminatorPlots += plots_ge4j_3t_STXS(data)

    # discriminatorPlots += plots_dnn(data, discrname)
    discriminatorPlots += plots_dnn_vs_inputs_ge4j_3t(data, discrname)
    discriminatorPlots += plots_dnn_vs_inputs_ge4j_ge4t(data, discrname)

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

def build_2D_plot(interf, interf2):
    plot = None
    binsX = None
    nbinsX = None
    xmin = None
    xmax = None
    binsY = None
    nbinsY = None
    ymin = None
    ymax = None
    
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
        xmax  = interf.maxxval
        xmin  = interf.minxval
    
    if not interf2.bin_edges is None:
        binsY  = array("f", interf2.bin_edges)
        nbinsY = len(binsY)-1 # last bin edge in array is overflow bin => subtract for nbins
        interf2.nhistobins = nbinsY # update number of bins
    elif not (interf2.minxval is None or interf2.maxxval is None):
        nbinsY = interf2.nhistobins
        ymax  = interf2.maxxval
        ymin  = interf2.minxval

    hname_2D = "{}_vs_{}".format(interf.histoname, interf2.histoname)
    htitle_2D = "{}_vs_{}".format(interf.histotitle, interf2.histotitle)
    if not binsX is None:
        if not binsY is None:
            plot = plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,binsX, nbinsY,binsY),
                        variable1 = interf.varname,
                        variable2 = interf2.varname,
                        selection = interf.selection,
                        label = interf.category_label)
        else: 
            print(nbinsX)
            print(binsX)
            print(nbinsY)
            print(ymin)
            print(ymax)
            plot = plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,binsX, nbinsY,ymin, ymax),
                        variable1 = interf.varname,
                        variable2 = interf2.varname,
                        selection = interf.selection,
                        label = interf.category_label)
    elif not (xmin is None or xmax is None):
        if not binsY is None:
            plot = plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,xmin, xmax, nbinsY,binsY),
                        variable1 = interf.varname,
                        variable2 = interf2.varname,
                        selection = interf.selection,
                        label = interf.category_label)
        else: 
            plot = plotClasses.TwoDimPlot( histo = ROOT.TH2F(hname_2D,htitle_2D,nbinsX,xmin, xmax, nbinsY,ymin, ymax),
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

def init_plots_2D(interfaces):
    plots = [] #init list of plotClasses objects to return
    dictionary = {}
    for i, interf in enumerate(interfaces):
        for interf2 in interfaces[i+1:]:
            plot = build_2D_plot(interf, interf2)
            plots.append(plot)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
