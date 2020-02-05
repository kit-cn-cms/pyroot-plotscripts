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

generalselection = "(Evt_Pt_MET>100.)*(N_LoosePhotons==0)*(DeltaPhi_AK4Jet_MET[0]>1.0)"

def control_plots_lep_CR_ttbarlep(data=None):
    label = "#scale[0.8]{t#bar{t} control region (leptonic)}"
    extension = "_lep_CR_ttbarlep"
    selection = generalselection
    selection += "*((N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu24_vX==1) || (N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele27_WPTight_Gsf_vX==1 || Triggered_HLT_Photon175_vX==1)))"
    selection += "*(N_BTagsM>=2)"

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
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
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
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{t}", 20, 10.0, 410.0),
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
                "Electron_Pt" + extension, "Tight Electron p_{t}", 20, 10.0, 410.0
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
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("M_W_transverse" + extension, "m_{W,transverse}", 30, 0., 600.),
            "M_W_transverse",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_lep_CR_Wlep(data=None):
    label = "#scale[0.8]{W control region (leptonic)}"
    extension = "_lep_CR_Wlep"
    selection = generalselection
    selection += "*((N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu24_vX==1) || (N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele27_WPTight_Gsf_vX==1 || Triggered_HLT_Photon175_vX==1)))"
    selection += "*(N_BTagsL==0)"

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
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
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
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{t}", 20, 10.0, 410.0),
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
                "Electron_Pt" + extension, "Tight Electron p_{t}", 20, 10.0, 410.0
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
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("M_W_transverse" + extension, "m_{W,transverse}", 30, 0., 600.),
            "M_W_transverse",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_lep_SR(data=None):
    label = "#scale[0.8]{signal region (leptonic)}"
    extension = "_lep_SR"
    selection = generalselection
    selection += "*((N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu24_vX==1) || (N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele27_WPTight_Gsf_vX==1 || Triggered_HLT_Photon175_vX==1)))"
    selection += "*(N_BTagsM<=1 && N_BTagsL>=1 && N_BTagsL<=2)"

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "Puppi MET", 50, 0.0, 1000.0),
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
            ROOT.TH1D("CaloMET" + extension, "Calo MET", 50, 0.0, 1000.0),
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
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
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
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{t}", 20, 10.0, 410.0),
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
                "Electron_Pt" + extension, "Tight Electron p_{t}", 20, 10.0, 410.0
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
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("M_W_transverse" + extension, "m_{W,transverse}", 30, 0., 600.),
            "M_W_transverse",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_lep_CR_ttbardilep(data=None):
    label = "#scale[0.8]{t#bar{t} control region (dileptonic)}"
    extension = "_lep_CR_ttbardilep"
    selection = generalselection
    selection += "*((N_LooseMuons==2 && N_TightMuons>=1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu24_vX==1 && (DiMuon_Mass<60 || DiMuon_Mass>120)) || (N_LooseElectrons==2 && N_TightElectrons>=1 && N_LooseMuons==0 && (Triggered_HLT_Ele27_WPTight_Gsf_vX==1 || Triggered_HLT_Photon175_vX==1) && (DiElectron_Mass<60 || DiElectron_Mass>120)) || (N_LooseMuons==1 && N_LooseElectrons==1 && ((N_TightMuons==1 && Triggered_HLT_IsoMu24_vX==1) || (N_TightElectrons==1 && (Triggered_HLT_Ele27_WPTight_Gsf_vX==1 || Triggered_HLT_Photon175_vX==1)))))"
    selection += "*(N_BTagsM>=2)"

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
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
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
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
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
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("M_W_transverse" + extension, "m_{W,transverse}", 30, 0., 600.),
            "M_W_transverse",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def getDiscriminatorPlots(data=None, discrname=""):
    discriminatorPlots = []
    discriminatorPlots += control_plots_lep_CR_ttbarlep(data)
    discriminatorPlots += control_plots_lep_CR_Wlep(data)
    discriminatorPlots += control_plots_lep_SR(data)
    #discriminatorPlots += control_plots_lep_CR_ttbardilep(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
