from scriptgenerator import *
from plotutils import *
import sys

path='/nfs/dust/cms/user/hmildner/trees0108/'
name='bdtplots_parrallel'

mcweight='(2.54*Weight_TopPt)*(N_LooseElectrons==0||N_LooseMuons==0)' 

samples=[Sample('t#bar{t}Htobb',ROOT.kBlue+1,path+'/ttHbb/*nominal*.root',mcweight,'ttHbb') ,     
         Sample('t#bar{t}',ROOT.kRed+1,path+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
]

plots=[Plot(ROOT.TH1F("N_Jets","Number of ak4 jets",11,-0.5,10.5),"N_Jets",''),
       MVAPlot(ROOT.TH1F("BDTcommon5","BDTcommon5",20,-1,1),"/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_64_common5.xml","N_Jets>=6&&N_BTagsM>=4"),
       Plot(ROOT.TH1F("BDTcommon5xc","BDTcommon5xc",20,-1,1),"BDT_common5_output","N_Jets>=6&&N_BTagsM>=4"),
       ]

outputpath=plotParallel(name,2000000,plots,samples)
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots)
writeListOfHistoLists(listOfHistoLists,samples,name,'')
