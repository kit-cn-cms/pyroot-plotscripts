import sys
import os
sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *


path='/nfs/dust/cms/user/hmildner/treesMEM0126/'
name='bdtplots'
sel_singleel="(N_LooseMuons==0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)" # and vice versa...
mcweight='(2.61)*(N_LooseElectrons==0||N_LooseMuons==0)' # some weights are only applied on mc
# selections for categories
sel1="((N_TightLeptons==1)*(N_LooseLeptons==1)*(N_BTagsM>=2)*(N_Jets>=4))" # l+jets channel
name1="1lge4ge2"

s43="(N_Jets==4&&N_BTagsM==3)"
s44="(N_Jets==4&&N_BTagsM>=4)"
s53="(N_Jets==5&&N_BTagsM==3)"
s54="(N_Jets==5&&N_BTagsM>=4)"
s62="(N_Jets>=6&&N_BTagsM==2)"
s63="(N_Jets>=6&&N_BTagsM==3)"
s64="(N_Jets>=6&&N_BTagsM>=4)"


# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samples_data=[Sample('SingleMu',ROOT.kBlack,path+'/mu_*/*nominal*.root',sel_singlemu,'SingleMu'),
              Sample('SingleEl',ROOT.kBlack,path+'/el_*/*nominal*.root',sel_singleel,'SingleEl')
              ]

# mc samples
samples=[Sample('t#bar{t}H',ROOT.kBlue+1,path+'/ttH*/*nominal*.root',mcweight,'ttH') ,     
#         Sample('t#bar{t}',ROOT.kRed+1,path+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
         Sample('t#bar{t}+lf',ROOT.kRed-7,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttl'),
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttcc'),
         Sample('t#bar{t}+b',ROOT.kRed-2,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','tt1b'),
         Sample('t#bar{t}+2b',ROOT.kRed+2,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','tt2b'),
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbb'),  
         Sample('Single Top',ROOT.kMagenta,path+'/st*/*nominal*.root',mcweight,'SingleTop') , 
         Sample('V+jets',ROOT.kGreen-3,path+'/??ets*/*nominal*.root',mcweight,'Vjets') , 
         #Sample('t#bar{t}+V',ROOT.kBlue-10,path+'/tt?_*/*nominal*.root',mcweight,'ttV'),         
         Sample('Diboson',ROOT.kAzure+2,path+'/??/*nominal*.root',mcweight,'Diboson') , 
#         Sample('QCD',ROOT.kYellow ,path+'/QCD*/*nominal*root',mcweight,'QCD') , 
]
plots=[]


# weights_Final_43_MEMBDTv2.xml
label="1 lepton, 4 jets, 3 b-tags"
plots+=[Plot(ROOT.TH1F("s43_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",20,0.9,1),"BDT_common5_input_avg_btag_disc_btags","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_HT","HT",20,0,1000),"BDT_common5_input_HT","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_MEM_transformed","MEM discriminator",20,0,0.95),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_third_highest_btag","third highest btag",22,0.89,1),"BDT_common5_input_third_highest_btag","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_Evt_CSV_Average","avg CSV (jets)",15,0.7,1),"Evt_CSV_Average","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_M3","M3",30,0,600),"BDT_common5_input_M3","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",20,0,1000),"BDT_common5_input_all_sum_pt_with_met","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_h1","H_{1}",30,-0.2,0.4),"BDT_common5_input_h1","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.,1),"BDT_common5_input_pt_all_jets_over_E_all_jets","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",35,0,3.5),"BDT_common5_input_dr_between_lep_and_closest_jet","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_first_jet_pt","jet 1 p_{T}",50,0,500),"BDT_common5_input_first_jet_pt","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",20,0,400),"BDT_common5_input_closest_tagged_dijet_mass","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_blr","B-tagging likelihood ratio",30,-3,8),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",'(N_Jets==4&&N_BTagsM==3)',label),
]

