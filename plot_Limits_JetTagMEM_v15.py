#!/usr/bin/python2

import sys
import getopt
import os
import imp
import importlib
import inspect
import ROOT
import subprocess
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import addRealData
from limittools import makeDatacards
from limittools import calcLimits
from limittools import replaceQ2scale

from analysisClass import *
from plotconfig_v14 import *


def main(argv):

    # Create analysis object with output name
    name='limits_JetTagMEM_v15'
    #analysis=Analysis(name,argv,'/nfs/dust/cms/user/mharrend/doktorarbeit/latest/ttbb-cutbased-analysis_limitInput.root')
    analysis=Analysis(name,argv,'/nfs/dust/cms/user/kelmorab/plotscriptsSpring17/Sep17/pyroot-plotscripts/NOTDEFINED/output_limitInput.root ', signalProcess='ttH')
    #analysis=Analysis(name,argv,'/nfs/dust/cms/user/mharrend/doktorarbeit/output20170626-reference/workdir/ttbb-cutbased-analysis/output_limitInput.root')

    analysis.plotBlinded=True
    analysis.makeSimplePlots=True
    analysis.makeMCControlPlots=True
    analysis.makeDatacards=True
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
    memexp='(memDBp>0.0)*(memDBp)+(memDBp<=0.0)*(0.01)'

    # define BDT output variables
    bdtweightpath="/nfs/dust/cms/user/kelmorab/Spring17BDTWeights/"
    bdtset="Spring17v1"
    # define additional variables necessary for selection in plotparallel
    additionalvariables=["Jet_Pt", "Muon_Pt", "Electron_Pt",
                         "Jet_Eta", "Muon_Eta", "Electron_Eta",
                         "Jet_CSV", "Jet_Flav", "N_Jets", "Jet_E", "Jet_Phi", "Jet_M",
                         "Evt_Pt_PrimaryLepton","Evt_E_PrimaryLepton","Evt_M_PrimaryLepton","Evt_Phi_PrimaryLepton","Evt_Eta_PrimaryLepton",
                         "Weight_CSV","Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown","Weight_CSVHFStats1up","Weight_CSVHFStats1down",
                         "Weight_CSVLFStats1up","Weight_CSVLFStats1down","Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
                         "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down",

                         'finalbdt_ljets_j4_t2:=Evt_HT_Jets',
                         'finalbdt_ljets_j5_t2:=Evt_HT_Jets',
                         'finalbdt_ljets_j4_t3:=Evt_blr_ETH_transformed',
                         'finalbdt_ljets_j4_t4:='+memexp,
                         'finalbdt_ljets_j5_t3:=Evt_blr_ETH_transformed',
                         'finalbdt_ljets_j5_tge4:='+memexp,
                         'finalbdt_ljets_jge6_t2:=Evt_blr_ETH_transformed',
                         'finalbdt_ljets_jge6_t3:='+memexp,
                         'finalbdt_ljets_jge6_tge4:='+memexp,
                         ]
    # append variables needed by NNFlow Interface
    #additionalvariables.extend(NNFlowInterface.getAdditionalVariablesList())
    print "Debug output: Print additional variables list: ", additionalvariables


    categorievars=[
        'top3vars:=(Evt_Deta_TaggedJetsAverage>=1.3 && Reco_Sum_LikelihoodRatio<=0.41 && Reco_Sum_LikelihoodTimesMERatio<=0.5)',
    ]
    additionalvariables=additionalvariables+categorievars

    # definition of categories
    #categoriesJT=[
                  #("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
                  #("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
                  #("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
                  #("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
                  #("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
                  #("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
                  #("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
    #]


    ## selections for categories
    #categoriesJTsel="("+categoriesJT[0][0]
    #for cat in categoriesJT[1:]:
      #categoriesJTsel+="||"+cat[0]
    #categoriesJTsel+=")"


    ## category strings
    #catstringJT="0"
    #for i,cat in enumerate(categoriesJT):
        #catstringJT+=("+"+str(i+1)+"*"+cat[0])



    # define categories
    categorienames_=[
                  ("(N_Jets==4&&N_BTagsM==2)","ljets_j4_t2",""),
                  ("(N_Jets==5&&N_BTagsM==2)","ljets_j5_t2",""),
                  ("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3",""),
                  ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4",""),
                  ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3",""),
                  ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4",""),
                  ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2",""),
                  ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3",""),
                  ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4","")
    ]


    categories=[]


    # add unsplit categories
    for cat in categorienames_:
        categories.append(cat)

    print categories

    nhistobins= [  20,20, 	20,   10,    20,    10,   20,   20,   10 ]
    minxvals=   [ 200, 200, -1,  0, -1,   0, 200, 0,   0]
    maxxvals=   [800,800,    7, 1,   7,    1,  800,  1,    1]
    discrs =    ['finalbdt_ljets_j4_t2','finalbdt_ljets_j5_t2','finalbdt_ljets_j4_t3', 'finalbdt_ljets_j4_t4', 'finalbdt_ljets_j5_t3', 'finalbdt_ljets_j5_tge4', 'finalbdt_ljets_jge6_t2','finalbdt_ljets_jge6_t3', 'finalbdt_ljets_jge6_tge4']



    assert(len(nhistobins)==len(maxxvals))
    assert(len(nhistobins)==len(minxvals))
    assert(len(nhistobins)==len(categories))
    assert(len(nhistobins)==len(discrs))

    # get input for plotting function
    plotPreselections= [c[0] for c in categories]
    binlabels= [c[1] for c in categories]



    systsamples=[]
    for sample in samples:
        for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
            thisnewsel=sample.selection
            systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname,samDict=sampleDict))

    ## WARNING: Adjust Slice for samples if changing ttbar contributions

    # add Parton shower variation samples
    for sample in samples[analysis.getTtbarSamplesLower() : analysis.getTtbarSamplesUpper()]: # only for ttbar samples
        for sysname,sysfilename in zip(PSSystNames,PSSystFileNames):
            thisoldsel=sample.selection
            thisnewsel=sample.selection.replace(ttbarMCWeight,"*1.0").replace(mcWeight+evenSel,mcWeightAll)
            print "adding sample for ", sysname
            print "selection ", thisnewsel
            print "instead of ", thisoldsel
            systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace(ttbarPathS,path_additionalSamples+"/ttbar_"+sysfilename+"/*nominal*.root"),thisnewsel,sample.nick+sysname,samDict=sampleDict))

    allsamples=samples+systsamples
    allsystnames=weightSystNames+otherSystNames+PSSystNames


    # define plots
    discriminatorPlots=[]
    print len(discrs),len(plotPreselections),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
    print len(zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals))
    for discr,b,bl,nb,minx,maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
        discriminatorPlots.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b,bl))

    theAdditionalVariablePlots=[]
    #plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
    #plotselection="(N_Jets>=4&&N_BTagsM>=2)"
    #generalPlots=[
        #Plot(ROOT.TH1F("JT" ,"jet-tag categories",len(categoriesJT),0.5,0.5+len(categoriesJT)),catstringJT,categoriesJTsel,"1 lepton"),
        #Plot(ROOT.TH1F("N_Jets","Number of ak4 jets",7,3.5,10.5),"N_Jets",plotselection,plotlabel),
        #Plot(ROOT.TH1F("N_BTagsM","Number of b-tags",4,1.5,5.5),"N_BTagsM",plotselection,plotlabel),
        #Plot(ROOT.TH1F("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",plotselection,plotlabel),
        #Plot(ROOT.TH1F("etaalljets","#eta of all jets",60,-2.5,2.5),"Jet_Eta",plotselection,plotlabel),
        #Plot(ROOT.TH1F("csvalljets","csv of all jets",44,-.1,1),"Jet_CSV",plotselection,plotlabel),
    #]
    ## Check if additional (input) variables should be plotted and if necessary add them here to the discriminatorPlots
    #if analysis.additionalPlotVariables:
      ## Construct list with additional plot variables, will need name of discrs and plotPreselections for this
      ##clearTextAdditionalPlotList = analysis.getAdditionalPlotVariables(discrs, plotPreselections, binlabels)
      ##evalAdditionalPlotList = [eval(x) for x in clearTextAdditionalPlotList]  
      #for discr,b,bl,nb,minx,maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
        #theAdditionalVariablePlots.append(Plot(ROOT.TH1F("Evt_blr_ETH_transformed_"+bl,"Evt_blr_ETH_transformed",nb,-10.0,10.0),"Evt_blr_ETH_transformed",b,bl))
        #theAdditionalVariablePlots.append(Plot(ROOT.TH1F("Evt_blr_ETH_transformed_"+bl,"Evt_blr_ETH_transformed",nb,-10.0,10.0),"Evt_blr_ETH_transformed",b,bl))
      #discriminatorPlots.extend(theAdditionalVariablePlots)
      #discriminatorPlots.extend(generalPlots)
      ##print "Additional variables added to discriminatorPlots: \n", clearTextAdditionalPlotList
    
    
    
    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel==False or analysis.plotNumber == None :
        if not os.path.exists(analysis.rootFilePath):
            print "Doing plotParallel step since root file was not found."
            outputpath=plotParallel(name,5000000,discriminatorPlots,samples+samples_data+systsamples,[''],['1.'],weightSystNames,systWeights,additionalvariables,[["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_Spring17_V1",False]],"/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_v5_08102017.json",otherSystNames+PSSystNames,cirun=False)
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
            renamedPath=outputpath[:-5]+'_limitInput.root'
            if os.path.exists(renamedPath):
              #if askYesNo('renamedFileExists. Repeat renaming?'):
              #  renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
              print "renamed file already exists"
            else:
              renameHistos(outputpath,renamedPath,allsystnames,analysis.getCheckBins(),False)
            #renameHistos(outputpath,outputpath[:-5]+'_limitInput.root',allsystnames,analysis.getCheckBins(),False)
            #addRealData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samplesDataControlPlots],binlabels,discrname)
            addPseudoData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
            #thecpcommand='cp -v '+outputpath[:-5]+'_limitInput.root'+' '+outputpath[:-5]+'_limitInputREALDATA.root'
            #subprocess.call(cmd,shell=True)
            #addRealData(outputpath[:-5]+'_limitInput.root',[s.nick for s in samplesDataControlPlots],binlabels,discrname)
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
        lll=createLLL_fromSuperHistoFileSyst(outputpath[:-5]+'_syst.root',samples[0:],discriminatorPlots,errorSystNames)
        labels=[plot.label for plot in discriminatorPlots]
        plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[0:]),samples[0:],lolT[0],samples[0],-2,name,[[lll,3354,ROOT.kBlack,True]],False,labels,True,analysis.plotBlinded)


    # Make yield table
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeEventYields==True :
        print "Making yield table."
        for hld,hl in zip(listOfHistoListsData,listOfHistoLists):
            hldName = hld[0].GetName()
            tablepath=("/".join((outputpath.split('/'))[:-1]))+"/"+name+hldName+"_yields"
            eventYields(hld,hl,samples,tablepath)



if __name__ == "__main__":

   MainClock=ROOT.TStopwatch()
   MainClock.Start()
   main(sys.argv[1:])
   print "TOTAL Elapsed time since beginning of analysis script", MainClock.RealTime()
