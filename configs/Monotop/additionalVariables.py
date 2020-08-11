def getAddVars():
    addVars = [
        "Jet_Pt",
        "Muon_Pt",
        "Electron_Pt",
        "Jet_Eta",
        "Muon_Eta",
        "Electron_Eta",
        "Muon_Pt_BeForeRC",
        "Electron_Pt_BeforeRun2Calibration",
        "Electron_Eta_Supercluster",
        "Jet_CSV",
        "Jet_Flav",
        "N_Jets",
        "Jet_E",
        "Jet_Phi",
        "Jet_M",
        # "Evt_Pt_PrimaryLepton:=LooseLepton_Pt[0]",
        # "Evt_E_PrimaryLepton:=LooseLepton_E[0]",
        # "Evt_M_PrimaryLepton:=LooseLepton_M[0]",
        # "Evt_Phi_PrimaryLepton:=LooseLepton_Phi[0]",
        # "Evt_Eta_PrimaryLepton:=LooseLepton_Eta[0]",
        # "Evt_Pt_MET:=Evt_MET_Pt",
        "Weight_CSV",
        "Weight_CSVLFup",
        "Weight_CSVLFdown",
        "Weight_CSVHFup",
        "Weight_CSVHFdown",
        "Weight_CSVHFStats1up",
        "Weight_CSVHFStats1down",
        "Weight_CSVLFStats1down",
        "Weight_CSVHFStats2up",
        "Weight_CSVHFStats2down",
        "Weight_CSVLFStats2up",
        "Weight_CSVLFStats2down",
        "Weight_CSVCErr1down",
        "Weight_CSVCErr2up",
        "Weight_CSVCErr2down",
        "Weight_pu69p2",
        "N_BTagsM",
        # "GenWeight_isr_Def_down:=GenWeight_8",
        # "GenWeight_isr_Def_up:=GenWeight_6",
        # "GenWeight_fsr_Def_down:=GenWeight_9",
        # "GenWeight_fsr_Def_up:=GenWeight_7",
        "BosonWeight_nominal",
        "BosonWeight_QCD1Up",
        "BosonWeight_QCD2Up",
        "BosonWeight_QCD3Up",
        "BosonWeight_QCD1Down",
        "BosonWeight_QCD2Down",
        "BosonWeight_QCD3Down",
        "BosonWeight_EW1Up",
        "BosonWeight_EW2Up",
        "BosonWeight_EW3Up",
        "BosonWeight_EW1Down",
        "BosonWeight_EW2Down",
        "BosonWeight_EW3Down",
        "BosonWeight_MixedUp",
        "BosonWeight_MixedDown",
        "BosonWeight_AlphaUp",
        "BosonWeight_AlphaDown",
        "BosonWeight_muRUp",
        "BosonWeight_muRDown",
        "BosonWeight_muFUp",
        "BosonWeight_muFDown",
        "W_Pt",
        "Z_Pt",
        "Gamma_Pt",
        "DeltaR_AK4Jet_LooseElectron",
        "DeltaR_AK4Jet_LooseMuon",
        "N_Jets",
        "N_LooseElectrons",
        "N_LooseMuons",
        "N_LoosePhotons",
        "DeltaPhi_AK4Jet_MET",
        "DeltaPhi_AK4Jet_Hadr_Recoil",
        "HT_AK4Jets",
        "N_AK15Jets",
        "AK15Jet_Pt",
        "Hadr_Recoil_Pt",
        #"AK15Jet_TopMatched",
        "AK15Jet_Eta",
        "N_GenPVs",
        "LoosePhoton_Phi",
        "Hadr_Recoil_Phi",
        "N_JetsMediumTagged_outside_lead_AK15Jet",
        "JetMediumTagged_outside_lead_AK15Jet_Pt",
        "JetMediumTagged_outside_lead_AK15Jet_Eta",
        "JetMediumTagged_outside_lead_AK15Jet_Flav",
        "JetLooseTagged_outside_lead_AK15Jet_Pt",
        "JetLooseTagged_outside_lead_AK15Jet_Eta",
        "JetLooseTagged_outside_lead_AK15Jet_Flav",

        "N_JetsMediumUntagged_outside_lead_AK15Jet",
        "JetMediumUntagged_outside_lead_AK15Jet_Pt",
        "JetMediumUntagged_outside_lead_AK15Jet_Eta",
        "JetMediumUntagged_outside_lead_AK15Jet_Flav",
        "JetLooseUntagged_outside_lead_AK15Jet_Pt",
        "JetLooseUntagged_outside_lead_AK15Jet_Eta",
        "JetLooseUntagged_outside_lead_AK15Jet_Flav",
       
        "N_JetsLooseTagged_outside_lead_AK15Jet",
        "JetLooseTagged_outside_lead_AK15Jet_Pt",
        "JetLooseTagged_outside_lead_AK15Jet_Eta",
        "JetLooseTagged_outside_lead_AK15Jet_Flav",
        "JetLooseTagged_outside_lead_AK15Jet_Pt",
        "JetLooseTagged_outside_lead_AK15Jet_Eta",
        "JetLooseTagged_outside_lead_AK15Jet_Flav",

        "N_JetsLooseUntagged_outside_lead_AK15Jet",
        "JetLooseUntagged_outside_lead_AK15Jet_Pt",
        "JetLooseUntagged_outside_lead_AK15Jet_Eta",
        "JetLooseUntagged_outside_lead_AK15Jet_Flav",
        "JetLooseUntagged_outside_lead_AK15Jet_Pt",
        "JetLooseUntagged_outside_lead_AK15Jet_Eta",
        "JetLooseUntagged_outside_lead_AK15Jet_Flav",
       
        ]

    return addVars
