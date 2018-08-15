#############
# plot general control distributions 
##############

from plotconfig_DATA import *
from plot_additional_DATA import *
from plot_cuts_DATA import *

sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy


ABCDeventhandling='oncefirst'

name='Zprime_DATA_'+ABCDeventhandling+'_'+ABCDversion+radi+'_'+WPs




plots=[

   



    #ABCD
    #no topbtag
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatA_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatB_Zprime_M" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatB_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatC_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatD_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1  ,"1 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatE_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatF_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatG_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3  + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatH_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1_anti  ,"1 btag") ,

    #withtopsubbtag
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Zprime_M" ,"m(Z') in GeV, CatA " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatA_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatB_Zprime_M" ,"m(Z') in GeV" ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatB_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatC_Zprime_M" ,"m(Z') in GeV, CatC " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatC_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2_anti + "&& " + cut1  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatD_Zprime_M" ,"m(Z') in GeV, CatD " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatD_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1  ,"2 btag"),

    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatE_Zprime_M" ,"m(Z') in GeV, CatE " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatE_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1_anti  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatF_Zprime_M" ,"m(Z') in GeV, CatF " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatF_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2 + "&& " + cut1_anti  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatG_Zprime_M" ,"m(Z') in GeV, CatG " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatG_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3  + "&&" + cut2_anti + "&& " + cut1_anti  ,"2 btag"),
    Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatH_Zprime_M" ,"m(Z') in GeV, CatH " ,80,1000,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatH_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3_anti + "&&" + cut2_anti + "&& " + cut1_anti  ,"2 btag") ,
    
    

    #Plot(ROOT.TH1F( ABCDversion + "_withtopbtag_CatA_Zprime_eff" ,"m(Z') in GeV, CatA " ,1,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatA_withtopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2 + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "2 btag"),
    #Plot(ROOT.TH1F( ABCDversion + "_notopbtag_CatA_Zprime_eff" ,"m(Z') in GeV, CatA " ,1,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD_CatID==ABCD_CatA_notopbtag" + " && " + generalselection + " && " + plotselection_topsubjetCSVv2_anti + " && " + cut3 + "&&" + cut2 + "&& " + cut1, "1 btag"),
    
    #Plot(ROOT.TH1F( "N_Gen_ZPrimes" ,"N_Gen_ZPrimes" ,1,0,5000),"N_Gen_ZPrimes", "N_Gen_ZPrimes>0", ""),

  

]





plotnames=[]
for i in plots:
    plotnames.append(i.name)

OnlyFirstList=len(plots)*[False]
#OnlyFirstList[plotnames.index("ABCD1_notopbtag_CatA_Zprime_M"):plotnames.index('ABCD2_inclusive_CatH_Tprime_M') +1 ] = len(OnlyFirstList[plotnames.index("ABCD1_notopbtag_CatA_Zprime_M"):plotnames.index('ABCD2_inclusive_CatH_Tprime_M') + 1 ] ) * [True]
OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_M"):plotnames.index(ABCDversion + "_withtopbtag_CatH_Zprime_M") +1 ] = len(OnlyFirstList[plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_M"):plotnames.index(ABCDversion + "_withtopbtag_CatH_Zprime_M") + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'



#print allweightsystnames
#print allsystweights

#print name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weigthsystnamesbasic+weightsystnamesMadgraphbantiZprimeM,systweightsbasic+systweightsMadgraphbantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+DataSamples,[""],["1"],weightsystnamesPythia8bantiZprimeM,systweightsPythia8bantiZprimeM,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile)
#print allweightsystnames
#print allsystweights, "OK"
#raw_input()

outputpath=plotParallel(name,2000000,plots,DataSamples,[""],["1"],allweightsystnames,allsystweights,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList,otherSystNames)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)


#rebinnedHistosExist=False
rebinnedHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned.root'
#rebinnedandaddedHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_added.root'
rebinnedBRHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_'+BR_name+'.root'

