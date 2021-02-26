
def setValues(module):

    # ps 0.7
    module.reco_bins = [0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.7, 2.1, 3.0]
    module.gen_bins =  [0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.7, 2.1, 3.0]
    module.n_bins_per_bin = [4, 5, 5, 5, 5, 5, 5, 1]

    module.genSel  = "((N_GenJets>=6)&&(N_GenBJets>=4))"
    module.recoSel = "((N_Jets>=6)&&(N_BTagsM>=4))"
    module.recoLabel = "\geq 6 jets, \geq 4 b-tags"
    module.recoTag = "jt64"

    module.gen_variable = "genInfo_ft_ClosestGenB_dR_bb"
    module.reco_variable = "genInfo_ft_mindRbb_dR_bb"

    module.name_tag = "dRbb"
    module.gen_label_tag  = "min#DeltaR(bb)"
    module.reco_label_tag = "min#DeltaR(bb)"

