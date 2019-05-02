
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


def plots_ge6j_ge3t():
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_blr","btag likelihood ratio",30,0.0,1.0),"MVA_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_blr_transformed","transformed b-tag likelihood ratio",30,-7.0,14.0),"MVA_blr_transformed",selection,label),
        ]

    return plots

def plots_5j_ge3t():
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"MVA_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_sphericity_jets","sphericity of jets",30,0.0,1.0),"MVA_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"MVA_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        ]

    return plots

def plots_4j_ge3t():
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_DeepJetCSV_3","DeepJet btag value of fourth jet",30,0.0,1.0),"Jet_DeepJetCSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_sphericity_jets","sphericity of jets",30,0.0,1.0),"MVA_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_blr","btag likelihood ratio",30,0.0,1.0),"MVA_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"MVA_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_blr_transformed","transformed b-tag likelihood ratio",30,-7.0,14.0),"MVA_blr_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        ]

    return plots


def plots_dnn(data, discrname):
    categories = []
    nhistobins = []
    minxvals = []
    maxxvals = []
    discrs = []
    categories += [
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==0)","ljets_ge6j_ge3t_ttH_node",""),
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==1)","ljets_ge6j_ge3t_ttbb_node",""),
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==2)","ljets_ge6j_ge3t_tt2b_node",""),
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==3)","ljets_ge6j_ge3t_ttb_node",""),
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==4)","ljets_ge6j_ge3t_ttcc_node",""),
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==5)","ljets_ge6j_ge3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_ge6j_ge3t_node_ttH",
        "DNNOutput_ge6j_ge3t_node_ttbb",
        "DNNOutput_ge6j_ge3t_node_tt2b",
        "DNNOutput_ge6j_ge3t_node_ttb",
        "DNNOutput_ge6j_ge3t_node_ttcc",
        "DNNOutput_ge6j_ge3t_node_ttlf",
        ]
    nhistobins += [15, 15, 15, 15, 15, 15]
    minxvals += [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    maxxvals += [0.6, 0.7, 0.5, 0.45, 0.35, 0.45]


    categories += [
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==0)","ljets_5j_ge3t_ttH_node",""),
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==1)","ljets_5j_ge3t_ttbb_node",""),
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==2)","ljets_5j_ge3t_tt2b_node",""),
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==3)","ljets_5j_ge3t_ttb_node",""),
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==4)","ljets_5j_ge3t_ttcc_node",""),
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==5)","ljets_5j_ge3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_5j_ge3t_node_ttH",
        "DNNOutput_5j_ge3t_node_ttbb",
        "DNNOutput_5j_ge3t_node_tt2b",
        "DNNOutput_5j_ge3t_node_ttb",
        "DNNOutput_5j_ge3t_node_ttcc",
        "DNNOutput_5j_ge3t_node_ttlf",
        ]
    nhistobins += [15, 15, 15, 15, 15, 15]
    minxvals += [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    maxxvals += [0.7, 0.7, 0.5, 0.45, 0.35, 0.45]


    categories += [
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==0)","ljets_4j_ge3t_ttH_node",""),
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==1)","ljets_4j_ge3t_ttbb_node",""),
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==2)","ljets_4j_ge3t_tt2b_node",""),
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==3)","ljets_4j_ge3t_ttb_node",""),
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==4)","ljets_4j_ge3t_ttcc_node",""),
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==5)","ljets_4j_ge3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_4j_ge3t_node_ttH",
        "DNNOutput_4j_ge3t_node_ttbb",
        "DNNOutput_4j_ge3t_node_tt2b",
        "DNNOutput_4j_ge3t_node_ttb",
        "DNNOutput_4j_ge3t_node_ttcc",
        "DNNOutput_4j_ge3t_node_ttlf",
        ]
    nhistobins += [15, 15, 15, 15, 15, 15]
    minxvals += [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    maxxvals += [0.65, 0.65, 0.5, 0.4, 0.35, 0.45]



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
    discriminatorPlots += plots_ge6j_ge3t()
    discriminatorPlots += plots_5j_ge3t()
    discriminatorPlots += plots_4j_ge3t()
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots
