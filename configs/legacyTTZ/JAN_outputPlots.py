
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

    
def plots_ge6j_ge3t(data = None):
    label = "\geq 6 jets, \geq 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=6&&N_BTagsM>=3)&&(1.)"

    plots = [
        #####################################################################################################################################################################################################
        # Z variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnZ_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnZ_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnZ_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnZ_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnZ_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnZ_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnZ_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnZ_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnZ_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnZ_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnZ_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnZ_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_E","reconstructed Z boson energy / GeV",50,40.,1200.),"dnnZ_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_Eta","reconstructed Z boson #eta",50,-4.,4.),"dnnZ_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_M","reconstructed Z boson mass / GeV",50,40.,180.),"dnnZ_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_Pt","reconstructed Z boson p_{T} / GeV",50,0.,450.),"dnnZ_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnZ_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnZ_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnZ_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnZ_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnZ_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnZ_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnZ_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnZ_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnZ_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnZ_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnZ_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnZ_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnZ_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnZ_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnZ_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnZ_ft_TightLepton_Pt_0",selection,label),

        #transformed Outputs
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_DNNOutput","Z boson reconstruction DNN output",50,0.,1.0),"dnnZ_ft_RecoX_DNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnZ_ft_RecoX_transformedDNNOutput","transformed Z boson reconstruction DNN output",50,-5.,5.0),"dnnZ_ft_RecoX_transformedDNNOutput",selection,label),




        #####################################################################################################################################################################################################
        # Higgs variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnH_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnH_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnH_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnH_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnH_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnH_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnH_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnH_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnH_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnH_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnH_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnH_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_E","reconstructed Higgs boson energy / GeV",50,40.,1200.),"dnnH_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_Eta","reconstructed Higgs boson #eta",50,-4.,4.),"dnnH_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_M","reconstructed Higgs boson mass / GeV",50,40.,180.),"dnnH_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_Pt","reconstructed Higgs boson p_{T} / GeV",50,0.,450.),"dnnH_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnH_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnH_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnH_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnH_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnH_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnH_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnH_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnH_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnH_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnH_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnH_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnH_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnH_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnH_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnH_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnH_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnH_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnH_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnH_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnH_ft_TightLepton_Pt_0",selection,label),

        #transformed Outputs
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_DNNOutput","Higgs boson reconstruction DNN output",50,0.,1.0),"dnnH_ft_RecoX_DNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnH_ft_RecoX_transformedDNNOutput","transformed Higgs boson reconstruction DNN output",50,-5.,5.0),"dnnH_ft_RecoX_transformedDNNOutput",selection,label),



        #####################################################################################################################################################################################################
        # cc variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnncc_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnncc_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnncc_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnncc_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnncc_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnncc_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnncc_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnncc_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnncc_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnncc_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnncc_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnncc_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnncc_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnncc_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnncc_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnncc_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnncc_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnncc_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnncc_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnncc_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnncc_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnncc_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnncc_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnncc_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnncc_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnncc_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnncc_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnncc_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnncc_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnncc_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnncc_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnncc_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnncc_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnncc_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnncc_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnncc_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnncc_ft_TightLepton_Pt_0",selection,label),

        
        #####################################################################################################################################################################################################
        # bb variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnbb_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnbb_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnbb_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnbb_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnbb_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnbb_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnbb_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnbb_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnbb_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnbb_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnbb_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnbb_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnnbb_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnnbb_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnnbb_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnnbb_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnbb_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnbb_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnbb_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnbb_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnbb_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnbb_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnbb_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnbb_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnbb_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnbb_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnbb_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnbb_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnbb_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnbb_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnbb_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnbb_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnbb_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnbb_ft_TightLepton_Pt_0",selection,label),


        
        #####################################################################################################################################################################################################
        # ttTobb variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnttTobb_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnttTobb_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnttTobb_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnttTobb_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnttTobb_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnttTobb_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnttTobb_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnttTobb_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnttTobb_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnttTobb_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnttTobb_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnttTobb_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnnttTobb_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnnttTobb_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnnttTobb_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnnttTobb_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnttTobb_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnttTobb_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnttTobb_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnttTobb_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnttTobb_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnttTobb_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnttTobb_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnttTobb_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnttTobb_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnttTobb_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnttTobb_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnttTobb_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnttTobb_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnttTobb_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge6j_ge3t_dnnttTobb_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnttTobb_ft_TightLepton_Pt_0",selection,label),

        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def plots_5j_ge3t(data = None):
    label = "5 jets, \geq 3 b-tags"
    interfaces = []
    selection = "(N_Jets==5&&N_BTagsM>=3)&&(1.)"

    plots = [
        #####################################################################################################################################################################################################
        # Z variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnZ_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnZ_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnZ_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnZ_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnZ_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnZ_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnZ_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnZ_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnZ_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnZ_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnZ_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnZ_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_E","reconstructed Z boson energy / GeV",50,40.,1200.),"dnnZ_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_Eta","reconstructed Z boson #eta",50,-4.,4.),"dnnZ_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_M","reconstructed Z boson mass / GeV",50,40.,180.),"dnnZ_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_Pt","reconstructed Z boson p_{T} / GeV",50,0.,450.),"dnnZ_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnZ_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnZ_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnZ_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnZ_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnZ_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnZ_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnZ_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnZ_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnZ_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnZ_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnZ_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnZ_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnZ_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnZ_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnZ_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnZ_ft_TightLepton_Pt_0",selection,label),

        #transformed Outputs
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_DNNOutput","Z boson reconstruction DNN output",50,0.,1.0),"dnnZ_ft_RecoX_DNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnZ_ft_RecoX_transformedDNNOutput","transformed Z boson reconstruction DNN output",50,-5.,5.0),"dnnZ_ft_RecoX_transformedDNNOutput",selection,label),




        #####################################################################################################################################################################################################
        # Higgs variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnH_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnH_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnH_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnH_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnH_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnH_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnH_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnH_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnH_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnH_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnH_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnH_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_E","reconstructed Higgs boson energy / GeV",50,40.,1200.),"dnnH_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_Eta","reconstructed Higgs boson #eta",50,-4.,4.),"dnnH_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_M","reconstructed Higgs boson mass / GeV",50,40.,180.),"dnnH_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_Pt","reconstructed Higgs boson p_{T} / GeV",50,0.,450.),"dnnH_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnH_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnH_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnH_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnH_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnH_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnH_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnH_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnH_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnH_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnH_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnH_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnH_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnH_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnH_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnH_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnH_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnH_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnH_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnH_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnH_ft_TightLepton_Pt_0",selection,label),

        #transformed Outputs
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_DNNOutput","Higgs boson reconstruction DNN output",50,0.,1.0),"dnnH_ft_RecoX_DNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnH_ft_RecoX_transformedDNNOutput","transformed Higgs boson reconstruction DNN output",50,-5.,5.0),"dnnH_ft_RecoX_transformedDNNOutput",selection,label),



        #####################################################################################################################################################################################################
        # cc variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnncc_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnncc_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnncc_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnncc_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnncc_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnncc_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnncc_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnncc_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnncc_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnncc_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnncc_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnncc_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnncc_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnncc_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnncc_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnncc_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnncc_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnncc_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnncc_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnncc_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnncc_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnncc_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnncc_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnncc_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnncc_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnncc_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnncc_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnncc_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnncc_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnncc_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnncc_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnncc_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnncc_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnncc_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnncc_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnncc_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnncc_ft_TightLepton_Pt_0",selection,label),

        
        #####################################################################################################################################################################################################
        # bb variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnbb_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnbb_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnbb_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnbb_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnbb_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnbb_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnbb_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnbb_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnbb_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnbb_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnbb_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnbb_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnnbb_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnnbb_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnnbb_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnnbb_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnbb_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnbb_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnbb_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnbb_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnbb_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnbb_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnbb_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnbb_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnbb_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnbb_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnbb_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnbb_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnbb_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnbb_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnbb_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnbb_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnbb_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnbb_ft_TightLepton_Pt_0",selection,label),


        
        #####################################################################################################################################################################################################
        # ttTobb variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnttTobb_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnttTobb_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnttTobb_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnttTobb_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnttTobb_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnttTobb_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnttTobb_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnttTobb_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnttTobb_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnttTobb_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnttTobb_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnttTobb_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnnttTobb_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnnttTobb_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnnttTobb_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnnttTobb_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnttTobb_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnttTobb_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnttTobb_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnttTobb_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnttTobb_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnttTobb_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnttTobb_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnttTobb_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnttTobb_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnttTobb_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnttTobb_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnttTobb_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnttTobb_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnttTobb_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_5j_ge3t_dnnttTobb_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnttTobb_ft_TightLepton_Pt_0",selection,label),

        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def plots_4j_ge3t(data = None):
    label = "4 jets, \geq 3 b-tags"
    interfaces = []
    selection = "(N_Jets==4&&N_BTagsM>=3)&&(1.)"

    plots = [
        #####################################################################################################################################################################################################
        # Z variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnZ_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnZ_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnZ_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnZ_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnZ_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnZ_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnZ_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnZ_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnZ_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnZ_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnZ_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnZ_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_E","reconstructed Z boson energy / GeV",50,40.,1200.),"dnnZ_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_Eta","reconstructed Z boson #eta",50,-4.,4.),"dnnZ_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_M","reconstructed Z boson mass / GeV",50,40.,180.),"dnnZ_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_Pt","reconstructed Z boson p_{T} / GeV",50,0.,450.),"dnnZ_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnZ_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnZ_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnZ_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnZ_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnZ_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnZ_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnZ_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnZ_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnZ_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnZ_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnZ_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnZ_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnZ_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnZ_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnZ_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnZ_ft_TightLepton_Pt_0",selection,label),

        #transformed Outputs
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_DNNOutput","Z boson reconstruction DNN output",50,0.,1.0),"dnnZ_ft_RecoX_DNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnZ_ft_RecoX_transformedDNNOutput","transformed Z boson reconstruction DNN output",50,-5.,5.0),"dnnZ_ft_RecoX_transformedDNNOutput",selection,label),




        #####################################################################################################################################################################################################
        # Higgs variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnH_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnH_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnH_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnH_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnH_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnH_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnH_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnH_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnH_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnH_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnH_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnH_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_E","reconstructed Higgs boson energy / GeV",50,40.,1200.),"dnnH_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_Eta","reconstructed Higgs boson #eta",50,-4.,4.),"dnnH_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_M","reconstructed Higgs boson mass / GeV",50,40.,180.),"dnnH_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_Pt","reconstructed Higgs boson p_{T} / GeV",50,0.,450.),"dnnH_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnH_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnH_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnH_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnH_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnH_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnH_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnH_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnH_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnH_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnH_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnH_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnH_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnH_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnH_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnH_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnH_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnH_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnH_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnH_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnH_ft_TightLepton_Pt_0",selection,label),

        #transformed Outputs
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_DNNOutput","Higgs boson reconstruction DNN output",50,0.,1.0),"dnnH_ft_RecoX_DNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnH_ft_RecoX_transformedDNNOutput","transformed Higgs boson reconstruction DNN output",50,-5.,5.0),"dnnH_ft_RecoX_transformedDNNOutput",selection,label),



        #####################################################################################################################################################################################################
        # cc variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnncc_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnncc_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnncc_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnncc_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnncc_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnncc_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnncc_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnncc_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnncc_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnncc_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnncc_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnncc_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnncc_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnncc_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnncc_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnncc_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnncc_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnncc_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnncc_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnncc_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnncc_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnncc_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnncc_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnncc_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnncc_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnncc_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnncc_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnncc_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnncc_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnncc_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnncc_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnncc_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnncc_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnncc_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnncc_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnncc_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnncc_ft_TightLepton_Pt_0",selection,label),

        
        #####################################################################################################################################################################################################
        # bb variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnbb_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnbb_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnbb_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnbb_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnbb_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnbb_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnbb_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnbb_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnbb_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnbb_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnbb_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnbb_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnnbb_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnnbb_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnnbb_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnnbb_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnbb_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnbb_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnbb_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnbb_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnbb_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnbb_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnbb_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnbb_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnbb_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnbb_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnbb_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnbb_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnbb_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnbb_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnbb_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnbb_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnbb_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnbb_ft_TightLepton_Pt_0",selection,label),


        
        #####################################################################################################################################################################################################
        # ttTobb variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnttTobb_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnttTobb_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnttTobb_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnttTobb_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnttTobb_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnttTobb_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnttTobb_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnttTobb_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnttTobb_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnttTobb_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnttTobb_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnttTobb_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnnttTobb_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnnttTobb_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnnttTobb_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnnttTobb_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnttTobb_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnttTobb_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnttTobb_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnttTobb_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnttTobb_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnttTobb_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnttTobb_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnttTobb_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnttTobb_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnttTobb_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnttTobb_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnttTobb_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnttTobb_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnttTobb_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_4j_ge3t_dnnttTobb_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnttTobb_ft_TightLepton_Pt_0",selection,label),

        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots


def plots_ge4j_ge3t(data = None):
    label = "\geq 4 jets, \geq 3 b-tags"
    interfaces = []
    selection = "(N_Jets>=4&&N_BTagsM>=3)&&(1.)"

    plots = [
        #####################################################################################################################################################################################################
        # Z variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnZ_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnZ_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnZ_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnZ_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnZ_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnZ_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnZ_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnZ_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnZ_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnZ_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnZ_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnZ_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_E","reconstructed Z boson energy / GeV",50,40.,1200.),"dnnZ_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_Eta","reconstructed Z boson #eta",50,-4.,4.),"dnnZ_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_M","reconstructed Z boson mass / GeV",50,40.,180.),"dnnZ_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_Pt","reconstructed Z boson p_{T} / GeV",50,0.,450.),"dnnZ_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnZ_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnZ_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnZ_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnZ_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnZ_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnZ_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnZ_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnZ_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnZ_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnZ_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnZ_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnZ_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnZ_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnZ_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnZ_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnZ_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnZ_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnZ_ft_TightLepton_Pt_0",selection,label),

        #transformed Outputs
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_DNNOutput","Z boson reconstruction DNN output",50,0.,1.0),"dnnZ_ft_RecoX_DNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnZ_ft_RecoX_transformedDNNOutput","transformed Z boson reconstruction DNN output",50,-5.,5.0),"dnnZ_ft_RecoX_transformedDNNOutput",selection,label),




        #####################################################################################################################################################################################################
        # Higgs variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnH_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnH_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnH_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnH_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnH_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnH_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnH_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnH_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnH_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnH_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnH_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnH_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_E","reconstructed Higgs boson energy / GeV",50,40.,1200.),"dnnH_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_Eta","reconstructed Higgs boson #eta",50,-4.,4.),"dnnH_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_M","reconstructed Higgs boson mass / GeV",50,40.,180.),"dnnH_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_Pt","reconstructed Higgs boson p_{T} / GeV",50,0.,450.),"dnnH_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnH_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnH_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnH_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnH_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnH_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnH_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnH_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnH_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnH_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnH_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnH_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnH_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnH_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnH_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnH_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnH_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnH_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnH_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnH_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnH_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnH_ft_TightLepton_Pt_0",selection,label),

        #transformed Outputs
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_DNNOutput","Higgs boson reconstruction DNN output",50,0.,1.0),"dnnH_ft_RecoX_DNNOutput",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnH_ft_RecoX_transformedDNNOutput","transformed Higgs boson reconstruction DNN output",50,-5.,5.0),"dnnH_ft_RecoX_transformedDNNOutput",selection,label),



        #####################################################################################################################################################################################################
        # cc variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnncc_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnncc_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnncc_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnncc_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnncc_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnncc_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnncc_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnncc_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnncc_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnncc_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnncc_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnncc_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnncc_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnncc_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnncc_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnncc_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnncc_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnncc_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnncc_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnncc_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnncc_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnncc_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnncc_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnncc_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnncc_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnncc_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnncc_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnncc_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnncc_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnncc_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnncc_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnncc_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnncc_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnncc_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnncc_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnncc_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnncc_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnncc_ft_TightLepton_Pt_0",selection,label),

        
        #####################################################################################################################################################################################################
        # bb variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnbb_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnbb_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnbb_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnbb_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_M","mass of first jet / GeV",50,5.,35.),"dnnbb_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnbb_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnbb_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,600.),"dnnbb_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnbb_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,250.),"dnnbb_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_M","mass of second jet / GeV",50,2.,35.),"dnnbb_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnbb_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnnbb_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnnbb_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnnbb_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnnbb_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnbb_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnbb_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnbb_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnbb_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,400.),"dnnbb_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.2,1.0),"dnnbb_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnbb_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnbb_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnbb_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnbb_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnbb_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnbb_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnbb_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnbb_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnbb_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnbb_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnbb_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnbb_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnbb_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnbb_ft_TightLepton_Pt_0",selection,label),


        
        #####################################################################################################################################################################################################
        # ttTobb variables
        #####################################################################################################################################################################################################
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_btagValue","btag value of first jet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_idx","index of first jet",10,0.0,9.0),"dnnttTobb_ft_RecoX_jet1_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_E","energy of first jet / GeV",50,30.,450.),"dnnttTobb_ft_RecoX_jet1_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_Eta","#eta of first jet",50,-2.4,2.4),"dnnttTobb_ft_RecoX_jet1_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_Pt","p_{T} of first jet / GeV",50,30.,250.),"dnnttTobb_ft_RecoX_jet1_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_M","mass of first jet / GeV",50,0.,35.),"dnnttTobb_ft_RecoX_jet1_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_Phi","#phi of first jet / GeV",50,-3.141,3.141),"dnnttTobb_ft_RecoX_jet1_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_btagValue","btag value of second jet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_btagValue",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_idx","index of second jet",10,0.0,9.0),"dnnttTobb_ft_RecoX_jet2_idx",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_E","energy of second jet / GeV",50,30.,900.),"dnnttTobb_ft_RecoX_jet2_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_Eta","#eta of second jet",50,-2.4,2.4),"dnnttTobb_ft_RecoX_jet2_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_Pt","p_{T} of second jet / GeV",50,30.,400.),"dnnttTobb_ft_RecoX_jet2_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_M","mass of second jet / GeV",50,0.,50.),"dnnttTobb_ft_RecoX_jet2_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_Phi","#phi of second jet / GeV",50,-3.141,3.141),"dnnttTobb_ft_RecoX_jet2_Phi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_E","reconstructed di-jet energy / GeV",50,40.,1200.),"dnnttTobb_ft_RecoX_X_E",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_Eta","reconstructed di-jet #eta",50,-4.,4.),"dnnttTobb_ft_RecoX_X_Eta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_M","reconstructed di-jet mass / GeV",50,40.,180.),"dnnttTobb_ft_RecoX_X_M",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_Pt","reconstructed di-jet p_{T} / GeV",50,0.,450.),"dnnttTobb_ft_RecoX_X_Pt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_openingAngle","opening angle of di-jet combination",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_openingAngle",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_dEta","#Delta#eta of di-jet combination",50,0.0,2.4),"dnnttTobb_ft_RecoX_X_dEta",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_dPhi","#Delta#phi of di-jet combination",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_dPhi",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_dR","#DeltaR of di-jet combination",50,0.4,3.6),"dnnttTobb_ft_RecoX_X_dR",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_dPt","#Deltap_{T} of di-jet combination / GeV",50,0.0,450.),"dnnttTobb_ft_RecoX_X_dPt",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_btagAverage","average of the two b-tag values",50,0.0,1.0),"dnnttTobb_ft_RecoX_X_btagAverage",selection,label),

        # tagging variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_CvsB_deepJet","jet1_CvsB_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_CvsL_deepJet","jet1_CvsL_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet1_CvsL_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_CvsB_deepJet","jet2_CvsB_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_CvsB_deepJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_CvsL_deepJet","jet2_CvsL_deepJet",50,0.0,1.0),"dnnttTobb_ft_RecoX_jet2_CvsL_deepJet",selection,label),

        #lepton realted variables
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_dEta_lept","#Delta#eta between first jet and lepton",50,0.0,4.7),"dnnttTobb_ft_RecoX_jet1_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_dEta_lept","#Delta#eta between second jet and lepton",50,0.0,4.),"dnnttTobb_ft_RecoX_jet2_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_dPhi_lept","#Delta#phi between first jet and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_jet1_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_dPhi_lept","#Delta#phi between second jet and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_jet2_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet1_dR_lept","#DeltaR between first jet and lepton",50,0.4,4.4),"dnnttTobb_ft_RecoX_jet1_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_jet2_dR_lept","#DeltaR between second jet and lepton",50,0.4,5.),"dnnttTobb_ft_RecoX_jet2_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_dEta_lept","#Delta#eta between di-jet combination and lepton",50,0.0,5.),"dnnttTobb_ft_RecoX_X_dEta_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_dPhi_lept","#Delta#phi between di-jet combination and lepton",50,0.0,3.141),"dnnttTobb_ft_RecoX_X_dPhi_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_RecoX_X_dR_lept","#DeltaR between di-jet combination and lepton",50,0.0,4.7),"dnnttTobb_ft_RecoX_X_dR_lept",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_TightLepton_E_0","lepton energy / GeV",50,0.,550.),"dnnttTobb_ft_TightLepton_E_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_TightLepton_Eta_0","lepton #eta",50,-2.4,2.4),"dnnttTobb_ft_TightLepton_Eta_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_TightLepton_M_0","lepton mass / GeV",50,-0.2,0.2),"dnnttTobb_ft_TightLepton_M_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_TightLepton_Phi_0","lepton #phi",50,3.141,3.141),"dnnttTobb_ft_TightLepton_Phi_0",selection,label),
        plotClasses.Plot(ROOT.TH1D("ljets_ge4j_ge3t_dnnttTobb_ft_TightLepton_Pt_0","lepton p_{T} / GeV",50,20.,300.),"dnnttTobb_ft_TightLepton_Pt_0",selection,label),

        ]


    if data:
        add_data_plots(plots=plots,data=data)
        return plots
    

    

def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_4j_ge3t(data)
    discriminatorPlots += plots_5j_ge3t(data)
    discriminatorPlots += plots_ge6j_ge3t(data)
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
    
