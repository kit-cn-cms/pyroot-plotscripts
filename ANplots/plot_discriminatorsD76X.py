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


name='76xBDToptionD_discrplots'

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
    categories.append(('('+cat[0]+')*(splitdummybdt'+cat[1]+'>'+str(bdt)+')',cat[1]+'_high',cat[2]+', BDT > '+str(bdt) ))
    categories.append(('('+cat[0]+')*(splitdummybdt'+cat[1]+'<='+str(bdt)+')',cat[1]+'_low',cat[2]+', BDT #leq '+str(bdt)))
  else:
    categories.append(cat )



discrname='BDT'

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
actualabels= [c[2] for c in categories]
samples=samplesControlPlots

allsystnames=weightsystnames+othersystnames

# corresponding weight names

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

helperbdts=[]

bdts=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,nb,minx,maxx,al in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals,actualabels):
  if bl == "ljets_jge6_tge4_high":
    print "tst"
    helperbdts.append(MVAPlot(ROOT.TH1F("splitdummybdt"+"ljets_jge6_tge4","BDT w/o MEM (for 2D splitting)",nb*10,-1.0,1.0),bdtweightpath+'/weights_Final_64_76blr.xml',b,al))
    bdts.append(MVAPlot(ROOT.TH1F("bdt"+"ljets_jge6_tge4","BDT w/o MEM (for 2D splitting)",10,-1.0,1.0),bdtweightpath+'/weights_Final_64_76blr.xml',"N_Jets>=6&&N_BTagsM>=4",'#geq 4 jets, 4 b-tags'))
  if bl == "ljets_j5_tge4_high":
    helperbdts.append(MVAPlot(ROOT.TH1F("splitdummybdt"+"ljets_j5_tge4","BDT for splitting ("+bl+")",nb*10,-1.0,1.0),bdtweightpath+'/weights_Final_54_76blr.xml',b,al))
    bdts.append(MVAPlot(ROOT.TH1F("bdt"+"ljets_j5_tge4","BDT w/o MEM (for 2D splitting)",10,-1.0,1.0),bdtweightpath+'/weights_Final_54_76blr.xml',"N_Jets==5&&N_BTagsM>=4",'#geq 5 jets, #geq 4 b-tags'))
  if bl == "ljets_j4_t4_high":
    helperbdts.append(MVAPlot(ROOT.TH1F("splitdummybdt"+"ljets_j4_t4","BDT w/o MEM (for 2D splitting)",nb*10,-1.0,1.0),bdtweightpath+'/weights_Final_44_76blr.xml',b,al))
    bdts.append(MVAPlot(ROOT.TH1F("bdt_"+"ljets_j4_t4","BDT w/o MEM (for 2D splitting)",10,-1.0,1.0),bdtweightpath+'/weights_Final_44_76blr.xml',"N_Jets==4&&N_BTagsM>=4",'4 jets, #geq 4 b-tags'))
  if '.xml' in discr:
    if "jge6_t2" in bl:
      bdts.append(MVAPlot(ROOT.TH1F(discrname+"_"+bl,"BDT w/o MEM discriminator",nb,minx,maxx),discr,b,al))
    else:
      bdts.append(MVAPlot(ROOT.TH1F(discrname+"_"+bl,"BDT incl. MEM discriminator",nb,minx,maxx),discr,b,al))
  else:
    bdts.append(Plot(ROOT.TH1F(discrname+"_"+bl,"BDT incl. MEM discriminator",nb,minx,maxx),discr,b,al))
  print discr,b,bl,nb,minx,maxx

#print "if cateries are correct press the \"any\" key"
#raw_input()

outputpath=plotParallel(name,500000,bdts+helperbdts,allsamples+samplesdata,[''],['1.'],weightsystnames, systweights)
if not os.path.exists(name):
  os.makedirs(name)

renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames)
#addPseudoData(name+'/'+name+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)


######################################
### data-MC
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samplesdata,bdts,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames)

lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],bdts,errorSystnames)
#lllforPS=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],bdts,PSSystnames)
labels=[plot.label for plot in bdts]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],-1,name+'_lin2',[[lll,3354,ROOT.kBlack,True]],False,labels,True,False)

