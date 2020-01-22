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
        #################
        # NJet weights ##


        "selection_hbb:=((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5))",
        "selection_nonhbb:=((abs(GenHiggs_DecProd1_PDGID)!=5 && abs(GenHiggs_DecProd2_PDGID)!=5))",
        "selection_ttsl:=(N_GenTopLep==1)",
        "selection_ttdl:=(N_GenTopLep==2)",
        "selection_ttfh:=(N_GenTopLep==0)",

        "selection_ttbb:=(GenEvt_I_TTPlusBB==3&&GenEvt_I_TTPlusCC==0)",
        "selection_ttb:=(GenEvt_I_TTPlusBB==1&&GenEvt_I_TTPlusCC==0)",
        "selection_tt2b:=(GenEvt_I_TTPlusBB==2&&GenEvt_I_TTPlusCC==0)",
        "selection_tthf:=(GenEvt_I_TTPlusBB>=1&&GenEvt_I_TTPlusCC==0)",
        "selection_ttcc:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==1)",
        "selection_ttlf:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==0)",




        "weight_SF_N_Jets__ttH_bb__btag_NOMINAL:=(((N_Jets==4)*0.970481455326)+((N_Jets==5)*0.962268292904)+((N_Jets==6)*0.956493616104)+((N_Jets==7)*0.950274646282)+((N_Jets==8)*0.935249090195)+((N_Jets>=9)*0.897339820862))",

        "weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL:=(((N_Jets==4)*0.923768460751)+((N_Jets==5)*0.909187436104)+((N_Jets==6)*0.899537801743)+((N_Jets==7)*0.889305531979)+((N_Jets==8)*0.86739128828)+((N_Jets>=9)*0.839902997017))",

        "weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL:=(((N_Jets==4)*0.956253767014)+((N_Jets==5)*0.938967347145)+((N_Jets==6)*0.907697737217)+((N_Jets==7)*0.873156309128)+((N_Jets==8)*0.841914653778)+((N_Jets>=9)*0.806181013584))",

        "weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL:=(((N_Jets==4)*0.899950027466)+((N_Jets==5)*0.861929535866)+((N_Jets==6)*0.832655131817)+((N_Jets==7)*0.808143079281)+((N_Jets==8)*0.782385587692)+((N_Jets>=9)*0.731020450592))",

        "weight_SF_N_Jets__ttbb_4FS_FH__btag_NOMINAL:=(((N_Jets==4)*0.970512211323)+((N_Jets==5)*0.96704107523)+((N_Jets==6)*0.967137515545)+((N_Jets==7)*0.946990668774)+((N_Jets==8)*0.931310713291)+((N_Jets>=9)*0.888953924179))",

        "weight_SF_N_Jets__ttlf_SL__btag_NOMINAL:=(((N_Jets==4)*0.982537746429)+((N_Jets==5)*0.953815460205)+((N_Jets==6)*0.916884481907)+((N_Jets==7)*0.889544725418)+((N_Jets==8)*0.837062060833)+((N_Jets>=9)*0.80877995491))",

        "weight_SF_N_Jets__ttlf_DL__btag_NOMINAL:=(((N_Jets==4)*0.881663143635)+((N_Jets==5)*0.840722262859)+((N_Jets==6)*0.805276632309)+((N_Jets==7)*0.794540822506)+((N_Jets==8)*0.723813295364)+((N_Jets>=9)*0.632046401501))",

        "weight_SF_N_Jets__ttlf_FH__btag_NOMINAL:=(((N_Jets==4)*1.02495276928)+((N_Jets==5)*1.02721893787)+((N_Jets==6)*1.01985883713)+((N_Jets==7)*0.998580396175)+((N_Jets==8)*0.969238340855)+((N_Jets>=9)*0.916663885117))",

        "weight_SF_N_Jets__ttcc_SL__btag_NOMINAL:=(((N_Jets==4)*0.982042789459)+((N_Jets==5)*0.961056947708)+((N_Jets==6)*0.937591254711)+((N_Jets==7)*0.902606189251)+((N_Jets==8)*0.871568977833)+((N_Jets>=9)*0.849099159241))",

        "weight_SF_N_Jets__ttcc_DL__btag_NOMINAL:=(((N_Jets==4)*0.919116318226)+((N_Jets==5)*0.875444710255)+((N_Jets==6)*0.824504375458)+((N_Jets==7)*0.805679142475)+((N_Jets==8)*0.800388813019)+((N_Jets>=9)*0.893658876419))",

        "weight_SF_N_Jets__ttcc_FH__btag_NOMINAL:=(((N_Jets==4)*1.01068091393)+((N_Jets==5)*1.00892996788)+((N_Jets==6)*1.0000667572)+((N_Jets==7)*0.993484854698)+((N_Jets==8)*0.963474154472)+((N_Jets>=9)*0.948463380337))",






        "sf_N_Jets__ttH__btag_NOMINAL:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_NOMINAL)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL))",
        "sf_N_Jets__ttbb__btag_NOMINAL:=((selection_ttdl*selection_tthf*weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL)+(selection_ttsl*selection_tthf*weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL)+(selection_ttfh*selection_tthf*weight_SF_N_Jets__ttbb_4FS_FH__btag_NOMINAL))",
        "sf_N_Jets__ttcc__btag_NOMINAL:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_NOMINAL)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_NOMINAL)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_NOMINAL))",
        "sf_N_Jets__ttlf__btag_NOMINAL:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_NOMINAL)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_NOMINAL)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_NOMINAL))",

        "sf_N_Jets__btag_NOMINAL:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_NOMINAL+sf_N_Jets__ttcc__btag_NOMINAL+sf_N_Jets__ttbb__btag_NOMINAL)+(isTthSample==1)*(sf_N_Jets__ttH__btag_NOMINAL)+(isTTbarSample==0&&isTthSample==0)*(1.))",



    ]
    return addVars
