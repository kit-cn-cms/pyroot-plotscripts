def getDNNInputVars():

    DNNVars = [    
        "CSV[1]",
        "Evt_CSV_Min",
        "Jet_Pt[3]",
        "Jet_Pt[0]",
        "Jet_Pt[1]",
        "Jet_Pt[2]",
        "Evt_Deta_TaggedJetsAverage",
        "Evt_Dr_MinDeltaRLeptonTaggedJet",
        "BDT_common5_input_transverse_sphericity_jets",
        "BDT_common5_input_HT_tag",
        "Evt_Dr_MinDeltaRLeptonJet",
        "Evt_Dr_TaggedJetsAverage",
        "N_BTagsT",
        "LooseLepton_Eta[0]",
        "Evt_JetPtOverJetE",
        "Evt_M_JetsAverage",
        "BDT_common5_input_aplanarity_tags",
        "Evt_M2_TaggedJetsAverage",
        "BDT_common5_input_h3",
        "BDT_common5_input_h1",
        "BDT_common5_input_h2",
        #"memDBp",
        "Jet_Eta[3]",
        "BDT_common5_input_sphericity_jets",
        "Evt_CSV_Average_Tagged",
        "Evt_CSV_Average",
        "Jet_CSV[2]",
        "Jet_CSV[1]",
        "Jet_CSV[0]",
        "Jet_CSV[3]",
        "BDT_common5_input_sphericity_tags",
        "Evt_HT",
        "BDT_common5_input_closest_tagged_dijet_mass",
        "BDT_common5_input_tagged_dijet_mass_closest_to_125",
        "Evt_blr_ETH_transformed",
        "Evt_blr_ETH",
        "BDT_common5_input_transverse_sphericity_tags",
        "BDT_common5_input_max_dR_bb",
        "CSV[0]",
        "CSV[0]",
        "LooseLepton_Pt[0]",
        "Evt_Dr_MinDeltaRJets",
        "Evt_CSV_Min_Tagged",
        "BDT_common5_input_dev_from_avg_disc_btags",
        "BDT_common5_input_max_dR_jj",
        "Jet_Eta[2]",
        "Jet_Eta[1]",
        "Jet_Eta[0]",
        "Evt_M_MinDeltaRLeptonTaggedJet",
        "Evt_Dr_MinDeltaRTaggedJets",
        "BDT_common5_input_pt_all_jets_over_E_all_jets_tags",
        "BDT_common5_input_aplanarity_jets",
    ]
    
    return DNNVars



