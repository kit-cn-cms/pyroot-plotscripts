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
    extension = "_SR"
    selection = "(N_LooseMuons==0 && N_LooseElectrons==0 && N_LoosePhotons==0)*(Evt_Pt_MET>250.)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET"+extension, "Puppi MET", 32, 200.0, 1000.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET"+extension, "Puppi MET #phi", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET"+extension, "Calo MET", 32, 200.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET_PFMET_ratio"+extension, "CaloMET_PFMET_ratio", 40, 0.0, 4.0),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio"+extension, "CaloMET_Hadr_Recoil_ratio", 40, 0.0, 4.0
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt"+extension, "AK15 Jet p_{t}", 32, 200.0, 1000.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta"+extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi"+extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet1_Pt"+extension, "AK15 SD Jet1 p_{t}", 40, 0.0, 1000.0),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet2_Pt"+extension, "AK15 SD Jet2 p_{t}", 40, 0.0, 1000.0),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD"+extension, "AK15 Jet DeepAK15 TvsQCD", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc"+extension, "AK15 Jet DeepAK15 probTbc", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq"+extension, "AK15 Jet DeepAK15 probTbcq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq"+extension, "AK15 Jet DeepAK15 probTbq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq"+extension, "AK15 Jet DeepAK15 probTbqq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_Njettiness_tau3_AK15Jet_Njettiness_tau2"+extension,
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
            ROOT.TH1D(
                "AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1"+extension,
                "AK15 Jet #tau_{2}/#tau_{1}",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_PuppiSoftDropMass"+extension, "AK15 Jet SD mass", 20, 50.0, 250.0),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_GenMET"+extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            "Evt_Pt_GenMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("NaiveMET"+extension, "Naive GEN MET", 40, 0.0, 1000.0),
            "NaiveMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Hadr_Recoil_Pt"+extension, "Hadronic Recoil", 32, 200.0, 1000.0),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Hadr_Recoil_Phi"+extension, "Hadronic Recoil #phi", 30, -3.14, 3.14),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N1_N2_Mass"+extension, "Mediator Mass", 50, 0.0, 5000.0),
            "N1_N2_Mass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N1_N2_Pt"+extension, "Mediator p_{t}", 50, 0.0, 5000.0),
            "N1_N2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Neutralino_Pt"+extension, "Neutralino p_{t}", 40, 0.0, 2000.0),
            "Neutralino_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Neutralino_Mass"+extension, "Neutralino Mass", 40, 0.0, 2000.0),
            "Neutralino_Mass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaPhi_AK15Jet_MET"+extension, "DeltaPhi_AK15Jet_MET", 30, 0.0, 3.14),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil"+extension,
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
            ROOT.TH1D("GenTopHad_B_DR"+extension, "GenTopHad_B_DR", 30, 0.0, 4.0),
            "GenTopHad_B_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_Q1_DR"+extension, "GenTopHad_Q1_DR", 30, 0.0, 4.0),
            "GenTopHad_Q1_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_Q2_DR"+extension, "GenTopHad_Q2_DR", 30, 0.0, 4.0),
            "GenTopHad_Q2_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_B_Q1_DR"+extension, "GenTopHad_B_Q1_DR", 30, 0.0, 4.0),
            "GenTopHad_B_Q1_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_B_Q2_DR"+extension, "GenTopHad_B_Q2_DR", 30, 0.0, 4.0),
            "GenTopHad_B_Q2_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_Q1_Q2_DR"+extension, "GenTopHad_Q1_Q2_DR", 30, 0.0, 4.0),
            "GenTopHad_Q1_Q2_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_W_Q1_DR"+extension, "GenTopHad_W_Q1_DR", 30, 0.0, 4.0),
            "GenTopHad_W_Q1_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("GenTopHad_W_Q2_DR"+extension, "GenTopHad_W_Q2_DR", 30, 0.0, 4.0),
            "GenTopHad_W_Q2_DR",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Weight_GEN_nom"+extension, "Generator weight", 1100, -100.0, 1000.0),
            "Weight_GEN_nom",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_mumu(data=None):
    label = "Hadr. Recoil > 250, AK15 Jet Pt > 250, 2 muons"
    extension = "_CRMuMu"
    selection = "(N_LooseMuons==2 && N_TightMuons>=1 && N_LooseElectrons==0 && N_LoosePhotons==0)*(Hadr_Recoil_Pt>250.)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET"+extension, "Puppi MET", 32, 200.0, 1000.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET"+extension, "Puppi MET #phi", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET"+extension, "Calo MET", 32, 200.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET_PFMET_ratio"+extension, "CaloMET_PFMET_ratio", 40, 0.0, 4.0),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio"+extension, "CaloMET_Hadr_Recoil_ratio", 40, 0.0, 4.0
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt"+extension, "AK15 Jet p_{t}", 32, 200.0, 1000.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta"+extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi"+extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet1_Pt"+extension, "AK15 SD Jet1 p_{t}", 40, 0.0, 1000.0),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet2_Pt"+extension, "AK15 SD Jet2 p_{t}", 40, 0.0, 1000.0),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD"+extension, "AK15 Jet DeepAK15 TvsQCD", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc"+extension, "AK15 Jet DeepAK15 probTbc", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq"+extension, "AK15 Jet DeepAK15 probTbcq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq"+extension, "AK15 Jet DeepAK15 probTbq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq"+extension, "AK15 Jet DeepAK15 probTbqq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_Njettiness_tau3_AK15Jet_Njettiness_tau2"+extension,
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
            ROOT.TH1D(
                "AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1"+extension,
                "AK15 Jet #tau_{2}/#tau_{1}",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_PuppiSoftDropMass"+extension, "AK15 Jet SD mass", 20, 50.0, 250.0),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_GenMET"+extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            "Evt_Pt_GenMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("NaiveMET"+extension, "Naive GEN MET", 40, 0.0, 1000.0),
            "NaiveMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Hadr_Recoil_Pt"+extension, "Hadronic Recoil", 32, 200.0, 1000.0),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Hadr_Recoil_Phi"+extension, "Hadronic Recoil #phi", 30, -3.14, 3.14),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaPhi_AK15Jet_MET"+extension, "DeltaPhi_AK15Jet_MET", 30, 0.0, 3.14),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil"+extension,
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
            ROOT.TH1D("Weight_GEN_nom"+extension, "Generator weight", 1100, -100.0, 1000.0),
            "Weight_GEN_nom",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("LooseMuon_Pt"+extension, "Loose Muon p_{t}", 39, 10.0, 400.0),
            "LooseMuon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("LooseMuon_Eta"+extension, "Loose Muon #eta", 25, -2.5, 2.5),
            "LooseMuon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("LooseMuon_Phi"+extension, "Loose Muon #phi", 30, -3.14, 3.14),
            "LooseMuon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt"+extension, "Tight Muon p_{t}", 39, 10.0, 400.0),
            "Muon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Eta"+extension, "Tight Muon #eta", 25, -2.5, 2.5),
            "Muon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Phi"+extension, "Tight Muon #phi", 30, -3.14, 3.14),
            "Muon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiMuon_Pt"+extension, "DiMuon p_{t}", 59, 10.0, 600.0),
            "DiMuon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiMuon_Eta"+extension, "DiMuon #eta", 25, -2.5, 2.5),
            "DiMuon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiMuon_Phi"+extension, "DiMuon #phi", 30, -3.14, 3.14),
            "DiMuon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiMuon_Mass"+extension, "DiMuon mass", 40, 0.0, 200.0),
            "DiMuon_Mass",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_ttbar(data=None):
    label = "Hadr. Recoil > 250, AK15 Jet Pt > 250, 1 electron/muon"
    extension = "_CRttbar"
    selection = "(((N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0) || (N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0)) && N_LoosePhotons==0)*(Hadr_Recoil_Pt>250.)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET"+extension, "Puppi MET", 32, 200.0, 1000.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET"+extension, "Puppi MET #phi", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET"+extension, "Calo MET", 32, 200.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET_PFMET_ratio"+extension, "CaloMET_PFMET_ratio", 40, 0.0, 4.0),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio"+extension, "CaloMET_Hadr_Recoil_ratio", 40, 0.0, 4.0
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt"+extension, "AK15 Jet p_{t}", 32, 200.0, 1000.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta"+extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi"+extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet1_Pt"+extension, "AK15 SD Jet1 p_{t}", 40, 0.0, 1000.0),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet2_Pt"+extension, "AK15 SD Jet2 p_{t}", 40, 0.0, 1000.0),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD"+extension, "AK15 Jet DeepAK15 TvsQCD", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc"+extension, "AK15 Jet DeepAK15 probTbc", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq"+extension, "AK15 Jet DeepAK15 probTbcq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq"+extension, "AK15 Jet DeepAK15 probTbq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq"+extension, "AK15 Jet DeepAK15 probTbqq", 20, 0.0, 1.0
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_Njettiness_tau3_AK15Jet_Njettiness_tau2"+extension,
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
            ROOT.TH1D(
                "AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1"+extension,
                "AK15 Jet #tau_{2}/#tau_{1}",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_PuppiSoftDropMass"+extension, "AK15 Jet SD mass", 20, 50.0, 250.0),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_GenMET"+extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            "Evt_Pt_GenMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("NaiveMET"+extension, "Naive GEN MET", 40, 0.0, 1000.0),
            "NaiveMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Hadr_Recoil_Pt"+extension, "Hadronic Recoil", 32, 200.0, 1000.0),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Hadr_Recoil_Phi"+extension, "Hadronic Recoil #phi", 30, -3.14, 3.14),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaPhi_AK15Jet_MET"+extension, "DeltaPhi_AK15Jet_MET", 30, 0.0, 3.14),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil"+extension,
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
            ROOT.TH1D("Weight_GEN_nom"+extension, "Generator weight", 1100, -100.0, 1000.0),
            "Weight_GEN_nom",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt"+extension, "Tight Muon p_{t}", 39, 10.0, 400.0),
            "Muon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Eta"+extension, "Tight Muon #eta", 25, -2.5, 2.5),
            "Muon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Phi"+extension, "Tight Muon #phi", 30, -3.14, 3.14),
            "Muon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Electron_Pt"+extension, "Tight Electron p_{t}", 39, 10.0, 400.0),
            "Electron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Electron_Eta"+extension, "Tight Electron #eta", 25, -2.5, 2.5),
            "Electron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Electron_Phi"+extension, "Tight Electron #phi", 30, -3.14, 3.14),
            "Electron_Phi",
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
    #discriminatorPlots += control_plots(data)
    discriminatorPlots += control_plots_mumu(data)
    #discriminatorPlots += control_plots_ttbar(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
