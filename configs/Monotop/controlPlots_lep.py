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


def control_plots_ttbar_lep(data=None):
    label = "#scale[0.8]{t#bar{t} control region (leptonic)}"
    extension = "_CRttbar_lep"
    selection = "((N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu24_vX==1) || (N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1 || Triggered_HLT_Ele32_WPTight_Gsf_vX==1))) && (Hadr_Recoil_Pt>250.) && (N_LoosePhotons==0) && (N_BTagsM>=2) && (N_HEM_Jets==0 && N_HEM_Electrons==0)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "Puppi MET", 25, 0.0, 500.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "Puppi MET #phi", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo MET", 25, 0.0, 500.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "CaloMET_PFMET_ratio", 25, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                25,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{t}", 40, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{t}",
                40,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass", 40, 0.0, 1000.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 20, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 20, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
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
                "AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
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
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass",
                25,
                0.0,
                250.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            "AK8Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            "AK8Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            "AK8Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_CHF" + extension, "AK8 Jet CHF", 20, 0.0, 1.0),
            "AK8Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_NHF" + extension, "AK8 Jet NHF", 20, 0.0, 1.0),
            "AK8Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet1_Pt" + extension,
                "AK8 SD Jet1 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK8Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet2_Pt" + extension,
                "AK8 SD Jet2 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK8Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK8 SD Jet1 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK8 SD Jet2 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_TvsQCD" + extension,
                "AK8 Jet DeepAK8 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbc" + extension,
                "AK8 Jet DeepAK8 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbcq" + extension,
                "AK8 Jet DeepAK8 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbq" + extension,
                "AK8 Jet DeepAK8 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbqq" + extension,
                "AK8 Jet DeepAK8 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
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
                "AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
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
            ROOT.TH1D(
                "AK8Jet_PuppiSoftDropMass" + extension,
                "AK8 Jet SD mass",
                25,
                0.0,
                250.0,
            ),
            "AK8Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            "Evt_Pt_GenMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            "NaiveMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "Hadronic Recoil", 40, 200.0, 1200.0
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "Hadronic Recoil #phi", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "DeltaPhi_AK15Jet_MET",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
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
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "DeltaPhi_AK4Jet_MET", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
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
            ROOT.TH1D(
                "Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            ),
            "Weight_GEN_nom",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{t}", 39, 10.0, 400.0),
            "Muon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Eta" + extension, "Tight Muon #eta", 25, -2.5, 2.5),
            "Muon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Phi" + extension, "Tight Muon #phi", 30, -3.14, 3.14),
            "Muon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Pt" + extension, "Tight Electron p_{t}", 39, 10.0, 400.0
            ),
            "Electron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Electron_Eta" + extension, "Tight Electron #eta", 25, -2.5, 2.5),
            "Electron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Phi" + extension, "Tight Electron #phi", 30, -3.14, 3.14
            ),
            "Electron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK8Jet_AK4JetTagged" + extension,
                "DeltaR_AK8Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK8Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            ),
            "DeltaR_AK8Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btags", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btags", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btags", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet pt", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet pt", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            "Weight_TopPt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK4Jet_AK15Jet_pt_ratio" + extension,
                "AK4Jet/AK15Jet pt ratio",
                40,
                0.0,
                2.0,
            ),
            "Jet_Pt[0]/AK15Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_W_lep(data=None):
    label = "#scale[0.8]{W control region (leptonic)}"
    extension = "_CRW_lep"
    selection = "((N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu24_vX==1) || (N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1 || Triggered_HLT_Ele32_WPTight_Gsf_vX==1))) && (Hadr_Recoil_Pt>250.) && (N_LoosePhotons==0) && (N_BTagsM==0) && (N_HEM_Jets==0 && N_HEM_Electrons==0)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "Puppi MET", 25, 0.0, 500.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "Puppi MET #phi", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo MET", 25, 0.0, 500.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "CaloMET_PFMET_ratio", 25, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                25,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{t}", 40, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{t}",
                40,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass", 40, 0.0, 1000.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 20, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 20, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
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
                "AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
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
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass",
                25,
                0.0,
                250.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            "AK8Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            "AK8Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            "AK8Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_CHF" + extension, "AK8 Jet CHF", 20, 0.0, 1.0),
            "AK8Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_NHF" + extension, "AK8 Jet NHF", 20, 0.0, 1.0),
            "AK8Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet1_Pt" + extension,
                "AK8 SD Jet1 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK8Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet2_Pt" + extension,
                "AK8 SD Jet2 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK8Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK8 SD Jet1 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK8 SD Jet2 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_TvsQCD" + extension,
                "AK8 Jet DeepAK8 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbc" + extension,
                "AK8 Jet DeepAK8 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbcq" + extension,
                "AK8 Jet DeepAK8 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbq" + extension,
                "AK8 Jet DeepAK8 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbqq" + extension,
                "AK8 Jet DeepAK8 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
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
                "AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
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
            ROOT.TH1D(
                "AK8Jet_PuppiSoftDropMass" + extension,
                "AK8 Jet SD mass",
                25,
                0.0,
                250.0,
            ),
            "AK8Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            "Evt_Pt_GenMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            "NaiveMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "Hadronic Recoil", 40, 200.0, 1200.0
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "Hadronic Recoil #phi", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "DeltaPhi_AK15Jet_MET",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
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
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "DeltaPhi_AK4Jet_MET", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
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
            ROOT.TH1D(
                "Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            ),
            "Weight_GEN_nom",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{t}", 39, 10.0, 400.0),
            "Muon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Eta" + extension, "Tight Muon #eta", 25, -2.5, 2.5),
            "Muon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Phi" + extension, "Tight Muon #phi", 30, -3.14, 3.14),
            "Muon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Pt" + extension, "Tight Electron p_{t}", 39, 10.0, 400.0
            ),
            "Electron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Electron_Eta" + extension, "Tight Electron #eta", 25, -2.5, 2.5),
            "Electron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Phi" + extension, "Tight Electron #phi", 30, -3.14, 3.14
            ),
            "Electron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK8Jet_AK4JetTagged" + extension,
                "DeltaR_AK8Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK8Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            ),
            "DeltaR_AK8Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btags", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btags", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btags", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet pt", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet pt", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            "Weight_TopPt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK4Jet_AK15Jet_pt_ratio" + extension,
                "AK4Jet/AK15Jet pt ratio",
                40,
                0.0,
                2.0,
            ),
            "Jet_Pt[0]/AK15Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_SR_lep(data=None):
    label = "#scale[0.8]{signal region (leptonic)}"
    extension = "_SR_lep"
    selection = "((N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu24_vX==1) || (N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele28_eta2p1_WPTight_Gsf_HT150_vX==1 || Triggered_HLT_Ele32_WPTight_Gsf_vX==1))) && (Hadr_Recoil_Pt>250.) && (N_LoosePhotons==0) && (N_BTagsM==1) && (N_HEM_Jets==0 && N_HEM_Electrons==0)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "Puppi MET", 25, 0.0, 500.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "Puppi MET #phi", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo MET", 25, 0.0, 500.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "CaloMET_PFMET_ratio", 25, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                25,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{t}", 40, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{t}",
                40,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass", 40, 0.0, 1000.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 20, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 20, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
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
                "AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
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
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass",
                25,
                0.0,
                250.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            "AK8Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            "AK8Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            "AK8Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_CHF" + extension, "AK8 Jet CHF", 20, 0.0, 1.0),
            "AK8Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK8Jet_NHF" + extension, "AK8 Jet NHF", 20, 0.0, 1.0),
            "AK8Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet1_Pt" + extension,
                "AK8 SD Jet1 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK8Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet2_Pt" + extension,
                "AK8 SD Jet2 p_{t}",
                40,
                0.0,
                1000.0,
            ),
            "AK8Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK8 SD Jet1 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK8 SD Jet2 DeepJetCSV",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_TvsQCD" + extension,
                "AK8 Jet DeepAK8 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbc" + extension,
                "AK8 Jet DeepAK8 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbcq" + extension,
                "AK8 Jet DeepAK8 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbq" + extension,
                "AK8 Jet DeepAK8 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_DeepAK8_probTbqq" + extension,
                "AK8 Jet DeepAK8 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK8Jet_DeepAK8_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
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
                "AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
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
            ROOT.TH1D(
                "AK8Jet_PuppiSoftDropMass" + extension,
                "AK8 Jet SD mass",
                25,
                0.0,
                250.0,
            ),
            "AK8Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            "Evt_Pt_GenMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            "NaiveMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "Hadronic Recoil", 40, 200.0, 1200.0
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "Hadronic Recoil #phi", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "DeltaPhi_AK15Jet_MET",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
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
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "DeltaPhi_AK4Jet_MET", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
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
            ROOT.TH1D(
                "Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            ),
            "Weight_GEN_nom",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{t}", 39, 10.0, 400.0),
            "Muon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Eta" + extension, "Tight Muon #eta", 25, -2.5, 2.5),
            "Muon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Phi" + extension, "Tight Muon #phi", 30, -3.14, 3.14),
            "Muon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Pt" + extension, "Tight Electron p_{t}", 39, 10.0, 400.0
            ),
            "Electron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Electron_Eta" + extension, "Tight Electron #eta", 25, -2.5, 2.5),
            "Electron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Phi" + extension, "Tight Electron #phi", 30, -3.14, 3.14
            ),
            "Electron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK8Jet_AK4JetTagged" + extension,
                "DeltaR_AK8Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK8Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            ),
            "DeltaR_AK8Jet_AK4Jet",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btags", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btags", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btags", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet pt", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet pt", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet pt", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            "Weight_TopPt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK4Jet_AK15Jet_pt_ratio" + extension,
                "AK4Jet/AK15Jet pt ratio",
                40,
                0.0,
                2.0,
            ),
            "Jet_Pt[0]/AK15Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def getDiscriminatorPlots(data=None, discrname=""):
    discriminatorPlots = []
    discriminatorPlots += control_plots_ttbar_lep(data)
    discriminatorPlots += control_plots_W_lep(data)
    discriminatorPlots += control_plots_SR_lep(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
