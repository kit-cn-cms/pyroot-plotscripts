
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



def plots_le5j_le3t_30GeV(data = None):
    label = "\leq 5 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le3t_60GeV(data = None):
    label = "\leq 5 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le3t_90GeV(data = None):
    label = "\leq 5 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le3t_30GeV_ttZZ(data = None):
    label = "\leq 5 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_30GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le3t_60GeV_ttZZ(data = None):
    label = "\leq 5 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_60GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le3t_90GeV_ttZZ(data = None):
    label = "\leq 5 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le3t_90GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le3t_30GeV(data = None):
    label = "\leq 7 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le3t_60GeV(data = None):
    label = "\leq 7 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le3t_90GeV(data = None):
    label = "\leq 7 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le3t_30GeV_ttZZ(data = None):
    label = "\leq 7 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_30GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le3t_60GeV_ttZZ(data = None):
    label = "\leq 7 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_60GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le3t_90GeV_ttZZ(data = None):
    label = "\leq 7 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le3t_90GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le4t_30GeV(data = None):
    label = "\leq 7 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le4t_60GeV(data = None):
    label = "\leq 7 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le4t_90GeV(data = None):
    label = "\leq 7 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le4t_30GeV_ttZZ(data = None):
    label = "\leq 7 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_30GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le4t_60GeV_ttZZ(data = None):
    label = "\leq 7 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_60GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le7j_le4t_90GeV_ttZZ(data = None):
    label = "\leq 7 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le7j_le4t_90GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le4t_30GeV(data = None):
    label = "\leq 5 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le4t_60GeV(data = None):
    label = "\leq 5 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le4t_90GeV(data = None):
    label = "\leq 5 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le4t_30GeV_ttZZ(data = None):
    label = "\leq 5 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_30GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le4t_60GeV_ttZZ(data = None):
    label = "\leq 5 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_60GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le5j_le4t_90GeV_ttZZ(data = None):
    label = "\leq 5 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le5j_le4t_90GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le4t_30GeV(data = None):
    label = "\leq 6 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le4t_60GeV(data = None):
    label = "\leq 6 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le4t_90GeV(data = None):
    label = "\leq 6 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le4t_30GeV_ttZZ(data = None):
    label = "\leq 6 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_30GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le4t_60GeV_ttZZ(data = None):
    label = "\leq 6 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_60GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le4t_90GeV_ttZZ(data = None):
    label = "\leq 6 jets, \leq 4 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le4t_90GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le3t_30GeV(data = None):
    label = "\leq 6 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le3t_60GeV(data = None):
    label = "\leq 6 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le3t_90GeV(data = None):
    label = "\leq 6 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le3t_30GeV_ttZZ(data = None):
    label = "\leq 6 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_30GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le3t_60GeV_ttZZ(data = None):
    label = "\leq 6 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_60GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_le6j_le3t_90GeV_ttZZ(data = None):
    label = "\leq 6 jets, \leq 3 b-tags"
    interfaces = []
    selection = "(Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Evt_CSV_avg","x",50,0.0,1.0),"Evt_CSV_avg",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Evt_Deta_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Evt_Pt_JetsAverage","x",50,-100.0,100.0),"Evt_Pt_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Evt_Pt_TaggedJetsAverage","x",50,-100.0,100.0),"Evt_Pt_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Evt_Pt_minDrTaggedJets","x",50,-100.0,100.0),"Evt_Pt_minDrTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_CSV_0","Jet CSV[0]",50,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_CSV_1","Jet CSV[1]",50,0.0,1.0),"Jet_CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_CSV_2","Jet CSV[2]",50,0.0,1.0),"Jet_CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_CSV_3","Jet CSV[3]",50,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Eta_0","Jet Eta[0]",50,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Eta_1","Jet Eta[1]",50,-2.4,2.4),"Jet_Eta[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Eta_2","Jet Eta[2]",50,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Eta_3","Jet Eta[3]",50,-2.4,2.4),"Jet_Eta[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_M_0","Jet M[0]",50,0.0,60.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_M_1","Jet M[1]",50,0.0,60.0),"Jet_M[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_M_2","Jet M[2]",50,0.0,60.0),"Jet_M[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_M_3","Jet M[3]",50,0.0,60.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Phi_0","Jet Phi[0]",50,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Phi_1","Jet Phi[1]",50,-3.14159265359,3.14159265359),"Jet_Phi[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Phi_2","Jet Phi[2]",50,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Phi_3","Jet Phi[3]",50,-3.14159265359,3.14159265359),"Jet_Phi[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Pt_0","Jet Pt[0]",50,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Pt_1","Jet Pt[1]",50,0.0,600.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Pt_2","Jet Pt[2]",50,0.0,600.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_Jet_Pt_3","Jet Pt[3]",50,0.0,600.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_le6j_le3t_90GeV_ttZZ_N_Jets","N (Jets)",6,5.5,11.5),"N_Jets",selection,label),
        ]

        
    if data:
        add_data_plots(plots=plots,data=data)
    return plots
    

