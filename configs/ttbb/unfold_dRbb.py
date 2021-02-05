
def setValues(module):

    # kerstin 0.4
    #module.reco_bins = [0.3, 0.5, 0.6, 0.8, 1.1, 1.7, 3.0]
    #module.gen_bins = [0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 3.0]
    # kerstin 0.5
    #reco_bins = [0.4, 0.6, 1.1, 2.1, 3.0]
    #gen_bins = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 3.0]
    # 0.4 symmetric
    #module.reco_bins = [0.4, 0.5, 0.6, 0.8, 1.1, 1.6, 4.0]
    #module.gen_bins = [0.4, 0.5, 0.6, 0.8, 1.1, 1.6, 4.0]
    # 0.35 symmetric
    #module.reco_bins = [0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.4, 3.0]
    #module.gen_bins = [0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.4, 3.0]
    module.reco_bins = [0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.4, 3.]
    module.gen_bins = [0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.4, 3.]
    module.n_bins_per_bin = [2, 5, 5, 5, 5, 5, 5, 1]
    #module.n_bins_per_bin = 5

    module.genSel  = "((N_GenJets>=6)&&(N_GenBJets>=4))"
    module.recoSel = "((N_Jets>=6)&&(N_BTagsM>=4))"
    module.recoLabel = "\geq 6 jets, \geq 4 b-tags"
    module.recoTag = "jt64"

    module.gen_variable = "genInfo_ft_AddGenB_dR_bb"
    module.reco_variable = "Evt_Dr_minDrTaggedJets"

    module.name_tag = "dRbb"
    module.gen_label_tag = "#DeltaR(bb)"
    module.reco_label_tag = "min#DeltaR(bb)"

