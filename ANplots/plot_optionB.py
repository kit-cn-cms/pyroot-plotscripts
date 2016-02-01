import sys
import os
sys.path.insert(0, '../limittools')
sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import makeDatacards
from limittools import calcLimits
from plotconfig import *

name='optionB'

nhistobins=      [ 10,10,          4,4 ,        10,10,         4,4,       16,    10,10,  6,6     ]
minxvals=        [0.]*8 + [-.8] + [0.]*4
maxxvals=        [.95]*8 + [.8] + [.95]*4
discrs =          ["((MEM_p_sig>0)*MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))"]*8+['BDT_common5_output']+['((MEM_p_sig>0)*MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))']*4
discrnames= ["MEM discriminator"]*8+["BDT discriminator"]+4*["MEM discriminator"]
categories_=[("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3","4 jets, 3 b-tags category"),
            ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4","4 jets, 4 b-tags category"),
            ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3","5 jets, 3 b-tags category"),
            ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4","5 jets, #geq4 b-tags category"),
            ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2","#geq6 jets, 2 b-tags category"),
            ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3","#geq6 jets, 3 b-tags category"),
            ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4","#geq6 jets, #geq4 b-tags category")]
categories=[]

bdtcuts=[0.2,0.2,0.15,
         0.2,0.1,0.1,0.1]

for cat,bdt in zip(categories_,bdtcuts):
  if cat[1]=='ljets_jge6_t2':
    categories.append(cat)
  else:
    categories.append(('('+cat[0]+')*(BDT_common5_output>'+str(bdt)+')',cat[1]+'_low',cat[2]+', BDT <= '+str(bdt)) )
    categories.append(('('+cat[0]+')*(BDT_common5_output<='+str(bdt)+')',cat[1]+'_high',cat[2]+', BDT > '+str(bdt)) )

print categories


discrname='BDT'

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
bintitles= [c[2] for c in categories]

samples=samplesLimits
allsystnames=weightsystnames+othersystnames

systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),sample.selection,sample.nick+sysname))
  
allsamples=samples+systsamples

bdts=[]
for discr,b,bl,bt,nb,minx,maxx in zip(discrs,bins,binlabels,bintitles,nhistobins,minxvals,maxxvals):
  if '.xml' in discr:
    bdts.append(MVAPlot(ROOT.TH1F(discrname+"_"+bl,"BDT discriminator w/o MEM in "+bt,nb,minx,maxx),discr,b))
  else:
    bdts.append(Plot(ROOT.TH1F(discrname+"_"+bl,"MEM discriminator in "+bt,nb,minx,maxx),discr,b))

outputpath=plotParallel(name,500000,bdts,allsamples,[''],['1.'],weightsystnames, systweights)
if not os.path.exists(name):
  os.makedirs(name)

renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames)
addPseudoData(name+'/'+name+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts)
lolT=transposeLOL(listOfHistoLists)
writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],20,name+'/'+name+'_controlplots')
makeDatacards(name+'/'+name+'_limitInput.root',name+'/'+name+'_datacard',binlabels)

#if askYesNo('Calculate limits?'):
limit=calcLimits(name+'/'+name+'_datacard',binlabels)
limit.dump()
