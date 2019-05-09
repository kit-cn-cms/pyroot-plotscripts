
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import ROOT



def evtYieldCategories():
    return [
    ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
    ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
    ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
    ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
    ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
    ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
    ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
    ]

memexp = ""


def plots_ge4j_3t():
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"BDT_common5_input_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"BDT_common5_input_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"BDT_common5_input_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_blr_ETH","btag likelihood ratio",30,0.0,1.0),"Evt_blr_ETH",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_memDBp","MEM",30,0.0,1.0),memexp,selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_JetPtOverJetE","p_{T}(jets)/E(jets)",30,0.2,1.0),"Evt_JetPtOverJetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_CSV_0","Jet CSV[0]",30,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"BDT_common5_input_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_HT_tag","H_{T}(tags)",30,100.0,900.0),"BDT_common5_input_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"BDT_common5_input_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Average","average btag value",30,0.3,1.0),"Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_blr_ETH_transformed","transformed btag likelihood ratio",30,-6.0,12.0),"Evt_blr_ETH_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_sphericity_jets","sphericity of jets",30,0.0,1.0),"BDT_common5_input_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        ]

    return plots

def plots_le5j_ge3t():
    label = "\leq 5 jets, \geq 3 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_BDT_common5_input_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"BDT_common5_input_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_BDT_common5_input_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"BDT_common5_input_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_BDT_common5_input_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"BDT_common5_input_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"BDT_common5_input_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_blr_ETH","btag likelihood ratio",30,0.0,1.0),"Evt_blr_ETH",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_memDBp","MEM",30,0.0,1.0),memexp,selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_BDT_common5_input_sphericity_jets","sphericity of jets",30,0.0,1.0),"BDT_common5_input_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_BDT_common5_input_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"BDT_common5_input_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_BDT_common5_input_HT_tag","H_{T}(tags)",30,100.0,900.0),"BDT_common5_input_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_Average","average btag value",30,0.3,1.0),"Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_blr_ETH_transformed","transformed btag likelihood ratio",30,-6.0,12.0),"Evt_blr_ETH_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        ]

    return plots

def plots_le5j_3t():
    label = "\leq 5 jets, 3 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM==3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_BDT_common5_input_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"BDT_common5_input_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_BDT_common5_input_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"BDT_common5_input_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_BDT_common5_input_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"BDT_common5_input_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"BDT_common5_input_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_blr_ETH","btag likelihood ratio",30,0.0,1.0),"Evt_blr_ETH",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_BDT_common5_input_sphericity_jets","sphericity of jets",30,0.0,1.0),"BDT_common5_input_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_BDT_common5_input_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"BDT_common5_input_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_BDT_common5_input_HT_tag","H_{T}(tags)",30,100.0,900.0),"BDT_common5_input_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_CSV_Average","average btag value",30,0.3,1.0),"Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Evt_blr_ETH_transformed","transformed btag likelihood ratio",30,-6.0,12.0),"Evt_blr_ETH_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_3t_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        ]

    return plots

def plots_le5j_ge4t():
    label = "\leq 5 jets, \geq 4 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM>=4)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_BDT_common5_input_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"BDT_common5_input_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_BDT_common5_input_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"BDT_common5_input_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_BDT_common5_input_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"BDT_common5_input_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"BDT_common5_input_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_blr_ETH","btag likelihood ratio",30,0.0,1.0),"Evt_blr_ETH",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_memDBp","MEM",30,0.0,1.0),memexp,selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_BDT_common5_input_sphericity_jets","sphericity of jets",30,0.0,1.0),"BDT_common5_input_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_BDT_common5_input_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"BDT_common5_input_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_BDT_common5_input_HT_tag","H_{T}(tags)",30,100.0,900.0),"BDT_common5_input_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_CSV_Average","average btag value",30,0.3,1.0),"Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Evt_blr_ETH_transformed","transformed btag likelihood ratio",30,-6.0,12.0),"Evt_blr_ETH_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge4t_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        ]

    return plots

def plots_ge4j_ge4t():
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"BDT_common5_input_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"BDT_common5_input_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"BDT_common5_input_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_blr_ETH","btag likelihood ratio",30,0.0,1.0),"Evt_blr_ETH",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_memDBp","MEM",30,0.0,1.0),memexp,selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_JetPtOverJetE","p_{T}(jets)/E(jets)",30,0.2,1.0),"Evt_JetPtOverJetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_CSV_0","Jet CSV[0]",30,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"BDT_common5_input_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_HT_tag","H_{T}(tags)",30,100.0,900.0),"BDT_common5_input_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"BDT_common5_input_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_Average","average btag value",30,0.3,1.0),"Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_blr_ETH_transformed","transformed btag likelihood ratio",30,-6.0,12.0),"Evt_blr_ETH_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_sphericity_jets","sphericity of jets",30,0.0,1.0),"BDT_common5_input_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        ]

    return plots

