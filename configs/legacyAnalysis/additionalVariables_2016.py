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

        "selection_ttbb:=(GenEvt_I_TTPlusBB==3&&GenEvt_I_TTPlusCC==0)",
        "selection_ttb:=(GenEvt_I_TTPlusBB==1&&GenEvt_I_TTPlusCC==0)",
        "selection_tt2b:=(GenEvt_I_TTPlusBB==2&&GenEvt_I_TTPlusCC==0)",
        "selection_tthf:=(GenEvt_I_TTPlusBB>=1&&GenEvt_I_TTPlusCC==0)",
        "selection_ttcc:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==1)",
        "selection_ttlf:=(GenEvt_I_TTPlusBB==0&&GenEvt_I_TTPlusCC==0)",




        "weight_SF_N_Jets__ttH_bb__btag_NOMINAL:=(((N_Jets==4)*0.984565317631)+((N_Jets==5)*0.983602821827)+((N_Jets==6)*0.981831669807)+((N_Jets==7)*0.976474165916)+((N_Jets==8)*0.970335483551)+((N_Jets>=9)*0.955639779568))",

        "weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL:=(((N_Jets==4)*0.973557591438)+((N_Jets==5)*0.966978728771)+((N_Jets==6)*0.961382508278)+((N_Jets==7)*0.954805850983)+((N_Jets==8)*0.945866346359)+((N_Jets>=9)*0.929779529572))",
        "weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL:=(((N_Jets==4)*0.965403258801)+((N_Jets==5)*0.95841383934)+((N_Jets==6)*0.952480196953)+((N_Jets==7)*0.93900001049)+((N_Jets==8)*0.924579381943)+((N_Jets>=9)*0.911359548569))",

        "weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL:=(((N_Jets==4)*0.95858836174)+((N_Jets==5)*0.948531806469)+((N_Jets==6)*0.934358894825)+((N_Jets==7)*0.926142632961)+((N_Jets==8)*0.905910730362)+((N_Jets>=9)*0.890256285667))",

        "weight_SF_N_Jets__ttlf_SL__btag_NOMINAL:=(((N_Jets==4)*0.992296516895)+((N_Jets==5)*0.983445227146)+((N_Jets==6)*0.971713364124)+((N_Jets==7)*0.959662795067)+((N_Jets==8)*0.930347323418)+((N_Jets>=9)*0.932259321213))",

        "weight_SF_N_Jets__ttlf_DL__btag_NOMINAL:=(((N_Jets==4)*0.970946669579)+((N_Jets==5)*0.958418726921)+((N_Jets==6)*0.946982383728)+((N_Jets==7)*0.933883786201)+((N_Jets==8)*0.910023331642)+((N_Jets>=9)*0.889549970627))",

        "weight_SF_N_Jets__ttlf_FH__btag_NOMINAL:=(((N_Jets==4)*0.997999727726)+((N_Jets==5)*0.997933328152)+((N_Jets==6)*0.994646906853)+((N_Jets==7)*0.981338918209)+((N_Jets==8)*0.972643733025)+((N_Jets>=9)*0.952476978302))",

        "weight_SF_N_Jets__ttcc_SL__btag_NOMINAL:=(((N_Jets==4)*0.992126882076)+((N_Jets==5)*0.986204743385)+((N_Jets==6)*0.977002203465)+((N_Jets==7)*0.967050671577)+((N_Jets==8)*0.956334590912)+((N_Jets>=9)*0.927379727364))",

        "weight_SF_N_Jets__ttcc_DL__btag_NOMINAL:=(((N_Jets==4)*0.979719817638)+((N_Jets==5)*0.969132423401)+((N_Jets==6)*0.950487554073)+((N_Jets==7)*0.93201571703)+((N_Jets==8)*0.940331816673)+((N_Jets>=9)*0.925750851631))",

        "weight_SF_N_Jets__ttcc_FH__btag_NOMINAL:=(((N_Jets==4)*0.996325850487)+((N_Jets==5)*0.996693789959)+((N_Jets==6)*0.992396354675)+((N_Jets==7)*0.983017206192)+((N_Jets==8)*0.975648164749)+((N_Jets>=9)*0.952305614948))",

        "sf_N_Jets__ttH__btag_NOMINAL:=((selection_hbb*weight_SF_N_Jets__ttH_bb__btag_NOMINAL)+(selection_nonhbb*weight_SF_N_Jets__ttH_nonbb__btag_NOMINAL))",
        "sf_N_Jets__ttbb__btag_NOMINAL:=((selection_ttdl*selection_tthf*weight_SF_N_Jets__ttbb_4FS_DL__btag_NOMINAL)+(selection_ttsl*selection_tthf*weight_SF_N_Jets__ttbb_4FS_SL__btag_NOMINAL))",
        "sf_N_Jets__ttcc__btag_NOMINAL:=((selection_ttdl*selection_ttcc*weight_SF_N_Jets__ttcc_DL__btag_NOMINAL)+(selection_ttsl*selection_ttcc*weight_SF_N_Jets__ttcc_SL__btag_NOMINAL)+(selection_ttfh*selection_ttcc*weight_SF_N_Jets__ttcc_FH__btag_NOMINAL))",
        "sf_N_Jets__ttlf__btag_NOMINAL:=((selection_ttdl*selection_ttlf*weight_SF_N_Jets__ttlf_DL__btag_NOMINAL)+(selection_ttsl*selection_ttlf*weight_SF_N_Jets__ttlf_SL__btag_NOMINAL)+(selection_ttfh*selection_ttlf*weight_SF_N_Jets__ttlf_FH__btag_NOMINAL))",

        "sf_N_Jets__btag_NOMINAL:=((isTTbarSample==1)*(sf_N_Jets__ttlf__btag_NOMINAL+sf_N_Jets__ttcc__btag_NOMINAL+sf_N_Jets__ttbb__btag_NOMINAL)+(isTthSample==1)*(sf_N_Jets__ttH__btag_NOMINAL)+(isTTbarSample==0&&isTthSample==0)*(1.))",





    ]

    return addVars
