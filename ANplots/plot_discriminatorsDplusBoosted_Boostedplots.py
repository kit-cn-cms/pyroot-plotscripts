import sys
import os
sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *
from plotconfig import *

name='discrplotsDplusBoosted_Boostedplots'

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
samples_data=samples_data_bdtplots

samples=samplesBDTplotsBoosted

plots=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,bn,nb,minx,maxx in zip(discrs,bins,binlabels,binnames,nhistobins,minxvals,maxxvals):
  if '.xml' in discr:
    plots.append(MVAPlot(ROOT.TH1F("BDT_"+bl,"BDT containing MEM",nb,minx,maxx),discr,b,bl))
  elif 'common5' in discr:
    plots.append(Plot(ROOT.TH1F("BDT_"+bl,"BDT discriminator",nb,minx,maxx),discr,b,bl))
  else:
    plots.append(Plot(ROOT.TH1F("BDT_"+bl,"MEM discriminator",nb,minx,maxx),discr,b,bl))
  print discr,b,bl,nb,minx,maxx


# plot parallel -- alternatively there are also options to plot more traditional that also return lists of histo lists
outputpath=plotParallel(name,2000000,plots,samples+samples_data)
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCan(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name,False,labels,True,True)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCan(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name+'_log',True,labels,True,True)
