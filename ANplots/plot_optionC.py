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

name='optionC'

nhistobins_=      [ 20,       10,     20,       10,   20,   20,  10    ]
minxvals_=        [-0.9,   -0.35,  -0.8, -0.75,   -0.80,  -0.8, -0.6]
maxxvals_=        [0.8,     0.5,  0.8,    0.75,    0.76,   0.8,   0.7]
discrs =          ['/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_43_MEMBDTv2.xml', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_44_MEMBDTv2.xml', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_53_MEMBDTv2.xml', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_54_MEMBDTv2.xml' , 'BDT_common5_output','/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_63_MEMBDTv2.xml','/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_64_MEMBDTv2.xml']

nhistobins=[]
minxvals=[]
maxxvals=[]
for n in nhistobins_:
  nhistobins.append(n)
for x in minxvals_:
  minxvals.append(x)
for x in maxxvals_:
  maxxvals.append(x)

categories_=[("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3"),
            ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4"),
            ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3"),
            ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4"),
            ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2"),
            ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3"),
            ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4")]
categories=[]
bdtcuts=[0.2,0.2,0.1,0.2,0.1,0.1,0.1]

for cat,bdt in zip(categories_,bdtcuts):
    categories.append(cat )
print categories


discrname='BDT'

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]

samples=samplesLimits
allsystnames=weightsystnames+othersystnames

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
    bdts.append(MVAPlot(ROOT.TH1F(discrname+"_"+bl,"final dicsriminator ("+bl+")",nb,minx,maxx),discr,b))
  else:
    bdts.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final dicsriminator ("+bl+")",nb,minx,maxx),discr,b))
  print discr,b,bl,nb,minx,maxx

#print "if cateries are correct press the \"any\" key"
#raw_input()

outputpath=plotParallel(name,1000000,bdts,allsamples,[''],['1.'],weightsystnames, systweights)
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
  
