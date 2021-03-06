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
        # "Evt_blr_ETH",
        # "Evt_blr_ETH_transformed",
        "njet_corr_CSV_ttH:=(((N_Jets==2)*0.988309581757)+((N_Jets==3)*0.986540359853)+((N_Jets==4)*0.98360406277)+((N_Jets==5)*0.973676528405)+((N_Jets==6)*0.961788960927)+((N_Jets==7)*0.936593321903)+((N_Jets==8)*0.932391402684)+((N_Jets>=9)*0.852955462593))",
        "njet_corr_CSV_others:=(((N_Jets==2)*1.01867411742)+((N_Jets==3)*1.00957297213)+((N_Jets==4)*0.980528837392)+((N_Jets==5)*0.958160887939)+((N_Jets==6)*0.961187304813)+((N_Jets==7)*0.793167148673)+((N_Jets==8)*0.931187544001)+((N_Jets>=9)*0.626016213144))",
        "njet_corr_CSV_ttlf:=(((N_Jets==2)*1.01004894628)+((N_Jets==3)*1.01810161589)+((N_Jets==4)*1.01386105709)+((N_Jets==5)*0.996573860992)+((N_Jets==6)*0.967816926298)+((N_Jets==7)*0.942772861624)+((N_Jets==8)*0.914060021758)+((N_Jets>=9)*0.939194200612))",
        "njet_corr_CSV_tt2b:=(((N_Jets==2)*1.02018533958)+((N_Jets==3)*1.01779685786)+((N_Jets==4)*1.00987345129)+((N_Jets==5)*1.00425030473)+((N_Jets==6)*0.994386027634)+((N_Jets==7)*0.963120255683)+((N_Jets==8)*0.970070241347)+((N_Jets>=9)*1.02234148622))",
        "njet_corr_CSV_ttb:=(((N_Jets==2)*0.991064874474)+((N_Jets==3)*0.9895858216)+((N_Jets==4)*0.984175944207)+((N_Jets==5)*0.965260405432)+((N_Jets==6)*0.933131727265)+((N_Jets==7)*0.923009990283)+((N_Jets==8)*0.855995350025)+((N_Jets>=9)*0.849372161097))",
        "njet_corr_CSV_ttbb:=(((N_Jets==2)*0.998293748366)+((N_Jets==3)*0.987628567101)+((N_Jets==4)*0.984501084389)+((N_Jets==5)*0.98077463045)+((N_Jets==6)*0.949139120293)+((N_Jets==7)*0.910364663192)+((N_Jets==8)*0.93158964452)+((N_Jets>=9)*0.948865586747))",
        "njet_corr_CSV_ttcc:=(((N_Jets==2)*1.00518597259)+((N_Jets==3)*1.00708806494)+((N_Jets==4)*1.00790459899)+((N_Jets==5)*0.993024010763)+((N_Jets==6)*0.973912278049)+((N_Jets==7)*0.942641604953)+((N_Jets==8)*0.952984849492)+((N_Jets>=9)*0.86061414658))",

        "njet_corr_CSV_tthf:=((njet_corr_CSV_ttb*(GenEvt_I_TTPlusBB==1))+(njet_corr_CSV_ttbb*(GenEvt_I_TTPlusBB==3))+(njet_corr_CSV_tt2b*(GenEvt_I_TTPlusBB==2)))",

        ]

    return addVars
