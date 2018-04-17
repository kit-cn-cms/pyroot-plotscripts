#############
# plot general control distributions
##############

from plotconfig_Zprime_MC_Lena import *
from plot_additional_Zprime_MC_Lena import *
from plot_cuts_ZPrime_MC_closuremass import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy



ABCDeventhandling='oncefirst'
#ABCDeventhandling='reweight'

name='Zprime_MC_ABCD'+radi+'_'+ABCDeventhandling+'_'+WPs
#SampleNames=['ttbar' , 'QCD_HT', 'QCD_Pt' ]
#SignalSampleNames=['Zprime1500900',  'Zprime20001200',  'Zprime25001200']



#Create Plots

plots=[



#ABCD3 bottomCSV W_MSD
    #no topbtag
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD3_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD3_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD3_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD3_CatID==ABCD3_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta3 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,

#ABCD5 W tau21 bottomCSV
    #no topbtag
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatA_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatB_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatC_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatD_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag"),

    Plot(ROOT.TH1F("ABCD5_notopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatE_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatF_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatG_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"1 btag"),
    Plot(ROOT.TH1F("ABCD5_notopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatH_notopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2_anti + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"1 btag") ,

    # withtopsubbtag
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatA_Zprime_M_beta_first" ,"m(Z') in GeV, CatA " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatA_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21, "2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatB_Zprime_M_beta_first" ,"m(Z') in GeV, CatB " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatB_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatC_Zprime_M_beta_first" ,"m(Z') in GeV, CatC " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatC_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatD_Zprime_M_beta_first" ,"m(Z') in GeV, CatD " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatD_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag"),

    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatE_Zprime_M_beta_first" ,"m(Z') in GeV, CatE " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatE_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatF_Zprime_M_beta_first" ,"m(Z') in GeV, CatF " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatF_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV + "&& " + plotselection_W_tau21_anti  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatG_Zprime_M_beta_first" ,"m(Z') in GeV, CatG " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatG_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti  + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21  ,"2 btag"),
    Plot(ROOT.TH1F("ABCD5_withtopbtag_CatH_Zprime_M_beta_first" ,"m(Z') in GeV, CatH " ,100,0,5000),"Zprimes_ABCD"+radi+"_M", "ABCD5_CatID==ABCD5_CatH_withtopbtag" + " && " + plotselection_ABCD_general_beta5 + " && " + plotselection_topsubjetCSVv2 + " && " + plotselection_W_MSD_anti + "&&" + plotselection_B_CSV_anti + "&& " + plotselection_W_tau21_anti  ,"2 btag") ,


#


]





CatAList=["ABCD_notopbtag_CatA_Zprime_M" , "ABCD_notopbtag_CatA_Zprime_M_beta", "ABCD_notopbtag_CatA_Zprime_M_beta_first", "ABCD_notopbtag_CatA_Zprime_M_first"]

plotnames=[]
for i in plots:
    plotnames.append(i.name)


OnlyFirstList=len(plots)*[False]
#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
OnlyFirstList[plotnames.index("ABCD3_notopbtag_CatA_Zprime_M_beta_first"):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first') +1 ] = len(OnlyFirstList[plotnames.index("ABCD3_notopbtag_CatA_Zprime_M_beta_first"):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first') + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'

#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
assert len(OnlyFirstList)==len(plots)
#raw_input()




print name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,4000000,plots,samples)
outputpath=plotParallel(name,2000000,plots,SignalSamples+BackgroundSamples, [''], ['1'] , [''], ['1'],additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)
#outputpath=plotParallel(name,2000000,plots,SignalSamples, [''], ['1'] , [''], ['1'],additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)
#outputpath=plotParallel(name,3000000,plots,SignalSamples+BackgroundSamples+CombinedSamples, [''], ['1'] , [''], ['1'], [],  OnlyFirstList)
#outputpathBackground=plotParallel(name,4000000,plots,BackgroundSamples)
#outputpathData=plotParallel(name,4000000,plots,DataSamples)

# plot dataMC comparison
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)

listOfHistoListsSignal=createHistoLists_fromSuperHistoFile(outputpath,SignalSamples,plots,1, [""], True )
#listOfHistoListsBackground=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples,plots,1) #needed? Same as  ABCD?
listOfHistoListsABCD=createHistoLists_fromSuperHistoFile(outputpath,BackgroundSamples ,plots,1,[""], True )
# listOfHistoListsSignalAndBackground=createHistoLists_fromSuperHistoFile(outputpath,CombinedSamples,plots,1, [""], True )

listOfHistoListsSignalAndBackground1500900=CloneListOfHistoLists(listOfHistoListsABCD+listOfHistoListsSignal)
listOfHistoListsSignalAndBackground20001200=CloneListOfHistoLists(listOfHistoListsABCD+listOfHistoListsSignal)
listOfHistoListsSignalAndBackground25001200=CloneListOfHistoLists(listOfHistoListsABCD+listOfHistoListsSignal)


#listOfHistoListsSignalAndBackground=[listOfHistoListsSignalAndBackground1500900, listOfHistoListsSignalAndBackground20001200, listOfHistoListsSignalAndBackground25001200]


#for lol in listOfHistoListsSignalAndBackground:
    #print lol[0][0], "Sind die pointer anders fuer die verschiedenen listOfHistoLists?"

labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)



#print [transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]]
#print listOfHistoListsSignal
print SignalSampleNames

#write


lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD)
listOfHistoListsABCD=lolABCD_rebinned
chekcNbins(listOfHistoListsABCD)


