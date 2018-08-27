import sys
import os

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)
import util.tools.plotClasses as plotClasses
import ROOT

memexp = ""
# define event yield categories
def evtYieldCategories():
    return None

def add_inclusive():
    # inclusive category
    plotLabel = "#slash{E}_{T}>250 GeV"
    plotSelection = "1.*DeltaPhi_Jet_MET[0]>1."
    plotPrefix = "incl"

    plots = [
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_MET","#slash{E}_{T}",23,250.,1400.),"Evt_Pt_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_GenMET","Gen #slash{E}_{T}",50,0.,1500.),"Evt_Pt_GenMET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Phi_MET","MET #phi",20,-3.2,3.2),"Evt_Phi_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Pt","jet p_{T}",20,0.,500.),"Jet_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Pt_0","leading jet p_{T}",20,0.,500.),"Jet_Pt[0]",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Phi","jet #phi ",20,-3.2,3.2),"Jet_Phi",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Phi_0","leading jet #phi",20,-3.2,3.2),"Jet_Phi[0]",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"N_Jets","N_Jets",10,0.5,10.5),"N_Jets",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_CaloMET","#slash{E}_{T,Calo}",22,200.,1400.),"CaloMET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"CaloMET_PFMET_ratio","#slash{E}_{T,Calo} #slash{E}_{T,PF} ratio",20,0.,1.),"CaloMET_PFMET_ratio",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"DeltaPhi_MET_Jet","#Delta #phi (#slash{E}_{T},jet)",32,0.,3.2),"DeltaPhi_Jet_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Hadr_Recoil_Pt","Hadr. Recoil Pt",23,250.,1400.),"Hadr_Recoil_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Hadr_Recoil_Phi","Hadr. Recoil #phi",20,-3.2,3.2),"Hadr_Recoil_Phi",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_MET_T1","#slash{E}_{T} type1",23,250.,1400.),"Evt_Pt_MET_T1",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Z_Pt","Z p_{T}",20,0.,500.),"Z_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"W_Pt","W p_{T}",20,0.,500.),"W_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"BosonWeight","BosonWeight",20,0.,2.),"internalBosonWeight_nominal",plotSelection,plotLabel),
    ]

    return plots



def add_met300():
    # met300 category
    plotLabel = "#slash{E}_{T}>300 GeV"
    plotSelection = "(Evt_Pt_MET>300.)*(DeltaPhi_Jet_MET[0]>1.)"
    plotPrefix = "MET300"

    plots300 = [
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_MET","#slash{E}_{T}",23,250.,1400.),"Evt_Pt_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_GenMET","Gen #slash{E}_{T}",50,0.,1500.),"Evt_Pt_GenMET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Phi_MET","MET #phi",20,-3.2,3.2),"Evt_Phi_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Pt","jet p_{T}",20,0.,500.),"Jet_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Pt_0","leading jet p_{T}",20,0.,500.),"Jet_Pt[0]",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Phi","jet #phi ",20,-3.2,3.2),"Jet_Phi",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Phi_0","leading jet #phi",20,-3.2,3.2),"Jet_Phi[0]",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"N_Jets","N_Jets",10,0.5,10.5),"N_Jets",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_CaloMET","#slash{E}_{T,Calo}",22,200.,1400.),"CaloMET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"CaloMET_PFMET_ratio","#slash{E}_{T,Calo} #slash{E}_{T,PF} ratio",20,0.,1.),"CaloMET_PFMET_ratio",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"DeltaPhi_MET_Jet","#Delta #phi (#slash{E}_{T},jet)",32,0.,3.2),"DeltaPhi_Jet_MET",plotSelection,plotLabel),
        #Plot(ROOT.TH1F(plotPrefix+"_"+"Hadr_Recoil_Pt","Hadr. Recoil Pt",23,250.,1400.),"Hadr_Recoil_Pt",plotSelection,plotLabel),
        #Plot(ROOT.TH1F(plotPrefix+"_"+"Hadr_Recoil_Phi","Hadr. Recoil #phi",20,-3.2,3.2),"Hadr_Recoil_Phi",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_MET_T1","#slash{E}_{T} type1",23,250.,1400.),"Evt_Pt_MET_T1",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Z_Pt","Z p_{T}",20,0.,500.),"Z_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"W_Pt","W p_{T}",20,0.,500.),"W_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"BosonWeight","BosonWeight",20,0.,2.),"internalBosonWeight_nominal",plotSelection,plotLabel),
    ]

    return plots300




