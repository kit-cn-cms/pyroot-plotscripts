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

from analysisClass import *
from plotconfig_AronsVariables import *


def main(argv):

    # Create analysis object with output name
    name='plots_FoxWolframs_v1'

    ## ADJUST THIS PATH
    analysis=Analysis(name,argv,'/nfs/dust/cms/user/kelmorab/plotscriptsSpring17/forAron/pyroot-plotscripts/NOTDEFINED/output_limitInput.root ', signalProcess='ttH')

    analysis.plotBlinded=False
    analysis.makeSimplePlots=True
    analysis.makeMCControlPlots=False
    analysis.makeDatacards=False
    analysis.checkBins=False
    analysis.makeEventYields=False
    makeROCPlots=True
    

    analysis.printChosenOptions()


    # samples
    samples=samplesControlPlots

    # define BDT output variables
    # define additional variables necessary for selection in plotparallel
    additionalvariables=["Jet_Pt", "Muon_Pt", "Electron_Pt",
                         "Jet_Eta", "Muon_Eta", "Electron_Eta",
                         "Jet_CSV", "Jet_Flav", "N_Jets", "Jet_E", "Jet_Phi", "Jet_M",
                         "Evt_Pt_PrimaryLepton","Evt_E_PrimaryLepton","Evt_M_PrimaryLepton","Evt_Phi_PrimaryLepton","Evt_Eta_PrimaryLepton",
                         "Evt_Phi_MET","Evt_Pt_MET",

                         "GenEvt_I_TTPlusBB","GenEvt_I_TTPlusCC",
                         
                         ]
                             
    # append variables needed by NNFlow Interface
    #additionalvariables.extend(NNFlowInterface.getAdditionalVariablesList())
    print "Debug output: Print additional variables list: ", additionalvariables


        # selections

    # book plots
    # Label put on the plots
    plotlabel="1 lepton, #geq 4 jets, #geq 2 b-tags"
    # selection for this set of plots
    plotselection="(N_Jets>=4&&N_BTagsM>=2)"
    discriminatorPlots=[
        # plot of N_Jets
        Plot(ROOT.TH1F("N_Jets","Number of jets",7,3.5,10.5),"N_Jets",plotselection,plotlabel),
        # plot of B-tag variables
        Plot(ROOT.TH1F("N_BTagsM","Number of b-tagged jets",4,1.5,5.5),"N_BTagsM",plotselection,plotlabel),
        Plot(ROOT.TH1F("CSV0","B-tag of leading jet",22,-.1,1),"Jet_CSV[0]",plotselection,plotlabel),
        Plot(ROOT.TH1F("CSV1","B-tag of second jet",22,-.1,1),"Jet_CSV[1]",plotselection,plotlabel),
        Plot(ROOT.TH1F("CSV","B-tag of all jets",22,-.1,1),"Jet_CSV",plotselection,plotlabel),
        
        Plot(ROOT.TH1F("CSV_ge0p5","B-tag of all jets for events with more than 5 jets",22,-.1,1),"Jet_CSV",plotselection+"*(N_Jets>5)",plotlabel),
        
        
        # Fox Wolfram plots for this selection
        # implement your variables here like
        # Plot(ROOT.TH1F("INTERNALNAME","AXIS TITLE",N-Bins,MINX,MAXX),"BRANCHNAME_OR_VARIABLEEYPRESSION",SELECTION,LABEL)
        Plot(ROOT.TH1F("H0_O","H_{0}^{O}",100,-0.2,1),"Evt_H0_O",plotselection,plotlabel),

        
    ]
    

    #actual sample to use
    allsamples=samples
    allsystnames=weightSystNames


    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel==False or analysis.plotNumber == None :
        #if not os.path.exists(analysis.rootFilePath):
            # create the histograms
            THEoutputpath=plotParallel(name,50000,discriminatorPlots,samples,[''],['1.'],weightSystNames,systWeights,additionalvariables,[],"",[],addCodeInterfacePaths=[],cirun=True,StopAfterCompileStep=False,haddParallel=True)
            #UPDATE
            if type(THEoutputpath)==str:
              outputpath=THEoutputpath
            else:
              outputpath=THEoutputpath[0]
            
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
              if type(THEoutputpath)==str:
                renameHistos(outputpath,renamedPath,allsystnames,False,False)
              else:
                renameHistos(THEoutputpath[1:],renamedPath,allsystnames,False,False)
        
            outputpath=outputpath[:-5]+'_limitInput.root'

    else:
        # Warning This time output path refers only to output.root
        # ToDo: Fix usage of output path and output limit path
        if not os.path.exists(analysis.rootFilePath[:-16]+'.root'):
            workdir=os.getcwd()+'/workdir/'+name
            outputpath=workdir+'/output.root'
        else:
            outputpath=analysis.rootFilePath[:-16]+'.root'

    # Now draw the histograms
    # Invoke drawParallel step
    #if analysis.doDrawParallel==True and analysis.plotNumber == None :
        ## Hand over opts to keep commandline options
        #print 'Starting DrawParallel'
        #DrawParallel(discriminatorPlots,name,os.path.realpath(inspect.getsourcefile(lambda:0)),analysis.opts)

    ## belongs to DrawParallel
    #if analysis.doDrawParallel==True and analysis.plotNumber != None :
        #discriminatorPlots=[discriminatorPlots[int(analysis.plotNumber)]]
    
    ## Lists needed later, produce them only if needed, so check if subsequent step comes
    #if (analysis.doDrawParallel==False or analysis.plotNumber != None) and (analysis.makeSimplePlots==True or analysis.makeMCControlPlots==True or analysis.makeEventYields==True):
        #print 'Create lists needed later'
        #listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,discriminatorPlots,1)
        #lolT=transposeLOL(listOfHistoLists)
        #print listOfHistoLists

    ## This is the function call to the actual draw function
    ## plot simple MC plots
    #if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeSimplePlots==True :
        #print "Making simple MC plots."
        ##writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_controlplots')
        #writeListOfHistoListsAN(transposeLOL(lolT),samples,"",name+'/'+name+'_shapes',True,False,False,'histo',False,True,False)
    
    # Lists needed later, produce them only if needed, so check if subsequent step comes
    if (analysis.doDrawParallel==True and analysis.plotNumber == None) and (analysis.makeSimplePlots==True or analysis.makeMCControlPlots==True or analysis.makeEventYields==True):
        print 'Create lists needed later'
        listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,discriminatorPlots,1)
        lolT=transposeLOL(listOfHistoLists)
        print listOfHistoLists

    # This is the function call to the actual draw function
    # plot simple MC plots
    if (analysis.doDrawParallel==True and analysis.plotNumber == None) and analysis.makeSimplePlots==True :
        print "Making simple MC plots."
        #writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_controlplots')
        labels=[]
        for plot in discriminatorPlots:
          labels.append(plot.label)
        writeListOfHistoListsAN(transposeLOL(lolT),samples,labels,name+'/'+name+'_shapes',True,False,False,'histo',False,True,False)
     
    if analysis.doDrawParallel==True and analysis.plotNumber == None and makeROCPlots==True:
      print "making ROCs"
      # get relevant histos from file
      # create a list of lists of plots (the ones defined above) for whcih the ROCs will be drawn together on a canvas
      # for example here we want to create a canvas comparing plots 2,3 and 4  and another cnavase comparing plots 1,2 and 3
      listOfListOfPlotsForROCs=[
        [discriminatorPlots[3],discriminatorPlots[4],discriminatorPlots[2]],
        [discriminatorPlots[1],discriminatorPlots[2],discriminatorPlots[3]],
        ]
      for iROC, listOfRelevantPlots in enumerate(listOfListOfPlotsForROCs):
        print iROC, listOfRelevantPlots
        listOfHistoListsForROCs=createHistoLists_fromSuperHistoFile(outputpath,samples,listOfRelevantPlots,1)
        rocs=[]
        names_=[]
        colors_=[]
        print listOfHistoListsForROCs
        # loop over variables
        iCol=0
        for plot, histoTuple in zip(listOfRelevantPlots, listOfHistoListsForROCs):
          iCol+=1
          # skip color 10 becuase it is white
          if iCol==10:
            iCol+=1
          # get ROC curve
          rocs.append(getROC(histoTuple[0], histoTuple[1],rej=True))
          # print ROCs on canvas
          names_.append(plot.histo.GetTitle())
          colors_.append(iCol)
        writeListOfROCs(graphs=rocs,names=names_,colors=colors_,filename=name+'/'+name+'_ROCs/'+name+'_roc_'+str(iROC),printInts=True,logscale=False,rej=True)
   


if __name__ == "__main__":

   MainClock=ROOT.TStopwatch()
   MainClock.Start()
   main(sys.argv[1:])
   print "TOTAL Elapsed time since beginning of analysis script", MainClock.RealTime()
