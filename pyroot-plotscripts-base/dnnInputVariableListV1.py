all_variables = {
    "pT_j1":                    "Jet_Pt[0]",
    "eta_j1":                   "Jet_Eta[0]",
    "CSV_j1":                   "Jet_CSV[0]",

    "pT_j2":                    "Jet_Pt[1]",
    "eta_j2":                   "Jet_Eta[1]",
    "CSV_j2":                   "Jet_CSV[1]",

    "pT_j3":                    "Jet_Pt[2]",
    "eta_j3":                   "Jet_Eta[2]",
    "CSV_j3":                   "Jet_CSV[2]",

    "pT_j4":                    "Jet_Pt[3]",
    "eta_j4":                   "Jet_Eta[3]",
    "CSV_j4":                   "Jet_CSV[3]",

    "pT_lep1":                  "LooseLepton_Pt[0]" ,
    "eta_lep1":                 "LooseLepton_Eta[0]",

    "HT":                       "Evt_HT",
    "HT_tag":                   "BDT_common5_input_HT_tag",

    "min_dR_jj":                "Evt_Dr_MinDeltaRJets",
    "min_dR_bb":                "Evt_Dr_MinDeltaRTaggedJets",

    "max_dR_jj":                "BDT_common5_input_max_dR_jj", 
    "max_dR_bb":                "BDT_common5_input_max_dR_bb",

    "aplanarity_jets":          "BDT_common5_input_aplanarity_jets",
    "aplanarity_tags":          "BDT_common5_input_aplanarity_tags",

    "centrality_jets":          "Evt_JetPtOverJetE",
    "centrality_tags":          "BDT_common5_input_pt_all_jets_over_E_all_jets_tags",

    "sphericity_jets":          "BDT_common5_input_sphericity_jets",
    "sphericity_tags":          "BDT_common5_input_sphericity_tags",

    # transverse sphericities
    "sphericityT_jets":         "BDT_common5_input_transverse_sphericity_jets",
    "sphericityT_tags":         "BDT_common5_input_transverse_sphericity_tags",

    "avg_CSV_jets":             "Evt_CSV_Average",
    "avg_CSV_tags":             "Evt_CSV_Average_Tagged",

    "max_CSV_jets":             "CSV[0]",
    "max_CSV_tags":             "CSV[0]",

    "min_CSV_jets":             "Evt_CSV_Min",
    "min_CSV_tags":             "Evt_CSV_Min_Tagged",

    "min_dR_lep_jet":           "Evt_Dr_MinDeltaRLeptonJet",
    "min_dR_lep_tag":           "Evt_Dr_MinDeltaRLeptonTaggedJet",

    # fox wolframs
    "H_2":                      "BDT_common5_input_h1",
    "H_3":                      "BDT_common5_input_h2",
    "H_4":                      "BDT_common5_input_h3",

    "M_lep_closest_tag":        "Evt_M_MinDeltaRLeptonTaggedJet",

    "avg_deta_bb":              "Evt_Deta_TaggedJetsAverage",
    "avg_dR_bb":                "Evt_Dr_TaggedJetsAverage",

    "M2_of_min_dR_bb":          "BDT_common5_input_closest_tagged_dijet_mass",
    "2nd_moment_tagged_jets_CSVs":      "BDT_common5_input_dev_from_avg_disc_btags",

    "avg_M_jets":               "Evt_M_JetsAverage",
    "avg_M2_tags":              "Evt_M2_TaggedJetsAverage",

    "N_tags_tight":             "N_BTagsT",

    "M2_bb_closest_to_125":     "BDT_common5_input_tagged_dijet_mass_closest_to_125",

    "2nd_highest_CSV":          "CSV[1]",

    "blr":                      "Evt_blr_ETH",
    "blr_transformed":          "Evt_blr_ETH_transformed",
#    "dank_MEM":                 "memDBp",
}


undefined_variables = [
#    "dank_MEM",
#    "max_CSV_tags", #already covered
    #"sphericityT_jets",
    #"sphericityT_tags",
    #"HT_tag",
    #"aplanarity_tags",
    #"aplanarity_jets",
    #"sphericity_jets",
    #"sphericity_tags",
    #"max_dR_bb",
    #"max_dR_jj",
    #"centrality_tags",
    ]


