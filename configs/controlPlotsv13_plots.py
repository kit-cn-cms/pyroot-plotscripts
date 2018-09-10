import sys
import os

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses
import ROOT

memexp = ""
# definition of categories
categoriesJT = [
    ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
    ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
    ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
    ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
    ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
    ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
    ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
]

# define event yield categories
def evtYieldCategories():
    return categoriesJT

# selection of categories
categoriesJTsel = "("+categoriesJT[0][0]
for cat in categoriesJT[1:]:
    categoriesJTsel += "||"+cat[0]
categoriesJTsel += ")"

# category strings
catstringJT="0"
for i, cat in enumerate(categoriesJT):
    catstringJT += ("+"+str(i+1)+"*"+cat[0])


def add_plots():
    # book plots
    plotLabel = "1 lepton, #geq 4 jets, #geq 2 b-tags"
    plotSelection = "(N_Jets>=4&&N_BTagsM>=2)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,categoriesJTsel,"1 lepton"),
        #plotClasses.Plot(ROOT.TH1D("BCAT" ,"jet-tag + boosted categories",len(categoriesJTB),0.5,0.5+len(categoriesJTB)),catstringJTB,categoriesJTBsel,"1 lepton"),
        plotClasses.Plot(ROOT.TH1D("N_Jets","Number of ak4 jets",11,3.5,14.5),"N_Jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("CSV0","B-tag of leading jet",22,-.1,1),"Jet_CSV[0]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("CSV1","B-tag of second jet",22,-.1,1),"Jet_CSV[1]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("CSV","B-tag of all jets",22,-.1,1),"Jet_CSV",plotSelection,plotLabel),

        plotClasses.Plot(ROOT.TH1D("eta1","#eta of leading jet",50,-2.5,2.5),"Jet_Eta[0]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("eta2","#eta of second jet",50,-2.5,2.5),"Jet_Eta[1]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("phij1","#phi of leading jet",64,-3.2,3.2),"Jet_Phi[0]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("phij2","#phi of second jet",64,-3.2,3.2),"Jet_Phi[1]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("Evt_HT_Jets","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("etaalljets","#eta of all jets",60,-2.5,2.5),"Jet_Eta",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("pumvaalljets","PU MVA of all jets",60,0,1.0),"Jet_PileUpMVA",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("puidalljets","PU MVA of all jets",60,0,1.0),"Jet_PileUpID",plotSelection,plotLabel),

        plotClasses.Plot(ROOT.TH1D("csvalljets","csv of all jets",44,-.1,1),"Jet_CSV",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("leppt","lepton p_{T}",50,0,200),"LooseLepton_Pt[0]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("lepeta","lepton #eta",50,-2.5,2.5),"LooseLepton_Eta[0]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("elleppt","electron p_{T}",50,0,200),"Electron_Pt[0]",'Electron_Pt[0]>10',plotLabel),
        plotClasses.Plot(ROOT.TH1D("ellepeta","electron #eta",50,-2.5,2.5),"Electron_Eta[0]",'Electron_Pt[0]>10',plotLabel),
        plotClasses.Plot(ROOT.TH1D("muleppt","muon p_{T}",50,0,200),"Muon_Pt[0]",'Muon_Pt[0]>10',plotLabel),
        plotClasses.Plot(ROOT.TH1D("mulepeta","muon #eta",50,-2.5,2.5),"Muon_Eta[0]",'Muon_Pt[0]>10',plotLabel),

        plotClasses.Plot(ROOT.TH1D("N_AK8_Jets","Number of ak8 jets",10,0.5,10.5),"N_AK8Jets",plotSelection,plotLabel),
    ]
    

    # additional plots
    plotsAdditional = [
        #plotClasses.Plot(ROOT.TH1D("CSV0NPVgeq20","B-tag of leading jet (NPV#geq20)",22,-.1,1),"Jet_CSV[0]",plotSelection+"*(N_PrimaryVertices>=20)",plotLabel),
        #plotClasses.Plot(ROOT.TH1D("CSV1NPVgeq20","B-tag of second jet (NPV#geq20)",22,-.1,1),"Jet_CSV[1]",plotSelection+"*(N_PrimaryVertices>=20)",plotLabel),
        #plotClasses.Plot(ROOT.TH1D("CSVNPVgeq20","B-tag of all jets (NPV#geq20)",22,-.1,1),"Jet_CSV",plotSelection+"*(N_PrimaryVertices>=20)",plotLabel),

        #plotClasses.Plot(ROOT.TH1D("CSV0NPV15to20","B-tag of leading jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[0]",plotSelection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotLabel),
        #plotClasses.Plot(ROOT.TH1D("CSV1NPV15to20","B-tag of second jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[1]",plotSelection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotLabel),
        #plotClasses.Plot(ROOT.TH1D("CSVNPV15to20","B-tag of all jets (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV",plotSelection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotLabel),

        #plotClasses.Plot(ROOT.TH1D("CSV0NPV10to15","B-tag of leading jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[0]",plotSelection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotLabel),
        #plotClasses.Plot(ROOT.TH1D("CSV1NPV10to15","B-tag of second jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[1]",plotSelection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotLabel),
        #plotClasses.Plot(ROOT.TH1D("CSVNPV10to15","B-tag of all jets (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV",plotSelection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotLabel),

        #plotClasses.Plot(ROOT.TH1D("CSV0NPV0to10","B-tag of leading jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[0]",plotSelection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotLabel),
        #plotClasses.Plot(ROOT.TH1D("CSV1NPV0to10","B-tag of second jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[1]",plotSelection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotLabel),
        #plotClasses.Plot(ROOT.TH1D("CSVNPV0to10","B-tag of all jets (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV",plotSelection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotLabel),


        plotClasses.Plot(ROOT.TH1D("pt1","p_{T} of leading jet",50,0,500),"Jet_Pt[0]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("pt2","p_{T} of second jet",50,0,500),"Jet_Pt[1]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("pt3","p_{T} of third jet",40,0,400),"Jet_Pt[2]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("pt4","p_{T} of fourth jet",60,0,300),"Jet_Pt[3]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("pt5","p_{T} of fifth jet",40,0,200),"Jet_Pt[4]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("pt6","p_{T} of sixth jet",40,0,200),"Jet_Pt[5]",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("pt2tagged","p_{T} of second tagged jet",50,0,500),"TaggedJet_Pt[1]",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("pt1tagged","p_{T} of leading tagged jet",50,0,500),"TaggedJet_Pt[0]",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("pt3tagged","p_{T} of third tagged jet",40,0,400),"TaggedJet_Pt[2]",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("pt4tagged","p_{T} of fourth tagged jet",60,0,300),"TaggedJet_Pt[3]",plotSelection,plotLabel),

        #plotClasses.Plot(ROOT.TH1D("Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX","Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",50,0,2.0),"Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Prescale_HLT_IsoMu22_vX","Prescale_HLT_IsoMu22_vX",50,0,2.0),"Prescale_HLT_IsoMu22_vX",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Prescale_HLT_IsoTkMu22_vX","Prescale_HLT_IsoTkMu22_vX",50,0,2.0),"Prescale_HLT_IsoTkMu22_vX",plotSelection,plotLabel),

        plotClasses.Plot(ROOT.TH1D("eliso","electron relative isolation",50,0,0.15),"Electron_RelIso[0]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("muiso","muon relative isolation",50,0,0.15),"Muon_RelIso[0]",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("MET","missing transverse energy",50,0,200),"Evt_Pt_MET",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("METphi","MET #phi",64,-3.2,3.2),"Evt_Phi_MET",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("N_PrimaryVertices","Reconstructed primary vertices",26,-.5,50.5),"N_PrimaryVertices",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D("blrAll","B-tagging likelihood ratio",44,-6,10),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_M_MinDeltaRJets","dijet mass of closest jets",30,0.,150),"Evt_M_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_M_MinDeltaRTaggedJets","mass of closest tagged jets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Dr_MinDeltaRJets","#Delta R of closest jets",50,0.,5.0),"Evt_Dr_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Dr_MinDeltaRTaggedJets","#Delta R of closest tagged jets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Jet_MaxDeta_Jets","max #Delta #eta (jet,jet)",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_TaggedJet_MaxDeta_Jets","max #Delta #eta (tag,jet)",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_TaggedJet_MaxDeta_TaggedJets","max #Delta #eta (tag,tag)",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D("Evt_H1","Evt_H1",60,-0.2,0.4),"Evt_H1",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_H2","Evt_H2",60,-0.2,0.4),"Evt_H2",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_H3","Evt_H3",50,-0.05,1.05),"Evt_H3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_H4","Evt_H4",50,-0.15,0.35),"Evt_H4",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Sphericity","Sphericity",50,0,1),"Evt_Sphericity",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Aplanarity","Aplanarity",50,0,0.5),"Evt_Aplanarity",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Deta_UntaggedJetsAverage","avg. #Delta #eta of untagged jets",50,0.,4.5),"Evt_Deta_UntaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Deta_TaggedJetsAverage","avg. #Delta #eta of tagged jets",50,0.,4.5),"Evt_Deta_TaggedJetsAverage",plotSelection,plotLabel),

        #plotClasses.Plot(ROOT.TH1D("Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",50,-0.1,1),"Reco_Sum_LikelihoodRatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",50,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",50,-0.1,200),"BDT_common5_input_closest_tagged_dijet_mass",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",50,-0.1,500),"Evt_Pt_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",50,-0.1,300),"Evt_M_MedianTaggedJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D("Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D("Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",50,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",50,50,200),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_M_MinDeltaRLeptonJet","mass of lepton and closest jet",30,0.,150),"Evt_M_MinDeltaRLeptonJet",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D("Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",50,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D("Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",50,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D("Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",50,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",50,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotSelection,plotLabel),


    ]

    return plots + plotsAdditional


def add_ak8jets():
    plotLabel = "1 lepton, #geq 4 jets, #geq 2 b-tags"
    plotSelectionBoosted="(N_Jets>=4&&N_BTagsM>=2&&N_AK8Jets>=1)*(AK8Jet_Pt>200)"   

    # AK8Jets
    plotsAK8Jets = [
        plotClasses.Plot(ROOT.TH1D("ptallak8jets","p_{T} of all ak8 jets",50,0,1000),"AK8Jet_Pt",plotSelectionBoosted,plotLabel),
        plotClasses.Plot(ROOT.TH1D("doublecsvallak8jets","double btag of all ak8 jets",44,-.1,1),"AK8Jet_DoubleCSV",plotSelectionBoosted,plotLabel),
        plotClasses.Plot(ROOT.TH1D("etaallak8jets","#eta of all ak8 jets",60,-2.5,2.5),"AK8Jet_Eta",plotSelectionBoosted,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b1N2","AK8Jet_EnergyCorrelation_b1N2",50,0,1),"AK8Jet_EnergyCorrelation_b1N2",plotSelectionBoosted,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b1N3","AK8Jet_EnergyCorrelation_b1N3",50,0,1),"AK8Jet_EnergyCorrelation_b1N3",plotSelectionBoosted,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b2N2","AK8Jet_EnergyCorrelation_b2N2",50,0,1),"AK8Jet_EnergyCorrelation_b2N2",plotSelectionBoosted,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b2N3","AK8Jet_EnergyCorrelation_b2N3",50,0,1),"AK8Jet_EnergyCorrelation_b2N3",plotSelectionBoosted,plotLabel),

        plotClasses.Plot(ROOT.TH1D("AK8Jet_Puppi_Softdrop_Mass","AK8Jet_Puppi_Softdrop_Mass",35,50,400),"AK8Jet_Puppi_Softdrop_Mass",plotSelectionBoosted,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_tau21","AK8 jet tau 21",50,0,1),"AK8Jet_Tau2/AK8Jet_Tau1",plotSelectionBoosted,plotLabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_tau32","AK8 jet tau 32",50,0,1),"AK8Jet_Tau3/AK8Jet_Tau2",plotSelectionBoosted,plotLabel),
        plotClasses.Plot(ROOT.TH1D("AK8Subjet1_DeepCSV","AK8Subjet1_DeepCSV",50,0,1),"AK8Subjet1_DeepCSV",plotSelectionBoosted,plotLabel),
        plotClasses.Plot(ROOT.TH1D("AK8Subjet2_DeepCSV","AK8Subjet2_DeepCSV",50,0,1),"AK8Subjet2_DeepCSV",plotSelectionBoosted,plotLabel),
        plotClasses.Plot(ROOT.TH1D("AK8Subjet1_Pt","AK8Subjet1_Pt",50,30,300),"AK8Subjet1_Pt",plotSelectionBoosted,plotLabel),
        plotClasses.Plot(ROOT.TH1D("AK8Subjet2_Pt","AK8Subjet2_Pt",50,30,300),"AK8Subjet2_Pt",plotSelectionBoosted,plotLabel),
        ]

    return plotsAK8Jets
    
def add_sl4j2t():
    # 4j2t cagegory
    plotLabel = "1 lepton, 4 jets, 2 b-tags"
    plotSelection = "((N_Jets==4&&N_BTagsM==2))"
    #plotSelection = "((N_Jets==4&&N_BTagsM==2)&&!"+boosted+")"
    plotPrefix = "4j2t"

    plots42 = [
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_HT","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotSelection,plotLabel),
    ]

    return plots42




