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
        #################a



        "selection_hbb:=((abs(GenHiggs_DecProd1_PDGID)==5 && abs(GenHiggs_DecProd2_PDGID)==5))",
        "selection_nonhbb:=((abs(GenHiggs_DecProd1_PDGID)!=5 && abs(GenHiggs_DecProd2_PDGID)!=5))",
        "selection_ttsl:=(N_GenTopLep==1)",
        "selection_ttdl:=(N_GenTopLep==2)",
        "selection_ttfh:=(N_GenTopLep==0)",

        "selection_tthf:=(GenEvt_I_TTPlusBB>=1&&GenEvt_I_TTPlusCC==0)",
        "selection_ttcc:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==1)",
        "selection_ttlf:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==0)",




        "weight_SF_N_Jets__ttH_bb__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.988865554333)+((N_Jets==2)*0.98002165556)+((N_Jets==3)*0.971673905849)+((N_Jets==4)*0.962099432945)+((N_Jets==5)*0.95226585865)+((N_Jets==6)*0.937746465206)+((N_Jets==7)*0.92169046402)+((N_Jets==8)*0.896255970001)+((N_Jets>=9)*0.843837320805))",

        "weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.978429436684)+((N_Jets==2)*0.957885921001)+((N_Jets==3)*0.934980869293)+((N_Jets==4)*0.91484940052)+((N_Jets==5)*0.895789206028)+((N_Jets==6)*0.87344032526)+((N_Jets==7)*0.851209819317)+((N_Jets==8)*0.823339760303)+((N_Jets>=9)*0.775687158108))",

        "weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.981049537659)+((N_Jets==2)*0.969747900963)+((N_Jets==3)*0.957269132137)+((N_Jets==4)*0.944093763828)+((N_Jets==5)*0.92059212923)+((N_Jets==6)*0.890409171581)+((N_Jets==7)*0.852391302586)+((N_Jets==8)*0.816106796265)+((N_Jets>=9)*0.757650673389))",

        "weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.987284004688)+((N_Jets==2)*0.967817366123)+((N_Jets==3)*0.939659535885)+((N_Jets==4)*0.899817109108)+((N_Jets==5)*0.862267076969)+((N_Jets==6)*0.826346516609)+((N_Jets==7)*0.789233386517)+((N_Jets==8)*0.753079116344)+((N_Jets>=9)*0.68210542202))",

        "weight_SF_N_Jets__ttbb_4FS_FH__btag_NOMINAL:=(((N_Jets==0)*0.0)+((N_Jets==1)*0.0)+((N_Jets==2)*0.0)+((N_Jets==3)*0.0)+((N_Jets==4)*0.0)+((N_Jets==5)*0.0)+((N_Jets==6)*0.0)+((N_Jets==7)*0.0)+((N_Jets==8)*0.0)+((N_Jets>=9)*0.0))",

        "weight_SF_N_Jets__ttlf_SL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.995147883892)+((N_Jets==2)*0.99578422308)+((N_Jets==3)*0.993053197861)+((N_Jets==4)*0.975041747093)+((N_Jets==5)*0.94109839201)+((N_Jets==6)*0.902526080608)+((N_Jets==7)*0.854845643044)+((N_Jets==8)*0.810196101665)+((N_Jets>=9)*0.751408994198))",

        "weight_SF_N_Jets__ttlf_DL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.990902066231)+((N_Jets==2)*0.974494695663)+((N_Jets==3)*0.930031359196)+((N_Jets==4)*0.891780793667)+((N_Jets==5)*0.853191435337)+((N_Jets==6)*0.808273553848)+((N_Jets==7)*0.760848581791)+((N_Jets==8)*0.720039367676)+((N_Jets>=9)*0.651212632656))",

        "weight_SF_N_Jets__ttlf_FH__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.997122824192)+((N_Jets==2)*0.996734201908)+((N_Jets==3)*1.00171661377)+((N_Jets==4)*1.00546967983)+((N_Jets==5)*1.00333666801)+((N_Jets==6)*0.984970986843)+((N_Jets==7)*0.950660467148)+((N_Jets==8)*0.90752184391)+((N_Jets>=9)*0.845465958118))",

        "weight_SF_N_Jets__ttcc_SL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.997388720512)+((N_Jets==2)*0.993322908878)+((N_Jets==3)*0.987954199314)+((N_Jets==4)*0.975121617317)+((N_Jets==5)*0.950840175152)+((N_Jets==6)*0.91629332304)+((N_Jets==7)*0.870342075825)+((N_Jets==8)*0.825753331184)+((N_Jets>=9)*0.776921331882))",

        "weight_SF_N_Jets__ttcc_DL__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.996227145195)+((N_Jets==2)*0.980564951897)+((N_Jets==3)*0.959204614162)+((N_Jets==4)*0.922122359276)+((N_Jets==5)*0.884214818478)+((N_Jets==6)*0.841689825058)+((N_Jets==7)*0.797565221786)+((N_Jets==8)*0.749123692513)+((N_Jets>=9)*0.714639663696))",

        "weight_SF_N_Jets__ttcc_FH__btag_NOMINAL:=(((N_Jets==0)*1.0)+((N_Jets==1)*0.994180142879)+((N_Jets==2)*0.990937054157)+((N_Jets==3)*0.993372261524)+((N_Jets==4)*0.994842529297)+((N_Jets==5)*0.988011538982)+((N_Jets==6)*0.974682867527)+((N_Jets==7)*0.948365032673)+((N_Jets==8)*0.914483785629)+((N_Jets>=9)*0.846462607384))",






        "sf_N_Jets__ttH__btag_NOMINAL:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_NOMINAL)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL))",
        "sf_N_Jets__ttbb__btag_NOMINAL:=((selection_ttdl*selection_tthf*weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL)+(selection_ttsl*selection_tthf*weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL)+(selection_ttfh*selection_tthf*weight_SF_N_Jets__ttbb_4FS_FH__btag_NOMINAL))",
        "sf_N_Jets__ttcc__btag_NOMINAL:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_NOMINAL)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_NOMINAL)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_NOMINAL))",
        "sf_N_Jets__ttlf__btag_NOMINAL:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_NOMINAL)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_NOMINAL)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_NOMINAL))",

        "sf_N_Jets__btag_NOMINAL:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_NOMINAL+sf_N_Jets__ttcc__btag_NOMINAL+sf_N_Jets__ttbb__btag_NOMINAL)+(isTthSample==1)*(sf_N_Jets__ttH__btag_NOMINAL)+(isTTbarSample==0&&isTthSample==0)*(1.))",






    ]

    return addVars
