import sys
import os
import ROOT
sys.path.append('pyroot-plotscripts-base')
sys.path.append('pyroot-plotscripts-base/limittools')

from scriptgenerator import *
from plotutils import *
from limittools import renameHistos
from limittools import addPseudoData
from limittools import addRealData
from limittools import makeDatacards
from limittools import calcLimits
from limittools import replaceQ2scale
from plotconfigSpring17v10 import *

MainClock=ROOT.TStopwatch()
MainClock.Start()

doDrawParallel=False


# output name
name='limits_MultiDNN_Spring17v10'

# define categories
categories_=[
              ("(N_Jets==4&&N_BTagsM==2)","ljets_j4_t2",""),
              ("(N_Jets==5&&N_BTagsM==2)","ljets_j5_t2",""),
              ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2",""),
              ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==0)","ljets_j4_tge3_ttHnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==0)","ljets_j5_tge3_ttHnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==0)","ljets_jge6_tge3_ttHnode",""),

              ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==1)","ljets_j4_tge3_ttbbnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==1)","ljets_j5_tge3_ttbbnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==1)","ljets_jge6_tge3_ttbbnode",""),

              ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==2)","ljets_j4_tge3_ttbnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==2)","ljets_j5_tge3_ttbnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==2)","ljets_jge6_tge3_ttbnode",""),

              ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==3)","ljets_j4_tge3_tt2bnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==3)","ljets_j5_tge3_tt2bnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==3)","ljets_jge6_tge3_tt2bnode",""),

              ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==4)","ljets_j4_tge3_ttccnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==4)","ljets_j5_tge3_ttccnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==4)","ljets_jge6_tge3_ttccnode",""),

              ("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==5)","ljets_j4_tge3_ttlfnode",""),
              ("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==5)","ljets_j5_tge3_ttlfnode",""),             
              ("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==5)","ljets_jge6_tge3_ttlfnode",""),

              #("(N_Jets==4&&N_BTagsM>=3&&aachen_pred_class==6)","ljets_j4_tge3_othernode",""),
              #("(N_Jets==5&&N_BTagsM>=3&&aachen_pred_class==6)","ljets_j5_tge3_othernode",""),             
              #("(N_Jets>=6&&N_BTagsM>=3&&aachen_pred_class==6)","ljets_jge6_tge3_othernode",""),
]
# DANGERZONE
# Need to remove the other node. Do not know what happens if the datacardmaker tries to use empty histograms
categories=[]

nhistobins= [  20,20,20, 	5,   5,    5, 	5,   5,    5, 	5,   5,    5, 	5,   5,    5, 	5,   5,    5, 	5,   5,    5,]
minxvals=   [ 200, 200,-0.8, 0.16,  0.16, 0.17, 0.16,  0.16, 0.16, 0.18,  0.18, 0.18, 0.16,  0.16, 0.16, 0.17,  0.17, 0.18, 0.17,  0.17, 0.19,]
maxxvals=   [800,800,0.8,    0.6,  0.6, 0.65,    0.6,  0.6, 0.6,    0.35,  0.32, 0.35,    0.45,  0.5, 0.55,    0.35,  0.24, 0.25,    0.5,  0.4, 0.45,]print len(nhistobins)
print len(minxvals)
print len(maxxvals)

# add unsplit categories
for cat in categories_:
  categories.append(cat)

print categories

# define MEM discriminator variable
memexp='(memDBp>0.0)*(memDBp_sig/(memDBp_sig+0.15*memDBp_bkg))+(memDBp<0.0)*(0.01)'

