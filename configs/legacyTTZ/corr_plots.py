
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
dnnRecoZ_Z_M_corr = "dnnRecoZ_Z_M*DNNOutput_ge4j_ge3t_node_dnnRecoZ_ft_GenZ_Z_massCorrection"
dnnRecoZ_Z_M_corr_dev = "abs(("+dnnRecoZ_Z_M_corr+")-91.3)/1.7"
dnnRecoZ_Z_M_corr_dev_log = "log(("+dnnRecoZ_Z_M_corr_dev+")+1e-5)"
dnnRecoZ_Z_M_corr_weird = "("+dnnRecoZ_Z_M_corr_dev+")*("+dnnRecoZ_Z_M_corr+")"
dnnRecoZ_Z_M_corr_weird_log = "log(("+dnnRecoZ_Z_M_corr_weird+")+1e-5)"

tightselection = "&&((("+dnnRecoZ_Z_M_corr+")>=85)&&(("+dnnRecoZ_Z_M_corr+")<=95))"

def plots_ge4j_ge3t(data = None):
    label = "\geq 4 jets, \geq 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&(1.)"
    jtr = "ljets_ge4j_ge3t_"

    plots = [


        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_CSV","btag value of first Z b-jet",30,0.0,1.0),"dnnRecoZ_B1_CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_E","energy of first Z b-jet",30,0.,500.),"dnnRecoZ_B1_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_Eta","#eta of first Z b-jet",30,-2.4,2.4),"dnnRecoZ_B1_Eta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_Pt","p_{T} of first Z b-jet",30,0.,500.),"dnnRecoZ_B1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_idx","index of first Z b-jet",8,-0.5,7.5),"dnnRecoZ_B1_idx",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_logE","log energy of first Z b-jet",30,2.,7.),"dnnRecoZ_B1_logE",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_logPt","log p_{T} of first Z b-jet",30,2.,7.),"dnnRecoZ_B1_logPt",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_CSV","btag value of second Z b-jet",30,0.0,1.0),"dnnRecoZ_B2_CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_E","energy of second Z b-jet",30,0.,500.),"dnnRecoZ_B2_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_Eta","#eta of second Z b-jet",30,-2.4,2.4),"dnnRecoZ_B2_Eta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_Pt","p_{T} of second Z b-jet",30,0.,500.),"dnnRecoZ_B2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_idx","index of second Z b-jet",8,-0.5,7.5),"dnnRecoZ_B2_idx",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_logE","log energy of first Z b-jet",30,2.,7.),"dnnRecoZ_B2_logE",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_logPt","log p_{T} of first Z b-jet",30,2.,7.),"dnnRecoZ_B2_logPt",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_E","reconstructed Z boson energy",30,0.,1000.),"dnnRecoZ_Z_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_Eta","reconstructed Z boson #eta",30,-2.4,2.4),"dnnRecoZ_Z_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M","reconstructed Z boson mass [GeV]",25,0.,250.),"dnnRecoZ_Z_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_dev","dev. of reconstructed Z boson mass from 90 GeV / 20 GeV",25,0.,7.5),"dnnRecoZ_Z_M_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_dev_log","log dev. of reconstructed Z boson mass from 90 GeV / 20 GeV",25,-4.,3.),"dnnRecoZ_Z_M_dev_log",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird","reconstructed Z boson mass times deviation",25,0.,300.),"dnnRecoZ_Z_M_weird",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird_log","log reconstructed Z boson mass times deviation",25,1.,8.),"dnnRecoZ_Z_M_weird_log",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird_v2","reconstructed Z boson mass times log(deviation)",25,-200,200),"dnnRecoZ_Z_M_weird_v2",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird_tight","reconstructed Z boson mass times deviation",10,0.,50.),"dnnRecoZ_Z_M_weird",selection+"&&(dnnRecoZ_Z_M_weird<=50.)",label),
        

        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr","reconstructed Z boson mass corrected [GeV]",25,70.,100.),dnnRecoZ_Z_M_corr,selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_tight","reconstructed Z boson mass corrected [GeV]",25,85.,95.),dnnRecoZ_Z_M_corr,selection+tightselection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_dev","dev. of corr. reconstructed Z boson mass from 91.3 GeV / 1.7 GeV",25,0.,5.),dnnRecoZ_Z_M_corr_dev,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_dev_log","sq. dev. of corr. reconstructed Z boson mass from 91.3 GeV / 1.7 GeV",25,-5.,4.),dnnRecoZ_Z_M_corr_dev_log,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_weird","corr. reconstructed Z boson mass times deviation",25,0.,300.),dnnRecoZ_Z_M_corr_weird,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_weird_log","log reconstructed Z boson mass times deviation",25,0.,9.),dnnRecoZ_Z_M_corr_weird_log,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_Pt","Reconstructed Z boson p_{T}",30,0.,500.),"dnnRecoZ_Z_Pt",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dEta","#Delta #eta of Z b-jets",30,0.0,4.0),"dnnRecoZ_dEta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dPhi","#Delta #phi of Z b-jets",30,0.0,3.141),"dnnRecoZ_dPhi",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dR","#DeltaR of Z b-jets",30,0.0,4.0),"dnnRecoZ_dR",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dPt","#Deltap_{T} of Z b-jets",30,0.0,200.0),"dnnRecoZ_dPt",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dKin","#DeltaKin of Z b-jets",30,0.0,1.0),"dnnRecoZ_dKin",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_DNNOutput","Z boson reconstruction DNN output",25,0.,1.0),"dnnRecoZ_DNNOutput",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_squaredDNNOutput","squared Z boson reconstruction DNN output",25,0.,1.0),"dnnRecoZ_squaredDNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_transformedDNNOutput","transformed Z boson reconstruction DNN output",25,-4.,6.0),"dnnRecoZ_transformedDNNOutput",selection,label),

        #plotClasses.TwoDimPlot(
        #    ROOT.TH2F("crosscheck_N_Jets","number of jets (orig tree vs friend tree)",6,3.5,9.5,6,3.5,9.5),
        #    "N_Jets","dnnRecoZ.N_Jets",selection,label),

        ]


    if data:
        add_data_plots(plots=plots,data=data)
    return plots

