
def setValues(module):

    # ps 0.6
    module.reco_bins = [40.0, 120.0, 180.0, 240.0, 320.0, 420.0, 540.0, 700.0, 1000.0]
    module.gen_bins =  [40.0, 120.0, 180.0, 240.0, 320.0, 420.0, 540.0, 700.0, 1000.0]
    module.n_bins_per_bin = [2, 5, 5, 5, 5, 5, 5, 2]

    module.genSel  = "((N_GenJets>=6)&&(N_GenBJets>=4))"
    module.recoSel = "((N_Jets>=6)&&(N_BTagsM>=4))"
    module.recoLabel = "\geq 6 jets, \geq 4 b-tags"
    module.recoTag = "jt64"

    module.gen_variable = "genInfo_ft_GenBJets_maxM_bb"
    module.reco_variable = "genInfo_ft_maxMbb_M_bb"

    module.name_tag = "maxMbb"
    module.gen_label_tag  = "mmax M(bb)"
    module.reco_label_tag = "max M(bb)"

