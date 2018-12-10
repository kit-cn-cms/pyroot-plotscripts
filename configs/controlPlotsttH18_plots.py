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
        plotClasses.Plot(ROOT.TH1D("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,categoriesJTsel,"1 lepton"),
        #plotClasses.Plot(ROOT.TH1D("BCAT" ,"jet-tag + boosted categories",len(categoriesJTB),0.5,0.5+len(categoriesJTB)),catstringJTB,categoriesJTBsel,"1 lepton"),
        plotClasses.Plot(ROOT.TH1D("N_Jets","Number of ak4 jets",11,3.5,14.5),"N_Jets",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("CSV0","B-tag of leading jet",22,-.1,1),"Jet_CSV[0]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("CSV1","B-tag of second jet",22,-.1,1),"Jet_CSV[1]",plotselection,plotlabel),
        plotClasses.Plot(ROOT.TH1D("CSV","B-tag of all jets",22,-.1,1),"Jet_CSV",plotselection,plotlabel),
        
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
        plotClasses.Plot(ROOT.TH1D("AK8Jet_tau21","AK8 jet tau 21",50,0,1),"AK8Jet_Tau2/AK8Jet_Tau1",plotselectionboosted,plotlabel),
        plotClasses.Plot(ROOT.TH1D("AK8Jet_tau32","AK8 jet tau 32",50,0,1),"AK8Jet_Tau3/AK8Jet_Tau2",plotselectionboosted,plotlabel),
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
        plotClasses.Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0.0,1.0),memexp,plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
    ]

    return plots43



def add_sl4j4t():
    plotlabel="1 lepton, 4 jets, 4 b-tags"
    plotselection=categoriesJT[4][0]
    plotprefix="s44_"
    # weights_Final_44_MEMBDTv2.xml
    plots44=[
        plotClasses.Plot(ROOT.TH1D(plotprefix+"MEM","MEM",20,0.0,1.0),memexp,plotselection,plotlabel),
        #plotClasses.Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",20,0.6,1.0),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
    ]

    return plots44



def add_sl5j3t():
    plotlabel="1 lepton, 5 jets, 3 b-tags"
    plotselection=categoriesJT[2][0]
    plotprefix="s53_"
    plots53=[
        plotClasses.Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0.0,1.0),memexp,plotselection,plotlabel),
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





def add_sl6j3tDNN():
    plotlabel="1 lepton, #geq6 jets, #geq3 b-tags"
    plotselection="((N_Jets>=6&&N_BTagsM>=3))"
    plotprefix="s63DNN_"
    plots63DNN = [
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.02,1.81),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.18,0.37),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-1.99,1.94),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.18,0.23),"BDT_common5_input_h3",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,18.02,861.33),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.01,3.17),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,16.22,515.07),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,2.6,910.95),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,-9.9,-9.9),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,31.53,583.19),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,20.06,1000.58),"BDT_common5_input_MET",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.19,2.39),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.01,8.39),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.5,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.21,0.65),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,30.75,345.31),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,1.71,23.94),"Evt_M_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0.34,4.56),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.1,0.33),"BDT_common5_input_h2",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,221.38,2875.98),"BDT_common5_input_HT",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,18.02,861.33),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.49,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.41,3.42),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.49,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.42),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.12,1.81),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,4.22,89.32),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,26.52,1009.42),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.41,3.46),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.51,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.51,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,49.98,4132.41),"BDT_common5_input_M3",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.25,0.96),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.14,0.44),"BDT_common5_input_h0",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-6.0,8.42),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-2.38,2.39),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,28.98,946.66),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,22.13,1173.17),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,49.98,4132.41),"Evt_M3",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.0),"Evt_blr_ETH",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,26.0,508.25),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,298.32,3568.78),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.55,4.17),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,0.47),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.41,3.46),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,-99.0,348.62),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.06),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0,1),memexp,plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.01,1.56),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,35.5,731.42),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.39,2.1),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,1.12,3.21),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,16.82,1124.39),"BDT_common5_input_Mlb",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,-0.1,0.28),"Evt_CSV_Min",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.55,4.17),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,43.47,1262.57),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.41,4.55),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,42.21,822.56),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.02,0.88),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,0.01,0.49),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.59,775.84),"BDT_common5_input_MHT",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,363.37,6764.74),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
    ]
    
    return plots63DNN


