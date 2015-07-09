from plotutils import *
# samples
samples=[Sample('t#bar{t}H',ROOT.kBlue,'/nfs/dust/cms/user/kelmorab/Phys14_BaseJuly6th/addedTrees/tth_nominal.root','') , Sample('t#bar{t}',ROOT.kRed+1,'/nfs/dust/cms/user/kelmorab/Phys14_BaseJuly6th/addedTrees/ttbar_nominal.root','')]

# selecion for categories
s4j3t="(N_Jets==4&&N_BTagsM==3)"
s4j4t="(N_Jets==4&&N_BTagsM>=4)"
s5j3t="(N_Jets==5&&N_BTagsM==3)"
s5j4t="(N_Jets==5&&N_BTagsM>=4)"
s6j2t="(N_Jets>=6&&N_BTagsM==2)"
s6j3t="(N_Jets>=6&&N_BTagsM==3)"
s6j4t="(N_Jets>=6&&N_BTagsM>=4)"

plots=[

    Plot(ROOT.TH1F("JT" ,"jet-tag categories",9,-0.5,8.5),"3*max(min(N_BTagsM-2,2),0)+max(min(N_Jets-4,2),0)",""),
    Plot(ROOT.TH1F("N_Jets" ,"Number of jets",9,-0.5,8.5),"N_Jets",""),
    Plot(ROOT.TH1F("N_BTagsM" ,"Number of medium b-tags",9,-0.5,8.5),"N_BTagsM",""),

    Plot(ROOT.TH1F("first_jet_pt_6j2t","first_jet_pt (6j2t)",50,0,500),"BDTOhio_v2_input_first_jet_pt",s6j2t),
    Plot(ROOT.TH1F("second_jet_pt_6j2t","second_jet_pt (6j2t)",50,0,500),"BDTOhio_v2_input_second_jet_pt",s6j2t),
    Plot(ROOT.TH1F("fourth_jet_pt_6j2t","fourth_jet_pt (6j2t)",30,0,300),"BDTOhio_v2_input_fourth_jet_pt",s6j2t),
    Plot(ROOT.TH1F("h0_6j2t","h0 (6j2t)",40,0.1,0.5),"BDTOhio_v2_input_h0",s6j2t),
    Plot(ROOT.TH1F("h1_6j2t","h1 (6j2t)",35,-0.2,0.5),"BDTOhio_v2_input_h1",s6j2t),
    Plot(ROOT.TH1F("all_sum_pt_with_met_6j2t","all_sum_pt_with_met (6j2t)",50,0,2000),"BDTOhio_v2_input_all_sum_pt_with_met",s6j2t),
    Plot(ROOT.TH1F("HT_6j2t","HT (6j2t)",50,0,2000),"BDTOhio_v2_input_HT",s6j2t),
    Plot(ROOT.TH1F("h3_6j2t","h3 (6j2t)",55,-.1,1),"BDTOhio_v2_input_h3",s6j2t),
    Plot(ROOT.TH1F("third_highest_btag_6j2t","third_highest_btag (6j2t)",50,0,1),"BDTOhio_v2_input_third_highest_btag",s6j2t),
    Plot(ROOT.TH1F("fourth_highest_btag_6j2t","fourth_highest_btag (6j2t)",50,0,1),"BDTOhio_v2_input_fourth_highest_btag",s6j2t),
    Plot(ROOT.TH1F("fifth_highest_CSV_6j2t","fifth_highest_CSV (6j2t)",50,0,1),"BDTOhio_v2_input_fifth_highest_CSV",s6j2t),
    Plot(ROOT.TH1F("maxeta_jet_jet_6j2t","maxeta_jet_jet (6j2t)",50,0,5),"BDTOhio_v2_input_maxeta_jet_jet",s6j2t),
    Plot(ROOT.TH1F("Mlb","Mlb (6j2t)",50,0,250),"BDTOhio_v2_input_Mlb",s6j2t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_6j2t","pt_all_jets_over_E_all_jets (6j2t)",50,0.,1),"BDTOhio_v2_input_pt_all_jets_over_E_all_jets",s6j2t),

    Plot(ROOT.TH1F("first_jet_pt_4j3t","first_jet_pt (4j3t)",50,0,500),"BDTOhio_v2_input_first_jet_pt",s4j3t),
    Plot(ROOT.TH1F("second_jet_pt_4j3t","second_jet_pt (4j3t)",50,0,500),"BDTOhio_v2_input_second_jet_pt",s4j3t),
    Plot(ROOT.TH1F("third_jet_pt_4j3t","third_jet_pt (4j3t)",30,0,300),"BDTOhio_v2_input_third_jet_pt",s4j3t),
    Plot(ROOT.TH1F("all_sum_pt_with_met_4j3t","all_sum_pt_with_met (4j3t)",50,0,2000),"BDTOhio_v2_input_all_sum_pt_with_met",s4j3t),
    Plot(ROOT.TH1F("HT_4j3t","HT (4j3t)",50,0,2000),"BDTOhio_v2_input_HT",s4j3t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_4j3t","avg_btag_disc_btags (4j3t)",40,0.8,1),"BDTOhio_v2_input_avg_btag_disc_btags",s4j3t),
    Plot(ROOT.TH1F("dev_from_avg_disc_btags_4j3t","dev_from_avg_disc_btags (4j3t)",50,0,0.01),"BDTOhio_v2_input_dev_from_avg_disc_btags",s4j3t),
    Plot(ROOT.TH1F("second_highest_btag_4j3t","second_highest_btag (4j3t)",50,0.8,1),"BDTOhio_v2_input_second_highest_btag",s4j3t),
    Plot(ROOT.TH1F("third_highest_btag_4j3t","third_highest_btag (4j3t)",50,0.8,1),"BDTOhio_v2_input_third_highest_btag",s4j3t),
    Plot(ROOT.TH1F("invariant_mass_of_everything_4j3t","invariant_mass_of_everything (4j3t)",50,0,2000),"BDTOhio_v2_input_invariant_mass_of_everything",s4j3t),

    Plot(ROOT.TH1F("second_jet_pt_5j3t","second_jet_pt (5j3t)",50,0,500),"BDTOhio_v2_input_second_jet_pt",s5j3t),
    Plot(ROOT.TH1F("third_jet_pt_5j3t","third_jet_pt (5j3t)",30,0,300),"BDTOhio_v2_input_third_jet_pt",s5j3t),
    Plot(ROOT.TH1F("fourth_jet_pt_5j3t","fourth_jet_pt (5j3t)",30,0,300),"BDTOhio_v2_input_fourth_jet_pt",s5j3t),
    Plot(ROOT.TH1F("all_sum_pt_with_met_5j3t","all_sum_pt_with_met (5j3t)",50,0,2000),"BDTOhio_v2_input_all_sum_pt_with_met",s5j3t),
    Plot(ROOT.TH1F("HT_5j3t","HT (5j3t)",50,0,2000),"BDTOhio_v2_input_HT",s5j3t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_5j3t","avg_dr_tagged_jets (5j3t)",50,0,5),"BDTOhio_v2_input_avg_dr_tagged_jets",s5j3t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_5j3t","avg_btag_disc_btags (5j3t)",50,0.8,1),"BDTOhio_v2_input_avg_btag_disc_btags",s5j3t),
    Plot(ROOT.TH1F("dev_from_avg_disc_btags_5j3t","dev_from_avg_disc_btags (5j3t)",50,0,0.01),"BDTOhio_v2_input_dev_from_avg_disc_btags",s5j3t),
    Plot(ROOT.TH1F("h3_5j3t","h3 (5j3t)",55,-0.1,1),"BDTOhio_v2_input_h3",s5j3t),
    Plot(ROOT.TH1F("second_highest_btag_5j3t","second_highest_btag (5j3t)",50,.8,1),"BDTOhio_v2_input_second_highest_btag",s5j3t),
    Plot(ROOT.TH1F("third_highest_btag_5j3t","third_highest_btag (5j3t)",50,.8,1),"BDTOhio_v2_input_third_highest_btag",s5j3t),
    Plot(ROOT.TH1F("maxeta_jet_jet_5j3t","maxeta_jet_jet (5j3t)",50,0,5),"BDTOhio_v2_input_maxeta_jet_jet",s5j3t),
    Plot(ROOT.TH1F("maxeta_jet_tag_5j3t","maxeta_jet_tag (5j3t)",50,0,5),"BDTOhio_v2_input_maxeta_jet_tag",s5j3t),
    Plot(ROOT.TH1F("maxeta_tag_tag_5j3t","maxeta_tag_tag (5j3t)",50,0,5),"BDTOhio_v2_input_maxeta_tag_tag",s5j3t),

    Plot(ROOT.TH1F("third_jet_pt_6j3t","third_jet_pt (6j3t)",40,0,400),"BDTOhio_v2_input_third_jet_pt",s6j3t),
    Plot(ROOT.TH1F("fouth_jet_pt_6j3t","fourth_jet_pt (6j3t)",30,0,300),"BDTOhio_v2_input_fourth_jet_pt",s6j3t),
    Plot(ROOT.TH1F("all_sum_pt_with_met_6j3t","all_sum_pt_with_met (6j3t)",50,0,2000),"BDTOhio_v2_input_all_sum_pt_with_met",s6j3t),
    Plot(ROOT.TH1F("HT_6j3t","HT (6j3t)",50,0,2000),"BDTOhio_v2_input_HT",s6j3t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_6j3t","avg_dr_tagged_jets (6j3t)",40,0,4),"BDTOhio_v2_input_avg_dr_tagged_jets",s6j3t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_6j3t","avg_btag_disc_btags (6j3t)",50,0.8,1),"BDTOhio_v2_input_avg_btag_disc_btags",s6j3t),
    Plot(ROOT.TH1F("dev_from_avg_disc_btags_6j3t","dev_from_avg_disc_btags (6j3t)",50,0,0.01),"BDTOhio_v2_input_dev_from_avg_disc_btags",s6j3t),
    Plot(ROOT.TH1F("h3_6j3t","h3 (6j3t)",55,-.1,1),"BDTOhio_v2_input_h3",s6j3t),
    Plot(ROOT.TH1F("second_highest_btag_6j3t","second_highest_btag (6j3t)",50,0.8,1),"BDTOhio_v2_input_second_highest_btag",s6j3t),
    Plot(ROOT.TH1F("third_highest_btag_6j3t","third_highest_btag (6j3t)",50,0.8,1),"BDTOhio_v2_input_third_highest_btag",s6j3t),
    Plot(ROOT.TH1F("fourth_highest_btag_6j3t","fourth_highest_btag (6j3t)",50,0.0,1),"BDTOhio_v2_input_fourth_highest_btag",s6j3t),
    Plot(ROOT.TH1F("maxeta_jet_tag_6j3t","maxeta_jet_tag (6j3t)",50,0,5),"BDTOhio_v2_input_maxeta_jet_tag",s6j3t),
    Plot(ROOT.TH1F("maxeta_tag_tag_6j3t","maxeta_tag_tag (6j3t)",50,0,5),"BDTOhio_v2_input_maxeta_tag_tag",s6j3t),
    Plot(ROOT.TH1F("min_dr_tagged_jets_6j3t","min_dr_tagged_jets (6j3t)",40,0,4),"BDTOhio_v2_input_min_dr_tagged_jets",s6j3t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_6j3t","pt_all_jets_over_E_all_jets (6j3t)",50,0,1),"BDTOhio_v2_input_pt_all_jets_over_E_all_jets",s6j3t),

    Plot(ROOT.TH1F("h1_4j4t","h1 (4j4t)",35,-0.2,0.5),"BDTOhio_v2_input_h1",s4j4t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_4j4t","avg_dr_tagged_jets (4j4t)",45,1,3.5),"BDTOhio_v2_input_avg_dr_tagged_jets",s4j4t),
    Plot(ROOT.TH1F("sphericity_4j4t","sphericity (4j4t)",50,0,1),"BDTOhio_v2_input_sphericity",s4j4t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_4j4t","avg_btag_disc_btags (4j4t)",50,0.8,1),"BDTOhio_v2_input_avg_btag_disc_btags",s4j4t),
    Plot(ROOT.TH1F("dev_from_avg_disc_btags_4j4t","dev_from_avg_disc_btags (4j4t)",50,0,0.01),"BDTOhio_v2_input_dev_from_avg_disc_btags",s4j4t),
    Plot(ROOT.TH1F("h2_4j4t","h2 (4j4t)",50,-0.2,.5),"BDTOhio_v2_input_h2",s4j4t),
    Plot(ROOT.TH1F("closest_tagged_dijet_mass_4j4t","closest_tagged_dijet_mass (4j4t)",30,0,300),"BDTOhio_v2_input_closest_tagged_dijet_mass",s4j4t),
    Plot(ROOT.TH1F("h3_4j4t","h3 (4j4t)",55,-.1,1),"BDTOhio_v2_input_h3",s4j4t),
    Plot(ROOT.TH1F("second_highest_btag_4j4t","second_highest_btag (4j4t)",50,0.8,1),"BDTOhio_v2_input_second_highest_btag",s4j4t),
    Plot(ROOT.TH1F("third_highest_btag_4j4t","third_highest_btag (4j4t)",50,0.8,1),"BDTOhio_v2_input_third_highest_btag",s4j4t),
    Plot(ROOT.TH1F("fourth_highest_btag_4j4t","fourth_highest_btag (4j4t)",50,0.8,1),"BDTOhio_v2_input_fourth_highest_btag",s4j4t),
    Plot(ROOT.TH1F("maxeta_jet_jet_4j4t","maxeta_jet_jet (4j4t)",40,0,4),"BDTOhio_v2_input_maxeta_jet_jet",s4j4t),
    Plot(ROOT.TH1F("min_dr_tagged_jets_4j4t","min_dr_tagged_jets (4j4t)",50,0,2.5),"BDTOhio_v2_input_min_dr_tagged_jets",s4j4t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_4j4t","pt_all_jets_over_E_all_jets (4j4t)",50,0,1),"BDTOhio_v2_input_pt_all_jets_over_E_all_jets",s4j4t),

    Plot(ROOT.TH1F("aplanarity_5j4t","aplanarity (5j4t)",50,0,0.5),"BDTOhio_v2_input_aplanarity",s5j4t),
    Plot(ROOT.TH1F("third_jet_pt_5j4t","third_jet_pt (5j4t)",30,0,300),"BDTOhio_v2_input_third_jet_pt",s5j4t),
    Plot(ROOT.TH1F("fourth_jet_pt_5j4t","fourth_jet_pt (5j4t)",30,0,300),"BDTOhio_v2_input_fourth_jet_pt",s5j4t),
    Plot(ROOT.TH1F("h1_5j4t","h1 (5j4t)",35,-0.2,0.5),"BDTOhio_v2_input_h1",s5j4t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_5j4t","avg_dr_tagged_jets (5j4t)",30,0.5,3.5),"BDTOhio_v2_input_avg_dr_tagged_jets",s5j4t),
    Plot(ROOT.TH1F("sphericity_5j4t","sphericity (5j4t)",50,0,1),"BDTOhio_v2_input_sphericity",s5j4t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_5j4t","avg_btag_disc_btags (5j4t)",50,0.8,1),"BDTOhio_v2_input_avg_btag_disc_btags",s5j4t),
    Plot(ROOT.TH1F("dev_from_avg_disc_btags_5j4t","dev_from_avg_disc_btags (5j4t)",50,0,0.01),"BDTOhio_v2_input_dev_from_avg_disc_btags",s5j4t),
    Plot(ROOT.TH1F("h2_5j4t","h2 (5j4t)",30,-0.2,0.4),"BDTOhio_v2_input_h2",s5j4t),
    Plot(ROOT.TH1F("h3_5j4t","h3 (5j4t)",50,-1,1),"BDTOhio_v2_input_h3",s5j4t),
    Plot(ROOT.TH1F("third_highest_btag_5j4t","third_highest_btag (5j4t)",50,0.8,1),"BDTOhio_v2_input_third_highest_btag",s5j4t),
    Plot(ROOT.TH1F("fourth_highest_btag_5j4t","fourth_highest_btag (5j4t)",50,0.8,1),"BDTOhio_v2_input_third_highest_btag",s5j4t),
    Plot(ROOT.TH1F("maxeta_jet_jet_5j4t","maxeta_jet_jet (5j4t)",50,0,5),"BDTOhio_v2_input_maxeta_jet_jet",s5j4t),
    Plot(ROOT.TH1F("maxeta_jet_tag_5j4t","maxeta_jet_tag (5j4t)",50,0,5),"BDTOhio_v2_input_maxeta_jet_tag",s5j4t),
    Plot(ROOT.TH1F("maxeta_tag_tag_5j4t","maxeta_tag_tag (5j4t)",50,0,5),"BDTOhio_v2_input_maxeta_tag_tag",s5j4t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_5j4t","pt_all_jets_over_E_all_jets (5j4t)",50,0,1),"BDTOhio_v2_input_pt_all_jets_over_E_all_jets",s5j4t),

    Plot(ROOT.TH1F("avg_dr_tagged_jets_6j4t","avg_dr_tagged_jets (6j4t)",50,0,5),"BDTOhio_v2_input_avg_dr_tagged_jets",s6j4t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_6j4t","avg_btag_disc_btags (6j4t)",50,0.8,1),"BDTOhio_v2_input_avg_btag_disc_btags",s6j4t),
    Plot(ROOT.TH1F("h2_6j4t","h2 (6j4t)",30,-0.2,0.4),"BDTOhio_v2_input_h2",s6j4t),
    Plot(ROOT.TH1F("h3_6j4t","h3 (6j4t)",55,-.1,1),"BDTOhio_v2_input_h3",s6j4t),
    Plot(ROOT.TH1F("second_highest_btag_6j4t","second_highest_btag (6j4t)",50,0.8,1),"BDTOhio_v2_input_second_highest_btag",s6j4t),
    Plot(ROOT.TH1F("third_highest_btag_6j4t","third_highest_btag (6j4t)",50,0.8,1),"BDTOhio_v2_input_third_highest_btag",s6j4t),
    Plot(ROOT.TH1F("fourth_highest_btag_6j4t","fourth_highest_btag (6j4t)",50,0.8,1),"BDTOhio_v2_input_fourth_highest_btag",s6j4t),
    Plot(ROOT.TH1F("maxeta_jet_jet_6j4t","maxeta_jet_jet (6j4t)",50,0,5),"BDTOhio_v2_input_maxeta_jet_jet",s6j4t),
    Plot(ROOT.TH1F("maxeta_jet_tag_6j4t","maxeta_jet_tag (6j4t)",50,0,5),"BDTOhio_v2_input_maxeta_jet_tag",s6j4t),
    Plot(ROOT.TH1F("maxeta_tag_tag_6j4t","maxeta_tag_tag (6j4t)",50,0,5),"BDTOhio_v2_input_maxeta_tag_tag",s6j4t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_6j4t","pt_all_jets_over_E_all_jets (6j4t)",50,0,1),"BDTOhio_v2_input_pt_all_jets_over_E_all_jets",s6j4t),
    Plot(ROOT.TH1F("tagged_dijet_mass_closest_to_125_6j4t","tagged_dijet_mass_closest_to_125 (6j4t)",30,50,200),"BDTOhio_v2_input_tagged_dijet_mass_closest_to_125",s6j4t),
    Plot(ROOT.TH1F("dEta_fn_6j4t","dEta_fn (6j4t)",50,0,5),"BDTOhio_v2_input_dEta_fn",s6j4t),
]

listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfhistoLists(listOfhistoLists,samples,"bdtvars2")

