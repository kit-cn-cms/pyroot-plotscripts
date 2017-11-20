#!/usr/bin/python2
# blub 

import sys
import getopt
import os
import imp
import importlib
import inspect
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
# UPDATE
from limittools import makeDatacardsParallel
from limittools import calcLimits
from limittools import replaceQ2scale

from analysisClass import *
from plotconfig_v14 import *


def main(argv):

    # Create analysis object with output name
    name='limits_All_v23'
    #analysis=Analysis(name,argv,'/nfs/dust/cms/user/mharrend/doktorarbeit/latest/ttbb-cutbased-analysis_limitInput.root')
    analysis=Analysis(name,argv,'/nfs/dust/cms/user/kelmorab/plotscriptsSpring17/Sep17/pyroot-plotscripts/NOTDEFINED/output_limitInput.root ', signalProcess='ttH')
    #analysis=Analysis(name,argv,'/nfs/dust/cms/user/mharrend/doktorarbeit/output20170626-reference/workdir/ttbb-cutbased-analysis/output_limitInput.root')

    analysis.plotBlinded=True
    analysis.makeSimplePlots=True
    analysis.makeMCControlPlots=True
    analysis.makeDataCards=True
    analysis.additionalPlotVariables=False

    # Make sure proper plotconfig is loaded for either ttbb or ttH
    print "We will import the following plotconfig: ", analysis.getPlotConfig()
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
    bdtset="Spring17v2"
    alternativebdtset="Spring17v3_ttbb"
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

                         'conditionFor_finalbdt_ljets_j4_t3:=(N_Jets==4 && N_BTagsM==3)',
                         'conditionFor_finalbdt_ljets_j4_t4:=(N_Jets==4 && N_BTagsM==4)',
                         'conditionFor_finalbdt_ljets_j5_t3:=(N_Jets==5 && N_BTagsM==3)',
                         'conditionFor_finalbdt_ljets_j5_tge4:=(N_Jets==5 && N_BTagsM>=4)',
                         'conditionFor_finalbdt_ljets_jge6_t2:=(N_Jets>=6 && N_BTagsM==2)',
                         'conditionFor_finalbdt_ljets_jge6_t3:=(N_Jets>=6 && N_BTagsM==3)',
                         'conditionFor_finalbdt_ljets_jge6_tge4:=(N_Jets>=6 && N_BTagsM>=4)',
                         'conditionFor_alternativebdt_ljets_jge6_tge4:=(N_Jets>=6 && N_BTagsM>=4)',
                         'conditionFor_alternativebdt_ljets_jge6_t3:=(N_Jets>=6 && N_BTagsM==3)',
                         'conditionFor_alternativebdt_ljets_j5_tge4:=(N_Jets==5 && N_BTagsM>=4)',
                         'conditionFor_alternativebdt_ljets_j4_t4:=(N_Jets==4 && N_BTagsM==4)',
                         "GenEvt_I_TTPlusBB","GenEvt_I_TTPlusCC",

             			 'finalbdt_ljets_j4_t2:=Evt_HT_Jets',
             			 'finalbdt_ljets_j5_t2:=Evt_HT_Jets',
                         'finalbdt_ljets_j4_t3:='+bdtweightpath+'/weights_Final_43_'+bdtset+'.xml',
                         'finalbdt_ljets_j4_t4:='+bdtweightpath+'/weights_Final_44_'+bdtset+'.xml',
                         'finalbdt_ljets_j5_t3:='+bdtweightpath+'/weights_Final_53_'+bdtset+'.xml',
                         'finalbdt_ljets_j5_tge4:='+bdtweightpath+'/weights_Final_54_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_t2:='+bdtweightpath+'/weights_Final_62_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_t3:='+bdtweightpath+'/weights_Final_63_'+bdtset+'.xml',
                         'finalbdt_ljets_jge6_tge4:='+bdtweightpath+'/weights_Final_64_'+bdtset+'.xml',
                         'alternativebdt_ljets_jge6_tge4:='+bdtweightpath+'/weights_Final_64_'+alternativebdtset+'.xml',
                         'alternativebdt_ljets_jge6_t3:='+bdtweightpath+'/weights_Final_63_'+alternativebdtset+'.xml',
                         'alternativebdt_ljets_j5_tge4:='+bdtweightpath+'/weights_Final_54_'+alternativebdtset+'.xml',
                         'alternativebdt_ljets_j4_t4:='+bdtweightpath+'/weights_Final_44_'+alternativebdtset+'.xml',
                         ]
    additionalvariables+=GetMEPDFadditionalVariablesList("/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/rate_factors_onlyinternal_powhegpythia.csv")
    # append variables needed by NNFlow Interface
    #additionalvariables.extend(NNFlowInterface.getAdditionalVariablesList())
    print "Debug output: Print additional variables list: ", additionalvariables

    # prepare discriminators
    categories=[]
    nhistobins=[]
    minxvals=[]
    maxxvals=[]
    discrs =[]
    
    # jet tag categories for BDTs
    categorienames_JTBDT=[
                  ("(N_Jets==4&&N_BTagsM==2)","ljets_j4_t2",""),
                  ("(N_Jets==5&&N_BTagsM==2)","ljets_j5_t2",""),
                  ("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3",""),
                  ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4",""),
                  ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3",""),
                  ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4",""),
                  ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2",""),
                  ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3",""),
                  ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4",""),
                  ]
    discrs_JTBDT=['finalbdt_ljets_j4_t2','finalbdt_ljets_j5_t2','finalbdt_ljets_j4_t3', 'finalbdt_ljets_j4_t4', 'finalbdt_ljets_j5_t3', 'finalbdt_ljets_j5_tge4', 'finalbdt_ljets_jge6_t2', 'finalbdt_ljets_jge6_t3', 'finalbdt_ljets_jge6_tge4']
    nhistobins_JTBDT = [  20,20,      20,   12,    25,    16,   25,   25,   16 ]
    minxvals_JTBDT =   [ 200, 200, -0.8,  -0.8, -0.8,   -0.9,         -0.6, -0.8,   -0.8]
    maxxvals_JTBDT =   [800,800,    0.75,  0.7,   0.7,    0.8,  0.7,  0.75,    0.76]
    discrs+=discrs_JTBDT
    nhistobins+=nhistobins_JTBDT
    minxvals+=minxvals_JTBDT
    maxxvals+=maxxvals_JTBDT
    categories+=categorienames_JTBDT
    
    # 2D analysis split at ttH median of BDTs
    unsplitcategorienames_JT2D=[
                  ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4",""),
                  ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4",""),
                  ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3",""),
                  ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4",""),
                  ]
    bdtcuts=[-0.2,-0.2,0.2,0.22,0.17,0.22,0.05,0.17,0.17]
    categorienames_JT2D=[]
    for cat,bdt in zip(unsplitcategorienames_JT2D,bdtcuts):
      if cat[1] in ["ljets_jge6_tge4","ljets_j5_tge4","ljets_j4_t4","ljets_jge6_t3"]:
        categories.append(('('+cat[0]+')*(finalbdt_'+cat[1]+'>'+str(bdt)+')',cat[1]+'_high') )
        categories.append(('('+cat[0]+')*(finalbdt_'+cat[1]+'<='+str(bdt)+')',cat[1]+'_low') )
    discrs_JT2D=[memexp, memexp, memexp, memexp,memexp, memexp,memexp, memexp]
    nhistobins_JT2D = [10,12, 8,10, 25,25,   12,15 ]
    minxvals_JT2D =   [ 0.05, 0.05,0.1,0.1,0,0,0.05,0]
    maxxvals_JT2D =   [1.0, 0.9,1.0,0.95,1.0,1.0,1.0,1.0]
    discrs+=discrs_JT2D
    nhistobins+=nhistobins_JT2D
    minxvals+=minxvals_JT2D
    maxxvals+=maxxvals_JT2D
    categories+=categorienames_JT2D

    ## 2D analysis split at ttH median of BDTs OPTIMIZED FOR ttbb vs rest
    #unsplitcategorienames_JT2DOPTIMIZED=[
                  #("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4",""),
                  #("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4",""),
                  #("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3",""),
                  #("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4",""),
                  #]
    #bdtcuts=[-0.2,-0.2,0.2,0.22,0.17,0.22,0.05,0.17,0.17]
    #categorienames_JT2DOPTIMIZED=[]
    #for cat,bdt in zip(unsplitcategorienames_JT2DOPTIMIZED,bdtcuts):
      #if cat[1] in ["ljets_jge6_tge4","ljets_j5_tge4","ljets_j4_t4","ljets_jge6_t3"]:
        #categories.append(('('+cat[0]+')*(alternativebdt_'+cat[1]+'>'+str(bdt)+')',cat[1]+'_ttbbOpt_high') )
        #categories.append(('('+cat[0]+')*(alternativebdt_'+cat[1]+'<='+str(bdt)+')',cat[1]+'_ttbbOpt_low') )
    #discrs_JT2DOPTIMIZED=[memexp, memexp, memexp, memexp,memexp, memexp,memexp, memexp]
    #nhistobins_JT2DOPTIMIZED = [10,12, 8,10, 25,25,   12,15 ]
    #minxvals_JT2DOPTIMIZED =   [ 0.05, 0.05,0.1,0.1,0,0,0.05,0]
    #maxxvals_JT2DOPTIMIZED =   [0.95, 0.9,1.0,1.0,1.0,1.0,1.0,1.0]
    #discrs+=discrs_JT2DOPTIMIZED
    #nhistobins+=nhistobins_JT2DOPTIMIZED
    #minxvals+=minxvals_JT2DOPTIMIZED
    #maxxvals+=maxxvals_JT2DOPTIMIZED
    #categories+=categorienames_JT2DOPTIMIZED


    assert(len(nhistobins)==len(maxxvals))
    assert(len(nhistobins)==len(minxvals))
    assert(len(nhistobins)==len(categories))
    assert(len(nhistobins)==len(discrs))

    # get input for plotting function
    plotPreselections= [c[0] for c in categories]
    binlabels= [c[1] for c in categories]


    # add systematic ntuples
    systsamples=[]
    for sample in samples:
        for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
            thisnewsel=sample.selection
            systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname,samDict=sampleDict))

    ## WARNING: Adjust Slice for samples if changing ttbar contributions

    # add Parton shower variation samples
    #for sample in samples[analysis.getTtbarSamplesLower() : analysis.getTtbarSamplesUpper()]: # only for ttbar samples
    for sample in samples:
        if sample.nick not in ['ttbarOther', 'ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B']:
          continue
        for sysname,sysfilename in zip(PSSystNames,PSSystFileNames):
            thisoldsel=sample.selection
            thisnewsel=sample.selection.replace(ttbarMCWeight,"*1.0").replace(mcWeight+evenSel,mcWeightAll)
            print "adding sample for ", sysname
            print "selection ", thisnewsel
            print "instead of ", thisoldsel
            systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace(ttbarPathS,path_additionalSamples+"/ttbar_"+sysfilename+"/*nominal*.root"),thisnewsel,sample.nick+sysname,samDict=sampleDict))
    
    # add QCD sytematic for QCD sample
    for sample in samples:
        if sample.name!='QCD':
          continue
        for sysname,sysreplacestring in zip(QCDSystNames,QCDSystReplacementStrings):
          thisnewsel=sample.selection.replace("internalQCDweight",sysreplacestring)
          systsamples.append(Sample(sample.name+sysname,sample.color,sample.path,thisnewsel,sample.nick+sysname,samDict=sampleDict))
    
    allsamples=samples+systsamples
    allsystnames=weightSystNames+otherSystNames+PSSystNames+QCDSystNames


    # define plots
    discriminatorPlots=[]
    print len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
    print len(zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals))
    for discr,b,bl,nb,minx,maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
        discriminatorPlots.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b,bl))


    # Check if additional (input) variables should be plotted and if necessary add them here to the discriminatorPlots
    if analysis.additionalPlotVariables:
      # Construct list with additional plot variables, will need name of discrs and plotPreselections for this
      clearTextAdditionalPlotList = analysis.getAdditionalPlotVariables(discrs, plotPreselections, binlabels)
      evalAdditionalPlotList = [eval(x) for x in clearTextAdditionalPlotList]
      discriminatorPlots.extend(evalAdditionalPlotList)
      print "Additional variables added to discriminatorPlots: \n", clearTextAdditionalPlotList


    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel==False or analysis.plotNumber == None :
        if not os.path.exists(analysis.rootFilePath):
            print "Doing plotParallel step since root file was not found."
            #UPDATE
            THEoutputpath=outputpath=plotParallel(name,5000000,discriminatorPlots,samples+samples_data+systsamples,[''],['1.'],weightSystNames,systWeights,additionalvariables,[["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_Spring17_V1",False]],"/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_latestAndGreatest.json",otherSystNames+PSSystNames+QCDSystNames,addCodeInterfacePaths=[],cirun=True,StopAfterCompileStep=False,haddParallel=True)
            #UPDATE
            if type(THEoutputpath)==str:
              outputpath=THEoutputpath
            else:
              outputpath=THEoutputpath[0]
            if analysis.getActivatedOptimizedRebinning():
              if analysis.getSignalProcess() == 'ttbb':
                # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                optimizeBinning(outputpath,signalsamples=[samples[0:3]], backgroundsamples=samples[3:],additionalSamples=samples_data, plots=discriminatorPlots, systnames=allsystnames, minBkgPerBin=2.0, optMode=analysis.getOptimzedRebinning(),considerStatUnc=False, maxBins=20, minBins=2,verbosity=2)
              elif analysis.getSignalProcess() == 'ttH':
                # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. Rest: background samples
                optimizeBinning(outputpath,signalsamples=[samples[0]], backgroundsamples=samples[9:],additionalSamples=samples[1:9]+samples_data, plots=discriminatorPlots, systnames=allsystnames, minBkgPerBin=2.0, optMode=analysis.getOptimzedRebinning(),considerStatUnc=False, maxBins=20, minBins=2,verbosity=2)
              else:
                print 'Warning: Could not find signal process.'

            # UPDATE
            # hadd histo files before renaming. The histograms are actually already renamed. But the checkbins thingy will not have been done yet.
            print "hadding from wildcard"
            haddFilesFromWildCard(outputpath,outputpath[:-11]+"/HaddOutputs/*.root")
            # Deactivate check bins functionality in renameHistos if additional plot variables are added via analysis class
            renamedPath=outputpath[:-5]+'_limitInput.root'
            if os.path.exists(renamedPath):
              #if askYesNo('renamedFileExists. Repeat renaming?'):
              #  renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
              print "renamed file already exists"
            else:
              #UPDATE
              if type(THEoutputpath)==str:
                renameHistos(outputpath,renamedPath,allsystnames,True,False)
              else:
                renameHistos(THEoutputpath[1:],renamedPath,allsystnames,True,False)