# categories
# SL 4j,>=3b
variables_4j_3b = [
    "pT_j1",
    "CSV_j1",

    "eta_j2",
    "CSV_j2",

    "eta_j3",
    "CSV_j3",

    "pT_j4",
    "eta_j4",
    "CSV_j4",

    "eta_lep1",

    "HT_tag",

    "min_dR_jj",
    "min_dR_bb",

    "aplanarity_tags",
    "sphericity_jets",

    "sphericityT_jets",
    "sphericityT_tags",

    "avg_CSV_jets",
    "avg_CSV_tags",
    "max_CSV_jets",
    #"max_CSV_tags",
    "min_CSV_jets",
    "min_CSV_tags",

    "min_dR_lep_jet",

    "H_3",
    "H_4",

    "M_lep_closest_tag",
    "M2_of_min_dR_bb",
    "2nd_moment_tagged_jets_CSVs",

    "avg_M_jets",
    "avg_M2_tags",

    "N_tags_tight",

    "2nd_highest_CSV",

    "blr",
    "blr_transformed",
#    "dank_MEM",
    ]

# SL 5j,>=3b
variables_5j_3b = [
    "pT_j1",
    "eta_j1",
    "CSV_j1",

    "pT_j2",
    "eta_j2",
    "CSV_j2",

    "pT_j3",
    "eta_j3",
    "CSV_j3",

    "pT_j4",
    "eta_j4",

    "pT_lep1",

    "HT",
    "HT_tag",

    "min_dR_jj",
    "min_dR_bb",

    "max_dR_jj",

    "aplanarity_jets",
    "aplanarity_tags",

    "sphericity_jets",
    "sphericity_tags",

    "sphericityT_jets",
    "sphericityT_tags",

    "avg_CSV_jets",
    "avg_CSV_tags",

    "max_CSV_jets",
    #"max_CSV_tags",

    "min_CSV_jets",
    "min_CSV_tags",

    "min_dR_lep_jet",
    "min_dR_lep_tag",

    "H_2",
    "H_3",

    "M_lep_closest_tag",

    "avg_dR_bb",

    "M2_of_min_dR_bb",
    "2nd_moment_tagged_jets_CSVs",

    "avg_M_jets",

    "N_tags_tight",

    "M2_bb_closest_to_125",

    "2nd_highest_CSV",

    "blr",
    "blr_transformed",
#    "dank_MEM",
    ]



# SL >=6j, >=3b
variables_6j_3b = [
    "eta_j1",
    "CSV_j1",

    "eta_j2",
    "CSV_j2",

    "eta_j3",
    "CSV_j3",

    "eta_j4",
    "CSV_j4",

    "pT_lep1",
    "eta_lep1",

    "HT_tag",

    "min_dR_jj",
    "min_dR_bb",

    "max_dR_bb",

    "aplanarity_jets",
    "aplanarity_tags",

    "centrality_jets",
    "centrality_tags",

    "sphericity_jets",
    "sphericity_tags",

    "sphericityT_jets",
    "sphericityT_tags",

    "avg_CSV_jets",
    "avg_CSV_tags",

    "max_CSV_jets",
    #"max_CSV_tags",

    "min_CSV_jets",
    "min_CSV_tags",

    "min_dR_lep_tag",

    "H_4",

    "M_lep_closest_tag",

    "avg_deta_bb",
    "avg_dR_bb",

    "M2_of_min_dR_bb",
    "2nd_moment_tagged_jets_CSVs",

    "avg_M_jets",
    "avg_M2_tags",

    "N_tags_tight",

    "M2_bb_closest_to_125",

    "2nd_highest_CSV",

    "blr",
    "blr_transformed",
#    "dank_MEM",
    ]


variables_4j_3b = [all_variables[var] for var in variables_4j_3b if not var in undefined_variables]
variables_5j_3b = [all_variables[var] for var in variables_5j_3b if not var in undefined_variables]
variables_6j_3b = [all_variables[var] for var in variables_6j_3b if not var in undefined_variables]
all_variables_list = [all_variables[var] for var in all_variables if not var in undefined_variables]

