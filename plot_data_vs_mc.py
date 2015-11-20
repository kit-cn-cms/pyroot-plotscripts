from scriptgenerator import *
from plotutils import *
import sys


path='/nfs/dust/cms/user/hmildner/trees1107/'

sel_singleel="(N_LooseMuons==0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)" # and vice versa...
mcweight='(1.28*Weight_PV)*(N_LooseElectrons==0||N_LooseMuons==0)' # some weights are only applied on mc

selection="((N_TightLeptons==1)*(N_LooseLeptons==1)*(N_BTagsM>=2)*(N_Jets>=4))" # l+jets channel

# samples
samples_data=[Sample('SingleMu',ROOT.kBlack,path+'/mu_prompt/*nominal*.root',sel_singlemu),
              Sample('SingleMuRe',ROOT.kBlack,path+'/mu_reminiaod/*nominal*.root',sel_singlemu),
              Sample('SingleEl',ROOT.kBlack,path+'/el_prompt/*nominal*.root',sel_singleel),
              Sample('SingleElRe',ROOT.kBlack,path+'/el_reminiaod/*nominal*.root',sel_singleel)]
samples=[Sample('t#bar{t}H',ROOT.kBlue+1,path+'/ttH*/*nominal*.root',mcweight,'ttH') ,     
         Sample('t#bar{t}',ROOT.kRed+1,path+'/ttbar/*nominal*.root',mcweight,'ttbar') ,     
         Sample('Single Top',ROOT.kMagenta,path+'/st*/*nominal*.root',mcweight,'SingleTop') , 
         Sample('W+jets',ROOT.kGreen-3,path+'/Wjets/*nominal*.root',mcweight,'Wjets') , 
         Sample('Z+jets',ROOT.kAzure-2 ,path+'/Zjets_*/*nominal*root',mcweight,'Zjets') , 
]

plots=[
    Plot(ROOT.TH1F("N_PrimaryVertices","Reconstructed primary vertices",31,-.5,30.5),"N_PrimaryVertices",selection),
    Plot(ROOT.TH1F("N_Jets","Number of ak4 jets",11,-0.5,10.5),"N_Jets",selection),
]
listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
listOfhistoLists_data=createHistoLists_fromTree(plots,samples_data,'MVATree')
plotDataMC(listOfhistoLists_data,listOfhistoLists,samples,"datavsmc",False,'')
