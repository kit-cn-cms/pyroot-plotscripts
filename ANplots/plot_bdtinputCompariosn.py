###############
# plot comparison for generators and data for input variables
###############

from plotconfig import *
sys.path.insert(0, '../limittools')
from limittools import renameHistos
import sys


#DoCats=['64']
DoCats=sys.argv[1:]
print DoCats
#exit(0)


samplesGenerators=[  
         Sample('t#bar{t} Powheg+Pythia8',ROOT.kRed,path_76x+'/ttbar_????_*/*nominal*.root',mcweight+ttbarMCweight,'ttbarPP8',systs_all_samples,0.05),
         #Sample('t#bar{t} aMC@NLOFXFX+Pythia8',ROOT.kAzure+5,path_76x+'/TTJETS_amcFXFX/TTJETS_amcFXFX_*_nominal_Tree.root','2.61*(N_Jets>=4 && N_BTagsM>=2)','ttbarAmcFxFx',systs_all_samples,0.05),
         Sample('t#bar{t} MadGraphMLM+Pythia8',ROOT.kSpring+5,path_76x+'/TTJETS_*_MGP8/*_nominal.root','2.61*(N_Jets>=4 && N_BTagsM>=2)','ttbarMGP8',systs_all_samples,0.05),
]

muSF="muonIDHelper.GetSF(muonPt,muonEta,0)*muonIsoHelper.GetSF(muonPt,muonEta,0)*muonTriggerHelper.GetSF(muonPt,muonEta,0)"
#muSF="1.0"
usualweights="(1*Weight_PU*"+muSF+"*csvReweighter.getCSVWeight(jetPts,jetEtas,jetCSVs,jetFlavors,internalSystName,csvWgtHF,csvWgtLF,csvWgtCF))"


THEweight=["NomWeight:="+usualweights+"*(DoWeights==1)+(DoWeights==0)*1.0",]


#path='/nfs/dust/cms/user/hmildner/treesMEM0126/'
name='76bdtInputPlotsComparisons'
for cat in DoCats:
  name+='_'+cat
sel_singleel="(N_LooseMuons==0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)" # and vice versa...

# selections for categories
sel1="((N_TightLeptons==1)*(N_LooseLeptons==1)*(N_BTagsM>=2)*(N_Jets>=4))" # l+jets channel
name1="1lge4ge2"

boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.485&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.8925)"                        
s43="((N_Jets==4&&N_BTagsM==3)&&!"+boosted+")"
s44="((N_Jets==4&&N_BTagsM>=4)&&!"+boosted+")"
s53="((N_Jets==5&&N_BTagsM==3)&&!"+boosted+")"
s54="((N_Jets==5&&N_BTagsM>=4)&&!"+boosted+")"
s62="((N_Jets>=6&&N_BTagsM==2)&&!"+boosted+")"
s63="((N_Jets>=6&&N_BTagsM==3)&&!"+boosted+")"
s64="((N_Jets>=6&&N_BTagsM>=4)&&!"+boosted+")"


# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samples=samplesControlPlots
samples_data=samples_data_controlplots
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),sample.selection,sample.nick+sysname))
allsamples=samples+systsamples
allsystnames=weightsystnames+othersystnames

allplots=[]
TwoDimPlots=[]
plots=[]



