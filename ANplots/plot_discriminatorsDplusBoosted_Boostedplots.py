import sys
import os
sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *
from plotconfig import *
sys.path.insert(0, '../limittools')
from limittools import renameHistos


path_karim='/nfs/dust/cms/user/kelmorab/Samples05022016/'

samples_data_controlplots=[Sample('SingleMu',ROOT.kBlack,path_karim+'/mu_*/*nominal*.root',sel_singlemu,'SingleMu'),
                           Sample('SingleEl',ROOT.kBlack,path_karim+'/el_*/*nominal*.root',sel_singleel,'SingleEl')
                       ]

samplesControlPlots=[Sample('t#bar{t}H',ROOT.kBlue+1,path_karim+'/ttH*/*nominal*.root',mcweight,'ttH',systs_all_samples) ,     
#         Sample('t#bar{t}',ROOT.kRed+1,path_incl4252+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
         Sample('t#bar{t}+lf',ROOT.kRed-7,path_karim+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther',systs_all_samples+systs_ttbar+systs_tt_lf,0.05),
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path_karim+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar',systs_all_samples+systs_ttbar+systs_tt_cc,0.5),
         Sample('t#bar{t}+b',ROOT.kRed-2,path_karim+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB',systs_all_samples+systs_ttbar+systs_tt_b,0.5),
         Sample('t#bar{t}+2b',ROOT.kRed+2,path_karim+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B',systs_all_samples+systs_ttbar+systs_tt_2b,0.5),
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path_karim+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar',systs_all_samples+systs_ttbar+systs_tt_bb,0.5),  
         Sample('Single Top',ROOT.kMagenta,path_karim+'/st*/*nominal*.root',mcweight,'SingleTop',systs_all_samples) , 
         Sample('V+jets',ROOT.kGreen-3,path_karim+'/??ets*/*nominal*.root',mcweight,'Vjets',systs_all_samples) , 
         Sample('t#bar{t}+V',ROOT.kBlue-10,path_karim+'/tt?_*/*nominal*.root',mcweight,'ttV',systs_all_samples),         
         Sample('Diboson',ROOT.kAzure+2,path_karim+'/??/*nominal*.root',mcweight,'Diboson',systs_all_samples) , 
#         Sample('QCD',ROOT.kYellow ,path_incl4252+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

name='newdiscrplotsDplusBoosted_Boostedplots_withRates'

sel_singleel="(N_LooseMuons==0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)" # and vice versa...

mcweight='2.0*2.61*(Evt_Odd==0)'
nhistobins_=  [   8]
minxvals_=    [-0.7]
maxxvals_=    [ 0.8]
discrs =      ["/nfs/dust/cms/user/shwillia/BoostedTTHScripts/LimitCalculation/Setup_160127/pyroot-plotscripts/ANplots/weights/FinalBDT_Setup_160127_WP2_CombDiscr_PSOttbbDiscr_PSO_BDTG.weights.xml"]

nhistobins=[]
minxvals=[]
maxxvals=[]
for n in nhistobins_:
  nhistobins.append(n)
for x in minxvals_:
  minxvals.append(x)

for x in maxxvals_:
  maxxvals.append(x)


boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.575&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.9075)"
categories=[("(N_Jets>=4&&N_BTagsM>=2)&&"+boosted ,"ljets_boosted","boosted category")]

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
binnames= [c[2] for c in categories]


# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samples_data=samples_data_controlplots
systsamples=[]
samples=samplesControlPlots
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),sample.selection,sample.nick+sysname))
  
allsamples=samples+systsamples
allsystnames=weightsystnames+othersystnames

plots=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,bn,nb,minx,maxx in zip(discrs,bins,binlabels,binnames,nhistobins,minxvals,maxxvals):
  if '.xml' in discr:
    plots.append(MVAPlot(ROOT.TH1F("BDT_"+bl,"BDT discriminator",nb,minx,maxx),discr,b,bl))
  elif 'common5' in discr:
    plots.append(Plot(ROOT.TH1F("BDT_"+bl,"BDT discriminator",nb,minx,maxx),discr,b,bl))
  else:
    plots.append(Plot(ROOT.TH1F("BDT_"+bl,"MEM discriminator",nb,minx,maxx),discr,b,bl))
  print discr,b,bl,nb,minx,maxx


# plot parallel -- alternatively there are also options to plot more traditional that also return lists of histo lists
#outputpath=plotParallel(name,2000000,plots,samples+samples_data)
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
#labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)
#plotDataMCan(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name,False,labels,True,True)

#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
#labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)
#plotDataMCan(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name+'_log',True,labels,True,True)


outputpath=plotParallel(name,2000000,plots,samples+samples_data+systsamples,[''],['1.'],weightsystnames, systweights)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames)
print othersystnames
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,allsystnames)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name,[[lll,3354,ROOT.kGray+1,True]],False,labels,True,True)

lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,allsystnames)
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name+'_log',[[lll,3354,ROOT.kGray+1,True]],True,labels,True,True)