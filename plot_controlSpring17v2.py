#############
# plot general control distributions
##############

from plotconfigSpring17v2 import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos

name='controlplotsSpring17v2p2_ttbarincl'

# if one wants to plot blinded: True (default: False)
plotBlinded = False

bdtset="V4"
additionalvariables=[
                      "Jet_Pt","Jet_Eta","Jet_CSV","Jet_Flav","N_Jets","Weight_CSV","Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown","Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down","Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down","Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down",
]

# selections
boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.485&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.8925)"
toptaggersel="(BoostedJet_Top_Pt[0]>=0)"
higgstaggersel="(BoostedJet_Filterjet2_Pt[0]>=0)"

# definition of categories
categoriesJT=[
              ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
              ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
              ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
              ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
              ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
              ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
              ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
]


# selections for categories
categoriesJTsel="("+categoriesJT[0][0]
for cat in categoriesJT[1:]:
  categoriesJTsel+="||"+cat[0]
categoriesJTsel+=")"


# category strings
catstringJT="0"
for i,cat in enumerate(categoriesJT):
    catstringJT+=("+"+str(i+1)+"*"+cat[0])
#catstringJTB="0"
#for i,cat in enumerate(categoriesJTB):
    #catstringJTB+=("+"+str(i+1)+"*"+cat[0])

# samples
samples=samplesControlPlots
samples_data=samples_data_controlplots
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    thisnewsel=sample.selection
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))

allsamples=samples+systsamples
allsystnames=weightsystnames+othersystnames

