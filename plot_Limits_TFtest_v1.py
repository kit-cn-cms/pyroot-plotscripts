#!/usr/bin/python2

import sys
import getopt
import os
import imp
import importlib
import inspect
import ROOT
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import addRealData
from limittools import addRealDataAllHistos
from limittools import addPseudoDataAllHistos
from limittools import makeDatacards
from limittools import calcLimits
from limittools import replaceQ2scale
import dnnInputVariableListV1

from analysisClass import *
from plotconfig_Limits_TFtest_v1 import *


def main(argv):

    #Create analysis object with output name
    name='limits_TFtest_v1'
    #analysis=Analysis(name,argv,'/nfs/dust/cms/user/mharrend/doktorarbeit/latest/ttbb-cutbased-analysis_limitInput.root')
    analysis=Analysis(name,argv,'/nfs/dust/cms/user/kelmorab/plotscripts18/July18/pyroot-plotscripts/NOTDEFINED/output_limitInput.root ', signalProcess='ttH')
    #analysis=Analysis(name,argv,'/nfs/dust/cms/user/mharrend/doktorarbeit/output20170626-reference/workdir/ttbb-cutbased-analysis/output_limitInput.root')

    analysis.plotBlinded=True
    analysis.makeSimplePlots=True
    analysis.makeMCControlPlots=True
    analysis.makeDatacards=True

    # Make sure proper plotconfig is loaded for either ttbb or ttH
    #print "We will import the following plotconfig: ", analysis.getPlotConfig()
    # make sure plotconfig gets imported into global namespace
    #globals().update(importlib.import_module(analysis.getPlotConfig()).__dict__)



    ## NNFlow interface
    # Create and configure NNFlow interface
    # NNFlowInterfacePath=os.getcwd()+'/pyroot-plotscripts-base/NNFlowInterface.py'
    # NNFlowInterface = imp.load_source("NNFlowInterface",NNFlowInterfacePath).theInterface()
    # NNFlowInterface.setDebugOutput(True)
    # NNFlowInterface.setModelFolderPath('/nfs/dust/cms/user/mharrend/doktorarbeit/tensorflowModels/neural_network_v3/multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20/model')
    # NNFlowInterface.setModelName('multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20.ckpt')
    # NNFlowInterface.update()
    #
    # print "NNFlowInterfacePath: ", NNFlowInterfacePath

    analysis.printChosenOptions()


    # samples
    #samples=samplesControlPlots
    samples=samplesLimits

    samples_data=samplesDataControlPlots


    # Name of final discriminator, should not contain underscore
    discrname='finaldiscr'
    # define MEM discriminator variable
    memexp='(memDBp>0.0)*(memDBp)+(memDBp<=0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # define BDT output variables
    bdtweightpath="/nfs/dust/cms/user/kelmorab/Spring17BDTWeights/"
    bdtset="Spring17v1"
    # define additional variables necessary for selection in plotparallel
    additionalvariables=["Jet_Pt", "Muon_Pt", "Electron_Pt",
                         "Jet_Eta", "Muon_Eta", "Electron_Eta",
                         "Muon_Pt_BeForeRC","Electron_Pt_BeforeRun2Calibration","Electron_Eta_Supercluster",
                         "Jet_CSV", "Jet_Flav", "N_Jets", "Jet_E", "Jet_Phi", "Jet_M",
                         "Evt_Pt_PrimaryLepton","Evt_E_PrimaryLepton","Evt_M_PrimaryLepton","Evt_Phi_PrimaryLepton","Evt_Eta_PrimaryLepton",
                         "Evt_Phi_MET","Evt_Pt_MET",
                         "Weight_CSV","Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown","Weight_CSVHFStats1up","Weight_CSVHFStats1down",
                         "Weight_CSVLFStats1up","Weight_CSVLFStats1down","Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
                         "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down","Evt_blr_ETH","Evt_blr_ETH_transformed",
                         
             			 'finalbdt_ljets_j4_t2:=Evt_HT_Jets',
             			 'finalbdt_ljets_j5_t2:=Evt_HT_Jets',
                         'finalbdt_ljets_j4_t3:='+bdtweightpath+'/weights_Final_43_'+bdtset+'.xml',
                         'finalbdt_ljets_j4_t4:='+bdtweightpath+'/weights_Final_44_'+bdtset+'.xml',
                         'finalbdt_ljets_j5_t3:='+bdtweightpath+'/weights_Final_53_'+bdtset+'.xml',
                         'finalbdt_ljets_j5_tge4:='+bdtweightpath+'/weights_Final_54_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_t2:='+bdtweightpath+'/weights_Final_62_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_t3:='+bdtweightpath+'/weights_Final_63_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_tge4:='+bdtweightpath+'/weights_Final_64_'+bdtset+'.xml',
                         ]
    dnnInputVariables=list(set(dnnInputVariableListV1.all_variables_list))
    additionalvariables+=dnnInputVariables
    
    
    # append variables needed by NNFlow Interface
    #additionalvariables.extend(NNFlowInterface.getAdditionalVariablesList())
    print "Debug output: Print additional variables list: ", additionalvariables


        # selections

    # definition of categories
    categoriesJT=[
                  ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
                  ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
                  ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
                  ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
                  ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
                  ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
                  ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
    ]
 
    # selections for categories
    categoriesJTsel="("+categoriesJT[0][0]
    for cat in categoriesJT[1:]:
      categoriesJTsel+="||"+cat[0]
    categoriesJTsel+=")"


    # category strings
    catstringJT="0"
    for i,cat in enumerate(categoriesJT):
        catstringJT+=("+"+str(i+1)+"*"+cat[0])



    # book plots
    plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
    #plotlabelboosted="#splitline{1 lepton, #geq 4 jets, #geq 2 b-tags}{#geq 1 C/A 1.5 jet p_{T} > 200 GeV}"
    plotselection="(N_Jets>=4&&N_BTagsM>=2)"
    
    plots=[
        Plot(ROOT.TH1D("N_Jets","Number of ak4 jets",11,3.5,14.5),"N_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1D("Evt_HT_Jets","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
        Plot(ROOT.TH1D("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",plotselection,plotlabel),
        
        TwoDimPlot(ROOT.TH2D("HT_vs_N_Jets","HT_vs_N_Jets",50,0,1500,11,3.5,14.5),"Evt_HT_Jets","N_Jets",plotselection,plotlabel),
        TwoDimPlot(ROOT.TH2D("HT_vs_JetPt","HT_vs_JetPt",50,0,1500,60,0,300),"Evt_HT_Jets","Jet_Pt",plotselection,plotlabel),
        #TwoDimPlot(ROOT.TH2D("AK8Pt_vs_JetPt","AK8Pt_vs_JetPt",50,0,1000,60,0,300),"AK8Jet_Pt","Jet_Pt",plotselection,plotlabel),
        
        #Plot(ROOT.TH1D("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,categoriesJTsel,"1 lepton"),
        ##Plot(ROOT.TH1D("BCAT" ,"jet-tag + boosted categories",len(categoriesJTB),0.5,0.5+len(categoriesJTB)),catstringJTB,categoriesJTBsel,"1 lepton"),
        #Plot(ROOT.TH1D("N_Jets","Number of ak4 jets",11,3.5,14.5),"N_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1D("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",plotselection,plotlabel),
        #Plot(ROOT.TH1D("CSV0","B-tag of leading jet",22,-.1,1),"Jet_CSV[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("CSV1","B-tag of second jet",22,-.1,1),"Jet_CSV[1]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("CSV","B-tag of all jets",22,-.1,1),"Jet_CSV",plotselection,plotlabel),
        
        #Plot(ROOT.TH1D("eta1","#eta of leading jet",50,-2.5,2.5),"Jet_Eta[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("eta2","#eta of second jet",50,-2.5,2.5),"Jet_Eta[1]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("phij1","#phi of leading jet",64,-3.2,3.2),"Jet_Phi[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("phij2","#phi of second jet",64,-3.2,3.2),"Jet_Phi[1]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("Evt_HT_Jets","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1D("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",plotselection,plotlabel),
        #Plot(ROOT.TH1D("etaalljets","#eta of all jets",60,-2.5,2.5),"Jet_Eta",plotselection,plotlabel),
        #Plot(ROOT.TH1D("pumvaalljets","PU MVA of all jets",60,0,1.0),"Jet_PileUpMVA",plotselection,plotlabel),
        #Plot(ROOT.TH1D("puidalljets","PU MVA of all jets",60,0,1.0),"Jet_PileUpID",plotselection,plotlabel),
        
        #Plot(ROOT.TH1D("csvalljets","csv of all jets",44,-.1,1),"Jet_CSV",plotselection,plotlabel),
        #Plot(ROOT.TH1D("leppt","lepton p_{T}",50,0,200),"LooseLepton_Pt[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("lepeta","lepton #eta",50,-2.5,2.5),"LooseLepton_Eta[0]",plotselection,plotlabel),
        #Plot(ROOT.TH1D("elleppt","electron p_{T}",50,0,200),"Electron_Pt[0]",'Electron_Pt[0]>10',plotlabel),
        #Plot(ROOT.TH1D("ellepeta","electron #eta",50,-2.5,2.5),"Electron_Eta[0]",'Electron_Pt[0]>10',plotlabel),
        #Plot(ROOT.TH1D("muleppt","muon p_{T}",50,0,200),"Muon_Pt[0]",'Muon_Pt[0]>10',plotlabel),
        #Plot(ROOT.TH1D("mulepeta","muon #eta",50,-2.5,2.5),"Muon_Eta[0]",'Muon_Pt[0]>10',plotlabel),
        
        #Plot(ROOT.TH1D("N_AK8_Jets","Number of ak8 jets",10,0.5,10.5),"N_AK8Jets",plotselection,plotlabel),
       
        
        
    ]
    discriminatorPlots=plots        
    
    
    # prepare discriminators
    categories=[]
    nhistobins=[]
    minxvals=[]
    maxxvals=[]
    discrs =[]
    
    # DNN classes DNN outputs
    categorienames_MultiDNN=[
              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==0)","ljets_j4_tge3_ttHnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==0)","ljets_j5_tge3_ttHnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==0)","ljets_jge6_tge3_ttHnode",""),

              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==2)","ljets_j4_tge3_ttbbnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==2)","ljets_j5_tge3_ttbbnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==2)","ljets_jge6_tge3_ttbbnode",""),
             
              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==3)","ljets_j4_tge3_tt2bnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==3)","ljets_j5_tge3_tt2bnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==3)","ljets_jge6_tge3_tt2bnode",""),

              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==1)","ljets_j4_tge3_ttbnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==1)","ljets_j5_tge3_ttbnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==1)","ljets_jge6_tge3_ttbnode",""),
              
             
              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==4)","ljets_j4_tge3_ttccnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==4)","ljets_j5_tge3_ttccnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==4)","ljets_jge6_tge3_ttccnode",""),

              ("(N_Jets==4&&N_BTagsM>=3&&DNN_4j3t_pred_class==5)","ljets_j4_tge3_ttlfnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&DNN_5j3t_pred_class==5)","ljets_j5_tge3_ttlfnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&DNN_6j3t_pred_class==5)","ljets_jge6_tge3_ttlfnode",""),

              #("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==0)","ljets_jge6_tge2_ttHnode",""),
              #("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==1)","ljets_jge6_tge2_ttbbnode",""),
              #("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==2)","ljets_jge6_tge2_ttbnode",""),
              #("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==3)","ljets_jge6_tge2_tt2bnode",""),
              #("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==4)","ljets_jge6_tge2_ttccnode",""),
              #("(N_Jets>=6&&N_BTagsM>=2&&aachen_pred_class==5)","ljets_jge6_tge2_ttlfnode",""),
              ]
    
    
    discrs_MultiDNN=[
	     "DNN_Out_4j3t_ttH",  "DNN_Out_5j3t_ttH",  "DNN_Out_6j3t_ttH",
"DNN_Out_4j3t_ttbarBB",  "DNN_Out_5j3t_ttbarBB",  "DNN_Out_6j3t_ttbarBB",
"DNN_Out_4j3t_ttbar2B",  "DNN_Out_5j3t_ttbar2B",  "DNN_Out_6j3t_ttbar2B",
"DNN_Out_4j3t_ttbarB",  "DNN_Out_5j3t_ttbarB",  "DNN_Out_6j3t_ttbarB",
"DNN_Out_4j3t_ttbarCC",  "DNN_Out_5j3t_ttbarCC",  "DNN_Out_6j3t_ttbarCC",
"DNN_Out_4j3t_ttbarlf",  "DNN_Out_5j3t_ttbarlf",  "DNN_Out_6j3t_ttbarlf",

             ]
    #nhistobins_MultiDNN= [   7,   10,    12,   7,   7,    12,   7,   7,    7,   8,   7,    7,   7,   7,    7,   7,   7,    4,]
    #minxvals_MultiDNN=   [ 0.2,  0.16, 0.17, 0.16,  0.16, 0.18, 0.2,  0.2, 0.18, 0.2,  0.16, 0.16, 0.17,  0.17, 0.21, 0.17,  0.17, 0.19,]
    #maxxvals_MultiDNN=   [0.6,  0.6, 0.7,    0.6,  0.6, 0.7,    0.4,  0.4, 0.35,    0.55,  0.5, 0.55,    0.35,  0.35, 0.3,    0.5,  0.4, 0.3,]
    #nhistobins_MultiDNN+=[12,12,7,7,7,7]
    #minxvals_MultiDNN+=[0.17,0.18,0.18,0.16,0.21,0.19]
    #maxxvals_MultiDNN+=[0.7,0.7,0.35,0.55,0.3,0.3]
    nhistobins_MultiDNN=[20]*18
    minxvals_MultiDNN=[0.0]*18
    maxxvals_MultiDNN=[1.0]*18

    discrs+=discrs_MultiDNN
    nhistobins+=nhistobins_MultiDNN
    minxvals+=minxvals_MultiDNN
    maxxvals+=maxxvals_MultiDNN
    categories+=categorienames_MultiDNN
    
            
    # get input for plotting function
    plotPreselections= [c[0] for c in categories]
    binlabels= [c[1] for c in categories]
        
            
            
    #exit(0)
    
    
    systsamples=[]
    for sample in samples:
        for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
            thisnewsel=sample.selection
            systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname,samDict=sampleDict))

    ## WARNING: Adjust Slice for samples if changing ttbar contributions

    # add Parton shower variation samples
    for sample in samples[1:6]: # only for ttbar samples
        for sysname,sysfilename in zip(PSSystNames,PSSystFileNames):
            thisoldsel=sample.selection
            thisnewsel=sample.selection
            #thisnewsel=sample.selection.replace(ttbarMCWeight,"*1.0").replace(mcWeight+evenSel,mcWeightAll)
            print "adding sample for ", sysname
            print "selection ", thisnewsel
            print "instead of ", thisoldsel
            systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("TuneCP5",sysfilename),thisnewsel,sample.nick+sysname,samDict=sampleDict))
    

    #allsamples=samples+systsamples
    #allsystnames=weightSystNames+otherSystNames+PSSystNames
    allsamples=samples
    allsystnames=weightSystNames


    # define plots
    discriminatorPlots=[]
    print len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
    print len(zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals))
    for discr,b,bl,nb,minx,maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
        discriminatorPlots.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b,bl))

    ## Check if additional (input) variables should be plotted and if necessary add them here to the discriminatorPlots
    #if analysis.additionalPlotVariables:
      ## Construct list with additional plot variables, will need name of discrs and plotPreselections for this
      #clearTextAdditionalPlotList = analysis.getAdditionalPlotVariables(discrs, plotPreselections, binlabels)
      #evalAdditionalPlotList = [eval(x) for x in clearTextAdditionalPlotList]
      #discriminatorPlots.extend(evalAdditionalPlotList)
      #print "Additional variables added to discriminatorPlots: \n", clearTextAdditionalPlotList


    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel==False or analysis.plotNumber == None :
        if not os.path.exists(analysis.rootFilePath):
            print "Doing plotParallel step since root file was not found."
            outputpath=plotParallel(name,500000,discriminatorPlots,samples+samples_data+systsamples,[''],['1.'],weightSystNames,systWeights,additionalvariables,[],"",otherSystNames+PSSystNames,addCodeInterfacePaths=["pyroot-plotscripts-base/dNNInterface_Keras.py"],cirun=False,StopAfterCompileStep=True)
            #outputpath=plotParallel(name,5000000,discriminatorPlots,samples+samples_data+systsamples,[''],['1.'],weightSystNames,systWeights,additionalvariables,[["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_Spring17_V1",False]],"/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_v5_08102017.json",otherSystNames+PSSystNames+QCDSystNames,addCodeInterfacePaths=["pyroot-plotscripts-base/dNNInterface_V6.py"],cirun=False)

            # Allow start of an improved rebinning algorithm
            if analysis.getActivatedOptimizedRebinning():
              if analysis.getSignalProcess() == 'ttbb':
                # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                optimizeBinning(outputpath,signalsamples=[samples[0:3]], backgroundsamples=samples[3:],additionalSamples=samples_data, plots=discriminatorPlots, systnames=allsystnames, minBkgPerBin=2.0, optMode=analysis.getOptimzedRebinning(),considerStatUnc=False, maxBins=20, minBins=2,verbosity=2)
              elif analysis.getSignalProcess() == 'ttH':
                # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. Rest: background samples
                optimizeBinning(outputpath,signalsamples=[samples[0]], backgroundsamples=samples[9:],additionalSamples=samples[1:9]+samples_data, plots=discriminatorPlots, systnames=allsystnames, minBkgPerBin=2.0, optMode=analysis.getOptimzedRebinning(),considerStatUnc=False, maxBins=20, minBins=2,verbosity=2)
              else:
                print 'Warning: Could not find signal process.'

            # Deactivate check bins functionality in renameHistos if additional plot variables are added via analysis class
            #renameHistos(outputpath,outputpath[:-5]+'_limitInput.root',allsystnames,analysis.getCheckBins(),False)
            renamedPath=outputpath[:-5]+'_syst.root'
            if os.path.exists(renamedPath):
              #if askYesNo('renamedFileExists. Repeat renaming?'):
              #  renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
              print "renamed file already exists"
            else:
              renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
            
            #addRealDataAllHistos(renamedPath,[s.nick for s in samples_data],discriminatorPlots,forceOverwrite=True) # use this version for all histograms even if they do not follow the cat_disc_var naming scheme
            #addRealData(renamedPath,[s.nick for s in samples_data],binlabels,discrname)
            addPseudoData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
            #outputpath=outputpath[:-5]+'_limitInput.root'
            outputpath=outputpath[:-5]+'_syst.root'
        else:
            print "Not doing plotParallel step since root file was found."
            outputpath=analysis.rootFilePath
        print "outputpath: ", outputpath
    else:
        # Warning This time output path refers only to output.root
        # ToDo: Fix usage of output path and output limit path
        if not os.path.exists(analysis.rootFilePath[:-16]+'.root'):
            workdir=os.getcwd()+'/workdir/'+name
            outputpath=workdir+'/output.root'
        else:
            outputpath=analysis.rootFilePath[:-16]+'.root'

    # make datacards
    if (analysis.doDrawParallel==False or analysis.plotNumber == None) and analysis.makeDataCards == True :
        #TODO
        # 1. Implement small Epsilon case
        # 2. Implement consisted Bin-by-Bin uncertainties
        print "Making Data cards."
        makeDatacards(outputpath,name+'/'+name+'_datacard',binlabels,doHdecay=True,discrname=discrname,datacardmaker=analysis.getDataCardMaker())


    # Invoke drawParallel step
    if analysis.doDrawParallel==True and analysis.plotNumber == None :
        # Hand over opts to keep commandline options
        print 'Starting DrawParallel'
        DrawParallel(discriminatorPlots,name,os.path.realpath(inspect.getsourcefile(lambda:0)),analysis.opts)

    # belongs to DrawParallel
    if analysis.doDrawParallel==True and analysis.plotNumber != None :
        discriminatorPlots=[discriminatorPlots[int(analysis.plotNumber)]]



    # Lists needed later, produce them only if needed, so check if subsequent step comes
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and (analysis.makeSimplePlots==True or analysis.makeMCControlPlots==True or analysis.makeEventYields==True):
        print 'Create lists needed later'
        listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,discriminatorPlots,1)
        #listOfHistoListsWith2D=createHistoLists_fromSuperHistoFile(outputpath,samples,discriminatorPlots,1,DoTwoDim=True)
        print listOfHistoLists
        print ""
        lolT=transposeLOL(listOfHistoLists)
        #lolTWith2D=transposeLOL(listOfHistoListsWith2D)
        listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,discriminatorPlots,1)
        #listOfHistoListsDataWith2D=createHistoLists_fromSuperHistoFile(outputpath,samples_data,discriminatorPlots,1,DoTwoDim=True)

    # plot simple MC plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeSimplePlots==True :
        print "Making simple MC plots."
        writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_controlplots')
        writeListOfHistoListsAN(transposeLOL([lolT[0]]+lolT[9:]),[samples[0]]+samples[9:],"",name+'/'+name+'_shapes',True,False,False,'histo',False,True,False)
        #writeListOfHistoListsAN(transposeLOL([lolT[0]]+lolT[9:]),[samples[0]]+samples[9:],"",name+'/'+name+'_shapes',True,False,False,'histo',False,True,False)

    ## Make MC Control plots
    #if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeMCControlPlots==True :
        #print "Making MC Control plots"
        #print "skipping"
        #lll=createLLL_fromSuperHistoFileSyst(outputpath,samples[1:],discriminatorPlots,errorSystNames)
        #labels=[plot.label for plot in discriminatorPlots]
        #print ""
        #print lll
        #print ""
        #print lolT
        #print ""
        #print listOfHistoListsData
        #plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-2,name,[[lll,3354,ROOT.kBlack,True]],False,labels,True,analysis.plotBlinded,verbosity=0)
        #plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-2,name+'_LOG',[[lll,3354,ROOT.kBlack,True]],True,labels,True,analysis.plotBlinded,verbosity=0)

    ## Make yield table
    #if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeEventYields==True :
        #print "Making yield table."
        #print "Will do only some plots"
        #for hld,hl in zip(listOfHistoListsData,listOfHistoLists):
          #if not ("JT" in hld[0].GetName() or "N_Jets" in hld[0].GetName()) :
            #continue
          #else:
            #hldName = hld[0].GetName()
            #for h in hld+hl:
              #for i,cat in enumerate(categoriesJT):
                #h.GetXaxis().SetBinLabel(i+1,cat[1])
            #tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+hldName+"_yields"
            #eventYields(hld,hl,samples,tablepath)



if __name__ == "__main__":

   MainClock=ROOT.TStopwatch()
   MainClock.Start()
   main(sys.argv[1:])
   print "TOTAL Elapsed time since beginning of analysis script", MainClock.RealTime()