def add_met400():
    # met400 category
    plotLabel = "#slash{E}_{T}>400 GeV"
    plotSelection = "(Evt_Pt_MET>400.)*(DeltaPhi_Jet_MET[0]>1.)"
    plotPrefix = "MET400"

    plots400 = [
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_MET","#slash{E}_{T}",23,250.,1400.),"Evt_Pt_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_GenMET","Gen #slash{E}_{T}",50,0.,1500.),"Evt_Pt_GenMET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Phi_MET","MET #phi",20,-3.2,3.2),"Evt_Phi_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Pt","jet p_{T}",20,0.,500.),"Jet_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Pt_0","leading jet p_{T}",20,0.,500.),"Jet_Pt[0]",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Phi","jet #phi ",20,-3.2,3.2),"Jet_Phi",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Phi_0","leading jet #phi",20,-3.2,3.2),"Jet_Phi[0]",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"N_Jets","N_Jets",10,0.5,10.5),"N_Jets",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_CaloMET","#slash{E}_{T,Calo}",22,200.,1400.),"CaloMET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"CaloMET_PFMET_ratio","#slash{E}_{T,Calo} #slash{E}_{T,PF} ratio",20,0.,1.),"CaloMET_PFMET_ratio",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"DeltaPhi_MET_Jet","#Delta #phi (#slash{E}_{T},jet)",32,0.,3.2),"DeltaPhi_Jet_MET",plotSelection,plotLabel),
        #Plot(ROOT.TH1F(plotPrefix+"_"+"Hadr_Recoil_Pt","Hadr. Recoil Pt",23,250.,1400.),"Hadr_Recoil_Pt",plotSelection,plotLabel),
        #Plot(ROOT.TH1F(plotPrefix+"_"+"Hadr_Recoil_Phi","Hadr. Recoil #phi",20,-3.2,3.2),"Hadr_Recoil_Phi",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_MET_T1","#slash{E}_{T} type1",23,250.,1400.),"Evt_Pt_MET_T1",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Z_Pt","Z p_{T}",20,0.,500.),"Z_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"W_Pt","W p_{T}",20,0.,500.),"W_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"BosonWeight","BosonWeight",20,0.,2.),"internalBosonWeight_nominal",plotSelection,plotLabel),
    ]

    return plots400



