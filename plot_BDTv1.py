from plotutils import *
# samples
samples=[Sample('t#bar{t}H',ROOT.kBlue,'/nfs/dust/cms/user/hmildner/trees/tth.root','') , Sample('t#bar{t}',ROOT.kRed+1,'/nfs/dust/cms/user/hmildner/trees/ttbar.root','')]

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

    Plot(ROOT.TH1F("BDToutput_6j2t","BDT output (6j2t)",20,-1,1),"BDTOhio_v1_output",s6j2t),
    Plot(ROOT.TH1F("HT_6j2t","HT (6j2t)",30,0,1500),"BDTOhio_v1_input_HT",s6j2t),
    Plot(ROOT.TH1F("sphericity_6j2t","sphericity (6j2t)",25,0,1),"BDTOhio_v1_input_sphericity",s6j2t),
    Plot(ROOT.TH1F("dr_between_lep_and_closest_jet_6j2t","dr_between_lep_and_closest_jet (6j2t)",30,0,3),"BDTOhio_v1_input_dr_between_lep_and_closest_jet",s6j2t),
    Plot(ROOT.TH1F("h2_6j2t","h2 (6j2t)",20,-0.2,0.4),"BDTOhio_v1_input_h2",s6j2t),
    Plot(ROOT.TH1F("third_highest_btag_6j2t","third_highest_btag (6j2t)",40,0.0,1),"BDTOhio_v1_input_third_highest_btag",s6j2t),
    Plot(ROOT.TH1F("fourth_highest_btag_6j2t","fourth_highest_btag (6j2t)",40,0.0,1),"BDTOhio_v1_input_fourth_highest_btag",s6j2t),
    Plot(ROOT.TH1F("maxeta_jet_jet_6j2t","maxeta_jet_jet (6j2t)",25,0,5),"BDTOhio_v1_input_maxeta_jet_jet",s6j2t),
    Plot(ROOT.TH1F("Mlb_6j2t","Mlb (6j2t)",30,0,300),"BDTOhio_v1_input_Mlb",s6j2t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_6j2t","pt_all_jets_over_E_all_jets (6j2t)",25,0,1),"BDTOhio_v1_input_pt_all_jets_over_E_all_jets",s6j2t),

    Plot(ROOT.TH1F("BDToutput_4j3t","BDT output (4j3t)",20,-1,1),"BDTOhio_v1_output",s4j3t),
    Plot(ROOT.TH1F("MET_4j3t","MET (4j3t)",30,0,300),"BDTOhio_v1_input_MET",s4j3t),
    Plot(ROOT.TH1F("first_jet_pt_4j3t","first_jet_pt (4j3t)",50,0,500),"BDTOhio_v1_input_first_jet_pt",s4j3t),
    Plot(ROOT.TH1F("second_jet_pt_4j3t","second_jet_pt (4j3t)",50,0,500),"BDTOhio_v1_input_second_jet_pt",s4j3t),
    Plot(ROOT.TH1F("third_jet_pt_4j3t","third_jet_pt (4j3t)",50,0,250),"BDTOhio_v1_input_third_jet_pt",s4j3t),
    Plot(ROOT.TH1F("fourth_jet_pt_4j3t","fourth_jet_pt (4j3t)",50,0,250),"BDTOhio_v1_input_fourth_jet_pt",s4j3t),
    Plot(ROOT.TH1F("all_sum_pt_with_met_4j3t","all_sum_pt_with_met (4j3t)",30,0,1500),"BDTOhio_v1_input_all_sum_pt_with_met",s4j3t),
    Plot(ROOT.TH1F("HT_4j3t","HT (4j3t)",30,0,1500),"BDTOhio_v1_input_HT",s4j3t),
    Plot(ROOT.TH1F("MHT_4j3t","MHT (4j3t)",25,0,500),"BDTOhio_v1_input_MHT",s4j3t),
    Plot(ROOT.TH1F("third_highest_btag_4j3t","third_highest_btag (4j3t)",20,0.8,1),"BDTOhio_v1_input_third_highest_btag",s4j3t),
    Plot(ROOT.TH1F("M3_4j3t","M3 (4j3t)",30,0,600),"BDTOhio_v1_input_M3",s4j3t),

    Plot(ROOT.TH1F("BDToutput_5j3t","BDT output (5j3t)",20,-1,1),"BDTOhio_v1_output",s5j3t),
    Plot(ROOT.TH1F("first_jet_pt_5j3t","first_jet_pt (5j3t)",50,0,500),"BDTOhio_v1_input_first_jet_pt",s5j3t),
    Plot(ROOT.TH1F("second_jet_pt_5j3t","second_jet_pt (5j3t)",50,0,500),"BDTOhio_v1_input_second_jet_pt",s5j3t),
    Plot(ROOT.TH1F("third_jet_pt_5j3t","third_jet_pt (5j3t)",50,0,250),"BDTOhio_v1_input_third_jet_pt",s5j3t),
    Plot(ROOT.TH1F("fourth_jet_pt_5j3t","fourth_jet_pt (5j3t)",50,0,250),"BDTOhio_v1_input_fourth_jet_pt",s5j3t),
    Plot(ROOT.TH1F("all_sum_pt_with_met_5j3t","all_sum_pt_with_met (5j3t)",30,0,1500),"BDTOhio_v1_input_all_sum_pt_with_met",s5j3t),
    Plot(ROOT.TH1F("HT_5j3t","HT (5j3t)",30,0,1500),"BDTOhio_v1_input_HT",s5j3t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_5j3t","avg_btag_disc_btags (5j3t)",30,0.8,1),"BDTOhio_v1_input_avg_btag_disc_btags",s5j3t),
    Plot(ROOT.TH1F("third_highest_btag_5j3t","third_highest_btag (5j3t)",20,0.8,1),"BDTOhio_v1_input_third_highest_btag",s5j3t),
    Plot(ROOT.TH1F("fourth_highest_btag_5j3t","fourth_highest_btag (5j3t)",40,0.0,1),"BDTOhio_v1_input_fourth_highest_btag",s5j3t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_5j3t","pt_all_jets_over_E_all_jets (5j3t)",25,0,1),"BDTOhio_v1_input_pt_all_jets_over_E_all_jets",s5j3t),

    Plot(ROOT.TH1F("BDToutput_6j3t","BDT output (6j3t)",20,-1,1),"BDTOhio_v1_output",s6j3t),
    Plot(ROOT.TH1F("h0_6j3t","h0 (6j3t)",20,0.,0.5),"BDTOhio_v1_input_h0",s6j3t),
    Plot(ROOT.TH1F("all_sum_pt_with_met_6j3t","all_sum_pt_with_met (6j3t)",30,0,1500),"BDTOhio_v1_input_all_sum_pt_with_met",s6j3t),
    Plot(ROOT.TH1F("sphericity_6j3t","sphericity (6j3t)",25,0,1),"BDTOhio_v1_input_sphericity",s6j3t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_6j3t","avg_btag_disc_btags (6j3t)",30,0.8,1),"BDTOhio_v1_input_avg_btag_disc_btags",s6j3t),
    Plot(ROOT.TH1F("second_highest_btag_6j3t","second_highest_btag (6j3t)",20,0.8,1),"BDTOhio_v1_input_second_highest_btag",s6j3t),
    Plot(ROOT.TH1F("third_highest_btag_6j3t","third_highest_btag (6j3t)",20,0.8,1),"BDTOhio_v1_input_third_highest_btag",s6j3t),
    Plot(ROOT.TH1F("fourth_highest_btag_6j3t","fourth_highest_btag (6j3t)",20,0.,1),"BDTOhio_v1_input_fourth_highest_btag",s6j3t),
    Plot(ROOT.TH1F("maxeta_jet_jet_6j3t","maxeta_jet_jet (6j3t)",25,0,5),"BDTOhio_v1_input_maxeta_jet_jet",s6j3t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_6j3t","pt_all_jets_over_E_all_jets (6j3t)",25,0,1),"BDTOhio_v1_input_pt_all_jets_over_E_all_jets",s6j3t),

    Plot(ROOT.TH1F("BDToutput_4j4t","BDT output (4j4t)",20,-1,1),"BDTOhio_v1_output",s4j4t),
    Plot(ROOT.TH1F("first_jet_pt_4j4t","first_jet_pt (4j4t)",50,0,500),"BDTOhio_v1_input_first_jet_pt",s4j4t),
    Plot(ROOT.TH1F("second_jet_pt_4j4t","second_jet_pt (4j4t)",50,0,500),"BDTOhio_v1_input_second_jet_pt",s4j4t),
    Plot(ROOT.TH1F("fourth_jet_pt_4j4t","fourth_jet_pt (4j4t)",50,0,250),"BDTOhio_v1_input_fourth_jet_pt",s4j4t),
    Plot(ROOT.TH1F("all_sum_pt_with_met_4j4t","all_sum_pt_with_met (4j4t)",30,0,1500),"BDTOhio_v1_input_all_sum_pt_with_met",s4j4t),
    Plot(ROOT.TH1F("HT_4j4t","HT (4j4t)",30,0,1500),"BDTOhio_v1_input_HT",s4j4t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_4j4t","avg_btag_disc_btags (4j4t)",30,0.8,1),"BDTOhio_v1_input_avg_btag_disc_btags",s4j4t),
    Plot(ROOT.TH1F("second_highest_btag_4j4t","second_highest_btag (4j4t)",20,0.8,1),"BDTOhio_v1_input_second_highest_btag",s4j4t),
    Plot(ROOT.TH1F("third_highest_btag_4j4t","third_highest_btag (4j4t)",20,0.8,1),"BDTOhio_v1_input_third_highest_btag",s4j4t),
    Plot(ROOT.TH1F("fourth_highest_btag_4j4t","fourth_highest_btag (4j4t)",20,0.8,1),"BDTOhio_v1_input_fourth_highest_btag",s4j4t),
    Plot(ROOT.TH1F("M3_4j4t","M3 (4j4t)",30,0,600),"BDTOhio_v1_input_M3",s4j4t),

    Plot(ROOT.TH1F("BDToutput_5j4t","BDT output (5j4t)",20,-1,1),"BDTOhio_v1_output",s5j4t),
    Plot(ROOT.TH1F("all_sum_pt_with_met_5j4t","all_sum_pt_with_met (5j4t)",30,0,1500),"BDTOhio_v1_input_all_sum_pt_with_met",s5j4t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_5j4t","avg_dr_tagged_jets (5j4t)",50,0,5),"BDTOhio_v1_input_avg_dr_tagged_jets",s5j4t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_5j4t","avg_btag_disc_btags (5j4t)",30,0.8,1),"BDTOhio_v1_input_avg_btag_disc_btags",s5j4t),
    Plot(ROOT.TH1F("dev_from_avg_disc_btags_5j4t","dev_from_avg_disc_btags (5j4t)",30,0,0.01),"BDTOhio_v1_input_dev_from_avg_disc_btags",s5j4t),
    Plot(ROOT.TH1F("lowest_btag_5j4t","lowest_btag (5j4t)",20,0.8,1),"BDTOhio_v1_input_lowest_btag",s5j4t),
    Plot(ROOT.TH1F("second_highest_btag_5j4t","second_highest_btag (5j4t)",20,0.8,1),"BDTOhio_v1_input_second_highest_btag",s5j4t),
    Plot(ROOT.TH1F("third_highest_btag_5j4t","third_highest_btag (5j4t)",20,0.8,1),"BDTOhio_v1_input_third_highest_btag",s5j4t),
    Plot(ROOT.TH1F("maxeta_jet_tag_5j4t","maxeta_jet_tag (5j4t)",25,0,5),"BDTOhio_v1_input_maxeta_jet_tag",s5j4t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_5j4t","pt_all_jets_over_E_all_jets (5j4t)",25,0,1),"BDTOhio_v1_input_pt_all_jets_over_E_all_jets",s5j4t),

    Plot(ROOT.TH1F("BDToutput_6j4t","BDT output (6j4t)",20,-1,1),"BDTOhio_v1_output",s6j4t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_6j4t","avg_dr_tagged_jets (6j4t)",50,0,5),"BDTOhio_v1_input_avg_dr_tagged_jets",s6j4t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_6j4t","avg_btag_disc_btags (6j4t)",30,0.8,1),"BDTOhio_v1_input_avg_btag_disc_btags",s6j4t),
    Plot(ROOT.TH1F("closest_tagged_dijet_mass_6j4t","closest_tagged_dijet_mass (6j4t)",40,0,400),"BDTOhio_v1_input_closest_tagged_dijet_mass",s6j4t),
    Plot(ROOT.TH1F("third_highest_btag_6j4t","third_highest_btag (6j4t)",20,0.8,1),"BDTOhio_v1_input_third_highest_btag",s6j4t),
    Plot(ROOT.TH1F("fourth_highest_btag_6j4t","fourth_highest_btag (6j4t)",20,0.8,1),"BDTOhio_v1_input_fourth_highest_btag",s6j4t),
    Plot(ROOT.TH1F("maxeta_tag_tag_6j4t","maxeta_tag_tag (6j4t)",25,0,5),"BDTOhio_v1_input_maxeta_tag_tag",s6j4t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_6j4t","pt_all_jets_over_E_all_jets (6j4t)",25,0,1),"BDTOhio_v1_input_pt_all_jets_over_E_all_jets",s6j4t),
    Plot(ROOT.TH1F("best_higgs_mass_6j4t","best_higgs_mass (6j4t)",40,0,400),"BDTOhio_v1_input_best_higgs_mass",s6j4t),
    Plot(ROOT.TH1F("dEta_fn_6j4t","dEta_fn (6j4t)",40,0,5),"BDTOhio_v1_input_dEta_fn",s6j4t)
]

listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfhistoLists(listOfhistoLists,samples,"bdtvars")