def add_sl5j2t():
    # s52 category
    plotLabel = "1 lepton, 5 jets, 2 b-tags"
    plotSelection = "((N_Jets==5&&N_BTagsM==2))"
    #plotSelection = "((N_Jets==5&&N_BTagsM==2)&&!"+boosted+")"
    plotPrefix = "s52_"

    plots52 = [
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_HT","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotSelection,plotLabel),
    ]

    return plots52



def add_sl4j3t():
    # s43 category
    plotLabel = "1 lepton, 4 jets, 3 b-tags"
    plotSelection = categoriesJT[1][0]
    plotPrefix = "s43_"

    plots43 = [
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,0.0,1000.0),"BDT_common5_input_HT",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,0.0,600.0),"BDT_common5_input_M3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,0.0,300.0),"BDT_common5_input_MET",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.0,250.0),"BDT_common5_input_MHT",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,0.0,250.0),"BDT_common5_input_Mlb",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.4),"BDT_common5_input_aplanarity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,5.0),"BDT_common5_input_dEta_fn",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,0.0,500.0),"BDT_common5_input_first_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,1.0),"BDT_common5_input_fourth_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.15,0.45),"BDT_common5_input_h0",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.2,0.2),"BDT_common5_input_h1",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.2,0.3),"BDT_common5_input_h2",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.2,0.2),"BDT_common5_input_h3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.8,1.0),"BDT_common5_input_lowest_btag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.8,1.0),"BDT_common5_input_second_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,0.0,300.0),"BDT_common5_input_second_jet_pt",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0,1.0),"BDT_common5_input_sphericity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.8,1.0),"BDT_common5_input_third_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,0.0,300.0),"BDT_common5_input_third_jet_pt",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.82,1.0),"Evt_CSV_Average_Tagged",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,0.0,1.0),"Evt_CSV_Min",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.0,5.0),"Evt_Dr_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,0.0,500.0),"Evt_E_PrimaryLepton",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-3.0,3.0),"Evt_Eta_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-3,3),"Evt_Eta_PrimaryLepton",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0,5),"Evt_Jet_MaxDeta_Jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,0.0,400.0),"Evt_M3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,0.0,30.0),"Evt_M_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,30.0,400.0),"Evt_M_MedianTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,10.0,250.0),"Evt_M_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,0.0,50.0),"Evt_M_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,0.0,400.0),"Evt_Pt_PrimaryLepton",plotSelection,plotLabel),    
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.1),"Evt_blr_ETH",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-10.0,10.0),"Evt_blr_ETH_transformed",plotSelection,plotLabel),


        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",50,-0.1,1),"Reco_Sum_LikelihoodRatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",50,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",50,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",50,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",50,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",50,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",50,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
    ]

    return plots43



