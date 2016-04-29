import sys
import os
sys.path.insert(0, 'limittools')

from scriptgenerator import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from plotconfig import *

# output name
name='discriminatorplots'

# define categories
boosted="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>=-0.485&&BoostedTopHiggs_HiggsCandidate_HiggsTag>=0.8925)"
categories_=[("(N_Jets==4&&N_BTagsM==3)&&!"+boosted+"","ljets_j4_t3","4 jets, 3 b-tags"),
            ("(N_Jets==4&&N_BTagsM>=4)&&!"+boosted+"","ljets_j4_t4","4 jets, 4 b-tags"),
            ("(N_Jets==5&&N_BTagsM==3)&&!"+boosted+"","ljets_j5_t3","5 jets, 3 b-tags"),
            ("(N_Jets==5&&N_BTagsM>=4)&&!"+boosted+"","ljets_j5_tge4","5 jets, #geq 4 b-tags"),
            ("(N_Jets>=6&&N_BTagsM==2)&&!"+boosted+"","ljets_jge6_t2","#geq 6 jets, 2 b-tags"),
            ("(N_Jets>=6&&N_BTagsM==3)&&!"+boosted+"","ljets_jge6_t3","#geq 6 jets, 3 b-tags"),
            ("(N_Jets>=6&&N_BTagsM>=4)&&!"+boosted+"","ljets_jge6_tge4","#geq 6 jets, #geq 4 b-tags"),
            (boosted,"ljets_boosted","boosted regime")]

categories=[]
bdtcuts=[0.2,0.2,0.1,0.2,0.1,0.1,0.1,0.2]
for cat,bdt in zip(categories_,bdtcuts):
  if cat[1] in ["ljets_jge6_tge4","ljets_j5_tge4","ljets_j4_t4"]:
    categories.append(('('+cat[0]+')*(finalbdt_'+cat[1]+'>'+str(bdt)+')',cat[1]+'_high',cat[2]+', BDT > '+str(bdt) ))
    categories.append(('('+cat[0]+')*(finalbdt_'+cat[1]+'<='+str(bdt)+')',cat[1]+'_low',cat[2]+', BDT #leq '+str(bdt)))
  else:
    categories.append(cat )

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
actualabels= [c[2] for c in categories]
samples=samplesControlPlots

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
      print "weights for scaleUp sample ", thisnewsel
      
    if sysname=="_CMS_scale_jDown":
      thisnewsel=thisnewsel.replace('*((N_BTagsM>=4)*((0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.0009753747*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))',
				    '*((N_BTagsM>=4)*((0.0010096664*(N_GenTopHad==1 && N_GenTopLep==1)+0.0008658787*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS)+(0.0084896859/Weight_XS)*(N_BTagsM<4))')
      
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
  
allsamples=samples+systsamples
samplesdata=samples_data_controlplots

# define plots
bdts=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,nb,minx,maxx,al in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals,actualabels):
  bdts.append(Plot(ROOT.TH1F('finaldiscr_'+bl,"BDT incl. MEM discriminator",nb,minx,maxx),discr,b,al))

# plot everthing
outputpath=plotParallel(name,500000,bdts,allsamples+samplesdata,[''],['1.'],weightsystnames,systweights,additionalvariables)
if not os.path.exists(name):
  os.makedirs(name)

# rename output histos and save in one file
renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames)

# create plots
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samplesdata,bdts,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames)

lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],bdts,errorSystnames)
labels=[plot.label for plot in bdts]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name+'_lin2',[[lll,3354,ROOT.kBlack,True]],False,labels,True,False)

