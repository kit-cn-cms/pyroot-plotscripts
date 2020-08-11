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

fast = False

def GetPlots(extension, selection, label):
    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "#slash{E}_{T} [GeV]", 50, 0.0, 1000.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "#phi(#slash{E}_{T})", 32, -3.2, 3.2),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo #slash{E}_{T} [GeV]", 50, 0.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "|Calo #slash{E}_{T} - #slash{E}_{T}|/Calo #slash{E}_{T}", 50, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"CaloMET_Hadr_Recoil_ratio" + extension,
                #"CaloMET_Hadr_Recoil_ratio",
                #25,
                #0.0,
                #10.0,
            #),
            #"CaloMET_Hadr_Recoil_ratio",
            #selection,
            #label,
        #),
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
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Hadr_Recoil_Pt" + extension, "Hadronic Recoil", 40, 200.0, 1200.0
            #),
            #"Hadr_Recoil_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Hadr_Recoil_Phi" + extension, "Hadronic Recoil #phi", 30, -3.14, 3.14
            #),
            #"Hadr_Recoil_Phi",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "#Delta#phi(AK4 Jet, #slash{E}_{T})", 32, 0.0, 3.2
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_0" + extension, "#Delta#phi(AK4 Jet 0, #slash{E}_{T})", 32, 0.0, 3.2
            ),
            "DeltaPhi_AK4Jet_MET[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_1" + extension, "#Delta#phi(AK4 Jet 1, #slash{E}_{T})", 32, 0.0, 3.2
            ),
            "DeltaPhi_AK4Jet_MET[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET_2" + extension, "#Delta#phi(AK4 Jet 2, #slash{E}_{T})", 32, 0.0, 3.2
            ),
            "DeltaPhi_AK4Jet_MET[2]",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
                #"DeltaPhi_AK4Jet_Hadr_Recoil",
                #30,
                #0.0,
                #3.14,
            #),
            #"DeltaPhi_AK4Jet_Hadr_Recoil",
            #selection,
            #label,
        #),
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
                "Electron_Pt" + extension, "Tight Electron p_{T} [GeV]", 30, 10.0, 610.0
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
                "Electron_Phi" + extension, "Tight Electron #phi", 32, -3.2, 3.2
            ),
            "Electron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{T} [GeV]", 30, 10.0, 610.0),
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
            ROOT.TH1D("Muon_Phi" + extension, "Tight Muon #phi", 32, -3.2, 3.2),
            "Muon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet p_{T} [GeV]", 49, 20, 1000),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet p_{T} [GeV]", 24, 20, 500),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet p_{T} [GeV]", 14, 20, 300
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
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 32, -3.2, 3.2),
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
        plotClasses.Plot(
            ROOT.TH1D("Jet_NHF_0" + extension, "leading AK4 Jet NHF", 40, 0, 1.),
            "Jet_NHF[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CHF_0" + extension, "leading AK4 Jet CHF", 40, 0, 1.),
            "Jet_CHF[0]",
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
            ROOT.TH1D("M_W_transverse" + extension, "m_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)),
            "M_W_transverse",
            selection,
            label,
        ),
        plotClasses.Plot(
                ROOT.TH1D("M_W_transverse_generic_binning" + extension, "m_{T} [GeV]", 40, 40, 440),
                "M_W_transverse",
                selection,
                label,
        ),
        plotClasses.Plot(
                ROOT.TH1D("M_W_transverse_binning_studies" + extension, "m_{T} [GeV]", 192, 40, 1000),
                "M_W_transverse",
                selection,
                label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_LooseElectron_MET" + extension, "#Delta#phi(e, #slash{E}_{T})", 32, 0.0, 3.2
            ),
            "DeltaPhi_LooseElectron_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron" + extension, "#DeltaR(AK4 jet, e)", 30, 0.0, 6.0 
            ),
            "DeltaR_AK4Jet_LooseElectron",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_0" + extension, "#DeltaR(e, AK4 Jet 0)", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_1" + extension, "#DeltaR(e, AK4 Jet 1)", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseElectron_2" + extension, "#DeltaR(e, AK4 Jet 2)", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseElectron[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_LooseMuon_MET" + extension, "#Delta#phi(#mu, #slash{E}_{T})", 32, 0.0, 3.2
            ),
            "DeltaPhi_LooseMuon_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon" + extension, "#DeltaR(#mu, AK4 Jet)", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_0" + extension, "#DeltaR(#mu 0, AK4 Jet)", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_1" + extension, "#DeltaR(#mu 1, AK4 Jet)", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK4Jet_LooseMuon_2" + extension, "#DeltaR(#mu 2, AK4 Jet)", 30, 0.0, 6.0
            ),
            "DeltaR_AK4Jet_LooseMuon[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "H_T" + extension, "H_{T} [GeV]", 50, 0, 1000
            ),
            "HT_AK4Jets",
            selection,
            label,
        ),
    ]
    if fast:
        plots = [
            plotClasses.Plot(
                ROOT.TH1D("M_W_transverse" + extension, "m_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)),
                "M_W_transverse",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("M_W_transverse_generic_binning" + extension, "m_{T} [GeV]", 40, 40, 440),
                "M_W_transverse",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("M_W_transverse_binning_studies" + extension, "m_{T} [GeV]", 192, 40, 1000),
                "M_W_transverse",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("Evt_Pt_MET" + extension, "#slash{E}_{T} [GeV]", 50, 0.0, 1000.0),
                "Evt_Pt_MET",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet p_{T} [GeV]", 49, 20, 1000),
                "Jet_Pt[0]",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                    "DeltaPhi_AK4Jet_MET_0" + extension, "#Delta#phi(AK4 Jet 0, #slash{E}_{T})", 32, 0.0, 3.2
                ),
                "DeltaPhi_AK4Jet_MET[0]",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                    "DeltaR_AK4Jet_LooseElectron_0" + extension, "#DeltaR(e, AK4 Jet 0)", 30, 0.0, 6.0
                ),
                "DeltaR_AK4Jet_LooseElectron[0]",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                    "Electron_Pt" + extension, "Tight Electron p_{T} [GeV]", 30, 10.0, 610.0
                ),
                "Electron_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{T} [GeV]", 30, 10.0, 610.0),
                "Muon_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
            )
        ]
            
    return plots
    

