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

generalselection = "(Evt_Pt_MET>150.)*(N_LoosePhotons==0)*(CaloMET>150.)*(DeltaPhi_AK4Jet_MET[0]>2.0)"
generalselection += "*(M_W_transverse[0]>=50.)"

def control_plots_lep_CR_ttbarEl(data=None):
    label = "#scale[0.8]{t#bar{t} control region (e)}"
    extension = "_lep_CR_ttbarEl"
    selection = generalselection
    selection += "*(N_BTagsM>=1 && N_BTagsL>=2)"
    selection += "*(N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Photon200_vX==1))"

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
                "DeltaPhi_AK4Jet_MET_0" + extension, "DeltaPhi_AK4Jet_MET_0", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_1" + extension, "DeltaPhi_AK4Jet_MET_1", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_2" + extension, "DeltaPhi_AK4Jet_MET_2", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[2]",
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
            ROOT.TH1D("Jet_NHF" + extension, "AK4 Jet NHF", 20, 0, 1.),
            "Jet_NHF",
            selection,
        label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CHF" + extension, "AK4 Jet CHF", 20, 0, 1.),
            "Jet_CHF",
            selection,
        label,
        ),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_NEMF" + extension, "AK4 Jet NEMF", 20, 0, 1.),
        #    "Jet_NEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_CEMF" + extension, "AK4 Jet CEMF", 20, 0, 1.),
        #    "Jet_CEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_MF" + extension, "AK4 Jet MF", 20, 0, 1.),
        #    "Jet_MF",
        #    selection,
        #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            #"Weight_TopPt",
            #selection,
            #label,
        #),
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
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_LooseElectron_MET" + extension, "DeltaPhi_LooseElectron_MET", 30, 0.0, 3.14
            ),
            "DeltaPhi_LooseElectron_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron" + extension, "DeltaR_AK4Jet_LooseElectron", 30, 0.0, 6.0 
            ),
            "DeltaR_AK4Jet_LooseElectron",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_0" + extension, "DeltaR_AK4Jet_LooseElectron_0", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_1" + extension, "DeltaR_AK4Jet_LooseElectron_1", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_2" + extension, "DeltaR_AK4Jet_LooseElectron_2", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[2]",
            selection,
            label,
        ),

    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_lep_CR_ttbarMu(data=None):
    label = "#scale[0.8]{t#bar{t} control region (mu)}"
    extension = "_lep_CR_ttbarMu"
    selection = generalselection
    selection += "*(N_BTagsM>=1 && N_BTagsL>=2)"
    selection += "*(N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu27_vX==1)"

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
                "DeltaPhi_AK4Jet_MET_0" + extension, "DeltaPhi_AK4Jet_MET_0", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_1" + extension, "DeltaPhi_AK4Jet_MET_1", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_2" + extension, "DeltaPhi_AK4Jet_MET_2", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[2]",
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
            ROOT.TH1D("Jet_NHF" + extension, "AK4 Jet NHF", 20, 0, 1.),
            "Jet_NHF",
            selection,
        label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CHF" + extension, "AK4 Jet CHF", 20, 0, 1.),
            "Jet_CHF",
            selection,
        label,
        ),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_NEMF" + extension, "AK4 Jet NEMF", 20, 0, 1.),
        #    "Jet_NEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_CEMF" + extension, "AK4 Jet CEMF", 20, 0, 1.),
        #    "Jet_CEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_MF" + extension, "AK4 Jet MF", 20, 0, 1.),
        #    "Jet_MF",
        #    selection,
        #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            #"Weight_TopPt",
            #selection,
            #label,
        #),
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
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_LooseMuon_MET" + extension, "DeltaPhi_LooseMuon_MET", 30, 0.0, 3.14
            ),
            "DeltaPhi_LooseMuon_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon" + extension, "DeltaR_AK4Jet_LooseMuon", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_0" + extension, "DeltaR_AK4Jet_LooseMuon_0", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_1" + extension, "DeltaR_AK4Jet_LooseMuon_1", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_2" + extension, "DeltaR_AK4Jet_LooseMuon_2", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[2]",
            selection,
            label,
        ),

    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_lep_CR_WEl(data=None):
    label = "#scale[0.8]{W control region (e)}"
    extension = "_lep_CR_WEl"
    selection = generalselection
    selection += "*(N_BTagsL==0)"
    selection += "*(N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Photon200_vX==1))"

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
                "DeltaPhi_AK4Jet_MET_0" + extension, "DeltaPhi_AK4Jet_MET_0", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_1" + extension, "DeltaPhi_AK4Jet_MET_1", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_2" + extension, "DeltaPhi_AK4Jet_MET_2", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[2]",
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
            ROOT.TH1D("Jet_NHF" + extension, "AK4 Jet NHF", 20, 0, 1.),
            "Jet_NHF",
            selection,
        label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CHF" + extension, "AK4 Jet CHF", 20, 0, 1.),
            "Jet_CHF",
            selection,
        label,
        ),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_NEMF" + extension, "AK4 Jet NEMF", 20, 0, 1.),
        #    "Jet_NEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_CEMF" + extension, "AK4 Jet CEMF", 20, 0, 1.),
        #    "Jet_CEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_MF" + extension, "AK4 Jet MF", 20, 0, 1.),
        #    "Jet_MF",
        #    selection,
        #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            #"Weight_TopPt",
            #selection,
            #label,
        #),
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
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_LooseElectron_MET" + extension, "DeltaPhi_LooseElectron_MET", 30, 0.0, 3.14
            ),
            "DeltaPhi_LooseElectron_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron" + extension, "DeltaR_AK4Jet_LooseElectron", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_0" + extension, "DeltaR_AK4Jet_LooseElectron_0", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_1" + extension, "DeltaR_AK4Jet_LooseElectron_1", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_2" + extension, "DeltaR_AK4Jet_LooseElectron_2", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[2]",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_lep_CR_WMu(data=None):
    label = "#scale[0.8]{W control region (mu)}"
    extension = "_lep_CR_WMu"
    selection = generalselection
    selection += "*(N_BTagsL==0)"
    selection += "*(N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu27_vX==1)"

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
                "DeltaPhi_AK4Jet_MET_0" + extension, "DeltaPhi_AK4Jet_MET_0", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_1" + extension, "DeltaPhi_AK4Jet_MET_1", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_2" + extension, "DeltaPhi_AK4Jet_MET_2", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[2]",
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
            ROOT.TH1D("Jet_NHF" + extension, "AK4 Jet NHF", 20, 0, 1.),
            "Jet_NHF",
            selection,
        label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CHF" + extension, "AK4 Jet CHF", 20, 0, 1.),
            "Jet_CHF",
            selection,
        label,
        ),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_NEMF" + extension, "AK4 Jet NEMF", 20, 0, 1.),
        #    "Jet_NEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_CEMF" + extension, "AK4 Jet CEMF", 20, 0, 1.),
        #    "Jet_CEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_MF" + extension, "AK4 Jet MF", 20, 0, 1.),
        #    "Jet_MF",
        #    selection,
        #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            #"Weight_TopPt",
            #selection,
            #label,
        #),
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
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_LooseMuon_MET" + extension, "DeltaPhi_LooseMuon_MET", 30, 0.0, 3.14
            ),
            "DeltaPhi_LooseMuon_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon" + extension, "DeltaR_AK4Jet_LooseMuon", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_0" + extension, "DeltaR_AK4Jet_LooseMuon_0", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_1" + extension, "DeltaR_AK4Jet_LooseMuon_1", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_2" + extension, "DeltaR_AK4Jet_LooseMuon_2", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[2]",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_lep_SR_El(data=None):
    label = "#scale[0.8]{signal region (e)}"
    extension = "_lep_SR_El"
    selection = generalselection
    selection += "*(N_BTagsM==1 && N_BTagsL==1)"
    selection += "*(N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Photon200_vX==1))"

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
                "DeltaPhi_AK4Jet_MET_0" + extension, "DeltaPhi_AK4Jet_MET_0", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_1" + extension, "DeltaPhi_AK4Jet_MET_1", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_2" + extension, "DeltaPhi_AK4Jet_MET_2", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[2]",
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
            ROOT.TH1D("Jet_NHF" + extension, "AK4 Jet NHF", 20, 0, 1.),
            "Jet_NHF",
            selection,
        label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CHF" + extension, "AK4 Jet CHF", 20, 0, 1.),
            "Jet_CHF",
            selection,
        label,
        ),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_NEMF" + extension, "AK4 Jet NEMF", 20, 0, 1.),
        #    "Jet_NEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_CEMF" + extension, "AK4 Jet CEMF", 20, 0, 1.),
        #    "Jet_CEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_MF" + extension, "AK4 Jet MF", 20, 0, 1.),
        #    "Jet_MF",
        #    selection,
        #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            #"Weight_TopPt",
            #selection,
            #label,
        #),
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
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_LooseElectron_MET" + extension, "DeltaPhi_LooseElectron_MET", 30, 0.0, 3.14
            ),
            "DeltaPhi_LooseElectron_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron" + extension, "DeltaR_AK4Jet_LooseElectron", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_0" + extension, "DeltaR_AK4Jet_LooseElectron_0", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_1" + extension, "DeltaR_AK4Jet_LooseElectron_1", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_2" + extension, "DeltaR_AK4Jet_LooseElectron_2", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[2]",
            selection,
            label,
        ),
    ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_lep_SR_Mu(data=None):
    label = "#scale[0.8]{signal region (mu)}"
    extension = "_lep_SR_Mu"
    selection = generalselection
    selection += "*(N_BTagsM==1 && N_BTagsL==1)"
    selection += "*(N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu27_vX==1)"

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
                "DeltaPhi_AK4Jet_MET_0" + extension, "DeltaPhi_AK4Jet_MET_0", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_1" + extension, "DeltaPhi_AK4Jet_MET_1", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_2" + extension, "DeltaPhi_AK4Jet_MET_2", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET[2]",
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
            ROOT.TH1D("Jet_NHF" + extension, "AK4 Jet NHF", 20, 0, 1.),
            "Jet_NHF",
            selection,
        label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CHF" + extension, "AK4 Jet CHF", 20, 0, 1.),
            "Jet_CHF",
            selection,
        label,
        ),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_NEMF" + extension, "AK4 Jet NEMF", 20, 0, 1.),
        #    "Jet_NEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_CEMF" + extension, "AK4 Jet CEMF", 20, 0, 1.),
        #    "Jet_CEMF",
        #    selection,
        #label,
        #),
        #plotClasses.Plot(
        #    ROOT.TH1D("Jet_MF" + extension, "AK4 Jet MF", 20, 0, 1.),
        #    "Jet_MF",
        #    selection,
        #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            #"Weight_TopPt",
            #selection,
            #label,
        #),
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
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_LooseMuon_MET" + extension, "DeltaPhi_LooseMuon_MET", 30, 0.0, 3.14
            ),
            "DeltaPhi_LooseMuon_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon" + extension, "DeltaR_AK4Jet_LooseMuon", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_0" + extension, "DeltaR_AK4Jet_LooseMuon_0", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_1" + extension, "DeltaR_AK4Jet_LooseMuon_1", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_2" + extension, "DeltaR_AK4Jet_LooseMuon_2", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[2]",
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
    selection += "*((N_LooseMuons==2 && N_TightMuons>=1 && N_LooseElectrons==0 && Triggered_HLT_IsoMu27_vX==1 && (DiMuon_Mass<60 || DiMuon_Mass>120)) || (N_LooseElectrons==2 && N_TightElectrons>=1 && N_LooseMuons==0 && (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Photon200_vX==1) && (DiElectron_Mass<60 || DiElectron_Mass>120)) || (N_LooseMuons==1 && N_LooseElectrons==1 && ((N_TightMuons==1 && Triggered_HLT_IsoMu27_vX==1) || (N_TightElectrons==1 && (Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Photon200_vX==1)))))"
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
        #plotClasses.Plot(
            #ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            #"Weight_TopPt",
            #selection,
            #label,
        #),
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
    discriminatorPlots += control_plots_lep_CR_ttbarEl(data)
    discriminatorPlots += control_plots_lep_CR_ttbarMu(data)
    discriminatorPlots += control_plots_lep_CR_WEl(data)
    discriminatorPlots += control_plots_lep_CR_WMu(data)
    discriminatorPlots += control_plots_lep_SR_El(data)
    discriminatorPlots += control_plots_lep_SR_Mu(data)
    #discriminatorPlots += control_plots_lep_CR_ttbardilep(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