def getAddVars():
    BDTWeightPath = "/nfs/dust/cms/user/kelmorab/Spring17BDTWeights/"
    BDTSet = "Spring17v1"
    #alternativeBDTSet = "Spring17v3_ttbb"

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
        "Evt_Pt_PrimaryLepton",
        "Evt_E_PrimaryLepton",
        "Evt_M_PrimaryLepton",
        "Evt_Phi_PrimaryLepton",
        "Evt_Eta_PrimaryLepton",
        "Evt_Pt_MET",
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
        "Evt_blr_ETH",
        "Evt_blr_ETH_transformed",
        #'finalbdt_ljets_j4_t2:=Evt_HT_Jets',
        #'finalbdt_ljets_j5_t2:=Evt_HT_Jets',
        #'finalbdt_ljets_j4_t3:='+BDTWeightPath+'/weights_Final_43_'+BDTSet+'.xml',
        #'finalbdt_ljets_j4_t4:='+BDTWeightPath+'/weights_Final_44_'+BDTSet+'.xml',
        #'finalbdt_ljets_j5_t3:='+BDTWeightPath+'/weights_Final_53_'+BDTSet+'.xml',
        #'finalbdt_ljets_j5_tge4:='+BDTWeightPath+'/weights_Final_54_'+BDTSet+'.xml',
        #'finalbdt_ljets_jge6_t2:='+BDTWeightPath+'/weights_Final_62_'+BDTSet+'.xml',
        #'finalbdt_ljets_jge6_t3:='+BDTWeightPath+'/weights_Final_63_'+BDTSet+'.xml',
        #'finalbdt_ljets_jge6_tge4:='+BDTWeightPath+'/weights_Final_64_'+BDTSet+'.xml',

        "L1ScaleFactor_j4_tge3_ttHnode:=((DoWeights==1)*(isTthSample==1)*0.976+(DoWeights==1)*(isTthSample==0)*0.979+(DoWeights==0)*1.0)",
        "L1ScaleFactor_j4_tge3_ttbbnode:=((DoWeights==1)*(isTthSample==1)*0.973+(DoWeights==1)*(isTthSample==0)*0.975+(DoWeights==0)*1.0)",
        "L1ScaleFactor_j4_tge3_ttbnode:=((DoWeights==1)*(isTthSample==1)*0.978+(DoWeights==1)*(isTthSample==0)*0.979+(DoWeights==0)*1.0)",
        "L1ScaleFactor_j4_tge3_tt2bnode:=((DoWeights==1)*(isTthSample==1)*0.971+(DoWeights==1)*(isTthSample==0)*0.972+(DoWeights==0)*1.0)",
        "L1ScaleFactor_j4_tge3_ttccnode:=((DoWeights==1)*(isTthSample==1)*0.97+(DoWeights==1)*(isTthSample==0)*0.974+(DoWeights==0)*1.0)",
        "L1ScaleFactor_j4_tge3_ttlfnode:=((DoWeights==1)*(isTthSample==1)*0.974+(DoWeights==1)*(isTthSample==0)*0.983+(DoWeights==0)*1.0)",

        "L1ScaleFactor_j5_tge3_ttHnode:=((DoWeights==1)*(isTthSample==1)*0.979+(DoWeights==1)*(isTthSample==0)*0.976+(DoWeights==0)*1.0)",
        "L1ScaleFactor_j5_tge3_ttbbnode:=((DoWeights==1)*(isTthSample==1)*0.972+(DoWeights==1)*(isTthSample==0)*0.968+(DoWeights==0)*1.0)",
        "L1ScaleFactor_j5_tge3_ttbnode:=((DoWeights==1)*(isTthSample==1)*0.978+(DoWeights==1)*(isTthSample==0)*0.976+(DoWeights==0)*1.0)",
        "L1ScaleFactor_j5_tge3_tt2bnode:=((DoWeights==1)*(isTthSample==1)*0.972+(DoWeights==1)*(isTthSample==0)*0.966+(DoWeights==0)*1.0)",
        "L1ScaleFactor_j5_tge3_ttccnode:=((DoWeights==1)*(isTthSample==1)*0.974+(DoWeights==1)*(isTthSample==0)*0.968+(DoWeights==0)*1.0)",
        "L1ScaleFactor_j5_tge3_ttlfnode:=((DoWeights==1)*(isTthSample==1)*0.975+(DoWeights==1)*(isTthSample==0)*0.976+(DoWeights==0)*1.0)",

        "L1ScaleFactor_jge6_tge3_ttHnode:=((DoWeights==1)*(isTthSample==1)*0.975+(DoWeights==1)*(isTthSample==0)*0.969+(DoWeights==0)*1.0)",
        "L1ScaleFactor_jge6_tge3_ttbbnode:=((DoWeights==1)*(isTthSample==1)*0.965+(DoWeights==1)*(isTthSample==0)*0.962+(DoWeights==0)*1.0)",
        "L1ScaleFactor_jge6_tge3_ttbnode:=((DoWeights==1)*(isTthSample==1)*0.973+(DoWeights==1)*(isTthSample==0)*0.969+(DoWeights==0)*1.0)",
        "L1ScaleFactor_jge6_tge3_tt2bnode:=((DoWeights==1)*(isTthSample==1)*0.966+(DoWeights==1)*(isTthSample==0)*0.956+(DoWeights==0)*1.0)",
        "L1ScaleFactor_jge6_tge3_ttccnode:=((DoWeights==1)*(isTthSample==1)*0.966+(DoWeights==1)*(isTthSample==0)*0.957+(DoWeights==0)*1.0)",
        "L1ScaleFactor_jge6_tge3_ttlfnode:=((DoWeights==1)*(isTthSample==1)*0.971+(DoWeights==1)*(isTthSample==0)*0.969+(DoWeights==0)*1.0)",
        ]

    addVars += list(set(getDNNInputVars()))
    return addVars


