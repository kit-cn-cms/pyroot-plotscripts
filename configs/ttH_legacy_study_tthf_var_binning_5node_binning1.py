
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

def plots_dnn(data, discrname):

    ndefaultbins = 15
    category_dict = {}
    this_dict = {}

    # plots for ge4j_3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==0)","ljets_ge4j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1775,
				# 0.2225,
				0.2675,
				# 0.3125,
				0.3575,
				# 0.4025,
				0.4475,
				# 0.4925,
				0.5375,
				# 0.5825,
				0.6275,
				0.6725,
				0.7175,
				0.7625,
				0.8075,
				0.83 
			]
    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==1)","ljets_ge4j_3t_ttb_bb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttb_bb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1836,
				# 0.2164,
				0.2493,
				# 0.2821,
				0.315,
				# 0.3479,
				0.3807,
				# 0.4136,
				0.4464,
				# 0.4793,
				0.5121,
				0.545,
				0.5779,
				0.6107,
				0.6436,
				0.66 
			]
    this_dict["ljets_ge4j_3t_ttb_bb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==2)","ljets_ge4j_3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_tt2b"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.75

    this_dict["ljets_ge4j_3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==3)","ljets_ge4j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.42

    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==4)","ljets_ge4j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.65

    this_dict["ljets_ge4j_3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==0)","ljets_ge4j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1764,
				0.2236,
				0.2707,
				0.3179,
				0.365,
				0.4121,
				0.4593,
				0.5064,
				0.5536,
				0.6007,
				0.6479,
				0.695,
				0.7421,
				0.7893,
				0.8364,
				0.86 
			]
    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==1)","ljets_ge4j_ge4t_ttb_bb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttb_bb"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 0.1832,
				0.2168,
				0.2504,
				0.2839,
				0.3175,
				0.3511,
				0.3846,
				0.4182,
				0.4518,
				0.4854,
				0.5189,
				0.5525,
				0.5861,
				0.6196,
				0.6532,
				0.67 
			]
    this_dict["ljets_ge4j_ge4t_ttb_bb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==2)","ljets_ge4j_ge4t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_tt2b"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.54

    this_dict["ljets_ge4j_ge4t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==3)","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.46

    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==4)","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["nhistobins"] = 1
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.64

    this_dict["ljets_ge4j_ge4t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    

    for l in this_dict:
        this_dict[l]["histoname"] = discrname+"_"+l
        this_dict[l]["histotitle"] = "final discriminator ({})".format(l)
        this_dict[l]["plotPreselections"] = this_dict[l]["category"][0]

    DNNPlots = init_plots(dictionary = this_dict, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = None):
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
    