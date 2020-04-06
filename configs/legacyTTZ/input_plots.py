
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

def plots_jtr(label, selection, jtr, data = None):
    plots = [
        # z plots
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B1_CSV","btag value of first Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoZ_B1_CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B1_E","energy of first Z b-jet",30,0.,500.),"dnnZ_ft_RecoZ_B1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B1_Eta","#eta of first Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoZ_B1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B1_Pt","p_{T} of first Z b-jet",30,0.,300.),"dnnZ_ft_RecoZ_B1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B1_idx","index of first Z b-jet",8,-0.5,7.5),"dnnZ_ft_RecoZ_B1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B1_logE","log energy of first Z b-jet",30,3,7.),"dnnZ_ft_RecoZ_B1_logE",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B1_logPt","log p_{T} of first Z b-jet",30,3,7.),"dnnZ_ft_RecoZ_B1_logPt",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B2_CSV","btag value of second Z b-jet",30,0.0,1.0),"dnnZ_ft_RecoZ_B2_CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B2_E","energy of second Z b-jet",30,0.,500.),"dnnZ_ft_RecoZ_B2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B2_Eta","#eta of second Z b-jet",30,-2.4,2.4),"dnnZ_ft_RecoZ_B2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B2_Pt","p_{T} of second Z b-jet",30,0.,300.),"dnnZ_ft_RecoZ_B2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B2_idx","index of second Z b-jet",8,-0.5,7.5),"dnnZ_ft_RecoZ_B2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B2_logE","log energy of second Z b-jet",30,3.5,7.),"dnnZ_ft_RecoZ_B2_logE",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_B2_logPt","log p_{T} of second Z b-jet",30,3.5,7.),"dnnZ_ft_RecoZ_B2_logPt",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_Z_E","reconstructed Z boson energy",30,100.,1000.),"dnnZ_ft_RecoZ_Z_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_Z_Pt","Reconstructed Z boson p_{T}",30,0.,500.),"dnnZ_ft_RecoZ_Z_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_Z_Eta","reconstructed Z boson #eta",30,-3,3.),"dnnZ_ft_RecoZ_Z_Eta",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_Z_M","reconstructed Z boson mass [GeV]",25,0.,200.),"dnnZ_ft_RecoZ_Z_M",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_Z_M_dev","dev. of reconstructed Z boson mass from 90 GeV / 20 GeV",25,0.,5),"RecoZ_Z_M_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_Z_M_dev_log","log dev. of reconstructed Z boson mass from 90 GeV / 20 GeV",25,-4.,2.),"RecoZ_Z_M_dev_log",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_Z_M_weird","reconstructed Z boson mass times deviation",25,0.,300.),"RecoZ_Z_M_weird",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_Z_M_weird_log","log reconstructed Z boson mass times deviation",25,1.,7.),"RecoZ_Z_M_weird_log",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_Z_M_weird_v2","reconstructed Z boson mass times log(deviation)",25,-200,200),"RecoZ_Z_M_weird_v2",selection,label),
        
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_dEta","#Delta #eta of Z b-jets",30,0.0,2.0),"dnnZ_ft_RecoZ_Z_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_dPhi","#Delta #phi of Z b-jets",30,0.0,3.141),"dnnZ_ft_RecoZ_Z_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_dR","#DeltaR of Z b-jets",30,0.4,3.5),"dnnZ_ft_RecoZ_Z_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_dPt","#Deltap_{T} of Z b-jets",30,0.0,200.0),"dnnZ_ft_RecoZ_Z_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_dKin","#DeltaKin of Z b-jets",30,0.1,0.7),"dnnZ_ft_RecoZ_Z_dKin",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_DNNOutput","Z boson reconstruction NN output",25,0.,1.0),"dnnZ_ft_RecoZ_DNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_squaredDNNOutput","squared Z boson reconstruction NN output",25,0.,1.0),"dnnZ_ft_RecoZ_squaredDNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_transformedDNNOutput","transformed Z boson reconstruction NN output",25,-2.,4.0),"dnnZ_ft_RecoZ_transformedDNNOutput",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoZ_DNNOutput_times_M","Z boson reconstruction NN output times Z mass",25,0.,200.0),"dnnZ_ft_RecoZ_DNNOutput*dnnZ_ft_RecoZ_Z_M",selection,label),

        # higgs plots
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B1_CSV","btag value of first Higgs b-jet",30,0.0,1.0),"dnnH_ft_RecoHiggs_B1_CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B1_E","energy of first Higgs b-jet",30,0.,500.),"dnnH_ft_RecoHiggs_B1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B1_Eta","#eta of first Higgs b-jet",30,-2.4,2.4),"dnnH_ft_RecoHiggs_B1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B1_Pt","p_{T} of first Higgs b-jet",30,0.,300.),"dnnH_ft_RecoHiggs_B1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B1_idx","index of first Higgs b-jet",8,-0.5,7.5),"dnnH_ft_RecoHiggs_B1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B1_logE","log energy of first Higgs b-jet",30,3,7.),"dnnH_ft_RecoHiggs_B1_logE",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B1_logPt","log p_{T} of first Higgs b-jet",30,3,7.),"dnnH_ft_RecoHiggs_B1_logPt",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B2_CSV","btag value of second Higgs b-jet",30,0.0,1.0),"dnnH_ft_RecoHiggs_B2_CSV",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B2_E","energy of second Higgs b-jet",30,0.,500.),"dnnH_ft_RecoHiggs_B2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B2_Eta","#eta of second Higgs b-jet",30,-2.4,2.4),"dnnH_ft_RecoHiggs_B2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B2_Pt","p_{T} of second Higgs b-jet",30,0.,300.),"dnnH_ft_RecoHiggs_B2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B2_idx","index of second Higgs b-jet",8,-0.5,7.5),"dnnH_ft_RecoHiggs_B2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B2_logE","log energy of second Higgs b-jet",30,3.5,7.),"dnnH_ft_RecoHiggs_B2_logE",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_B2_logPt","log p_{T} of second Higgs b-jet",30,3.5,7.),"dnnH_ft_RecoHiggs_B2_logPt",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_H_E","reconstructed Higgs boson energy",30,100.,1000.),"dnnH_ft_RecoHiggs_H_E",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_H_Pt","Reconstructed Higgs boson p_{T}",30,0.,500.),"dnnH_ft_RecoHiggs_H_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_H_Eta","reconstructed Higgs boson #eta",30,3.5,3.5),"dnnH_ft_RecoHiggs_H_Eta",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_H_M","reconstructed Higgs boson mass [GeV]",25,50.,200.),"dnnH_ft_RecoHiggs_H_M",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_H_M_dev","dev. of reconstructed Higgs boson mass from 120 GeV / 20 GeV",25,0.,4.),"RecoHiggs_H_M_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_H_M_dev_log","log dev. of reconstructed Higgs boson mass from 120 GeV / 20 GeV",25,-4.,3.),"RecoHiggs_H_M_dev_log",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_H_M_weird","reconstructed Higgs boson mass times deviation",25,0.,300.),"RecoHiggs_H_M_weird",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_H_M_weird_log","log reconstructed Higgs boson mass times deviation",25,1.,8.),"RecoHiggs_H_M_weird_log",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_H_M_weird_v2","reconstructed Higgs boson mass times log(deviation)",25,-300,200),"RecoHiggs_H_M_weird_v2",selection,label),
        
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_dEta","#Delta #eta of Higgs b-jets",30,0.0,3.0),"dnnH_ft_RecoHiggs_H_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_dPhi","#Delta #phi of Higgs b-jets",30,0.0,3.141),"dnnH_ft_RecoHiggs_H_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_dR","#DeltaR of Higgs b-jets",30,0.0,3.5),"dnnH_ft_RecoHiggs_H_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_dPt","#Deltap_{T} of Higgs b-jets",30,0.0,200.0),"dnnH_ft_RecoHiggs_H_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_dKin","#DeltaKin of Higgs b-jets",30,0.1,0.7),"dnnH_ft_RecoHiggs_H_dKin",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_DNNOutput","Higgs boson reconstruction NN output",25,0.,1.0),"dnnH_ft_RecoHiggs_DNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_squaredDNNOutput","squared Higgs boson reconstruction NN output",25,0.,1.0),"dnnH_ft_RecoHiggs_squaredDNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnH_ft_RecoHiggs_transformedDNNOutput","transformed Higgs boson reconstruction NN output",25,-2.,4.0),"dnnH_ft_RecoHiggs_transformedDNNOutput",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_dnnZ_ft_RecoHiggs_DNNOutput_times_M","Higgs boson reconstruction NN output times Higgs mass",25,0.,200.0),"dnnH_ft_RecoHiggs_DNNOutput*dnnH_ft_RecoHiggs_H_M",selection,label),

        # ratios of dnn outputs
        plotClasses.Plot(ROOT.TH1D(jtr+"_DNNOutputRatio_H_vs_Z","reconstruction NN output ratio (H/Z)",25,0.,2.0),"dnnH_ft_RecoHiggs_DNNOutput/(dnnZ_ft_RecoZ_DNNOutput+1e-10)",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_DNNOutputRatio_Z_vs_H","reconstruction NN output ratio (Z/H)",25,0.,2.0),"dnnZ_ft_RecoZ_DNNOutput/(dnnH_ft_RecoHiggs_DNNOutput+1e-10)",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_DNNOutputDiff_Z_minus_H","reconstruction NN output difference (Z - H)",25,-0.75,0.75),"dnnZ_ft_RecoZ_DNNOutput-dnnH_ft_RecoHiggs_DNNOutput",selection,label),

        plotClasses.Plot(ROOT.TH1D(jtr+"_DNNOutputFraction_H","reconstruction NN output fraction (H)",25,0.2,0.8),
            "dnnH_ft_RecoHiggs_DNNOutput/(dnnZ_ft_RecoZ_DNNOutput+dnnH_ft_RecoHiggs_DNNOutput)",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"_DNNOutputFraction_Z","reconstruction NN output fraction (Z)",25,0.2,0.8),
            "dnnZ_ft_RecoZ_DNNOutput/(dnnZ_ft_RecoZ_DNNOutput+dnnH_ft_RecoHiggs_DNNOutput)",selection,label),
        ]


    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_ge4j_ge3t(data = None):
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&(1.)"
    jtr = "ljets_ge4j_ge3t"

    plots = plots_jtr(label, selection, jtr, data)
    return plots

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge3t(data)

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
    