def add_met500():
    # met500 category
    plotLabel = "#slash{E}_{T}>500 GeV"
    plotSelection = "(Evt_Pt_MET>500.)*(DeltaPhi_Jet_MET[0]>1.)"
    plotPrefix = "MET500"

    plots500 = [
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_MET","#slash{E}_{T}",23,250.,1400.),"Evt_Pt_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_GenMET","Gen #slash{E}_{T}",50,0.,1500.),"Evt_Pt_GenMET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Phi_MET","MET #phi",20,-3.2,3.2),"Evt_Phi_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Pt","jet p_{T}",20,0.,500.),"Jet_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Pt_0","leading jet p_{T}",20,0.,500.),"Jet_Pt[0]",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Phi","jet #phi ",20,-3.2,3.2),"Jet_Phi",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Phi_0","leading jet #phi",20,-3.2,3.2),"Jet_Phi[0]",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"N_Jets","N_Jets",10,0.5,10.5),"N_Jets",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_CaloMET","#slash{E}_{T,Calo}",22,200.,1400.),"CaloMET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"CaloMET_PFMET_ratio","#slash{E}_{T,Calo} #slash{E}_{T,PF} ratio",20,0.,1.),"CaloMET_PFMET_ratio",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"DeltaPhi_MET_Jet","#Delta #phi (#slash{E}_{T},jet)",32,0.,3.2),"DeltaPhi_Jet_MET",plotSelection,plotLabel),
        #Plot(ROOT.TH1F(plotPrefix+"_"+"Hadr_Recoil_Pt","Hadr. Recoil Pt",23,250.,1400.),"Hadr_Recoil_Pt",plotSelection,plotLabel),
        #Plot(ROOT.TH1F(plotPrefix+"_"+"Hadr_Recoil_Phi","Hadr. Recoil #phi",20,-3.2,3.2),"Hadr_Recoil_Phi",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_MET_T1","#slash{E}_{T} type1",23,250.,1400.),"Evt_Pt_MET_T1",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Z_Pt","Z p_{T}",20,0.,500.),"Z_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"W_Pt","W p_{T}",20,0.,500.),"W_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"BosonWeight","BosonWeight",20,0.,2.),"internalBosonWeight_nominal",plotSelection,plotLabel),
    ]
    
    return plots500




def add_met600():
    # met600 category
    plotLabel = "#slash{E}_{T}>600 GeV"
    plotSelection = "(Evt_Pt_MET>600.)*(DeltaPhi_Jet_MET[0]>1.)"
    plotPrefix = "MET600"

    plots54 = [
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_MET","#slash{E}_{T}",23,250.,1400.),"Evt_Pt_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_GenMET","Gen #slash{E}_{T}",50,0.,1000.),"Evt_Pt_GenMET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Phi_MET","MET #phi",20,-3.2,3.2),"Evt_Phi_MET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Pt","jet p_{T}",20,0.,500.),"Jet_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Pt_0","leading jet p_{T}",20,0.,500.),"Jet_Pt[0]",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Phi","jet #phi ",20,-3.2,3.2),"Jet_Phi",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Jet_Phi_0","leading jet #phi",20,-3.2,3.2),"Jet_Phi[0]",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"N_Jets","N_Jets",10,0.5,10.5),"N_Jets",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_CaloMET","#slash{E}_{T,Calo}",22,200.,1400.),"CaloMET",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"CaloMET_PFMET_ratio","#slash{E}_{T,Calo} #slash{E}_{T,PF} ratio",20,0.,1.),"CaloMET_PFMET_ratio",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"DeltaPhi_MET_Jet","#Delta #phi (#slash{E}_{T},jet)",32,0.,3.2),"DeltaPhi_Jet_MET",plotSelection,plotLabel),
        #Plot(ROOT.TH1F(plotPrefix+"_"+"Hadr_Recoil_Pt","Hadr. Recoil Pt",23,250.,1400.),"Hadr_Recoil_Pt",plotSelection,plotLabel),
        #Plot(ROOT.TH1F(plotPrefix+"_"+"Hadr_Recoil_Phi","Hadr. Recoil #phi",20,-3.2,3.2),"Hadr_Recoil_Phi",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Evt_Pt_MET_T1","#slash{E}_{T} type1",23,250.,1400.),"Evt_Pt_MET_T1",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"Z_Pt","Z p_{T}",20,0.,500.),"Z_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"W_Pt","W p_{T}",20,0.,500.),"W_Pt",plotSelection,plotLabel),
        Plot(ROOT.TH1F(plotPrefix+"_"+"BosonWeight","BosonWeight",20,0.,2.),"internalBosonWeight_nominal",plotSelection,plotLabel),
    ]
    
    return plots600

def getDiscriminatorPlots(data = None, discrname = None):
    discriminatorPlots = add_inclusive()
    discriminatorPlots += add_met300()
    discriminatorPlots += add_met400()
    discriminatorPlots += add_met500()
    discriminatorPlots += add_met600()

    return discriminatorPlots


