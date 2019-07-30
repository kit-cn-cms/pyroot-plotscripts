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
            "(N_LooseMuons==0 && N_LooseElectrons==0 && N_LoosePhotons==0)*(Evt_Pt_MET>250.)",
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
            ROOT.TH1D("CaloMET", "Calo MET", 32, 200.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET_PFMET_ratio", "CaloMET_PFMET_ratio", 40, 0.0, 4.0),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio", "CaloMET_Hadr_Recoil_ratio", 40, 0.0, 4.0
            ),
            "CaloMET_Hadr_Recoil_ratio",
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
            ROOT.TH1D("AK15Jet_SoftDropJet1_Pt", "AK15 SD Jet1 p_{t}", 40, 0.0, 1000.0),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet2_Pt", "AK15 SD Jet2 p_{t}", 40, 0.0, 1000.0),
            "AK15Jet_SoftDropJet2_Pt",
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
                "AK15Jet_DeepAK15_probTbc", "AK15 Jet DeepAK15 probTbc", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq", "AK15 Jet DeepAK15 probTbcq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq", "AK15 Jet DeepAK15 probTbq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq", "AK15 Jet DeepAK15 probTbqq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbqq",
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
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_GenMET", "Puppi GEN MET", 40, 0.0, 1000.0),
            "Evt_Pt_GenMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("NaiveMET", "Naive GEN MET", 40, 0.0, 1000.0),
            "NaiveMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Hadr_Recoil_Pt", "Hadronic Recoil", 32, 200.0, 1000.0),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N1_N2_Mass", "Mediator Mass", 50, 0.0, 5000.0),
            "N1_N2_Mass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N1_N2_Pt", "Mediator p_{t}", 50, 0.0, 5000.0),
            "N1_N2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Neutralino_Pt", "Neutralino p_{t}", 40, 0.0, 2000.0),
            "Neutralino_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Neutralino_Mass", "Neutralino Mass", 40, 0.0, 2000.0),
            "Neutralino_Mass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaPhi_AK15Jet_MET", "DeltaPhi_AK15Jet_MET", 30, 0.0, 3.14),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil",
                "DeltaPhi_AK15Jet_Hadr_Recoil",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_Hadr_Recoil",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_B_DR", "GenTopHad_B_DR", 30, 0.0, 4.0),
            "GenTopHad_B_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_Q1_DR", "GenTopHad_Q1_DR", 30, 0.0, 4.0),
            "GenTopHad_Q1_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_Q2_DR", "GenTopHad_Q2_DR", 30, 0.0, 4.0),
            "GenTopHad_Q2_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_B_Q1_DR", "GenTopHad_B_Q1_DR", 30, 0.0, 4.0),
            "GenTopHad_B_Q1_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_B_Q2_DR", "GenTopHad_B_Q2_DR", 30, 0.0, 4.0),
            "GenTopHad_B_Q2_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_Q1_Q2_DR", "GenTopHad_Q1_Q2_DR", 30, 0.0, 4.0),
            "GenTopHad_Q1_Q2_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_W_Q1_DR", "GenTopHad_W_Q1_DR", 30, 0.0, 4.0),
            "GenTopHad_W_Q1_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_W_Q2_DR", "GenTopHad_W_Q2_DR", 30, 0.0, 4.0),
            "GenTopHad_W_Q2_DR",
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
