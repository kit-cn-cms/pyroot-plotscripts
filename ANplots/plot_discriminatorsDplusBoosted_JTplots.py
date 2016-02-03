import sys
import os
sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *
from plotconfig import *
sys.path.insert(0, '../limittools')
from limittools import renameHistos

name='discrplotsDplusBoosted_JTplots'

sel_singleel="(N_LooseMuons==0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)" # and vice versa...

mcweight='2.0*2.61*(Evt_Odd==0)'
nhistobins_=      [ 20,       4,   4,     20,       4,     4,   20,   20,  6 ,6    ]
minxvals_=        [-0.9,    0.,  0.,     -0.8,     0.,     0.,   -0.80,  -0.8,  0.,   0.]
maxxvals_=        [0.8,     .95,   0.95,  0.8,    0.95,   0.95,    0.76,   0.8,   0.95,    0.95]
discrs =          ['/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_43_MEMBDTv2.xml', 'MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)','MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_53_MEMBDTv2.xml', 'MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)' ,'MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)' , 'BDT_common5_output','/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_63_MEMBDTv2.xml','MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)','MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)']

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
categories_=[ ("(N_Jets==4&&N_BTagsM==3)&&!"+boosted,"ljets_j4_t3","4 jets, 3 b-tags category"),
              ("(N_Jets==4&&N_BTagsM>=4)&&!"+boosted,"ljets_j4_t4","4 jets, 4 b-tags category"),
              ("(N_Jets==5&&N_BTagsM==3)&&!"+boosted,"ljets_j5_t3","5 jets, 3 b-tags category"),
              ("(N_Jets==5&&N_BTagsM>=4)&&!"+boosted,"ljets_j5_tge4","5 jets, #geq4 b-tags category"),
              ("(N_Jets>=6&&N_BTagsM==2)&&!"+boosted,"ljets_jge6_t2","#geq6 jets, 2 b-tags category"),
              ("(N_Jets>=6&&N_BTagsM==3)&&!"+boosted,"ljets_jge6_t3","#geq6 jets, 3 b-tags category"),
              ("(N_Jets>=6&&N_BTagsM>=4)&&!"+boosted,"ljets_jge6_tge4","#geq6 jets, #geq4 b-tags category")]
              
categories=[]
bdtcuts=[0.2,0.2,0.1,0.2,0.1,0.1,0.1]

for cat,bdt in zip(categories_,bdtcuts):
  if "4 b-tags" in cat[2]:
    categories.append(('('+cat[0]+')*(BDT_common5_output>'+str(bdt)+')', cat[1]+'_high',cat[2]+' BDT > '+str(bdt)) )
    categories.append(('('+cat[0]+')*(BDT_common5_output<='+str(bdt)+')', cat[1]+'_low',cat[2]+' BDT <= '+str(bdt)) )
  else:
    categories.append(cat )
  
  print categories[-1]
  print len(categories[-1])
  
#print categories

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
binnames= [c[2] for c in categories]

samples=samplesBDTplots
samples_data=samples_data_bdtplots
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),sample.selection,sample.nick+sysname))
allsamples=samples+systsamples
allsystnames=weightsystnames+othersystnames

plots=[]
#print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
#print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,bn,nb,minx,maxx in zip(discrs,bins,binlabels,binnames,nhistobins,minxvals,maxxvals):
  if '.xml' in discr:
    plots.append(MVAPlot(ROOT.TH1F("BDT_"+bl,"BDT containing MEM",nb,minx,maxx),discr,b,bl))
  elif 'common5' in discr:
    plots.append(Plot(ROOT.TH1F("BDT_"+bl,"BDT discriminator",nb,minx,maxx),discr,b,bl))
  else:
    plots.append(Plot(ROOT.TH1F("BDT_"+bl,"MEM discriminator",nb,minx,maxx),discr,b,bl))
  
  print discr,b,bl,nb,minx,maxx


# plot parallel -- alternatively there are also options to plot more traditional that also return lists of histo lists
outputpath=plotParallel(name,2000000,plots,samples+samples_data+systsamples,[''],['1.'],weightsystnames, systweights)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames)

lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,allsystnames)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name,lll,False,labels,True,True)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,allsystnames)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name+'_log',lll,True,labels,True,True)