rebinnedandaddedBRHistoPath=os.getcwd()+'/workdir/'+name+'/output_rebinned_'+BR_name+'_added.root'


allweightsystnames=allweightsystnames+JECsystnames
print allweightsystnames

print 'debug filesave 1 ', rebinnedHistoPath[:-5]
#print 'debug filesave 2 ', rebinnedandaddedHistoPath[:-5]
print 'debug filesave 3 ', rebinnedandaddedBRHistoPath[:-5]
print 'debug filesave 4 ', rebinnedBRHistoPath[:-5]





if not os.path.isfile(rebinnedHistoPath):


    #lllSignal=createLLL_fromSuperHistoFileSyst(outputpath,SignalSamples,plots,allweightsystnames)
    #lllBackground=createLLL_fromSuperHistoFileSyst(outputpath,BackgroundSamples,plots,allweightsystnames)
    
    #create_envelopes_new(lllSignal)
    
    
    
    #for ll1,ll2,ll3,ll4 in zip(transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index('ttbar')]]),transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index('ST_tW')]]),transposeLOL([transposeLOL(lllBackground)   [BackgroundSampleNames.index('ST_t')]]),transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index('ST_s')]])):
        #for l1,l2,l3,l4 in zip(ll1,ll2,ll3,ll4):
            #for h1, h2,h3,h4 in zip(l1,l2,l3,l4):
                #h1.Add(h2)
                #h1.Add(h3)
                #h1.Add(h4)    
    
    #lllBackground=transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index('ttbar')]])
                               
    #BackgroundSamples=[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]
    
    #BackgroundSampleNames=[BackgroundSampleNames[BackgroundSampleNames.index('ttbar')]]
    
    #create_envelopes_new(lllBackground)


    
    lllData=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,allweightsystnames)
    #lllData_Pythia=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,allweightsystnames)
    forcombine=True
    #lllSignal=rebintovarbinsLLL(lllSignal,name,True,True,False,forcombine)
    #lllBackground=rebintovarbinsLLL(lllBackground,name,True,True,False,forcombine)
    lllData=rebintovarbinsLLL(lllData,name,True,True,False,forcombine)
    
    #llltofile=lllBackground+lllData
    llltofile=lllData
    writeLLLtoFile(llltofile,rebinnedHistoPath[:-5])

    #createBRLLL(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_"+BR_name+""):SignalSampleNames.index("SigZprime25001500_"+BR_name+"")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_tWb"):SignalSampleNames.index("SigZprime25001500_tWb")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_ttZ"):SignalSampleNames.index("SigZprime25001500_ttZ")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_ttH"):SignalSampleNames.index("SigZprime25001500_ttH")+1]),BR[0],BR[1],BR[2])
    
    #createBRLLL(transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_"+BR_name+"_1pb"):BackgroundSampleNames.index("SC_Zprime25001500_"+BR_name+"_1pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_tWb_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_tWb_1_0pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_ttZ_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttZ_1_0pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_ttH_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttH_1_0pb")+1]),BR[0],BR[1],BR[2])
    
    #createBRLLL(transposeLOL(transposeLOL(lllData)[DataSampleNames.index("DATA_Zprime15001200_"+BR_name+"_1pb"):DataSampleNames.index("DATA_Zprime25001500_"+BR_name+"_1pb")+1]),transposeLOL(transposeLOL(lllData)[DataSampleNames.index("DATA_Zprime15001200_tWb_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_tWb_1_0pb")+1]),transposeLOL(transposeLOL(lllData)[DataSampleNames.index("DATA_Zprime15001200_ttZ_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_ttZ_1_0pb")+1]),transposeLOL(transposeLOL(lllData)[DataSampleNames.index("DATA_Zprime15001200_ttH_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_ttH_1_0pb")+1]),BR[0],BR[1],BR[2])
    
    #scaleToLatestLimit(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_"+BR_name+""):SignalSampleNames.index("SigZprime25001500_ttH")+1]),expectedSignals)
    #scaleToLatestLimit(transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_"+BR_name+"_1pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttH_1_0pb")+1]),expectedSignals)
    #scaleToLatestLimit(transposeLOL(transposeLOL(lllData)[DataSampleNames.index("DATA_Zprime15001200_"+BR_name+"_1pb"):DataSampleNames.index("DATA_Zprime25001500_ttH_1_0pb")+1]),expectedSignals)

    #BRllltofile=lllData+lllBackground+lllSignal
    #writeLLLtoFile(BRllltofile,rebinnedBRHistoPath[:-5])     
    
    
    #addLLLtoLLL(lllData,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),name,False,allweightsystnames,True)
    #addedllltofile=lllData+lllBackground+lllSignal
    #writeLLLtoFile(addedllltofile,rebinnedandaddedBRHistoPath[:-5])
   
    