#lolBackgroundT=transposeLOL(listOfHistoListsBackground)
lolABCDT=transposeLOL(listOfHistoListsABCD)
#lolDataT=transposeLOL(listOfHistoListsData)

#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)
#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)


lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD)

chekcNbins(lolABCD_rebinned)

#writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT')]])[plotnames.index('ABCD_notopbtag_CatA_Zprime_M_beta_first'):plotnames.index('ABCD7_inclusive_CatH_Zprime_M_beta_first')+1],[BackgroundSamples[BackgroundSampleNames.index('QCD_HT')]], '','single_regions_QCD'+radi,False,False,False,'histoE')


####
for ABCDversion in ['ABCD3','ABCD5']:
	ABCDclosure1D(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]),plotnames,samples,ABCDversion+'_notopbtag_CatA_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatB_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatC_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatD_Zprime_M_beta_first', ABCDversion+'_notopbtag_CatE_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatF_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatG_Zprime_M_beta_first',ABCDversion+'_notopbtag_CatH_Zprime_M_beta_first',False,1,'','closuremass/'+ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_notopbtag')
	ABCDclosure1D(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]),plotnames,samples,ABCDversion+'_withtopbtag_CatA_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatB_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatC_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatD_Zprime_M_beta_first', ABCDversion+'_withtopbtag_CatE_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatF_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatG_Zprime_M_beta_first',ABCDversion+'_withtopbtag_CatH_Zprime_M_beta_first',False,1,'','closuremass/'+ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_withtopbtag')
	#ABCDclosure1D(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1]),plotnames,samples,ABCDversion+'_inclusive_CatA_Zprime_M_beta_first',ABCDversion+'_inclusive_CatB_Zprime_M_beta_first',ABCDversion+'_inclusive_CatC_Zprime_M_beta_first',ABCDversion+'_inclusive_CatD_Zprime_M_beta_first',ABCDversion+'_inclusive_CatE_Zprime_M_beta_first',ABCDversion+'_inclusive_CatF_Zprime_M_beta_first',ABCDversion+'_inclusive_CatG_Zprime_M_beta_first',ABCDversion+'_inclusive_CatH_Zprime_M_beta_first',False,1,'','closuremass/'+ABCDversion+'/checkforABCD'+radi+ABCDeventhandling+'_'+WPs+'_inclusive')


#################################################################################################################
##Here Starts: Plots And Calculating



##Stack Plot, Background and Signal, Z_Prime_M
##writeLOLSeveralOnTop(transposeLOL(lolBackgroundT[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1])[:plotnames.index("Sideband_top_anti_W_anti_bottom_anti_Topfirst_Zprime_M")+1],BackgroundSamples[BackgroundSampleNames.index("ttbar"):BackgroundSampleNames.index("QCD_HT")+1],transposeLOL(lolSignalT),SignalSamples,-0.2,'Zprime',False ,'histoE','samehistoE')
##print "plot_Zprime_MC_Lena Len(listOfHistoListsABCD):"+str( len(listOfHistoListsABCD) )


#writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_bottom_csv_v2_vs_Zprime_M")+1], BackgroundSamples , plotnames[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_bottom_csv_v2_vs_Zprime_M")+1], 'ABCD_2D_Zprime' , True, False, False, "colz", False, False, False, True)
#writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_withtopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_W_tau21_vs_ZprimeM")+1], BackgroundSamples , plotnames[plotnames.index('ABCD_withtopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_W_tau21_vs_ZprimeM")+1], 'ABCD_2D_Zprime' , True, False, False, "colz", False, False, False, True)

#writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_notopbtag_CatA_Zprime_M" ) : plotnames.index( "ABCD_notopbtag_CatH_Zprime_M_first" ) +1] , "Integrallist_before_multiplication.tex" , SampleNames )
##writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_beta" ) : plotnames.index( "ABCD_notopbtag_CatH_Zprime_M_beta" ) +1] , "Integrallist_before_multiplication_beta.tex" , SampleNames )


##Compare BackgroundAndSignal in SignalSample (mistaged Signal infuences Background prediction )
#compareEntriesInBackgroundAndSignalRegion( transposeLOL(listOfHistoListsSignal), "ComparisonIntegralsinSignalSample.txt" )

# Correlationfactor  (with difference to selection with only first element)
#writeCorrLOL(listOfHistoListsABCD[plotnames.index('ABCD_notopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_Bottom_CSV_v2_vs_TprimeM")+1] , "Correlationfactors"+radi+".txt", plotnames[plotnames.index('ABCD_notopbtag_top_tau32_vs_top_MSD'):plotnames.index("ABCD_withtopbtag_Bottom_CSV_v2_vs_TprimeM")+1], ["tt-bar", "QCD_HT", "QCD_Pt", "QCD_comb"] , True )





#### Correlationfactor  (with difference to selection with only first element)
#writeCorrLOLinTEX( transposeLOL(lolABCDT)[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_withtopbtag_W_tau21_vs_TprimeM")+1], "Correlationfactors.tex", plotnames[plotnames.index('ABCD_top_tau32_vs_Zprime_M'):plotnames.index("ABCD_withtopbtag_W_tau21_vs_TprimeM")+1], ["tt-bar", "QCD_HT", "QCD_Pt", "QCD_comb"] , True )



###################
##Test if shape of CatA=shape of CatB






## # ABCD-Zprime_M Plots Work?
## writeListOfHistoLists( transposeLOL(lolABCDT)[plotnames.index('ABCD_notopbtag_CatA_Zprime_M'):plotnames.index('ABCD_notopbtag_CatH_Zprime_M_first_beta')+1], BackgroundSamples , plotnames[plotnames.index('ABCD_notopbtag_CatA_Zprime_M'):plotnames.index('ABCD_notopbtag_CatH_Zprime_M_first_beta')+1], 'ABCD_ZPrime_M' , True, False, False, "histoE", False, False, False, True)


##
##
##
##
### Multiply and Divide for ABCD Methode - short verion with funktion ReconstructWithABCD()
#for plotname in CatAList:
    #ReconstructWithABCD(listOfHistoListsABCD, plotname, plotnames)
    #ReconstructWithABCD(listOfHistoListsSignal, plotname, plotnames)

##
##
##
##
##Add Signal and Backgroundhistos
#XC_Factor=1
#weights= [ XC_Factor/138.07, XC_Factor/86.28, XC_Factor/37.6 ]
#for plotnameindex in range(plotnames.index("ABCD_notopbtag_CatA_Zprime_M"), plotnames.index("ABCD_notopbtag_CatH_Zprime_M_first") ):
    #for index, listOfHistoList, weight in zip(range(3),listOfHistoListsSignalAndBackground, weights):
        #addHistos(listOfHistoList, plotnameindex, plotnameindex + len(plotnames), weight , True, index)

##Multiply and Divide for ABCD
#for listOfHistoList in listOfHistoListsSignalAndBackground:
    #for plotname in CatAList:
        #ReconstructWithABCD(listOfHistoList, plotname, plotnames)

##
##
##
##
##
##
##
###Write ListOfIntegralLists
#writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_notopbtag_CatA_Zprime_M" ) : plotnames.index( "ABCD_notopbtag_CatH_Zprime_M_first" ) +1] , "Integrallist_after_multiplication.tex" , SampleNames )
## writeIntegralLOLinTEX( listOfHistoListsABCD[ plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_beta" ) : plotnames.index( "ABCD_notopbtag_CatH_Zprime_M_beta" ) +1] , "Integrallist_after_multiplication_beta.tex" , SampleNames )
##
##
##
##
##

##Create and Write List Of RatioPlots
##Workaround to use writeListOfHistoLists with a Transposed ListOfHistoList (uses trnasposeLOLextendet in plotutils.py)

