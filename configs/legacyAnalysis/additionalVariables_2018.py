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

        "selection_tthf:=(GenEvt_I_TTPlusBB>=1&&GenEvt_I_TTPlusCC==0)",
        "selection_ttcc:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==1)",
        "selection_ttlf:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==0)",




        "weight_SF_N_Jets__ttH_bb__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.987944662571)+((N_Jets==2)*0.983631968498)+((N_Jets==3)*0.976970016956)+((N_Jets==4)*0.96991199255)+((N_Jets==5)*0.965793609619)+((N_Jets==6)*0.96144080162)+((N_Jets==7)*0.955342948437)+((N_Jets==8)*0.940639138222)+((N_Jets>=9)*0.906148672104))",

        "weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.979229271412)+((N_Jets==2)*0.95835596323)+((N_Jets==3)*0.941134333611)+((N_Jets==4)*0.928279161453)+((N_Jets==5)*0.916184127331)+((N_Jets==6)*0.905698120594)+((N_Jets==7)*0.893927335739)+((N_Jets==8)*0.879107773304)+((N_Jets>=9)*0.846335947514))",

        "weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.984696626663)+((N_Jets==2)*0.976046919823)+((N_Jets==3)*0.968483269215)+((N_Jets==4)*0.957964777946)+((N_Jets==5)*0.939464688301)+((N_Jets==6)*0.913318574429)+((N_Jets==7)*0.886076927185)+((N_Jets==8)*0.855828821659)+((N_Jets>=9)*0.815186977386))",

        "weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.988386750221)+((N_Jets==2)*0.968368291855)+((N_Jets==3)*0.939254999161)+((N_Jets==4)*0.898201704025)+((N_Jets==5)*0.867239177227)+((N_Jets==6)*0.836635291576)+((N_Jets==7)*0.808776140213)+((N_Jets==8)*0.773631095886)+((N_Jets>=9)*0.738255798817))",

        "weight_SF_N_Jets__ttbb_4FS_FH__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.982359170914)+((N_Jets==2)*0.973529160023)+((N_Jets==3)*0.969319880009)+((N_Jets==4)*0.971303761005)+((N_Jets==5)*0.97164106369)+((N_Jets==6)*0.967205941677)+((N_Jets==7)*0.95445817709)+((N_Jets==8)*0.934999644756)+((N_Jets>=9)*0.896767854691))",

        "weight_SF_N_Jets__ttlf_SL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.998926758766)+((N_Jets==2)*1.00131475925)+((N_Jets==3)*1.00113630295)+((N_Jets==4)*0.987345576286)+((N_Jets==5)*0.958571255207)+((N_Jets==6)*0.926406800747)+((N_Jets==7)*0.894873797894)+((N_Jets==8)*0.853602707386)+((N_Jets>=9)*0.803937494755))",

        "weight_SF_N_Jets__ttlf_DL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.990425229073)+((N_Jets==2)*0.968368649483)+((N_Jets==3)*0.920110404491)+((N_Jets==4)*0.884227454662)+((N_Jets==5)*0.851005911827)+((N_Jets==6)*0.815002679825)+((N_Jets==7)*0.785849571228)+((N_Jets==8)*0.745138525963)+((N_Jets>=9)*0.690179049969))",

        "weight_SF_N_Jets__ttlf_FH__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*1.00115025043)+((N_Jets==2)*1.00643789768)+((N_Jets==3)*1.01712059975)+((N_Jets==4)*1.02871286869)+((N_Jets==5)*1.03414750099)+((N_Jets==6)*1.02775597572)+((N_Jets==7)*1.00635373592)+((N_Jets==8)*0.979930400848)+((N_Jets>=9)*0.93187636137))",

        "weight_SF_N_Jets__ttcc_SL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.999156951904)+((N_Jets==2)*0.995605587959)+((N_Jets==3)*0.992774605751)+((N_Jets==4)*0.98462665081)+((N_Jets==5)*0.967760384083)+((N_Jets==6)*0.939565718174)+((N_Jets==7)*0.914899647236)+((N_Jets==8)*0.88917952776)+((N_Jets>=9)*0.848915874958))",

        "weight_SF_N_Jets__ttcc_DL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.993640065193)+((N_Jets==2)*0.979560494423)+((N_Jets==3)*0.953917443752)+((N_Jets==4)*0.920010626316)+((N_Jets==5)*0.885033488274)+((N_Jets==6)*0.846443235874)+((N_Jets==7)*0.807622611523)+((N_Jets==8)*0.788562119007)+((N_Jets>=9)*0.74731618166))",

        "weight_SF_N_Jets__ttcc_FH__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.997326254845)+((N_Jets==2)*0.996948957443)+((N_Jets==3)*1.00287139416)+((N_Jets==4)*1.01527678967)+((N_Jets==5)*1.01272332668)+((N_Jets==6)*1.01043140888)+((N_Jets==7)*0.997365355492)+((N_Jets==8)*0.969473421574)+((N_Jets>=9)*0.941547572613))",






        "sf_N_Jets__ttH__btag_NOMINAL:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_NOMINAL)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL))",
        "sf_N_Jets__ttbb__btag_NOMINAL:=((selection_ttdl*selection_tthf*weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL)+(selection_ttsl*selection_tthf*weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL)+(selection_ttfh*selection_tthf*weight_SF_N_Jets__ttbb_4FS_FH__btag_NOMINAL))",
        "sf_N_Jets__ttcc__btag_NOMINAL:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_NOMINAL)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_NOMINAL)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_NOMINAL))",
        "sf_N_Jets__ttlf__btag_NOMINAL:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_NOMINAL)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_NOMINAL)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_NOMINAL))",

        "sf_N_Jets__btag_NOMINAL:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_NOMINAL+sf_N_Jets__ttcc__btag_NOMINAL+sf_N_Jets__ttbb__btag_NOMINAL)+(isTthSample==1)*(sf_N_Jets__ttH__btag_NOMINAL)+(isTTbarSample==0&&isTthSample==0)*(1.))",





    ]
    return addVars
