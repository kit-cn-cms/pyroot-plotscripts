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
        (
            "(N_LooseMuons==0 && N_LooseElectrons==0 && N_LoosePhotons==0)",
            "Puppi MET > 250, AK15 Jet Pt > 250, lepton veto",
            "",
        )
    ]


def control_plots(data=None):
    label = "Puppi MET > 250, AK15 Jet Pt > 250, lepton veto"
    selection = "(N_LooseMuons==0 && N_LooseElectrons==0 && N_LoosePhotons==0)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET", "Puppi MET", 32, 200.0, 1000.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt", "AK15 Jet p_{t}", 32, 200.0, 1000.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD", "AK15 Jet DeepAK15 TvsQCD", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_Njettiness_tau3_AK15Jet_Njettiness_tau2",
                "AK15 Jet #tau_{3}/#tau_{2}",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_Njettiness_tau3/AK15Jet_Njettiness_tau2",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_PuppiSoftDropMass", "AK15 Jet SD mass", 20, 50.0, 250.0),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def getDiscriminatorPlots(data=None, discrname=""):
    discriminatorPlots = []
    # discriminatorPlots += plots_ge4j_ge4t(data)
    # discriminatorPlots += plots_ge6j_ge3t(data)
    # discriminatorPlots += plots_le5j_ge3t(data)
    # discriminatorPlots += plots_5j_ge3t(data)
    # discriminatorPlots += plots_ge4j_ge3t(data)
    # discriminatorPlots += plots_4j_ge3t(data)
    # discriminatorPlots += plots_ge4j_3t(data)
    discriminatorPlots += control_plots(data)
    # discriminatorPlots += reco_plots(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