def add_sl5j3tDNN():
    plotlabel="1 lepton, 5 jets, #geq3 b-tags"
    plotselection="((N_Jets==5&&N_BTagsM>=3))"
    plotprefix="s53DNN_"

    plots53DNN = [
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.03,1.74),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.2,0.35),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-1.94,1.94),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.19,0.26),"BDT_common5_input_h3",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,18.68,701.63),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.02,3.15),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,17.71,540.7),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,4.5,875.86),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,-9.9,-9.9),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,31.06,367.44),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,20.01,916.31),"BDT_common5_input_MET",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.1,2.65),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,0.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.5,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.32,0.75),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,30.06,226.82),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,2.62,22.36),"Evt_M_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0.3,4.76),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.12,0.34),"BDT_common5_input_h2",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,171.35,1767.02),"BDT_common5_input_HT",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,18.68,701.63),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.49,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.4,3.47),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.49,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.45),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.04,1.74),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,5.09,53.99),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,26.19,1154.1),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.4,3.36),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.52,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.52,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,47.17,3078.04),"BDT_common5_input_M3",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.23,0.99),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.13,0.4),"BDT_common5_input_h0",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-8.88,8.36),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-2.4,2.4),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,32.83,1103.22),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,29.3,1153.92),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,47.17,3078.04),"Evt_M3",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.0),"Evt_blr_ETH",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,26.01,675.21),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,245.99,2657.9),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.53,4.1),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-0.1,0.47),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.4,3.36),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,-99.0,348.85),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.06),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0,1),memexp,plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.01,1.55),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,32.99,665.85),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.4,2.24),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,1.18,3.56),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,17.13,573.16),"BDT_common5_input_Mlb",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,-0.1,0.47),"Evt_CSV_Min",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.53,4.1),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,38.94,1323.06),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.4,3.55),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,43.3,1342.05),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.01,0.92),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,0.49),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,1.43,925.82),"BDT_common5_input_MHT",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,303.69,4137.55),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
    ]
    
    return plots53DNN