def plots_ge6j_ge3t(data = None):
    label = "\geq 6 jets, \geq 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=6&&N_BTagsM>=3)&&(1.)"

    jtr = "ljets_ge6j_ge3t_"

    plots = [
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_CSV","btag value of first Z b-jet",30,0.0,1.0),"dnnRecoZ_B1_CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_E","energy of first Z b-jet",30,0.,500.),"dnnRecoZ_B1_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_Eta","#eta of first Z b-jet",30,-2.4,2.4),"dnnRecoZ_B1_Eta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_Pt","p_{T} of first Z b-jet",30,0.,500.),"dnnRecoZ_B1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_idx","index of first Z b-jet",8,-0.5,7.5),"dnnRecoZ_B1_idx",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_logE","log energy of first Z b-jet",30,2.,7.),"dnnRecoZ_B1_logE",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_logPt","log p_{T} of first Z b-jet",30,2.,7.),"dnnRecoZ_B1_logPt",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_CSV","btag value of second Z b-jet",30,0.0,1.0),"dnnRecoZ_B2_CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_E","energy of second Z b-jet",30,0.,500.),"dnnRecoZ_B2_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_Eta","#eta of second Z b-jet",30,-2.4,2.4),"dnnRecoZ_B2_Eta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_Pt","p_{T} of second Z b-jet",30,0.,500.),"dnnRecoZ_B2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_idx","index of second Z b-jet",8,-0.5,7.5),"dnnRecoZ_B2_idx",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_logE","log energy of first Z b-jet",30,2.,7.),"dnnRecoZ_B2_logE",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_logPt","log p_{T} of first Z b-jet",30,2.,7.),"dnnRecoZ_B2_logPt",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_E","reconstructed Z boson energy",30,0.,1000.),"dnnRecoZ_Z_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_Eta","reconstructed Z boson #eta",30,-2.4,2.4),"dnnRecoZ_Z_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M","reconstructed Z boson mass [GeV]",25,0.,250.),"dnnRecoZ_Z_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_dev","dev. of reconstructed Z boson mass from 90 GeV / 20 GeV",25,0.,7.5),"dnnRecoZ_Z_M_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_dev_log","log dev. of reconstructed Z boson mass from 90 GeV / 20 GeV",25,-4.,3.),"dnnRecoZ_Z_M_dev_log",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird","reconstructed Z boson mass times deviation",25,0.,300.),"dnnRecoZ_Z_M_weird",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird_log","log reconstructed Z boson mass times deviation",25,1.,8.),"dnnRecoZ_Z_M_weird_log",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird_v2","reconstructed Z boson mass times log(deviation)",25,-200,200),"dnnRecoZ_Z_M_weird_v2",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird_tight","reconstructed Z boson mass times deviation",10,0.,50.),"dnnRecoZ_Z_M_weird",selection+"&&(dnnRecoZ_Z_M_weird<=50.)",label),
        

        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr","reconstructed Z boson mass corrected [GeV]",25,70.,100.),dnnRecoZ_Z_M_corr,selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_tight","reconstructed Z boson mass corrected [GeV]",25,85.,95.),dnnRecoZ_Z_M_corr,selection+tightselection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_dev","dev. of corr. reconstructed Z boson mass from 91.3 GeV / 1.7 GeV",25,0.,5.),dnnRecoZ_Z_M_corr_dev,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_dev_log","sq. dev. of corr. reconstructed Z boson mass from 91.3 GeV / 1.7 GeV",25,-5.,4.),dnnRecoZ_Z_M_corr_dev_log,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_weird","corr. reconstructed Z boson mass times deviation",25,0.,300.),dnnRecoZ_Z_M_corr_weird,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_weird_log","log reconstructed Z boson mass times deviation",25,0.,9.),dnnRecoZ_Z_M_corr_weird_log,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_Pt","Reconstructed Z boson p_{T}",30,0.,500.),"dnnRecoZ_Z_Pt",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dEta","#Delta #eta of Z b-jets",30,0.0,4.0),"dnnRecoZ_dEta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dPhi","#Delta #phi of Z b-jets",30,0.0,3.141),"dnnRecoZ_dPhi",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dR","#DeltaR of Z b-jets",30,0.0,4.0),"dnnRecoZ_dR",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dPt","#Deltap_{T} of Z b-jets",30,0.0,200.0),"dnnRecoZ_dPt",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dKin","#DeltaKin of Z b-jets",30,0.0,1.0),"dnnRecoZ_dKin",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_DNNOutput","Z boson reconstruction DNN output",25,0.,1.0),"dnnRecoZ_DNNOutput",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_squaredDNNOutput","squared Z boson reconstruction DNN output",25,0.,1.0),"dnnRecoZ_squaredDNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_transformedDNNOutput","transformed Z boson reconstruction DNN output",25,-4.,6.0),"dnnRecoZ_transformedDNNOutput",selection,label),

        ]


    if data:
        add_data_plots(plots=plots,data=data)
    return plots

