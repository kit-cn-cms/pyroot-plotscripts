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
        "Evt_Pt_PrimaryLepton:=LooseLepton_Pt[0]",
        "Evt_E_PrimaryLepton:=LooseLepton_E[0]",
        "Evt_M_PrimaryLepton:=LooseLepton_M[0]",
        "Evt_Phi_PrimaryLepton:=LooseLepton_Phi[0]",
        "Evt_Eta_PrimaryLepton:=LooseLepton_Eta[0]",
        "Evt_MET_Pt",
        "N_GenTopLep",
        "GenHiggs_DecProd1_PDGID",
        ]

    return addVars
