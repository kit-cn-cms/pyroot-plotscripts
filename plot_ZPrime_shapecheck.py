#############
# plot general control distributions
##############

from plotconfig_Zprime_DATA_Lena import *
from plot_additional_Zprime_DATA_Lena import *
from plot_cuts_ZPrime_MC_Lena import *
sys.path.insert(0, 'limittools')
from limittools import renameHistos
import copy



ABCDeventhandling='oncefirst'
#ABCDeventhandling='reweight'

name='Zprime_MC_ABCD_shapecheck'+radi+'_'+ABCDeventhandling+'_'+WPs
SampleNames=['ttbar' , 'QCD_HT', 'QCD_Pt' ]
SignalSampleNames=['Zprime1500900',  'Zprime20001200',  'Zprime25001200']




#Create Plots

plots=[

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

]






plotnames=[]
for i in plots:
    plotnames.append(i.name)


OnlyFirstList=len(plots)*[False]
#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
OnlyFirstList[plotnames.index("ABCD5_notopbtag_CatA_Zprime_M_beta_first"):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first') +1 ] = len(OnlyFirstList[plotnames.index("ABCD5_notopbtag_CatA_Zprime_M_beta_first"):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first') + 1 ] ) * [True]

print OnlyFirstList, 'This is the boolean List for only first elements'

#print 'length of OnlyFirstList=', len(OnlyFirstList), ' length of plots=', len(plots)
assert len(OnlyFirstList)==len(plots)
#raw_input()




print name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples,[''],['1.']
#outputpath=plotParallel(name,4000000,plots,samples)
outputpath=plotParallel(name,2000000,plots,SignalSamples+BackgroundSamples+DataSamples, [''], ['1'] , weigthsystnamesMCSFs, systweightnamesMCSFs,additionalvariables,additionalfunctions,additionalobjectsfromaddtionalrootfile,OnlyFirstList)

listOfHistoListsABCD=createHistoLists_fromSuperHistoFile(outputpath,DataSamples ,plots,1,[""], True )
listOfHistoListsABCDttbar=createHistoLists_fromSuperHistoFile(outputpath,[BackgroundSamples[0]] ,plots,1,[""], True )
listOfHistoListsABCDQCD=createHistoLists_fromSuperHistoFile(outputpath,[BackgroundSamples[1]] ,plots,1,[""], True )

Datalll=createLLL_fromSuperHistoFileSyst(outputpath,DataSamples,plots,weigthsystnamesMCSFs)
ttbarlll=createLLL_fromSuperHistoFileSyst(outputpath,[BackgroundSamples[0]],plots,weigthsystnamesMCSFs)


#for lol in listOfHistoListsSignalAndBackground:
    #print lol[0][0], "Sind die pointer anders fuer die verschiedenen listOfHistoLists?"

labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)



print plotnames
#raw_input()

lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD,False,False,False,True)

#lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD)
listOfHistoListsABCD=lolABCD_rebinned
lolABCDttbar_rebinned=rebintovarbinsLOL(listOfHistoListsABCDttbar,False,False,False,True)
listOfHistoListsABCDttbar=lolABCDttbar_rebinned
lolABCDQCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCDQCD,False,False,False,True)
listOfHistoListsABCDQCD=lolABCDQCD_rebinned


Datalll=rebintovarbinsLLL(Datalll,False,False,False,False)
ttbarlll=rebintovarbinsLLL(ttbarlll,False,False,False,False)


#chekcNbins(listOfHistoListsABCD)


#lolBackgroundT=transposeLOL(listOfHistoListsBackground)
lolABCDT=transposeLOL(listOfHistoListsABCD)
lolABCDttbarT=transposeLOL(listOfHistoListsABCDttbar)
#lolDataT=transposeLOL(listOfHistoListsData)

#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_notopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)
#SchmonCorrelation(transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("ABCD_withtopbtag_CatA_Zprime_M_beta_first")],transposeLOL(transposeLOL(listOfHistoListsABCD)[BackgroundSampleNames.index('QCD_HT'):BackgroundSampleNames.index('QCD_PT')+1])[plotnames.index("Signal_withtopbtag_Topfirst_Zprime_M")],name='SchmonCorrelation', rebin=1)


