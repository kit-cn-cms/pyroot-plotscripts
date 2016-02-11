import sys
import os
sys.path.insert(0, '../limittools')
sys.path.insert(0, '../')

from scriptgeneratorSubBDT import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import makeDatacards
from limittools import calcLimits
from plotconfig import *


name='newBDToptionDplusBoosted_Boostedplots'

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
              
discrname='BDT'

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
samples=samplesLimitsBoosted

allsystnames=weightsystnames+othersystnames

# corresponding weight names
pdfweightscalefactor=1.0

systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),sample.selection,sample.nick+sysname))
  
allsamples=samples+systsamples

bdts=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,nb,minx,maxx in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals):
    
  if '.xml' in discr:
    bdts.append(MVAPlot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b))
  else:
    bdts.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b))
  print discr,b,bl,nb,minx,maxx

#print "if cateries are correct press the \"any\" key"
#raw_input()

outputpath=plotParallel(name,1000000,bdts,allsamples,[''],['1.'],weightsystnames, systweights)
if not os.path.exists(name):
  os.makedirs(name)

renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts)
lolT=transposeLOL(listOfHistoLists)
writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],20,name+'/'+name+'_controlplots')