#            addRealData(renamedPath,[s.nick for s in samples_data],binlabels,discrname)
            #addPseudoData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
            #outputpath=outputpath[:-5]+'_limitInput.root'
            outputpath=outputpath[:-5]+'_limitInput.root'
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
        #UPDATE
        makeDatacardsParallel(outputpath,name+'/'+name+'_datacard',binlabels,doHdecay=True,discrname=discrname,datacardmaker="mk_datacard_JESTest13TeVPara")


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
        lolT=transposeLOL(listOfHistoLists)
        listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,discriminatorPlots,1)

    # plot simple MC plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeSimplePlots==True :
        print "Making simple MC plots."
        writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_controlplots')
        writeListOfHistoListsAN(transposeLOL([lolT[0]]+lolT[9:]),[samples[0]]+samples[9:],"",name+'/'+name+'_shapes',True,False,False,'histo',False,True,False)


    # Make MC Control plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeMCControlPlots==True :
        print "Making MC Control plots"
        print "skipping"
        lll=createLLL_fromSuperHistoFileSyst(outputpath,samples[9:],discriminatorPlots,errorSystNamesNoQCD)
        labels=[plot.label for plot in discriminatorPlots]
        plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-2,name,[[lll,3354,ROOT.kBlack,True]],False,labels,True,analysis.plotBlinded)



if __name__ == "__main__":

   MainClock=ROOT.TStopwatch()
   MainClock.Start()
   main(sys.argv[1:])
   print "TOTAL Elapsed time since beginning of analysis script", MainClock.RealTime()