# define BDT output variables
bdtweightpath="/nfs/dust/cms/user/kelmorab/Spring17BDTWeights/"
bdtset="Spring17v1"
additionalvariables=[
			'finalbdt_ljets_j4_t2:=Evt_HT_Jets',
			'finalbdt_ljets_j5_t2:=Evt_HT_Jets',
                      'dummybdt_ljets_j4_t3:='+bdtweightpath+'/weights_Final_43_'+bdtset+'.xml',
                      'dummybdt_ljets_j4_t4:='+bdtweightpath+'/weights_Final_44_'+bdtset+'.xml',
                      'dummybdt_ljets_j5_t3:='+bdtweightpath+'/weights_Final_53_'+bdtset+'.xml',
                      'dummybdt_ljets_j5_tge4:='+bdtweightpath+'/weights_Final_54_'+bdtset+'.xml',
                      'finalbdt_ljets_jge6_t2:='+bdtweightpath+'/weights_Final_62_'+bdtset+'.xml',
                      'dummybdt_ljets_jge6_t3:='+bdtweightpath+'/weights_Final_63_'+bdtset+'.xml',
                      'dummybdt_ljets_jge6_tge4:='+bdtweightpath+'/weights_Final_64_'+bdtset+'.xml',
                      'finalbdt_ljets_j4_tge3:=((N_Jets==4&&N_BTagsM==3)*dummybdt_ljets_j4_t3 + (N_Jets==4&&N_BTagsM==4)*dummybdt_ljets_j4_t4)',
                      'finalbdt_ljets_j5_tge3:=((N_Jets==5&&N_BTagsM==3)*dummybdt_ljets_j5_t3 + (N_Jets==5&&N_BTagsM>=4)*dummybdt_ljets_j5_tge4)',
                      'finalbdt_ljets_jge6_tge3:=((N_Jets>=6&&N_BTagsM==3)*dummybdt_ljets_jge6_t3 + (N_Jets>=6&&N_BTagsM>=4)*dummybdt_ljets_jge6_tge4)',
               
                      "Muon_Pt","Electron_Pt","Muon_Eta","Electron_Eta","Jet_Pt","Jet_Eta","Jet_CSV","Jet_Flav","N_Jets","Jet_Phi","Jet_E","Jet_M",
                      "Evt_Pt_PrimaryLepton","Evt_E_PrimaryLepton","Evt_M_PrimaryLepton","Evt_Phi_PrimaryLepton","Evt_Eta_PrimaryLepton",
                      "Weight_CSV","Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown","Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down","Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down","Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down",
]


discrs =    ['finalbdt_ljets_j4_t2','finalbdt_ljets_j5_t2','finalbdt_ljets_jge6_t2',
	     'aachen_Out_ttH','aachen_Out_ttH','aachen_Out_ttH',
	     'aachen_Out_ttbarBB','aachen_Out_ttbarBB','aachen_Out_ttbarBB',
	     'aachen_Out_ttbarB','aachen_Out_ttbarB','aachen_Out_ttbarB',
	     'aachen_Out_ttbar2B','aachen_Out_ttbar2B','aachen_Out_ttbar2B',
	     'aachen_Out_ttbarCC','aachen_Out_ttbarCC','aachen_Out_ttbarCC',
	     'aachen_Out_ttbarOther','aachen_Out_ttbarOther','aachen_Out_ttbarOther',
	     ]
discrname='finaldiscr'
assert(len(nhistobins)==len(maxxvals))
assert(len(nhistobins)==len(minxvals))
assert(len(nhistobins)==len(categories))
assert(len(nhistobins)==len(discrs))

# get input for plotting function
bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
allsystnames=weightSystNames+otherSystNames+PSSystNames

# samples
samples=samplesLimits
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(otherSystNames,otherSystFileNames):
    thisnewsel=sample.selection
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname,samDict=sampleDict))

# add Parton shower variation samples
for sample in samples[9:14]: # only for ttbar samples
  for sysname,sysfilename in zip(PSSystNames,PSSystFileNames):
    thisoldsel=sample.selection
    thisnewsel=sample.selection.replace(ttbarMCWeight,"*1.0").replace(mcWeight+evenSel,mcWeightAll)
    print "adding sample for ", sysname
    print "selection ", thisnewsel
    print "instead of ", thisoldsel
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace(ttbarPathS,path_additionalSamples+"/ttbar_"+sysfilename+"/*nominal*.root"),thisnewsel,sample.nick+sysname,samDict=sampleDict))
  
allsamples=samples+systsamples
samples_data=samplesDataControlPlots

# define plots
bdts=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,nb,minx,maxx in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals):
  bdts.append(Plot(ROOT.TH1F("finaldiscr_"+bl,"final discriminator ("+bl+")",nb,minx,maxx),discr,b))

print bdts
plots=bdts

