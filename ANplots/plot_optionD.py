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


#print "!!! NO MEMS ANYWHERE FOR TEST REASONS !!!"
#print "!!! NO BOOSTED ANYWHERE FOR TEST REASONS !!!"

name='76xBDToptionD'

bdtweightpath="/nfs/dust/cms/user/kelmorab/76xBDTWeights/"
memexp='(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)'
#memexp='1.0'


nhistobins_=      [ 20,        4,      4,    	 20,    	4,     	4,    	20,   	20,  	6,       6, 	10    ]
minxvals_=        [ -0.9,       0.,     0.,    -0.85,    	0.,    	0.,   	-0.8,  -0.8,   	0.,      0., 	-0.9  ]
maxxvals_=        [ 0.85, 0.9, 0.9, 0.825,0.95,0.95,0.75,0.85,0.95,0.95,0.825 ] 

discrs =          [bdtweightpath+'/weights_Final_43_76mem.xml', memexp, memexp, bdtweightpath+'/weights_Final_53_76mem.xml',memexp , memexp, bdtweightpath+'/weights_Final_62_76blr2.xml',bdtweightpath+'/weights_Final_63_76mem.xml',memexp, memexp,bdtweightpath+'/weights_Final_DB_boosted_76xmem.xml']

nhistobins=[]
minxvals=[]
maxxvals=[]
for n in nhistobins_:
  nhistobins.append(n)
for x in minxvals_:
  minxvals.append(x)

for x in maxxvals_:
  maxxvals.append(x)

boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.485&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.8925)"                        
categories_=[("(N_Jets==4&&N_BTagsM==3)&&!"+boosted+"","ljets_j4_t3"),
            ("(N_Jets==4&&N_BTagsM>=4)&&!"+boosted+"","ljets_j4_t4"),
            ("(N_Jets==5&&N_BTagsM==3)&&!"+boosted+"","ljets_j5_t3"),
            ("(N_Jets==5&&N_BTagsM>=4)&&!"+boosted+"","ljets_j5_tge4"),
            ("(N_Jets>=6&&N_BTagsM==2)&&!"+boosted+"","ljets_jge6_t2"),
            ("(N_Jets>=6&&N_BTagsM==3)&&!"+boosted+"","ljets_jge6_t3"),
            ("(N_Jets>=6&&N_BTagsM>=4)&&!"+boosted+"","ljets_jge6_tge4"),
            (boosted,"ljets_boosted")]
categories=[]
bdtcuts=[0.2,0.2,0.1,0.2,0.1,0.1,0.1,0.2]

for cat,bdt in zip(categories_,bdtcuts):
  if cat[1] in ["ljets_jge6_tge4","ljets_j5_tge4","ljets_j4_t4"]:
    categories.append(('('+cat[0]+')*(splitdummybdt'+cat[1]+'>'+str(bdt)+')',cat[1]+'_high') )
    categories.append(('('+cat[0]+')*(splitdummybdt'+cat[1]+'<='+str(bdt)+')',cat[1]+'_low') )
  else:
    categories.append(cat )
print categories


discrname='BDT'

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
samples=samplesLimits

allsystnames=weightsystnames+othersystnames

# corresponding weight names

systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    thisnewsel=sample.selection
    if sysname=="_CMS_ttH_PSscaleUp":
      thisnewsel=thisnewsel.replace('*(0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.000707116*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS','*(0.003106675*(N_GenTopHad==1 && N_GenTopLep==1)+0.00251279*(N_GenTopLep==2 && N_GenTopHad==0)+0.017175278*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS')
      print "weights for scaleUp sample ", thisnewsel
    if sysname=="_CMS_ttH_PSscaleDown":
      thisnewsel=thisnewsel.replace('*(0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.000707116*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS','*(0.003070913*(N_GenTopHad==1 && N_GenTopLep==1)+0.002519151*(N_GenTopLep==2 && N_GenTopHad==0)+0.016839284*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS')
      print "weights for scaleDown sample ", thisnewsel
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
  
allsamples=samples+systsamples
samplesdata=samples_data_controlplots

helperbdts=[]

bdts=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,nb,minx,maxx in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals):
  if bl == "ljets_jge6_tge4_high":
    print "tst"
    helperbdts.append(MVAPlot(ROOT.TH1F("splitdummybdt"+"ljets_jge6_tge4","BDT for splitting ("+bl+")",nb*10,-1.0,1.0),bdtweightpath+'/weights_Final_64_76blr.xml',b))
  if bl == "ljets_j5_tge4_high":
    helperbdts.append(MVAPlot(ROOT.TH1F("splitdummybdt"+"ljets_j5_tge4","BDT for splitting ("+bl+")",nb*10,-1.0,1.0),bdtweightpath+'/weights_Final_54_76blr.xml',b))
  if bl == "ljets_j4_t4_high":
    helperbdts.append(MVAPlot(ROOT.TH1F("splitdummybdt"+"ljets_j4_t4","BDT for splitting ("+bl+")",nb*10,-1.0,1.0),bdtweightpath+'/weights_Final_44_76blr.xml',b))
  if '.xml' in discr:
    bdts.append(MVAPlot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b))
  else:
    bdts.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b))
  print discr,b,bl,nb,minx,maxx

#print "if cateries are correct press the \"any\" key"
#raw_input()

outputpath=plotParallel(name,500000,bdts+helperbdts,allsamples+samplesdata,[''],['1.'],weightsystnames, systweights)
if not os.path.exists(name):
  os.makedirs(name)

renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames)
addPseudoData(name+'/'+name+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts)
lolT=transposeLOL(listOfHistoLists)
writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],20,name+'/'+name+'_controlplots')
makeDatacards(name+'/'+name+'_limitInput.root',name+'/'+name+'_datacard',binlabels)

##if askYesNo('Calculate limits?'):
limit=calcLimits(name+'/'+name+'_datacard',binlabels)
limit.dump()
  
