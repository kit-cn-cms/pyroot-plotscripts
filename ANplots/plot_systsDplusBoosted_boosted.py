import sys
import os
sys.path.insert(0, '../limittools')

sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *
from plotconfig import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import makeDatacards
from limittools import calcLimits

name='systplots_boosted'



sel_singleel="(N_LooseMuons==0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)" # and vice versa...

mcweight='2.0*2.61*(Evt_Odd==0)'
nhistobins_=  [   8]
minxvals_=    [-0.7]
maxxvals_=    [ 0.8]
discrs =      ["/nfs/dust/cms/user/shwillia/BoostedTTHScripts/LimitCalculation/Setup_160127/pyroot-plotscripts/ANplots/weights/FinalBDT_Setup_160127_WP2_CombDiscr_PSOttbbDiscr_PSO_BDTG.weights.xml"]

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
categories=[("(N_Jets>=4&&N_BTagsM>=2)&&"+boosted ,"ljets_boosted","boosted")]


#categories=[]
#bdtcuts=[0.2,0.2,0.1,0.2,0.1,0.1,0.1]

#for cat,bdt in zip(categories_,bdtcuts):
  ##if "ljets_jge6_t3"!=cat[1]:
    ##continue
  #print cat[1]
  #if "4 b-tags" in cat[2]:
    #categories.append(('('+cat[0]+')*(BDT_common5_output>'+str(bdt)+')', cat[1]+'_high',cat[2]+' BDT > '+str(bdt)) )
    #categories.append(('('+cat[0]+')*(BDT_common5_output<='+str(bdt)+')', cat[1]+'_low',cat[2]+' BDT <= '+str(bdt)) )
  #else:
    #categories.append(cat )
  
  #print categories[-1]
  #print len(categories[-1])
  
#print categories

discrname='BDT'

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
bintitles= [c[2] for c in categories]
samples=samplesLimits
allsystnames=weightsystnames+othersystnames

# corresponding weight names
pdfweightscalefactor=1.0

samples_nom=[Sample('t#bar{t}H',ROOT.kBlue+1,path_incl4252+'/ttH*/*nominal*.root',mcweight,'ttH') ,     
        Sample('t#bar{t}',ROOT.kRed+1,path_incl4252+'/ttbar/*nominal*.root',mcweight,'ttbar') ]

systsamples=[]
for sample in samples_nom:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),sample.selection,sample.nick+sysname))
  
allsamples=samples_nom+systsamples