def add_sl4j4t():
    # s44 category
    plotLabel = "1 lepton, 4 jets, 4 b-tags"
    plotSelection = categoriesJT[4][0]
    plotPrefix = "s44_"
    # weights_Final_44_MEMBDTv2.xml

    plots44 = [
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",20,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",20,0.0,1000.0),"BDT_common5_input_HT",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",20,0.0,600.0),"BDT_common5_input_M3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",20,0.0,300.0),"BDT_common5_input_MET",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",20,0.0,250.0),"BDT_common5_input_MHT",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0.0,250.0),"BDT_common5_input_Mlb",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",20,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",20,0.0,0.4),"BDT_common5_input_aplanarity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",20,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",20,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",20,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",20,0.0,5.0),"BDT_common5_input_dEta_fn",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",20,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",20,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",20,0.0,500.0),"BDT_common5_input_first_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",20,0.8,1.0),"BDT_common5_input_fourth_highest_btag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",20,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",20,0.15,0.45),"BDT_common5_input_h0",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",20,-0.2,0.2),"BDT_common5_input_h1",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",20,-0.2,0.3),"BDT_common5_input_h2",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",20,-0.2,0.2),"BDT_common5_input_h3",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",20,0.8,1.0),"BDT_common5_input_lowest_btag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",20,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",20,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",20,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",20,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",20,0.8,1.0),"BDT_common5_input_second_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",20,0.0,300.0),"BDT_common5_input_second_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",20,0.0,1.0),"BDT_common5_input_sphericity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",20,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",20,0.8,1.0),"BDT_common5_input_third_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",20,0.0,300.0),"BDT_common5_input_third_jet_pt",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",20,0.82,1.0),"Evt_CSV_Average_Tagged",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",20,0.0,1.0),"Evt_CSV_Min",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",20,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",20,0.0,5.0),"Evt_Dr_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",20,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",20,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",20,0.0,500.0),"Evt_E_PrimaryLepton",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",20,-3.0,3.0),"Evt_Eta_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",20,-3,3),"Evt_Eta_PrimaryLepton",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",20,0,5),"Evt_Jet_MaxDeta_Jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",20,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",20,0.0,400.0),"Evt_M3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",20,0.0,30.0),"Evt_M_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,30.0,400.0),"Evt_M_MedianTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",20,10.0,250.0),"Evt_M_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",20,0.0,50.0),"Evt_M_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",20,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",20,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",20,0.0,400.0),"Evt_Pt_PrimaryLepton",plotSelection,plotLabel),    
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",20,0.0,1.1),"Evt_blr_ETH",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",20,-10.0,10.0),"Evt_blr_ETH_transformed",plotSelection,plotLabel),

        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",20,-0.1,1),"Reco_Sum_LikelihoodRatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",20,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",20,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",20,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
    ]
    return plots44




