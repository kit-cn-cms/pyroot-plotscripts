import sys
import os

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses
import ROOT


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

# selection for categories
categoriesJTsel="("+categoriesJT[0][0]
for cat in categoriesJT[1:]:
    categoriesJTsel+="||"+cat[0]
categoriesJTsel+=")"

# category strings 
catstringJT="0"
for i,cat in enumerate(categoriesJT):
    catstringJT+=("+"+str(i+1)+"*"+cat[0])

def add_plots():
    # book plots
    plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
    #plotlabelboosted="#splitline{1 lepton, #geq 4 jets, #geq 2 b-tags}{#geq 1 C/A 1.5 jet p_{T} > 200 GeV}"
    plotselection="(N_Jets>=4&&N_BTagsM>=2)"
    plots=[
        #plotClasses.Plot(ROOT.TH1D("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,categoriesJTsel,"1 lepton"),
        #plotClasses.Plot(ROOT.TH1D("BCAT" ,"jet-tag + boosted categories",len(categoriesJTB),0.5,0.5+len(categoriesJTB)),catstringJTB,categoriesJTBsel,"1 lepton"),
        plotClasses.Plot(ROOT.TH1D("N_Jets","Number of ak4 jets",11,3.5,14.5),"N_Jets",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSV0","B-tag of leading jet",22,-.1,1),"Jet_CSV[0]",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSV1","B-tag of second jet",22,-.1,1),"Jet_CSV[1]",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSV","B-tag of all jets",22,-.1,1),"Jet_CSV",plotselection,plotlabel),
        
        #plotClasses.Plot(ROOT.TH1D("eta1","#eta of leading jet",50,-2.5,2.5),"Jet_Eta[0]",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("eta2","#eta of second jet",50,-2.5,2.5),"Jet_Eta[1]",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("phij1","#phi of leading jet",64,-3.2,3.2),"Jet_Phi[0]",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("phij2","#phi of second jet",64,-3.2,3.2),"Jet_Phi[1]",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_HT_Jets","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("etaalljets","#eta of all jets",60,-2.5,2.5),"Jet_Eta",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("pumvaalljets","PU MVA of all jets",60,0,1.0),"Jet_PileUpMVA",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("puidalljets","PU MVA of all jets",60,0,1.0),"Jet_PileUpID",plotselection,plotlabel),
        
        plotClasses.Plot(ROOT.TH1D("csvalljets","DeepCSV of all jets",44,-.1,1),"Jet_CSV",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("leppt","lepton p_{T}",50,0,200),"LooseLepton_Pt[0]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("lepeta","lepton #eta",50,-2.5,2.5),"LooseLepton_Eta[0]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("elleppt","electron p_{T}",50,0,200),"Electron_Pt[0]",'Electron_Pt[0]>10',plotlabel),
        plotClasses.Plot(ROOT.TH1D("ellepeta","electron #eta",50,-2.5,2.5),"Electron_Eta[0]",'Electron_Pt[0]>10',plotlabel),
        plotClasses.Plot(ROOT.TH1D("muleppt","muon p_{T}",50,0,200),"Muon_Pt[0]",'Muon_Pt[0]>10',plotlabel),
        plotClasses.Plot(ROOT.TH1D("mulepeta","muon #eta",50,-2.5,2.5),"Muon_Eta[0]",'Muon_Pt[0]>10',plotlabel),
        
        #plotClasses.Plot(ROOT.TH1D("N_AK8_Jets","Number of ak8 jets",10,0.5,10.5),"N_AK8Jets",plotselection,plotlabel),
    ]




    plotsAdditional=[
        #plotClasses.Plot(ROOT.TH1D("CSV0NPVgeq20","B-tag of leading jet (NPV#geq20)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSV1NPVgeq20","B-tag of second jet (NPV#geq20)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSVNPVgeq20","B-tag of all jets (NPV#geq20)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices>=20)",plotlabel),

        #plotClasses.Plot(ROOT.TH1D("CSV0NPV15to20","B-tag of leading jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSV1NPV15to20","B-tag of second jet (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSVNPV15to20","B-tag of all jets (15#leqNPV#leq20)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=20 && N_PrimaryVertices>=15)",plotlabel),

        #plotClasses.Plot(ROOT.TH1D("CSV0NPV10to15","B-tag of leading jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSV1NPV10to15","B-tag of second jet (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSVNPV10to15","B-tag of all jets (10#leqNPV#leq15)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=15 && N_PrimaryVertices>=10)",plotlabel),

        #plotClasses.Plot(ROOT.TH1D("CSV0NPV0to10","B-tag of leading jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[0]",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSV1NPV0to10","B-tag of second jet (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV[1]",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),
        #plotClasses.Plot(ROOT.TH1D("CSVNPV0to10","B-tag of all jets (0#leqNPV#leq10)",22,-.1,1),"Jet_CSV",plotselection+"*(N_PrimaryVertices<=10 && N_PrimaryVertices>=0)",plotlabel),


        plotClasses.Plot(ROOT.TH1D("pt1","p_{T} of leading jet",50,0,500),"Jet_Pt[0]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("pt2","p_{T} of second jet",50,0,500),"Jet_Pt[1]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("pt3","p_{T} of third jet",40,0,400),"Jet_Pt[2]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("pt4","p_{T} of fourth jet",60,0,300),"Jet_Pt[3]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("pt5","p_{T} of fifth jet",40,0,200),"Jet_Pt[4]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("pt6","p_{T} of sixth jet",40,0,200),"Jet_Pt[5]",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("pt2tagged","p_{T} of second tagged jet",50,0,500),"TaggedJet_Pt[1]",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("pt1tagged","p_{T} of leading tagged jet",50,0,500),"TaggedJet_Pt[0]",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("pt3tagged","p_{T} of third tagged jet",40,0,400),"TaggedJet_Pt[2]",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("pt4tagged","p_{T} of fourth tagged jet",60,0,300),"TaggedJet_Pt[3]",plotselection,plotlabel),

        #plotClasses.Plot(ROOT.TH1D("Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX","Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",50,0,2.0),"Prescale_HLT_Ele27_eta2p1_WPTight_Gsf_vX",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Prescale_HLT_IsoMu22_vX","Prescale_HLT_IsoMu22_vX",50,0,2.0),"Prescale_HLT_IsoMu22_vX",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Prescale_HLT_IsoTkMu22_vX","Prescale_HLT_IsoTkMu22_vX",50,0,2.0),"Prescale_HLT_IsoTkMu22_vX",plotselection,plotlabel),

        plotClasses.Plot(ROOT.TH1D("eliso","electron relative isolation",50,0,0.15),"Electron_RelIso[0]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("muiso","muon relative isolation",50,0,0.15),"Muon_RelIso[0]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("MET","missing transverse energy",50,0,200),"Evt_Pt_MET",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("METphi","MET #phi",64,-3.2,3.2),"Evt_Phi_MET",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("N_PrimaryVertices","Reconstructed primary vertices",26,-.5,50.5),"N_PrimaryVertices",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("blrAll","B-tagging likelihood ratio",44,-6,10),"TMath::Log(Evt_blr_ETH/(1-Evt_blr_ETH))",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_M_MinDeltaRJets","dijet mass of closest jets",30,0.,150),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_M_MinDeltaRTaggedJets","mass of closest tagged jets",45,0.,450),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Dr_MinDeltaRJets","#Delta R of closest jets",50,0.,5.0),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Dr_MinDeltaRTaggedJets","#Delta R of closest tagged jets",50,0.,5.0),"Evt_Dr_MinDeltaRTaggedJets",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Jet_MaxDeta_Jets","max #Delta #eta (jet,jet)",50,0.,5.0),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_TaggedJet_MaxDeta_Jets","max #Delta #eta (tag,jet)",50,0.,5.0),"Evt_TaggedJet_MaxDeta_Jets",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_TaggedJet_MaxDeta_TaggedJets","max #Delta #eta (tag,tag)",60,0.,6.0),"Evt_TaggedJet_MaxDeta_TaggedJets",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_H1","Evt_H1",60,-0.2,0.4),"Evt_H1",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_H2","Evt_H2",60,-0.2,0.4),"Evt_H2",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_H3","Evt_H3",50,-0.05,1.05),"Evt_H3",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_H4","Evt_H4",50,-0.15,0.35),"Evt_H4",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Sphericity","Sphericity",50,0,1),"Evt_Sphericity",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Aplanarity","Aplanarity",50,0,0.5),"Evt_Aplanarity",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Deta_UntaggedJetsAverage","avg. #Delta #eta of untagged jets",50,0.,4.5),"Evt_Deta_UntaggedJetsAverage",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Deta_TaggedJetsAverage","avg. #Delta #eta of tagged jets",50,0.,4.5),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        
        #plotClasses.Plot(ROOT.TH1D("Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio",50,-0.1,1),"Reco_Sum_LikelihoodRatio",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio",50,-0.1,1),"Reco_Sum_LikelihoodTimesMERatio",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",50,-0.1,200),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",50,-0.1,500),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",50,-0.1,300),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        ##plotClasses.Plot(ROOT.TH1D("Reco_TTBBME_best_TTLikelihood_comb","Reco_TTBBME_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBME_best_TTLikelihood_comb",plotselection,plotlabel),
        ##plotClasses.Plot(ROOT.TH1D("Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",50,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",50,50,200),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Evt_M_MinDeltaRLeptonJet","mass of lepton and closest jet",30,0.,150),"Evt_M_MinDeltaRLeptonJet",plotselection,plotlabel),
        ##plotClasses.Plot(ROOT.TH1D("Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME","Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",50,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihoodTimesME",plotselection,plotlabel),
        ##plotClasses.Plot(ROOT.TH1D("Reco_TTBBLikelihood_best_TTBBLikelihood","Reco_TTBBLikelihood_best_TTBBLikelihood",50,-0.1,1),"Reco_TTBBLikelihood_best_TTBBLikelihood",plotselection,plotlabel),
        ##plotClasses.Plot(ROOT.TH1D("Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",50,-0.1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood",50,-0.1,1),"Reco_Dr_BB_best_TTLikelihood",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Reco_TTBBME_off_best_TTLikelihood_comb","Reco_TTBBME_off_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBME_off_best_TTLikelihood_comb",plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb","Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",50,-0.1,1),"Reco_TTBBLikelihoodTimesME_off_best_TTLikelihood_comb",plotselection,plotlabel),
    ]

    return plots + plotsAdditional


def add_ak8():

    plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
    plotselection="(N_Jets>=4&&N_BTagsM>=2)"
    plotlabelboosted="#splitline{1 lepton, #geq 4 jets, #geq 2 b-tags}{#geq 1 Ak8 jet p_{T} > 200 GeV}"
    plotselectionboosted="(N_Jets>=4&&N_BTagsM>=2&&N_AK8Jets>=1)*(AK8Jet_Pt>200)"
    plotsAK8jets=[
        plotClasses.Plot(ROOT.TH1D("ptallak8jets","p_{T} of all ak8 jets",50,0,1000),"AK8Jet_Pt",plotselectionboosted,plotlabel),
        plotClasses.Plot(ROOT.TH1D("doublecsvallak8jets","double btag of all ak8 jets",44,-.1,1),"AK8Jet_DoubleCSV",plotselectionboosted,plotlabel),
        plotClasses.Plot(ROOT.TH1D("etaallak8jets","#eta of all ak8 jets",60,-2.5,2.5),"AK8Jet_Eta",plotselectionboosted,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b1N2","AK8Jet_EnergyCorrelation_b1N2",50,0,1),"AK8Jet_EnergyCorrelation_b1N2",plotselectionboosted,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b1N3","AK8Jet_EnergyCorrelation_b1N3",50,0,1),"AK8Jet_EnergyCorrelation_b1N3",plotselectionboosted,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b2N2","AK8Jet_EnergyCorrelation_b2N2",50,0,1),"AK8Jet_EnergyCorrelation_b2N2",plotselectionboosted,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_EnergyCorrelation_b2N3","AK8Jet_EnergyCorrelation_b2N3",50,0,1),"AK8Jet_EnergyCorrelation_b2N3",plotselectionboosted,plotlabel),

        plotClasses.Plot(ROOT.TH1D("AK8Jet_Puppi_Softdrop_Mass","AK8Jet_Puppi_Softdrop_Mass",35,50,400),"AK8Jet_Puppi_Softdrop_Mass",plotselectionboosted,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_tau21","AK8 jet tau 21",50,0,1),"AK8Jet_Tau2/AK8Jet_Tau1",plotselectionboosted,plotlabel),
        #plotClasses.Plot(ROOT.TH1D("AK8Jet_tau32","AK8 jet tau 32",50,0,1),"AK8Jet_Tau3/AK8Jet_Tau2",plotselectionboosted,plotlabel),
        plotClasses.Plot(ROOT.TH1D("AK8Subjet1_DeepCSV","AK8Subjet1_DeepCSV",50,0,1),"AK8Subjet1_DeepCSV",plotselectionboosted,plotlabel),
        plotClasses.Plot(ROOT.TH1D("AK8Subjet2_DeepCSV","AK8Subjet2_DeepCSV",50,0,1),"AK8Subjet2_DeepCSV",plotselectionboosted,plotlabel),
        plotClasses.Plot(ROOT.TH1D("AK8Subjet1_Pt","AK8Subjet1_Pt",50,30,300),"AK8Subjet1_Pt",plotselectionboosted,plotlabel),
        plotClasses.Plot(ROOT.TH1D("AK8Subjet2_Pt","AK8Subjet2_Pt",50,30,300),"AK8Subjet2_Pt",plotselectionboosted,plotlabel),
    ]

    return plotsAK8jets

def add_sl4j2t():
    plotlabel="1 lepton, 4 jets, 2 b-tags"
    plotselection="((N_Jets==4&&N_BTagsM==2))"
    #plotselection="((N_Jets==4&&N_BTagsM==2)&&!"+boosted+")"

    plotprefix="4j2t"
    plots42=[
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_HT","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
    ]

    return plots42


def add_sl5j2t():
    plotlabel="1 lepton, 5 jets, 2 b-tags"
    plotselection="((N_Jets==5&&N_BTagsM==2))"
    #plotselection="((N_Jets==5&&N_BTagsM==2)&&!"+boosted+")"

    plotprefix="s52_"
    plots52=[
        plotClasses.Plot(ROOT.TH1D(plotprefix+"Evt_HT","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
    ]

    return plots52


def add_sl4j3t():
    plotlabel="1 lepton, 4 jets, 3 b-tags"
    plotselection=categoriesJT[1][0]
    plotprefix="s43_"
    plots43=[
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0.0,1.0),memexp,plotselection,plotlabel),
    ]

    return plots43



def add_sl4j4t():
    plotlabel="1 lepton, 4 jets, 4 b-tags"
    plotselection=categoriesJT[4][0]
    plotprefix="s44_"
    # weights_Final_44_MEMBDTv2.xml
    plots44=[
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"MEM","MEM",20,0.0,1.0),memexp,plotselection,plotlabel),
    ]

    return plots44