# weights_Final_43_MEMBDTv2.xml
label="1 lepton, 4 jets, 3 b-tags"
plots43=[
	Plot(ROOT.TH1F("s43_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",30,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_HT","HT",20,0,1000),"BDT_common5_input_HT",s43,label),
        #Plot(ROOT.TH1F("s43_MEM_transformed","MEM discriminator",24,0,1.2),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_third_highest_btag","third highest btag",22,0.79,1),"BDT_common5_input_third_highest_btag",s43,label),
        Plot(ROOT.TH1F("s43_Evt_CSV_Average","avg CSV (jets)",20,0.5,0.9),"Evt_CSV_Average",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_M3","M3",30,0,600),"BDT_common5_input_M3",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",20,0,1000),"BDT_common5_input_all_sum_pt_with_met",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_h1","H_{1}",30,-0.2,0.4),"BDT_common5_input_h1",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",35,0,3.5),"BDT_common5_input_dr_between_lep_and_closest_jet",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_first_jet_pt","jet 1 p_{T}",50,0,500),"BDT_common5_input_first_jet_pt",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",20,0,400),"BDT_common5_input_closest_tagged_dijet_mass",s43,label),
        Plot(ROOT.TH1F("s43_blr","B-tagging likelihood ratio",30,-3,8),"Evt_blr_ETH_transformed",'(N_Jets==4&&N_BTagsM==3)',label),
	Plot(ROOT.TH1F("s43_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",20,0,4),"BDT_common5_input_avg_dr_tagged_jets",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_dev_from_avg_disc_btags","dev from avg CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_min_dr_tagged_jets","min #Delta R(tag,tag)",30,0.3,3.5),"BDT_common5_input_min_dr_tagged_jets",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_h3","H_{3}",30,-0.2,0.9),"BDT_common5_input_h3",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_second_jet_pt","jet 2 p_{T}",40,0,300),"BDT_common5_input_second_jet_pt",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",40,0,200),"BDT_common5_input_fourth_jet_pt",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_maxeta_tag_tag","max #Delta #eta(tag,tag)",20,0.,1.6),"BDT_common5_input_maxeta_tag_tag",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",20,0.,1.6),"BDT_common5_input_maxeta_jet_tag",s43,label),
        Plot(ROOT.TH1F("s43_Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",20,0,3),"Evt_Deta_JetsAverage",s43,label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_third_jet_pt","jet 1 p_{T}",40,0,500),"BDT_common5_input_third_jet_pt",s43,label),
        ]

        
label="1 lepton, 4 jets, 4 b-tags"
thiscatsel=s44
catsuf="s44"
# weights_Final_44_MEMBDTv2.xml
plots44=[
  #Plot(ROOT.TH1F("s44_MEM_transformed","MEM discriminator",6,0,1.2),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",6,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",7,30,100),"BDT_common5_input_fourth_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_first_jet_pt","jet 1 p_{T}",15,0,400),"BDT_common5_input_first_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",15,0,3),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",16,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth-highest CSV",11,0.8,1),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",15,0,1500),"BDT_common5_input_invariant_mass_of_everything",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_M3","M3",15,0,800),"BDT_common5_input_M3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",10,-4,12),"Evt_blr_ETH_transformed",'(N_Jets==4&&N_BTagsM>=4)',label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",10,1.6,3.6),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",12,0,2.4),"BDT_common5_input_min_dr_tagged_jets",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",10,0,1000),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_HT","HT",15,0,1000),"BDT_common5_input_HT",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h1","H_{1}",15,-0.2,0.4),"BDT_common5_input_h1",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third-highest CSV",11,0.8,1),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",15,-0.2,1.0),"BDT_common5_input_h3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_Mlb","mass(lepton,closest tag)",15,0,250),"BDT_common5_input_Mlb",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_second_highest_btag","second-highest CSV",11,0.8,1),"BDT_common5_input_second_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_jet","max #Delta #eta(jet,jet)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h0","H_{0}",15,0.2,0.4),"BDT_common5_input_h0",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_second_jet_pt","jet 2 p_{T}",20,0,250),"BDT_common5_input_second_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dev_from_avg_disc_btags","dev from avg CSV (tags)",15,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h2","H_{2}",15,-0.2,0.4),"BDT_common5_input_h2",thiscatsel,label),
      ]

label="1 lepton, 5 jets, 3 b-tags"
thiscatsel=s53
catsuf="s53"
    # weights_Final_53_MEMBDTv2.xml
plots53=[
	#Plot(ROOT.TH1F(catsuf+"_MEM_transformed","MEM discriminator",20,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",30,0,1500),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third highest CSV",22,.8,1),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth highest CSV",22,-.1,1),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta jets",25,0,2.5),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_CSV_Average","avg CSV",25,0.5,0.9),"Evt_CSV_Average",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",20,-2,10),"Evt_blr_ETH_transformed",'(N_Jets==5&&N_BTagsM==3)',label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h1","H_{1}",27,-.2,.34),"BDT_common5_input_h1",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",30,0.5,3.5),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_sphericity","sphericity",25,0,1),"BDT_common5_input_sphericity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_HT","HT",25,0,1000),"BDT_common5_input_HT",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",25,0,2.4),"BDT_common5_input_min_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",25,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",25,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",25,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",25,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_second_jet_pt","jet 2 p_{T}",20,0,300),"BDT_common5_input_second_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_jet_pt","jet 3 p_{T}",20,0,250),"BDT_common5_input_third_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h2","H_{2}",20,0,0.3),"BDT_common5_input_h2",thiscatsel,label),
]

label="1 lepton, 5 jets, #geq4 b-tags"
thiscatsel=s54
catsuf="s54"

# weights_Final_54_MEMBDTv2.xml
plots54=[
	#Plot(ROOT.TH1F(catsuf+"_MEM_transformed","MEM discriminator",10,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",7,.8,1.04),"BDT_common5_input_avg_btag_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta jets",10,0,2.5),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",15,0,150),"BDT_common5_input_fourth_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_M3","M3",20,0,1000),"BDT_common5_input_M3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",12,0,1200),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h2","H_{2}",15,-.15,0.3),"BDT_common5_input_h2",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",10,1,4),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",10,-2,12),"Evt_blr_ETH_transformed",'(N_Jets==5&&N_BTagsM>=4)',label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",10,80,180),"BDT_common5_input_tagged_dijet_mass_closest_to_125",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_HT","HT",10,0,1000),"BDT_common5_input_HT",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h1","H_{1}",10,-.2,.34),"BDT_common5_input_h1",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_best_higgs_mass","best higgs mass",10,0,400),"BDT_common5_input_best_higgs_mass",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third highest CSV",10,.8,1),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_sphericity","sphericity",10,0,1),"BDT_common5_input_sphericity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",10,0,1),"BDT_common5_input_h3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth highest CSV",10,0.79,1),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fifth_highest_CSV","fifth highest CSV",10,-.1,.91),"BDT_common5_input_fifth_highest_CSV",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",15,0,1.5),"BDT_common5_input_maxeta_jet_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",16,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",15,0,1500),"BDT_common5_input_invariant_mass_of_everything",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",12,0,2.4),"BDT_common5_input_min_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_second_highest_btag","second highest btag",10,.8,1),"BDT_common5_input_second_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h0","H_{0}",10,0.2,1.0),"BDT_common5_input_h0",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_CSV_Average","avg CSV",10,0.5,1),"Evt_CSV_Average",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_jet_pt","jet 3 p_{T}",15,0,200),"BDT_common5_input_third_jet_pt",thiscatsel,label),
   ]
label="1 lepton, #geq6 jets, 2 b-tags"
thiscatsel=s62
catsuf="s62"
# /nfs/dust/cms/user/kelmorab/newTrain/3makeHistosAndCards/weights/CommonWeights/weights_Final_62_v5_OldVars.xml
plots62=[
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h1","H_{1}",27,-0.2,.34),"BDT_common5_input_h1",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",25,0,5),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third highest CSV",22,0,1.1),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_HT","HT",20,0,1400),"BDT_common5_input_HT",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_Mlb","mass(lepton,closest tag)",20,0,250),"BDT_common5_input_Mlb",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fifth_highest_CSV","fifth highest CSV",20,-.1,.91),"BDT_common5_input_fifth_highest_CSV",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth highest CSV",20,-.1,.9),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",20,-5,3),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM==2)',label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",30,0.5,3.4),"BDT_common5_input_min_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",30,.8,1.04),"BDT_common5_input_avg_btag_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta jets",30,0,2.5),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",30,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",30,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",30,0,1.5),"BDT_common5_input_maxeta_jet_jet",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",30,0.2,1.1),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",30,200,1300),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h2","H_{2}",30,-.15,0.3),"BDT_common5_input_h2",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_aplanarity","aplanarity",30,0,0.3),"BDT_common5_input_aplanarity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_CSV_Average","avg CSV",25,0.2,0.65),"Evt_CSV_Average",thiscatsel,label),
        
        Plot(ROOT.TH1F(catsuf+"Evt_Deta_2JetsAverage","Evt_Deta_2JetsAverage", 60,0.0,3),"Evt_Deta_2JetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Deta_3JetsAverage","Evt_Deta_3JetsAverage", 60,0.0,3),"Evt_Deta_3JetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Deta_4JetsAverage","Evt_Deta_4JetsAverage", 60,0.0,3),"Evt_Deta_4JetsAverage",thiscatsel,label),


       Plot(ROOT.TH1F(catsuf+"Evt_Deta_UntaggedJetsAverage","Evt_Deta_UntaggedJetsAverage",45,0.,4.5),"Evt_Deta_UntaggedJetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",45,0.,4.5),"Evt_Deta_TaggedJetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Deta_2TaggedJetsAverage","Evt_Deta_2TaggedJetsAverage", 60,0.0,3),"Evt_Deta_2TaggedJetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Deta_3TaggedJetsAverage","Evt_Deta_3TaggedJetsAverage", 60,0.0,3),"Evt_Deta_3TaggedJetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Deta_4TaggedJetsAverage","Evt_Deta_4TaggedJetsAverage", 60,0.0,3),"Evt_Deta_4TaggedJetsAverage",thiscatsel,label),

       Plot(ROOT.TH1F(catsuf+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",35,0.5,4.),"Evt_Dr_JetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Dr_2JetsAverage","Evt_Dr_2JetsAverage",35,0.5,4.),"Evt_Dr_2JetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Dr_2TaggedJetsAverage","Evt_Dr_2TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_2TaggedJetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Dr_3JetsAverage","Evt_Dr_3JetsAverage",35,0.5,4.),"Evt_Dr_3JetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Dr_3TaggedJetsAverage","Evt_Dr_3TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_3TaggedJetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Dr_4JetsAverage","Evt_Dr_4JetsAverage",35,0.5,4.),"Evt_Dr_4JetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Dr_4TaggedJetsAverage","Evt_Dr_4TaggedJetsAverage",45,0.4,4.9),"Evt_Dr_4TaggedJetsAverage",thiscatsel,label),

       Plot(ROOT.TH1F(catsuf+"Evt_Dr_UntaggedJetsAverage","Evt_Dr_UntaggedJetsAverage",50,0.,5),"Evt_Dr_UntaggedJetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M2_JetsAverage","Evt_M2_JetsAverage",50,0,250),"Evt_M2_JetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M2_UntaggedJetsAverage","Evt_M2_UntaggedJetsAverage",50,0.,250),"Evt_M2_UntaggedJetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",50,0.,250),"Evt_M2_TaggedJetsAverage",thiscatsel,label),

       Plot(ROOT.TH1F(catsuf+"Evt_M2_2JetsAverage","Evt_M2_2JetsAverage",50,0,250),"Evt_M2_2JetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M2_2TaggedJetsAverage","Evt_M2_2TaggedJetsAverage",50,0.,250),"Evt_M2_2TaggedJetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M2_3JetsAverage","Evt_M2_3JetsAverage",50,0,250),"Evt_M2_3JetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M2_3TaggedJetsAverage","Evt_M2_3TaggedJetsAverage",50,0.,250),"Evt_M2_3TaggedJetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M2_4JetsAverage","Evt_M2_4JetsAverage",50,0,250),"Evt_M2_4JetsAverage",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M2_4TaggedJetsAverage","Evt_M2_4TaggedJetsAverage",50,0.,250),"Evt_M2_4TaggedJetsAverage",thiscatsel,label),

       Plot(ROOT.TH1F(catsuf+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,0.,150),"Evt_M_MinDeltaRJets",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M_MinDeltaRUntaggedJets","Evt_M_MinDeltaRUntaggedJets",45,0.,450),"Evt_M_MinDeltaRUntaggedJets",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_M_MinDeltaRLeptonJet","Evt_M_MinDeltaRLeptonJet",60,0.4,3.4),"Evt_M_MinDeltaRLeptonJet",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",50,0.,5.0),"Evt_Dr_MinDeltaRJets",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Dr_MinDeltaRTaggedJets","Evt_Dr_MinDeltaRTaggedJets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Dr_MinDeltaRUntaggedJets","Evt_Dr_MinDeltaRUntaggedJets",50,0.,5.0),"Evt_Dr_MinDeltaRUntaggedJets",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",60,0.4,3.4),"Evt_Dr_MinDeltaRLeptonJet",thiscatsel,label),

       Plot(ROOT.TH1F(catsuf+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_TaggedJet_MaxDeta_Jets","Evt_TaggedJet_MaxDeta_Jets",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_TaggedJet_MaxDeta_TaggedJets","Evt_TaggedJet_MaxDeta_TaggedJets",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",thiscatsel,label),

       Plot(ROOT.TH1F(catsuf+"Evt_M_Total","Evt_M_Total",40,0.,4000),"Evt_M_Total",thiscatsel,label),

       Plot(ROOT.TH1F(catsuf+"Evt_H0","Evt_H0",40,0.5,4.5),"Evt_H0",thiscatsel,label),
       Plot(ROOT.TH1F(catsuf+"Evt_H4","Evt_H4",50,-0.15,0.35),"Evt_H4",thiscatsel,label),
]


label="1 lepton, #geq6 jets, 3 b-tags"
thiscatsel=s63
catsuf="s63"
# weights_Final_63_MEMBDTv2.xml
plots63=[
	#Plot(ROOT.TH1F(catsuf+"_MEM_transformed","MEM discriminator",20,0.,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",15,0,1.5),"BDT_common5_input_maxeta_jet_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",16,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta jets",25,0,2.5),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",25,0,2000),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth-highest b-tag",18,0,0.9),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_aplanarity","aplanarity",20,0,0.4),"BDT_common5_input_aplanarity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",30,.8,1.05),"BDT_common5_input_avg_btag_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",28,0.5,3.9),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",20,0,160),"BDT_common5_input_fourth_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",30,0,300),"BDT_common5_input_tagged_dijet_mass_closest_to_125",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h2","H_{2}",20,-.1,.3),"BDT_common5_input_h2",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fifth_highest_CSV","fifth-highest CSV",20,-.1,.8),"BDT_common5_input_fifth_highest_CSV",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",20,-2,8),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM==3)',label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",17,0,3.4),"BDT_common5_input_min_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dEta_fn","#sqrt{#Delta #eta(t^{lep}, bb) #times #Delta #eta(t^{had}, bb)}",20,0,5),"BDT_common5_input_dEta_fn",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h1","H_{1}",27,-.2,.34),"BDT_common5_input_h1",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third highest CSV",22,0.79,1.1),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.1),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
]
   
label="1 lepton, #geq6 jets, #geq4 b-tags"
thiscatsel=s64
catsuf="s64"
# weights_Final_64_MEMBDTv2.xml
plots64=[
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third-highest CSV",16,.8,1.05),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        #Plot(ROOT.TH1F(catsuf+"_MEM_transformed","MEM discriminator",10,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",14,0,2.8),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",20,0,200),"BDT_common5_input_fourth_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_aplanarity","aplanarity",20,0,0.4),"BDT_common5_input_aplanarity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_M3","M3",20,0,1000),"BDT_common5_input_M3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_jet_pt","jet 3 p_{T}",20,0,250),"BDT_common5_input_third_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",14,0,12),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM>=4)',label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",25,1,3.5),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_best_higgs_mass","best higgs mass",30,0,600),"BDT_common5_input_best_higgs_mass",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",17,40,210),"BDT_common5_input_tagged_dijet_mass_closest_to_125",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth highest btag",22,.8,1),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",25,0,250),"BDT_common5_input_closest_tagged_dijet_mass",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fifth_highest_CSV","fifth highest CSV",22,-.1,1),"BDT_common5_input_fifth_highest_CSV",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_second_highest_btag","second highest btag",22,.8,1),"BDT_common5_input_second_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dr_between_lep_and_closest_jet","min #Delta R (lepton,jet)",25,0,2.5),"BDT_common5_input_dr_between_lep_and_closest_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_HT","HT",10,0,2000),"BDT_common5_input_HT",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",10,200,2000),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",10,400,1600),"BDT_common5_input_invariant_mass_of_everything",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",15,0,1.5),"BDT_common5_input_maxeta_jet_jet",thiscatsel,label),
]