# book plots
plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
plotlabelboosted="#splitline{1 lepton, #geq 4 jets, #geq 2 b-tags}{#geq 1 C/A 1.5 jet p_{T} > 200 GeV}"
plotselection="(N_Jets>=4&&N_BTagsM>=2)"
plots=[
    Plot(ROOT.TH1F("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,categoriesJTsel,"1 lepton"),
    #Plot(ROOT.TH1F("BCAT" ,"jet-tag + boosted categories",len(categoriesJTB),0.5,0.5+len(categoriesJTB)),catstringJTB,categoriesJTBsel,"1 lepton"),
    Plot(ROOT.TH1F("N_Jets","Number of ak4 jets",7,3.5,10.5),"N_Jets",plotselection,plotlabel),
    Plot(ROOT.TH1F("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",plotselection,plotlabel),
    Plot(ROOT.TH1F("CSV0","B-tag of leading jet",22,-.1,1),"Jet_CSV[0]",plotselection,plotlabel),
    Plot(ROOT.TH1F("CSV1","B-tag of second jet",22,-.1,1),"Jet_CSV[1]",plotselection,plotlabel),
    Plot(ROOT.TH1F("CSV","B-tag of all jets",22,-.1,1),"Jet_CSV",plotselection,plotlabel),

    #Plot(ROOT.TH1F("CSV0NPVgeq20","B-tag of leading jet (NPV#geq20)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
    #Plot(ROOT.TH1F("CSV1NPVgeq20","B-tag of second jet (NPV#geq20)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
    #Plot(ROOT.TH1F("CSVNPVgeq20","B-tag of all jets (NPV#geq20)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),

    #Plot(ROOT.TH1F("CSV0NPV15to20","B-tag of leading jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
    #Plot(ROOT.TH1F("CSV1NPV15to20","B-tag of second jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
    #Plot(ROOT.TH1F("CSVNPV15to20","B-tag of all jets (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),

    #Plot(ROOT.TH1F("CSV0NPV10to15","B-tag of leading jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),
    #Plot(ROOT.TH1F("CSV1NPV10to15","B-tag of second jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),
    #Plot(ROOT.TH1F("CSVNPV10to15","B-tag of all jets (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),

    #Plot(ROOT.TH1F("CSV0NPV0to10","B-tag of leading jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),
    #Plot(ROOT.TH1F("CSV1NPV0to10","B-tag of second jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),
    #Plot(ROOT.TH1F("CSVNPV0to10","B-tag of all jets (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),


    Plot(ROOT.TH1F("pt1","p_{T} of leading jet",50,0,500),"Jet_Pt[0]",plotselection,plotlabel),
    Plot(ROOT.TH1F("pt2","p_{T} of second jet",50,0,500),"Jet_Pt[1]",plotselection,plotlabel),
    Plot(ROOT.TH1F("pt3","p_{T} of third jet",40,0,400),"Jet_Pt[2]",plotselection,plotlabel),
    Plot(ROOT.TH1F("pt4","p_{T} of fourth jet",60,0,300),"Jet_Pt[3]",plotselection,plotlabel),
    Plot(ROOT.TH1F("pt5","p_{T} of fifth jet",40,0,200),"Jet_Pt[4]",plotselection,plotlabel),
    Plot(ROOT.TH1F("pt6","p_{T} of sixth jet",40,0,200),"Jet_Pt[5]",plotselection,plotlabel),
    #Plot(ROOT.TH1F("pt1tagged","p_{T} of leading tagged jet",50,0,500),"TaggedJet_Pt[0]",plotselection,plotlabel),
    #Plot(ROOT.TH1F("pt2tagged","p_{T} of second tagged jet",50,0,500),"TaggedJet_Pt[1]",plotselection,plotlabel),
    #Plot(ROOT.TH1F("pt3tagged","p_{T} of third tagged jet",40,0,400),"TaggedJet_Pt[2]",plotselection,plotlabel),
    #Plot(ROOT.TH1F("pt4tagged","p_{T} of fourth tagged jet",60,0,300),"TaggedJet_Pt[3]",plotselection,plotlabel),


    Plot(ROOT.TH1F("eta1","#eta of leading jet",50,-2.5,2.5),"Jet_Eta[0]",plotselection,plotlabel),
    Plot(ROOT.TH1F("eta2","#eta of second jet",50,-2.5,2.5),"Jet_Eta[1]",plotselection,plotlabel),
    Plot(ROOT.TH1F("phij1","#phi of leading jet",64,-3.2,3.2),"Jet_Phi[0]",plotselection,plotlabel),
    Plot(ROOT.TH1F("phij2","#phi of second jet",64,-3.2,3.2),"Jet_Phi[1]",plotselection,plotlabel),
    Plot(ROOT.TH1F("Evt_HT_Jets","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
    Plot(ROOT.TH1F("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",plotselection,plotlabel),
    Plot(ROOT.TH1F("csvalljets","csv of all jets",44,-.1,1),"Jet_CSV",plotselection,plotlabel),
    Plot(ROOT.TH1F("leppt","lepton p_{T}",50,0,200),"LooseLepton_Pt[0]",plotselection,plotlabel),
    Plot(ROOT.TH1F("lepeta","lepton #eta",50,-2.5,2.5),"LooseLepton_Eta[0]",plotselection,plotlabel),
    Plot(ROOT.TH1F("elleppt","electron p_{T}",50,0,200),"Electron_Pt[0]",'Electron_Pt[0]>10',plotlabel),
    Plot(ROOT.TH1F("ellepeta","electron #eta",50,-2.5,2.5),"Electron_Eta[0]",'Electron_Pt[0]>10',plotlabel),
    Plot(ROOT.TH1F("muleppt","muon p_{T}",50,0,200),"Muon_Pt[0]",'Muon_Pt[0]>10',plotlabel),
    Plot(ROOT.TH1F("mulepeta","muon #eta",50,-2.5,2.5),"Muon_Eta[0]",'Muon_Pt[0]>10',plotlabel),

    #Plot(ROOT.TH1F("Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX","Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",50,0,2.0),"Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",plotselection,plotlabel),
    #Plot(ROOT.TH1F("Prescale_HLT_IsoMu22_vX","Prescale_HLT_IsoMu22_vX",50,0,2.0),"Prescale_HLT_IsoMu22_vX",plotselection,plotlabel),
    #Plot(ROOT.TH1F("Prescale_HLT_IsoTkMu22_vX","Prescale_HLT_IsoTkMu22_vX",50,0,2.0),"Prescale_HLT_IsoTkMu22_vX",plotselection,plotlabel),

    #Plot(ROOT.TH1F("eliso","electron relative isolation",50,0,0.15),"Electron_RelIso[0]",plotselection,plotlabel),
    #Plot(ROOT.TH1F("muiso","muon relative isolation",50,0,0.15),"Muon_RelIso[0]",plotselection,plotlabel),
    Plot(ROOT.TH1F("MET","missing transverse energy",50,0,200),"Evt_Pt_MET",plotselection,plotlabel),
    Plot(ROOT.TH1F("METphi","MET #phi",64,-3.2,3.2),"Evt_Phi_MET",plotselection,plotlabel),
    Plot(ROOT.TH1F("N_PrimaryVertices","Reconstructed primary vertices",26,-.5,25.5),"N_PrimaryVertices",plotselection,plotlabel),
    Plot(ROOT.TH1F("blrAll","B-tagging likelihood ratio",44,-6,10),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",plotselection,plotlabel),
    Plot(ROOT.TH1F("Evt_M_MinDeltaRJets","dijet mass of closest jets",30,0.,150),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
    Plot(ROOT.TH1F("Evt_M_MinDeltaRTaggedJets","mass of closest tagged jets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
    Plot(ROOT.TH1F("Evt_Dr_MinDeltaRJets","#Delta R of closest jets",50,0.,5.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
    Plot(ROOT.TH1F("Evt_Dr_MinDeltaRTaggedJets","#Delta R of closest tagged jets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
    Plot(ROOT.TH1F("Evt_Jet_MaxDeta_Jets","max #Delta #eta (jet,jet)",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
    Plot(ROOT.TH1F("Evt_TaggedJet_MaxDeta_Jets","max #Delta #eta (tag,jet)",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",plotselection,plotlabel),
    Plot(ROOT.TH1F("Evt_TaggedJet_MaxDeta_TaggedJets","max #Delta #eta (tag,tag)",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",plotselection,plotlabel),
    #Plot(ROOT.TH1F("Evt_H1","Evt_H1",60,-0.2,0.4),"Evt_H1",plotselection,plotlabel),
    #Plot(ROOT.TH1F("Evt_H2","Evt_H2",60,-0.2,0.4),"Evt_H2",plotselection,plotlabel),
    #Plot(ROOT.TH1F("Evt_H3","Evt_H3",50,-0.05,1.05),"Evt_H3",plotselection,plotlabel),
    #Plot(ROOT.TH1F("Evt_H4","Evt_H4",50,-0.15,0.35),"Evt_H4",plotselection,plotlabel),
    #Plot(ROOT.TH1F("Sphericity","Sphericity",50,0,1),"Evt_Sphericity",plotselection,plotlabel),
    #Plot(ROOT.TH1F("Aplanarity","Aplanarity",50,0,0.5),"Evt_Aplanarity",plotselection,plotlabel),
    Plot(ROOT.TH1F("Evt_Deta_UntaggedJetsAverage","avg. #Delta #eta of untagged jets",45,0.,4.5),"Evt_Deta_UntaggedJetsAverage",plotselection,plotlabel),
    Plot(ROOT.TH1F("Evt_Deta_TaggedJetsAverage","avg. #Delta #eta of tagged jets",45,0.,4.5),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
]


plotlabel="1 lepton, 4 jets, 2 b-tags"
plotselection="((N_Jets==4&&N_BTagsM==2))"
#plotselection="((N_Jets==4&&N_BTagsM==2)&&!"+boosted+")"

plotprefix="4j2t"
plots42=[
    Plot(ROOT.TH1F(plotprefix+"Evt_HT","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
]

plotlabel="1 lepton, 5 jets, 2 b-tags"
plotselection="((N_Jets==5&&N_BTagsM==2))"
#plotselection="((N_Jets==5&&N_BTagsM==2)&&!"+boosted+")"

plotprefix="s52_"
plots52=[
    Plot(ROOT.TH1F(plotprefix+"Evt_HT","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
]

plotlabel="1 lepton, 4 jets, 3 b-tags"
plotselection=categoriesJT[1][0]
plotprefix="s43_"
plots43=[
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_HT","HT",20,0,1000),"BDT_common5_input_HT",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_third_highest_btag","third highest btag",22,0.79,1),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_h1","H_{1}",30,-0.2,0.4),"BDT_common5_input_h1",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",35,0,3.5),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_blr","B-tagging likelihood ratio",30,-3,8),"Evt_blr_ETH_transformed",'(N_Jets==4&&N_BTagsM==3)',plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_dev_from_avg_disc_btags","dev from avg b-tag (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"s43_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",32,0,160),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
]


plotlabel="1 lepton, 4 jets, 4 b-tags"
plotselection=categoriesJT[4][0]
plotprefix="s44_"
# weights_Final_44_MEMBDTv2.xml
plots44=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",6,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","dijet mass of closest tagged jets",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",10,0,1000),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h3","H_{3}",15,-0.2,1.0),"BDT_common5_input_h3",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
]


plotlabel="1 lepton, 5 jets, 3 b-tags"
plotselection=categoriesJT[2][0]
plotprefix="s53_"
plots53=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",30,0,1500),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",20,-2,10),"Evt_blr_ETH_transformed",'(N_Jets==5&&N_BTagsM==3)',plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",30,0.5,3.5),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_sphericity","sphericity",25,0,1),"BDT_common5_input_sphericity",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",25,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",25,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,avg tag #eta)",25,0,1.5),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_third_jet_pt","jet 3 p_{T}",20,0,250),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","H_{2}",20,0,0.15),"BDT_common5_input_h2",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","dijet mass of closest tagged jets",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
]


plotlabel="1 lepton, 5 jets, #geq4 b-tags"
plotselection=categoriesJT[5][0]
plotprefix="s54_"
plots54=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",7,.8,1.04),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_Deta_JetsAverage","avg #Delta #eta jets",10,0,2.5),"Evt_Deta_JetsAverage",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_M3","M3",20,0,1000),"BDT_common5_input_M3",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",12,0,1200),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",10,1,4),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",10,80,180),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_HT","HT",10,0,1000),"BDT_common5_input_HT",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity",plotselection,plotlabel),
    #Plot(ROOT.TH1F(plotprefix+"Evt_H1","Evt_H1",60,-0.2,0.4),"Evt_H1",plotselection,plotlabel),
    #Plot(ROOT.TH1F(plotprefix+"Evt_H2","Evt_H2",60,-0.2,0.4),"Evt_H2",plotselection,plotlabel),
    #Plot(ROOT.TH1F(plotprefix+"Evt_H3","Evt_H3",50,-0.05,1.05),"Evt_H3",plotselection,plotlabel),
    #Plot(ROOT.TH1F(plotprefix+"Evt_H4","Evt_H4",50,-0.15,0.35),"Evt_H4",plotselection,plotlabel),
    #Plot(ROOT.TH1F(plotprefix+"Sphericity","Sphericity",50,0,1),"Evt_Sphericity",plotselection,plotlabel),
    #Plot(ROOT.TH1F(plotprefix+"Aplanarity","Aplanarity",50,0,0.5),"Evt_Aplanarity",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_TaggedJet_MaxDeta_Jets","Evt_TaggedJet_MaxDeta_Jets",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_TaggedJet_MaxDeta_TaggedJets","Evt_TaggedJet_MaxDeta_TaggedJets",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRTaggedJets","Evt_Dr_MinDeltaRTaggedJets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_Dr_MinDeltaRUntaggedJets","Evt_Dr_MinDeltaRUntaggedJets",50,0.,5.0),"Evt_Dr_MinDeltaRUntaggedJets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_M_MinDeltaRUntaggedJets","Evt_M_MinDeltaRUntaggedJets",45,0.,450),"Evt_M_MinDeltaRUntaggedJets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_Deta_UntaggedJetsAverage","Evt_Deta_UntaggedJetsAverage",45,0.,4.5),"Evt_Deta_UntaggedJetsAverage",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",45,0.,4.5),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
]


plotlabel="1 lepton, #geq6 jets, 2 b-tags"
plotselection=categoriesJT[0][0]
plotprefix="s62_"
plots62=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h1","H_{1}",27,-0.2,.34),"BDT_common5_input_h1",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_Mlb","mass(lepton,closest tag)",20,0,250),"BDT_common5_input_Mlb",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",20,-5,3),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM==2)',plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",30,0.5,3.4),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",30,.8,1.04),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,avg tag #eta)",30,0,1.5),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",30,0.2,1.1),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",30,200,1300),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_h2","H_{2}",30,-.15,0.3),"BDT_common5_input_h2",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",30,0,0.3),"BDT_common5_input_aplanarity",plotselection,plotlabel),
]


plotlabel="1 lepton, #geq6 jets, 3 b-tags"
plotselection=categoriesJT[3][0]
plotprefix="s63_"
plots63=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",25,0,2000),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_aplanarity","aplanarity",20,0,0.4),"BDT_common5_input_aplanarity",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"blr","B-tagging likelihood ratio",20,-2,8),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM==3)',plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",17,0,3.4),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_dEta_fn","#sqrt{#Delta #eta(t^{lep}, bb) #times #Delta #eta(t^{had}, bb)}",20,0,5),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.1),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
]

plotlabel="1 lepton, #geq6 jets, #geq4 b-tags"
plotselection=categoriesJT[6][0]
plotprefix="s64"
plots64=[
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_best_higgs_mass","best higgs mass",30,0,600),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",17,40,210),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fourth_highest_btag","fourth highest btag",22,.8,1),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_fifth_highest_CSV","fifth highest CSV",22,-.1,1),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",10,200,2000),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
    Plot(ROOT.TH1F(plotprefix+"BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",10,400,1600),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
]


bdtplots=plots64+plots63+plots62+plots54+plots53+plots44+plots43+plots42+plots52
plots+=bdtplots
#plots=plots44
#plots+=plots62+plots63

print name,2000000,plots,samples+samples_data,[''],['1.'],weightsystnames, systweights
outputpath=plotParallel(name,2000000,plots,samples+samples_data+systsamples,[''],['1.'],weightsystnames, systweights,additionalvariables,[],"")

# plot dataMC comparison
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames,False)
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)


labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name,[[lll,3354,ROOT.kBlack,True]],False,labels,True,plotBlinded)

#exit(0)

# make log plots
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,errorSystnames)
#lllcsv=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,CSVSystnames)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name+'_log',[[lll,3354,ROOT.kBlack,True]],True,labels,True,plotBlinded)

# make category plots
categoryplotsindex=3
listOfHistoListsForCategories=createHistoLists_fromSuperHistoFile(outputpath,samples,plots[:categoryplotsindex],1)
listOfHistoListsDataForCategories=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots[:categoryplotsindex],1)
lllForCategories=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots[:categoryplotsindex],errorSystnames)

listOfcustomBinLabels=[]

categoriesJTlist=[]
for i,cat in enumerate(categoriesJT):
  categoriesJTlist.append(cat[1])
#categoriesJTBlist=[]
#for i,cat in enumerate(categoriesJTB):
  #categoriesJTBlist.append(cat[1])
#categoriesSplitByBDToptDlist=[]
#for i,cat in enumerate(categoriesSplitByBDToptD):
  #categoriesSplitByBDToptDlist.append(cat[1])

listOfcustomBinLabels=[categoriesJTlist]
labels=[plot.label for plot in plots[:categoryplotsindex]]
lolT=transposeLOL(listOfHistoListsForCategories)
plotDataMCanWsystCustomBinLabels(listOfHistoListsDataForCategories,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name+'Categories_log',[[lllForCategories,3354,ROOT.kBlack,True]],listOfcustomBinLabels,True,labels,True,plotBlinded)



# make category plots
# again without log
categoryplotsindex=3
listOfHistoListsForCategoriesNL=createHistoLists_fromSuperHistoFile(outputpath,samples,plots[:categoryplotsindex],1)
listOfHistoListsDataForCategoriesNL=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots[:categoryplotsindex],1)
lllForCategoriesNL=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots[:categoryplotsindex],errorSystnames)

listOfcustomBinLabels=[]

categoriesJTlist=[]
for i,cat in enumerate(categoriesJT):
  categoriesJTlist.append(cat[1])

listOfcustomBinLabels=[categoriesJTlist]
labels=[plot.label for plot in plots[:categoryplotsindex]]
lolTNL=transposeLOL(listOfHistoListsForCategoriesNL)
plotDataMCanWsystCustomBinLabels(listOfHistoListsDataForCategoriesNL,transposeLOL(lolTNL[1:]),samples[1:],lolTNL[0],samples[0],-1,name+'Categories_nolog',[[lllForCategoriesNL,3354,ROOT.kBlack,True]],listOfcustomBinLabels,False,labels,True,plotBlinded)
