from plotutils import *
# samples
samples=[Sample('t#bar{t}Hbb',ROOT.kBlack,'/nfs/dust/cms/user/hmildner/trees0818/tth.root','') , 
         Sample('t#bar{t}+b',4,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusBB==1'),
         Sample('t#bar{t}+2b',6,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusBB==2'),
         Sample('t#bar{t}+bb',3,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusBB==3'),
         Sample('t#bar{t}+cc',5,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusCC==1'),
         Sample('t#bar{t}+l',2,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0'),


]

# selecion for categories
sall="Evt_Odd==0"

s4j3t="(N_Jets==4&&N_BTagsM==3)"
s4j4t="(N_Jets==4&&N_BTagsM>=4)"
s5j3t="(N_Jets==5&&N_BTagsM==3)"
s5j4t="(N_Jets==5&&N_BTagsM>=4)"
s6j2t="(N_Jets>=6&&N_BTagsM==2)"
s6j3t="(N_Jets>=6&&N_BTagsM==3)"
s6j4t="(N_Jets>=6&&N_BTagsM>=4)"

nbins=20

plots=[

#    Plot(ROOT.TH1F("JT" ,"jet-tag categories",9,-0.5,8.5),"3*max(min(N_BTagsM-2,2),0)+max(min(N_Jets-4,2),0)",""),
#    Plot(ROOT.TH1F("N_Jets" ,"Number of jets",9,-0.5,8.5),"N_Jets",""),
#    Plot(ROOT.TH1F("N_BTagsM" ,"Number of medium b-tags",9,-0.5,8.5),"N_BTagsM",""),
    Plot(ROOT.TH1F("BDT_v3_output_6j2t","BDT_v3_output (6j2t)",20,-1,1),"BDT_v3_output",s6j2t),
    Plot(ROOT.TH1F("BDT_v3_output_4j3t","BDT_v3_output (4j3t)",20,-1,1),"BDT_v3_output",s4j3t),
    Plot(ROOT.TH1F("BDT_v3_output_5j3t","BDT_v3_output (5j3t)",20,-1,1),"BDT_v3_output",s5j3t),
    Plot(ROOT.TH1F("BDT_v3_output_6j3t","BDT_v3_output (6j3t)",20,-1,1),"BDT_v3_output",s6j3t),
    Plot(ROOT.TH1F("BDT_v3_output_4j4t","BDT_v3_output (4j4t)",10,-1,1),"BDT_v3_output",s4j4t),
    Plot(ROOT.TH1F("BDT_v3_output_5j4t","BDT_v3_output (5j4t)",10,-1,1),"BDT_v3_output",s5j4t),
    Plot(ROOT.TH1F("BDT_v3_output_6j4t","BDT_v3_output (6j4t)",10,-1,1),"BDT_v3_output",s6j4t),

]
plots_unbinned=[



    # 62
    Plot(ROOT.TH1F("h1_6j2t","h1 (6j2t)",nbins,0,0),"BDT_v3_input_h1",s6j2t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_6j2t","avg_dr_tagged_jets (6j2t)",nbins,0,0),"BDT_v3_input_avg_dr_tagged_jets",s6j2t),
    Plot(ROOT.TH1F("sphericity_6j2t","sphericity (6j2t)",nbins,0,0),"BDT_v3_input_sphericity",s6j2t),
    Plot(ROOT.TH1F("third_highest_btag_6j2t","third_highest_btag (6j2t)",nbins,0,0),"BDT_v3_input_third_highest_btag",s6j2t),
    Plot(ROOT.TH1F("h3_6j2t","h3 (6j2t)",nbins,0,0),"BDT_v3_input_h3",s6j2t),
    Plot(ROOT.TH1F("HT_6j2t","HT (6j2t)",nbins,0,0),"BDT_v3_input_HT",s6j2t),
    Plot(ROOT.TH1F("Mlb_6j2t","Mlb (6j2t)",nbins,0,0),"BDT_v3_input_Mlb",s6j2t),
    Plot(ROOT.TH1F("fifth_highest_CSV_6j2t","fifth_highest_CSV (6j2t)",nbins,0,0),"BDT_v3_input_fifth_highest_CSV",s6j2t),
    Plot(ROOT.TH1F("fourth_highest_btag_6j2t","fourth_highest_btag (6j2t)",nbins,0,0),"BDT_v3_input_fourth_highest_btag",s6j2t),
    
    # 43
    Plot(ROOT.TH1F("h1_4j3t","h1 (4j3t)",nbins,0,0),"BDT_v3_input_h1",s4j3t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_4j3t","avg_dr_tagged_jets (4j3t)",nbins,0,0),"BDT_v3_input_avg_dr_tagged_jets",s4j3t),
    Plot(ROOT.TH1F("sphericity_4j3t","sphericity (4j3t)",nbins,0,0),"BDT_v3_input_sphericity",s4j3t),
    Plot(ROOT.TH1F("third_highest_btag_4j3t","third_highest_btag (4j3t)",nbins,0,0),"BDT_v3_input_third_highest_btag",s4j3t),
    Plot(ROOT.TH1F("HT_4j3t","HT (4j3t)",nbins,0,0),"BDT_v3_input_HT",s4j3t),
    Plot(ROOT.TH1F("dev_from_avg_disc_btags_4j3t","dev_from_avg_disc_btags (4j3t)",nbins,0,0),"BDT_v3_input_dev_from_avg_disc_btags",s4j3t),
    Plot(ROOT.TH1F("M3_4j3t","M3 (4j3t)",nbins,0,0),"BDT_v3_input_M3",s4j3t),
    Plot(ROOT.TH1F("min_dr_tagged_jets_4j3t","min_dr_tagged_jets (4j3t)",nbins,0,0),"BDT_v3_input_min_dr_tagged_jets",s4j3t),
    Plot(ROOT.TH1F("Evt_CSV_Average_4j3t","Evt_CSV_Average (4j3t)",nbins,0,0),"BDT_v3_input_Evt_CSV_Average",s4j3t),
    
    # 53
    Plot(ROOT.TH1F("h1_5j3t","h1 (5j3t)",nbins,0,0),"BDT_v3_input_h1",s5j3t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_5j3t","avg_dr_tagged_jets (5j3t)",nbins,0,0),"BDT_v3_input_avg_dr_tagged_jets",s5j3t),
    Plot(ROOT.TH1F("sphericity_5j3t","sphericity (5j3t)",nbins,0,0),"BDT_v3_input_sphericity",s5j3t),
    Plot(ROOT.TH1F("third_highest_btag_5j3t","third_highest_btag (5j3t)",nbins,0,0),"BDT_v3_input_third_highest_btag",s5j3t),
    Plot(ROOT.TH1F("h3_5j3t","h3 (5j3t)",nbins,0,0),"BDT_v3_input_h3",s5j3t),
    Plot(ROOT.TH1F("HT_5j3t","HT (5j3t)",nbins,0,0),"BDT_v3_input_HT",s5j3t),
    Plot(ROOT.TH1F("dev_from_avg_disc_btags_5j3t","dev_from_avg_disc_btags (5j3t)",nbins,0,0),"BDT_v3_input_dev_from_avg_disc_btags",s5j3t),
    Plot(ROOT.TH1F("fourth_highest_btag_5j3t","fourth_highest_btag (5j3t)",nbins,0,0),"BDT_v3_input_fourth_highest_btag",s5j3t),
    
    # 63
    Plot(ROOT.TH1F("h1_6j3t","h1 (6j3t)",nbins,0,0),"BDT_v3_input_h1",s6j3t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_6j3t","avg_dr_tagged_jets (6j3t)",nbins,0,0),"BDT_v3_input_avg_dr_tagged_jets",s6j3t),
    Plot(ROOT.TH1F("third_highest_btag_6j3t","third_highest_btag (6j3t)",nbins,0,0),"BDT_v3_input_third_highest_btag",s6j3t),
    Plot(ROOT.TH1F("HT_6j3t","HT (6j3t)",nbins,0,0),"BDT_v3_input_HT",s6j3t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_6j3t","pt_all_jets_over_E_all_jets (6j3t)",nbins,0,0),"BDT_v3_input_pt_all_jets_over_E_all_jets",s6j3t),
    Plot(ROOT.TH1F("fifth_highest_CSV_6j3t","fifth_highest_CSV (6j3t)",nbins,0,0),"BDT_v3_input_fifth_highest_CSV",s6j3t),
    Plot(ROOT.TH1F("fourth_highest_btag_6j3t","fourth_highest_btag (6j3t)",nbins,0,0),"BDT_v3_input_fourth_highest_btag",s6j3t),
    Plot(ROOT.TH1F("min_dr_tagged_jets_6j3t","min_dr_tagged_jets (6j3t)",nbins,0,0),"BDT_v3_input_min_dr_tagged_jets",s6j3t),
    
    # 44
    Plot(ROOT.TH1F("h1_4j4t","h1 (4j4t)",nbins,0,0),"BDT_v3_input_h1",s4j4t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_4j4t","avg_dr_tagged_jets (4j4t)",nbins,0,0),"BDT_v3_input_avg_dr_tagged_jets",s4j4t),
    Plot(ROOT.TH1F("sphericity_4j4t","sphericity (4j4t)",nbins,0,0),"BDT_v3_input_sphericity",s4j4t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_4j4t","avg_btag_disc_btags (4j4t)",nbins,0,0),"BDT_v3_input_avg_btag_disc_btags",s4j4t),
    Plot(ROOT.TH1F("h2_4j4t","h2 (4j4t)",nbins,0,0),"BDT_v3_input_h2",s4j4t),
    Plot(ROOT.TH1F("closest_tagged_dijet_mass_4j4t","closest_tagged_dijet_mass (4j4t)",nbins,0,0),"BDT_v3_input_closest_tagged_dijet_mass",s4j4t),
    Plot(ROOT.TH1F("second_highest_btag_4j4t","second_highest_btag (4j4t)",nbins,0,0),"BDT_v3_input_second_highest_btag",s4j4t),
    Plot(ROOT.TH1F("fourth_highest_btag_4j4t","fourth_highest_btag (4j4t)",nbins,0,0),"BDT_v3_input_fourth_highest_btag",s4j4t),
    Plot(ROOT.TH1F("maxeta_jet_jet_4j4t","maxeta_jet_jet (4j4t)",nbins,0,0),"BDT_v3_input_maxeta_jet_jet",s4j4t),
    Plot(ROOT.TH1F("pt_all_jets_over_E_all_jets_4j4t","pt_all_jets_over_E_all_jets (4j4t)",nbins,0,0),"BDT_v3_input_pt_all_jets_over_E_all_jets",s4j4t),
    
    # 54
    Plot(ROOT.TH1F("avg_dr_tagged_jets_5j4t","avg_dr_tagged_jets (5j4t)",nbins,0,0),"BDT_v3_input_avg_dr_tagged_jets",s5j4t),
    Plot(ROOT.TH1F("HT_5j4t","HT (5j4t)",nbins,0,0),"BDT_v3_input_HT",s5j4t),
    Plot(ROOT.TH1F("M3_5j4t","M3 (5j4t)",nbins,0,0),"BDT_v3_input_M3",s5j4t),
    Plot(ROOT.TH1F("fifth_highest_CSV_5j4t","fifth_highest_CSV (5j4t)",nbins,0,0),"BDT_v3_input_fifth_highest_CSV",s5j4t),
    Plot(ROOT.TH1F("fourth_highest_btag_5j4t","fourth_highest_btag (5j4t)",nbins,0,0),"BDT_v3_input_fourth_highest_btag",s5j4t),
    Plot(ROOT.TH1F("Evt_Deta_JetsAverage_5j4t","Evt_Deta_JetsAverage (5j4t)",nbins,0,0),"BDT_v3_input_Evt_Deta_JetsAverage",s5j4t),
    Plot(ROOT.TH1F("avg_btag_disc_btags_5j4t","avg_btag_disc_btags (5j4t)",nbins,0,0),"BDT_v3_input_avg_btag_disc_btags",s5j4t),
    
    # 64
    Plot(ROOT.TH1F("h2_6j4t","h2 (6j4t)",nbins,0,0),"BDT_v3_input_h2",s6j4t),
    Plot(ROOT.TH1F("avg_dr_tagged_jets_6j4t","avg_dr_tagged_jets (6j4t)",nbins,0,0),"BDT_v3_input_avg_dr_tagged_jets",s6j4t),
    Plot(ROOT.TH1F("third_highest_btag_6j4t","third_highest_btag (6j4t)",nbins,0,0),"BDT_v3_input_third_highest_btag",s6j4t),
    Plot(ROOT.TH1F("M3_6j4t","M3 (6j4t)",nbins,0,0),"BDT_v3_input_M3",s6j4t),
    Plot(ROOT.TH1F("fifth_highest_CSV_6j4t","fifth_highest_CSV (6j4t)",nbins,0,0),"BDT_v3_input_fifth_highest_CSV",s6j4t),
    Plot(ROOT.TH1F("fourth_highest_btag_6j4t","fourth_highest_btag (6j4t)",nbins,0,0),"BDT_v3_input_fourth_highest_btag",s6j4t),
    Plot(ROOT.TH1F("best_higgs_mass_6j4t","best_higgs_mass (6j4t)",nbins,0,0),"BDT_v3_input_best_higgs_mass",s6j4t),
    Plot(ROOT.TH1F("dEta_fn_6j4t","dEta_fn (6j4t)",nbins,0,0),"BDT_v3_input_dEta_fn",s6j4t)
]
newplots=plots+setPlotRangeAuto(plots_unbinned,samples,'MVATree')
listOfhistoLists=createHistoLists_fromTree(newplots,samples,'MVATree')
writeListOfhistoLists(listOfhistoLists,samples,"bdtvars3")