bdts=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,nb,minx,maxx in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals):
  if '.xml' in discr:
    bdts.append(MVAPlot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b))
  else:
    bdts.append(Plot(ROOT.TH1F(discrname+"_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b))
  print discr,b,bl,nb,minx,maxx

#print "if cateries are correct press the \"any\" key"
#raw_input()


outputpath=plotParallel(name,1000000,bdts,allsamples,[''],['1.'],weightsystnames, systweightsForSysTest)
if not os.path.exists(name):
  os.makedirs(name)
#renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames)
#addPseudoData(name+'/'+name+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)

allbdts=[]

print outputpath
print "test"
listOfHistoLists=createHistoLists_fromFiles([outputpath])
print listOfHistoLists
print listOfHistoLists[0][0].GetName()

upsystnames=[]
downsystnames=[]
for sys in allsystnames:
  if "Up" in sys:
    upsystnames.append(sys)
  if "Down" in sys:
    downsystnames.append(sys)

myyields=[]

for b,bl,bt in zip(bins,binlabels,bintitles):
  for sysup,sysdown in zip(upsystnames,downsystnames):
    print sysup,sysdown
    histoNom=None
    histoUp=None
    histoDown=None
    sampleNom=Sample('t#bar{t}H ',ROOT.kBlue+1,path_excl4252+'/ttH*/*nominal*.root',mcweight,'ttH')
    sampleUp=Sample('t#bar{t}H '+sysup.replace("_CMS_ttH_","").replace("_"," ").replace("scale","").replace("Up"," Up"),ROOT.kRed+1,path_excl4252+'/ttH*/*nominal*.root',mcweight,'ttHUp')
    sampleDown=Sample('t#bar{t}H '+sysdown.replace("_CMS_ttH_","").replace("_"," ").replace("scale","").replace("Down"," Down"),ROOT.kGreen+1,path_excl4252+'/ttH*/*nominal*.root',mcweight,'ttHDown')

    for h in listOfHistoLists:
      if h[0].GetName()=="ttH_BDT_"+bl:
	histoNom=h[0]
      if sysup=="_CMS_scale_jUp":
	if h[0].GetName()=="ttH_CMS_scale_jUp_BDT_"+bl:
	  histoUp=h[0]
	if h[0].GetName()=="ttH_CMS_scale_jDown_BDT_"+bl:
	  histoDown=h[0]
      else:
	if h[0].GetName()=="ttH_BDT_"+bl+sysup:
	  histoUp=h[0]
	if h[0].GetName()=="ttH_BDT_"+bl+sysdown:
	  histoDown=h[0]
    yn=histoNom.Integral()
    yup=histoUp.Integral()
    ydown=histoDown.Integral()
    print yn, type(yn)
    myyields.append([["ttH nominal",yn],["ttH "+sysup,yup],["ttH "+sysdown,ydown]])
    writeListOfHistoListsAN([[histoNom,histoUp,histoDown]],[sampleNom,sampleUp,sampleDown], bt,name+"/"+bl+"_"+"ttH"+sysup.replace("Up",""),False,False,False,'histoE',False, False,True)
    
  for sysup,sysdown in zip(upsystnames,downsystnames):
    histoNom=None
    histoUp=None
    histoDown=None
    sampleNom=Sample('t#bar{t} ',ROOT.kBlue+1,path_excl4252+'/ttbar*/*nominal*.root',mcweight,'ttbar')
    sampleUp=Sample('t#bar{t} '+sysup.replace("_CMS_ttH_","").replace("_"," ").replace("scale","").replace("Up"," Up"),ROOT.kRed+1,path_excl4252+'/ttbar*/*nominal*.root',mcweight,'ttbarUp')
    sampleDown=Sample('t#bar{t} '+sysdown.replace("_CMS_ttH_","").replace("_"," ").replace("scale","").replace("Down"," Down"),ROOT.kGreen+1,path_excl4252+'/ttbar*/*nominal*.root',mcweight,'ttbarDown')

    for h in listOfHistoLists:
      if h[0].GetName()=="ttbar_BDT_"+bl:
	histoNom=h[0]
      if sysup=="_CMS_scale_jUp":
	if h[0].GetName()=="ttbar_CMS_scale_jUp_BDT_"+bl:
	  histoUp=h[0]
	if h[0].GetName()=="ttbar_CMS_scale_jDown_BDT_"+bl:
	  histoDown=h[0]
      else:
	if h[0].GetName()=="ttbar_BDT_"+bl+sysup:
	  histoUp=h[0]
	if h[0].GetName()=="ttbar_BDT_"+bl+sysdown:
	  histoDown=h[0]
    yn=histoNom.Integral()
    yup=histoUp.Integral()
    ydown=histoDown.Integral()
    
    myyields.append([["ttbar nominal",yn],["ttbar "+sysup,yup],["ttbar "+sysdown,ydown]])  
    writeListOfHistoListsAN([[histoNom,histoUp,histoDown]],[sampleNom,sampleUp,sampleDown], bt,name+"/"+bl+"_"+"ttbar"+sysup.replace("Up",""),False,False,False,'histoE',False, False,True)

#writeListOfHistoLists(listOfHistoLists,samples, label,name,normalize=True,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False,ratio=False

#lolT=transposeLOL(listOfHistoLists)
#print lolT

for hists in myyields:
  print " "
  print hists[0][0], hists[0][1]
  print hists[1][0], hists[1][1], hists[1][1]/hists[0][1]
  print hists[2][0], hists[2][1], hists[2][1]/hists[0][1]
  
exit(0)


