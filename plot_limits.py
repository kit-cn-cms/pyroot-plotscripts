import sys
import os
sys.path.insert(0, 'limittools')

from scriptgenerator import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import addRealData
from limittools import makeDatacards
from limittools import calcLimits
from limittools import replaceQ2scale
from plotconfig import *

# output name
name='limits'

# define categories
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
    categories.append(('('+cat[0]+')*(finalbdt_'+cat[1]+'>'+str(bdt)+')',cat[1]+'_high') )
    categories.append(('('+cat[0]+')*(finalbdt_'+cat[1]+'<='+str(bdt)+')',cat[1]+'_low') )
  else:
    categories.append(cat)
print categories

# define MEM discriminator variable
memexp='(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)'

# define BDT output variables
bdtweightpath="/nfs/dust/cms/user/kelmorab/76xBDTWeights/"
additionalvariables=[
                      'finalbdt_ljets_j4_t3:='+bdtweightpath+'/weights_Final_43_76mem.xml',
                      'finalbdt_ljets_j4_t4:='+bdtweightpath+'/weights_Final_44_76blr.xml',
                      'finalbdt_ljets_j5_t3:='+bdtweightpath+'/weights_Final_53_76mem.xml',
                      'finalbdt_ljets_j5_tge4:='+bdtweightpath+'/weights_Final_54_76blr.xml',
                      'finalbdt_ljets_jge6_t2:='+bdtweightpath+'/weights_Final_62_76blr2.xml',
                      'finalbdt_ljets_jge6_t3:='+bdtweightpath+'/weights_Final_63_76mem.xml',
                      'finalbdt_ljets_jge6_tge4:='+bdtweightpath+'/weights_Final_64_76blr.xml',
                      'finalbdt_ljets_boosted:='+bdtweightpath+'/weights_Final_DB_boosted_76xmem.xml',
]

# set discriminator histograms configuration
nhistobins= [   20,   4,   4,    20,    4,    4,   20,   20,    6,    6,    10 ]
minxvals=   [ -0.9,  0.,  0., -0.85,   0.,   0., -0.8, -0.8,   0.,   0.,  -0.9 ]
maxxvals=   [ 0.85, 0.9, 0.9, 0.825, 0.95, 0.95, 0.75, 0.85, 0.95, 0.95, 0.825 ] 

discrs =    ['finalbdt_ljets_j4_t3', memexp, memexp, 'finalbdt_ljets_j5_t3', memexp, memexp, 'finalbdt_ljets_jge6_t2', 'finalbdt_ljets_jge6_t3', memexp, memexp, 'finalbdt_ljets_boosted']

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
    if sysname=="_CMS_ttH_PSscaleUp":
      thisnewsel=thisnewsel.replace('*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))',
				    '*((N_BTagsM>=4)*((0.0033838531*(N_GenTopHad==1 && N_GenTopLep==1)+0.0027473283*(N_GenTopLep==2 && N_GenTopHad==0)+0.017175278*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.017175278/Weight_XS)*(N_BTagsM<4))')
      print "weights for scaleUp sample ", thisnewsel
      
    if sysname=="_CMS_ttH_PSscaleDown":
      thisnewsel=thisnewsel.replace('*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))',
				    '*((N_BTagsM>=4)*((0.003070913*(N_GenTopHad==1 && N_GenTopLep==1)+0.0027532915*(N_GenTopLep==2 && N_GenTopHad==0)+0.016839284*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.016839284/Weight_XS)*(N_BTagsM<4))')
      print "weights for scaleDown sample ", thisnewsel
    
    if sysname=="_CMS_scale_jUp":
      thisnewsel=thisnewsel.replace('*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))',
				    '*((N_BTagsM>=4)*((0.0011192298*(N_GenTopHad==1 && N_GenTopLep==1)+0.0007071164*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))')
      print "weights for jes scaleUp sample ", thisnewsel
      
    if sysname=="_CMS_scale_jDown":
      thisnewsel=thisnewsel.replace('*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))',
				    '*((N_BTagsM>=4)*((0.0010096664*(N_GenTopHad==1 && N_GenTopLep==1)+0.0008658787*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))')
      print "weights for jes scaleDown sample ", thisnewsel

    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
  
allsamples=samples+systsamples
samplesdata=samples_data_controlplots

# define plots
bdts=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,nb,minx,maxx in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals):
  bdts.append(Plot(ROOT.TH1F("finaldiscr_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b))

# plot everthing
outputpath=plotParallel(name,500000,bdts+helperbdts,allsamples+samplesdata,[''],['1.'],weightsystnames,systweights,additionalvariables)

if not os.path.exists(name):
  os.makedirs(name)

# rename output histos and save in one file
renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames)
#replaceQ2scale( os.getcwd()+'/'+name+'/'+name+'_limitInput.root')

# add real/pseudo data
# addPseudoData(name+'/'+name+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)
addRealData(name+'/'+name+'_limitInput.root',[s.nick for s in samples_data_controlplots],binlabels,discrname)

# make datacards
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts)
lolT=transposeLOL(listOfHistoLists)
writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],20,name+'/'+name+'_controlplots')
makeDatacards(name+'/'+name+'_limitInput.root',name+'/'+name+'_datacard',binlabels)

# calculate limits
if askYesNo('Calculate limits?'):
limit=calcLimits(name+'/'+name+'_datacard',binlabels)
limit.dump()