def add_sl4j3tDNN():
    plotlabel="1 lepton, 4 jets, #geq3 b-tags"
    plotselection="((N_Jets==4&&N_BTagsM>=3))"
    plotprefix="s43DNN_"

    plots43DNN = [
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_tag","BDT_common5_input_maxeta_jet_tag",30,0.02,1.7),"BDT_common5_input_maxeta_jet_tag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h1","BDT_common5_input_h1",30,-0.21,0.35),"BDT_common5_input_h1",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Eta_JetsAverage","Evt_Eta_JetsAverage",30,-2.13,2.09),"Evt_Eta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h3","BDT_common5_input_h3",30,-0.2,0.27),"BDT_common5_input_h3",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRTaggedJets","Evt_M_MinDeltaRTaggedJets",30,17.72,695.16),"Evt_M_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Deta_TaggedJetsAverage","Evt_Deta_TaggedJetsAverage",30,0.01,3.08),"Evt_Deta_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_MinDeltaRJets","Evt_M_MinDeltaRJets",30,17.53,525.74),"Evt_M_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRTaggedJets","Evt_Pt_MinDeltaRTaggedJets",30,3.66,1058.73),"Evt_Pt_MinDeltaRTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_best_higgs_mass","BDT_common5_input_best_higgs_mass",30,-9.9,-9.9),"BDT_common5_input_best_higgs_mass",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_jet_pt","BDT_common5_input_third_jet_pt",30,30.02,309.91),"BDT_common5_input_third_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MET","BDT_common5_input_MET",30,20.01,797.98),"BDT_common5_input_MET",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_Deta_JetsAverage","BDT_common5_input_Evt_Deta_JetsAverage",30,0.02,2.88),"BDT_common5_input_Evt_Deta_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dEta_fn","BDT_common5_input_dEta_fn",30,0.0,0.0),"BDT_common5_input_dEta_fn",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_highest_btag","BDT_common5_input_second_highest_btag",30,0.5,1.0),"BDT_common5_input_second_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Evt_CSV_Average","BDT_common5_input_Evt_CSV_Average",30,0.39,0.86),"BDT_common5_input_Evt_CSV_Average",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_jet_pt","BDT_common5_input_fourth_jet_pt",30,30.0,250.22),"BDT_common5_input_fourth_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_JetsAverage","Evt_M_JetsAverage",30,3.3,44.21),"Evt_M_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Jet_MaxDeta_Jets","Evt_Jet_MaxDeta_Jets",30,0.12,4.92),"Evt_Jet_MaxDeta_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h2","BDT_common5_input_h2",30,-0.14,0.32),"BDT_common5_input_h2",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_HT","BDT_common5_input_HT",30,132.31,1587.17),"BDT_common5_input_HT",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_closest_tagged_dijet_mass","BDT_common5_input_closest_tagged_dijet_mass",30,17.72,695.16),"BDT_common5_input_closest_tagged_dijet_mass",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_lowest_btag","BDT_common5_input_lowest_btag",30,0.49,1.0),"BDT_common5_input_lowest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_min_dr_tagged_jets","BDT_common5_input_min_dr_tagged_jets",30,0.39,3.63),"BDT_common5_input_min_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_third_highest_btag","BDT_common5_input_third_highest_btag",30,0.49,1.0),"BDT_common5_input_third_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_aplanarity","BDT_common5_input_aplanarity",30,0.0,0.42),"BDT_common5_input_aplanarity",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_jet_jet","BDT_common5_input_maxeta_jet_jet",30,0.02,1.7),"BDT_common5_input_maxeta_jet_jet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_TaggedJetsAverage","Evt_M_TaggedJetsAverage",30,4.77,86.11),"Evt_M_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_E_PrimaryLepton","Evt_E_PrimaryLepton",30,26.06,1159.94),"Evt_E_PrimaryLepton",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dr_between_lep_and_closest_jet","BDT_common5_input_dr_between_lep_and_closest_jet",30,0.4,3.47),"BDT_common5_input_dr_between_lep_and_closest_jet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Average_Tagged","Evt_CSV_Average_Tagged",30,0.51,1.0),"Evt_CSV_Average_Tagged",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_btag_disc_btags","BDT_common5_input_avg_btag_disc_btags",30,0.51,1.0),"BDT_common5_input_avg_btag_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_M3","BDT_common5_input_M3",30,43.29,1823.53),"BDT_common5_input_M3",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_pt_all_jets_over_E_all_jets","BDT_common5_input_pt_all_jets_over_E_all_jets",30,0.21,0.99),"BDT_common5_input_pt_all_jets_over_E_all_jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_h0","BDT_common5_input_h0",30,0.09,0.37),"BDT_common5_input_h0",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH_transformed","Evt_blr_ETH_transformed",30,-11.63,7.72),"Evt_blr_ETH_transformed",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Eta_PrimaryLepton","Evt_Eta_PrimaryLepton",30,-2.4,2.4),"Evt_Eta_PrimaryLepton",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M2_TaggedJetsAverage","Evt_M2_TaggedJetsAverage",30,31.29,933.36),"Evt_M2_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M_MedianTaggedJets","Evt_M_MedianTaggedJets",30,28.59,1081.63),"Evt_M_MedianTaggedJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_M3","Evt_M3",30,43.29,1823.53),"Evt_M3",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_blr_ETH","Evt_blr_ETH",30,0.0,1.0),"Evt_blr_ETH",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Pt_PrimaryLepton","Evt_Pt_PrimaryLepton",30,26.02,482.72),"Evt_Pt_PrimaryLepton",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_all_sum_pt_with_met","BDT_common5_input_all_sum_pt_with_met",30,210.94,2186.35),"BDT_common5_input_all_sum_pt_with_met",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_avg_dr_tagged_jets","BDT_common5_input_avg_dr_tagged_jets",30,0.53,4.05),"BDT_common5_input_avg_dr_tagged_jets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fifth_highest_CSV","BDT_common5_input_fifth_highest_CSV",30,-1.0,-1.0),"BDT_common5_input_fifth_highest_CSV",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonJet","Evt_Dr_MinDeltaRLeptonJet",30,0.4,3.47),"Evt_Dr_MinDeltaRLeptonJet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_tagged_dijet_mass_closest_to_125","BDT_common5_input_tagged_dijet_mass_closest_to_125",30,-99.0,348.86),"BDT_common5_input_tagged_dijet_mass_closest_to_125",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_dev_from_avg_disc_btags","BDT_common5_input_dev_from_avg_disc_btags",30,0.0,0.06),"BDT_common5_input_dev_from_avg_disc_btags",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"MEM","MEM",30,0,1),memexp,plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_maxeta_tag_tag","BDT_common5_input_maxeta_tag_tag",30,0.01,1.54),"BDT_common5_input_maxeta_tag_tag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_second_jet_pt","BDT_common5_input_second_jet_pt",30,31.6,586.67),"BDT_common5_input_second_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRJets","Evt_Dr_MinDeltaRJets",30,0.39,3.03),"Evt_Dr_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_JetsAverage","Evt_Dr_JetsAverage",30,0.87,3.8),"Evt_Dr_JetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_Mlb","BDT_common5_input_Mlb",30,16.83,542.31),"BDT_common5_input_Mlb",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_CSV_Min","Evt_CSV_Min",30,-0.1,0.49),"Evt_CSV_Min",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_TaggedJetsAverage","Evt_Dr_TaggedJetsAverage",30,0.53,4.05),"Evt_Dr_TaggedJetsAverage",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_first_jet_pt","BDT_common5_input_first_jet_pt",30,34.11,929.54),"BDT_common5_input_first_jet_pt",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Dr_MinDeltaRLeptonTaggedJet","Evt_Dr_MinDeltaRLeptonTaggedJet",30,0.4,3.77),"Evt_Dr_MinDeltaRLeptonTaggedJet",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"Evt_Pt_MinDeltaRJets","Evt_Pt_MinDeltaRJets",30,9.22,1058.73),"Evt_Pt_MinDeltaRJets",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_sphericity","BDT_common5_input_sphericity",30,0.01,0.93),"BDT_common5_input_sphericity",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_fourth_highest_btag","BDT_common5_input_fourth_highest_btag",30,-0.1,0.49),"BDT_common5_input_fourth_highest_btag",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_MHT","BDT_common5_input_MHT",30,0.86,660.85),"BDT_common5_input_MHT",plotselection,plotlabel),
        Plot(ROOT.TH1D(plotprefix+"BDT_common5_input_invariant_mass_of_everything","BDT_common5_input_invariant_mass_of_everything",30,249.55,3475.23),"BDT_common5_input_invariant_mass_of_everything",plotselection,plotlabel),
    ]







def getDiscriminatorPlots(data = None, discrname = None):
    discriminatorPlots = add_plots()
    discriminatorPlots += add_ak8()
    discriminatorPlots += add_sl6j4t()
    discriminatorPlots += add_sl6j3t()
    discriminatorPlots += add_sl5j4t()
    discriminatorPlots += add_sl5j3t()
    discriminatorPlots += add_sl4j4t()
    discriminatorPlots += add_sl4j3t()
    discriminatorPlots += add_sl4j3tDNN()
    discriminatorPlots += add_sl5j3tDNN()
    discriminatorPlots += add_sl6j3tDNN()


    return discriminatorPlots