def add_sl5j3t():
    plotlabel="1 lepton, 5 jets, 3 b-tags"
    plotselection=categoriesJT[2][0]
    plotprefix="s53_"
    plots53=[
        plotClasses.Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0.0,1.0),memexp,plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
    ]
    
    return plots53


def add_sl5j4t():
    plotlabel="1 lepton, 5 jets, #geq4 b-tags"
    plotselection=categoriesJT[5][0]
    plotprefix="s54_"
    plots54=[
        plotClasses.Plot(ROOT.TH1D(plotprefix+"MEM","MEM",20,0.0,1.0),memexp,plotselection,plotlabel),
    ]

    return plots54


def add_sl6j2t():
    plotlabel="1 lepton, #geq6 jets, 2 b-tags"
    plotselection=categoriesJT[0][0]
    plotprefix="s62_"
    plots62=[
    ]
    
    return plots62



def add_sl6j3t():
    plotlabel="1 lepton, #geq6 jets, 3 b-tags"
    plotselection=categoriesJT[3][0]
    plotprefix="s63_"
    plots63=[
        ###plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0.0,1.0),memexp,plotselection,plotlabel),
    ]

    return plots63



def add_sl6j4t():
    plotlabel="1 lepton, #geq6 jets, #geq4 b-tags"
    plotselection=categoriesJT[6][0]
    plotprefix="s64"
    plots64=[
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D(plotprefix+"MEM","MEM",20,0.0,1.0),memexp,plotselection,plotlabel),
    ]

    return plots64

