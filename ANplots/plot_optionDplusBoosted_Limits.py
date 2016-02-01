import sys
import os
sys.path.insert(0, '../limittools')
sys.path.insert(0, '../')

from scriptgenerator import *
from plotutils import *
from limittools import mergeHistFiles
from limittools import addPseudoData
from limittools import makeDatacards
from limittools import calcLimits
from plotconfig import *

name='optionDplusBoosted_Limits'


jtplots="/nfs/dust/cms/user/shwillia/BoostedTTHScripts/LimitCalculation/Setup_160127/Vers_160201/pyroot-plotscripts/ANplots/optionDplusBoosted_JTplots/optionDplusBoosted_JTplots_limitInput.root"
boostedplots="/nfs/dust/cms/user/shwillia/BoostedTTHScripts/LimitCalculation/Setup_160127/Vers_160201/pyroot-plotscripts/ANplots/optionDplusBoosted_Boostedplots/optionDplusBoosted_Boostedplots_limitInput.root"

categoriesToTakeFrom2= ["boosted"]

nhistobins_=      [  20,       4,   4,     20,       4,     4,   20,   20,  6 ,6,    8]
minxvals_=        [-0.9,    0.,  0.,     -0.8,     0.,     0.,   -0.80,  -0.8,  0.,   0., -0.7]
#maxxvals_=        [ 0.8,     .95,   0.95,  0.8,    0.95,   0.95,    0.76,   0.8,   0.95,    0.95, 0.8] 
maxxvals_=        [ 0.8,     .95,   0.95,  0.8,    0.95,   0.95,    0.76,   0.6,   0.95,    0.95, 0.8] 

discrs =          ['/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_43_MEMBDTv2.xml', 'MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)','MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_53_MEMBDTv2.xml', 'MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)' ,'MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)' , 'BDT_common5_output','/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_63_MEMBDTv2.xml','MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)','MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg)','/nfs/dust/cms/user/shwillia/BoostedTTHScripts/LimitCalculation/Setup_160127/pyroot-plotscripts/ANplots/weights/FinalBDT_Setup_160127_WP2_CombDiscr_PSOttbbDiscr_PSO_BDTG.weights.xml']

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
categories_=[ ("(N_Jets==4&&N_BTagsM==3)&&!"+boosted,"ljets_j4_t3"),
              ("(N_Jets==4&&N_BTagsM>=4)&&!"+boosted,"ljets_j4_t4"),
              ("(N_Jets==5&&N_BTagsM==3)&&!"+boosted,"ljets_j5_t3"),
              ("(N_Jets==5&&N_BTagsM>=4)&&!"+boosted,"ljets_j5_tge4"),
              ("(N_Jets>=6&&N_BTagsM==2)&&!"+boosted,"ljets_jge6_t2"),
              ("(N_Jets>=6&&N_BTagsM==3)&&!"+boosted,"ljets_jge6_t3"),
              ("(N_Jets>=6&&N_BTagsM>=4)&&!"+boosted,"ljets_jge6_tge4"),
              ("(N_Jets>=4&&N_BTagsM>=2)&&"+boosted ,"ljets_boosted")]

categories=[]
bdtcuts=[0.2,0.2,0.1,0.2,0.1,0.1,0.1,0.1]

for cat,bdt in zip(categories_,bdtcuts):
  if cat[1] in ["ljets_jge6_tge4","ljets_j5_tge4","ljets_j4_t4"]:
    categories.append(('('+cat[0]+')*(BDT_common5_output>'+str(bdt)+')',cat[1]+'_high') )
    categories.append(('('+cat[0]+')*(BDT_common5_output<='+str(bdt)+')',cat[1]+'_low') )
  else:
    categories.append(cat )
print categories


discrname='BDT'

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
samples=samplesLimits

allsystnames=weightsystnames+othersystnames

# corresponding weight names
pdfweightscalefactor=1.0

systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),sample.selection,sample.nick+sysname))
  
allsamples=samples+systsamples

if not os.path.exists(name):
  os.makedirs(name)

mergeHistFiles(jtplots,boostedplots,categoriesToTakeFrom2,name+'/'+name+'_limitInput.root')

addPseudoData(name+'/'+name+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)

makeDatacards(name+'/'+name+'_limitInput.root',name+'/'+name+'_datacard',binlabels)

#if askYesNo('Calculate limits?'):
limit=calcLimits(name+'/'+name+'_datacard',binlabels)
limit.dump()
  
