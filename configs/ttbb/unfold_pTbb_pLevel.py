
def setValues(module):

    # ps 0.6
    module.reco_bins = [3.0, 90.0, 130.0, 180.0, 240.0, 300.0, 400.0, 500.0, 800.0]
    module.gen_bins =  [3.0, 90.0, 130.0, 180.0, 240.0, 300.0, 400.0, 500.0, 800.0]
    module.n_bins_per_bin = [2, 5, 5, 5, 5, 5, 5, 3]

    module.genSel  = "((N_GenJets>=6)&&(N_GenBJets>=4))"
    module.recoSel = "((N_Jets>=6)&&(N_BTagsM>=4))"
    module.recoLabel = "\geq 6 jets, \geq 4 b-tags"
    module.recoTag = "jt64"

    module.gen_variable = "genInfo_ft_ClosestGenB_Pt_bb"
    module.reco_variable = "genInfo_ft_mindRbb_Pt_bb"

    module.name_tag = "pTbb"
    module.gen_label_tag  = "min#DeltaR p_{T}(bb)"
    module.reco_label_tag = "min#DeltaR p_{T}(bb)"