label="boosted"
thiscatsel=boosted+"*(N_Jets>=4&&N_BTagsM>=2)"
catsuf="sBoosted"
# weights_Final_64_MEMBDTv2.xml
plotsBoosted=[
	Plot(ROOT.TH1F(catsuf+"BoostedTopHiggs_HiggsCandidate_M2","BoostedTopHiggs_HiggsCandidate_M2",20,30,250),"BoostedTopHiggs_HiggsCandidate_M2",thiscatsel,label),
 	Plot(ROOT.TH1F(catsuf+"BoostedTopHiggs_HiggsCandidate_Pt2","BoostedTopHiggs_HiggsCandidate_Pt2",20,30,600),"BoostedTopHiggs_HiggsCandidate_Pt2",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"BoostedTopHiggs_HiggsCandidate_Subjetiness21","BoostedTopHiggs_HiggsCandidate_Subjetiness21",20,0,1),"BoostedTopHiggs_HiggsCandidate_Subjetiness2/BoostedTopHiggs_HiggsCandidate_Subjetiness1",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"BoostedTopHiggs_HiggsCandidate_Dr_Lepton","BoostedTopHiggs_HiggsCandidate_Dr_Lepton",20,0,4),"BoostedTopHiggs_HiggsCandidate_Dr_Lepton",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"BoostedTopHiggs_HiggsCandidate_Deta_TopHadCandidate","BoostedTopHiggs_HiggsCandidate_Deta_TopHadCandidate",20,0,4),"BoostedTopHiggs_HiggsCandidate_Deta_TopHadCandidate",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_HT","Evt_HT",20,200,2000),"Evt_HT",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_Dr_MinDeltaRTaggedJets","Evt_Dr_MinDeltaRTaggedJets",20,0,4),"Evt_Dr_MinDeltaRTaggedJets",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,0,600),"Evt_M_MinDeltaRTaggedJets",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",20,0,4),"Evt_Dr_TaggedJetsAverage",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_Sphericity","Evt_Sphericity",20,0,1),"Evt_Sphericity",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"BoostedTopHiggs_TopHadCandidate_Top_M","BoostedTopHiggs_TopHadCandidate_Top_M",20,29,300),"BoostedTopHiggs_TopHadCandidate_Top_M",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"BoostedTopHiggs_TopHadCandidate_B_CSV","BoostedTopHiggs_TopHadCandidate_B_CSV",20,-0.1,1),"BoostedTopHiggs_TopHadCandidate_B_CSV",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"BoostedTopHiggs_TopHadCandidate_W1_CSV","BoostedTopHiggs_TopHadCandidate_W1_CSV",20,-0.1,1),"BoostedTopHiggs_TopHadCandidate_W1_CSV",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"BoostedTopHiggs_TopHadCandidate_W2_CSV","BoostedTopHiggs_TopHadCandidate_W2_CSV",20,-0.1,1),"BoostedTopHiggs_TopHadCandidate_W2_CSV",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_H0","Evt_H0",20,0.2,0.5),"Evt_H0",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_H3","Evt_H3",20,0,1),"Evt_H3",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_JetPtOverJetE","Evt_JetPtOverJetE",20,0,1),"Evt_JetPtOverJetE",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_Deta_JetsAverage","Evt_Deta_JetsAverage",20,0,2.5),"Evt_Deta_JetsAverage",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"CSV2","CSV2",20,-0.1,1),"CSV[2]",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"CSV3","CSV3",20,-0.1,1),"CSV[3]",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"CSV4","CSV4",20,-0.1,1),"CSV[4]",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_CSV_Average","Evt_CSV_Average",20,0,1),"Evt_CSV_Average",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_TaggedJet_MaxDeta_TaggedJets","Evt_TaggedJet_MaxDeta_TaggedJets",20,0,4),"Evt_TaggedJet_MaxDeta_TaggedJets",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,0,800),"Evt_M_MedianTaggedJets",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_Deta_2TaggedJetsAverage","Evt_Deta_2TaggedJetsAverage",20,0,4),"Evt_Deta_2TaggedJetsAverage",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_Aplanarity","Evt_Aplanarity",20,0,0.4),"Evt_Aplanarity",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0,0.006),"BDT_common5_input_dev_from_avg_disc_btags",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,0,3000),"BDT_common5_input_invariant_mass_of_everything",thiscatsel,label),
  Plot(ROOT.TH1F(catsuf+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0,200),"BDT_common5_input_Mlb",thiscatsel,label),
  Plot(ROOT.TH1F(catsuf+"Evt_M_Total","Evt_M_Total",20,400,4000),"Evt_M_Total",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"Evt_CSV_Dev","Evt_CSV_Dev",20,0,0.25),"Evt_CSV_Dev",thiscatsel,label),
]