#WASamples = 50*[ BackgroundSamples[0], BackgroundSamples[1] ]
#WAPlotNames =  [   "ABCD_notopbtag_CatA_Zprime_M"   ,
                 #"ABCD_notopbtag_CatE_Zprime_M"  ,
                 #"ABCD_notopbtag_CatA_Zprime_M_beta" ,
                 #"ABCD_notopbtag_CatE_Zprime_M_beta" ,
                 ## "ABCD_notopbtag_CatA_Zprime_M_one_sided" ,
                 ## "ABCD_notopbtag_CatE_Zprime_M_one_sided",
                 #"ABCD_notopbtag_CatA_Zprime_M_beta_first",
                 #"ABCD_notopbtag_CatE_Zprime_M_beta_first",
                 #"ABCD_notopbtag_CatA_Zprime_M_first",
                 #"ABCD_notopbtag_CatE_Zprime_M_first" ]

#IndexListToTranspose = [ [plotnames.index( "ABCD_notopbtag_CatA_Zprime_M" ) , plotnames.index( "ABCD_notopbtag_CatB_Zprime_M" ) ] ,
    #[ plotnames.index( "ABCD_notopbtag_CatE_Zprime_M" ), plotnames.index( "ABCD_notopbtag_CatF_Zprime_M" ) ],
    #[plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_beta" ), plotnames.index( "ABCD_notopbtag_CatB_Zprime_M_beta" ) ] ,
    #[plotnames.index( "ABCD_notopbtag_CatE_Zprime_M_beta" ), plotnames.index( "ABCD_notopbtag_CatF_Zprime_M_beta" ) ] ,
    ## [plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_one_sided" ), plotnames.index( "ABCD_notopbtag_CatB_Zprime_M_one_sided" ) ],
    ## [plotnames.index( "ABCD_notopbtag_CatE_Zprime_M_one_sided" ), plotnames.index( "ABCD_notopbtag_CatF_Zprime_M_one_sided" ) ],
    #[plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_beta_first") , plotnames.index("ABCD_notopbtag_CatB_Zprime_M_beta_first") ] ,
    #[plotnames.index( "ABCD_notopbtag_CatE_Zprime_M_beta_first") , plotnames.index( "ABCD_notopbtag_CatF_Zprime_M_beta_first")],
    #[plotnames.index( "ABCD_notopbtag_CatA_Zprime_M_first") , plotnames.index("ABCD_notopbtag_CatB_Zprime_M_first") ] ,
    #[plotnames.index( "ABCD_notopbtag_CatE_Zprime_M_first") , plotnames.index( "ABCD_notopbtag_CatF_Zprime_M_first")]]





### For BackgroundSamples
#WASLnames2 =[]
#for string in WAPlotNames:
    #for sample in SampleNames:
        #WASLnames2.append( string + "_" + sample )

#RatioPlotList = transposeLOLextended( listOfHistoListsABCD,  IndexListToTranspose)
#writeListOfHistoLists( RatioPlotList , WASamples ,  WASLnames2 , 'RatioPlotList' , False , False, False, "histoE", False, False, True, False)



####Print all Plots for Z_Prime (Signal)
##WASignalSamplePlotNames2=[]
##for string in WAPlotNames:
    ##for sample in SignalSampleNames:
        ##WASignalSamplePlotNames2.append( string + "_" + sample)

##RatioPlotListSignal = transposeLOLextended( listOfHistoListsSignal, IndexListToTranspose )
##writeListOfHistoLists( RatioPlotListSignal , WASamples , WASignalSamplePlotNames2 , 'RatioPlotListSignal' , False , False, False, "histoE", False, False, True, False)




##RatioPlots for Combined Background and Signal Sample
#WASignalSamplePlotNameListOfLists=[]
#for SignalSampleName in SignalSampleNames:
    #ListToAppend=[]
    #for PlotName in WAPlotNames:
        #for SampleName in SampleNames:
            #ListToAppend.append(SignalSampleName+SampleName+PlotName)
    #WASignalSamplePlotNameListOfLists.append(ListToAppend)

#for WASignalSamplePlotNameList, SignalSampleName, listOfHistoListSignalAndBackground in zip(WASignalSamplePlotNameListOfLists, SignalSampleNames, listOfHistoListsSignalAndBackground):
    #RatioPlotListComb = transposeLOLextended( listOfHistoListSignalAndBackground, IndexListToTranspose )
    #writeListOfHistoLists( RatioPlotListComb , WASamples , WASignalSamplePlotNameList , 'RatioPlotListComb'+SignalSampleName , False , False, False, "histoE", False, False, True, False)