def add_sl5j3t():
    # s53 category
    plotLabel = "1 lepton, 5 jets, 3 b-tags"
    plotSelection = categoriesJT[2][0]
    plotPrefix = "s53_"

    plots53=[
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,0.0,1000.0),"BDT_common5_input_HT",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,0.0,600.0),"BDT_common5_input_M3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,0.0,300.0),"BDT_common5_input_MET",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.0,250.0),"BDT_common5_input_MHT",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,0.0,250.0),"BDT_common5_input_Mlb",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.4),"BDT_common5_input_aplanarity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,5.0),"BDT_common5_input_dEta_fn",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,0.0,500.0),"BDT_common5_input_first_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,1.0),"BDT_common5_input_fourth_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.15,0.45),"BDT_common5_input_h0",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.2,0.2),"BDT_common5_input_h1",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.2,0.3),"BDT_common5_input_h2",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.2,0.2),"BDT_common5_input_h3",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.8,1.0),"BDT_common5_input_lowest_btag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.8,1.0),"BDT_common5_input_second_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,0.0,300.0),"BDT_common5_input_second_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0,1.0),"BDT_common5_input_sphericity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.8,1.0),"BDT_common5_input_third_highest_btag",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,0.0,300.0),"BDT_common5_input_third_jet_pt",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.82,1.0),"Evt_CSV_Average_Tagged",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,0.0,1.0),"Evt_CSV_Min",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.0,5.0),"Evt_Dr_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,0.0,500.0),"Evt_E_PrimaryLepton",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-3.0,3.0),"Evt_Eta_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-3,3),"Evt_Eta_PrimaryLepton",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0,5),"Evt_Jet_MaxDeta_Jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,0.0,400.0),"Evt_M3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,0.0,30.0),"Evt_M_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,30.0,400.0),"Evt_M_MedianTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,10.0,250.0),"Evt_M_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,0.0,50.0),"Evt_M_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,0.0,400.0),"Evt_Pt_PrimaryLepton",plotSelection,plotLabel),    
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.1),"Evt_blr_ETH",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-10.0,10.0),"Evt_blr_ETH_transformed",plotSelection,plotLabel),

        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",30,-0.1,1),"Reco_Sum_LikelihoodRatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",30,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",30,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",30,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",30,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",30,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",30,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
    ]
    
    return plots53




def add_sl5j4t():
    plotLabel = "1 lepton, 5 jets, #geq4 b-tags"
    plotSelection = categoriesJT[5][0]
    plotPrefix = "s54_"
    plots54 = [
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",20,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",20,0.0,1000.0),"BDT_common5_input_HT",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",20,0.0,600.0),"BDT_common5_input_M3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",20,0.0,300.0),"BDT_common5_input_MET",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",20,0.0,250.0),"BDT_common5_input_MHT",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0.0,250.0),"BDT_common5_input_Mlb",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",20,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",20,0.0,0.4),"BDT_common5_input_aplanarity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",20,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",20,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",20,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",20,0.0,5.0),"BDT_common5_input_dEta_fn",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",20,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",20,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",20,0.0,500.0),"BDT_common5_input_first_jet_pt",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",20,0.8,1.0),"BDT_common5_input_fourth_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",20,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",20,0.15,0.45),"BDT_common5_input_h0",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",20,-0.2,0.2),"BDT_common5_input_h1",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",20,-0.2,0.3),"BDT_common5_input_h2",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",20,-0.2,0.2),"BDT_common5_input_h3",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",20,0.8,1.0),"BDT_common5_input_lowest_btag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",20,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",20,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",20,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",20,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",20,0.8,1.0),"BDT_common5_input_second_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",20,0.0,300.0),"BDT_common5_input_second_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",20,0.0,1.0),"BDT_common5_input_sphericity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",20,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",20,0.8,1.0),"BDT_common5_input_third_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",20,0.0,300.0),"BDT_common5_input_third_jet_pt",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",20,0.82,1.0),"Evt_CSV_Average_Tagged",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",20,0.0,1.0),"Evt_CSV_Min",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",20,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",20,0.0,5.0),"Evt_Dr_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",20,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",20,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",20,0.0,500.0),"Evt_E_PrimaryLepton",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",20,-3.0,3.0),"Evt_Eta_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",20,-3,3),"Evt_Eta_PrimaryLepton",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",20,0,5),"Evt_Jet_MaxDeta_Jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",20,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",20,0.0,400.0),"Evt_M3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",20,0.0,30.0),"Evt_M_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,30.0,400.0),"Evt_M_MedianTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",20,10.0,250.0),"Evt_M_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",20,0.0,50.0),"Evt_M_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",20,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",20,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",20,0.0,400.0),"Evt_Pt_PrimaryLepton",plotSelection,plotLabel),    
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",20,0.0,1.1),"Evt_blr_ETH",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",20,-10.0,10.0),"Evt_blr_ETH_transformed",plotSelection,plotLabel),

        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",20,-0.1,1),"Reco_Sum_LikelihoodRatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",20,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",20,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",20,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
    ]

    
    return plots54