#else:
    ##if not os.path.isfile(rebinnedBRHistoPath):
        
        #BackgroundSamples=[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]
        #BackgroundSampleNames=[BackgroundSampleNames[BackgroundSampleNames.index('ttbar')]]
        
        
        ##lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,SignalSamples,plots,allweightsystnames)
        #lllBackground=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,BackgroundSamples,plots,allweightsystnames)
    
        
        
        
        #lllData=createLLL_fromSuperHistoFileSyst(rebinnedHistoPath,DataSamples,plots,allweightsystnames) 

        #createBRLLL(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_"+BR_name+""):SignalSampleNames.index("SigZprime25001500_"+BR_name+"")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_tWb"):SignalSampleNames.index("SigZprime25001500_tWb")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_ttZ"):SignalSampleNames.index("SigZprime25001500_ttZ")+1]),transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_ttH"):SignalSampleNames.index("SigZprime25001500_ttH")+1]),BR[0],BR[1],BR[2])
        
        #createBRLLL(transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_"+BR_name+"_1pb"):BackgroundSampleNames.index("SC_Zprime25001500_"+BR_name+"_1pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_tWb_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_tWb_1_0pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_ttZ_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttZ_1_0pb")+1]),transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_ttH_1_0pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttH_1_0pb")+1]),BR[0],BR[1],BR[2])
        
        #createBRLLL(transposeLOL(transposeLOL(lllData)[DataSampleNames.index("DATA_Zprime15001200_"+BR_name+"_1pb"):DataSampleNames.index("DATA_Zprime25001500_"+BR_name+"_1pb")+1]),transposeLOL(transposeLOL(lllData)[DataSampleNames.index("DATA_Zprime15001200_tWb_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_tWb_1_0pb")+1]),transposeLOL(transposeLOL(lllData)[DataSampleNames.index("DATA_Zprime15001200_ttZ_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_ttZ_1_0pb")+1]),transposeLOL(transposeLOL(lllData)[DataSampleNames.index("DATA_Zprime15001200_ttH_1_0pb"):DataSampleNames.index("DATA_Zprime25001500_ttH_1_0pb")+1]),BR[0],BR[1],BR[2])

        #scaleToLatestLimit(transposeLOL(transposeLOL(lllSignal)[SignalSampleNames.index("SigZprime15001200_"+BR_name+""):SignalSampleNames.index("SigZprime25001500_ttH")+1]),expectedSignals)
        #scaleToLatestLimit(transposeLOL(transposeLOL(lllBackground)[BackgroundSampleNames.index("SC_Zprime15001200_"+BR_name+"_1pb"):BackgroundSampleNames.index("SC_Zprime25001500_ttH_1_0pb")+1]),expectedSignals)
        #scaleToLatestLimit(transposeLOL(transposeLOL(lllData)[DataSampleNames.index("DATA_Zprime15001200_"+BR_name+"_1pb"):DataSampleNames.index("DATA_Zprime25001500_ttH_1_0pb")+1]),expectedSignals)


        #BRllltofile=lllData+lllBackground+lllSignal
        #writeLLLtoFile(BRllltofile,rebinnedBRHistoPath[:-5])
        
        #addLLLtoLLL(lllData,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),name,False,allweightsystnames,True)
        #addedllltofile=lllData+lllBackground+lllSignal
        #writeLLLtoFile(addedllltofile,rebinnedandaddedBRHistoPath[:-5])
       
    
    #else:
        
        
        #if not os.path.isfile(rebinnedandaddedBRHistoPath):
            
            #BackgroundSamples=[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+BackgroundSamples[BackgroundSampleNames.index('QCDMadgraph'):BackgroundSampleNames.index('SC_none')+1]           
            #BackgroundSampleNames=[BackgroundSampleNames[BackgroundSampleNames.index('ttbar')]]+BackgroundSampleNames[BackgroundSampleNames.index('QCDMadgraph'):BackgroundSampleNames.index('SC_none')+1]
            
              
            #lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedBRHistoPath,SignalSamples,plots,allweightsystnames)
            #lllBackground=createLLL_fromSuperHistoFileSyst(rebinnedBRHistoPath,BackgroundSamples,plots,allweightsystnames)
            #lllData=createLLL_fromSuperHistoFileSyst(rebinnedBRHistoPath,DataSamples,plots,allweightsystnames) 

    
            #addLLLtoLLL(lllData,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),name,False,allweightsystnames,True)
            #addedllltofile=lllData+lllBackground+lllSignal
            #writeLLLtoFile(addedllltofile,rebinnedandaddedBRHistoPath[:-5])  
            
        #else:
            
            #BackgroundSamples=[BackgroundSamples[BackgroundSampleNames.index('ttbar')]]+BackgroundSamples[BackgroundSampleNames.index('QCDMadgraph'):BackgroundSampleNames.index('SC_none')+1]    
            #BackgroundSampleNames=[BackgroundSampleNames[BackgroundSampleNames.index('ttbar')]]+BackgroundSampleNames[BackgroundSampleNames.index('QCDMadgraph'):BackgroundSampleNames.index('SC_none')+1]
            
            
            #lllSignal=createLLL_fromSuperHistoFileSyst(rebinnedandaddedBRHistoPath,SignalSamples,plots,allweightsystnames)
            #lllBackground=createLLL_fromSuperHistoFileSyst(rebinnedandaddedBRHistoPath,BackgroundSamples,plots,allweightsystnames)
            #lllData=createLLL_fromSuperHistoFileSyst(rebinnedandaddedBRHistoPath,DataSamples,plots,allweightsystnames)            
    
    











