
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
				0.2,
				0.2252,
				0.2315,
				0.2378,
				0.2441,
				0.2504,
				0.2567,
				0.263,
				0.2693,
				0.2756,
				0.2819,
				0.2882,
				0.2945,
				0.3008,
				0.3071,
				0.3134,
				0.3197,
				0.326,
				0.3323,
				0.3386,
				0.3449,
				0.3512,
				0.3575,
				0.3638,
				0.3701,
				0.3764,
				0.3827,
				0.389,
				0.3953,
				0.4016,
				0.4079,
				0.4142,
				0.4205,
				0.4268,
				0.4331,
				0.4394,
				0.4457,
				0.452,
				0.4583,
				0.4646,
				0.4709,
				0.4772,
				0.4835,
				0.4898,
				0.4961,
				0.5024,
				0.5087,
				0.515,
				0.5213,
				0.5276,
				0.5339,
				0.5402,
				0.5465,
				0.5528,
				0.5591,
				0.5654,
				0.5717,
				0.578,
				0.5843,
				0.5906,
				0.5969,
				0.6032,
				0.6095,
				0.6158,
				0.6221,
				0.6284,
				0.6347,
				0.6473,
				0.6599,
				0.6725,
				0.6914,
				0.8363
				]
    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttb_bb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttb_bb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.223,
				0.2276,
				0.2322,
				0.2368,
				0.2414,
				0.246,
				0.2506,
				0.2552,
				0.2598,
				0.2644,
				0.269,
				0.2736,
				0.2782,
				0.2828,
				0.2874,
				0.292,
				0.2966,
				0.3012,
				0.3058,
				0.3104,
				0.315,
				0.3196,
				0.3242,
				0.3288,
				0.3334,
				0.338,
				0.3426,
				0.3472,
				0.3518,
				0.3564,
				0.361,
				0.3656,
				0.3702,
				0.3748,
				0.3794,
				0.384,
				0.3886,
				0.3932,
				0.3978,
				0.4024,
				0.407,
				0.4116,
				0.4162,
				0.4208,
				0.4254,
				0.43,
				0.4346,
				0.4392,
				0.4438,
				0.4484,
				0.453,
				0.4576,
				0.4622,
				0.4668,
				0.4714,
				0.476,
				0.4806,
				0.4852,
				0.4898,
				0.4944,
				0.499,
				0.5036,
				0.5082,
				0.5128,
				0.5174,
				0.522,
				0.5266,
				0.5312,
				0.5404,
				0.5496,
				0.5588,
				0.5726,
				0.591,
				0.6646
				]
    this_dict["ljets_ge4j_3t_ttb_bb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.222,
				0.2275,
				0.233,
				0.2385,
				0.244,
				0.2495,
				0.255,
				0.2605,
				0.266,
				0.2715,
				0.277,
				0.2825,
				0.288,
				0.2935,
				0.299,
				0.3045,
				0.31,
				0.3155,
				0.321,
				0.3265,
				0.332,
				0.3375,
				0.343,
				0.3485,
				0.354,
				0.3595,
				0.365,
				0.3705,
				0.376,
				0.3815,
				0.387,
				0.3925,
				0.398,
				0.4035,
				0.409,
				0.4145,
				0.42,
				0.4255,
				0.431,
				0.4365,
				0.442,
				0.4475,
				0.453,
				0.4585,
				0.464,
				0.4695,
				0.475,
				0.4805,
				0.486,
				0.4915,
				0.497,
				0.5025,
				0.508,
				0.5135,
				0.519,
				0.5245,
				0.53,
				0.5355,
				0.541,
				0.5465,
				0.552,
				0.5575,
				0.563,
				0.5685,
				0.5795,
				0.5905,
				0.6015,
				0.618,
				0.64,
				0.7555
				]
    this_dict["ljets_ge4j_3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2198,
				0.2242,
				0.2286,
				0.2308,
				0.233,
				0.2352,
				0.2374,
				0.2396,
				0.2418,
				0.244,
				0.2462,
				0.2484,
				0.2506,
				0.2528,
				0.255,
				0.2572,
				0.2594,
				0.2616,
				0.2638,
				0.266,
				0.2682,
				0.2704,
				0.2726,
				0.2748,
				0.277,
				0.2792,
				0.2814,
				0.2836,
				0.2858,
				0.288,
				0.2902,
				0.2924,
				0.2946,
				0.2968,
				0.299,
				0.3012,
				0.3034,
				0.3056,
				0.3078,
				0.31,
				0.3122,
				0.3144,
				0.3166,
				0.3188,
				0.321,
				0.3232,
				0.3254,
				0.3276,
				0.3298,
				0.332,
				0.3342,
				0.3364,
				0.3386,
				0.3408,
				0.343,
				0.3452,
				0.3474,
				0.3496,
				0.3518,
				0.354,
				0.3562,
				0.3584,
				0.3606,
				0.3628,
				0.365,
				0.3672,
				0.3694,
				0.3716,
				0.3738,
				0.376,
				0.3782,
				0.3804,
				0.3826,
				0.387,
				0.3914,
				0.4222
				]
    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2225,
				0.227,
				0.2315,
				0.236,
				0.2405,
				0.245,
				0.2495,
				0.254,
				0.2585,
				0.263,
				0.2675,
				0.272,
				0.2765,
				0.281,
				0.2855,
				0.29,
				0.2945,
				0.299,
				0.3035,
				0.308,
				0.3125,
				0.317,
				0.3215,
				0.326,
				0.3305,
				0.335,
				0.3395,
				0.344,
				0.3485,
				0.353,
				0.3575,
				0.362,
				0.3665,
				0.371,
				0.3755,
				0.38,
				0.3845,
				0.389,
				0.3935,
				0.398,
				0.4025,
				0.407,
				0.4115,
				0.416,
				0.4205,
				0.425,
				0.4295,
				0.434,
				0.4385,
				0.443,
				0.4475,
				0.452,
				0.4565,
				0.461,
				0.4655,
				0.47,
				0.4745,
				0.479,
				0.4835,
				0.488,
				0.4925,
				0.497,
				0.5015,
				0.506,
				0.5105,
				0.515,
				0.5195,
				0.524,
				0.5285,
				0.533,
				0.5375,
				0.542,
				0.5465,
				0.551,
				0.5555,
				0.56,
				0.5645,
				0.569,
				0.5735,
				0.578,
				0.5825,
				0.587,
				0.5915,
				0.596,
				0.6005,
				0.605,
				0.6095,
				0.614,
				0.6185,
				0.623,
				0.632,
				0.6545
				]
    this_dict["ljets_ge4j_3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2462,
				0.266,
				0.2792,
				0.2924,
				0.3056,
				0.3188,
				0.332,
				0.3452,
				0.3584,
				0.3716,
				0.3848,
				0.398,
				0.4112,
				0.4244,
				0.4376,
				0.4508,
				0.464,
				0.4772,
				0.4904,
				0.497,
				0.5036,
				0.5168,
				0.53,
				0.5432,
				0.5564,
				0.5696,
				0.5828,
				0.596,
				0.6092,
				0.6224,
				0.6356,
				0.6488,
				0.6686,
				0.6884,
				0.7082,
				0.7346,
				0.8666
				]
    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttb_bb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttb_bb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.247,
				0.2611,
				0.2705,
				0.2799,
				0.2893,
				0.2987,
				0.3081,
				0.3175,
				0.3222,
				0.3269,
				0.3363,
				0.341,
				0.3457,
				0.3504,
				0.3551,
				0.3598,
				0.3645,
				0.3692,
				0.3739,
				0.3786,
				0.3833,
				0.388,
				0.3927,
				0.3974,
				0.4021,
				0.4068,
				0.4115,
				0.4162,
				0.4209,
				0.4256,
				0.4303,
				0.435,
				0.4397,
				0.4444,
				0.4491,
				0.4538,
				0.4585,
				0.4632,
				0.4679,
				0.4726,
				0.482,
				0.4914,
				0.5008,
				0.5102,
				0.5196,
				0.529,
				0.5384,
				0.5478,
				0.5572,
				0.5666,
				0.5807,
				0.5948,
				0.6089,
				0.6277,
				0.6747
				]
    this_dict["ljets_ge4j_ge4t_ttb_bb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_tt2b"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2476,
				0.2578,
				0.2646,
				0.2714,
				0.2782,
				0.285,
				0.2884,
				0.2952,
				0.302,
				0.3088,
				0.3156,
				0.3224,
				0.3292,
				0.336,
				0.3428,
				0.3496,
				0.3564,
				0.3666,
				0.3768,
				0.387,
				0.4006,
				0.4176,
				0.5434
				]
    this_dict["ljets_ge4j_ge4t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2442,
				0.2546,
				0.2624,
				0.2676,
				0.2728,
				0.278,
				0.2832,
				0.2884,
				0.2936,
				0.2988,
				0.304,
				0.3092,
				0.3144,
				0.3196,
				0.3248,
				0.33,
				0.3352,
				0.3404,
				0.3456,
				0.3508,
				0.356,
				0.3638,
				0.369,
				0.3768,
				0.3846,
				0.395,
				0.408,
				0.4626
				]
    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.2,
				0.2484,
				0.2616,
				0.2704,
				0.2792,
				0.288,
				0.2968,
				0.3012,
				0.3056,
				0.31,
				0.3144,
				0.3188,
				0.3232,
				0.3276,
				0.332,
				0.3364,
				0.3408,
				0.3452,
				0.3496,
				0.354,
				0.3584,
				0.3628,
				0.3672,
				0.3716,
				0.376,
				0.3804,
				0.3848,
				0.3892,
				0.3936,
				0.398,
				0.4024,
				0.4068,
				0.4112,
				0.4156,
				0.42,
				0.4244,
				0.4288,
				0.4332,
				0.4376,
				0.4464,
				0.4552,
				0.464,
				0.4728,
				0.4816,
				0.4904,
				0.4992,
				0.5124,
				0.5256,
				0.5432,
				0.5696,
				0.6444
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
    