def add_sl6j2t():
    # s62 category
    plotLabel = "1 lepton, #geq6 jets, 2 b-tags"
    plotSelection = categoriesJT[0][0]
    plotPrefix = "s62_"
    plots62 = [
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,0.0,1000.0),"BDT_common5_input_HT",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,0.0,600.0),"BDT_common5_input_M3",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,0.0,300.0),"BDT_common5_input_MET",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.0,250.0),"BDT_common5_input_MHT",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,0.0,250.0),"BDT_common5_input_Mlb",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.4),"BDT_common5_input_aplanarity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,5.0),"BDT_common5_input_dEta_fn",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,0.0,500.0),"BDT_common5_input_first_jet_pt",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,1.0),"BDT_common5_input_fourth_highest_btag",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.15,0.45),"BDT_common5_input_h0",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.2,0.2),"BDT_common5_input_h1",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.2,0.3),"BDT_common5_input_h2",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.2,0.2),"BDT_common5_input_h3",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.8,1.0),"BDT_common5_input_lowest_btag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.8,1.0),"BDT_common5_input_second_highest_btag",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,0.0,300.0),"BDT_common5_input_second_jet_pt",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0,1.0),"BDT_common5_input_sphericity",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.8,1.0),"BDT_common5_input_third_highest_btag",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,0.0,300.0),"BDT_common5_input_third_jet_pt",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.82,1.0),"Evt_CSV_Average_Tagged",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,0.0,1.0),"Evt_CSV_Min",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.0,5.0),"Evt_Dr_JetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,0.0,500.0),"Evt_E_PrimaryLepton",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-3.0,3.0),"Evt_Eta_JetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-3,3),"Evt_Eta_PrimaryLepton",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0,5),"Evt_Jet_MaxDeta_Jets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,0.0,400.0),"Evt_M3",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,0.0,30.0),"Evt_M_JetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,30.0,400.0),"Evt_M_MedianTaggedJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,10.0,250.0),"Evt_M_MinDeltaRJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,0.0,50.0),"Evt_M_TaggedJetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,0.0,400.0),"Evt_Pt_PrimaryLepton",plotSelection,plotLabel),    
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.1),"Evt_blr_ETH",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-10.0,10.0),"Evt_blr_ETH_transformed",plotSelection,plotLabel),
    ]

    return plots62
    