#def createBRLLL(final_lllBR,lll1,lll2,lll3, c1=1.0, c2=1.0, c2=1.0):


#addLOLtoLOL(listOfHistoListsDataMadgraph,transposeLOL([transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("ttbar")]]))
#addLOLtoLOL(listOfHistoListsDataPythia,transposeLOL([transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("QCDPythia8")]]+[transposeLOL(listOfHistoListsBackground)[BackgroundSampleNames.index("ttbar")]]))

#addLLLtoLLL(lllData,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDMadgraph")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),True,allweightsystnames)
#addLLLtoLLL(lllData_Pythia,transposeLOL([transposeLOL(lllBackground)[BackgroundSampleNames.index("QCDPythia8")]]+[transposeLOL(lllBackground)[BackgroundSampleNames.index("ttbar")]]),True,allweightsystnames)


#################################################################Transosed LOL ######################
#LOLSumw2(listOfHistoLists)
#dummylist=[[]]
labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)
#lolSignalT=transposeLOL(listOfHistoListsSignal)
#lolBackgroundT=transposeLOL(listOfHistoListsBackground)
#lolDataMadgraphT=transposeLOL(listOfHistoListsDataMadgraph)
#lolDataPythiaT=transposeLOL(listOfHistoListsDataPythia)


