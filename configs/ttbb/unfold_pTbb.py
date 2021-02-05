
def setValues(module):

    # 0.4 symmetric
    #module.reco_bins = [0.0, 100.0, 140.0, 200.0, 270.0, 350.0, 430.0, 510.0, 600.0]
    #module.gen_bins = [0.0, 100.0, 140.0, 200.0, 270.0, 350.0, 430.0, 510.0, 600.0]
    # 0.35 symmetric
    module.reco_bins = [0.0, 90.0, 120.0, 160.0, 210.0, 270.0, 340.0, 420.0, 500.0, 570.0, 690.0, 900.0]
    module.gen_bins = [0.0, 90.0, 120.0, 160.0, 210.0, 270.0, 340.0, 420.0, 500.0, 570.0, 690.0, 900.0]

    module.genSel  = "(N_GenJets>=6&&N_GenBJets>=4&&N_GenTopLep==1)"
    module.recoSel = "(N_Jets>=6&&N_BTagsM>=4&&N_TightLeptons==1)"
    module.recoLabel = "\geq 6 jets, \geq 4 b-tags"
    module.recoTag = "jt64"

    module.gen_variable = "genInfo_ft_AddGenB_Pt_bb"
    module.reco_variable = "Evt_Pt_minDrTaggedJets"

    module.name_tag = "pTbb"
    module.gen_label_tag = "p_{T}(bb)"
    module.reco_label_tag = "min#DeltaR p_{T}(bb)"

