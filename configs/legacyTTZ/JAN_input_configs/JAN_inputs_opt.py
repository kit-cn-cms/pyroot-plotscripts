
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
				
				]
    interf_ljets_ge4j_ge3t_Zbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_Zbb_node)
    
    interf_ljets_ge4j_ge3t_Hbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_Hbb",
                                            label          = "ljets_ge4j_ge3t_Hbb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==1))")
    interf_ljets_ge4j_ge3t_Hbb_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==1))","ljets_ge4j_ge3t_Hbb_node","")
    interf_ljets_ge4j_ge3t_Hbb_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_Hbb_node.bin_edges = [ 
				
				]
    interf_ljets_ge4j_ge3t_Hbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_Hbb_node)
    
    interf_ljets_ge4j_ge3t_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_bb",
                                            label          = "ljets_ge4j_ge3t_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==2))")
    interf_ljets_ge4j_ge3t_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==2))","ljets_ge4j_ge3t_bb_node","")
    interf_ljets_ge4j_ge3t_bb_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_bb_node.bin_edges = [ 
				
				]
    interf_ljets_ge4j_ge3t_bb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_bb_node)
    
    interf_ljets_ge4j_ge3t_cc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_cc",
                                            label          = "ljets_ge4j_ge3t_cc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==3))")
    interf_ljets_ge4j_ge3t_cc_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==3))","ljets_ge4j_ge3t_cc_node","")
    interf_ljets_ge4j_ge3t_cc_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_cc_node.bin_edges = [ 
				
				]
    interf_ljets_ge4j_ge3t_cc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_cc_node)
    
    interf_ljets_ge4j_ge3t_ttTobb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_ttTobb",
                                            label          = "ljets_ge4j_ge3t_ttTobb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==4))")
    interf_ljets_ge4j_ge3t_ttTobb_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==4))","ljets_ge4j_ge3t_ttTobb_node","")
    interf_ljets_ge4j_ge3t_ttTobb_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_ttTobb_node.bin_edges = [ 
				
				]
    interf_ljets_ge4j_ge3t_ttTobb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_ttTobb_node)
    
    interf_ljets_ge4j_ge3t_bkg_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_bkg",
                                            label          = "ljets_ge4j_ge3t_bkg_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==5))")
    interf_ljets_ge4j_ge3t_bkg_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&((Evt_Odd==1))&&(DNNPredictedClass_ge4j_ge3t==5))","ljets_ge4j_ge3t_bkg_node","")
    interf_ljets_ge4j_ge3t_bkg_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_bkg_node.bin_edges = [ 
				
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
    