def plots_dnn(data, discrname):

    ndefaultbins = 15
    interfaces = []


    # plots for le5j_le3t_30GeV

    interf_ljets_le5j_le3t_30GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_node_ttH",
                                            label          = "ljets_le5j_le3t_30GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==0))")
    interf_ljets_le5j_le3t_30GeV_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==0))","ljets_le5j_le3t_30GeV_ttH_node","")
    interf_ljets_le5j_le3t_30GeV_ttH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttH_node.minxval = 0.17
    interf_ljets_le5j_le3t_30GeV_ttH_node.maxxval = 0.38
    interf_ljets_le5j_le3t_30GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttH_node)
    
    interf_ljets_le5j_le3t_30GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_node_ttbb",
                                            label          = "ljets_le5j_le3t_30GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==1))")
    interf_ljets_le5j_le3t_30GeV_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==1))","ljets_le5j_le3t_30GeV_ttbb_node","")
    interf_ljets_le5j_le3t_30GeV_ttbb_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttbb_node.minxval = 0.17
    interf_ljets_le5j_le3t_30GeV_ttbb_node.maxxval = 0.43
    interf_ljets_le5j_le3t_30GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttbb_node)
    
    interf_ljets_le5j_le3t_30GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_node_ttcc",
                                            label          = "ljets_le5j_le3t_30GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==2))")
    interf_ljets_le5j_le3t_30GeV_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==2))","ljets_le5j_le3t_30GeV_ttcc_node","")
    interf_ljets_le5j_le3t_30GeV_ttcc_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttcc_node.minxval = 0.17
    interf_ljets_le5j_le3t_30GeV_ttcc_node.maxxval = 0.42
    interf_ljets_le5j_le3t_30GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttcc_node)
    
    interf_ljets_le5j_le3t_30GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_node_ttlf",
                                            label          = "ljets_le5j_le3t_30GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==3))")
    interf_ljets_le5j_le3t_30GeV_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==3))","ljets_le5j_le3t_30GeV_ttlf_node","")
    interf_ljets_le5j_le3t_30GeV_ttlf_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttlf_node.minxval = 0.17
    interf_ljets_le5j_le3t_30GeV_ttlf_node.maxxval = 0.51
    interf_ljets_le5j_le3t_30GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttlf_node)
    
    interf_ljets_le5j_le3t_30GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_node_ttHH",
                                            label          = "ljets_le5j_le3t_30GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==4))")
    interf_ljets_le5j_le3t_30GeV_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==4))","ljets_le5j_le3t_30GeV_ttHH_node","")
    interf_ljets_le5j_le3t_30GeV_ttHH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttHH_node.minxval = 0.17
    interf_ljets_le5j_le3t_30GeV_ttHH_node.maxxval = 0.59
    interf_ljets_le5j_le3t_30GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttHH_node)
    
    interf_ljets_le5j_le3t_30GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_node_tt4b",
                                            label          = "ljets_le5j_le3t_30GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==5))")
    interf_ljets_le5j_le3t_30GeV_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV==5))","ljets_le5j_le3t_30GeV_tt4b_node","")
    interf_ljets_le5j_le3t_30GeV_tt4b_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_tt4b_node.minxval = 0.17
    interf_ljets_le5j_le3t_30GeV_tt4b_node.maxxval = 0.56
    interf_ljets_le5j_le3t_30GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_tt4b_node)
    


    # plots for le5j_le3t_60GeV

    interf_ljets_le5j_le3t_60GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_node_ttH",
                                            label          = "ljets_le5j_le3t_60GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==0))")
    interf_ljets_le5j_le3t_60GeV_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==0))","ljets_le5j_le3t_60GeV_ttH_node","")
    interf_ljets_le5j_le3t_60GeV_ttH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttH_node.minxval = 0.17
    interf_ljets_le5j_le3t_60GeV_ttH_node.maxxval = 0.36
    interf_ljets_le5j_le3t_60GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttH_node)
    
    interf_ljets_le5j_le3t_60GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_node_ttbb",
                                            label          = "ljets_le5j_le3t_60GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==1))")
    interf_ljets_le5j_le3t_60GeV_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==1))","ljets_le5j_le3t_60GeV_ttbb_node","")
    interf_ljets_le5j_le3t_60GeV_ttbb_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttbb_node.minxval = 0.17
    interf_ljets_le5j_le3t_60GeV_ttbb_node.maxxval = 0.4
    interf_ljets_le5j_le3t_60GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttbb_node)
    
    interf_ljets_le5j_le3t_60GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_node_ttcc",
                                            label          = "ljets_le5j_le3t_60GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==2))")
    interf_ljets_le5j_le3t_60GeV_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==2))","ljets_le5j_le3t_60GeV_ttcc_node","")
    interf_ljets_le5j_le3t_60GeV_ttcc_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttcc_node.minxval = 0.17
    interf_ljets_le5j_le3t_60GeV_ttcc_node.maxxval = 0.62
    interf_ljets_le5j_le3t_60GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttcc_node)
    
    interf_ljets_le5j_le3t_60GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_node_ttlf",
                                            label          = "ljets_le5j_le3t_60GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==3))")
    interf_ljets_le5j_le3t_60GeV_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==3))","ljets_le5j_le3t_60GeV_ttlf_node","")
    interf_ljets_le5j_le3t_60GeV_ttlf_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttlf_node.minxval = 0.17
    interf_ljets_le5j_le3t_60GeV_ttlf_node.maxxval = 0.44
    interf_ljets_le5j_le3t_60GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttlf_node)
    
    interf_ljets_le5j_le3t_60GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_node_ttHH",
                                            label          = "ljets_le5j_le3t_60GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==4))")
    interf_ljets_le5j_le3t_60GeV_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==4))","ljets_le5j_le3t_60GeV_ttHH_node","")
    interf_ljets_le5j_le3t_60GeV_ttHH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttHH_node.minxval = 0.17
    interf_ljets_le5j_le3t_60GeV_ttHH_node.maxxval = 0.56
    interf_ljets_le5j_le3t_60GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttHH_node)
    
    interf_ljets_le5j_le3t_60GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_node_tt4b",
                                            label          = "ljets_le5j_le3t_60GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==5))")
    interf_ljets_le5j_le3t_60GeV_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV==5))","ljets_le5j_le3t_60GeV_tt4b_node","")
    interf_ljets_le5j_le3t_60GeV_tt4b_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_tt4b_node.minxval = 0.17
    interf_ljets_le5j_le3t_60GeV_tt4b_node.maxxval = 0.5
    interf_ljets_le5j_le3t_60GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_tt4b_node)
    


    # plots for le5j_le3t_90GeV

    interf_ljets_le5j_le3t_90GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_node_ttH",
                                            label          = "ljets_le5j_le3t_90GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==0))")
    interf_ljets_le5j_le3t_90GeV_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==0))","ljets_le5j_le3t_90GeV_ttH_node","")
    interf_ljets_le5j_le3t_90GeV_ttH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttH_node.minxval = 0.17
    interf_ljets_le5j_le3t_90GeV_ttH_node.maxxval = 0.36
    interf_ljets_le5j_le3t_90GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttH_node)
    
    interf_ljets_le5j_le3t_90GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_node_ttbb",
                                            label          = "ljets_le5j_le3t_90GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==1))")
    interf_ljets_le5j_le3t_90GeV_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==1))","ljets_le5j_le3t_90GeV_ttbb_node","")
    interf_ljets_le5j_le3t_90GeV_ttbb_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttbb_node.minxval = 0.17
    interf_ljets_le5j_le3t_90GeV_ttbb_node.maxxval = 0.4
    interf_ljets_le5j_le3t_90GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttbb_node)
    
    interf_ljets_le5j_le3t_90GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_node_ttcc",
                                            label          = "ljets_le5j_le3t_90GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==2))")
    interf_ljets_le5j_le3t_90GeV_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==2))","ljets_le5j_le3t_90GeV_ttcc_node","")
    interf_ljets_le5j_le3t_90GeV_ttcc_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttcc_node.minxval = 0.17
    interf_ljets_le5j_le3t_90GeV_ttcc_node.maxxval = 0.53
    interf_ljets_le5j_le3t_90GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttcc_node)
    
    interf_ljets_le5j_le3t_90GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_node_ttlf",
                                            label          = "ljets_le5j_le3t_90GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==3))")
    interf_ljets_le5j_le3t_90GeV_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==3))","ljets_le5j_le3t_90GeV_ttlf_node","")
    interf_ljets_le5j_le3t_90GeV_ttlf_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttlf_node.minxval = 0.17
    interf_ljets_le5j_le3t_90GeV_ttlf_node.maxxval = 0.48
    interf_ljets_le5j_le3t_90GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttlf_node)
    
    interf_ljets_le5j_le3t_90GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_node_ttHH",
                                            label          = "ljets_le5j_le3t_90GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==4))")
    interf_ljets_le5j_le3t_90GeV_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==4))","ljets_le5j_le3t_90GeV_ttHH_node","")
    interf_ljets_le5j_le3t_90GeV_ttHH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttHH_node.minxval = 0.17
    interf_ljets_le5j_le3t_90GeV_ttHH_node.maxxval = 0.48
    interf_ljets_le5j_le3t_90GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttHH_node)
    
    interf_ljets_le5j_le3t_90GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_node_tt4b",
                                            label          = "ljets_le5j_le3t_90GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==5))")
    interf_ljets_le5j_le3t_90GeV_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV==5))","ljets_le5j_le3t_90GeV_tt4b_node","")
    interf_ljets_le5j_le3t_90GeV_tt4b_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_tt4b_node.minxval = 0.17
    interf_ljets_le5j_le3t_90GeV_tt4b_node.maxxval = 0.46
    interf_ljets_le5j_le3t_90GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_tt4b_node)
    


    # plots for le5j_le3t_30GeV_ttZZ

    interf_ljets_le5j_le3t_30GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_ttZZ_node_ttH",
                                            label          = "ljets_le5j_le3t_30GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==0))")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==0))","ljets_le5j_le3t_30GeV_ttZZ_ttH_node","")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttH_node.maxxval = 0.29
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttZZ_ttH_node)
    
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le5j_le3t_30GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==1))")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==1))","ljets_le5j_le3t_30GeV_ttZZ_ttbb_node","")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttbb_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttbb_node.maxxval = 0.39
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttZZ_ttbb_node)
    
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le5j_le3t_30GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==2))")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==2))","ljets_le5j_le3t_30GeV_ttZZ_ttcc_node","")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttcc_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttcc_node.maxxval = 0.41
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttZZ_ttcc_node)
    
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le5j_le3t_30GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==3))")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==3))","ljets_le5j_le3t_30GeV_ttZZ_ttlf_node","")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttlf_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttlf_node.maxxval = 0.5
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttZZ_ttlf_node)
    
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le5j_le3t_30GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==4))")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==4))","ljets_le5j_le3t_30GeV_ttZZ_ttHH_node","")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttHH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttHH_node.maxxval = 0.4
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttZZ_ttHH_node)
    
    interf_ljets_le5j_le3t_30GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le5j_le3t_30GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==5))")
    interf_ljets_le5j_le3t_30GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==5))","ljets_le5j_le3t_30GeV_ttZZ_tt4b_node","")
    interf_ljets_le5j_le3t_30GeV_ttZZ_tt4b_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le5j_le3t_30GeV_ttZZ_tt4b_node.maxxval = 0.46
    interf_ljets_le5j_le3t_30GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttZZ_tt4b_node)
    
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_30GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le5j_le3t_30GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==6))")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_30GeV_ttZZ==6))","ljets_le5j_le3t_30GeV_ttZZ_ttzz_node","")
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttzz_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttzz_node.maxxval = 0.52
    interf_ljets_le5j_le3t_30GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_30GeV_ttZZ_ttzz_node)
    


    # plots for le5j_le3t_60GeV_ttZZ

    interf_ljets_le5j_le3t_60GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_ttZZ_node_ttH",
                                            label          = "ljets_le5j_le3t_60GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==0))")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==0))","ljets_le5j_le3t_60GeV_ttZZ_ttH_node","")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttH_node.maxxval = 0.29
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttZZ_ttH_node)
    
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le5j_le3t_60GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==1))")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==1))","ljets_le5j_le3t_60GeV_ttZZ_ttbb_node","")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttbb_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttbb_node.maxxval = 0.39
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttZZ_ttbb_node)
    
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le5j_le3t_60GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==2))")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==2))","ljets_le5j_le3t_60GeV_ttZZ_ttcc_node","")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttcc_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttcc_node.maxxval = 0.47
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttZZ_ttcc_node)
    
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le5j_le3t_60GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==3))")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==3))","ljets_le5j_le3t_60GeV_ttZZ_ttlf_node","")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttlf_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttlf_node.maxxval = 0.47
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttZZ_ttlf_node)
    
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le5j_le3t_60GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==4))")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==4))","ljets_le5j_le3t_60GeV_ttZZ_ttHH_node","")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttHH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttHH_node.maxxval = 0.38
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttZZ_ttHH_node)
    
    interf_ljets_le5j_le3t_60GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le5j_le3t_60GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==5))")
    interf_ljets_le5j_le3t_60GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==5))","ljets_le5j_le3t_60GeV_ttZZ_tt4b_node","")
    interf_ljets_le5j_le3t_60GeV_ttZZ_tt4b_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le5j_le3t_60GeV_ttZZ_tt4b_node.maxxval = 0.42
    interf_ljets_le5j_le3t_60GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttZZ_tt4b_node)
    
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_60GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le5j_le3t_60GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==6))")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_60GeV_ttZZ==6))","ljets_le5j_le3t_60GeV_ttZZ_ttzz_node","")
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttzz_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttzz_node.maxxval = 0.37
    interf_ljets_le5j_le3t_60GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_60GeV_ttZZ_ttzz_node)
    


    # plots for le5j_le3t_90GeV_ttZZ

    interf_ljets_le5j_le3t_90GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_ttZZ_node_ttH",
                                            label          = "ljets_le5j_le3t_90GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==0))")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==0))","ljets_le5j_le3t_90GeV_ttZZ_ttH_node","")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttH_node.maxxval = 0.28
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttZZ_ttH_node)
    
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le5j_le3t_90GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==1))")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==1))","ljets_le5j_le3t_90GeV_ttZZ_ttbb_node","")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttbb_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttbb_node.maxxval = 0.33
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttZZ_ttbb_node)
    
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le5j_le3t_90GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==2))")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==2))","ljets_le5j_le3t_90GeV_ttZZ_ttcc_node","")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttcc_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttcc_node.maxxval = 0.46
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttZZ_ttcc_node)
    
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le5j_le3t_90GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==3))")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==3))","ljets_le5j_le3t_90GeV_ttZZ_ttlf_node","")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttlf_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttlf_node.maxxval = 0.46
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttZZ_ttlf_node)
    
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le5j_le3t_90GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==4))")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==4))","ljets_le5j_le3t_90GeV_ttZZ_ttHH_node","")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttHH_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttHH_node.maxxval = 0.34
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttZZ_ttHH_node)
    
    interf_ljets_le5j_le3t_90GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le5j_le3t_90GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==5))")
    interf_ljets_le5j_le3t_90GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==5))","ljets_le5j_le3t_90GeV_ttZZ_tt4b_node","")
    interf_ljets_le5j_le3t_90GeV_ttZZ_tt4b_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le5j_le3t_90GeV_ttZZ_tt4b_node.maxxval = 0.39
    interf_ljets_le5j_le3t_90GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttZZ_tt4b_node)
    
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le3t_90GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le5j_le3t_90GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==6))")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le5j_le3t_90GeV_ttZZ==6))","ljets_le5j_le3t_90GeV_ttZZ_ttzz_node","")
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttzz_node.category_label = "\leq 5 jets, \leq 3 b-tags"
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttzz_node.maxxval = 0.35
    interf_ljets_le5j_le3t_90GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le3t_90GeV_ttZZ_ttzz_node)
    


    # plots for le7j_le3t_30GeV

    interf_ljets_le7j_le3t_30GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_node_ttH",
                                            label          = "ljets_le7j_le3t_30GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==0))")
    interf_ljets_le7j_le3t_30GeV_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==0))","ljets_le7j_le3t_30GeV_ttH_node","")
    interf_ljets_le7j_le3t_30GeV_ttH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttH_node.minxval = 0.17
    interf_ljets_le7j_le3t_30GeV_ttH_node.maxxval = 0.41
    interf_ljets_le7j_le3t_30GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttH_node)
    
    interf_ljets_le7j_le3t_30GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_node_ttbb",
                                            label          = "ljets_le7j_le3t_30GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==1))")
    interf_ljets_le7j_le3t_30GeV_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==1))","ljets_le7j_le3t_30GeV_ttbb_node","")
    interf_ljets_le7j_le3t_30GeV_ttbb_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttbb_node.minxval = 0.17
    interf_ljets_le7j_le3t_30GeV_ttbb_node.maxxval = 0.41
    interf_ljets_le7j_le3t_30GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttbb_node)
    
    interf_ljets_le7j_le3t_30GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_node_ttcc",
                                            label          = "ljets_le7j_le3t_30GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==2))")
    interf_ljets_le7j_le3t_30GeV_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==2))","ljets_le7j_le3t_30GeV_ttcc_node","")
    interf_ljets_le7j_le3t_30GeV_ttcc_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttcc_node.minxval = 0.17
    interf_ljets_le7j_le3t_30GeV_ttcc_node.maxxval = 0.43
    interf_ljets_le7j_le3t_30GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttcc_node)
    
    interf_ljets_le7j_le3t_30GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_node_ttlf",
                                            label          = "ljets_le7j_le3t_30GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==3))")
    interf_ljets_le7j_le3t_30GeV_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==3))","ljets_le7j_le3t_30GeV_ttlf_node","")
    interf_ljets_le7j_le3t_30GeV_ttlf_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttlf_node.minxval = 0.17
    interf_ljets_le7j_le3t_30GeV_ttlf_node.maxxval = 0.53
    interf_ljets_le7j_le3t_30GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttlf_node)
    
    interf_ljets_le7j_le3t_30GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_node_ttHH",
                                            label          = "ljets_le7j_le3t_30GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==4))")
    interf_ljets_le7j_le3t_30GeV_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==4))","ljets_le7j_le3t_30GeV_ttHH_node","")
    interf_ljets_le7j_le3t_30GeV_ttHH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttHH_node.minxval = 0.17
    interf_ljets_le7j_le3t_30GeV_ttHH_node.maxxval = 0.59
    interf_ljets_le7j_le3t_30GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttHH_node)
    
    interf_ljets_le7j_le3t_30GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_node_tt4b",
                                            label          = "ljets_le7j_le3t_30GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==5))")
    interf_ljets_le7j_le3t_30GeV_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV==5))","ljets_le7j_le3t_30GeV_tt4b_node","")
    interf_ljets_le7j_le3t_30GeV_tt4b_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_tt4b_node.minxval = 0.17
    interf_ljets_le7j_le3t_30GeV_tt4b_node.maxxval = 0.54
    interf_ljets_le7j_le3t_30GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_tt4b_node)
    


    # plots for le7j_le3t_60GeV

    interf_ljets_le7j_le3t_60GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_node_ttH",
                                            label          = "ljets_le7j_le3t_60GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==0))")
    interf_ljets_le7j_le3t_60GeV_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==0))","ljets_le7j_le3t_60GeV_ttH_node","")
    interf_ljets_le7j_le3t_60GeV_ttH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttH_node.minxval = 0.17
    interf_ljets_le7j_le3t_60GeV_ttH_node.maxxval = 0.41
    interf_ljets_le7j_le3t_60GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttH_node)
    
    interf_ljets_le7j_le3t_60GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_node_ttbb",
                                            label          = "ljets_le7j_le3t_60GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==1))")
    interf_ljets_le7j_le3t_60GeV_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==1))","ljets_le7j_le3t_60GeV_ttbb_node","")
    interf_ljets_le7j_le3t_60GeV_ttbb_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttbb_node.minxval = 0.17
    interf_ljets_le7j_le3t_60GeV_ttbb_node.maxxval = 0.43
    interf_ljets_le7j_le3t_60GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttbb_node)
    
    interf_ljets_le7j_le3t_60GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_node_ttcc",
                                            label          = "ljets_le7j_le3t_60GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==2))")
    interf_ljets_le7j_le3t_60GeV_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==2))","ljets_le7j_le3t_60GeV_ttcc_node","")
    interf_ljets_le7j_le3t_60GeV_ttcc_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttcc_node.minxval = 0.17
    interf_ljets_le7j_le3t_60GeV_ttcc_node.maxxval = 0.43
    interf_ljets_le7j_le3t_60GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttcc_node)
    
    interf_ljets_le7j_le3t_60GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_node_ttlf",
                                            label          = "ljets_le7j_le3t_60GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==3))")
    interf_ljets_le7j_le3t_60GeV_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==3))","ljets_le7j_le3t_60GeV_ttlf_node","")
    interf_ljets_le7j_le3t_60GeV_ttlf_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttlf_node.minxval = 0.17
    interf_ljets_le7j_le3t_60GeV_ttlf_node.maxxval = 0.5
    interf_ljets_le7j_le3t_60GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttlf_node)
    
    interf_ljets_le7j_le3t_60GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_node_ttHH",
                                            label          = "ljets_le7j_le3t_60GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==4))")
    interf_ljets_le7j_le3t_60GeV_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==4))","ljets_le7j_le3t_60GeV_ttHH_node","")
    interf_ljets_le7j_le3t_60GeV_ttHH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttHH_node.minxval = 0.17
    interf_ljets_le7j_le3t_60GeV_ttHH_node.maxxval = 0.5
    interf_ljets_le7j_le3t_60GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttHH_node)
    
    interf_ljets_le7j_le3t_60GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_node_tt4b",
                                            label          = "ljets_le7j_le3t_60GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==5))")
    interf_ljets_le7j_le3t_60GeV_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV==5))","ljets_le7j_le3t_60GeV_tt4b_node","")
    interf_ljets_le7j_le3t_60GeV_tt4b_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_tt4b_node.minxval = 0.17
    interf_ljets_le7j_le3t_60GeV_tt4b_node.maxxval = 0.56
    interf_ljets_le7j_le3t_60GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_tt4b_node)
    


    # plots for le7j_le3t_90GeV

    interf_ljets_le7j_le3t_90GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_node_ttH",
                                            label          = "ljets_le7j_le3t_90GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==0))")
    interf_ljets_le7j_le3t_90GeV_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==0))","ljets_le7j_le3t_90GeV_ttH_node","")
    interf_ljets_le7j_le3t_90GeV_ttH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttH_node.minxval = 0.17
    interf_ljets_le7j_le3t_90GeV_ttH_node.maxxval = 0.41
    interf_ljets_le7j_le3t_90GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttH_node)
    
    interf_ljets_le7j_le3t_90GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_node_ttbb",
                                            label          = "ljets_le7j_le3t_90GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==1))")
    interf_ljets_le7j_le3t_90GeV_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==1))","ljets_le7j_le3t_90GeV_ttbb_node","")
    interf_ljets_le7j_le3t_90GeV_ttbb_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttbb_node.minxval = 0.17
    interf_ljets_le7j_le3t_90GeV_ttbb_node.maxxval = 0.39
    interf_ljets_le7j_le3t_90GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttbb_node)
    
    interf_ljets_le7j_le3t_90GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_node_ttcc",
                                            label          = "ljets_le7j_le3t_90GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==2))")
    interf_ljets_le7j_le3t_90GeV_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==2))","ljets_le7j_le3t_90GeV_ttcc_node","")
    interf_ljets_le7j_le3t_90GeV_ttcc_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttcc_node.minxval = 0.17
    interf_ljets_le7j_le3t_90GeV_ttcc_node.maxxval = 0.45
    interf_ljets_le7j_le3t_90GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttcc_node)
    
    interf_ljets_le7j_le3t_90GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_node_ttlf",
                                            label          = "ljets_le7j_le3t_90GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==3))")
    interf_ljets_le7j_le3t_90GeV_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==3))","ljets_le7j_le3t_90GeV_ttlf_node","")
    interf_ljets_le7j_le3t_90GeV_ttlf_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttlf_node.minxval = 0.17
    interf_ljets_le7j_le3t_90GeV_ttlf_node.maxxval = 0.48
    interf_ljets_le7j_le3t_90GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttlf_node)
    
    interf_ljets_le7j_le3t_90GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_node_ttHH",
                                            label          = "ljets_le7j_le3t_90GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==4))")
    interf_ljets_le7j_le3t_90GeV_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==4))","ljets_le7j_le3t_90GeV_ttHH_node","")
    interf_ljets_le7j_le3t_90GeV_ttHH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttHH_node.minxval = 0.17
    interf_ljets_le7j_le3t_90GeV_ttHH_node.maxxval = 0.49
    interf_ljets_le7j_le3t_90GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttHH_node)
    
    interf_ljets_le7j_le3t_90GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_node_tt4b",
                                            label          = "ljets_le7j_le3t_90GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==5))")
    interf_ljets_le7j_le3t_90GeV_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV==5))","ljets_le7j_le3t_90GeV_tt4b_node","")
    interf_ljets_le7j_le3t_90GeV_tt4b_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_tt4b_node.minxval = 0.17
    interf_ljets_le7j_le3t_90GeV_tt4b_node.maxxval = 0.52
    interf_ljets_le7j_le3t_90GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_tt4b_node)
    


    # plots for le7j_le3t_30GeV_ttZZ

    interf_ljets_le7j_le3t_30GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_ttZZ_node_ttH",
                                            label          = "ljets_le7j_le3t_30GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==0))")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==0))","ljets_le7j_le3t_30GeV_ttZZ_ttH_node","")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttH_node.maxxval = 0.3
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttZZ_ttH_node)
    
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le7j_le3t_30GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==1))")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==1))","ljets_le7j_le3t_30GeV_ttZZ_ttbb_node","")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttbb_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttbb_node.maxxval = 0.37
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttZZ_ttbb_node)
    
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le7j_le3t_30GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==2))")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==2))","ljets_le7j_le3t_30GeV_ttZZ_ttcc_node","")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttcc_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttcc_node.maxxval = 0.4
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttZZ_ttcc_node)
    
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le7j_le3t_30GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==3))")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==3))","ljets_le7j_le3t_30GeV_ttZZ_ttlf_node","")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttlf_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttlf_node.maxxval = 0.53
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttZZ_ttlf_node)
    
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le7j_le3t_30GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==4))")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==4))","ljets_le7j_le3t_30GeV_ttZZ_ttHH_node","")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttHH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttHH_node.maxxval = 0.39
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttZZ_ttHH_node)
    
    interf_ljets_le7j_le3t_30GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le7j_le3t_30GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==5))")
    interf_ljets_le7j_le3t_30GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==5))","ljets_le7j_le3t_30GeV_ttZZ_tt4b_node","")
    interf_ljets_le7j_le3t_30GeV_ttZZ_tt4b_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le7j_le3t_30GeV_ttZZ_tt4b_node.maxxval = 0.48
    interf_ljets_le7j_le3t_30GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttZZ_tt4b_node)
    
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_30GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le7j_le3t_30GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==6))")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_30GeV_ttZZ==6))","ljets_le7j_le3t_30GeV_ttZZ_ttzz_node","")
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttzz_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttzz_node.maxxval = 0.48
    interf_ljets_le7j_le3t_30GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_30GeV_ttZZ_ttzz_node)
    


    # plots for le7j_le3t_60GeV_ttZZ

    interf_ljets_le7j_le3t_60GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_ttZZ_node_ttH",
                                            label          = "ljets_le7j_le3t_60GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==0))")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==0))","ljets_le7j_le3t_60GeV_ttZZ_ttH_node","")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttH_node.maxxval = 0.34
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttZZ_ttH_node)
    
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le7j_le3t_60GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==1))")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==1))","ljets_le7j_le3t_60GeV_ttZZ_ttbb_node","")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttbb_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttbb_node.maxxval = 0.34
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttZZ_ttbb_node)
    
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le7j_le3t_60GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==2))")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==2))","ljets_le7j_le3t_60GeV_ttZZ_ttcc_node","")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttcc_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttcc_node.maxxval = 0.4
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttZZ_ttcc_node)
    
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le7j_le3t_60GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==3))")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==3))","ljets_le7j_le3t_60GeV_ttZZ_ttlf_node","")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttlf_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttlf_node.maxxval = 0.47
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttZZ_ttlf_node)
    
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le7j_le3t_60GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==4))")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==4))","ljets_le7j_le3t_60GeV_ttZZ_ttHH_node","")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttHH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttHH_node.maxxval = 0.34
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttZZ_ttHH_node)
    
    interf_ljets_le7j_le3t_60GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le7j_le3t_60GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==5))")
    interf_ljets_le7j_le3t_60GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==5))","ljets_le7j_le3t_60GeV_ttZZ_tt4b_node","")
    interf_ljets_le7j_le3t_60GeV_ttZZ_tt4b_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le7j_le3t_60GeV_ttZZ_tt4b_node.maxxval = 0.49
    interf_ljets_le7j_le3t_60GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttZZ_tt4b_node)
    
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_60GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le7j_le3t_60GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==6))")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_60GeV_ttZZ==6))","ljets_le7j_le3t_60GeV_ttZZ_ttzz_node","")
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttzz_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttzz_node.maxxval = 0.44
    interf_ljets_le7j_le3t_60GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_60GeV_ttZZ_ttzz_node)
    


    # plots for le7j_le3t_90GeV_ttZZ

    interf_ljets_le7j_le3t_90GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_ttZZ_node_ttH",
                                            label          = "ljets_le7j_le3t_90GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==0))")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==0))","ljets_le7j_le3t_90GeV_ttZZ_ttH_node","")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttH_node.maxxval = 0.35
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttZZ_ttH_node)
    
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le7j_le3t_90GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==1))")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==1))","ljets_le7j_le3t_90GeV_ttZZ_ttbb_node","")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttbb_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttbb_node.maxxval = 0.36
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttZZ_ttbb_node)
    
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le7j_le3t_90GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==2))")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==2))","ljets_le7j_le3t_90GeV_ttZZ_ttcc_node","")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttcc_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttcc_node.maxxval = 0.43
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttZZ_ttcc_node)
    
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le7j_le3t_90GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==3))")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==3))","ljets_le7j_le3t_90GeV_ttZZ_ttlf_node","")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttlf_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttlf_node.maxxval = 0.42
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttZZ_ttlf_node)
    
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le7j_le3t_90GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==4))")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==4))","ljets_le7j_le3t_90GeV_ttZZ_ttHH_node","")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttHH_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttHH_node.maxxval = 0.35
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttZZ_ttHH_node)
    
    interf_ljets_le7j_le3t_90GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le7j_le3t_90GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==5))")
    interf_ljets_le7j_le3t_90GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==5))","ljets_le7j_le3t_90GeV_ttZZ_tt4b_node","")
    interf_ljets_le7j_le3t_90GeV_ttZZ_tt4b_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le7j_le3t_90GeV_ttZZ_tt4b_node.maxxval = 0.43
    interf_ljets_le7j_le3t_90GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttZZ_tt4b_node)
    
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le3t_90GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le7j_le3t_90GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==6))")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le7j_le3t_90GeV_ttZZ==6))","ljets_le7j_le3t_90GeV_ttZZ_ttzz_node","")
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttzz_node.category_label = "\leq 7 jets, \leq 3 b-tags"
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttzz_node.maxxval = 0.43
    interf_ljets_le7j_le3t_90GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le3t_90GeV_ttZZ_ttzz_node)
    


    # plots for le7j_le4t_30GeV

    interf_ljets_le7j_le4t_30GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_node_ttH",
                                            label          = "ljets_le7j_le4t_30GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==0))")
    interf_ljets_le7j_le4t_30GeV_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==0))","ljets_le7j_le4t_30GeV_ttH_node","")
    interf_ljets_le7j_le4t_30GeV_ttH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttH_node.minxval = 0.17
    interf_ljets_le7j_le4t_30GeV_ttH_node.maxxval = 0.39
    interf_ljets_le7j_le4t_30GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttH_node)
    
    interf_ljets_le7j_le4t_30GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_node_ttbb",
                                            label          = "ljets_le7j_le4t_30GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==1))")
    interf_ljets_le7j_le4t_30GeV_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==1))","ljets_le7j_le4t_30GeV_ttbb_node","")
    interf_ljets_le7j_le4t_30GeV_ttbb_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttbb_node.minxval = 0.17
    interf_ljets_le7j_le4t_30GeV_ttbb_node.maxxval = 0.43
    interf_ljets_le7j_le4t_30GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttbb_node)
    
    interf_ljets_le7j_le4t_30GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_node_ttcc",
                                            label          = "ljets_le7j_le4t_30GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==2))")
    interf_ljets_le7j_le4t_30GeV_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==2))","ljets_le7j_le4t_30GeV_ttcc_node","")
    interf_ljets_le7j_le4t_30GeV_ttcc_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttcc_node.minxval = 0.17
    interf_ljets_le7j_le4t_30GeV_ttcc_node.maxxval = 0.46
    interf_ljets_le7j_le4t_30GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttcc_node)
    
    interf_ljets_le7j_le4t_30GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_node_ttlf",
                                            label          = "ljets_le7j_le4t_30GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==3))")
    interf_ljets_le7j_le4t_30GeV_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==3))","ljets_le7j_le4t_30GeV_ttlf_node","")
    interf_ljets_le7j_le4t_30GeV_ttlf_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttlf_node.minxval = 0.17
    interf_ljets_le7j_le4t_30GeV_ttlf_node.maxxval = 0.58
    interf_ljets_le7j_le4t_30GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttlf_node)
    
    interf_ljets_le7j_le4t_30GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_node_ttHH",
                                            label          = "ljets_le7j_le4t_30GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==4))")
    interf_ljets_le7j_le4t_30GeV_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==4))","ljets_le7j_le4t_30GeV_ttHH_node","")
    interf_ljets_le7j_le4t_30GeV_ttHH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttHH_node.minxval = 0.17
    interf_ljets_le7j_le4t_30GeV_ttHH_node.maxxval = 0.77
    interf_ljets_le7j_le4t_30GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttHH_node)
    
    interf_ljets_le7j_le4t_30GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_node_tt4b",
                                            label          = "ljets_le7j_le4t_30GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==5))")
    interf_ljets_le7j_le4t_30GeV_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV==5))","ljets_le7j_le4t_30GeV_tt4b_node","")
    interf_ljets_le7j_le4t_30GeV_tt4b_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_tt4b_node.minxval = 0.17
    interf_ljets_le7j_le4t_30GeV_tt4b_node.maxxval = 0.63
    interf_ljets_le7j_le4t_30GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_tt4b_node)
    


    # plots for le7j_le4t_60GeV

    interf_ljets_le7j_le4t_60GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_node_ttH",
                                            label          = "ljets_le7j_le4t_60GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==0))")
    interf_ljets_le7j_le4t_60GeV_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==0))","ljets_le7j_le4t_60GeV_ttH_node","")
    interf_ljets_le7j_le4t_60GeV_ttH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttH_node.minxval = 0.17
    interf_ljets_le7j_le4t_60GeV_ttH_node.maxxval = 0.5
    interf_ljets_le7j_le4t_60GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttH_node)
    
    interf_ljets_le7j_le4t_60GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_node_ttbb",
                                            label          = "ljets_le7j_le4t_60GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==1))")
    interf_ljets_le7j_le4t_60GeV_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==1))","ljets_le7j_le4t_60GeV_ttbb_node","")
    interf_ljets_le7j_le4t_60GeV_ttbb_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttbb_node.minxval = 0.17
    interf_ljets_le7j_le4t_60GeV_ttbb_node.maxxval = 0.4
    interf_ljets_le7j_le4t_60GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttbb_node)
    
    interf_ljets_le7j_le4t_60GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_node_ttcc",
                                            label          = "ljets_le7j_le4t_60GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==2))")
    interf_ljets_le7j_le4t_60GeV_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==2))","ljets_le7j_le4t_60GeV_ttcc_node","")
    interf_ljets_le7j_le4t_60GeV_ttcc_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttcc_node.minxval = 0.17
    interf_ljets_le7j_le4t_60GeV_ttcc_node.maxxval = 0.5
    interf_ljets_le7j_le4t_60GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttcc_node)
    
    interf_ljets_le7j_le4t_60GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_node_ttlf",
                                            label          = "ljets_le7j_le4t_60GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==3))")
    interf_ljets_le7j_le4t_60GeV_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==3))","ljets_le7j_le4t_60GeV_ttlf_node","")
    interf_ljets_le7j_le4t_60GeV_ttlf_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttlf_node.minxval = 0.17
    interf_ljets_le7j_le4t_60GeV_ttlf_node.maxxval = 0.57
    interf_ljets_le7j_le4t_60GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttlf_node)
    
    interf_ljets_le7j_le4t_60GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_node_ttHH",
                                            label          = "ljets_le7j_le4t_60GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==4))")
    interf_ljets_le7j_le4t_60GeV_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==4))","ljets_le7j_le4t_60GeV_ttHH_node","")
    interf_ljets_le7j_le4t_60GeV_ttHH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttHH_node.minxval = 0.17
    interf_ljets_le7j_le4t_60GeV_ttHH_node.maxxval = 0.68
    interf_ljets_le7j_le4t_60GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttHH_node)
    
    interf_ljets_le7j_le4t_60GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_node_tt4b",
                                            label          = "ljets_le7j_le4t_60GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==5))")
    interf_ljets_le7j_le4t_60GeV_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV==5))","ljets_le7j_le4t_60GeV_tt4b_node","")
    interf_ljets_le7j_le4t_60GeV_tt4b_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_tt4b_node.minxval = 0.17
    interf_ljets_le7j_le4t_60GeV_tt4b_node.maxxval = 0.66
    interf_ljets_le7j_le4t_60GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_tt4b_node)
    


    # plots for le7j_le4t_90GeV

    interf_ljets_le7j_le4t_90GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_node_ttH",
                                            label          = "ljets_le7j_le4t_90GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==0))")
    interf_ljets_le7j_le4t_90GeV_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==0))","ljets_le7j_le4t_90GeV_ttH_node","")
    interf_ljets_le7j_le4t_90GeV_ttH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttH_node.minxval = 0.17
    interf_ljets_le7j_le4t_90GeV_ttH_node.maxxval = 0.37
    interf_ljets_le7j_le4t_90GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttH_node)
    
    interf_ljets_le7j_le4t_90GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_node_ttbb",
                                            label          = "ljets_le7j_le4t_90GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==1))")
    interf_ljets_le7j_le4t_90GeV_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==1))","ljets_le7j_le4t_90GeV_ttbb_node","")
    interf_ljets_le7j_le4t_90GeV_ttbb_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttbb_node.minxval = 0.17
    interf_ljets_le7j_le4t_90GeV_ttbb_node.maxxval = 0.38
    interf_ljets_le7j_le4t_90GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttbb_node)
    
    interf_ljets_le7j_le4t_90GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_node_ttcc",
                                            label          = "ljets_le7j_le4t_90GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==2))")
    interf_ljets_le7j_le4t_90GeV_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==2))","ljets_le7j_le4t_90GeV_ttcc_node","")
    interf_ljets_le7j_le4t_90GeV_ttcc_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttcc_node.minxval = 0.17
    interf_ljets_le7j_le4t_90GeV_ttcc_node.maxxval = 0.46
    interf_ljets_le7j_le4t_90GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttcc_node)
    
    interf_ljets_le7j_le4t_90GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_node_ttlf",
                                            label          = "ljets_le7j_le4t_90GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==3))")
    interf_ljets_le7j_le4t_90GeV_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==3))","ljets_le7j_le4t_90GeV_ttlf_node","")
    interf_ljets_le7j_le4t_90GeV_ttlf_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttlf_node.minxval = 0.17
    interf_ljets_le7j_le4t_90GeV_ttlf_node.maxxval = 0.53
    interf_ljets_le7j_le4t_90GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttlf_node)
    
    interf_ljets_le7j_le4t_90GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_node_ttHH",
                                            label          = "ljets_le7j_le4t_90GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==4))")
    interf_ljets_le7j_le4t_90GeV_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==4))","ljets_le7j_le4t_90GeV_ttHH_node","")
    interf_ljets_le7j_le4t_90GeV_ttHH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttHH_node.minxval = 0.17
    interf_ljets_le7j_le4t_90GeV_ttHH_node.maxxval = 0.72
    interf_ljets_le7j_le4t_90GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttHH_node)
    
    interf_ljets_le7j_le4t_90GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_node_tt4b",
                                            label          = "ljets_le7j_le4t_90GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==5))")
    interf_ljets_le7j_le4t_90GeV_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV==5))","ljets_le7j_le4t_90GeV_tt4b_node","")
    interf_ljets_le7j_le4t_90GeV_tt4b_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_tt4b_node.minxval = 0.17
    interf_ljets_le7j_le4t_90GeV_tt4b_node.maxxval = 0.61
    interf_ljets_le7j_le4t_90GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_tt4b_node)
    


    # plots for le7j_le4t_30GeV_ttZZ

    interf_ljets_le7j_le4t_30GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_ttZZ_node_ttH",
                                            label          = "ljets_le7j_le4t_30GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==0))")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==0))","ljets_le7j_le4t_30GeV_ttZZ_ttH_node","")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttH_node.maxxval = 0.3
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttZZ_ttH_node)
    
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le7j_le4t_30GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==1))")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==1))","ljets_le7j_le4t_30GeV_ttZZ_ttbb_node","")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttbb_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttbb_node.maxxval = 0.39
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttZZ_ttbb_node)
    
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le7j_le4t_30GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==2))")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==2))","ljets_le7j_le4t_30GeV_ttZZ_ttcc_node","")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttcc_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttcc_node.maxxval = 0.41
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttZZ_ttcc_node)
    
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le7j_le4t_30GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==3))")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==3))","ljets_le7j_le4t_30GeV_ttZZ_ttlf_node","")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttlf_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttlf_node.maxxval = 0.55
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttZZ_ttlf_node)
    
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le7j_le4t_30GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==4))")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==4))","ljets_le7j_le4t_30GeV_ttZZ_ttHH_node","")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttHH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttHH_node.maxxval = 0.49
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttZZ_ttHH_node)
    
    interf_ljets_le7j_le4t_30GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le7j_le4t_30GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==5))")
    interf_ljets_le7j_le4t_30GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==5))","ljets_le7j_le4t_30GeV_ttZZ_tt4b_node","")
    interf_ljets_le7j_le4t_30GeV_ttZZ_tt4b_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le7j_le4t_30GeV_ttZZ_tt4b_node.maxxval = 0.55
    interf_ljets_le7j_le4t_30GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttZZ_tt4b_node)
    
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_30GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le7j_le4t_30GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==6))")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_30GeV_ttZZ==6))","ljets_le7j_le4t_30GeV_ttZZ_ttzz_node","")
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttzz_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttzz_node.maxxval = 0.53
    interf_ljets_le7j_le4t_30GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_30GeV_ttZZ_ttzz_node)
    


    # plots for le7j_le4t_60GeV_ttZZ

    interf_ljets_le7j_le4t_60GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_ttZZ_node_ttH",
                                            label          = "ljets_le7j_le4t_60GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==0))")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==0))","ljets_le7j_le4t_60GeV_ttZZ_ttH_node","")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttH_node.maxxval = 0.34
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttZZ_ttH_node)
    
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le7j_le4t_60GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==1))")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==1))","ljets_le7j_le4t_60GeV_ttZZ_ttbb_node","")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttbb_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttbb_node.maxxval = 0.34
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttZZ_ttbb_node)
    
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le7j_le4t_60GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==2))")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==2))","ljets_le7j_le4t_60GeV_ttZZ_ttcc_node","")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttcc_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttcc_node.maxxval = 0.47
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttZZ_ttcc_node)
    
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le7j_le4t_60GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==3))")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==3))","ljets_le7j_le4t_60GeV_ttZZ_ttlf_node","")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttlf_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttlf_node.maxxval = 0.54
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttZZ_ttlf_node)
    
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le7j_le4t_60GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==4))")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==4))","ljets_le7j_le4t_60GeV_ttZZ_ttHH_node","")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttHH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttHH_node.maxxval = 0.44
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttZZ_ttHH_node)
    
    interf_ljets_le7j_le4t_60GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le7j_le4t_60GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==5))")
    interf_ljets_le7j_le4t_60GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==5))","ljets_le7j_le4t_60GeV_ttZZ_tt4b_node","")
    interf_ljets_le7j_le4t_60GeV_ttZZ_tt4b_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le7j_le4t_60GeV_ttZZ_tt4b_node.maxxval = 0.54
    interf_ljets_le7j_le4t_60GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttZZ_tt4b_node)
    
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_60GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le7j_le4t_60GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==6))")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_60GeV_ttZZ==6))","ljets_le7j_le4t_60GeV_ttZZ_ttzz_node","")
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttzz_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttzz_node.maxxval = 0.61
    interf_ljets_le7j_le4t_60GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_60GeV_ttZZ_ttzz_node)
    


    # plots for le7j_le4t_90GeV_ttZZ

    interf_ljets_le7j_le4t_90GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_ttZZ_node_ttH",
                                            label          = "ljets_le7j_le4t_90GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==0))")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==0))","ljets_le7j_le4t_90GeV_ttZZ_ttH_node","")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttH_node.maxxval = 0.31
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttZZ_ttH_node)
    
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le7j_le4t_90GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==1))")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==1))","ljets_le7j_le4t_90GeV_ttZZ_ttbb_node","")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttbb_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttbb_node.maxxval = 0.38
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttZZ_ttbb_node)
    
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le7j_le4t_90GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==2))")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==2))","ljets_le7j_le4t_90GeV_ttZZ_ttcc_node","")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttcc_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttcc_node.maxxval = 0.44
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttZZ_ttcc_node)
    
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le7j_le4t_90GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==3))")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==3))","ljets_le7j_le4t_90GeV_ttZZ_ttlf_node","")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttlf_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttlf_node.maxxval = 0.5
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttZZ_ttlf_node)
    
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le7j_le4t_90GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==4))")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==4))","ljets_le7j_le4t_90GeV_ttZZ_ttHH_node","")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttHH_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttHH_node.maxxval = 0.47
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttZZ_ttHH_node)
    
    interf_ljets_le7j_le4t_90GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le7j_le4t_90GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==5))")
    interf_ljets_le7j_le4t_90GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==5))","ljets_le7j_le4t_90GeV_ttZZ_tt4b_node","")
    interf_ljets_le7j_le4t_90GeV_ttZZ_tt4b_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le7j_le4t_90GeV_ttZZ_tt4b_node.maxxval = 0.52
    interf_ljets_le7j_le4t_90GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttZZ_tt4b_node)
    
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le7j_le4t_90GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le7j_le4t_90GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==6))")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=7&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le7j_le4t_90GeV_ttZZ==6))","ljets_le7j_le4t_90GeV_ttZZ_ttzz_node","")
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttzz_node.category_label = "\leq 7 jets, \leq 4 b-tags"
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttzz_node.maxxval = 0.5
    interf_ljets_le7j_le4t_90GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le7j_le4t_90GeV_ttZZ_ttzz_node)
    


    # plots for le5j_le4t_30GeV

    interf_ljets_le5j_le4t_30GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_node_ttH",
                                            label          = "ljets_le5j_le4t_30GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==0))")
    interf_ljets_le5j_le4t_30GeV_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==0))","ljets_le5j_le4t_30GeV_ttH_node","")
    interf_ljets_le5j_le4t_30GeV_ttH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttH_node.minxval = 0.17
    interf_ljets_le5j_le4t_30GeV_ttH_node.maxxval = 0.37
    interf_ljets_le5j_le4t_30GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttH_node)
    
    interf_ljets_le5j_le4t_30GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_node_ttbb",
                                            label          = "ljets_le5j_le4t_30GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==1))")
    interf_ljets_le5j_le4t_30GeV_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==1))","ljets_le5j_le4t_30GeV_ttbb_node","")
    interf_ljets_le5j_le4t_30GeV_ttbb_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttbb_node.minxval = 0.17
    interf_ljets_le5j_le4t_30GeV_ttbb_node.maxxval = 0.42
    interf_ljets_le5j_le4t_30GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttbb_node)
    
    interf_ljets_le5j_le4t_30GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_node_ttcc",
                                            label          = "ljets_le5j_le4t_30GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==2))")
    interf_ljets_le5j_le4t_30GeV_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==2))","ljets_le5j_le4t_30GeV_ttcc_node","")
    interf_ljets_le5j_le4t_30GeV_ttcc_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttcc_node.minxval = 0.17
    interf_ljets_le5j_le4t_30GeV_ttcc_node.maxxval = 0.47
    interf_ljets_le5j_le4t_30GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttcc_node)
    
    interf_ljets_le5j_le4t_30GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_node_ttlf",
                                            label          = "ljets_le5j_le4t_30GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==3))")
    interf_ljets_le5j_le4t_30GeV_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==3))","ljets_le5j_le4t_30GeV_ttlf_node","")
    interf_ljets_le5j_le4t_30GeV_ttlf_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttlf_node.minxval = 0.17
    interf_ljets_le5j_le4t_30GeV_ttlf_node.maxxval = 0.54
    interf_ljets_le5j_le4t_30GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttlf_node)
    
    interf_ljets_le5j_le4t_30GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_node_ttHH",
                                            label          = "ljets_le5j_le4t_30GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==4))")
    interf_ljets_le5j_le4t_30GeV_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==4))","ljets_le5j_le4t_30GeV_ttHH_node","")
    interf_ljets_le5j_le4t_30GeV_ttHH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttHH_node.minxval = 0.17
    interf_ljets_le5j_le4t_30GeV_ttHH_node.maxxval = 0.8
    interf_ljets_le5j_le4t_30GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttHH_node)
    
    interf_ljets_le5j_le4t_30GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_node_tt4b",
                                            label          = "ljets_le5j_le4t_30GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==5))")
    interf_ljets_le5j_le4t_30GeV_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV==5))","ljets_le5j_le4t_30GeV_tt4b_node","")
    interf_ljets_le5j_le4t_30GeV_tt4b_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_tt4b_node.minxval = 0.17
    interf_ljets_le5j_le4t_30GeV_tt4b_node.maxxval = 0.61
    interf_ljets_le5j_le4t_30GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_tt4b_node)
    


    # plots for le5j_le4t_60GeV

    interf_ljets_le5j_le4t_60GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_node_ttH",
                                            label          = "ljets_le5j_le4t_60GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==0))")
    interf_ljets_le5j_le4t_60GeV_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==0))","ljets_le5j_le4t_60GeV_ttH_node","")
    interf_ljets_le5j_le4t_60GeV_ttH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttH_node.minxval = 0.17
    interf_ljets_le5j_le4t_60GeV_ttH_node.maxxval = 0.37
    interf_ljets_le5j_le4t_60GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttH_node)
    
    interf_ljets_le5j_le4t_60GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_node_ttbb",
                                            label          = "ljets_le5j_le4t_60GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==1))")
    interf_ljets_le5j_le4t_60GeV_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==1))","ljets_le5j_le4t_60GeV_ttbb_node","")
    interf_ljets_le5j_le4t_60GeV_ttbb_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttbb_node.minxval = 0.17
    interf_ljets_le5j_le4t_60GeV_ttbb_node.maxxval = 0.4
    interf_ljets_le5j_le4t_60GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttbb_node)
    
    interf_ljets_le5j_le4t_60GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_node_ttcc",
                                            label          = "ljets_le5j_le4t_60GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==2))")
    interf_ljets_le5j_le4t_60GeV_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==2))","ljets_le5j_le4t_60GeV_ttcc_node","")
    interf_ljets_le5j_le4t_60GeV_ttcc_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttcc_node.minxval = 0.17
    interf_ljets_le5j_le4t_60GeV_ttcc_node.maxxval = 0.52
    interf_ljets_le5j_le4t_60GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttcc_node)
    
    interf_ljets_le5j_le4t_60GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_node_ttlf",
                                            label          = "ljets_le5j_le4t_60GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==3))")
    interf_ljets_le5j_le4t_60GeV_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==3))","ljets_le5j_le4t_60GeV_ttlf_node","")
    interf_ljets_le5j_le4t_60GeV_ttlf_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttlf_node.minxval = 0.17
    interf_ljets_le5j_le4t_60GeV_ttlf_node.maxxval = 0.51
    interf_ljets_le5j_le4t_60GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttlf_node)
    
    interf_ljets_le5j_le4t_60GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_node_ttHH",
                                            label          = "ljets_le5j_le4t_60GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==4))")
    interf_ljets_le5j_le4t_60GeV_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==4))","ljets_le5j_le4t_60GeV_ttHH_node","")
    interf_ljets_le5j_le4t_60GeV_ttHH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttHH_node.minxval = 0.17
    interf_ljets_le5j_le4t_60GeV_ttHH_node.maxxval = 0.69
    interf_ljets_le5j_le4t_60GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttHH_node)
    
    interf_ljets_le5j_le4t_60GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_node_tt4b",
                                            label          = "ljets_le5j_le4t_60GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==5))")
    interf_ljets_le5j_le4t_60GeV_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV==5))","ljets_le5j_le4t_60GeV_tt4b_node","")
    interf_ljets_le5j_le4t_60GeV_tt4b_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_tt4b_node.minxval = 0.17
    interf_ljets_le5j_le4t_60GeV_tt4b_node.maxxval = 0.62
    interf_ljets_le5j_le4t_60GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_tt4b_node)
    


    # plots for le5j_le4t_90GeV

    interf_ljets_le5j_le4t_90GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_node_ttH",
                                            label          = "ljets_le5j_le4t_90GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==0))")
    interf_ljets_le5j_le4t_90GeV_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==0))","ljets_le5j_le4t_90GeV_ttH_node","")
    interf_ljets_le5j_le4t_90GeV_ttH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttH_node.minxval = 0.17
    interf_ljets_le5j_le4t_90GeV_ttH_node.maxxval = 0.37
    interf_ljets_le5j_le4t_90GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttH_node)
    
    interf_ljets_le5j_le4t_90GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_node_ttbb",
                                            label          = "ljets_le5j_le4t_90GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==1))")
    interf_ljets_le5j_le4t_90GeV_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==1))","ljets_le5j_le4t_90GeV_ttbb_node","")
    interf_ljets_le5j_le4t_90GeV_ttbb_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttbb_node.minxval = 0.17
    interf_ljets_le5j_le4t_90GeV_ttbb_node.maxxval = 0.41
    interf_ljets_le5j_le4t_90GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttbb_node)
    
    interf_ljets_le5j_le4t_90GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_node_ttcc",
                                            label          = "ljets_le5j_le4t_90GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==2))")
    interf_ljets_le5j_le4t_90GeV_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==2))","ljets_le5j_le4t_90GeV_ttcc_node","")
    interf_ljets_le5j_le4t_90GeV_ttcc_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttcc_node.minxval = 0.17
    interf_ljets_le5j_le4t_90GeV_ttcc_node.maxxval = 0.55
    interf_ljets_le5j_le4t_90GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttcc_node)
    
    interf_ljets_le5j_le4t_90GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_node_ttlf",
                                            label          = "ljets_le5j_le4t_90GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==3))")
    interf_ljets_le5j_le4t_90GeV_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==3))","ljets_le5j_le4t_90GeV_ttlf_node","")
    interf_ljets_le5j_le4t_90GeV_ttlf_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttlf_node.minxval = 0.17
    interf_ljets_le5j_le4t_90GeV_ttlf_node.maxxval = 0.49
    interf_ljets_le5j_le4t_90GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttlf_node)
    
    interf_ljets_le5j_le4t_90GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_node_ttHH",
                                            label          = "ljets_le5j_le4t_90GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==4))")
    interf_ljets_le5j_le4t_90GeV_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==4))","ljets_le5j_le4t_90GeV_ttHH_node","")
    interf_ljets_le5j_le4t_90GeV_ttHH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttHH_node.minxval = 0.17
    interf_ljets_le5j_le4t_90GeV_ttHH_node.maxxval = 0.67
    interf_ljets_le5j_le4t_90GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttHH_node)
    
    interf_ljets_le5j_le4t_90GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_node_tt4b",
                                            label          = "ljets_le5j_le4t_90GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==5))")
    interf_ljets_le5j_le4t_90GeV_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV==5))","ljets_le5j_le4t_90GeV_tt4b_node","")
    interf_ljets_le5j_le4t_90GeV_tt4b_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_tt4b_node.minxval = 0.17
    interf_ljets_le5j_le4t_90GeV_tt4b_node.maxxval = 0.47
    interf_ljets_le5j_le4t_90GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_tt4b_node)
    


    # plots for le5j_le4t_30GeV_ttZZ

    interf_ljets_le5j_le4t_30GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_ttZZ_node_ttH",
                                            label          = "ljets_le5j_le4t_30GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==0))")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==0))","ljets_le5j_le4t_30GeV_ttZZ_ttH_node","")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttH_node.maxxval = 0.29
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttZZ_ttH_node)
    
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le5j_le4t_30GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==1))")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==1))","ljets_le5j_le4t_30GeV_ttZZ_ttbb_node","")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttbb_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttbb_node.maxxval = 0.38
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttZZ_ttbb_node)
    
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le5j_le4t_30GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==2))")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==2))","ljets_le5j_le4t_30GeV_ttZZ_ttcc_node","")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttcc_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttcc_node.maxxval = 0.45
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttZZ_ttcc_node)
    
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le5j_le4t_30GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==3))")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==3))","ljets_le5j_le4t_30GeV_ttZZ_ttlf_node","")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttlf_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttlf_node.maxxval = 0.53
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttZZ_ttlf_node)
    
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le5j_le4t_30GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==4))")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==4))","ljets_le5j_le4t_30GeV_ttZZ_ttHH_node","")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttHH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttHH_node.maxxval = 0.49
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttZZ_ttHH_node)
    
    interf_ljets_le5j_le4t_30GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le5j_le4t_30GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==5))")
    interf_ljets_le5j_le4t_30GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==5))","ljets_le5j_le4t_30GeV_ttZZ_tt4b_node","")
    interf_ljets_le5j_le4t_30GeV_ttZZ_tt4b_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le5j_le4t_30GeV_ttZZ_tt4b_node.maxxval = 0.51
    interf_ljets_le5j_le4t_30GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttZZ_tt4b_node)
    
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_30GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le5j_le4t_30GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==6))")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_30GeV_ttZZ==6))","ljets_le5j_le4t_30GeV_ttZZ_ttzz_node","")
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttzz_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttzz_node.maxxval = 0.51
    interf_ljets_le5j_le4t_30GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_30GeV_ttZZ_ttzz_node)
    


    # plots for le5j_le4t_60GeV_ttZZ

    interf_ljets_le5j_le4t_60GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_ttZZ_node_ttH",
                                            label          = "ljets_le5j_le4t_60GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==0))")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==0))","ljets_le5j_le4t_60GeV_ttZZ_ttH_node","")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttH_node.maxxval = 0.3
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttZZ_ttH_node)
    
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le5j_le4t_60GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==1))")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==1))","ljets_le5j_le4t_60GeV_ttZZ_ttbb_node","")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttbb_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttbb_node.maxxval = 0.4
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttZZ_ttbb_node)
    
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le5j_le4t_60GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==2))")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==2))","ljets_le5j_le4t_60GeV_ttZZ_ttcc_node","")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttcc_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttcc_node.maxxval = 0.47
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttZZ_ttcc_node)
    
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le5j_le4t_60GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==3))")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==3))","ljets_le5j_le4t_60GeV_ttZZ_ttlf_node","")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttlf_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttlf_node.maxxval = 0.49
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttZZ_ttlf_node)
    
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le5j_le4t_60GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==4))")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==4))","ljets_le5j_le4t_60GeV_ttZZ_ttHH_node","")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttHH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttHH_node.maxxval = 0.48
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttZZ_ttHH_node)
    
    interf_ljets_le5j_le4t_60GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le5j_le4t_60GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==5))")
    interf_ljets_le5j_le4t_60GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==5))","ljets_le5j_le4t_60GeV_ttZZ_tt4b_node","")
    interf_ljets_le5j_le4t_60GeV_ttZZ_tt4b_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le5j_le4t_60GeV_ttZZ_tt4b_node.maxxval = 0.52
    interf_ljets_le5j_le4t_60GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttZZ_tt4b_node)
    
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_60GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le5j_le4t_60GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==6))")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_60GeV_ttZZ==6))","ljets_le5j_le4t_60GeV_ttZZ_ttzz_node","")
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttzz_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttzz_node.maxxval = 0.49
    interf_ljets_le5j_le4t_60GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_60GeV_ttZZ_ttzz_node)
    


    # plots for le5j_le4t_90GeV_ttZZ

    interf_ljets_le5j_le4t_90GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_ttZZ_node_ttH",
                                            label          = "ljets_le5j_le4t_90GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==0))")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==0))","ljets_le5j_le4t_90GeV_ttZZ_ttH_node","")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttH_node.maxxval = 0.29
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttZZ_ttH_node)
    
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le5j_le4t_90GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==1))")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==1))","ljets_le5j_le4t_90GeV_ttZZ_ttbb_node","")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttbb_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttbb_node.maxxval = 0.33
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttZZ_ttbb_node)
    
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le5j_le4t_90GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==2))")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==2))","ljets_le5j_le4t_90GeV_ttZZ_ttcc_node","")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttcc_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttcc_node.maxxval = 0.56
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttZZ_ttcc_node)
    
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le5j_le4t_90GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==3))")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==3))","ljets_le5j_le4t_90GeV_ttZZ_ttlf_node","")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttlf_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttlf_node.maxxval = 0.51
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttZZ_ttlf_node)
    
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le5j_le4t_90GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==4))")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==4))","ljets_le5j_le4t_90GeV_ttZZ_ttHH_node","")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttHH_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttHH_node.maxxval = 0.45
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttZZ_ttHH_node)
    
    interf_ljets_le5j_le4t_90GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le5j_le4t_90GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==5))")
    interf_ljets_le5j_le4t_90GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==5))","ljets_le5j_le4t_90GeV_ttZZ_tt4b_node","")
    interf_ljets_le5j_le4t_90GeV_ttZZ_tt4b_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le5j_le4t_90GeV_ttZZ_tt4b_node.maxxval = 0.4
    interf_ljets_le5j_le4t_90GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttZZ_tt4b_node)
    
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le5j_le4t_90GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le5j_le4t_90GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==6))")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=5&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le5j_le4t_90GeV_ttZZ==6))","ljets_le5j_le4t_90GeV_ttZZ_ttzz_node","")
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttzz_node.category_label = "\leq 5 jets, \leq 4 b-tags"
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttzz_node.maxxval = 0.42
    interf_ljets_le5j_le4t_90GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le5j_le4t_90GeV_ttZZ_ttzz_node)
    


    # plots for le6j_le4t_30GeV

    interf_ljets_le6j_le4t_30GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_node_ttH",
                                            label          = "ljets_le6j_le4t_30GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==0))")
    interf_ljets_le6j_le4t_30GeV_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==0))","ljets_le6j_le4t_30GeV_ttH_node","")
    interf_ljets_le6j_le4t_30GeV_ttH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttH_node.minxval = 0.17
    interf_ljets_le6j_le4t_30GeV_ttH_node.maxxval = 0.4
    interf_ljets_le6j_le4t_30GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttH_node)
    
    interf_ljets_le6j_le4t_30GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_node_ttbb",
                                            label          = "ljets_le6j_le4t_30GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==1))")
    interf_ljets_le6j_le4t_30GeV_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==1))","ljets_le6j_le4t_30GeV_ttbb_node","")
    interf_ljets_le6j_le4t_30GeV_ttbb_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttbb_node.minxval = 0.17
    interf_ljets_le6j_le4t_30GeV_ttbb_node.maxxval = 0.4
    interf_ljets_le6j_le4t_30GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttbb_node)
    
    interf_ljets_le6j_le4t_30GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_node_ttcc",
                                            label          = "ljets_le6j_le4t_30GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==2))")
    interf_ljets_le6j_le4t_30GeV_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==2))","ljets_le6j_le4t_30GeV_ttcc_node","")
    interf_ljets_le6j_le4t_30GeV_ttcc_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttcc_node.minxval = 0.17
    interf_ljets_le6j_le4t_30GeV_ttcc_node.maxxval = 0.46
    interf_ljets_le6j_le4t_30GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttcc_node)
    
    interf_ljets_le6j_le4t_30GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_node_ttlf",
                                            label          = "ljets_le6j_le4t_30GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==3))")
    interf_ljets_le6j_le4t_30GeV_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==3))","ljets_le6j_le4t_30GeV_ttlf_node","")
    interf_ljets_le6j_le4t_30GeV_ttlf_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttlf_node.minxval = 0.17
    interf_ljets_le6j_le4t_30GeV_ttlf_node.maxxval = 0.55
    interf_ljets_le6j_le4t_30GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttlf_node)
    
    interf_ljets_le6j_le4t_30GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_node_ttHH",
                                            label          = "ljets_le6j_le4t_30GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==4))")
    interf_ljets_le6j_le4t_30GeV_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==4))","ljets_le6j_le4t_30GeV_ttHH_node","")
    interf_ljets_le6j_le4t_30GeV_ttHH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttHH_node.minxval = 0.17
    interf_ljets_le6j_le4t_30GeV_ttHH_node.maxxval = 0.76
    interf_ljets_le6j_le4t_30GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttHH_node)
    
    interf_ljets_le6j_le4t_30GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_node_tt4b",
                                            label          = "ljets_le6j_le4t_30GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==5))")
    interf_ljets_le6j_le4t_30GeV_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV==5))","ljets_le6j_le4t_30GeV_tt4b_node","")
    interf_ljets_le6j_le4t_30GeV_tt4b_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_tt4b_node.minxval = 0.17
    interf_ljets_le6j_le4t_30GeV_tt4b_node.maxxval = 0.66
    interf_ljets_le6j_le4t_30GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_tt4b_node)
    


    # plots for le6j_le4t_60GeV

    interf_ljets_le6j_le4t_60GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_node_ttH",
                                            label          = "ljets_le6j_le4t_60GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==0))")
    interf_ljets_le6j_le4t_60GeV_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==0))","ljets_le6j_le4t_60GeV_ttH_node","")
    interf_ljets_le6j_le4t_60GeV_ttH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttH_node.minxval = 0.17
    interf_ljets_le6j_le4t_60GeV_ttH_node.maxxval = 0.43
    interf_ljets_le6j_le4t_60GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttH_node)
    
    interf_ljets_le6j_le4t_60GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_node_ttbb",
                                            label          = "ljets_le6j_le4t_60GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==1))")
    interf_ljets_le6j_le4t_60GeV_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==1))","ljets_le6j_le4t_60GeV_ttbb_node","")
    interf_ljets_le6j_le4t_60GeV_ttbb_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttbb_node.minxval = 0.17
    interf_ljets_le6j_le4t_60GeV_ttbb_node.maxxval = 0.37
    interf_ljets_le6j_le4t_60GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttbb_node)
    
    interf_ljets_le6j_le4t_60GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_node_ttcc",
                                            label          = "ljets_le6j_le4t_60GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==2))")
    interf_ljets_le6j_le4t_60GeV_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==2))","ljets_le6j_le4t_60GeV_ttcc_node","")
    interf_ljets_le6j_le4t_60GeV_ttcc_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttcc_node.minxval = 0.17
    interf_ljets_le6j_le4t_60GeV_ttcc_node.maxxval = 0.48
    interf_ljets_le6j_le4t_60GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttcc_node)
    
    interf_ljets_le6j_le4t_60GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_node_ttlf",
                                            label          = "ljets_le6j_le4t_60GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==3))")
    interf_ljets_le6j_le4t_60GeV_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==3))","ljets_le6j_le4t_60GeV_ttlf_node","")
    interf_ljets_le6j_le4t_60GeV_ttlf_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttlf_node.minxval = 0.17
    interf_ljets_le6j_le4t_60GeV_ttlf_node.maxxval = 0.57
    interf_ljets_le6j_le4t_60GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttlf_node)
    
    interf_ljets_le6j_le4t_60GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_node_ttHH",
                                            label          = "ljets_le6j_le4t_60GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==4))")
    interf_ljets_le6j_le4t_60GeV_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==4))","ljets_le6j_le4t_60GeV_ttHH_node","")
    interf_ljets_le6j_le4t_60GeV_ttHH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttHH_node.minxval = 0.17
    interf_ljets_le6j_le4t_60GeV_ttHH_node.maxxval = 0.76
    interf_ljets_le6j_le4t_60GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttHH_node)
    
    interf_ljets_le6j_le4t_60GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_node_tt4b",
                                            label          = "ljets_le6j_le4t_60GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==5))")
    interf_ljets_le6j_le4t_60GeV_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV==5))","ljets_le6j_le4t_60GeV_tt4b_node","")
    interf_ljets_le6j_le4t_60GeV_tt4b_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_tt4b_node.minxval = 0.17
    interf_ljets_le6j_le4t_60GeV_tt4b_node.maxxval = 0.66
    interf_ljets_le6j_le4t_60GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_tt4b_node)
    


    # plots for le6j_le4t_90GeV

    interf_ljets_le6j_le4t_90GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_node_ttH",
                                            label          = "ljets_le6j_le4t_90GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==0))")
    interf_ljets_le6j_le4t_90GeV_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==0))","ljets_le6j_le4t_90GeV_ttH_node","")
    interf_ljets_le6j_le4t_90GeV_ttH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttH_node.minxval = 0.17
    interf_ljets_le6j_le4t_90GeV_ttH_node.maxxval = 0.37
    interf_ljets_le6j_le4t_90GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttH_node)
    
    interf_ljets_le6j_le4t_90GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_node_ttbb",
                                            label          = "ljets_le6j_le4t_90GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==1))")
    interf_ljets_le6j_le4t_90GeV_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==1))","ljets_le6j_le4t_90GeV_ttbb_node","")
    interf_ljets_le6j_le4t_90GeV_ttbb_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttbb_node.minxval = 0.17
    interf_ljets_le6j_le4t_90GeV_ttbb_node.maxxval = 0.36
    interf_ljets_le6j_le4t_90GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttbb_node)
    
    interf_ljets_le6j_le4t_90GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_node_ttcc",
                                            label          = "ljets_le6j_le4t_90GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==2))")
    interf_ljets_le6j_le4t_90GeV_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==2))","ljets_le6j_le4t_90GeV_ttcc_node","")
    interf_ljets_le6j_le4t_90GeV_ttcc_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttcc_node.minxval = 0.17
    interf_ljets_le6j_le4t_90GeV_ttcc_node.maxxval = 0.49
    interf_ljets_le6j_le4t_90GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttcc_node)
    
    interf_ljets_le6j_le4t_90GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_node_ttlf",
                                            label          = "ljets_le6j_le4t_90GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==3))")
    interf_ljets_le6j_le4t_90GeV_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==3))","ljets_le6j_le4t_90GeV_ttlf_node","")
    interf_ljets_le6j_le4t_90GeV_ttlf_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttlf_node.minxval = 0.17
    interf_ljets_le6j_le4t_90GeV_ttlf_node.maxxval = 0.54
    interf_ljets_le6j_le4t_90GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttlf_node)
    
    interf_ljets_le6j_le4t_90GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_node_ttHH",
                                            label          = "ljets_le6j_le4t_90GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==4))")
    interf_ljets_le6j_le4t_90GeV_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==4))","ljets_le6j_le4t_90GeV_ttHH_node","")
    interf_ljets_le6j_le4t_90GeV_ttHH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttHH_node.minxval = 0.17
    interf_ljets_le6j_le4t_90GeV_ttHH_node.maxxval = 0.68
    interf_ljets_le6j_le4t_90GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttHH_node)
    
    interf_ljets_le6j_le4t_90GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_node_tt4b",
                                            label          = "ljets_le6j_le4t_90GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==5))")
    interf_ljets_le6j_le4t_90GeV_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV==5))","ljets_le6j_le4t_90GeV_tt4b_node","")
    interf_ljets_le6j_le4t_90GeV_tt4b_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_tt4b_node.minxval = 0.17
    interf_ljets_le6j_le4t_90GeV_tt4b_node.maxxval = 0.58
    interf_ljets_le6j_le4t_90GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_tt4b_node)
    


    # plots for le6j_le4t_30GeV_ttZZ

    interf_ljets_le6j_le4t_30GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_ttZZ_node_ttH",
                                            label          = "ljets_le6j_le4t_30GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==0))")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==0))","ljets_le6j_le4t_30GeV_ttZZ_ttH_node","")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttH_node.maxxval = 0.29
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttZZ_ttH_node)
    
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le6j_le4t_30GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==1))")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==1))","ljets_le6j_le4t_30GeV_ttZZ_ttbb_node","")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttbb_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttbb_node.maxxval = 0.38
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttZZ_ttbb_node)
    
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le6j_le4t_30GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==2))")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==2))","ljets_le6j_le4t_30GeV_ttZZ_ttcc_node","")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttcc_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttcc_node.maxxval = 0.45
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttZZ_ttcc_node)
    
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le6j_le4t_30GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==3))")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==3))","ljets_le6j_le4t_30GeV_ttZZ_ttlf_node","")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttlf_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttlf_node.maxxval = 0.54
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttZZ_ttlf_node)
    
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le6j_le4t_30GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==4))")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==4))","ljets_le6j_le4t_30GeV_ttZZ_ttHH_node","")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttHH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttHH_node.maxxval = 0.49
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttZZ_ttHH_node)
    
    interf_ljets_le6j_le4t_30GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le6j_le4t_30GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==5))")
    interf_ljets_le6j_le4t_30GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==5))","ljets_le6j_le4t_30GeV_ttZZ_tt4b_node","")
    interf_ljets_le6j_le4t_30GeV_ttZZ_tt4b_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le6j_le4t_30GeV_ttZZ_tt4b_node.maxxval = 0.52
    interf_ljets_le6j_le4t_30GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttZZ_tt4b_node)
    
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_30GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le6j_le4t_30GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==6))")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_30GeV_ttZZ==6))","ljets_le6j_le4t_30GeV_ttZZ_ttzz_node","")
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttzz_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttzz_node.maxxval = 0.52
    interf_ljets_le6j_le4t_30GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_30GeV_ttZZ_ttzz_node)
    


    # plots for le6j_le4t_60GeV_ttZZ

    interf_ljets_le6j_le4t_60GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_ttZZ_node_ttH",
                                            label          = "ljets_le6j_le4t_60GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==0))")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==0))","ljets_le6j_le4t_60GeV_ttZZ_ttH_node","")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttH_node.maxxval = 0.29
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttZZ_ttH_node)
    
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le6j_le4t_60GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==1))")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==1))","ljets_le6j_le4t_60GeV_ttZZ_ttbb_node","")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttbb_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttbb_node.maxxval = 0.35
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttZZ_ttbb_node)
    
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le6j_le4t_60GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==2))")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==2))","ljets_le6j_le4t_60GeV_ttZZ_ttcc_node","")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttcc_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttcc_node.maxxval = 0.47
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttZZ_ttcc_node)
    
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le6j_le4t_60GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==3))")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==3))","ljets_le6j_le4t_60GeV_ttZZ_ttlf_node","")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttlf_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttlf_node.maxxval = 0.51
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttZZ_ttlf_node)
    
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le6j_le4t_60GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==4))")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==4))","ljets_le6j_le4t_60GeV_ttZZ_ttHH_node","")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttHH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttHH_node.maxxval = 0.48
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttZZ_ttHH_node)
    
    interf_ljets_le6j_le4t_60GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le6j_le4t_60GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==5))")
    interf_ljets_le6j_le4t_60GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==5))","ljets_le6j_le4t_60GeV_ttZZ_tt4b_node","")
    interf_ljets_le6j_le4t_60GeV_ttZZ_tt4b_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le6j_le4t_60GeV_ttZZ_tt4b_node.maxxval = 0.55
    interf_ljets_le6j_le4t_60GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttZZ_tt4b_node)
    
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_60GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le6j_le4t_60GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==6))")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_60GeV_ttZZ==6))","ljets_le6j_le4t_60GeV_ttZZ_ttzz_node","")
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttzz_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttzz_node.maxxval = 0.56
    interf_ljets_le6j_le4t_60GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_60GeV_ttZZ_ttzz_node)
    


    # plots for le6j_le4t_90GeV_ttZZ

    interf_ljets_le6j_le4t_90GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_ttZZ_node_ttH",
                                            label          = "ljets_le6j_le4t_90GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==0))")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==0))","ljets_le6j_le4t_90GeV_ttZZ_ttH_node","")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttH_node.maxxval = 0.33
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttZZ_ttH_node)
    
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le6j_le4t_90GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==1))")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==1))","ljets_le6j_le4t_90GeV_ttZZ_ttbb_node","")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttbb_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttbb_node.maxxval = 0.34
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttZZ_ttbb_node)
    
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le6j_le4t_90GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==2))")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==2))","ljets_le6j_le4t_90GeV_ttZZ_ttcc_node","")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttcc_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttcc_node.maxxval = 0.43
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttZZ_ttcc_node)
    
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le6j_le4t_90GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==3))")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==3))","ljets_le6j_le4t_90GeV_ttZZ_ttlf_node","")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttlf_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttlf_node.maxxval = 0.49
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttZZ_ttlf_node)
    
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le6j_le4t_90GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==4))")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==4))","ljets_le6j_le4t_90GeV_ttZZ_ttHH_node","")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttHH_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttHH_node.maxxval = 0.47
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttZZ_ttHH_node)
    
    interf_ljets_le6j_le4t_90GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le6j_le4t_90GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==5))")
    interf_ljets_le6j_le4t_90GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==5))","ljets_le6j_le4t_90GeV_ttZZ_tt4b_node","")
    interf_ljets_le6j_le4t_90GeV_ttZZ_tt4b_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le6j_le4t_90GeV_ttZZ_tt4b_node.maxxval = 0.5
    interf_ljets_le6j_le4t_90GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttZZ_tt4b_node)
    
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le4t_90GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le6j_le4t_90GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==6))")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=4)&&(1.)&&(DNNPredictedClass_le6j_le4t_90GeV_ttZZ==6))","ljets_le6j_le4t_90GeV_ttZZ_ttzz_node","")
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttzz_node.category_label = "\leq 6 jets, \leq 4 b-tags"
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttzz_node.maxxval = 0.49
    interf_ljets_le6j_le4t_90GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le4t_90GeV_ttZZ_ttzz_node)
    


    # plots for le6j_le3t_30GeV

    interf_ljets_le6j_le3t_30GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_node_ttH",
                                            label          = "ljets_le6j_le3t_30GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==0))")
    interf_ljets_le6j_le3t_30GeV_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==0))","ljets_le6j_le3t_30GeV_ttH_node","")
    interf_ljets_le6j_le3t_30GeV_ttH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttH_node.minxval = 0.17
    interf_ljets_le6j_le3t_30GeV_ttH_node.maxxval = 0.37
    interf_ljets_le6j_le3t_30GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttH_node)
    
    interf_ljets_le6j_le3t_30GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_node_ttbb",
                                            label          = "ljets_le6j_le3t_30GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==1))")
    interf_ljets_le6j_le3t_30GeV_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==1))","ljets_le6j_le3t_30GeV_ttbb_node","")
    interf_ljets_le6j_le3t_30GeV_ttbb_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttbb_node.minxval = 0.17
    interf_ljets_le6j_le3t_30GeV_ttbb_node.maxxval = 0.41
    interf_ljets_le6j_le3t_30GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttbb_node)
    
    interf_ljets_le6j_le3t_30GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_node_ttcc",
                                            label          = "ljets_le6j_le3t_30GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==2))")
    interf_ljets_le6j_le3t_30GeV_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==2))","ljets_le6j_le3t_30GeV_ttcc_node","")
    interf_ljets_le6j_le3t_30GeV_ttcc_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttcc_node.minxval = 0.17
    interf_ljets_le6j_le3t_30GeV_ttcc_node.maxxval = 0.46
    interf_ljets_le6j_le3t_30GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttcc_node)
    
    interf_ljets_le6j_le3t_30GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_node_ttlf",
                                            label          = "ljets_le6j_le3t_30GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==3))")
    interf_ljets_le6j_le3t_30GeV_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==3))","ljets_le6j_le3t_30GeV_ttlf_node","")
    interf_ljets_le6j_le3t_30GeV_ttlf_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttlf_node.minxval = 0.17
    interf_ljets_le6j_le3t_30GeV_ttlf_node.maxxval = 0.53
    interf_ljets_le6j_le3t_30GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttlf_node)
    
    interf_ljets_le6j_le3t_30GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_node_ttHH",
                                            label          = "ljets_le6j_le3t_30GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==4))")
    interf_ljets_le6j_le3t_30GeV_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==4))","ljets_le6j_le3t_30GeV_ttHH_node","")
    interf_ljets_le6j_le3t_30GeV_ttHH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttHH_node.minxval = 0.17
    interf_ljets_le6j_le3t_30GeV_ttHH_node.maxxval = 0.58
    interf_ljets_le6j_le3t_30GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttHH_node)
    
    interf_ljets_le6j_le3t_30GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_node_tt4b",
                                            label          = "ljets_le6j_le3t_30GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==5))")
    interf_ljets_le6j_le3t_30GeV_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV==5))","ljets_le6j_le3t_30GeV_tt4b_node","")
    interf_ljets_le6j_le3t_30GeV_tt4b_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_tt4b_node.minxval = 0.17
    interf_ljets_le6j_le3t_30GeV_tt4b_node.maxxval = 0.54
    interf_ljets_le6j_le3t_30GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_tt4b_node)
    


    # plots for le6j_le3t_60GeV

    interf_ljets_le6j_le3t_60GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_node_ttH",
                                            label          = "ljets_le6j_le3t_60GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==0))")
    interf_ljets_le6j_le3t_60GeV_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==0))","ljets_le6j_le3t_60GeV_ttH_node","")
    interf_ljets_le6j_le3t_60GeV_ttH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttH_node.minxval = 0.17
    interf_ljets_le6j_le3t_60GeV_ttH_node.maxxval = 0.4
    interf_ljets_le6j_le3t_60GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttH_node)
    
    interf_ljets_le6j_le3t_60GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_node_ttbb",
                                            label          = "ljets_le6j_le3t_60GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==1))")
    interf_ljets_le6j_le3t_60GeV_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==1))","ljets_le6j_le3t_60GeV_ttbb_node","")
    interf_ljets_le6j_le3t_60GeV_ttbb_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttbb_node.minxval = 0.17
    interf_ljets_le6j_le3t_60GeV_ttbb_node.maxxval = 0.38
    interf_ljets_le6j_le3t_60GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttbb_node)
    
    interf_ljets_le6j_le3t_60GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_node_ttcc",
                                            label          = "ljets_le6j_le3t_60GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==2))")
    interf_ljets_le6j_le3t_60GeV_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==2))","ljets_le6j_le3t_60GeV_ttcc_node","")
    interf_ljets_le6j_le3t_60GeV_ttcc_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttcc_node.minxval = 0.17
    interf_ljets_le6j_le3t_60GeV_ttcc_node.maxxval = 0.46
    interf_ljets_le6j_le3t_60GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttcc_node)
    
    interf_ljets_le6j_le3t_60GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_node_ttlf",
                                            label          = "ljets_le6j_le3t_60GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==3))")
    interf_ljets_le6j_le3t_60GeV_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==3))","ljets_le6j_le3t_60GeV_ttlf_node","")
    interf_ljets_le6j_le3t_60GeV_ttlf_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttlf_node.minxval = 0.17
    interf_ljets_le6j_le3t_60GeV_ttlf_node.maxxval = 0.51
    interf_ljets_le6j_le3t_60GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttlf_node)
    
    interf_ljets_le6j_le3t_60GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_node_ttHH",
                                            label          = "ljets_le6j_le3t_60GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==4))")
    interf_ljets_le6j_le3t_60GeV_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==4))","ljets_le6j_le3t_60GeV_ttHH_node","")
    interf_ljets_le6j_le3t_60GeV_ttHH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttHH_node.minxval = 0.17
    interf_ljets_le6j_le3t_60GeV_ttHH_node.maxxval = 0.56
    interf_ljets_le6j_le3t_60GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttHH_node)
    
    interf_ljets_le6j_le3t_60GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_node_tt4b",
                                            label          = "ljets_le6j_le3t_60GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==5))")
    interf_ljets_le6j_le3t_60GeV_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV==5))","ljets_le6j_le3t_60GeV_tt4b_node","")
    interf_ljets_le6j_le3t_60GeV_tt4b_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_tt4b_node.minxval = 0.17
    interf_ljets_le6j_le3t_60GeV_tt4b_node.maxxval = 0.55
    interf_ljets_le6j_le3t_60GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_tt4b_node)
    


    # plots for le6j_le3t_90GeV

    interf_ljets_le6j_le3t_90GeV_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_node_ttH",
                                            label          = "ljets_le6j_le3t_90GeV_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==0))")
    interf_ljets_le6j_le3t_90GeV_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==0))","ljets_le6j_le3t_90GeV_ttH_node","")
    interf_ljets_le6j_le3t_90GeV_ttH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttH_node.minxval = 0.17
    interf_ljets_le6j_le3t_90GeV_ttH_node.maxxval = 0.39
    interf_ljets_le6j_le3t_90GeV_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttH_node)
    
    interf_ljets_le6j_le3t_90GeV_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_node_ttbb",
                                            label          = "ljets_le6j_le3t_90GeV_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==1))")
    interf_ljets_le6j_le3t_90GeV_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==1))","ljets_le6j_le3t_90GeV_ttbb_node","")
    interf_ljets_le6j_le3t_90GeV_ttbb_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttbb_node.minxval = 0.17
    interf_ljets_le6j_le3t_90GeV_ttbb_node.maxxval = 0.39
    interf_ljets_le6j_le3t_90GeV_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttbb_node)
    
    interf_ljets_le6j_le3t_90GeV_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_node_ttcc",
                                            label          = "ljets_le6j_le3t_90GeV_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==2))")
    interf_ljets_le6j_le3t_90GeV_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==2))","ljets_le6j_le3t_90GeV_ttcc_node","")
    interf_ljets_le6j_le3t_90GeV_ttcc_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttcc_node.minxval = 0.17
    interf_ljets_le6j_le3t_90GeV_ttcc_node.maxxval = 0.48
    interf_ljets_le6j_le3t_90GeV_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttcc_node)
    
    interf_ljets_le6j_le3t_90GeV_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_node_ttlf",
                                            label          = "ljets_le6j_le3t_90GeV_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==3))")
    interf_ljets_le6j_le3t_90GeV_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==3))","ljets_le6j_le3t_90GeV_ttlf_node","")
    interf_ljets_le6j_le3t_90GeV_ttlf_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttlf_node.minxval = 0.17
    interf_ljets_le6j_le3t_90GeV_ttlf_node.maxxval = 0.42
    interf_ljets_le6j_le3t_90GeV_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttlf_node)
    
    interf_ljets_le6j_le3t_90GeV_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_node_ttHH",
                                            label          = "ljets_le6j_le3t_90GeV_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==4))")
    interf_ljets_le6j_le3t_90GeV_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==4))","ljets_le6j_le3t_90GeV_ttHH_node","")
    interf_ljets_le6j_le3t_90GeV_ttHH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttHH_node.minxval = 0.17
    interf_ljets_le6j_le3t_90GeV_ttHH_node.maxxval = 0.51
    interf_ljets_le6j_le3t_90GeV_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttHH_node)
    
    interf_ljets_le6j_le3t_90GeV_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_node_tt4b",
                                            label          = "ljets_le6j_le3t_90GeV_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==5))")
    interf_ljets_le6j_le3t_90GeV_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV==5))","ljets_le6j_le3t_90GeV_tt4b_node","")
    interf_ljets_le6j_le3t_90GeV_tt4b_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_tt4b_node.minxval = 0.17
    interf_ljets_le6j_le3t_90GeV_tt4b_node.maxxval = 0.5
    interf_ljets_le6j_le3t_90GeV_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_tt4b_node)
    


    # plots for le6j_le3t_30GeV_ttZZ

    interf_ljets_le6j_le3t_30GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_ttZZ_node_ttH",
                                            label          = "ljets_le6j_le3t_30GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==0))")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==0))","ljets_le6j_le3t_30GeV_ttZZ_ttH_node","")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttH_node.maxxval = 0.29
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttZZ_ttH_node)
    
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le6j_le3t_30GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==1))")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==1))","ljets_le6j_le3t_30GeV_ttZZ_ttbb_node","")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttbb_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttbb_node.maxxval = 0.35
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttZZ_ttbb_node)
    
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le6j_le3t_30GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==2))")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==2))","ljets_le6j_le3t_30GeV_ttZZ_ttcc_node","")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttcc_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttcc_node.maxxval = 0.44
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttZZ_ttcc_node)
    
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le6j_le3t_30GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==3))")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==3))","ljets_le6j_le3t_30GeV_ttZZ_ttlf_node","")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttlf_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttlf_node.maxxval = 0.52
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttZZ_ttlf_node)
    
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le6j_le3t_30GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==4))")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==4))","ljets_le6j_le3t_30GeV_ttZZ_ttHH_node","")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttHH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttHH_node.maxxval = 0.39
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttZZ_ttHH_node)
    
    interf_ljets_le6j_le3t_30GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le6j_le3t_30GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==5))")
    interf_ljets_le6j_le3t_30GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==5))","ljets_le6j_le3t_30GeV_ttZZ_tt4b_node","")
    interf_ljets_le6j_le3t_30GeV_ttZZ_tt4b_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le6j_le3t_30GeV_ttZZ_tt4b_node.maxxval = 0.5
    interf_ljets_le6j_le3t_30GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttZZ_tt4b_node)
    
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_30GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le6j_le3t_30GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==6))")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=30)&&(Jet_Pt[1]>=30)&&(Jet_Pt[2]>=30)&&(Jet_Pt[3]>=30)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_30GeV_ttZZ==6))","ljets_le6j_le3t_30GeV_ttZZ_ttzz_node","")
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttzz_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttzz_node.maxxval = 0.51
    interf_ljets_le6j_le3t_30GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_30GeV_ttZZ_ttzz_node)
    


    # plots for le6j_le3t_60GeV_ttZZ

    interf_ljets_le6j_le3t_60GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_ttZZ_node_ttH",
                                            label          = "ljets_le6j_le3t_60GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==0))")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==0))","ljets_le6j_le3t_60GeV_ttZZ_ttH_node","")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttH_node.maxxval = 0.33
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttZZ_ttH_node)
    
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le6j_le3t_60GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==1))")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==1))","ljets_le6j_le3t_60GeV_ttZZ_ttbb_node","")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttbb_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttbb_node.maxxval = 0.31
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttZZ_ttbb_node)
    
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le6j_le3t_60GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==2))")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==2))","ljets_le6j_le3t_60GeV_ttZZ_ttcc_node","")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttcc_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttcc_node.maxxval = 0.48
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttZZ_ttcc_node)
    
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le6j_le3t_60GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==3))")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==3))","ljets_le6j_le3t_60GeV_ttZZ_ttlf_node","")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttlf_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttlf_node.maxxval = 0.48
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttZZ_ttlf_node)
    
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le6j_le3t_60GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==4))")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==4))","ljets_le6j_le3t_60GeV_ttZZ_ttHH_node","")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttHH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttHH_node.maxxval = 0.35
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttZZ_ttHH_node)
    
    interf_ljets_le6j_le3t_60GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le6j_le3t_60GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==5))")
    interf_ljets_le6j_le3t_60GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==5))","ljets_le6j_le3t_60GeV_ttZZ_tt4b_node","")
    interf_ljets_le6j_le3t_60GeV_ttZZ_tt4b_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le6j_le3t_60GeV_ttZZ_tt4b_node.maxxval = 0.52
    interf_ljets_le6j_le3t_60GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttZZ_tt4b_node)
    
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_60GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le6j_le3t_60GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==6))")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=60)&&(Jet_Pt[1]>=60)&&(Jet_Pt[2]>=60)&&(Jet_Pt[3]>=60)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_60GeV_ttZZ==6))","ljets_le6j_le3t_60GeV_ttZZ_ttzz_node","")
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttzz_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttzz_node.maxxval = 0.57
    interf_ljets_le6j_le3t_60GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_60GeV_ttZZ_ttzz_node)
    


    # plots for le6j_le3t_90GeV_ttZZ

    interf_ljets_le6j_le3t_90GeV_ttZZ_ttH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_ttZZ_node_ttH",
                                            label          = "ljets_le6j_le3t_90GeV_ttZZ_ttH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==0))")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==0))","ljets_le6j_le3t_90GeV_ttZZ_ttH_node","")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttH_node.minxval = 0.14
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttH_node.maxxval = 0.29
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttZZ_ttH_node)
    
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttbb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_ttZZ_node_ttbb",
                                            label          = "ljets_le6j_le3t_90GeV_ttZZ_ttbb_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==1))")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttbb_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==1))","ljets_le6j_le3t_90GeV_ttZZ_ttbb_node","")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttbb_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttbb_node.minxval = 0.14
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttbb_node.maxxval = 0.33
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttbb_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttZZ_ttbb_node)
    
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_ttZZ_node_ttcc",
                                            label          = "ljets_le6j_le3t_90GeV_ttZZ_ttcc_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==2))")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttcc_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==2))","ljets_le6j_le3t_90GeV_ttZZ_ttcc_node","")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttcc_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttcc_node.minxval = 0.14
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttcc_node.maxxval = 0.41
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttcc_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttZZ_ttcc_node)
    
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_ttZZ_node_ttlf",
                                            label          = "ljets_le6j_le3t_90GeV_ttZZ_ttlf_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==3))")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttlf_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==3))","ljets_le6j_le3t_90GeV_ttZZ_ttlf_node","")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttlf_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttlf_node.minxval = 0.14
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttlf_node.maxxval = 0.45
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttlf_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttZZ_ttlf_node)
    
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttHH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_ttZZ_node_ttHH",
                                            label          = "ljets_le6j_le3t_90GeV_ttZZ_ttHH_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==4))")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttHH_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==4))","ljets_le6j_le3t_90GeV_ttZZ_ttHH_node","")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttHH_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttHH_node.minxval = 0.14
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttHH_node.maxxval = 0.35
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttHH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttZZ_ttHH_node)
    
    interf_ljets_le6j_le3t_90GeV_ttZZ_tt4b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_ttZZ_node_tt4b",
                                            label          = "ljets_le6j_le3t_90GeV_ttZZ_tt4b_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==5))")
    interf_ljets_le6j_le3t_90GeV_ttZZ_tt4b_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==5))","ljets_le6j_le3t_90GeV_ttZZ_tt4b_node","")
    interf_ljets_le6j_le3t_90GeV_ttZZ_tt4b_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttZZ_tt4b_node.minxval = 0.14
    interf_ljets_le6j_le3t_90GeV_ttZZ_tt4b_node.maxxval = 0.43
    interf_ljets_le6j_le3t_90GeV_ttZZ_tt4b_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttZZ_tt4b_node)
    
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttzz_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_le6j_le3t_90GeV_ttZZ_node_ttzz",
                                            label          = "ljets_le6j_le3t_90GeV_ttZZ_ttzz_node",
                                            selection      = "((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==6))")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttzz_node.category = ("((Jet_Pt[0]>=90)&&(Jet_Pt[1]>=90)&&(Jet_Pt[2]>=90)&&(Jet_Pt[3]>=90)&&(N_Jets<=6&&N_BTagsM<=3)&&(1.)&&(DNNPredictedClass_le6j_le3t_90GeV_ttZZ==6))","ljets_le6j_le3t_90GeV_ttZZ_ttzz_node","")
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttzz_node.category_label = "\leq 6 jets, \leq 3 b-tags"
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttzz_node.minxval = 0.14
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttzz_node.maxxval = 0.43
    interf_ljets_le6j_le3t_90GeV_ttZZ_ttzz_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_le6j_le3t_90GeV_ttZZ_ttzz_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l if not discrname == "" else l 
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_le5j_le3t_30GeV(data)
    discriminatorPlots += plots_le5j_le3t_60GeV(data)
    discriminatorPlots += plots_le5j_le3t_90GeV(data)
    discriminatorPlots += plots_le5j_le3t_30GeV_ttZZ(data)
    discriminatorPlots += plots_le5j_le3t_60GeV_ttZZ(data)
    discriminatorPlots += plots_le5j_le3t_90GeV_ttZZ(data)
    discriminatorPlots += plots_le7j_le3t_30GeV(data)
    discriminatorPlots += plots_le7j_le3t_60GeV(data)
    discriminatorPlots += plots_le7j_le3t_90GeV(data)
    discriminatorPlots += plots_le7j_le3t_30GeV_ttZZ(data)
    discriminatorPlots += plots_le7j_le3t_60GeV_ttZZ(data)
    discriminatorPlots += plots_le7j_le3t_90GeV_ttZZ(data)
    discriminatorPlots += plots_le7j_le4t_30GeV(data)
    discriminatorPlots += plots_le7j_le4t_60GeV(data)
    discriminatorPlots += plots_le7j_le4t_90GeV(data)
    discriminatorPlots += plots_le7j_le4t_30GeV_ttZZ(data)
    discriminatorPlots += plots_le7j_le4t_60GeV_ttZZ(data)
    discriminatorPlots += plots_le7j_le4t_90GeV_ttZZ(data)
    discriminatorPlots += plots_le5j_le4t_30GeV(data)
    discriminatorPlots += plots_le5j_le4t_60GeV(data)
    discriminatorPlots += plots_le5j_le4t_90GeV(data)
    discriminatorPlots += plots_le5j_le4t_30GeV_ttZZ(data)
    discriminatorPlots += plots_le5j_le4t_60GeV_ttZZ(data)
    discriminatorPlots += plots_le5j_le4t_90GeV_ttZZ(data)
    discriminatorPlots += plots_le6j_le4t_30GeV(data)
    discriminatorPlots += plots_le6j_le4t_60GeV(data)
    discriminatorPlots += plots_le6j_le4t_90GeV(data)
    discriminatorPlots += plots_le6j_le4t_30GeV_ttZZ(data)
    discriminatorPlots += plots_le6j_le4t_60GeV_ttZZ(data)
    discriminatorPlots += plots_le6j_le4t_90GeV_ttZZ(data)
    discriminatorPlots += plots_le6j_le3t_30GeV(data)
    discriminatorPlots += plots_le6j_le3t_60GeV(data)
    discriminatorPlots += plots_le6j_le3t_90GeV(data)
    discriminatorPlots += plots_le6j_le3t_30GeV_ttZZ(data)
    discriminatorPlots += plots_le6j_le3t_60GeV_ttZZ(data)
    discriminatorPlots += plots_le6j_le3t_90GeV_ttZZ(data)
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
    