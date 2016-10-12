import sys
import os
sys.path.insert(0, 'limittools')

from scriptgeneratorMEMDB import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import addRealData
from limittools import makeDatacards
from limittools import calcLimits
from limittools import replaceQ2scale
from plotconfigAnalysisV3 import *

# output name
name='sl2DBDTMEMsplitTTHRAW'

# define categories
boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.485&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.8925)"                        
categories_=[
              ("(N_Jets==4&&N_BTagsM==2)","ljets_j4_t2",""),
              ("(N_Jets==5&&N_BTagsM==2)","ljets_j5_t2",""),
              ("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3",""),
              ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4",""),
              ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3",""),
              ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4",""),             
              ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2",""),
              ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3",""),
              ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4","")
]

categories=[]
#categories=categories_
bdtcuts=[-0.2,-0.2,0.2,0.26,0.17,0.26,0.1,0.12,0.13]
for cat,bdt in zip(categories_,bdtcuts):
  if cat[1] in ["ljets_jge6_tge4","ljets_j5_tge4","ljets_j4_t4","ljets_jge6_t3","ljets_j5_t3","ljets_j4_t3"]:
    categories.append(('('+cat[0]+')*(finalbdt_'+cat[1]+'>'+str(bdt)+')',cat[1]+'_high') )
    categories.append(('('+cat[0]+')*(finalbdt_'+cat[1]+'<='+str(bdt)+')',cat[1]+'_low') )
  else:
    categories.append(cat)
print categories

# define MEM discriminator variable
memexp='(memDBp>0.0)*(memDBp_sig/(memDBp_sig+0.15*memDBp_bkg))+(memDBp<0.0)*(0.01)'

# define BDT output variables
bdtweightpath="/nfs/dust/cms/user/kelmorab/80xBDTWeights/"
bdtset="V4"
additionalvariables=[
			'finalbdt_ljets_j4_t2:=Evt_HT_Jets',
			'finalbdt_ljets_j5_t2:=Evt_HT_Jets',
                      'finalbdt_ljets_j4_t3:='+bdtweightpath+'/weights_43_'+bdtset+'.xml',
                      'finalbdt_ljets_j4_t4:='+bdtweightpath+'/weights_44_'+bdtset+'.xml',
                      'finalbdt_ljets_j5_t3:='+bdtweightpath+'/weights_53_'+bdtset+'.xml',
                      'finalbdt_ljets_j5_tge4:='+bdtweightpath+'/weights_54_'+bdtset+'.xml',
                      'finalbdt_ljets_jge6_t2:='+bdtweightpath+'/weights_62_'+bdtset+'.xml',
                      'finalbdt_ljets_jge6_t3:='+bdtweightpath+'/weights_63_'+bdtset+'.xml',
                      'finalbdt_ljets_jge6_tge4:='+bdtweightpath+'/weights_64_'+bdtset+'.xml',
                      #'finalbdt_ljets_boosted:='+bdtweightpath+'/weights_Final_DB_boosted_76xmem.xml',
]

# set discriminator histograms configuration
nhistobins= [  40,40, 	10, 10,     5,5,         10,10,    5,5,       20,      10,10,   5,5 ]
minxvals=   [200, 200, 0, 0,  	    0,0,         0,0       ,0,0 ,     -0.8,    0,0,0,0,]
maxxvals=   [800,800,  0.95, 0.95,  0.93,0.93,   1.0,1.0,    1.0,1.0 ,   0.9,  1.0,   1.0,1.0,   1.0]


#nhistobins= [  200]*9
#minxvals=   [ 200, 200, -1,-1,-1,-1,-1,-1,-1]
#maxxvals=   [700,700, 1.0,1.0,1.0,1.0,1.0,1.0,1.0]

#nhistobins= [   50 ]*7
#minxvals=   [-1.0]*7
#maxxvals=   [1.0]*7

discrs =    ['finalbdt_ljets_j4_t2','finalbdt_ljets_j5_t2',memexp, memexp, memexp, memexp,memexp, memexp,memexp, memexp, 'finalbdt_ljets_jge6_t2', memexp, memexp,memexp, memexp]
discrname='finaldiscr'
assert(len(nhistobins)==len(maxxvals))
assert(len(nhistobins)==len(minxvals))
assert(len(nhistobins)==len(categories))
assert(len(nhistobins)==len(discrs))

# get input for plotting function
bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
samples=samplesLimits
allsystnames=weightsystnames+othersystnames

# adapt weights for exlusive samples
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    thisnewsel=sample.selection
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
  
allsamples=samples+systsamples
samplesdata=samples_data_controlplots

# define plots
bdts=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,nb,minx,maxx in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals):
  bdts.append(Plot(ROOT.TH1F("finaldiscr_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b))

print bdts
# plot everthing
outputpath=plotParallel(name,500000,bdts,allsamples+samplesdata,[''],['1.'],weightsystnames,systweights,additionalvariables,[["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_ICHEP_V5New",False]],"/nfs/dust/cms/user/kelmorab/plotscripts80X/higgsCoupling/pyroot-plotscripts/treejson.json")

if not os.path.exists(name):
  os.makedirs(name)

# rename output histos and save in one file
renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames)
#replaceQ2scale( os.getcwd()+'/'+name+'/'+name+'_limitInput.root')

print samples
# add real/pseudo data
addPseudoData(name+'/'+name+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
#addRealData(name+'/'+name+'_limitInput.root',[s.nick for s in samples_data_controlplots],binlabels,discrname)

# make datacards
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts)
lolT=transposeLOL(listOfHistoLists)
writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],20,name+'/'+name+'_controlplots')
#writeListOfHistoListsAN(transposeLOL([lolT[0]]+lolT[9:]),samples_,"",name+'/'+name+'_controlplots_no_stack',True,False,False,'histo',False,False,False)

#exit(0)
makeDatacards(name+'/'+name+'_limitInput.root',name+'/'+name+'_datacard',binlabels)

# calculate limits
#if askYesNo('Calculate limits?'):
  #limit=calcLimits(name+'/'+name+'_datacard',binlabels)
  #limit.dump()