bdtsHighNBins=[]
for discr,b,bl,nb,minx,maxx in zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals):
  bdtsHighNBins.append(Plot(ROOT.TH1F("HIGHBIN_finaldiscr_"+bl,"HIGHBIN final discriminator ("+bl+")",500,minx,maxx),discr,b))


# belongs to DrawParallel
if doDrawParallel and  len(sys.argv) > 1 :
    plots=[plots[int(sys.argv[1])]]
print plots

if not os.path.exists(name):
  os.makedirs(name)

# plot everthing

if doDrawParallel==False or len(sys.argv) == 1 :                      #if some option is given plotParallelStep will be skipped
    outputpath=plotParallel(name,5000000,plots+bdtsHighNBins,samples+samples_data+systsamples,[''],['1.'],weightSystNames, systWeights,additionalvariables,[],"/nfs/dust/cms/user/kelmorab/plotscriptsSpring17/pyroot-plotscripts/treejson08062017.json",otherSystNames+PSSystNames,True)
else:
    workdir=os.getcwd()+'/workdir/'+name
    outputpath=workdir+'/output.root'

if doDrawParallel==False or len(sys.argv) == 1 :                      #if some option is given old systematic histo file will be used      
    # rename output histos and save in one file
    if not os.path.exists(name+'/'+name+'_limitInput.root') or not askYesNo('reuse renamed histofile?'):
      print "does syst file exist?", os.path.exists(name+'/'+name+'_limitInput.root')
      renameHistos(outputpath,name+'/'+name+'_limitInput.root',allsystnames,True,False)
    addPseudoData(name+'/'+name+'_limitInput.root',[s.nick for s in samples[9:]],binlabels,allsystnames,discrname)    
    #addRealData(name+'/'+name+'_limitInput.root',[s.nick for s in samplesDataControlPlots],binlabels,discrname)

if doDrawParallel==False or len(sys.argv) > 1 :
    listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots)    
    lolT=transposeLOL(listOfHistoLists)
    writeLOLAndOneOnTop(transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_controlplots')
    writeListOfHistoListsAN(transposeLOL([lolT[0]]+lolT[9:]),[samples[0]]+samples[9:],"",name+'/'+name+'_shapes',True,False,False,'histo',False,True,False)


if doDrawParallel==False or len(sys.argv) == 1 :
  listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdtsHighNBins)    
  for icat, cat in enumerate(categories):
    ttHHisto=listOfHistoLists[icat][0]
    ttHColor=samples[0].color
    ttHName=samples[0].name
    rocGraphs=[]
    rocNames=[]
    rocColors=[]
    for sample, histo in zip(samples[9:],listOfHistoLists[icat][9:]):
      rocGraphs.append(getROC(ttHHisto,histo))
      #rocGraphs[-1].SetColor(sample.color)
      rocNames.append(sample.name)
      rocColors.append(sample.color)
    writeListOfROCs(rocGraphs,rocNames,rocColors,name+'/'+name+'_ROC_'+cat[1])


# NO UNBLINDED PLOTS FOR NOW !!!
#plotdiscriminants
#labels=[plot.label for plot in bdts]
#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,bdts,1)
#if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    #renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames,False)
#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[9:],bdts,errorSystnames)
#plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_Blinded',[[lll,3354,ROOT.kBlack,True]],False,labels,True,True)

#listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,bdts,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,bdts,1)
#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[9:],bdts,errorSystnames)
#plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[9:]),samples[9:],lolT[0],samples[0],-1,name+'/'+name+'_Unblinded',[[lll,3354,ROOT.kBlack,True]],False,labels,True,False)

if doDrawParallel==False or len(sys.argv) == 1 :                      #if some option is given old systematic histo file will be used      
    # make datacards
    #TODO
    # 1. Implement small Epsilon case
    # 2. Implement consisted Bin-by-Bin uncertainties
    makeDatacards(name+'/'+name+'_limitInput.root',name+'/'+name+'_datacard',binlabels,doHdecay=True,discrname='finaldiscr',datacardmaker='mk_datacard_JESTest13TeV')


print "TOTAL Elapsed time since beginning of plotscript", MainClock.RealTime()
exit(0)