def plots_ge4j_3t():
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"BDT_common5_input_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"BDT_common5_input_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"BDT_common5_input_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_blr_ETH","btag likelihood ratio",30,0.0,1.0),"Evt_blr_ETH",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_memDBp","MEM",30,0.0,1.0),memexp,selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_JetPtOverJetE","p_{T}(jets)/E(jets)",30,0.2,1.0),"Evt_JetPtOverJetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_CSV_0","Jet CSV[0]",30,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"BDT_common5_input_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_HT_tag","H_{T}(tags)",30,100.0,900.0),"BDT_common5_input_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"BDT_common5_input_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Average","average btag value",30,0.3,1.0),"Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_blr_ETH_transformed","transformed btag likelihood ratio",30,-6.0,12.0),"Evt_blr_ETH_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_sphericity_jets","sphericity of jets",30,0.0,1.0),"BDT_common5_input_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        ]

    return plots


def plots_dnn(data, discrname):
    categories = []
    nhistobins = []
    minxvals = []
    maxxvals = []
    discrs = []

    ndefaultbins = 15




    # plots for ge4j_3t
    categories += [
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==0)","ljets_ge4j_3t_ttH_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==1)","ljets_ge4j_3t_ttb_bb_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==2)","ljets_ge4j_3t_tt2b_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==3)","ljets_ge4j_3t_ttcc_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==4)","ljets_ge4j_3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_ge4j_3t_node_ttH",
        "DNNOutput_ge4j_3t_node_ttb_bb",
        "DNNOutput_ge4j_3t_node_tt2b",
        "DNNOutput_ge4j_3t_node_ttcc",
        "DNNOutput_ge4j_3t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins]
    minxvals += [0.2, 0.2, 0.2, 0.2, 0.2]
    maxxvals += [0.83, 0.66, 0.75, 0.42, 0.65]





    # plots for le5j_ge3t
    categories += [
        ("((N_Jets<=5&&N_BTagsM>=3)&&DNNPredictedClass_le5j_ge3t==0)","ljets_le5j_ge3t_ttH_node",""),
        ("((N_Jets<=5&&N_BTagsM>=3)&&DNNPredictedClass_le5j_ge3t==1)","ljets_le5j_ge3t_ttb_bb_node",""),
        ("((N_Jets<=5&&N_BTagsM>=3)&&DNNPredictedClass_le5j_ge3t==2)","ljets_le5j_ge3t_tt2b_node",""),
        ("((N_Jets<=5&&N_BTagsM>=3)&&DNNPredictedClass_le5j_ge3t==3)","ljets_le5j_ge3t_ttcc_node",""),
        ("((N_Jets<=5&&N_BTagsM>=3)&&DNNPredictedClass_le5j_ge3t==4)","ljets_le5j_ge3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_le5j_ge3t_node_ttH",
        "DNNOutput_le5j_ge3t_node_ttb_bb",
        "DNNOutput_le5j_ge3t_node_tt2b",
        "DNNOutput_le5j_ge3t_node_ttcc",
        "DNNOutput_le5j_ge3t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins]
    minxvals += [0.2, 0.2, 0.2, 0.2, 0.2]
    maxxvals += [0.91, 0.66, 0.71, 0.42, 0.6]





    # plots for le5j_3t
    categories += [
        ("((N_Jets<=5&&N_BTagsM==3)&&DNNPredictedClass_le5j_3t==0)","ljets_le5j_3t_ttH_node",""),
        ("((N_Jets<=5&&N_BTagsM==3)&&DNNPredictedClass_le5j_3t==1)","ljets_le5j_3t_ttb_bb_node",""),
        ("((N_Jets<=5&&N_BTagsM==3)&&DNNPredictedClass_le5j_3t==2)","ljets_le5j_3t_tt2b_node",""),
        ("((N_Jets<=5&&N_BTagsM==3)&&DNNPredictedClass_le5j_3t==3)","ljets_le5j_3t_ttcc_node",""),
        ("((N_Jets<=5&&N_BTagsM==3)&&DNNPredictedClass_le5j_3t==4)","ljets_le5j_3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_le5j_3t_node_ttH",
        "DNNOutput_le5j_3t_node_ttb_bb",
        "DNNOutput_le5j_3t_node_tt2b",
        "DNNOutput_le5j_3t_node_ttcc",
        "DNNOutput_le5j_3t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins]
    minxvals += [0.2, 0.2, 0.2, 0.2, 0.2]
    maxxvals += [0.88, 0.58, 0.72, 0.42, 0.58]





    # plots for le5j_ge4t
    categories += [
        ("((N_Jets<=5&&N_BTagsM>=4)&&DNNPredictedClass_le5j_ge4t==0)","ljets_le5j_ge4t_ttH_node",""),
        ("((N_Jets<=5&&N_BTagsM>=4)&&DNNPredictedClass_le5j_ge4t==1)","ljets_le5j_ge4t_ttb_bb_node",""),
        ("((N_Jets<=5&&N_BTagsM>=4)&&DNNPredictedClass_le5j_ge4t==2)","ljets_le5j_ge4t_tt2b_node",""),
        ("((N_Jets<=5&&N_BTagsM>=4)&&DNNPredictedClass_le5j_ge4t==3)","ljets_le5j_ge4t_ttcc_node",""),
        ("((N_Jets<=5&&N_BTagsM>=4)&&DNNPredictedClass_le5j_ge4t==4)","ljets_le5j_ge4t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_le5j_ge4t_node_ttH",
        "DNNOutput_le5j_ge4t_node_ttb_bb",
        "DNNOutput_le5j_ge4t_node_tt2b",
        "DNNOutput_le5j_ge4t_node_ttcc",
        "DNNOutput_le5j_ge4t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins]
    minxvals += [0.2, 0.2, 0.2, 0.2, 0.2]
    maxxvals += [0.91, 0.61, 0.65, 0.45, 0.55]





    # plots for ge4j_ge4t
    categories += [
        ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==0)","ljets_ge4j_ge4t_ttH_node",""),
        ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==1)","ljets_ge4j_ge4t_ttb_bb_node",""),
        ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==2)","ljets_ge4j_ge4t_tt2b_node",""),
        ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==3)","ljets_ge4j_ge4t_ttcc_node",""),
        ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==4)","ljets_ge4j_ge4t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_ge4j_ge4t_node_ttH",
        "DNNOutput_ge4j_ge4t_node_ttb_bb",
        "DNNOutput_ge4j_ge4t_node_tt2b",
        "DNNOutput_ge4j_ge4t_node_ttcc",
        "DNNOutput_ge4j_ge4t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins]
    minxvals += [0.2, 0.2, 0.2, 0.2, 0.2]
    maxxvals += [0.86, 0.67, 0.54, 0.46, 0.64]





    # plots for ge4j_3t
    categories += [
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==0)","ljets_ge4j_3t_ttH_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==1)","ljets_ge4j_3t_ttb_bb_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==2)","ljets_ge4j_3t_tt2b_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==3)","ljets_ge4j_3t_ttcc_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==4)","ljets_ge4j_3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_ge4j_3t_node_ttH",
        "DNNOutput_ge4j_3t_node_ttb_bb",
        "DNNOutput_ge4j_3t_node_tt2b",
        "DNNOutput_ge4j_3t_node_ttcc",
        "DNNOutput_ge4j_3t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins, ndefaultbins]
    minxvals += [0.2, 0.2, 0.2, 0.2, 0.2]
    maxxvals += [0.83, 0.66, 0.75, 0.42, 0.65]



    plotPreselections = [c[0] for c in categories]
    binlabels =         [c[1] for c in categories]

    DNNPlots = []
    for discr, sel, label, nbins, minx, maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
        DNNPlots.append(
            plotClasses.Plot(
                ROOT.TH1F(discrname+"_"+label,"final discriminator ("+label+")",nbins,minx,maxx),
                discr,sel,label))

    data.categories += categories
    data.discrs     += discrs
    data.nhistobins += nhistobins
    data.minxvals   += minxvals
    data.maxxvals   += maxxvals
    
    data.plotPreselections  += plotPreselections
    data.binlabels          += binlabels

    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = None):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_3t()
    discriminatorPlots += plots_le5j_ge3t()
    discriminatorPlots += plots_le5j_3t()
    discriminatorPlots += plots_le5j_ge4t()
    discriminatorPlots += plots_ge4j_ge4t()
    discriminatorPlots += plots_ge4j_3t()
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots