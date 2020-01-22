
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

yieldExpression = "(N_Jets==4 && N_BTagsM==3)*1"
yieldExpression+="+(N_Jets==5 && N_BTagsM==3)*2"
yieldExpression+="+(N_Jets>=6 && N_BTagsM==3)*3"
yieldExpression+="+(N_Jets==4 && N_BTagsM>=4)*4"
yieldExpression+="+(N_Jets==5 && N_BTagsM>=4)*5"
yieldExpression+="+(N_Jets>=6 && N_BTagsM>=4)*6"



def plots_control_mem(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_memDBp","MEM",30,0.0,1.0),memexp,selection,label)
    ]
    return plots

def plots_control(cat,selection,label):
    plots = [
        plotClasses.Plot(ROOT.TH1D(cat+"_memDBp","MEM",30,0.0,1.0),memexp,selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_evtYields","event yields",6,0.5,6.5),yieldExpression,selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_yields","total yield",1,-1.,1.),"0.",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_N_PV","N_PrimaryVertices",80,0,80),"N_PrimaryVertices",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Pt","p_{T}(electron)",50,0,400),"Electron_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_E","E(electron)",50,0,450),"Electron_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Eta","#eta(electron)",50,-2.5,2.5),"Electron_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Electron_Phi","#phi(electron)",50,-3.3,3.3),"Electron_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Pt","p_{T}(muon)",50,0,300),"Muon_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_E","E(muon)",50,0,450),"Muon_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Eta","#eta(muon)",50,-2.5,2.5),"Muon_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Muon_Phi","#phi(muon)",50,-3.3,3.3),"Muon_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Pt","p_{T}(lepton)",50,0,300),"LooseLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_E","E(lepton)",50,0,450),"LooseLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Eta","#eta(lepton)",50,-2.5,2.5),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Lepton_Phi","#phi(lepton)",50,-3.141,3.141),"LooseLepton_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Pt","p_{T}(tight lepton)",50,0,300),"TightLepton_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_E","E(tight lepton)",50,0,450),"TightLepton_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Eta","#eta(tight lepton)",50,-2.5,2.5),"TightLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_TightLepton_Phi","#phi(tight lepton)",50,-3.141,3.141),"TightLepton_Phi[0]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_N_BTagsM","N_BTagsM",8,2.5,10.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_N_Jets","N_Jets",9,3.5,12.5),"N_Jets",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_HT","H_{T}",45,150.0,1500.0),"Evt_HT",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV","Jet_CSV",30,0.0,1.0),"Jet_CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_0","Jet CSV[0]",30,0.3,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_1","Jet CSV[1]",30,0.3,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_2","Jet CSV[2]",30,0.3,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV","CSV",30,0,1),"CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_0","CSV[0]",30,0.3,1.0),"CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_1","CSV[1]",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_2","CSV[2]",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_CSV_3","CSV[3]",30,0.0,1.0),"CSV[3]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_blr","Evt_blr",30,-0.05,1.0),"Evt_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Evt_blr_transformed","Evt_blr_transformed",30,-6.0,16.0),"Evt_blr_transformed",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_0","Jet_Pt[0]",30,20,500),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_1","Jet_Pt[1]",30,20,500),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_2","Jet_Pt[2]",30,20,350),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt_3","Jet_Pt[3]",30,20,250),"Jet_Pt[3]",selection,label),

        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_E","Jet_E",60,0,800),"Jet_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Eta","Jet_Eta",30,-2.5,2.5),"Jet_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_M","Jet_M",30,0.0,50.0),"Jet_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Phi","Jet_Phi",30,-3.3,3.3),"Jet_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_Jet_Pt","Jet_Pt",40,20,400),"Jet_Pt",selection,label),
        ]
    return plots

def plots_HiggsReco(cat,selection,label):
    plots_Higgs=[
        #plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_BJet1_E","RecoHiggs_BJet1_E",50,0.,400.),"RecoHiggs_BJet1_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_BJet1_Eta","RecoHiggs_BJet1_Eta",50,-2.5,2.5),"RecoHiggs_BJet1_Eta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_BJet1_M","RecoHiggs_BJet1_M",50,0.,100.),"RecoHiggs_BJet1_M",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_BJet1_Phi","RecoHiggs_BJet1_Phi",50,-3.141,3.141),"RecoHiggs_BJet1_Phi",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_BJet1_Pt","RecoHiggs_BJet1_Pt",50,0.,400.),"RecoHiggs_BJet1_Pt",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_BJet2_E","RecoHiggs_BJet2_E",50,0.,400.),"RecoHiggs_BJet2_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_BJet2_Eta","RecoHiggs_BJet2_Eta",50,-2.5,2.5),"RecoHiggs_BJet2_Eta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_BJet2_M","RecoHiggs_BJet2_M",50,0.,100.),"RecoHiggs_BJet2_M",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_BJet2_Phi","RecoHiggs_BJet2_Phi",50,-3.141,3.141),"RecoHiggs_BJet2_Phi",selection,label),
        #plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_BJet2_Pt","RecoHiggs_BJet2_Pt",50,0.,400.),"RecoHiggs_BJet2_Pt",selection,label),


        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_Chi2","RecoHiggs_Chi2",50,0.,10.),"RecoHiggs_Chi2",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_Deta","RecoHiggs_Deta",50,0.,5.),"RecoHiggs_Deta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_Dphi","RecoHiggs_Dphi",50,0.,2.*3.141),"RecoHiggs_Dphi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_Dr","RecoHiggs_Dr",50,0.,6.),"RecoHiggs_Dr",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_E","RecoHiggs_E",50,0.,1000.),"RecoHiggs_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_Eta","RecoHiggs_Eta",50,-4.5,4.5),"RecoHiggs_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_M","RecoHiggs_M",50,0.,300.),"RecoHiggs_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_Phi","RecoHiggs_Phi",50,-3.141,3.141),"RecoHiggs_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_Pt","RecoHiggs_Pt",50,0.,500.),"RecoHiggs_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_cosdTheta","RecoHiggs_cosdTheta",50,-1.,1.),"RecoHiggs_cosdTheta",selection,label),
        plotClasses.Plot(ROOT.TH1D(cat+"_RecoHiggs_logChi2","RecoHiggs_logChi2",50,-10.,10.),"RecoHiggs_logChi2",selection,label),
    ]
    return plots_Higgs



#baseline
def plots_ge4j_ge3t(data=None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    tag = "ge4j_ge3t"
    # plots = plots_control_mem(tag, selection, label)    
    plots = plots_control(tag, selection, label)    
    plots += plots_HiggsReco(tag, selection, label)

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

#analysis categories w/o forward stuff
def plots_ge4j_3t(data=None):
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"

    tag = "ge4j_3t"
    # plots = plots_control_mem(tag, selection, label)    
    plots = plots_control(tag, selection, label)    
    plots += plots_HiggsReco(tag, selection, label)

    if data:
        add_data_plots(plots=plots,data=data)

    return plots

def plots_ge4j_ge4t(data=None):
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)"

    tag = "ge4j_ge4t"
    # plots = plots_control_mem(tag, selection, label)    
    plots = plots_control(tag, selection, label)    
    plots += plots_HiggsReco(tag, selection, label)

    if data:
        add_data_plots(plots=plots,data=data)

    return plots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    #baseline
    discriminatorPlots += plots_ge4j_ge3t(data)

    #analysis categories w/o forward stuff
    discriminatorPlots += plots_ge4j_3t(data)
    discriminatorPlots += plots_ge4j_ge4t(data)

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

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
