
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
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Eta_0","#eta of leading jet",50,-2.6,2.6),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Eta_1","#eta of subleading jet",50,-2.6,2.6),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Eta_2","#eta of third jet",50,-2.6,2.6),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Eta_3","#eta of fourth jet",50,-2.6,2.6),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_M_0","Jet_M[0]",50,5.0,150.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_M_1","mass of subleading jet",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_M_2","mass of third jet",50,0.0,40.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,50.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Phi_0","#phi of leading jet",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Phi_1","#phi of subleading jet",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Phi_2","#phi of third jet",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Phi_3","#phi of fourth jet",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Pt_0","p_{T} of leading jet",50,0.0,500.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Pt_1","Jet_Pt[1]",50,0.0,400.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Pt_2","p_{T} of third jet",50,0.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",50,0.0,200.0),"Jet_Pt[3]",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    
def plots_dnn(data, discrname):

    ndefaultbins = 15
    interfaces = []


    # plots for ge4j_ge3t

    interf_ljets_ge4j_ge3t_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_ttH",
                                            label          = "ljets_ge4j_ge3t_ttH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==0))")
    interf_ljets_ge4j_ge3t_ttH_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==0))","ljets_ge4j_ge3t_ttH_node","")
    interf_ljets_ge4j_ge3t_ttH_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_ttH_node.minxval = 0.17
    interf_ljets_ge4j_ge3t_ttH_node.maxxval = 0.33
    interf_ljets_ge4j_ge3t_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_ttH_node)
    
    interf_ljets_ge4j_ge3t_tthf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_tthf",
                                            label          = "ljets_ge4j_ge3t_tthf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==1))")
    interf_ljets_ge4j_ge3t_tthf_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==1))","ljets_ge4j_ge3t_tthf_node","")
    interf_ljets_ge4j_ge3t_tthf_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_tthf_node.minxval = 0.17
    interf_ljets_ge4j_ge3t_tthf_node.maxxval = 0.31
    interf_ljets_ge4j_ge3t_tthf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_tthf_node)
    
    interf_ljets_ge4j_ge3t_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_ttHH",
                                            label          = "ljets_ge4j_ge3t_ttHH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==2))")
    interf_ljets_ge4j_ge3t_ttHH_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==2))","ljets_ge4j_ge3t_ttHH_node","")
    interf_ljets_ge4j_ge3t_ttHH_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_ttHH_node.minxval = 0.17
    interf_ljets_ge4j_ge3t_ttHH_node.maxxval = 0.78
    interf_ljets_ge4j_ge3t_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_ttHH_node)
    
    interf_ljets_ge4j_ge3t_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_tt4b",
                                            label          = "ljets_ge4j_ge3t_tt4b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==3))")
    interf_ljets_ge4j_ge3t_tt4b_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==3))","ljets_ge4j_ge3t_tt4b_node","")
    interf_ljets_ge4j_ge3t_tt4b_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_tt4b_node.minxval = 0.17
    interf_ljets_ge4j_ge3t_tt4b_node.maxxval = 0.95
    interf_ljets_ge4j_ge3t_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_tt4b_node)
    
    interf_ljets_ge4j_ge3t_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_ttcc",
                                            label          = "ljets_ge4j_ge3t_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==4))")
    interf_ljets_ge4j_ge3t_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==4))","ljets_ge4j_ge3t_ttcc_node","")
    interf_ljets_ge4j_ge3t_ttcc_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_ttcc_node.minxval = 0.17
    interf_ljets_ge4j_ge3t_ttcc_node.maxxval = 0.35
    interf_ljets_ge4j_ge3t_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_ttcc_node)
    
    interf_ljets_ge4j_ge3t_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_ttlf",
                                            label          = "ljets_ge4j_ge3t_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==5))")
    interf_ljets_ge4j_ge3t_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==5))","ljets_ge4j_ge3t_ttlf_node","")
    interf_ljets_ge4j_ge3t_ttlf_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_ttlf_node.minxval = 0.17
    interf_ljets_ge4j_ge3t_ttlf_node.maxxval = 0.57
    interf_ljets_ge4j_ge3t_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_ttlf_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
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
    