def add_dnn(data, discrname):
    categories=[]
    nhistobins=[]
    minxvals=[]
    maxxvals=[]
    discrs =[]
    
    # DNN classes DNN outputs
    categorienames_MultiDNN=[
        # 3 tag and 4 tag events
        ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==0)","ljets_j4_tge3_ttHnode",""),
        ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==1)","ljets_j4_tge3_ttbbnode",""),
        ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==2)","ljets_j4_tge3_tt2bnode",""),
        ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==3)","ljets_j4_tge3_ttbnode",""),
        ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==4)","ljets_j4_tge3_ttccnode",""),
        ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==5)","ljets_j4_tge3_ttlfnode",""),

        ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==0)","ljets_j5_tge3_ttHnode",""),             
        ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==1)","ljets_j5_tge3_ttbbnode",""),             
        ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==2)","ljets_j5_tge3_tt2bnode",""),             
        ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==3)","ljets_j5_tge3_ttbnode",""),             
        ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==4)","ljets_j5_tge3_ttccnode",""),             
        ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==5)","ljets_j5_tge3_ttlfnode",""),             


        ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==0)","ljets_jge6_tge3_ttHnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==1)","ljets_jge6_tge3_ttbbnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==2)","ljets_jge6_tge3_tt2bnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==3)","ljets_jge6_tge3_ttbnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==4)","ljets_jge6_tge3_ttccnode",""),
        ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==5)","ljets_jge6_tge3_ttlfnode",""),

        # 3 tag and 4 tag events with MIN node output cuts
        #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==0&&DNN_Out_4j3t_ttH>0.25)","ljets_j4_tge3_discrCut_ttHnode",""),
        #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==1&&DNN_Out_4j3t_ttbarBB>0.2)","ljets_j4_tge3_discrCut_ttbbnode",""),
        #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==2&&DNN_Out_4j3t_ttbar2B>0.3)","ljets_j4_tge3_discrCut_tt2bnode",""),
        #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==3&&DNN_Out_4j3t_ttbarB>0.3)","ljets_j4_tge3_discrCut_ttbnode",""),
        #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==4&&DNN_Out_4j3t_ttbarCC>0.2)","ljets_j4_tge3_discrCut_ttccnode",""),
        #("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==5&&DNN_Out_4j3t_ttbarlf>0.35)","ljets_j4_tge3_discrCut_ttlfnode",""),

        #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==0&&DNN_Out_5j3t_ttH>0.25)","ljets_j5_tge3_discrCut_ttHnode",""),             
        #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==1&&DNN_Out_5j3t_ttbarBB>0.2)","ljets_j5_tge3_discrCut_ttbbnode",""),             
        #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==2&&DNN_Out_5j3t_ttbar2B>0.3)","ljets_j5_tge3_discrCut_tt2bnode",""),             
        #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==3&&DNN_Out_5j3t_ttbarB>0.3)","ljets_j5_tge3_discrCut_ttbnode",""),             
        #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==4&&DNN_Out_5j3t_ttbarCC>0.2)","ljets_j5_tge3_discrCut_ttccnode",""),             
        #("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==5&&DNN_Out_5j3t_ttbarlf>0.35)","ljets_j5_tge3_discrCut_ttlfnode",""),             


        #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==0&&DNN_Out_6j3t_ttH>0.25)","ljets_jge6_tge3_discrCut_ttHnode",""),
        #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==1&&DNN_Out_6j3t_ttbarBB>0.2)","ljets_jge6_tge3_discrCut_ttbbnode",""),
        #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==2&&DNN_Out_6j3t_ttbar2B>0.3)","ljets_jge6_tge3_discrCut_tt2bnode",""),
        #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==3&&DNN_Out_6j3t_ttbarB>0.3)","ljets_jge6_tge3_discrCut_ttbnode",""),
        #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==4&&DNN_Out_6j3t_ttbarCC>0.2)","ljets_jge6_tge3_discrCut_ttccnode",""),
        #("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==5&&DNN_Out_6j3t_ttbarlf>0.35)","ljets_jge6_tge3_discrCut_ttlfnode",""),

        #### only 3 tag events 
        #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==0)","ljets_j4_t3_ttHnode",""),
        #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==1)","ljets_j4_t3_ttbbnode",""),
        #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==2)","ljets_j4_t3_tt2bnode",""),
        #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==3)","ljets_j4_t3_ttbnode",""),
        #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==4)","ljets_j4_t3_ttccnode",""),
        #("(N_Jets==4&&N_BTagsM==3&&DNN_4j3t_pred_class==5)","ljets_j4_t3_ttlfnode",""),

        #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==0)","ljets_j5_t3_ttHnode",""),             
        #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==1)","ljets_j5_t3_ttbbnode",""),             
        #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==2)","ljets_j5_t3_tt2bnode",""),             
        #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==3)","ljets_j5_t3_ttbnode",""),             
        #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==4)","ljets_j5_t3_ttccnode",""),             
        #("(N_Jets==5&&N_BTagsM==3&&DNN_5j3t_pred_class==5)","ljets_j5_t3_ttlfnode",""),             


        #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==0)","ljets_jge6_t3_ttHnode",""),
        #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==1)","ljets_jge6_t3_ttbbnode",""),
        #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==2)","ljets_jge6_t3_tt2bnode",""),
        #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==3)","ljets_jge6_t3_ttbnode",""),
        #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==4)","ljets_jge6_t3_ttccnode",""),
        #("(N_Jets>=6&&N_BTagsM==3&&DNN_6j3t_pred_class==5)","ljets_jge6_t3_ttlfnode",""),

        #### only 4 tag events 
        #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==0)","ljets_j4_tge4_ttHnode",""),
        #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==1)","ljets_j4_tge4_ttbbnode",""),
        #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==2)","ljets_j4_tge4_tt2bnode",""),
        #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==3)","ljets_j4_tge4_ttbnode",""),
        #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==4)","ljets_j4_tge4_ttccnode",""),
        #("(N_Jets==4&&N_BTagsM>=4&&DNN_4j3t_pred_class==5)","ljets_j4_tge4_ttlfnode",""),

        #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==0)","ljets_j5_tge4_ttHnode",""),             
        #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==1)","ljets_j5_tge4_ttbbnode",""),             
        #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==2)","ljets_j5_tge4_tt2bnode",""),             
        #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==3)","ljets_j5_tge4_ttbnode",""),             
        #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==4)","ljets_j5_tge4_ttccnode",""),             
        #("(N_Jets==5&&N_BTagsM>=4&&DNN_5j3t_pred_class==5)","ljets_j5_tge4_ttlfnode",""),             


        #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==0)","ljets_jge6_tge4_ttHnode",""),
        #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==1)","ljets_jge6_tge4_ttbbnode",""),
        #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==2)","ljets_jge6_tge4_tt2bnode",""),
        #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==3)","ljets_jge6_tge4_ttbnode",""),
        #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==4)","ljets_jge6_tge4_ttccnode",""),
        #("(N_Jets>=6&&N_BTagsM>=4&&DNN_6j3t_pred_class==5)","ljets_jge6_tge4_ttlfnode",""),

        ]


    discrs_MultiDNN=[
        # 3 and 4 tags        
        'DNN_Out_4j3t_ttH',
        'DNN_Out_4j3t_ttbarBB',
        'DNN_Out_4j3t_ttbar2B',
        'DNN_Out_4j3t_ttbarB',
        'DNN_Out_4j3t_ttbarCC',
        'DNN_Out_4j3t_ttbarlf',
        'DNN_Out_5j3t_ttH',
        'DNN_Out_5j3t_ttbarBB',
        'DNN_Out_5j3t_ttbar2B',
        'DNN_Out_5j3t_ttbarB',
        'DNN_Out_5j3t_ttbarCC',
        'DNN_Out_5j3t_ttbarlf',
        'DNN_Out_6j3t_ttH',
        'DNN_Out_6j3t_ttbarBB',
        'DNN_Out_6j3t_ttbar2B',
        'DNN_Out_6j3t_ttbarB',
        'DNN_Out_6j3t_ttbarCC',
        'DNN_Out_6j3t_ttbarlf',

        # 3 and 4 tags with minimal node output values 
        #'DNN_Out_4j3t_ttH',
        #'DNN_Out_4j3t_ttbarBB',
        #'DNN_Out_4j3t_ttbar2B',
        #'DNN_Out_4j3t_ttbarB',
        #'DNN_Out_4j3t_ttbarCC',
        #'DNN_Out_4j3t_ttbarlf',
        #'DNN_Out_5j3t_ttH',
        #'DNN_Out_5j3t_ttbarBB',
        #'DNN_Out_5j3t_ttbar2B',
        #'DNN_Out_5j3t_ttbarB',
        #'DNN_Out_5j3t_ttbarCC',
        #'DNN_Out_5j3t_ttbarlf',
        #'DNN_Out_6j3t_ttH',
        #'DNN_Out_6j3t_ttbarBB',
        #'DNN_Out_6j3t_ttbar2B',
        #'DNN_Out_6j3t_ttbarB',
        #'DNN_Out_6j3t_ttbarCC',
        #'DNN_Out_6j3t_ttbarlf',


        ## only 3 tag events
        #'DNN_Out_4j3t_ttH',
        #'DNN_Out_4j3t_ttbarBB',
        #'DNN_Out_4j3t_ttbar2B',
        #'DNN_Out_4j3t_ttbarB',
        #'DNN_Out_4j3t_ttbarCC',
        #'DNN_Out_4j3t_ttbarlf',
        #'DNN_Out_5j3t_ttH',
        #'DNN_Out_5j3t_ttbarBB',
        #'DNN_Out_5j3t_ttbar2B',
        #'DNN_Out_5j3t_ttbarB',
        #'DNN_Out_5j3t_ttbarCC',
        #'DNN_Out_5j3t_ttbarlf',
        #'DNN_Out_6j3t_ttH',
        #'DNN_Out_6j3t_ttbarBB',
        #'DNN_Out_6j3t_ttbar2B',
        #'DNN_Out_6j3t_ttbarB',
        #'DNN_Out_6j3t_ttbarCC',
        #'DNN_Out_6j3t_ttbarlf',

        ## only 4 tag events 
        #'DNN_Out_4j3t_ttH',
        #'DNN_Out_4j3t_ttbarBB',
        #'DNN_Out_4j3t_ttbar2B',
        #'DNN_Out_4j3t_ttbarB',
        #'DNN_Out_4j3t_ttbarCC',
        #'DNN_Out_4j3t_ttbarlf',
        #'DNN_Out_5j3t_ttH',
        #'DNN_Out_5j3t_ttbarBB',
        #'DNN_Out_5j3t_ttbar2B',
        #'DNN_Out_5j3t_ttbarB',
        #'DNN_Out_5j3t_ttbarCC',
        #'DNN_Out_5j3t_ttbarlf',
        #'DNN_Out_6j3t_ttH',
        #'DNN_Out_6j3t_ttbarBB',
        #'DNN_Out_6j3t_ttbar2B',
        #'DNN_Out_6j3t_ttbarB',
        #'DNN_Out_6j3t_ttbarCC',
        #'DNN_Out_6j3t_ttbarlf',
    ]

    # 3 and 4 tags
    nhistobins_MultiDNN=[15, 15, 15, 15, 15, 15,
                         15, 15, 15, 15, 15, 15,
                         15, 15, 15, 12, 15, 15]

    minxvals_MultiDNN=[0.16, 0.16, 0.16, 0.2,  0.2,  0.2,
                       0.16, 0.16, 0.2,  0.2,  0.2,  0.2,
                       0.16, 0.16, 0.2,  0.2,  0.2,  0.2]

    maxxvals_MultiDNN=[0.75, 0.8,  0.65, 0.4,  0.4,  0.63,
                       0.85, 0.8,  0.6,  0.45, 0.4,  0.5,
                       0.85, 0.8,  0.65, 0.5,  0.4,  0.6]

    # 3 and 4 tags with minimal node output of 0.25
    #nhistobins_MultiDNN+=[15, 15, 15, 15, 15, 15,
    #                      15, 15, 15, 15, 15, 15,
    #                      15, 15, 15, 12, 15, 15]

    #minxvals_MultiDNN+=[0.25]*18
    #maxxvals_MultiDNN+=[0.75, 0.8, 0.65, 0.4,  0.4, 0.63,
    #                    0.85, 0.8, 0.6,  0.45, 0.4, 0.5,
    #                    0.85, 0.8, 0.65, 0.5,  0.4, 0.6]
    
    ## only 3 tags
    #nhistobins_MultiDNN+=[15,  15 , 15, 15,15, 15, 15, 15, 15, 15, 15, 15 , 15, 15, 15, 12, 15, 15  ]
    #minxvals_MultiDNN+=[0.16, 0.16, 0.16, 0.16, 0.2, 0.2,
                       #0.16, 0.16, 0.2, 0.16, 0.2, 0.2,
                       #0.16, 0.16, 0.16, 0.2, 0.2, 0.2        ]
    #maxxvals_MultiDNN+=[0.75, 0.8, 0.65, 0.4, 0.4, 0.63,
                       #0.85, 0.8, 0.6, 0.45, 0.4, 0.5,
                       #0.85, 0.8, 0.65, 0.5, 0.4, 0.6  ]

    ## only 4 tags
    #nhistobins_MultiDNN+=[9,  15 , 3, 3, 4, 5,
                          #10, 10, 4, 3, 4, 4 ,
                          #10, 10, 10, 4, 5, 5  ]
    #minxvals_MultiDNN+=[0.16, 0.25, 0.2, 0.2, 0.16, 0.16,
                        #0.2, 0.16, 0.2, 0.2, 0.2, 0.2,
                        #0.2, 0.2, 0.2, 0.2, 0.2, 0.2        ]
    #maxxvals_MultiDNN+=[0.85, 0.85, 0.3, 0.3, 0.3, 0.3,
                        #0.9, 0.9, 0.5, 0.35, 0.4, 0.5,
                        #0.9, 0.9, 0.45, 0.4, 0.4, 0.4     ]

    discrs+=discrs_MultiDNN
    nhistobins+=nhistobins_MultiDNN
    minxvals+=minxvals_MultiDNN
    maxxvals+=maxxvals_MultiDNN
    categories+=categorienames_MultiDNN
    
    # now do only MEM for 4 tag events 
    
    categorienames_MEM=[
        ### only 4 tag events 
        ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_tge4_MEM",""),
        ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4_MEM",""),             
        ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4_MEM",""),
        ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3_MEM",""),
        ]
    discrs_MEM=[
        memexp,
        memexp,
        memexp,
        memexp,
        ]

    #nhistobins_MultiDNN= [   7,   10,    12,   7,   7,    12,   7,   7,    7,   8,   7,    7,   7,   7,    7,   7,   7,    4,]
    #minxvals_MultiDNN=   [ 0.2,  0.16, 0.17, 0.16,  0.16, 0.18, 0.2,  0.2, 0.18, 0.2,  0.16, 0.16, 0.17,  0.17, 0.21, 0.17,  0.17, 0.19,]
    #maxxvals_MultiDNN=   [0.6,  0.6, 0.7,    0.6,  0.6, 0.7,    0.4,  0.4, 0.35,    0.55,  0.5, 0.55,    0.35,  0.35, 0.3,    0.5,  0.4, 0.3,]
    #nhistobins_MultiDNN+=[12,12,7,7,7,7]
    #minxvals_MultiDNN+=[0.17,0.18,0.18,0.16,0.21,0.19]
    #maxxvals_MultiDNN+=[0.7,0.7,0.35,0.55,0.3,0.3]
    nhistobins_MEM=[10,  10,  10,  20]
    minxvals_MEM=  [0.0, 0.0, 0.0, 0.0]
    maxxvals_MEM=  [1.0, 1.0, 1.0, 1.0]
    
    discrs+=discrs_MEM
    nhistobins+=nhistobins_MEM
    minxvals+=minxvals_MEM
    maxxvals+=maxxvals_MEM
    categories+=categorienames_MEM    
    
    
    ## plot the DNNs again but without the argmax classification
    ## DNN classes DNN outputs
    #categorienames_PlainDNN=[
              ## 3 tag and 4 tag events
              #("(N_Jets==4&&N_BTagsM>=3)","ljets_j4_tge3_plain_ttHnode",""),
              #("(N_Jets==4&&N_BTagsM>=3)","ljets_j4_tge3_plain_ttbbnode",""),
              #("(N_Jets==4&&N_BTagsM>=3)","ljets_j4_tge3_plain_tt2bnode",""),
              #("(N_Jets==4&&N_BTagsM>=3)","ljets_j4_tge3_plain_ttbnode",""),
              #("(N_Jets==4&&N_BTagsM>=3)","ljets_j4_tge3_plain_ttccnode",""),
              #("(N_Jets==4&&N_BTagsM>=3)","ljets_j4_tge3_plain_ttlfnode",""),
              
              #("(N_Jets==5&&N_BTagsM>=3)","ljets_j5_tge3_plain_ttHnode",""),             
              #("(N_Jets==5&&N_BTagsM>=3)","ljets_j5_tge3_plain_ttbbnode",""),             
              #("(N_Jets==5&&N_BTagsM>=3)","ljets_j5_tge3_plain_tt2bnode",""),             
              #("(N_Jets==5&&N_BTagsM>=3)","ljets_j5_tge3_plain_ttbnode",""),             
              #("(N_Jets==5&&N_BTagsM>=3)","ljets_j5_tge3_plain_ttccnode",""),             
              #("(N_Jets==5&&N_BTagsM>=3)","ljets_j5_tge3_plain_ttlfnode",""),             


              #("(N_Jets>=6&&N_BTagsM>=3)","ljets_jge6_tge3_plain_ttHnode",""),
              #("(N_Jets>=6&&N_BTagsM>=3)","ljets_jge6_tge3_plain_ttbbnode",""),
              #("(N_Jets>=6&&N_BTagsM>=3)","ljets_jge6_tge3_plain_tt2bnode",""),
              #("(N_Jets>=6&&N_BTagsM>=3)","ljets_jge6_tge3_plain_ttbnode",""),
              #("(N_Jets>=6&&N_BTagsM>=3)","ljets_jge6_tge3_plain_ttccnode",""),
              #("(N_Jets>=6&&N_BTagsM>=3)","ljets_jge6_tge3_plain_ttlfnode",""),


              #]
    
    
    #discrs_PlainDNN=[
        #'DNN_Out_4j3t_ttH',
        #'DNN_Out_4j3t_ttbarBB',
        #'DNN_Out_4j3t_ttbar2B',
        #'DNN_Out_4j3t_ttbarB',
        #'DNN_Out_4j3t_ttbarCC',
        #'DNN_Out_4j3t_ttbarlf',
        #'DNN_Out_5j3t_ttH',
        #'DNN_Out_5j3t_ttbarBB',
        #'DNN_Out_5j3t_ttbar2B',
        #'DNN_Out_5j3t_ttbarB',
        #'DNN_Out_5j3t_ttbarCC',
        #'DNN_Out_5j3t_ttbarlf',
        #'DNN_Out_6j3t_ttH',
        #'DNN_Out_6j3t_ttbarBB',
        #'DNN_Out_6j3t_ttbar2B',
        #'DNN_Out_6j3t_ttbarB',
        #'DNN_Out_6j3t_ttbarCC',
        #'DNN_Out_6j3t_ttbarlf',

    #]
    ##nhistobins_PlainDNN= [   7,   10,    12,   7,   7,    12,   7,   7,    7,   8,   7,    7,   7,   7,    7,   7,   7,    4,]
    ##minxvals_PlainDNN=   [ 0.2,  0.16, 0.17, 0.16,  0.16, 0.18, 0.2,  0.2, 0.18, 0.2,  0.16, 0.16, 0.17,  0.17, 0.21, 0.17,  0.17, 0.19,]
    ##maxxvals_PlainDNN=   [0.6,  0.6, 0.7,    0.6,  0.6, 0.7,    0.4,  0.4, 0.35,    0.55,  0.5, 0.55,    0.35,  0.35, 0.3,    0.5,  0.4, 0.3,]
    ##nhistobins_PlainDNN+=[12,12,7,7,7,7]
    ##minxvals_PlainDNN+=[0.17,0.18,0.18,0.16,0.21,0.19]
    ##maxxvals_PlainDNN+=[0.7,0.7,0.35,0.55,0.3,0.3]
    #nhistobins_PlainDNN=[50]*18
    #minxvals_PlainDNN=[0.0]*18
    #maxxvals_PlainDNN=[1.0]*18
    
    #discrs+=discrs_PlainDNN
    #nhistobins+=nhistobins_PlainDNN
    #minxvals+=minxvals_PlainDNN
    #maxxvals+=maxxvals_PlainDNN
    #categories+=categorienames_PlainDNN
            
    # get input for plotting function
    plotPreselections= [c[0] for c in categories]
    binlabels= [c[1] for c in categories]

    DNNplots = []
    print len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
    assert(len(set([len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals)]))==1)
    print len(zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals))

    for discr, b, bl, nb, minx, maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
        DNNplots.append(plotClasses.Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b,bl))

    data.categories += categories
    data.discrs += discrs
    data.nhistobins += nhistobins
    data.minxvals += minxvals
    data.maxxvals += maxxvals
    data.plotPreselections = plotPreselections
    data.binlabels = binlabels

    return DNNplots















def getDiscriminatorPlots(data = None, discrname = None):
    discriminatorPlots = add_plots()
    discriminatorPlots += add_sl6j4t()
    discriminatorPlots += add_sl6j3t()
    discriminatorPlots += add_sl5j4t()
    discriminatorPlots += add_sl5j3t()
    discriminatorPlots += add_sl4j4t()
    discriminatorPlots += add_sl4j3t()
    discriminatorPlots += add_dnn(data, discrname)

    return discriminatorPlots

