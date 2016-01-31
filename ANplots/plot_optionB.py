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

path='/nfs/dust/cms/user/hmildner/merged_trees/output/'
name='optionB'
mcweight='2.0*2.61*(Evt_Odd==0)'
# hcc is uu dd ss cc with ids 1 2 3 4
hccSel='*((abs(GenHiggs_DecProd1_PDGID)==1 && abs(GenHiggs_DecProd2_PDGID)==1) || (abs(GenHiggs_DecProd1_PDGID)==2 && abs(GenHiggs_DecProd2_PDGID)==2) || (abs(GenHiggs_DecProd1_PDGID)==3 && abs(GenHiggs_DecProd2_PDGID)==3) || (abs(GenHiggs_DecProd1_PDGID)==4 && abs(GenHiggs_DecProd2_PDGID)==4) )'
# htt is mumu tautau with ids 13 15
httSel='*((abs(GenHiggs_DecProd1_PDGID)==13 && abs(GenHiggs_DecProd2_PDGID)==13) || (abs(GenHiggs_DecProd1_PDGID)==15 && abs(GenHiggs_DecProd2_PDGID)==15))'
# hgg is gammagamma with id 22
hggSel='*((abs(GenHiggs_DecProd1_PDGID)==22 && abs(GenHiggs_DecProd2_PDGID)==22))'
# hgluglu with id 21
hglugluSel='*((abs(GenHiggs_DecProd1_PDGID)==21 && abs(GenHiggs_DecProd2_PDGID)==21))'
# hww with id 24
hwwSel='*((abs(GenHiggs_DecProd1_PDGID)==24 && abs(GenHiggs_DecProd2_PDGID)==24))'
# hzz with id 23
hzzSel='*((abs(GenHiggs_DecProd1_PDGID)==23 && abs(GenHiggs_DecProd2_PDGID)==23))'
# hzg with id 23 and id 22
hzgSel='*((abs(GenHiggs_DecProd1_PDGID)==23 && abs(GenHiggs_DecProd2_PDGID)==22) || (abs(GenHiggs_DecProd1_PDGID)==22 && abs(GenHiggs_DecProd2_PDGID)==23))'

nhistobins=      [ 10,10,          4,4 ,        10,10,         4,4,       16,    10,10,  6,6     ]
minxvals=        [0.]*8 + [-.8] + [0.]*4
maxxvals=        [.95]*8 + [.8] + [.95]*4
discrs =          ["((MEM_p_sig>0)*MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))"]*8+['BDT_common5_output']+['((MEM_p_sig>0)*MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))']*4
discrnames= ["MEM discriminator"]*8+["BDT discriminator"]+4*["MEM discriminator"]
categories_=[("(N_Jets==4&&N_BTagsM==3)","ljets_j4_t3","4 jets, 3 b-tags category"),
            ("(N_Jets==4&&N_BTagsM>=4)","ljets_j4_t4","4 jets, 4 b-tags category"),
            ("(N_Jets==5&&N_BTagsM==3)","ljets_j5_t3","5 jets, 3 b-tags category"),
            ("(N_Jets==5&&N_BTagsM>=4)","ljets_j5_tge4","5 jets, #geq4 b-tags category"),
            ("(N_Jets>=6&&N_BTagsM==2)","ljets_jge6_t2","#geq6 jets, 2 b-tags category"),
            ("(N_Jets>=6&&N_BTagsM==3)","ljets_jge6_t3","#geq6 jets, 3 b-tags category"),
            ("(N_Jets>=6&&N_BTagsM>=4)","ljets_jge6_tge4","#geq6 jets, #geq4 b-tags category")]
categories=[]

bdtcuts=[0.2,0.2,0.15,
         0.2,0.1,0.1,0.1]

for cat,bdt in zip(categories_,bdtcuts):
  if cat[1]=='ljets_jge6_t2':
    categories.append(cat)
  else:
    categories.append(('('+cat[0]+')*(BDT_common5_output>'+str(bdt)+')',cat[1]+'_low',cat[2]+', BDT <= '+str(bdt)) )
    categories.append(('('+cat[0]+')*(BDT_common5_output<='+str(bdt)+')',cat[1]+'_high',cat[2]+', BDT > '+str(bdt)) )

print categories


discrname='BDT'

bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
bintitles= [c[2] for c in categories]

