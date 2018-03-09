import sys
import os
import ROOT

sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')
sys.path.append('limittools')

from scriptgenerator import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import addRealData
from limittools import makeDatacards
#UPDATE
from limittools import makeDatacardsParallel
from limittools import calcLimits
from limittools import replaceQ2scale

from MonoJet_cfg import *

jobname = "MonoJet_Plots"

additionalvariables=[    "N_TightMuons","N_TightElectrons","Evt_Pt_PrimaryLepton","N_BTagsM",
                         "Jet_Pt", "Muon_Pt", "Electron_Pt",
                         "Jet_Eta", "Muon_Eta", "Electron_Eta",
                         "Muon_Pt_BeForeRC","Electron_Pt_BeforeRun2Calibration","Electron_Eta_Supercluster",
                         "Jet_CSV", "Jet_Flav", "N_Jets", "Jet_E", "Jet_Phi", "Jet_M",
                         "Weight_CSV","Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown","Weight_CSVHFStats1up","Weight_CSVHFStats1down",
                         "Weight_CSVLFStats1up","Weight_CSVLFStats1down","Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
                         "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down","Weight_pu69p2",
                         "Evt_E_PrimaryLepton","Evt_Phi_PrimaryLepton","Evt_Eta_PrimaryLepton","Evt_M_PrimaryLepton","GenEvt_I_TTPlusCC","GenEvt_I_TTPlusBB","Weight_GenValue"
                         ]
additionalvariables+=GetMEPDFadditionalVariablesList("/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/rate_factors_onlyinternal_powhegpythia.csv")


plotselection_inclusive = "1."
plotlabel_inclusive = "inclusive"
plotprefix = "incl"
plots_inclusive=[
    
        Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MET","MET_Pt",30,250.,1150.),"Evt_Pt_MET",plotselection_inclusive,plotlabel_inclusive),
        Plot(ROOT.TH1F(plotprefix+"Evt_Pt_GenMET","GenMET_Pt",50,0.,1500.),"Evt_Pt_GenMET",plotselection_inclusive,plotlabel_inclusive),
        Plot(ROOT.TH1F(plotprefix+"Evt_Phi_MET","MET #phi",20,-3.2,3.2),"Evt_Phi_MET",plotselection_inclusive,plotlabel_inclusive),
        Plot(ROOT.TH1F(plotprefix+"Jet_Pt","Jet Pt",20,0.,500.),"Jet_Pt",plotselection_inclusive,plotlabel_inclusive),
        Plot(ROOT.TH1F(plotprefix+"Jet_Pt_0","Jet Pt [0]",20,0.,500.),"Jet_Pt[0]",plotselection_inclusive,plotlabel_inclusive),
        Plot(ROOT.TH1F(plotprefix+"Jet_Phi","Jet Phi ",20,-3.2,3.2),"Jet_Phi",plotselection_inclusive,plotlabel_inclusive),
        Plot(ROOT.TH1F(plotprefix+"Jet_Phi_0","Jet Phi [0]",20,-3.2,3.2),"Jet_Phi[0]",plotselection_inclusive,plotlabel_inclusive),
    ]

plotselection_MET300 = "Evt_Pt_MET>300."
plotlabel_MET300 = "MET>300"
plotprefix = "MET300"
plots_MET300=[
    
        Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MET","MET_Pt",30,250.,1150.),"Evt_Pt_MET",plotselection_MET300,plotlabel_MET300),
        Plot(ROOT.TH1F(plotprefix+"Evt_Pt_GenMET","GenMET_Pt",50,0.,1500.),"Evt_Pt_GenMET",plotselection_MET300,plotlabel_MET300),
        Plot(ROOT.TH1F(plotprefix+"Evt_Phi_MET","MET #phi",20,-3.2,3.2),"Evt_Phi_MET",plotselection_MET300,plotlabel_MET300),
        Plot(ROOT.TH1F(plotprefix+"Jet_Pt","Jet Pt",20,0.,500.),"Jet_Pt",plotselection_MET300,plotlabel_MET300)
        
    ]

plotselection_MET400 = "Evt_Pt_MET>400."
plotlabel_MET400 = "MET>400"
plotprefix = "MET400"
plots_MET400=[
    
        Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MET","MET_Pt",30,250.,1150.),"Evt_Pt_MET",plotselection_MET400,plotlabel_MET400),
        Plot(ROOT.TH1F(plotprefix+"Evt_Pt_GenMET","GenMET_Pt",50,0.,1500.),"Evt_Pt_GenMET",plotselection_MET400,plotlabel_MET400),
        Plot(ROOT.TH1F(plotprefix+"Evt_Phi_MET","MET #phi",20,-3.2,3.2),"Evt_Phi_MET",plotselection_MET400,plotlabel_MET400),
        Plot(ROOT.TH1F(plotprefix+"Jet_Pt","Jet Pt",20,0.,500.),"Jet_Pt",plotselection_MET400,plotlabel_MET400)
        
    ]