######### create Envelope for renorm and factorization ##############

#writeListOfHistoLists2(transposeLOL(transposeLOL(lllBackground[plotnames.index('ABCD1_notopbtag_CatA_Zprime_M')])[allweightsystnames.index('_MCSF_PDF0'),allweightsystnames.index('_MCSF_PDF100')]),BackgroundSamples, '','PDFstuff',False,False,False,'histo',False, False,True)

#envlll_nom=selectsubLLL(lllBackground,range(plotnames.index('ABCD1_notopbtag_CatA_Zprime_M'),plotnames.index('ABCD2_inclusive_CatE_Tprime_M')+1),[allweightsystnames.index('')],range(BackgroundSampleNames.index('QCDMadgraph'),BackgroundSampleNames.index('QCDPythia8')+1))
#envlll_up=selectsubLLL(lllBackground,range(plotnames.index('ABCD1_notopbtag_CatA_Zprime_M'),plotnames.index('ABCD2_inclusive_CatE_Tprime_M')+1),[allweightsystnames.index('_MCSF_renfac_envUp')],range(BackgroundSampleNames.index('QCDMadgraph'),BackgroundSampleNames.index('QCDPythia8')+1))
#envlll_down=selectsubLLL(lllBackground,range(plotnames.index('ABCD1_notopbtag_CatA_Zprime_M'),plotnames.index('ABCD2_inclusive_CatE_Tprime_M')+1),[allweightsystnames.index('_MCSF_renfac_envDown')],range(BackgroundSampleNames.index('QCDMadgraph'),BackgroundSampleNames.index('QCDPythia8')+1))
#envlll_lll=selectsubLLL(lllBackground,range(plotnames.index('ABCD1_notopbtag_CatA_Zprime_M'),plotnames.index('ABCD2_inclusive_CatE_Tprime_M')+1),range(allweightsystnames.index('_MCSF_renfacUp'),allweightsystnames.index('_MCSF_facDown')+1),range(BackgroundSampleNames.index('QCDMadgraph'),BackgroundSampleNames.index('QCDPythia8')+1))

#create_envelope(envlll_nom,envlll_up,envlll_down,envlll_lll)

##transposeLOL(transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index('_ABCD1_notopbtag_CatA_Zprime_M')])[weightsystnames.index('_MCSF_renfacUp'):weightsystnames.index('_MCSF_renfacDown')+1])[BackgroundSampleNames.index('ttbar')]

#writeListOfHistoLists([transposeLOL(transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index('ABCD1_notopbtag_CatA_Zprime_M')])[weightsystnames.index('_MCSF_PDF000'):weightsystnames.index('_MCSF_PDF100')+1])[BackgroundSampleNames.index('ttbar')]], 'PDFs_ttbar','PDFs_ttbar',False,False,False,'histo',False, False,True)
#writeListOfHistoLists([transposeLOL(transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index('ABCD1_withtopbtag_CatA_Zprime_M')])[weightsystnames.index('_MCSF_PDF000'):weightsystnames.index('_MCSF_PDF100')+1])[BackgroundSampleNames.index('ttbar')]], 'PDFs_ttbar','PDFs_ttbar',False,False,False,'histo',False, False,True)
#writeListOfHistoLists([transposeLOL(transposeLOL(lllBackgroundWithweightsyscopyABCD[plotnames.index('ABCD1_inclusive_CatA_Zprime_M')])[weightsystnames.index('_MCSF_PDF000'):weightsystnames.index('_MCSF_PDF100')+1])[BackgroundSampleNames.index('ttbar')]], 'PDFs_ttbar','PDFs_ttbar',False,False,False,'histo',False, False,True)

#doABCD=True

