
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import ROOT
from array import array
from copy import deepcopy



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
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

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
def plots_ge4j_ge4t():
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

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

def plots_dnn(data, discrname):

    ndefaultbins = 15
    category_dict = {}
    this_dict = {}




    # plots for ge4j_3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.25,
				0.2686,
				0.2748,
				0.281,
				0.2872,
				0.2934,
				0.2996,
				0.3058,
				0.312,
				0.3182,
				0.3244,
				0.3306,
				0.3368,
				0.343,
				0.3492,
				0.3554,
				0.3616,
				0.3678,
				0.374,
				0.3802,
				0.3864,
				0.3926,
				0.3988,
				0.405,
				0.4112,
				0.4174,
				0.4236,
				0.4298,
				0.436,
				0.4422,
				0.4484,
				0.4546,
				0.4608,
				0.467,
				0.4732,
				0.4794,
				0.4856,
				0.4918,
				0.498,
				0.5042,
				0.5104,
				0.5166,
				0.5228,
				0.529,
				0.5352,
				0.5414,
				0.5476,
				0.5538,
				0.56,
				0.5662,
				0.5724,
				0.5786,
				0.5848,
				0.591,
				0.5972,
				0.6034,
				0.6096,
				0.6158,
				0.622,
				0.6282,
				0.6344,
				0.6406,
				0.6468,
				0.653,
				0.6592,
				0.6654,
				0.6716,
				0.6778,
				0.684,
				0.6902,
				0.6964,
				0.7026,
				0.7088,
				0.715,
				0.7212,
				0.7274,
				0.7336,
				0.746,
				0.7584,
				0.777,
				0.8762
				]
    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.25,
				0.2686,
				0.2748,
				0.281,
				0.2872,
				0.2934,
				0.2996,
				0.3058,
				0.312,
				0.3182,
				0.3244,
				0.3306,
				0.3368,
				0.343,
				0.3492,
				0.3554,
				0.3616,
				0.3678,
				0.374,
				0.3802,
				0.3864,
				0.3926,
				0.3988,
				0.405,
				0.4112,
				0.4174,
				0.4236,
				0.4298,
				0.436,
				0.4422,
				0.4484,
				0.4546,
				0.4608,
				0.467,
				0.4732,
				0.4794,
				0.4856,
				0.4918,
				0.498,
				0.5042,
				0.5104,
				0.5166,
				0.5228,
				0.529,
				0.5352,
				0.5414,
				0.5476,
				0.5538,
				0.56,
				0.5662,
				0.5724,
				0.5786,
				0.5848,
				0.591,
				0.5972,
				0.6034,
				0.6096,
				0.6158,
				0.622,
				0.6282,
				0.6344,
				0.6406,
				0.6468,
				0.653,
				0.6592,
				0.6654,
				0.6716,
				0.6778,
				0.684,
				0.6902,
				0.6964,
				0.7026,
				0.7088,
				0.715,
				0.7212,
				0.7274,
				0.7336,
				0.7398,
				0.746,
				0.7522,
				0.7584,
				0.7708,
				0.7832,
				0.7956,
				0.8762
				]
    this_dict["ljets_ge4j_3t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.25,
				0.265,
				0.268,
				0.271,
				0.274,
				0.277,
				0.28,
				0.283,
				0.286,
				0.289,
				0.292,
				0.295,
				0.298,
				0.301,
				0.304,
				0.307,
				0.31,
				0.313,
				0.316,
				0.319,
				0.322,
				0.325,
				0.328,
				0.331,
				0.334,
				0.337,
				0.34,
				0.343,
				0.346,
				0.349,
				0.352,
				0.355,
				0.358,
				0.361,
				0.364,
				0.367,
				0.37,
				0.373,
				0.376,
				0.379,
				0.382,
				0.385,
				0.388,
				0.391,
				0.394,
				0.397,
				0.4,
				0.403,
				0.406,
				0.409,
				0.412,
				0.415,
				0.418,
				0.421,
				0.424,
				0.427,
				0.43,
				0.433,
				0.436,
				0.439,
				0.442,
				0.445,
				0.448,
				0.451,
				0.454,
				0.457,
				0.46,
				0.463,
				0.466,
				0.469,
				0.472,
				0.475,
				0.478,
				0.481,
				0.484,
				0.487,
				0.49,
				0.493,
				0.496,
				0.502,
				0.508,
				0.517,
				0.553
				]
    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.25,
				0.268,
				0.2725,
				0.277,
				0.2815,
				0.286,
				0.2905,
				0.295,
				0.2995,
				0.304,
				0.3085,
				0.313,
				0.3175,
				0.322,
				0.3265,
				0.331,
				0.3355,
				0.34,
				0.3445,
				0.349,
				0.3535,
				0.358,
				0.3625,
				0.367,
				0.3715,
				0.376,
				0.3805,
				0.385,
				0.3895,
				0.394,
				0.3985,
				0.403,
				0.4075,
				0.412,
				0.4165,
				0.421,
				0.4255,
				0.43,
				0.4345,
				0.439,
				0.4435,
				0.448,
				0.4525,
				0.457,
				0.4615,
				0.466,
				0.4705,
				0.475,
				0.4795,
				0.484,
				0.4885,
				0.493,
				0.4975,
				0.502,
				0.5065,
				0.511,
				0.5155,
				0.52,
				0.5245,
				0.529,
				0.5335,
				0.538,
				0.5425,
				0.547,
				0.5515,
				0.556,
				0.5605,
				0.565,
				0.5695,
				0.574,
				0.5785,
				0.583,
				0.5875,
				0.592,
				0.5965,
				0.601,
				0.6055,
				0.61,
				0.6145,
				0.619,
				0.6235,
				0.628,
				0.6325,
				0.637,
				0.6415,
				0.646,
				0.6505,
				0.655,
				0.6595,
				0.664,
				0.6685,
				0.673,
				0.6775,
				0.7045
				]
    this_dict["ljets_ge4j_3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.25,
				0.3004,
				0.3193,
				0.3319,
				0.3445,
				0.3571,
				0.3697,
				0.3823,
				0.3949,
				0.4075,
				0.4201,
				0.4327,
				0.4453,
				0.4579,
				0.4705,
				0.4831,
				0.4894,
				0.4957,
				0.5083,
				0.5146,
				0.5209,
				0.5335,
				0.5398,
				0.5461,
				0.5524,
				0.565,
				0.5776,
				0.5902,
				0.6028,
				0.6154,
				0.628,
				0.6406,
				0.6532,
				0.6658,
				0.6784,
				0.691,
				0.7036,
				0.7162,
				0.7288,
				0.7414,
				0.7603,
				0.7792,
				0.8863
				]
    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_tthf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_tthf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.25,
				0.308,
				0.3196,
				0.3312,
				0.3428,
				0.3486,
				0.3544,
				0.3602,
				0.366,
				0.3718,
				0.3776,
				0.3892,
				0.395,
				0.4008,
				0.4066,
				0.4124,
				0.4182,
				0.424,
				0.4298,
				0.4356,
				0.4414,
				0.4472,
				0.453,
				0.4588,
				0.4646,
				0.4704,
				0.4762,
				0.482,
				0.4878,
				0.4936,
				0.4994,
				0.5052,
				0.511,
				0.5168,
				0.5226,
				0.5284,
				0.5342,
				0.54,
				0.5458,
				0.5516,
				0.5574,
				0.5632,
				0.569,
				0.5748,
				0.5806,
				0.5864,
				0.5922,
				0.598,
				0.6038,
				0.6096,
				0.6154,
				0.6212,
				0.627,
				0.6328,
				0.6444,
				0.656,
				0.6676,
				0.6792,
				0.6908,
				0.7024,
				0.714,
				0.7314,
				0.7488,
				0.7662,
				0.8358
				]
    this_dict["ljets_ge4j_ge4t_tthf_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.25,
				0.2986,
				0.3121,
				0.3202,
				0.3283,
				0.3337,
				0.3391,
				0.3445,
				0.3499,
				0.3553,
				0.3607,
				0.3661,
				0.3715,
				0.3769,
				0.3823,
				0.3877,
				0.3931,
				0.3985,
				0.4039,
				0.4066,
				0.4093,
				0.4147,
				0.4201,
				0.4255,
				0.4309,
				0.4363,
				0.4417,
				0.4471,
				0.4525,
				0.4579,
				0.4633,
				0.4687,
				0.4768,
				0.4849,
				0.4957,
				0.5227
				]
    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.25,
				0.3064,
				0.3205,
				0.3299,
				0.3393,
				0.3487,
				0.3581,
				0.3675,
				0.3769,
				0.3816,
				0.3863,
				0.391,
				0.3957,
				0.4004,
				0.4051,
				0.4098,
				0.4145,
				0.4192,
				0.4239,
				0.4286,
				0.4333,
				0.438,
				0.4427,
				0.4474,
				0.4521,
				0.4568,
				0.4615,
				0.4662,
				0.4709,
				0.4756,
				0.4803,
				0.485,
				0.4897,
				0.4944,
				0.4991,
				0.5038,
				0.5085,
				0.5132,
				0.5179,
				0.5226,
				0.532,
				0.5414,
				0.5508,
				0.5602,
				0.5696,
				0.579,
				0.5884,
				0.5978,
				0.6072,
				0.6213,
				0.6401,
				0.6636,
				0.7247
				]
    this_dict["ljets_ge4j_ge4t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    

    for l in this_dict:
        this_dict[l]["histoname"] = discrname+"_"+l
        this_dict[l]["histotitle"] = "final discriminator ({})".format(l)
        this_dict[l]["plotPreselections"] = this_dict[l]["category"][0]

    DNNPlots = init_plots(dictionary = this_dict, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_3t()
    discriminatorPlots += plots_ge4j_ge4t()
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def init_plots(dictionary, data = None):
    plots = [] #init list of plotClasses objects to return
    for label in dictionary:
        subdict = dictionary[label] #for easy access
        discr = subdict["discr"] # load discriminator name
        sel = subdict["plotPreselections"] # load selection
        histoname = subdict["histoname"] # load histogram name
        histotitle = subdict["histotitle"] # load histogram title

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if "bin_edges" in subdict:
            bins = array("f", subdict["bin_edges"])
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            subdict["nhistobins"] = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname,histotitle,nbins,bins),
                    discr,sel,label))
        elif "minxval" in subdict and "maxxval" in subdict:
            nbins = subdict["nhistobins"]
            xmax  = subdict["maxxval"]
            xmin  = subdict["minxval"]
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname, histotitle,nbins,xmin, xmax),
                    discr,sel,label))
    if not data is None:
        data.categories.update(dictionary)
    return plots
    