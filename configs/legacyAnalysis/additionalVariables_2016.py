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
        #################


        "selection_hbb:=((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5))",
        "selection_nonhbb:=((abs(GenHiggs_DecProd1_PDGID)!=5 && abs(GenHiggs_DecProd2_PDGID)!=5))",
        "selection_ttsl:=(N_GenTopLep==1)",
        "selection_ttdl:=(N_GenTopLep==2)",
        "selection_ttfh:=(N_GenTopLep==0)",

        "selection_tthf:=(GenEvt_I_TTPlusBB>=1&&GenEvt_I_TTPlusCC==0)",
        "selection_ttcc:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==1)",
        "selection_ttlf:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==0)",




        "weight_SF_N_Jets__ttH_bb__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.982494771481)+((N_Jets==2)*0.982300698757)+((N_Jets==3)*0.984105169773)+((N_Jets==4)*0.98446816206)+((N_Jets==5)*0.983937501907)+((N_Jets==6)*0.982140183449)+((N_Jets==7)*0.978164792061)+((N_Jets==8)*0.971113085747)+((N_Jets>=9)*0.955243468285))",

        "weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.986445188522)+((N_Jets==2)*0.981625318527)+((N_Jets==3)*0.977841675282)+((N_Jets==4)*0.973282277584)+((N_Jets==5)*0.96854943037)+((N_Jets==6)*0.962581634521)+((N_Jets==7)*0.955457091331)+((N_Jets==8)*0.946955680847)+((N_Jets>=9)*0.931564331055))",

        "weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.98113411665)+((N_Jets==2)*0.973539292812)+((N_Jets==3)*0.969055652618)+((N_Jets==4)*0.965047955513)+((N_Jets==5)*0.960202157497)+((N_Jets==6)*0.951478362083)+((N_Jets==7)*0.941661596298)+((N_Jets==8)*0.929684400558)+((N_Jets>=9)*0.912008106709))",

        "weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.990555524826)+((N_Jets==2)*0.981050610542)+((N_Jets==3)*0.969926655293)+((N_Jets==4)*0.958970069885)+((N_Jets==5)*0.94923889637)+((N_Jets==6)*0.936845242977)+((N_Jets==7)*0.927608847618)+((N_Jets==8)*0.910140275955)+((N_Jets>=9)*0.886935412884))",

        "weight_SF_N_Jets__ttlf_SL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.991251349449)+((N_Jets==2)*0.993392527103)+((N_Jets==3)*0.99547547102)+((N_Jets==4)*0.992564558983)+((N_Jets==5)*0.983659446239)+((N_Jets==6)*0.973386108875)+((N_Jets==7)*0.95909267664)+((N_Jets==8)*0.940494179726)+((N_Jets>=9)*0.921710908413))",

        "weight_SF_N_Jets__ttlf_DL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.994752705097)+((N_Jets==2)*0.989726424217)+((N_Jets==3)*0.980377614498)+((N_Jets==4)*0.969927966595)+((N_Jets==5)*0.958158373833)+((N_Jets==6)*0.944619834423)+((N_Jets==7)*0.928691506386)+((N_Jets==8)*0.909633100033)+((N_Jets>=9)*0.887500941753))",

        "weight_SF_N_Jets__ttlf_FH__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.988212883472)+((N_Jets==2)*0.990465700626)+((N_Jets==3)*0.994249284267)+((N_Jets==4)*0.998134672642)+((N_Jets==5)*0.999131202698)+((N_Jets==6)*0.99506098032)+((N_Jets==7)*0.984604120255)+((N_Jets==8)*0.972359478474)+((N_Jets>=9)*0.952823519707))",

        "weight_SF_N_Jets__ttcc_SL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.994210422039)+((N_Jets==2)*0.993563950062)+((N_Jets==3)*0.994744062424)+((N_Jets==4)*0.992002487183)+((N_Jets==5)*0.986479520798)+((N_Jets==6)*0.976410210133)+((N_Jets==7)*0.96356344223)+((N_Jets==8)*0.952506363392)+((N_Jets>=9)*0.931370913982))",

        "weight_SF_N_Jets__ttcc_DL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.996512711048)+((N_Jets==2)*0.993187069893)+((N_Jets==3)*0.988283991814)+((N_Jets==4)*0.97943520546)+((N_Jets==5)*0.968304812908)+((N_Jets==6)*0.954210877419)+((N_Jets==7)*0.943681657314)+((N_Jets==8)*0.930189013481)+((N_Jets>=9)*0.90473729372))",

        "weight_SF_N_Jets__ttcc_FH__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.987637758255)+((N_Jets==2)*0.991748988628)+((N_Jets==3)*0.992637097836)+((N_Jets==4)*0.99407595396)+((N_Jets==5)*0.994823038578)+((N_Jets==6)*0.990967512131)+((N_Jets==7)*0.983588337898)+((N_Jets==8)*0.974810242653)+((N_Jets>=9)*0.954049825668))",






        "sf_N_Jets__ttH__btag_NOMINAL:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_NOMINAL)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL))",
        "sf_N_Jets__ttbb__btag_NOMINAL:=((selection_ttdl*selection_tthf*weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL)+(selection_ttsl*selection_tthf*weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL))",
        "sf_N_Jets__ttcc__btag_NOMINAL:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_NOMINAL)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_NOMINAL)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_NOMINAL))",
        "sf_N_Jets__ttlf__btag_NOMINAL:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_NOMINAL)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_NOMINAL)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_NOMINAL))",

        "sf_N_Jets__btag_NOMINAL:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_NOMINAL+sf_N_Jets__ttcc__btag_NOMINAL+sf_N_Jets__ttbb__btag_NOMINAL)+(isTthSample==1)*(sf_N_Jets__ttH__btag_NOMINAL)+(isTTbarSample==0&&isTthSample==0)*(1.))",







    ]

    return addVars
