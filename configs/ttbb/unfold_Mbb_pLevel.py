
def setValues(module):

    # ps 0.6
    module.reco_bins = [20.0, 40.0, 60.0, 85.0, 120.0, 175.0, 350.0]
    module.gen_bins =  [20.0, 40.0, 60.0, 85.0, 120.0, 175.0, 350.0]
    module.n_bins_per_bin = [2, 5, 5, 5, 5, 5, 1]

    module.genSel  = "((N_GenJets>=6)&&(N_GenBJets>=4))"
    module.recoSel = "((N_Jets>=6)&&(N_BTagsM>=4))"
    module.recoLabel = "\geq 6 jets, \geq 4 b-tags"
    module.recoTag = "jt64"

    module.gen_variable = "genInfo_ft_ClosestGenB_M_bb"
    module.reco_variable = "genInfo_ft_mindRbb_M_bb"

    module.name_tag = "Mbb"
    module.gen_label_tag  = "min#DeltaR M(bb)"
    module.reco_label_tag = "min#DeltaR M(bb)"