def add_sl6j3t():
    # s63 category
    plotLabel = "1 lepton, #geq6 jets, 3 b-tags"
    plotSelection = categoriesJT[3][0]
    plotPrefix = "s63_"
    plots63 = [
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,0.0,1000.0),"BDT_common5_input_HT",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,0.0,600.0),"BDT_common5_input_M3",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,0.0,300.0),"BDT_common5_input_MET",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.0,250.0),"BDT_common5_input_MHT",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,0.0,250.0),"BDT_common5_input_Mlb",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.4),"BDT_common5_input_aplanarity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,5.0),"BDT_common5_input_dEta_fn",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,0.0,500.0),"BDT_common5_input_first_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,1.0),"BDT_common5_input_fourth_highest_btag",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.15,0.45),"BDT_common5_input_h0",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.2,0.2),"BDT_common5_input_h1",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.2,0.3),"BDT_common5_input_h2",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.2,0.2),"BDT_common5_input_h3",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.8,1.0),"BDT_common5_input_lowest_btag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.8,1.0),"BDT_common5_input_second_highest_btag",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,0.0,300.0),"BDT_common5_input_second_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.0,1.0),"BDT_common5_input_sphericity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.8,1.0),"BDT_common5_input_third_highest_btag",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,0.0,300.0),"BDT_common5_input_third_jet_pt",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.82,1.0),"Evt_CSV_Average_Tagged",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,0.0,1.0),"Evt_CSV_Min",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.0,5.0),"Evt_Dr_JetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,0.0,500.0),"Evt_E_PrimaryLepton",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-3.0,3.0),"Evt_Eta_JetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-3,3),"Evt_Eta_PrimaryLepton",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0,5),"Evt_Jet_MaxDeta_Jets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,0.0,400.0),"Evt_M3",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,0.0,30.0),"Evt_M_JetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,30.0,400.0),"Evt_M_MedianTaggedJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,10.0,250.0),"Evt_M_MinDeltaRJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,0.0,50.0),"Evt_M_TaggedJetsAverage",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotSelection,plotLabel),
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,0.0,400.0),"Evt_Pt_PrimaryLepton",plotSelection,plotLabel),    
        ##plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.1),"Evt_blr_ETH",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-10.0,10.0),"Evt_blr_ETH_transformed",plotSelection,plotLabel),

        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",30,-0.1,1),"Reco_Sum_LikelihoodRatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",30,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",30,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",30,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",30,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",30,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",30,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",30,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
    ]

    return plots63




