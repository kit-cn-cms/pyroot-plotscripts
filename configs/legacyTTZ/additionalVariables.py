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

        "RecoZ_Z_M_dev:=abs(dnnZ_ft_RecoZ_Z_M-90.)/20.",
        "RecoZ_Z_M_dev_log:=log(RecoZ_Z_M_dev+1e-10)",
        "RecoZ_Z_M_weird:=RecoZ_Z_M_dev*dnnZ_ft_RecoZ_Z_M",
        "RecoZ_Z_M_weird_log:=log(RecoZ_Z_M_weird+1e-5)",
        "RecoZ_Z_M_weird_v2:=RecoZ_Z_M_dev_log*dnnZ_ft_RecoZ_Z_M",

        "RecoHiggs_H_M_dev:=abs(dnnH_ft_RecoHiggs_H_M-120.)/20.",
        "RecoHiggs_H_M_dev_log:=log(RecoHiggs_H_M_dev+1e-10)",
        "RecoHiggs_H_M_weird:=RecoHiggs_H_M_dev*dnnH_ft_RecoHiggs_H_M",
        "RecoHiggs_H_M_weird_log:=log(RecoHiggs_H_M_weird+1e-5)",
        "RecoHiggs_H_M_weird_v2:=RecoHiggs_H_M_dev_log*dnnH_ft_RecoHiggs_H_M",

        ]

    return addVars
