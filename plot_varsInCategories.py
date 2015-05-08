from plotutils import *

#samples
samples=[Sample('t#bar{t}H',ROOT.kBlue,'/nfs/dust/cms/user/hmildner/trees/tth.root','') , Sample('t#bar{t}',ROOT.kRed+1,'/nfs/dust/cms/user/hmildner/trees/ttbar.root','')]

#histos
histos=[ROOT.TH1F('BDToutput','BDT output',10,-1,1),
        ROOT.TH1F("all_sum_pt_with_met","all_sum_pt_with_met",30,0,1500),
        ROOT.TH1F("avg_btag_disc_btags","avg_btag_disc_btags",30,0.8,1),
        ROOT.TH1F("avg_dr_tagged_jets","avg_dr_tagged_jets",30,0,3),
        ROOT.TH1F("best_higgs_mass","best_higgs_mass",40,0,400),
        ROOT.TH1F("closest_tagged_dijet_mass","closest_tagged_dijet_mass",40,0,400),
        ROOT.TH1F("dEta_fn","dEta_fn",30,0,6),
        ROOT.TH1F("dev_from_avg_disc_btags","dev_from_avg_disc_btags",30,0,0.01),
        ROOT.TH1F("dr_between_lep_and_closest_jet","dr_between_lep_and_closest_jet",25,0,5),
        ROOT.TH1F("first_jet_pt","first_jet_pt",30,0,600),
        ROOT.TH1F("fourth_highest_btag","fourth_highest_btag",40,0.0,1),
        ROOT.TH1F("fourth_jet_pt","fourth_jet_pt",30,0,300),
        ROOT.TH1F("h0","h0",20,0.,0.5),
        ROOT.TH1F("h2","h2",20,-0.2,0.4),
        ROOT.TH1F("HT","HT",30,0,1500),
        ROOT.TH1F("lowest_btag","lowest_btag",20,0.8,1),
        ROOT.TH1F("M3","M3",30,0,600),
        ROOT.TH1F("maxeta_jet_jet","maxeta_jet_jet",25,0,5),
        ROOT.TH1F("maxeta_jet_tag","maxeta_jet_tag",25,0,5),
        ROOT.TH1F("maxeta_tag_tag","maxeta_tag_tag",25,0,5),
        ROOT.TH1F("MET","MET",30,0,300),
        ROOT.TH1F("MHT","MHT",25,0,500),
        ROOT.TH1F("Mlb","Mlb",30,0,300),
        ROOT.TH1F("pt_all_jets_over_E_all_jets","pt_all_jets_over_E_all_jets",25,0,1),
        ROOT.TH1F("second_highest_btag","second_highest_btag",40,0.,1),
        ROOT.TH1F("second_jet_pt","second_jet_pt",25,0,500),
        ROOT.TH1F("sphericity","sphericity",25,0,1),
        ROOT.TH1F("third_highest_btag","third_highest_btag",40,0.,1),
        ROOT.TH1F("third_jet_pt","third_jet_pt",30,0,300)]
#corresponding variables
variables=["BDTOhio_v1_output",
           "BDTOhio_v1_input_all_sum_pt_with_met",
           "BDTOhio_v1_input_avg_btag_disc_btags",
           "BDTOhio_v1_input_avg_dr_tagged_jets",
           "BDTOhio_v1_input_best_higgs_mass",
           "BDTOhio_v1_input_closest_tagged_dijet_mass",
           "BDTOhio_v1_input_dEta_fn",
           "BDTOhio_v1_input_dev_from_avg_disc_btags",
           "BDTOhio_v1_input_dr_between_lep_and_closest_jet",
           "BDTOhio_v1_input_first_jet_pt",
           "BDTOhio_v1_input_fourth_highest_btag",
           "BDTOhio_v1_input_fourth_jet_pt",
           "BDTOhio_v1_input_h0",
           "BDTOhio_v1_input_h2",
           "BDTOhio_v1_input_HT",
           "BDTOhio_v1_input_lowest_btag",
           "BDTOhio_v1_input_M3",
           "BDTOhio_v1_input_maxeta_jet_jet",
           "BDTOhio_v1_input_maxeta_jet_tag",
           "BDTOhio_v1_input_maxeta_tag_tag",
           "BDTOhio_v1_input_MET",
           "BDTOhio_v1_input_MHT",
           "BDTOhio_v1_input_Mlb",
           "BDTOhio_v1_input_pt_all_jets_over_E_all_jets",
           "BDTOhio_v1_input_second_highest_btag",
           "BDTOhio_v1_input_second_jet_pt",
           "BDTOhio_v1_input_sphericity",
           "BDTOhio_v1_input_third_highest_btag",
           "BDTOhio_v1_input_third_jet_pt"]
# selections of different categories
selections=[ "(N_Jets==4&&N_BTagsM==3)",
              "(N_Jets==4&&N_BTagsM>=4)",
              "(N_Jets==5&&N_BTagsM==3)",
              "(N_Jets==5&&N_BTagsM>=4)",
              "(N_Jets>=6&&N_BTagsM==2)",
              "(N_Jets>=6&&N_BTagsM==3)",
              "(N_Jets>=6&&N_BTagsM>=4)"
            ]
selectionnames=["4j3t","4j4t","5j3t","5j4t","6j2t","6j3t","6j4t"]

plots=plotsForSelections_cross_Histos(selections,selectionnames,histos,variables)

listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfhistoLists(listOfhistoLists,samples,'plots')

