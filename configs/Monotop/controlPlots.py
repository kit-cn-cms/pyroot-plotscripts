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


def control_plots_SR(data=None):
    label = "#scale[0.8]{signal region}"
    extension = "_SR"
    selection = "(N_LooseMuons==0 && N_LooseElectrons==0 && N_LoosePhotons==0)*((Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_vX == 1) || (Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_vX == 1))*(Hadr_Recoil_Pt>250.)*(AK15Jet_SoftDrop_Pt[0]>250)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield"+extension, "yield", 1, 0., 2.),
            "1.",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET"+extension, "Puppi MET", 40, 200.0, 1200.0),
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
            ROOT.TH1D("CaloMET"+extension, "Calo MET", 40, 200.0, 1200.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET_PFMET_ratio"+extension, "CaloMET_PFMET_ratio", 25, 0.0, 10.0),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio"+extension, "CaloMET_Hadr_Recoil_ratio", 25, 0.0, 10.0
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt"+extension, "AK15 Jet p_{t}", 40, 200.0, 1200.0),
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
            ROOT.TH1D("AK15Jet_SoftDrop_Pt"+extension, "AK15 SD Jet p_{t}", 40, 200.0, 1200.0),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Eta"+extension, "AK15 SD Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Phi"+extension, "AK15 SD Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Mass"+extension, "AK15 SD Jet mass", 40, 0.0, 1000.0),
            "AK15Jet_SoftDrop_M",
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
            ROOT.TH1D("AK15Jet_SoftDropJet1_DeepJetCSV"+extension, "AK15 SD Jet1 DeepJetCSV", 20, 0.0, 1.0),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet2_DeepJetCSV"+extension, "AK15 SD Jet2 DeepJetCSV", 20, 0.0, 1.0),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
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
            ROOT.TH1D("AK15Jet_PuppiSoftDropMass"+extension, "AK15 Jet SD mass", 25, 0.0, 250.0),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF"+extension, "AK15 Jet CHF", 20, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF"+extension, "AK15 Jet NHF", 20, 0.0, 1.0),
            "AK15Jet_NHF",
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
            ROOT.TH1D("Hadr_Recoil_Pt"+extension, "Hadronic Recoil", 40, 200.0, 1200.0),
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
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM"+extension, "medium btags", 5, 0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL"+extension, "loose btags", 5, 0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT"+extension, "tight btags", 5, 0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt"+extension, "AK4 Jet pt", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta"+extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi"+extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV"+extension, "AK4 Jet DeepJet", 20, 0., 1.),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets"+extension, "number of AK4 jets", 5, 0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK15Jet_AK4JetTagged"+extension, "DeltaR_AK15Jet_AK4JetTagged", 40, 0., 4.),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK15Jet_AK4Jet"+extension, "DeltaR_AK15Jet_AK4Jet", 40, 0., 4.),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK4Jet_AK15Jet_pt_ratio"+extension, "AK4Jet/AK15Jet pt ratio", 40, 0., 2.),
            "Jet_Pt[0]/AK15Jet_Pt[0]",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_mumu(data=None):
    label = "#scale[0.8]{Z(#mu#bar{#mu}) control region}"
    extension = "_CRMuMu"
    selection = "(N_LooseMuons==2 && N_TightMuons>=1 && N_LooseElectrons==0 && N_LoosePhotons==0)*(Triggered_HLT_IsoMu24_vX==1)*(Hadr_Recoil_Pt>250.)*(DiMuon_Mass>60)*(DiMuon_Mass<120)*(DiMuon_Pt>200)*(AK15Jet_SoftDrop_Pt[0]>250)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield"+extension, "yield", 1, 0., 2.),
            "1.",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET"+extension, "Puppi MET", 20, 0.0, 200.0),
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
            ROOT.TH1D("CaloMET"+extension, "Calo MET", 20, 0.0, 200.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET_PFMET_ratio"+extension, "CaloMET_PFMET_ratio", 25, 0.0, 10.0),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio"+extension, "CaloMET_Hadr_Recoil_ratio", 25, 0.0, 10.0
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt"+extension, "AK15 Jet p_{t}", 40, 200.0, 1200.0),
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
            ROOT.TH1D("AK15Jet_SoftDrop_Pt"+extension, "AK15 SD Jet p_{t}", 40, 200.0, 1200.0),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Eta"+extension, "AK15 SD Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Phi"+extension, "AK15 SD Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Mass"+extension, "AK15 SD Jet mass", 40, 0.0, 1000.0),
            "AK15Jet_SoftDrop_M",
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
            ROOT.TH1D("AK15Jet_SoftDropJet1_DeepJetCSV"+extension, "AK15 SD Jet1 DeepJetCSV", 20, 0.0, 1.0),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet2_DeepJetCSV"+extension, "AK15 SD Jet2 DeepJetCSV", 20, 0.0, 1.0),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
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
                "AK15pJet_Njettiness_tau3_AK15Jet_Njettiness_tau2"+extension,
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
            ROOT.TH1D("AK15Jet_PuppiSoftDropMass"+extension, "AK15 Jet SD mass", 25, 0.0, 250.0),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Pt"+extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            "AK8Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Eta"+extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            "AK8Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Phi"+extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            "AK8Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet1_Pt"+extension, "AK8 SD Jet1 p_{t}", 40, 0.0, 1000.0),
            "AK8Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet2_Pt"+extension, "AK8 SD Jet2 p_{t}", 40, 0.0, 1000.0),
            "AK8Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet1_DeepJetCSV"+extension, "AK8 SD Jet1 DeepJetCSV", 20, 0.0, 1.0),
            "AK8Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet2_DeepJetCSV"+extension, "AK8 SD Jet2 DeepJetCSV", 20, 0.0, 1.0),
            "AK8Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
               "AK8Jet_DeepAK8_TvsQCD"+extension, "AK8 Jet DeepAK8 TvsQCD", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
               "AK8Jet_DeepAK8_probTbc"+extension, "AK8 Jet DeepAK8 probTbc", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
               "AK8Jet_DeepAK8_probTbcq"+extension, "AK8 Jet DeepAK8 probTbcq", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
               "AK8Jet_DeepAK8_probTbq"+extension, "AK8 Jet DeepAK8 probTbq", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
               "AK8Jet_DeepAK8_probTbqq"+extension, "AK8 Jet DeepAK8 probTbqq", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2"+extension,
                "AK8 Jet #tau_{3}/#tau_{2}",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1"+extension,
                "AK8 Jet #tau_{2}/#tau_{1}",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_PuppiSoftDropMass"+extension, "AK8 Jet SD mass", 25, 0.0, 250.0),
            "AK8Jet_PuppiSoftDropMass",
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
            ROOT.TH1D("Hadr_Recoil_Pt"+extension, "Hadronic Recoil", 40, 200.0, 1200.0),
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
            ROOT.TH1D("DeltaPhi_AK4Jet_MET"+extension, "DeltaPhi_AK4Jet_MET", 30, 0.0, 3.14),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil"+extension,
                "DeltaPhi_AK4Jet_Hadr_Recoil",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
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
            ROOT.TH1D("LooseMuon_Pt"+extension, "Loose Muon p_{t}", 49, 10.0, 500.0),
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
            ROOT.TH1D("Muon_Pt"+extension, "Tight Muon p_{t}", 49, 10.0, 500.0),
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
            ROOT.TH1D("DiMuon_Pt"+extension, "DiMuon p_{t}", 69, 10.0, 700.0),
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
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM"+extension, "medium btags", 5, 0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL"+extension, "loose btags", 5, 0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT"+extension, "tight btags", 5, 0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt"+extension, "AK4 Jet pt", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0"+extension, "leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1"+extension, "sub-leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_2"+extension, "sub-sub-leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta"+extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi"+extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV"+extension, "AK4 Jet DeepJet", 20, 0., 1.),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets"+extension, "number of AK4 jets", 5, 0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK15Jet_AK4JetTagged"+extension, "DeltaR_AK15Jet_AK4JetTagged", 40, 0., 4.),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK15Jet_AK4Jet"+extension, "DeltaR_AK15Jet_AK4Jet", 40, 0., 4.),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK8Jet_AK4JetTagged"+extension, "DeltaR_AK8Jet_AK4JetTagged", 40, 0., 4.),
            "DeltaR_AK8Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK8Jet_AK4Jet"+extension, "DeltaR_AK8Jet_AK4Jet", 40, 0., 4.),
            "DeltaR_AK8Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK4Jet_AK15Jet_pt_ratio"+extension, "AK4Jet/AK15Jet pt ratio", 40, 0., 2.),
            "Jet_Pt[0]/AK15Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF"+extension, "AK15 Jet CHF", 20, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF"+extension, "AK15 Jet NHF", 20, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK15Jet_DiMuon"+extension, "DeltaR_AK15Jet_DiMuon", 50, 0., 5.),
            "sqrt(pow(AK15Jet_Eta[0]-DiMuon_Eta,2)+pow(AK15Jet_Phi[0]-DiMuon_Phi,2))",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_elel(data=None):
    label = "#scale[0.8]{Z(e#bar{e}) control region}"
    extension = "_CRElEl"
    selection = "(N_LooseElectrons==2 && N_TightElectrons>=1 && N_LooseMuons==0 && N_TightPhotons==0)*(Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1 || Triggered_HLT_Ele32_WPTight_Gsf_vX==1)*(Hadr_Recoil_Pt>250.)*(DiElectron_Mass>60)*(DiElectron_Mass<120)*(DiElectron_Pt>200)*(AK15Jet_SoftDrop_Pt[0]>250)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield"+extension, "yield", 1, 0., 2.),
            "1.",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET"+extension, "Puppi MET", 20, 0.0, 200.0),
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
            ROOT.TH1D("CaloMET"+extension, "Calo MET", 20, 0.0, 200.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET_PFMET_ratio"+extension, "CaloMET_PFMET_ratio", 25, 0.0, 10.0),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio"+extension, "CaloMET_Hadr_Recoil_ratio", 25, 0.0, 10.0
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt"+extension, "AK15 Jet p_{t}", 40, 200.0, 1200.0),
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
            ROOT.TH1D("AK15Jet_SoftDrop_Pt"+extension, "AK15 SD Jet p_{t}", 40, 200.0, 1200.0),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Eta"+extension, "AK15 SD Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Phi"+extension, "AK15 SD Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Mass"+extension, "AK15 SD Jet mass", 40, 0.0, 1000.0),
            "AK15Jet_SoftDrop_M",
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
            ROOT.TH1D("AK15Jet_SoftDropJet1_DeepJetCSV"+extension, "AK15 SD Jet1 DeepJetCSV", 20, 0.0, 1.0),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet2_DeepJetCSV"+extension, "AK15 SD Jet2 DeepJetCSV", 20, 0.0, 1.0),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
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
            ROOT.TH1D("AK15Jet_PuppiSoftDropMass"+extension, "AK15 Jet SD mass", 25, 0.0, 250.0),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Pt"+extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            "AK8Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Eta"+extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            "AK8Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Phi"+extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            "AK8Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet1_Pt"+extension, "AK8 SD Jet1 p_{t}", 40, 0.0, 1000.0),
            "AK8Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet2_Pt"+extension, "AK8 SD Jet2 p_{t}", 40, 0.0, 1000.0),
            "AK8Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet1_DeepJetCSV"+extension, "AK8 SD Jet1 DeepJetCSV", 20, 0.0, 1.0),
            "AK8Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet2_DeepJetCSV"+extension, "AK8 SD Jet2 DeepJetCSV", 20, 0.0, 1.0),
            "AK8Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_TvsQCD"+extension, "AK8 Jet DeepAK8 TvsQCD", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbc"+extension, "AK8 Jet DeepAK8 probTbc", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbcq"+extension, "AK8 Jet DeepAK8 probTbcq", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbq"+extension, "AK8 Jet DeepAK8 probTbq", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbqq"+extension, "AK8 Jet DeepAK8 probTbqq", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2"+extension,
                "AK8 Jet #tau_{3}/#tau_{2}",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1"+extension,
                "AK8 Jet #tau_{2}/#tau_{1}",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_PuppiSoftDropMass"+extension, "AK8 Jet SD mass", 25, 0.0, 250.0),
            "AK8Jet_PuppiSoftDropMass",
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
            ROOT.TH1D("Hadr_Recoil_Pt"+extension, "Hadronic Recoil", 40, 200.0, 1200.0),
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
            ROOT.TH1D("DeltaPhi_AK4Jet_MET"+extension, "DeltaPhi_AK4Jet_MET", 30, 0.0, 3.14),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil"+extension,
                "DeltaPhi_AK4Jet_Hadr_Recoil",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
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
            ROOT.TH1D("LooseElectron_Pt"+extension, "Loose Electron p_{t}", 49, 10.0, 500.0),
            "LooseElectron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("LooseElectron_Eta"+extension, "Loose Electron #eta", 25, -2.5, 2.5),
            "LooseElectron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("LooseElectron_Phi"+extension, "Loose Electron #phi", 30, -3.14, 3.14),
            "LooseElectron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Electron_Pt"+extension, "Tight Electron p_{t}", 49, 10.0, 500.0),
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
        plotClasses.Plot(
            ROOT.TH1D("DiElectron_Pt"+extension, "DiElectron p_{t}", 69, 10.0, 700.0),
            "DiElectron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiElectron_Eta"+extension, "DiElectron #eta", 25, -2.5, 2.5),
            "DiElectron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiElectron_Phi"+extension, "DiElectron #phi", 30, -3.14, 3.14),
            "DiElectron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiElectron_Mass"+extension, "DiElectron mass", 40, 0.0, 200.0),
            "DiElectron_Mass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM"+extension, "medium btags", 5, 0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL"+extension, "loose btags", 5, 0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT"+extension, "tight btags", 5, 0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt"+extension, "AK4 Jet pt", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0"+extension, "leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1"+extension, "sub-leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_2"+extension, "sub-sub-leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta"+extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi"+extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV"+extension, "AK4 Jet DeepJet", 20, 0., 1.),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets"+extension, "number of AK4 jets", 5, 0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK15Jet_AK4JetTagged"+extension, "DeltaR_AK15Jet_AK4JetTagged", 40, 0., 4.),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK15Jet_AK4Jet"+extension, "DeltaR_AK15Jet_AK4Jet", 40, 0., 4.),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK8Jet_AK4JetTagged"+extension, "DeltaR_AK8Jet_AK4JetTagged", 40, 0., 4.),
            "DeltaR_AK8Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK8Jet_AK4Jet"+extension, "DeltaR_AK8Jet_AK4Jet", 40, 0., 4.),
            "DeltaR_AK8Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK4Jet_AK15Jet_pt_ratio"+extension, "AK4Jet/AK15Jet pt ratio", 40, 0., 2.),
            "Jet_Pt[0]/AK15Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF"+extension, "AK15 Jet CHF", 20, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF"+extension, "AK15 Jet NHF", 20, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK15Jet_DiElectron"+extension, "DeltaR_AK15Jet_DiElectron", 50, 0., 5.),
            "sqrt(pow(AK15Jet_Eta[0]-DiElectron_Eta,2)+pow(AK15Jet_Phi[0]-DiElectron_Phi,2))",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_ttbar(data=None):
    label = "#scale[0.8]{t#bar{t} control region}"
    extension = "_CRttbar"
    selection = "((N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu24_vX==1) || (N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1 || Triggered_HLT_Ele32_WPTight_Gsf_vX==1))) && (Hadr_Recoil_Pt>250.) && (N_TightPhotons==0) && (N_AK4JetsTagged_outside_AK15Jets==1) && (N_HEM_Electrons==0 && N_HEM_Muons==0) && (AK15Jet_SoftDrop_Pt[0]>250)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield"+extension, "yield", 1, 0., 2.),
            "1.",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET"+extension, "Puppi MET", 25, 0.0, 500.0),
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
            ROOT.TH1D("CaloMET"+extension, "Calo MET", 25, 0.0, 500.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET_PFMET_ratio"+extension, "CaloMET_PFMET_ratio", 25, 0.0, 10.0),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio"+extension, "CaloMET_Hadr_Recoil_ratio", 25, 0.0, 10.0
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt"+extension, "AK15 Jet p_{t}", 40, 200.0, 1200.0),
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
            ROOT.TH1D("AK15Jet_SoftDrop_Pt"+extension, "AK15 SD Jet p_{t}", 40, 200.0, 1200.0),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Eta"+extension, "AK15 SD Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Phi"+extension, "AK15 SD Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDrop_Mass"+extension, "AK15 SD Jet mass", 40, 0.0, 1000.0),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF"+extension, "AK15 Jet CHF", 20, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF"+extension, "AK15 Jet NHF", 20, 0.0, 1.0),
            "AK15Jet_NHF",
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
            ROOT.TH1D("AK15Jet_SoftDropJet1_DeepJetCSV"+extension, "AK15 SD Jet1 DeepJetCSV", 20, 0.0, 1.0),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_SoftDropJet2_DeepJetCSV"+extension, "AK15 SD Jet2 DeepJetCSV", 20, 0.0, 1.0),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
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
            ROOT.TH1D("AK15Jet_PuppiSoftDropMass"+extension, "AK15 Jet SD mass", 25, 0.0, 250.0),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Pt"+extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            "AK8Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Eta"+extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            "AK8Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Phi"+extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            "AK8Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_CHF"+extension, "AK8 Jet CHF", 20, 0.0, 1.0),
            "AK8Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_NHF"+extension, "AK8 Jet NHF", 20, 0.0, 1.0),
            "AK8Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet1_Pt"+extension, "AK8 SD Jet1 p_{t}", 40, 0.0, 1000.0),
            "AK8Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet2_Pt"+extension, "AK8 SD Jet2 p_{t}", 40, 0.0, 1000.0),
            "AK8Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),   
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet1_DeepJetCSV"+extension, "AK8 SD Jet1 DeepJetCSV", 20, 0.0, 1.0),
            "AK8Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_SoftDropJet2_DeepJetCSV"+extension, "AK8 SD Jet2 DeepJetCSV", 20, 0.0, 1.0),
            "AK8Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_TvsQCD"+extension, "AK8 Jet DeepAK8 TvsQCD", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbc"+extension, "AK8 Jet DeepAK8 probTbc", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbcq"+extension, "AK8 Jet DeepAK8 probTbcq", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbq"+extension, "AK8 Jet DeepAK8 probTbq", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbqq"+extension, "AK8 Jet DeepAK8 probTbqq", 20, 0.0, 1.0
            ),
            "AK8Jet_DeepAK8_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2"+extension,
                "AK8 Jet #tau_{3}/#tau_{2}",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1"+extension,
                "AK8 Jet #tau_{2}/#tau_{1}",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_PuppiSoftDropMass"+extension, "AK8 Jet SD mass", 25, 0.0, 250.0),
            "AK8Jet_PuppiSoftDropMass",
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
            ROOT.TH1D("Hadr_Recoil_Pt"+extension, "Hadronic Recoil", 40, 200.0, 1200.0),
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
            ROOT.TH1D("DeltaPhi_AK4Jet_MET"+extension, "DeltaPhi_AK4Jet_MET", 30, 0.0, 3.14),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil"+extension,
                "DeltaPhi_AK4Jet_Hadr_Recoil",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
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
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK15Jet_AK4JetTagged"+extension, "DeltaR_AK15Jet_AK4JetTagged", 40, 0., 4.),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK15Jet_AK4Jet"+extension, "DeltaR_AK15Jet_AK4Jet", 40, 0., 4.),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK8Jet_AK4JetTagged"+extension, "DeltaR_AK8Jet_AK4JetTagged", 40, 0., 4.),
            "DeltaR_AK8Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DeltaR_AK8Jet_AK4Jet"+extension, "DeltaR_AK8Jet_AK4Jet", 40, 0., 4.),
            "DeltaR_AK8Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM"+extension, "medium btags", 5, 0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL"+extension, "loose btags", 5, 0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT"+extension, "tight btags", 5, 0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt"+extension, "AK4 Jet pt", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0"+extension, "leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1"+extension, "sub-leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_2"+extension, "sub-sub-leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta"+extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi"+extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV"+extension, "AK4 Jet DeepJet", 20, 0., 1.),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets"+extension, "number of AK4 jets", 5, 0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Weight_TopPt"+extension, "Weight Top Pt", 20, 0., 2.),
            "Weight_TopPt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK4Jet_AK15Jet_pt_ratio"+extension, "AK4Jet/AK15Jet pt ratio", 40, 0., 2.),
            "Jet_Pt[0]/AK15Jet_Pt[0]",
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
    #discriminatorPlots += control_plots_SR(data)
    discriminatorPlots += control_plots_mumu(data)
    discriminatorPlots += control_plots_ttbar(data)
    discriminatorPlots += control_plots_elel(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