samples=[Sample('t#bar{t}H',ROOT.kBlue+1,path+'/ttH*/*nominal*.root',mcweight,'ttH') ,  
	 Sample('t#bar{t}H, H to b#bar{b}',ROOT.kBlue+1,path+'/ttHbb*/*nominal*.root',mcweight,'ttH_hbb') ,  
	 Sample('t#bar{t}H, H to c#bar{c}',ROOT.kBlue+1,path+'/ttHnonbb*/*nominal*.root',mcweight+hccSel,'ttH_hcc') ,  
 	 Sample('t#bar{t}H, H to #tau#tau',ROOT.kBlue+1,path+'/ttHnonbb*/*nominal*.root',mcweight+httSel,'ttH_htt') ,  
	 Sample('t#bar{t}H, H to #gamma#gamma',ROOT.kBlue+1,path+'/ttHnonbb*/*nominal*.root',mcweight+hggSel,'ttH_hgg') ,  
	 Sample('t#bar{t}H, H to gluglu',ROOT.kBlue+1,path+'/ttHnonbb*/*nominal*.root',mcweight+hglugluSel,'ttH_hgluglu') ,  
	 Sample('t#bar{t}H, H to WW',ROOT.kBlue+1,path+'/ttHnonbb*/*nominal*.root',mcweight+hwwSel,'ttH_hww') ,  
	 Sample('t#bar{t}H, H to ZZ',ROOT.kBlue+1,path+'/ttHnonbb*/*nominal*.root',mcweight+hzzSel,'ttH_hzz') ,  
  	 Sample('t#bar{t}H, H to #gamma Z',ROOT.kBlue+1,path+'/ttHnonbb*/*nominal*.root',mcweight+hzgSel,'ttH_hzg') ,
  	 
         Sample('t#bar{t}+lf',ROOT.kRed-7,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)','ttbarOther'),
         Sample('t#bar{t}+c#bar{c}',ROOT.kRed+1,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusCC==1)','ttbarPlusCCbar'),
         Sample('t#bar{t}+b',ROOT.kRed-2,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==1)','ttbarPlusB'),
         Sample('t#bar{t}+2b',ROOT.kRed+2,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==2)','ttbarPlus2B'),
         Sample('t#bar{t}+b#bar{b}',ROOT.kRed+3,path+'/ttbar/*nominal*.root',mcweight+'*(GenEvt_I_TTPlusBB==3)','ttbarPlusBBbar'),  
         Sample('Single Top',ROOT.kMagenta,path+'/st*/*nominal*.root',mcweight,'singlet') , 
         Sample('Z+jets',ROOT.kGreen-3,path+'/Zjets*/*nominal*.root',mcweight,'zjets') , 
         Sample('W+jets',ROOT.kGreen-7,path+'/WJets*/*nominal*.root',mcweight,'wjets') , 
         Sample('t#bar{t}+W',ROOT.kBlue-10,path+'/ttW_*/*nominal*.root',mcweight,'ttW'),
         Sample('t#bar{t}+Z',ROOT.kBlue-6,path+'/ttZ_*/*nominal*.root',mcweight,'ttZ'),
         Sample('Diboson',ROOT.kAzure+2,path+'/??/*nominal*.root',mcweight,'diboson') , 
         #Sample('QCD',ROOT.kYellow ,path+'/QCD*/*nominal*root',mcweight,'QCD') , 
]

# names of the systematics (proper names needed e.g. for combination)
weightsystnames=["",
           "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
           "_CMS_ttH_Q2scale_ttbarOtherUp","_CMS_ttH_Q2scale_ttbarPlusBUp","_CMS_ttH_Q2scale_ttbarPlus2BUp","_CMS_ttH_Q2scale_ttbarPlusBBbarUp","_CMS_ttH_Q2scale_ttbarPlusCCbarUp",
           "_CMS_ttH_Q2scale_ttbarOtherDown","_CMS_ttH_Q2scale_ttbarPlusBDown","_CMS_ttH_Q2scale_ttbarPlus2BDown","_CMS_ttH_Q2scale_ttbarPlusBBbarDown","_CMS_ttH_Q2scale_ttbarPlusCCbarDown",
           "_CMS_ttH_NNPDFUp","_CMS_ttH_NNPDFDown"
           ]

othersystnames=["_CMS_scale_jUp",
                "_CMS_scale_jDown",
#                "_CMS_res_jUp",
#                "_CMS_res_jDown"
                ]
allsystnames=weightsystnames+othersystnames

othersystfilenames=["JESUP",
                    "JESDOWN",
#                    "JERUP",
#                    "JERDOWN"
                    ]

# corresponding weight names
pdfweightscalefactor=1.0
systweights=["1",
             "Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown",
             "Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down",
             "Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
             "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down",
             "QScaleTTLFUp:=Weight_muRupmuFup/"+str(pdfweightscalefactor),"QScaleTTBUp:=Weight_muRupmuFup/"+str(pdfweightscalefactor),"QScaleTTtwoBUp:=Weight_muRupmuFup/"+str(pdfweightscalefactor),"QScaleTTBBUp:=Weight_muRupmuFup/"+str(pdfweightscalefactor),"QScaleTTCCUp:=Weight_muRupmuFup/"+str(pdfweightscalefactor),
             "QScaleTTLFDown:=Weight_muRdownmuFdown/"+str(pdfweightscalefactor),"QScaleTTBDown:=Weight_muRdownmuFdown/"+str(pdfweightscalefactor),"QScaleTTtwoBDown:=Weight_muRdownmuFdown/"+str(pdfweightscalefactor),"QScaleTTBBDown:=Weight_muRdownmuFdown/"+str(pdfweightscalefactor),"QScaleTTCCDown:=Weight_muRdownmuFdown/"+str(pdfweightscalefactor),
             "PDFweightUp:=Weight_NNPDFid260067/"+str(pdfweightscalefactor),"PDFWeightDown:=Weight_NNPDFid260005/"+str(pdfweightscalefactor)
             ]

systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),sample.selection,sample.nick+sysname))
  
allsamples=samples+systsamples

bdts=[]
for discr,b,bl,bt,nb,minx,maxx in zip(discrs,bins,binlabels,bintitles,nhistobins,minxvals,maxxvals):
  if '.xml' in discr:
    bdts.append(MVAPlot(ROOT.TH1F(discrname+"_"+bl,"BDT discriminator w/o MEM in "+bt,nb,minx,maxx),discr,b))
  else:
    bdts.append(Plot(ROOT.TH1F(discrname+"_"+bl,"MEM discriminator in "+bt,nb,minx,maxx),discr,b))

outputpath=plotParallel(name,500000,bdts,allsamples,[''],['1.'],weightsystnames, systweights)
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