#discr_binning = [0+(2*i) for i in range(150)]
#discr_binning += [300+(5*i) for i in range(80)]
#discr_binning += [700+(10*i) for i in range(31)]
#discr_binning = [100.0, 102.0, 106.0, 110.0, 114.0, 118.0, 122.0, 126.0, 130.0, 134.0, 138.0, 142.0, 146.0,
#discr_binning = [150.0, 154.0, 158.0, 162.0, 166.0, 170.0, 174.0, 178.0, 182.0, 186.0, 190.0, 194.0, 198.0, 202.0, 206.0, 210.0, 214.0, 218.0, 224.0, 230.0, 236.0, 242.0, 248.0, 254.0, 262.0, 270.0, 278.0, 288.0, 298.0, 315.0, 335.0, 360.0, 395.0, 465.0]
# discr_binning = [150.0, 165.0, 180.0, 200.0, 220.0, 240.0, 270.0, 310.0, 350.0, 500.0]
discr_binning = [40.0,60.0,80.0,100.0,125.0,150.0, 165.0, 180.0, 200.0, 220.0, 240.0, 270.0, 310.0, 350.0, 500.0]
discr_binning.append(1000.)

# met + no photons + "highly" energetic jet 
generalselection = "(Evt_Pt_MET>100.)*(N_LoosePhotons==0)*(Jet_Pt[0]>50.)"

# HEM jet veto
#generalselection += "*(N_HEM_Jets==0)"#"*(N_HEM_METS==0)"

# only interested in range of higher transverse masses
generalselection += "*(M_W_transverse[0]>=40.)"

# leading jet and met should be approximately back-to-back
# also modeling in the vetoed region is not great
generalselection += "*(DeltaPhi_AK4Jet_MET[0]>1.5)"