# /nfs/dust/cms/user/kelmorab/newTrain/3makeHistosAndCards/weights/CommonWeights/weights_Final_43_v5_OldVars.xml
plots+=[Plot(ROOT.TH1F("s43_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",20,0,4),"BDT_common5_input_avg_dr_tagged_jets","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_dev_from_avg_disc_btags","dev from avg CSV (tags)",25,0,0.0025),"BDT_common5_input_dev_from_avg_disc_btags","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_min_dr_tagged_jets","min #Delta R(tag,tag)",30,0.5,3.5),"BDT_common5_input_min_dr_tagged_jets","(N_Jets==4&&N_BTagsM==3)",label)]

        
label="1 lepton, 4 jets, 4 b-tags"
# weights_Final_44_MEMBDTv2.xml
plots+=[Plot(ROOT.TH1F("s44_MEM_transformed","MEM discriminator",10,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",10,0.9,1),"BDT_common5_input_avg_btag_disc_btags","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",9,30,120),"BDT_common5_input_fourth_jet_pt","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_BDT_common5_input_maxeta_tag_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_tag_tag","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_BDT_common5_input_first_jet_pt","jet 1 p_{T}",20,0,400),"BDT_common5_input_first_jet_pt","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",15,0,3),"Evt_Deta_JetsAverage","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",16,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_BDT_common5_input_fourth_highest_btag","fourth-highest CSV",11,0.89,1),"BDT_common5_input_fourth_highest_btag","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",15,0,1500),"BDT_common5_input_invariant_mass_of_everything","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_BDT_common5_input_M3","M3",20,0,800),"BDT_common5_input_M3","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s44_blr","B-tagging likelihood ratio",10,-0,12),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",'(N_Jets==4&&N_BTagsM>=4)',label),

        ]

# /nfs/dust/cms/user/kelmorab/newTrain/3makeHistosAndCards/weights/CommonWeights/weights_Final_44_v5_OldVars.xml
plots+=[
 Plot(ROOT.TH1F("s44_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",10,1.6,3.6),"BDT_common5_input_avg_dr_tagged_jets","(N_Jets==4&&N_BTagsM>=4)",label),
Plot(ROOT.TH1F("s44_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass","(N_Jets==4&&N_BTagsM>=4)",label),
 Plot(ROOT.TH1F("s44_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",12,0,2.4),"BDT_common5_input_min_dr_tagged_jets","(N_Jets==4&&N_BTagsM>=4)",label),
Plot(ROOT.TH1F("s44_BDT_common5_input_maxeta_jet_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_jet_tag","(N_Jets==4&&N_BTagsM>=4)",label),
Plot(ROOT.TH1F("s44_BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",10,0,1000),"BDT_common5_input_all_sum_pt_with_met","(N_Jets==4&&N_BTagsM>=4)",label),
Plot(ROOT.TH1F("s44_BDT_common5_input_HT","HT",20,0,1000),"BDT_common5_input_HT","(N_Jets==4&&N_BTagsM>=4)",label),
]

label="1 lepton, 5 jets, 3 b-tags"
    # weights_Final_53_MEMBDTv2.xml
plots+=[Plot(ROOT.TH1F("s53_MEM_transformed","MEM discriminator",20,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0,1),"BDT_common5_input_pt_all_jets_over_E_all_jets","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",30,0,1500),"BDT_common5_input_all_sum_pt_with_met","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_BDT_common5_input_third_highest_btag","third highest CSV",22,.89,1),"BDT_common5_input_third_highest_btag","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_BDT_common5_input_fourth_highest_btag","fourth highest CSV",22,-.1,1),"BDT_common5_input_fourth_highest_btag","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_Evt_Deta_JetsAverage","avg #Delta #eta jets",25,0,2.5),"Evt_Deta_JetsAverage","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_Evt_CSV_Average","avg CSV",25,0.5,1),"Evt_CSV_Average","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_blr","B-tagging likelihood ratio",20,-2,10),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",'(N_Jets==5&&N_BTagsM==3)',label),
        ]
# /nfs/dust/cms/user/kelmorab/newTrain/3makeHistosAndCards/weights/CommonWeights/weights_Final_53_v5_OldVars.xml
plots+=[Plot(ROOT.TH1F("s53_BDT_common5_input_h1","H_{1}",27,-.2,.34),"BDT_common5_input_h1","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",30,0.5,3.5),"BDT_common5_input_avg_dr_tagged_jets","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_BDT_common5_input_sphericity","sphericity",25,0,1),"BDT_common5_input_sphericity","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_BDT_common5_input_HT","HT",25,0,1000),"BDT_common5_input_HT","(N_Jets==5&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s53_BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.0025),"BDT_common5_input_dev_from_avg_disc_btags","(N_Jets==5&&N_BTagsM==3)",label),
]