listOf1DPlotLists=[]
for cat in DoCats:
  if cat=='43':
    listOf1DPlotLists.append(plots43)
  if cat=='44':
      listOf1DPlotLists.append(plots44)
  if cat=='53':
      listOf1DPlotLists.append(plots53)
  if cat=='54':
      listOf1DPlotLists.append(plots54)
  if cat=='62':
      listOf1DPlotLists.append(plots62)
  if cat=='63':
      listOf1DPlotLists.append(plots63)
  if cat=='64':
      listOf1DPlotLists.append(plots64)
  if cat=='boosted':
      listOf1DPlotLists.append(plotsBoosted)


#listOf1DPlotLists=[plots64,plots63,plots62,plots54,plots53,plots44,plots43]

TwoDimPlots=[]
for plotlist in listOf1DPlotLists:
  #print plotlist
  for ipl1, plot1 in enumerate(plotlist):
    for plot2 in plotlist:
      newName=plot1.name+"VS"+plot2.name
      newTitle=plot1.histo.GetTitle()+" VS "+plot2.histo.GetTitle()
      bins1=plot1.histo.GetNbinsX()
      minX1=plot1.histo.GetXaxis().GetXmin()
      maxX1=plot1.histo.GetXaxis().GetXmax()
      bins2=plot2.histo.GetNbinsX()
      minX2=plot2.histo.GetXaxis().GetXmin()
      maxX2=plot2.histo.GetXaxis().GetXmax()
      #newvarexp=plot2.variable+":"+plot1.variable
      newsel=plot1.selection
      newlabel=plot1.label
      TwoDimPlots+=[TwoDimPlot(ROOT.TH2F(newName,newTitle+";"+plot1.histo.GetTitle()+";"+plot2.histo.GetTitle(),bins1,minX1,maxX1,bins2,minX2,maxX2),plot1.variable,plot2.variable,newsel,newlabel)]