#lolABCD_rebinned=rebintovarbinsLOL(listOfHistoListsABCD)

#chekcNbins(lolABCD_rebinned)

subtract_lols(listOfHistoListsABCD,listOfHistoListsABCDttbar)
subtract_llls(Datalll,ttbarlll)



print Datalll

DataLoL=[]

for ll,plotname in zip(Datalll,plotnames):
    templ=[]
    for l in ll:
        for h,systname in zip(l,weigthsystnamesMCSFs):
          for ABCDversion in ['ABCD5']:
            if ABCDversion in plotname and ABCDversion in systname:
                print "if ",h, "    ", systname, "    " ,plotname , "      ", h.Integral()
                templ.append(h)
    DataLoL.append(templ)
    
    
print Datalll

print "right? ",  DataLoL



datalol=copy.deepcopy(DataLoL)
datalol2=copy.deepcopy(DataLoL)
divideHistos(datalol, plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatF_Zprime_M_beta_first'))
divideHistos(datalol2, plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatG_Zprime_M_beta_first'))
divideHistos(datalol, plotnames.index('ABCD5_withtopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatF_Zprime_M_beta_first'))
divideHistos(datalol2, plotnames.index('ABCD5_withtopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatG_Zprime_M_beta_first'))

#datalol2=copy.deepcopy(DataLoL)
#divideHistos(datalol2, plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatG_Zprime_M_beta_first'))
#divideHistos(datalol2, plotnames.index('ABCD5_withtopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatF_Zprime_M_beta_first'))


divideHistos(DataLoL, plotnames.index('ABCD5_notopbtag_CatB_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatD_Zprime_M_beta_first'))
divideHistos(DataLoL, plotnames.index('ABCD5_notopbtag_CatC_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatD_Zprime_M_beta_first'))
divideHistos(DataLoL, plotnames.index('ABCD5_withtopbtag_CatB_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatD_Zprime_M_beta_first'))
divideHistos(DataLoL, plotnames.index('ABCD5_withtopbtag_CatC_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatD_Zprime_M_beta_first'))

divideHistos(DataLoL, plotnames.index('ABCD5_notopbtag_CatF_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatH_Zprime_M_beta_first'))
divideHistos(DataLoL, plotnames.index('ABCD5_notopbtag_CatG_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatH_Zprime_M_beta_first'))
divideHistos(DataLoL, plotnames.index('ABCD5_withtopbtag_CatF_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first'))
divideHistos(DataLoL, plotnames.index('ABCD5_withtopbtag_CatG_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first'))


writeListOfHistoLists(transposeLOL([transposeLOL(DataLoL)[0]])[plotnames.index('ABCD5_notopbtag_CatB_Zprime_M_beta_first'):plotnames.index('ABCD5_notopbtag_CatH_Zprime_M_beta_first')+1],[DataSamples[0]], '','shapecomparison_'+name,False,False,False,'histoE')
writeListOfHistoLists(transposeLOL([transposeLOL(DataLoL)[0]])[plotnames.index('ABCD5_withtopbtag_CatB_Zprime_M_beta_first'):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first')+1],[DataSamples[0]], '','shapecomparison_'+name,False,False,False,'histoE')

writeListOfHistoLists([transposeLOL([transposeLOL(datalol)[0]])[plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first')]],[DataSamples[0]], '','shapecomparison2_'+name+'_overF',False,False,False,'histoE')
writeListOfHistoLists([transposeLOL([transposeLOL(datalol2)[0]])[plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first')]],[DataSamples[0]], '','shapecomparison2_'+name+'_overG',False,False,False,'histoE')
writeListOfHistoLists([transposeLOL([transposeLOL(datalol)[0]])[plotnames.index('ABCD5_withtopbtag_CatE_Zprime_M_beta_first')]],[DataSamples[0]], '','shapecomparison2_'+name+'_overF',False,False,False,'histoE')
writeListOfHistoLists([transposeLOL([transposeLOL(datalol2)[0]])[plotnames.index('ABCD5_withtopbtag_CatE_Zprime_M_beta_first')]],[DataSamples[0]], '','shapecomparison2_'+name+'_overG',False,False,False,'histoE')




print listOfHistoListsABCDQCD

LOL_ABCDQCD=copy.deepcopy(listOfHistoListsABCDQCD)
LOL_ABCDQCD2=copy.deepcopy(listOfHistoListsABCDQCD)
divideHistos(LOL_ABCDQCD, plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatF_Zprime_M_beta_first'))
divideHistos(LOL_ABCDQCD2, plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatG_Zprime_M_beta_first'))
divideHistos(LOL_ABCDQCD, plotnames.index('ABCD5_withtopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatF_Zprime_M_beta_first'))
divideHistos(LOL_ABCDQCD2, plotnames.index('ABCD5_withtopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatG_Zprime_M_beta_first'))

#datalol2=copy.deepcopy(DataLoL)
#divideHistos(datalol2, plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatG_Zprime_M_beta_first'))
#divideHistos(datalol2, plotnames.index('ABCD5_withtopbtag_CatE_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatF_Zprime_M_beta_first'))


divideHistos(listOfHistoListsABCDQCD, plotnames.index('ABCD5_notopbtag_CatB_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatD_Zprime_M_beta_first'))
divideHistos(listOfHistoListsABCDQCD, plotnames.index('ABCD5_notopbtag_CatC_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatD_Zprime_M_beta_first'))
divideHistos(listOfHistoListsABCDQCD, plotnames.index('ABCD5_withtopbtag_CatB_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatD_Zprime_M_beta_first'))
divideHistos(listOfHistoListsABCDQCD, plotnames.index('ABCD5_withtopbtag_CatC_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatD_Zprime_M_beta_first'))

divideHistos(listOfHistoListsABCDQCD, plotnames.index('ABCD5_notopbtag_CatF_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatH_Zprime_M_beta_first'))
divideHistos(listOfHistoListsABCDQCD, plotnames.index('ABCD5_notopbtag_CatG_Zprime_M_beta_first'), plotnames.index('ABCD5_notopbtag_CatH_Zprime_M_beta_first'))
divideHistos(listOfHistoListsABCDQCD, plotnames.index('ABCD5_withtopbtag_CatF_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first'))
divideHistos(listOfHistoListsABCDQCD, plotnames.index('ABCD5_withtopbtag_CatG_Zprime_M_beta_first'), plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first'))


writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCDQCD)[0]])[plotnames.index('ABCD5_notopbtag_CatB_Zprime_M_beta_first'):plotnames.index('ABCD5_notopbtag_CatH_Zprime_M_beta_first')+1],[BackgroundSamples[1]], '','shapecomparison_'+name,False,False,False,'histoE')
writeListOfHistoLists(transposeLOL([transposeLOL(listOfHistoListsABCDQCD)[0]])[plotnames.index('ABCD5_withtopbtag_CatB_Zprime_M_beta_first'):plotnames.index('ABCD5_withtopbtag_CatH_Zprime_M_beta_first')+1],[BackgroundSamples[1]], '','shapecomparison_'+name,False,False,False,'histoE')

writeListOfHistoLists([transposeLOL([transposeLOL(LOL_ABCDQCD)[0]])[plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first')]],[BackgroundSamples[1]], '','shapecomparison2_'+name+'_overF',False,False,False,'histoE')
writeListOfHistoLists([transposeLOL([transposeLOL(LOL_ABCDQCD2)[0]])[plotnames.index('ABCD5_notopbtag_CatE_Zprime_M_beta_first')]],[BackgroundSamples[1]], '','shapecomparison2_'+name+'_overG',False,False,False,'histoE')
writeListOfHistoLists([transposeLOL([transposeLOL(LOL_ABCDQCD)[0]])[plotnames.index('ABCD5_withtopbtag_CatE_Zprime_M_beta_first')]],[BackgroundSamples[1]], '','shapecomparison2_'+name+'_overF',False,False,False,'histoE')
writeListOfHistoLists([transposeLOL([transposeLOL(LOL_ABCDQCD2)[0]])[plotnames.index('ABCD5_withtopbtag_CatE_Zprime_M_beta_first')]],[BackgroundSamples[1]], '','shapecomparison2_'+name+'_overG',False,False,False,'histoE')

