
def setValues(module):

    # 0.4 symmetric
    module.reco_bins = [0.0, 40.0, 60.0, 90.0, 140.0, 400.0]
    module.gen_bins = [0.0, 40.0, 60.0, 90.0, 140.0, 400.0]

    module.genSel  = "(N_GenJets>=6&&N_GenBJets>=4&&N_GenTopLep==1)"
    module.recoSel = "(N_Jets>=6&&N_BTagsM>=4&&N_TightLeptons==1)"
    module.recoLabel = "\geq 6 jets, \geq 4 b-tags"
    module.recoTag = "jt64"

    module.gen_variable = "genInfo_ft_AddGenB_M_bb"
    module.reco_variable = "Evt_M2_minDrTaggedJets"

    module.name_tag = "Mbb"
    module.gen_label_tag = "#M(bb)"
    module.reco_label_tag = "min#DeltaR #M(bb)"