#### RatioPlots and Error Fit Polinomial , A/B - Signal over Background
##for WASignalSamplePlotNameList, SignalSampleName, listOfHistoListSignalAndBackground in zip(WASignalSamplePlotNameListOfLists, SignalSampleNames, listOfHistoListsSignalAndBackground):
    ##RatioPlotListComb = transposeLOLextended( listOfHistoListSignalAndBackground, IndexListToTranspose )
    ##ListOfPureRatioPlots = []
    ##for HistoList in RatioPlotListComb:
        ##HistoList[0].Divide(HistoList[1])
        ##ListOfPureRatioPlots.append( [HistoList[0] ]  )
    ### writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol2_"+SignalSampleName, 1, "pol2", WASignalSamplePlotNameList, True)
    ##writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol0_"+SignalSampleName, 1, "pol0", WASignalSamplePlotNameList, True)
    ### writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol0_"+SignalSampleName, 1, "pol0", WASignalSamplePlotNameList, True)


### Ratio Plot with Errors, A/B - Signal over Background, without Signalcontamination
#ListOfPureRatioPlots=[]
#for histoList in RatioPlotList:
    #histoList[0].Divide(histoList[1])
    #ListOfPureRatioPlots.append( [histoList[0] ])
#writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol0_Background", 1, "pol0", WASLnames2, True)
## writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol2_Background", 1, "pol2", WASLnames2, True)
## writeHistoListwithXYErrors(ListOfPureRatioPlots, [ WASamples[0] ], "RatioPlotFit_pol0_Background", 1, "pol0", WASLnames2, True)




### Uncomple STACK PLOT


####Modify Signal And Background listOfHistoList (substract from backgroundprediction)
##for index in range( plotnames.index("ABCD_notopbtag_CatA_Zprime_M"),plotnames.index("ABCD_notopbtag_CatH_Zprime_M_first") +1):
    ##if plotnames[index][8] =="B":
        ##listOfHistoListsSignalAndBackground25001200[index][1].Add(listOfHistoListsABCD[index][1], -1)
        ###listOfHistoListsSignalAndBackground25001200[index][1].Multiply(-1)

        ##listOfHistoListsSignalAndBackground25001200[index-1][1].Add(listOfHistoListsABCD[index-1][0])#Add to Signal and QCD-Background in Signal ttbar in Signal Region

####Create a hISTOlIST TO DO stackPlotABCD
##ListOfHistoListsFinalStackPlot = []
##titlelist = []
##for index in range( plotnames.index("ABCD_notopbtag_CatA_Zprime_M"), plotnames.index("ABCD_notopbtag_CatH_Zprime_M_first") +1):
    ##if plotnames[index][8] =="A":
        ##ListToAppend = []
        ##titlelist.append( listOfHistoListsABCD[index][0].GetName()[5:] )
        ##ListToAppend.append(listOfHistoListsSignalAndBackground25001200[index+1][0]) #Signal
        ##ListToAppend.append(listOfHistoListsSignalAndBackground25001200[index+1][1]) #Signalkontamination
        ##ListToAppend.append(listOfHistoListsABCD[index+1][1]) #QCD_HAT in CatB
        ##ListToAppend.append(listOfHistoListsABCD[index][0]) #ttbar in Signal Region
        ##ListOfHistoListsFinalStackPlot.append(ListToAppend)

##colorlist =[ ROOT.kBlack , ROOT.kRed, ROOT.kYellow,ROOT.kBlue]
##stacklist = [False, True, True, True]
##optionlist = ["E", "histoE", "histoE", "histoE"]
##stackPlotABCD(ListOfHistoListsFinalStackPlot, "StackPlotsABCD", colorlist=colorlist, labellist=["ttbar", "QCD-Backgroundestimation", "Signalcontamination", "Signal"], titlelist = titlelist, stacklist = stacklist, optionlist = optionlist)

##print "Plotnames contains:"
##for i in plotnames:
    ##print i
    
    
    
    
#Anmerkungen fuer Simon:
#Das Skript erzeugt die folgenden Dateien:
#
#Integrallist_before_multiplication.tex
#2D Histogramme in Ordner "ABCD_2D"
#Correlationfactors.tex
#Integrallist_after_multiplication.tex
#Rekonstruktion von Kategoie A und E in "RatioPlotList"
#Signalkontamination in "RatioPlotListComb"+SignalSampleName
#Fehlerbaender in "RatioPlotFit_pol0_Background"