OneDimplots=[]
for plotlist in listOf1DPlotLists:
  OneDimplots+=plotlist
allplots=OneDimplots+TwoDimPlots

# plot parallel -- alternatively there are also options to plot more traditional that also return lists of histo lists
outputpath=plotParallel(name,2000000,allplots,samplesGenerators+samples_data,[''],['1.'],[''],THEweight)

#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,OneDimplots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,OneDimplots,1)
#if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    #renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames)

#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],OneDimplots,errorSystnames)
#lllforPS=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],OneDimplots,PSSystnames)

#labels=[plot.label for plot in OneDimplots]
#lolT=transposeLOL(listOfHistoLists)
#plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name,[[lll,3354,ROOT.kGray+1,True],[lllforPS,3545,ROOT.kYellow,False]],False,labels)

listOfHistoListsDataForGenerators=createHistoLists_fromSuperHistoFile(outputpath,samples_data,allplots,1,[""],True)
listOfHistoListsGenerators=createHistoLists_fromSuperHistoFile(outputpath,samplesGenerators,allplots,1,[""],True)
#print "genData"
print listOfHistoListsDataForGenerators
#print "Generators"
print listOfHistoListsGenerators

#TlistOfHistoListsDataForGenerators=transposeLOL(listOfHistoListsDataForGenerators)
#TlistOfHistoListsGenerators=transposeLOL(listOfHistoListsGenerators)
#print TlistOfHistoListsDataForGenerators
#print TlistOfHistoListsGenerators

listOfComparisonLists=[]
for histolistData, histoListGenerators in zip(listOfHistoListsDataForGenerators, listOfHistoListsGenerators):
  thishisto=histolistData[0].Clone()
  thishisto.Add(histolistData[1])
  thislist=[thishisto]
  for histo in histoListGenerators:
    thislist.append(histo)
  listOfComparisonLists.append(thislist)
print listOfComparisonLists
#raw_input()
labels=[plot.label for plot in allplots]

outname='comparisonsBDT'
for cat in DoCats:
  outname+=cat
print "plotting"
# this is just a dummy sample
samplesForComparison=[Sample('data',ROOT.kBlack,path_76x+'/mu_*/*nominal*.root','','SingleMu'),]+samplesGenerators
writeListOfHistoLists(listOfComparisonLists,samplesForComparison,labels,outname,True,False,False,'histoE',True,False,True,True)