def add_sl6j4t():
    # s64 category
    plotLabel = "1 lepton, #geq6 jets, #geq4 b-tags"
    plotSelection = categoriesJT[6][0]
    plotPrefix = "s64"
    plots64 = [
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",20,0.0,3.4),"BDT_common5_input_Evt_Deta_JetsAverage",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",20,0.0,1000.0),"BDT_common5_input_HT",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",20,0.0,600.0),"BDT_common5_input_M3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",20,0.0,300.0),"BDT_common5_input_MET",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",20,0.0,250.0),"BDT_common5_input_MHT",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",20,0.0,250.0),"BDT_common5_input_Mlb",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",20,200,900.0),"BDT_common5_input_all_sum_pt_with_met",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",20,0.0,0.4),"BDT_common5_input_aplanarity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",20,0.8,1.0),"BDT_common5_input_avg_btag_disc_btags",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_avg_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",20,0.0,200.0),"BDT_common5_input_best_higgs_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",20,0.0,250.0),"BDT_common5_input_closest_tagged_dijet_mass",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",20,0.0,5.0),"BDT_common5_input_dEta_fn",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",20,0.0,0.02),"BDT_common5_input_dev_from_avg_disc_btags",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",20,0.0,3.0),"BDT_common5_input_dr_between_lep_and_closest_jet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",20,-0.1,1.0),"BDT_common5_input_fifth_highest_CSV",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",20,0.0,500.0),"BDT_common5_input_first_jet_pt",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",20,0.8,1.0),"BDT_common5_input_fourth_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",20,0.0,300.0),"BDT_common5_input_fourth_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",20,0.15,0.45),"BDT_common5_input_h0",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",20,-0.2,0.2),"BDT_common5_input_h1",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",20,-0.2,0.3),"BDT_common5_input_h2",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",20,-0.2,0.2),"BDT_common5_input_h3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",20,500.0,1200.0),"BDT_common5_input_invariant_mass_of_everything",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",20,0.8,1.0),"BDT_common5_input_lowest_btag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",20,0.0,2.0),"BDT_common5_input_maxeta_jet_jet",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",20,0.0,2.0),"BDT_common5_input_maxeta_jet_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",20,0.0,2.0),"BDT_common5_input_maxeta_tag_tag",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",20,0.0,5.0),"BDT_common5_input_min_dr_tagged_jets",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",20,0.0,1.0),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",20,0.8,1.0),"BDT_common5_input_second_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",20,0.0,300.0),"BDT_common5_input_second_jet_pt",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",20,0.0,1.0),"BDT_common5_input_sphericity",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",20,40.0,230.0),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",20,0.8,1.0),"BDT_common5_input_third_highest_btag",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",20,0.0,300.0),"BDT_common5_input_third_jet_pt",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",20,0.82,1.0),"Evt_CSV_Average_Tagged",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",20,0.0,1.0),"Evt_CSV_Min",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",20,0.0,3.0),"Evt_Deta_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",20,0.0,5.0),"Evt_Dr_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",20,0.0,3.0),"Evt_Dr_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonJet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",20,0.0,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",20,0.0,5.0),"Evt_Dr_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",20,0.0,500.0),"Evt_E_PrimaryLepton",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",20,-3.0,3.0),"Evt_Eta_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",20,-3,3),"Evt_Eta_PrimaryLepton",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",20,0,5),"Evt_Jet_MaxDeta_Jets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",20,0.0,400.0),"Evt_M2_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",20,0.0,400.0),"Evt_M3",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",20,0.0,30.0),"Evt_M_JetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",20,30.0,400.0),"Evt_M_MedianTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",20,10.0,250.0),"Evt_M_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",20,10.0,300.0),"Evt_M_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",20,0.0,50.0),"Evt_M_TaggedJetsAverage",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",20,0.0,400.0),"Evt_Pt_MinDeltaRJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",20,0.0,400.0),"Evt_Pt_MinDeltaRTaggedJets",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",20,0.0,400.0),"Evt_Pt_PrimaryLepton",plotSelection,plotLabel),    
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",20,0.0,1.1),"Evt_blr_ETH",plotSelection,plotLabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",20,-10.0,10.0),"Evt_blr_ETH_transformed",plotSelection,plotLabel),

        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",20,-0.1,1),"Reco_Sum_LikelihoodRatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",20,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",20,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",20,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",20,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",20,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotSelection,plotLabel),
    ]

    return plots64




def add_dnn():
    # dnn category
    plotPrefix = "dnn_"
    plotsDNNcontrol = [
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"43_ttHnode","DNN ttH node",20,0,1),"aachen_Out_ttH","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"43_ttbbnode","DNN ttbb node",20,0,1),"aachen_Out_ttbarBB","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"43_tt2bnode","DNN tt2b node",20,0,1),"aachen_Out_ttbar2B","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"43_ttbnode","DNN ttb node",20,0,1),"aachen_Out_ttbarB","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"43_ttlfnode","DNN ttlf node",20,0,1),"aachen_Out_ttbarOther","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"43_ttccnode","DNN ttcc node",20,0,1),"aachen_Out_ttbarCC","((N_Jets>=4&&N_BTagsM==3))","1 lepton, #geq4jets, 3 b-tags"),
    ]
    
    return plotsDNNcontrol




def getDiscriminatorPlots(data = None, discrname = None):
    discriminatorPlots = add_plots()
    #discriminatorPlots += add_ak8jets()
    #discriminatorPlots += add_sl6j4t()
    #discriminatorPlots += add_sl6j3t()
    #discriminatorPlots += add_sl6j2t()
    #discriminatorPlots += add_sl5j4t()
    #discriminatorPlots += add_sl5j3t()
    #discriminatorPlots += add_sl4j4t()
    #discriminatorPlots += add_sl4j3t()
    #discriminatorPlots += add_sl4j2t()
    #discriminatorPlots += add_sl5j2t()
    #discriminatorPlots += add_dnn()

    return discriminatorPlots