label="1 lepton, 5 jets, #geq4 b-tags"
# weights_Final_54_MEMBDTv2.xml
plots+=[Plot(ROOT.TH1F("s54_MEM_transformed","MEM discriminator",10,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",10,.9,1),"BDT_common5_input_avg_btag_disc_btags","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_Evt_Deta_JetsAverage","avg #Delta #eta jets",10,0,2.5),"Evt_Deta_JetsAverage","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",15,0,150),"BDT_common5_input_fourth_jet_pt","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_M3","M3",20,0,1000),"BDT_common5_input_M3","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",12,0,1200),"BDT_common5_input_all_sum_pt_with_met","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_h2","H_{2}",15,-.15,0.3),"BDT_common5_input_h2","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",18,0,3.6),"BDT_common5_input_avg_dr_tagged_jets","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_blr","B-tagging likelihood ratio",10,-0,12),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",'(N_Jets==5&&N_BTagsM>=4)',label),

    ]
# /nfs/dust/cms/user/kelmorab/newTrain/3makeHistosAndCards/weights/CommonWeights/weights_Final_54_v5_OldVars.xml
plots+=[Plot(ROOT.TH1F("s54_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0,1),"BDT_common5_input_pt_all_jets_over_E_all_jets","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",10,80,180),"BDT_common5_input_tagged_dijet_mass_closest_to_125","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_HT","HT",20,0,1000),"BDT_common5_input_HT","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_h1","H_{1}",18,-.2,.34),"BDT_common5_input_h1","(N_Jets==5&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s54_BDT_common5_input_best_higgs_mass","best higgs mass",20,0,400),"BDT_common5_input_best_higgs_mass","(N_Jets==5&&N_BTagsM>=4)",label),
   ]
label="1 lepton, #geq6 jets, 3 b-tags"
# /nfs/dust/cms/user/kelmorab/newTrain/3makeHistosAndCards/weights/CommonWeights/weights_Final_62_v5_OldVars.xml
plots+=[Plot(ROOT.TH1F("s62_BDT_common5_input_h1","H_{1}",27,-0.2,.34),"BDT_common5_input_h1","(N_Jets>=6&&N_BTagsM==2)",label),
        Plot(ROOT.TH1F("s62_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",25,0,5),"BDT_common5_input_avg_dr_tagged_jets","(N_Jets>=6&&N_BTagsM==2)",label),
        Plot(ROOT.TH1F("s62_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity","(N_Jets>=6&&N_BTagsM==2)",label),
        Plot(ROOT.TH1F("s62_BDT_common5_input_third_highest_btag","third highest CSV",20,-.1,.9),"BDT_common5_input_third_highest_btag","(N_Jets>=6&&N_BTagsM==2)",label),
        Plot(ROOT.TH1F("s62_BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3","(N_Jets>=6&&N_BTagsM==2)",label),
        Plot(ROOT.TH1F("s62_BDT_common5_input_HT","HT",20,0,2000),"BDT_common5_input_HT","(N_Jets>=6&&N_BTagsM==2)",label),
        Plot(ROOT.TH1F("s62_BDT_common5_input_Mlb","mass(lepton,closest tag)",20,0,400),"BDT_common5_input_Mlb","(N_Jets>=6&&N_BTagsM==2)",label),
        Plot(ROOT.TH1F("s62_BDT_common5_input_fifth_highest_CSV","fifth highest CSV",20,-.1,.91),"BDT_common5_input_fifth_highest_CSV","(N_Jets>=6&&N_BTagsM==2)",label),
        Plot(ROOT.TH1F("s62_BDT_common5_input_fourth_highest_btag","fourth highes CSV",20,-.1,.9),"BDT_common5_input_fourth_highest_btag","(N_Jets>=6&&N_BTagsM==2)",label),
        Plot(ROOT.TH1F("s62_blr","B-tagging likelihood ratio",20,-6,6),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",'(N_Jets>=6&&N_BTagsM==2)',label),
]


label="1 lepton, #geq6 jets, 3 b-tags"
# weights_Final_63_MEMBDTv2.xml
plots+=[Plot(ROOT.TH1F("s63_MEM_transformed","MEM discriminator",20,0.,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_Evt_Deta_JetsAverage","avg #Delta #eta jets",25,0,2.5),"Evt_Deta_JetsAverage","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",25,0,2000),"BDT_common5_input_all_sum_pt_with_met","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_fourth_highest_btag","fourth-highest b-tag",18,0,0.9),"BDT_common5_input_fourth_highest_btag","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_aplanarity","aplanarity",20,0,0.4),"BDT_common5_input_aplanarity","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",22,.89,1),"BDT_common5_input_avg_btag_disc_btags","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",20,0.5,3.5),"BDT_common5_input_avg_dr_tagged_jets","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",20,0,200),"BDT_common5_input_fourth_jet_pt","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",30,0,300),"BDT_common5_input_tagged_dijet_mass_closest_to_125","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_h2","H_{2}",20,-.1,.3),"BDT_common5_input_h2","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_fifth_highest_CSV","fifth-highest CSV",20,-.1,.9),"BDT_common5_input_fifth_highest_CSV","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_blr","B-tagging likelihood ratio",20,-2,8),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",'(N_Jets>=6&&N_BTagsM==3)',label),

    ]
# /nfs/dust/cms/user/kelmorab/newTrain/3makeHistosAndCards/weights/CommonWeights/weights_Final_63_v5_OldVars.xml
plots+=[Plot(ROOT.TH1F("s63_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",17,0,3.4),"BDT_common5_input_min_dr_tagged_jets","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_dEta_fn","#sqrt{#Delta #eta(t^{lep}, bb) #times #Delta #eta(t^{had}, bb)}",20,0,5),"BDT_common5_input_dEta_fn","(N_Jets>=6&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s63_BDT_common5_input_h1","H_{1}",27,-.2,.34),"BDT_common5_input_h1","(N_Jets>=6&&N_BTagsM==3)",label),
]
   
label="1 lepton, #geq6 jets, #geq4 b-tags"
# weights_Final_64_MEMBDTv2.xml
plots+=[Plot(ROOT.TH1F("s64_BDT_common5_input_third_highest_btag","third-highest CSV",22,.89,1),"BDT_common5_input_third_highest_btag","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_MEM_transformed","MEM discriminator",20,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",22,0,2.2),"Evt_Deta_JetsAverage","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",20,0,200),"BDT_common5_input_fourth_jet_pt","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_aplanarity","aplanarity",20,0,0.4),"BDT_common5_input_aplanarity","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_M3","M3",20,0,1000),"BDT_common5_input_M3","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_third_jet_pt","jet 3 p_{T}",20,0,400),"BDT_common5_input_third_jet_pt","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_blr","B-tagging likelihood ratio",20,0,12),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",'(N_Jets>=6&&N_BTagsM>=4)',label),

       ]

# /nfs/dust/cms/user/kelmorab/newTrain/3makeHistosAndCards/weights/CommonWeights/weights_Final_64_v5_OldVars.xml
plots+=[
        Plot(ROOT.TH1F("s64_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",25,1,3.5),"BDT_common5_input_avg_dr_tagged_jets","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_best_higgs_mass","best higgs mass",30,0,600),"BDT_common5_input_best_higgs_mass","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",20,0,200),"BDT_common5_input_tagged_dijet_mass_closest_to_125","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_fourth_highest_btag","fourth highest btag",22,.89,1),"BDT_common5_input_fourth_highest_btag","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",25,0,250),"BDT_common5_input_closest_tagged_dijet_mass","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_fifth_highest_CSV","fifth highest CSV",22,-.1,1),"BDT_common5_input_fifth_highest_CSV","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_second_highest_btag","second highest btag",22,.89,1),"BDT_common5_input_second_highest_btag","(N_Jets>=6&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F("s64_BDT_common5_input_dr_between_lep_and_closest_jet","min #Delta R (lepton,jet)",25,0,2.5),"BDT_common5_input_dr_between_lep_and_closest_jet","(N_Jets>=6&&N_BTagsM>=4)",label),
]

# plot parallel -- alternatively there are also options to plot more traditional that also return lists of histo lists
outputpath=plotParallel(name,2000000,plots,samples+samples_data)
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCan(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name,False,labels)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCan(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name+'_log',True,labels)
