import sys
import os
sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *
from plotconfig import *

name='discrplotsB'
sel_singleel="(N_LooseMuons==0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)" # and vice versa...

nhistobins=      [ 10,10,          4,4 ,        10,10,         4,4,       16,    10,10,  6,6     ]
minxvals=        [0.]*8 + [-.8] + [0.]*4
maxxvals=        [.95]*8 + [.8] + [.95]*4
discrs =          ["((MEM_p_sig>0)*MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))"]*8+['BDT_common5_output']+['((MEM_p_sig>0)*MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))']*4
discrnames= ["MEM discriminator"]*8+["BDT discriminator"]+4*["MEM discriminator"]
categories_=[("(N_Jets==4&&N_BTagsM==3)","4 jets, 3 b-tags","s43"),
            ("(N_Jets==4&&N_BTagsM>=4)","4 jets, #geq4 b-tags","s44"),
            ("(N_Jets==5&&N_BTagsM==3)","5 jets, 3 b-tags","s53"),
            ("(N_Jets==5&&N_BTagsM>=4)","5 jets, #geq4 b-tags","s54"),
            ("(N_Jets>=6&&N_BTagsM==2)","#geq6 jets, 2 b-tags","s62"),
            ("(N_Jets>=6&&N_BTagsM==3)","#geq6 jets, 3 b-tags","s63"),
            ("(N_Jets>=6&&N_BTagsM>=4)","#geq6 jets, #geq4 b-tags","s64")]
categories=[]

bdtcuts=[0.2,0.2,0.15,
         0.2,0.1,0.1,0.1]

for cat,bdt in zip(categories_,bdtcuts):
  if cat[2]=='s62':
    categories.append(cat)
  else:
    categories.append(('('+cat[0]+')*(BDT_common5_output>'+str(bdt)+')',cat[1]+', BDT <= '+str(bdt),cat[2]+'_low',) )
    categories.append(('('+cat[0]+')*(BDT_common5_output<='+str(bdt)+')',cat[1]+', BDT > '+str(bdt),cat[2]+'_high',) )

print categories


discrname='BDT'

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
bintitles= [c[2] for c in categories]

# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samples_data=samples_data_bdtplots

# mc samples
samples=SamplesBDTplots
plots=[]
for discr,b,bl,bt,nb,minx,maxx in zip(discrs,bins,binlabels,bintitles,nhistobins,minxvals,maxxvals):
  if 'common5' in discr:
    plots.append(Plot(ROOT.TH1F("BDT_"+bt,"BDT discriminator",nb,minx,maxx),discr,b,bl))
  else:
    plots.append(Plot(ROOT.TH1F("BDT_"+bt,"MEM dicsriminator",nb,minx,maxx),discr,b,bl))


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