#if doABCD:

  #if not doBR:
    #for dataname, signalname, SC_name in zip(DataSampleNames,SignalSampleNames+[SignalSampleNames[0]],BackgroundSampleNames[BackgroundSampleNames.index('SC_Zprime15001200_tWb_8_6pb'):BackgroundSampleNames.index('SC_none')+1]):
    ##for dataname, signalname, SC_name in zip([DataSampleNames[DataSampleNames.index('DATA_noSignal')]],[SignalSampleNames[0]],[BackgroundSampleNames[BackgroundSampleNames.index('SC_none')]]):
        #for QCDname in ['QCDMadgraph']:
            ##for ABCDversion in ['ABCD1','ABCD2']:
            #for ABCDversion in [ABCDversion]:
                #for Category in ['notopbtag','withtopbtag']:#,'inclusive']:
          
#################Final with ABCD only ###################
##################with Syst notoptag #####################R
                    #if QCDname is 'QCDMadgraph':
                        #for ABCD_syst,ABCD_syst_name in zip([False,True],['Rateonly','RateAndShape']):
                        ##for ABCD_syst,ABCD_syst_name in zip([True],['RateAndShape']):
                            #ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(lllData,lllBackground,lllSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,dataname,SC_name,signalname,ABCDversion+'_'+Category+'_CatA', ABCDversion+'_'+Category+'_CatB', ABCDversion+'_'+Category+'_CatC', ABCDversion+'_'+Category+'_CatD',QCDname, ABCDversion+'/fancy_'+ABCDversion+'_'+ABCDeventhandling+'_'+WPs+'_'+ABCD_syst_name,ABCD_syst)



  #else:
    #for dataname, signalname, SC_name in zip(DataSampleNames,SignalSampleNames+[SignalSampleNames[0]],BackgroundSampleNames[BackgroundSampleNames.index('SC_Zprime15001200_tWb_1_0pb'):BackgroundSampleNames.index('SC_none')+1]):
    ##for dataname, signalname, SC_name in zip([DataSampleNames[DataSampleNames.index('DATA_noSignal')]],[SignalSampleNames[0]],[BackgroundSampleNames[BackgroundSampleNames.index('SC_none')]]):
        #for QCDname in ['QCDMadgraph']:
            ##for ABCDversion in ['ABCD1','ABCD2']:
            #for ABCDversion in [ABCDversion]:
                #for Category in ['notopbtag','withtopbtag']:#,'inclusive']:
          
#################Final with ABCD only ###################
##################with Syst notoptag #####################R
                    #if QCDname is 'QCDMadgraph':
                        #for ABCD_syst,ABCD_syst_name in zip([False,True],['Rateonly','RateAndShape']):
                        ##for ABCD_syst,ABCD_syst_name in zip([True],['RateAndShape']):
                            #ABCDBackgroundEstimationCalculationAndPlotsWithSystematics(lllData,lllBackground,lllSignal,BackgroundSamples,SignalSamples,DataSampleNames,BackgroundSampleNames, SignalSampleNames, plotnames,allweightsystnames,dataname,SC_name,signalname,ABCDversion+'_'+Category+'_CatA', ABCDversion+'_'+Category+'_CatB', ABCDversion+'_'+Category+'_CatC', ABCDversion+'_'+Category+'_CatD',QCDname, ABCDversion+'/fancy_'+ABCDversion+'_'+ABCDeventhandling+'_'+WPs+'_'+ABCD_syst_name,ABCD_syst)
#print "signal efficiency in %"

#for l1,l2,l3,signame in zip(lllSignal[plotnames.index(ABCDversion + "_withtopbtag_CatA_Zprime_eff")],lllSignal[plotnames.index(ABCDversion + "_notopbtag_CatA_Zprime_eff")],lllSignal[plotnames.index("N_Gen_ZPrimes")], SignalSampleNames):
    #print signame, " 2 b-tag:", l1[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()/l3[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()*100.0 ,"   1 b-tag:", l2[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()/l3[allweightsystnames.index('_'+ABCDversion+'_nominal')].Integral()*100.0