plotselection_MET500 = "Evt_Pt_MET>500."
plotlabel_MET500 = "MET>500"
plotprefix = "MET500"
plots_MET500=[
    
        Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MET","MET_Pt",30,250.,1150.),"Evt_Pt_MET",plotselection_MET500,plotlabel_MET500),
        Plot(ROOT.TH1F(plotprefix+"Evt_Pt_GenMET","GenMET_Pt",50,0.,1500.),"Evt_Pt_GenMET",plotselection_MET500,plotlabel_MET500),
        Plot(ROOT.TH1F(plotprefix+"Evt_Phi_MET","MET #phi",20,-3.2,3.2),"Evt_Phi_MET",plotselection_MET500,plotlabel_MET500),
        Plot(ROOT.TH1F(plotprefix+"Jet_Pt","Jet Pt",20,0.,500.),"Jet_Pt",plotselection_MET400,plotlabel_MET500)
        
    ]

plotselection_MET600 = "Evt_Pt_MET>600."
plotlabel_MET600 = "MET>600"
plotprefix = "MET600"
plots_MET600=[
    
        Plot(ROOT.TH1F(plotprefix+"Evt_Pt_MET","MET_Pt",50,250.,1000.),"Evt_Pt_MET",plotselection_MET600,plotlabel_MET600),
        Plot(ROOT.TH1F(plotprefix+"Evt_Pt_GenMET","GenMET_Pt",50,0.,1000.),"Evt_Pt_GenMET",plotselection_MET600,plotlabel_MET600),
        Plot(ROOT.TH1F(plotprefix+"Evt_Phi_MET","MET #phi",20,-3.2,3.2),"Evt_Phi_MET",plotselection_MET600,plotlabel_MET600),
        Plot(ROOT.TH1F(plotprefix+"Jet_Pt","Jet Pt",20,0.,500.),"Jet_Pt",plotselection_MET600,plotlabel_MET600)
        
    ]

plots = plots_inclusive+plots_MET300+plots_MET400+plots_MET500+plots_MET600

allsystnames=weightSystNames+otherSystNames

THEoutputpath=plotParallel(jobname,5000000,plots,samples_signal+samples_background+samples_data,[''],['1.'],weightSystNames,systWeights,additionalvariables,[],"/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_FAST.json",otherSystNames,addCodeInterfacePaths=[],cirun=False,StopAfterCompileStep=False,haddParallel=True)
print "---------------------------------------------"
print "THEoutputpath=",THEoutputpath
print "---------------------------------------------"
if type(THEoutputpath)==str:
    outputpath=THEoutputpath
else:
    outputpath=THEoutputpath[0]
    
print "hadding from wildcard"
haddFilesFromWildCard(outputpath,outputpath[:-11]+"/HaddOutputs/*.root")

renamedPath=outputpath[:-5]+'_limitInput.root'

if os.path.exists(renamedPath):
    #if askYesNo('renamedFileExists. Repeat renaming?'):
    #  renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
    print "renamed file already exists"
else:
    #UPDATE
    if type(THEoutputpath)==str:
        renameHistos(outputpath,renamedPath,allsystnames,False,False)
    else:
        renameHistos(THEoutputpath[1:],renamedPath,allsystnames,False,False)
        
outputpath=outputpath[:-5]+'_limitInput.root'

print "---------------------------------------------"
print "outputpath=",outputpath
print "---------------------------------------------"

print 'Create lists needed later'
# background samples
listOfHistoLists_background=createHistoLists_fromSuperHistoFile(outputpath,samples_background,plots,1)
lolT_background=transposeLOL(listOfHistoLists_background)
print "listOfHistoLists_background=",listOfHistoLists_background
print "listOfHistoListsTransposed_background=",lolT_background
# signal samples
listOfHistoLists_signal=createHistoLists_fromSuperHistoFile(outputpath,samples_signal,plots,1)
lolT_signal=transposeLOL(listOfHistoLists_signal)
print "listOfHistoLists_signal=",listOfHistoLists_signal
print "listOfHistoListsTransposed_signal=",lolT_signal
# data
listOfHistoLists_data=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
print "listOfHistoLists_data=",listOfHistoLists_data

print "Making MC Control plots"
print "skipping"

lll=createLLL_fromSuperHistoFileSyst(outputpath,samples_background,plots,allsystnames)
#lllnoQCD=createLLL_fromSuperHistoFileSyst(outputpath,samples[1:],discriminatorPlots,errorSystNamesNoPSNoQCD)
labels=[plot.label for plot in plots]
plotDataMCanWsyst(listOfHistoLists_data,transposeLOL(lolT_background),samples_background,lolT_signal[0],samples_signal[0],-1,jobname,[[lll,3354,ROOT.kBlack,True]],False,labels,True,False)
