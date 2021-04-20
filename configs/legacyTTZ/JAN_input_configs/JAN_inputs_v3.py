
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import util.variableHistoInterface as vhi
import ROOT
from array import array
from copy import deepcopy


memexp = ""



def plots_ge4j_ge3t(data = None):
    label = "\geq 4 jets, \geq 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_N_BTagsM","N_BTagsM",5.0,3.5,8.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_N_Jets","N_Jets",7.0,3.5,10.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_E","boson candidate energy / GeV",50.0,0.0,1700.0),"RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_Eta","#eta of boson candidate",50.0,-5.0,5.0),"RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_M","boson candidate mass / GeV",50.0,0.0,500.0),"RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_Pt","boson candidate p_{T} / GeV",50.0,0.0,500.0),"RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_btagAverage","average of the two b-tag values",50.0,0.0,1.0),"RecoX_X_btagAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_dEta","#Delta#eta of boson candidate",50.0,0.0,4.7),"RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_dEta_lept","#Delta#eta between boson and lepton",nan,nan,nan),"RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_dPhi","#Delta#phi of boson candidate",50.0,0.0,3.14),"RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_dPhi_lept","#Delta#phi between boson and lepton",nan,nan,nan),"RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_dPt","#Deltap_{T} of boson candidate / GeV",50.0,0.0,700.0),"RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_dR","#DeltaR of boson candidate",50.0,0.4,4.0),"RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_dR_lept","#DeltaR between boson and lepton",50.0,0.0,6.0),"RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_X_openingAngle","opening angle of boson candidate",50.0,0.0,3.141),"RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_CvsB_deepJet","RecoX_jet1_CvsB_deepJet",nan,nan,nan),"RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_CvsL_deepJet","RecoX_jet1_CvsL_deepJet",nan,nan,nan),"RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_E","Energy of first jet / GeV",50.0,30.0,1500.0),"RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_Eta","#eta of first jet",nan,nan,nan),"RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_M","Mass of first jet / GeV",50.0,0.0,120.0),"RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_Phi","#phi of first jet",nan,nan,nan),"RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_Pt","p_{T} of first jet / GeV",50.0,30.0,700.0),"RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_btagValue","b-tag value of first jet",50.0,0.0,1.0),"RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50.0,0.0,4.7),"RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",nan,nan,nan),"RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50.0,0.4,4.4),"RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet1_idx","first jet index",nan,nan,nan),"RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_CvsB_deepJet","RecoX_jet2_CvsB_deepJet",nan,nan,nan),"RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_CvsL_deepJet","RecoX_jet2_CvsL_deepJet",nan,nan,nan),"RecoX_jet2_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_E","Energy of second jet / GeV",50.0,30.0,1100.0),"RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_Eta","#eta of second jet",nan,nan,nan),"RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_M","Mass of second jet / GeV",50.0,0.0,60.0),"RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_Phi","#phi of second jet",nan,nan,nan),"RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_Pt","p_{T} of second jet / GeV",50.0,30.0,500.0),"RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_btagValue","b-tag value of second jet",50.0,0.0,1.0),"RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50.0,0.0,4.7),"RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",nan,nan,nan),"RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50.0,0.4,5.5),"RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_RecoX_jet2_idx","second jet index",nan,nan,nan),"RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_TightLepton_E_0","lepton energy / GeV",50.0,0.0,1000.0),"TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_TightLepton_Eta_0","lepton #eta",50.0,-2.4,2.4),"TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_TightLepton_M_0","lepton mass / GeV",50.0,-0.3,0.3),"TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_TightLepton_Phi_0","lepton #phi",50.0,-3.1415,3.1415),"TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_TightLepton_Pt_0","lepton p_{T} / GeV",50.0,0.0,550.0),"TightLepton_Pt_0",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_dnn(data, discrname):

    ndefaultbins = 50
    interfaces = []


    # plots for ge4j_ge3t

    interf_ljets_ge4j_ge3t_Zbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_Zbb",
                                            label          = "ljets_ge4j_ge3t_Zbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==0))")
    interf_ljets_ge4j_ge3t_Zbb_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==0))","ljets_ge4j_ge3t_Zbb_node","")
    interf_ljets_ge4j_ge3t_Zbb_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_Zbb_node.bin_edges = [ 
				0.1616,
				0.1784,
				0.1951,
				0.2118,
				0.2286,
				0.2453,
				0.262,
				0.2788,
				0.2955,
				0.3122,
				0.329,
				0.3457,
				0.3624,
				0.3792,
				0.3959,
				0.4127,
				0.4294,
				0.4461,
				0.4629,
				0.4796,
				0.4963,
				0.5131,
				0.5298,
				0.5465,
				0.5633,
				0.58,
				0.5967,
				0.6135,
				0.6302,
				0.6469,
				0.6637,
				0.6804,
				0.6971,
				0.7139,
				0.7306,
				0.7473,
				0.7641,
				0.7808,
				0.7976,
				0.8143,
				0.831,
				0.8478,
				0.8645,
				0.8812,
				0.898,
				0.9147,
				0.9314,
				0.9482,
				0.9649,
				0.9816,
				0.99
				]
    interf_ljets_ge4j_ge3t_Zbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_Zbb_node)
    
    interf_ljets_ge4j_ge3t_Hbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_Hbb",
                                            label          = "ljets_ge4j_ge3t_Hbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==1))")
    interf_ljets_ge4j_ge3t_Hbb_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==1))","ljets_ge4j_ge3t_Hbb_node","")
    interf_ljets_ge4j_ge3t_Hbb_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_Hbb_node.bin_edges = [ 
				0.1618,
				0.1782,
				0.1945,
				0.2108,
				0.2271,
				0.2435,
				0.2598,
				0.2761,
				0.2924,
				0.3088,
				0.3251,
				0.3414,
				0.3578,
				0.3741,
				0.3904,
				0.4067,
				0.4231,
				0.4394,
				0.4557,
				0.472,
				0.4884,
				0.5047,
				0.521,
				0.5373,
				0.5537,
				0.57,
				0.5863,
				0.6027,
				0.619,
				0.6353,
				0.6516,
				0.668,
				0.6843,
				0.7006,
				0.7169,
				0.7333,
				0.7496,
				0.7659,
				0.7822,
				0.7986,
				0.8149,
				0.8312,
				0.8476,
				0.8639,
				0.8802,
				0.8965,
				0.9129,
				0.9292,
				0.9455,
				0.9618,
				0.97
				]
    interf_ljets_ge4j_ge3t_Hbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_Hbb_node)
    
    interf_ljets_ge4j_ge3t_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_bb",
                                            label          = "ljets_ge4j_ge3t_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==2))")
    interf_ljets_ge4j_ge3t_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==2))","ljets_ge4j_ge3t_bb_node","")
    interf_ljets_ge4j_ge3t_bb_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_bb_node.bin_edges = [ 
				0.1615,
				0.1785,
				0.1954,
				0.2123,
				0.2293,
				0.2462,
				0.2632,
				0.2801,
				0.297,
				0.314,
				0.3309,
				0.3479,
				0.3648,
				0.3817,
				0.3987,
				0.4156,
				0.4326,
				0.4495,
				0.4664,
				0.4834,
				0.5003,
				0.5172,
				0.5342,
				0.5511,
				0.5681,
				0.585,
				0.6019,
				0.6189,
				0.6358,
				0.6528,
				0.6697,
				0.6866,
				0.7036,
				0.7205,
				0.7374,
				0.7544,
				0.7713,
				0.7883,
				0.8052,
				0.8221,
				0.8391,
				0.856,
				0.873,
				0.8899,
				0.9068,
				0.9238,
				0.9407,
				0.9577,
				0.9746,
				0.9915,
				1.0
				]
    interf_ljets_ge4j_ge3t_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_bb_node)
    
    interf_ljets_ge4j_ge3t_cc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_cc",
                                            label          = "ljets_ge4j_ge3t_cc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==3))")
    interf_ljets_ge4j_ge3t_cc_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==3))","ljets_ge4j_ge3t_cc_node","")
    interf_ljets_ge4j_ge3t_cc_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_cc_node.bin_edges = [ 
				0.1617,
				0.1783,
				0.1948,
				0.2113,
				0.2279,
				0.2444,
				0.2609,
				0.2774,
				0.294,
				0.3105,
				0.327,
				0.3436,
				0.3601,
				0.3766,
				0.3932,
				0.4097,
				0.4262,
				0.4428,
				0.4593,
				0.4758,
				0.4923,
				0.5089,
				0.5254,
				0.5419,
				0.5585,
				0.575,
				0.5915,
				0.6081,
				0.6246,
				0.6411,
				0.6577,
				0.6742,
				0.6907,
				0.7072,
				0.7238,
				0.7403,
				0.7568,
				0.7734,
				0.7899,
				0.8064,
				0.823,
				0.8395,
				0.856,
				0.8726,
				0.8891,
				0.9056,
				0.9221,
				0.9387,
				0.9552,
				0.9717,
				0.98
				]
    interf_ljets_ge4j_ge3t_cc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_cc_node)
    
    interf_ljets_ge4j_ge3t_ttTobb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_ttTobb",
                                            label          = "ljets_ge4j_ge3t_ttTobb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==4))")
    interf_ljets_ge4j_ge3t_ttTobb_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==4))","ljets_ge4j_ge3t_ttTobb_node","")
    interf_ljets_ge4j_ge3t_ttTobb_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_ttTobb_node.bin_edges = [ 
				0.1616,
				0.1784,
				0.1951,
				0.2118,
				0.2286,
				0.2453,
				0.262,
				0.2788,
				0.2955,
				0.3122,
				0.329,
				0.3457,
				0.3624,
				0.3792,
				0.3959,
				0.4127,
				0.4294,
				0.4461,
				0.4629,
				0.4796,
				0.4963,
				0.5131,
				0.5298,
				0.5465,
				0.5633,
				0.58,
				0.5967,
				0.6135,
				0.6302,
				0.6469,
				0.6637,
				0.6804,
				0.6971,
				0.7139,
				0.7306,
				0.7473,
				0.7641,
				0.7808,
				0.7976,
				0.8143,
				0.831,
				0.8478,
				0.8645,
				0.8812,
				0.898,
				0.9147,
				0.9314,
				0.9482,
				0.9649,
				0.9816,
				0.99
				]
    interf_ljets_ge4j_ge3t_ttTobb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_ttTobb_node)
    
    interf_ljets_ge4j_ge3t_bkg_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_bkg",
                                            label          = "ljets_ge4j_ge3t_bkg_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==5))")
    interf_ljets_ge4j_ge3t_bkg_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==5))","ljets_ge4j_ge3t_bkg_node","")
    interf_ljets_ge4j_ge3t_bkg_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_bkg_node.bin_edges = [ 
				0.1615,
				0.1785,
				0.1954,
				0.2123,
				0.2293,
				0.2462,
				0.2632,
				0.2801,
				0.297,
				0.314,
				0.3309,
				0.3479,
				0.3648,
				0.3817,
				0.3987,
				0.4156,
				0.4326,
				0.4495,
				0.4664,
				0.4834,
				0.5003,
				0.5172,
				0.5342,
				0.5511,
				0.5681,
				0.585,
				0.6019,
				0.6189,
				0.6358,
				0.6528,
				0.6697,
				0.6866,
				0.7036,
				0.7205,
				0.7374,
				0.7544,
				0.7713,
				0.7883,
				0.8052,
				0.8221,
				0.8391,
				0.856,
				0.873,
				0.8899,
				0.9068,
				0.9238,
				0.9407,
				0.9577,
				0.9746,
				0.9915,
				1.0
				]
    interf_ljets_ge4j_ge3t_bkg_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_bkg_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge3t(data)
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def init_plots(interfaces, data = None):
    plots = [] #init list of plotClasses objects to return
    dictionary = {}
    for interf in interfaces:

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if not interf.bin_edges is None:
            bins  = array("f", interf.bin_edges)
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            interf.nhistobins = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,bins),
                    interf.varname,interf.selection,interf.category_label))

        elif not (interf.minxval is None or interf.maxxval is None):
            nbins = interf.nhistobins
            xmax  = interf.maxxval
            xmin  = interf.minxval
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,xmin, xmax),
                    interf.varname,interf.selection,interf.category_label))
        else:
            print("FATAL ERROR: Unable to load bin edges or min/max values for histogram!")
            print(interf)
            raise ValueError
        dictionary[interf.label] = interf.getDictionary()

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    