def plots_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    jtr = "ljets_ge4j_ge4t_"

    plots = [
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_CSV","btag value of first Z b-jet",30,0.0,1.0),"dnnRecoZ_B1_CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_E","energy of first Z b-jet",30,0.,500.),"dnnRecoZ_B1_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_Eta","#eta of first Z b-jet",30,-2.4,2.4),"dnnRecoZ_B1_Eta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_Pt","p_{T} of first Z b-jet",30,0.,500.),"dnnRecoZ_B1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_idx","index of first Z b-jet",8,-0.5,7.5),"dnnRecoZ_B1_idx",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_logE","log energy of first Z b-jet",30,2.,7.),"dnnRecoZ_B1_logE",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B1_logPt","log p_{T} of first Z b-jet",30,2.,7.),"dnnRecoZ_B1_logPt",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_CSV","btag value of second Z b-jet",30,0.0,1.0),"dnnRecoZ_B2_CSV",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_E","energy of second Z b-jet",30,0.,500.),"dnnRecoZ_B2_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_Eta","#eta of second Z b-jet",30,-2.4,2.4),"dnnRecoZ_B2_Eta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_Pt","p_{T} of second Z b-jet",30,0.,500.),"dnnRecoZ_B2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_idx","index of second Z b-jet",8,-0.5,7.5),"dnnRecoZ_B2_idx",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_logE","log energy of first Z b-jet",30,2.,7.),"dnnRecoZ_B2_logE",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_B2_logPt","log p_{T} of first Z b-jet",30,2.,7.),"dnnRecoZ_B2_logPt",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_E","reconstructed Z boson energy",30,0.,1000.),"dnnRecoZ_Z_E",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_Eta","reconstructed Z boson #eta",30,-2.4,2.4),"dnnRecoZ_Z_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M","reconstructed Z boson mass [GeV]",25,0.,250.),"dnnRecoZ_Z_M",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_dev","dev. of reconstructed Z boson mass from 90 GeV / 20 GeV",25,0.,7.5),"dnnRecoZ_Z_M_dev",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_dev_log","log dev. of reconstructed Z boson mass from 90 GeV / 20 GeV",25,-4.,3.),"dnnRecoZ_Z_M_dev_log",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird","reconstructed Z boson mass times deviation",25,0.,300.),"dnnRecoZ_Z_M_weird",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird_log","log reconstructed Z boson mass times deviation",25,1.,8.),"dnnRecoZ_Z_M_weird_log",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird_v2","reconstructed Z boson mass times log(deviation)",25,-200,200),"dnnRecoZ_Z_M_weird_v2",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_weird_tight","reconstructed Z boson mass times deviation",10,0.,50.),"dnnRecoZ_Z_M_weird",selection+"&&(dnnRecoZ_Z_M_weird<=50.)",label),
        

        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr","reconstructed Z boson mass corrected [GeV]",25,70.,100.),dnnRecoZ_Z_M_corr,selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_tight","reconstructed Z boson mass corrected [GeV]",25,85.,95.),dnnRecoZ_Z_M_corr,selection+tightselection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_dev","dev. of corr. reconstructed Z boson mass from 91.3 GeV / 1.7 GeV",25,0.,5.),dnnRecoZ_Z_M_corr_dev,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_dev_log","sq. dev. of corr. reconstructed Z boson mass from 91.3 GeV / 1.7 GeV",25,-5.,4.),dnnRecoZ_Z_M_corr_dev_log,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_weird","corr. reconstructed Z boson mass times deviation",25,0.,300.),dnnRecoZ_Z_M_corr_weird,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_M_corr_weird_log","log reconstructed Z boson mass times deviation",25,0.,9.),dnnRecoZ_Z_M_corr_weird_log,selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_Z_Pt","Reconstructed Z boson p_{T}",30,0.,500.),"dnnRecoZ_Z_Pt",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dEta","#Delta #eta of Z b-jets",30,0.0,4.0),"dnnRecoZ_dEta",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dPhi","#Delta #phi of Z b-jets",30,0.0,3.141),"dnnRecoZ_dPhi",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dR","#DeltaR of Z b-jets",30,0.0,4.0),"dnnRecoZ_dR",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dPt","#Deltap_{T} of Z b-jets",30,0.0,200.0),"dnnRecoZ_dPt",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_dKin","#DeltaKin of Z b-jets",30,0.0,1.0),"dnnRecoZ_dKin",selection,label),

        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_DNNOutput","Z boson reconstruction DNN output",25,0.,1.0),"dnnRecoZ_DNNOutput",selection,label),
        #plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_squaredDNNOutput","squared Z boson reconstruction DNN output",25,0.,1.0),"dnnRecoZ_squaredDNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D(jtr+"dnnRecoZ_transformedDNNOutput","transformed Z boson reconstruction DNN output",25,-4.,6.0),"dnnRecoZ_transformedDNNOutput",selection,label),

        ]


    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def plots_dnn(data, discrname):

    ndefaultbins = 30
    interfaces = []


    # plots for ge4j_ge3t

    interf_ljets_ge4j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_dnnRecoZ_ft_GenZ_Z_massCorrection",
                                            label          = "zMassCorrectionFactor_ge4j_ge3t",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==0))")
    interf_ljets_ge4j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.category = ("((N_Jets>=4&&N_BTagsM>=3)&&(1.))","zMassCorrectionFactor","")
    interf_ljets_ge4j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.category_label = "\geq 4 jets, \geq 3 b-tags"
    interf_ljets_ge4j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.minxval = 0.0
    interf_ljets_ge4j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.maxxval = 2.3
    interf_ljets_ge4j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node)

    interf_ljets_ge4j_ge4t_dnnRecoZ_ft_GenZ_Z_massCorrection_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_dnnRecoZ_ft_GenZ_Z_massCorrection",
                                            label          = "zMassCorrectionFactor_ge4j_ge4t",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==0))")
    interf_ljets_ge4j_ge4t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.))","zMassCorrectionFactor","")
    interf_ljets_ge4j_ge4t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.category_label = "\geq 4 jets, \geq 4 b-tags"
    interf_ljets_ge4j_ge4t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.minxval = 0.0
    interf_ljets_ge4j_ge4t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.maxxval = 2.3
    interf_ljets_ge4j_ge4t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_dnnRecoZ_ft_GenZ_Z_massCorrection_node)

    interf_ljets_ge6j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge3t_node_dnnRecoZ_ft_GenZ_Z_massCorrection",
                                            label          = "zMassCorrectionFactor_ge6j_ge3t",
                                            selection      = "((N_Jets>=6&&N_BTagsM>=3)&&(1.)&&(DNNPredictedClass_ge4j_ge3t==0))")
    interf_ljets_ge6j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.category = ("((N_Jets>=6&&N_BTagsM>=3)&&(1.))","zMassCorrectionFactor","")
    interf_ljets_ge6j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.category_label = "\geq 6 jets, \geq 3 b-tags"
    interf_ljets_ge6j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.minxval = 0.0
    interf_ljets_ge6j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.maxxval = 2.3
    interf_ljets_ge6j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge6j_ge3t_dnnRecoZ_ft_GenZ_Z_massCorrection_node)


    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_dnn(data, discrname)
    discriminatorPlots += plots_ge4j_ge3t(data)
    discriminatorPlots += plots_ge6j_ge3t(data)
    discriminatorPlots += plots_ge4j_ge4t(data)

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
    