def control_plots_lep_CR_ttbarEl(data=None):
    label = "#scale[0.8]{t#bar{t} control region (e)}"
    extension = "_lep_CR_ttbarEl"
    
    selection = generalselection
    
    # btagging requirement to enrich ttbar
    selection += "*(N_BTagsM>=2)"
    
    # single electron requirement
    selection += "*(N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0)"
    
    # single electron trigger requirement
    selection += "*(Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Photon200_vX==1 || Triggered_HLT_Ele115_CaloIdVT_GsfTrkIdT_vX==1)"
    
    # no great modeling in the regions with large deltaR between leptons and jets
    #selection += "*(DeltaR_AK4Jet_LooseElectron[0]<3.4)"
    selection += "*(DeltaR_AK4Jets_LooseElectron_Smaller_3p4)"

    plots = GetPlots(extension, selection, label)
    
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_lep_CR_ttbarMu(data=None):
    label = "#scale[0.8]{t#bar{t} control region (mu)}"
    extension = "_lep_CR_ttbarMu"
    
    selection = generalselection
    
    # btagging requirement to enrich ttbar
    selection += "*(N_BTagsM>=2)"
    
    # single muon requirement
    selection += "*(N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0)"
    
    # single muon trigger requirement
    selection += "*(Triggered_HLT_IsoMu27_vX==1)"
    
    # no great modeling in the regions with large deltaR between leptons and jets
    #selection += "*(DeltaR_AK4Jet_LooseMuon[0]<3.4)"
    selection += "*(DeltaR_AK4Jets_LooseMuon_Smaller_3p4)"

    plots = GetPlots(extension, selection, label)
    
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_lep_CR_WEl(data=None):
    label = "#scale[0.8]{W control region (e)}"
    extension = "_lep_CR_WEl"
    
    selection = generalselection
    
    # btagging requirement to enrich w+jets
    selection += "*(N_BTagsM==0)"
    
    # single electron requirement
    selection += "*(N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0)"
    
    # single electron trigger requirement
    selection += "*(Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Photon200_vX==1 || Triggered_HLT_Ele115_CaloIdVT_GsfTrkIdT_vX==1)"
    
    # no great modeling in the regions with large deltaR between leptons and jets
    #selection += "*(DeltaR_AK4Jet_LooseElectron[0]<3.4)"
    selection += "*(DeltaR_AK4Jets_LooseElectron_Smaller_3p4)"

    plots = GetPlots(extension, selection, label)
    
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_lep_CR_WMu(data=None):
    label = "#scale[0.8]{W control region (mu)}"
    extension = "_lep_CR_WMu"
    selection = generalselection
    
    # btagging requirement to enrich w+jets
    selection += "*(N_BTagsM==0)"
    
    # single muon requirement
    selection += "*(N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0)"
    
    # single muon trigger requirement
    selection += "*(Triggered_HLT_IsoMu27_vX==1)"
    
    # no great modeling in the regions with large deltaR between leptons and jets
    #selection += "*(DeltaR_AK4Jet_LooseMuon[0]<3.4)"
    selection += "*(DeltaR_AK4Jets_LooseMuon_Smaller_3p4)"

    plots = GetPlots(extension, selection, label)
    
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_lep_SR_El(data=None):
    label = "#scale[0.8]{signal region (e)}"
    extension = "_lep_SR_El"
    
    selection = generalselection
    
    # btagging requirement to enrich signal
    selection += "*(N_BTagsM==1)"
    
    # single electron requirement
    selection += "*(N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0)"
    
    # single electron trigger requirement
    selection += "*(Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Photon200_vX==1 || Triggered_HLT_Ele115_CaloIdVT_GsfTrkIdT_vX==1)"
    
    # no great modeling in the regions with large deltaR between leptons and jets
    #selection += "*(DeltaR_AK4Jet_LooseElectron[0]<3.4)"
    selection += "*(DeltaR_AK4Jets_LooseElectron_Smaller_3p4)"

    plots = GetPlots(extension, selection, label)
    
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_lep_SR_Mu(data=None):
    label = "#scale[0.8]{signal region (mu)}"
    extension = "_lep_SR_Mu"
    
    selection = generalselection
    
    # btagging requirement to enrich signal
    selection += "*(N_BTagsM==1)"
    
    # single muon requirement
    selection += "*(N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0)"
    
    # single muon trigger requirement
    selection += "*(Triggered_HLT_IsoMu27_vX==1)"
    
    # no great modeling in the regions with large deltaR between leptons and jets
    #selection += "*(DeltaR_AK4Jet_LooseMuon[0]<3.4)"
    selection += "*(DeltaR_AK4Jets_LooseMuon_Smaller_3p4)"

    plots = GetPlots(extension, selection, label)
    
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_lep_CR_inclEl(data=None):
    label = "#scale[0.8]{inclusive control region (e)}"
    extension = "_lep_CR_inclEl"
    
    selection = generalselection
    
    # no btagging requirement to get w+jets, ttbar, and signal in one region which can be used to look in data
    
    # single electron requirement
    selection += "*(N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0)"
    
    # single electron trigger requirement
    selection += "*(Triggered_HLT_Ele35_WPTight_Gsf_vX==1 || Triggered_HLT_Photon200_vX==1 || Triggered_HLT_Ele115_CaloIdVT_GsfTrkIdT_vX==1)"
    
    # no great modeling in the regions with large deltaR between leptons and jets
    #selection += "*(DeltaR_AK4Jet_LooseElectron[0]<3.4)"
    selection += "*(DeltaR_AK4Jets_LooseElectron_Smaller_3p4)"

    plots = GetPlots(extension, selection, label)
    
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_lep_CR_inclMu(data=None):
    label = "#scale[0.8]{inclusive control region (mu)}"
    extension = "_lep_CR_inclMu"
    
    selection = generalselection
    
    # no btagging requirement to get w+jets, ttbar, and signal in one region which can be used to look in data
    
    # single muon requirement
    selection += "*(N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0)"
    
    # single muon trigger requirement
    selection += "*(Triggered_HLT_IsoMu27_vX==1)"
    
    # no great modeling in the regions with large deltaR between leptons and jets
    #selection += "*(DeltaR_AK4Jet_LooseMuon[0]<3.4)"
    selection += "*(DeltaR_AK4Jets_LooseMuon_Smaller_3p4)"

    plots = GetPlots(extension, selection, label)
    
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
    #discriminatorPlots += control_plots_lep_CR_inclEl(data)
    #discriminatorPlots += control_plots_lep_CR_inclMu(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
