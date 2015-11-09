from scriptgenerator import *
from plotutils import *
import sys

lumi='1.28'
path='/nfs/dust/cms/user/hmildner/trees1027/'

sel="(N_TightLeptons==1)*(N_LooseLeptons==1)*(N_BTagsM>=2)*(N_Jets>=4)"
sel_mu='(N_TightMuons==1)*(N_LooseMuons==1)*(N_LooseElectrons==0)'
sel_el='(N_TightElectrons==1)*(N_LooseElectrons==1)*(N_LooseMuons==0)'
mcmatch='(BoostedJet_Top_Pt[0]>0)&&((BoostedJet_Dr_GenB[0]>=0&&BoostedJet_Dr_GenB[0]<1.5)&&(BoostedJet_Dr_GenQ1[0]>=0&&BoostedJet_Dr_GenQ1[0]<1.5)&&(BoostedJet_Dr_GenQ2[0]>=0&&BoostedJet_Dr_GenQ2[0]<1.5))'
notmcmatch='(!((BoostedJet_Top_Pt[0]>0)&&((BoostedJet_Dr_GenB[0]>=0&&BoostedJet_Dr_GenB[0]<1.5)&&(BoostedJet_Dr_GenQ1[0]>=0&&BoostedJet_Dr_GenQ1[0]<1.5)&&(BoostedJet_Dr_GenQ2[0]>=0&&BoostedJet_Dr_GenQ2[0]<1.5))))'
# samples

samples_data=[Sample('SingleMu',ROOT.kBlack,path+'/mu_prompt/*nominal*.root',sel_mu),
              Sample('SingleMuRe',ROOT.kBlack,path+'/mu_reminiaod/*nominal*.root',sel_mu),
              Sample('SingleEl',ROOT.kBlack,path+'/el_prompt/*nominal*.root',sel_el),
              Sample('SingleElRe',ROOT.kBlack,path+'/el_reminiaod/*nominal*.root',sel_el)]
samples=[Sample('t#bar{t}',ROOT.kRed+1,path+'/ttbar/*nominal*.root',lumi,'ttbar') ,     
         Sample('Single Top',ROOT.kMagenta,path+'/st_*/*nominal*.root',lumi,'SingleTop') , 
         Sample('W+jets',ROOT.kGreen-3,path+'/Wjets/*nominal*.root',lumi,'Wjets') , 
         Sample('Z+jets',ROOT.kAzure-2 ,path+'/Zjets_*/*nominal*root',lumi,'Zjets') , 
]

plots=[
    Plot(ROOT.TH1F("BoostedTop_TopHadCandidate_Pt","p_{T} (leading CA 1.5 jet)",50,150,650),"BoostedJet_FatJet_Pt[0]","(BoostedJet_Top_Pt[0]>10)"),
    Plot(ROOT.TH1F("BoostedTop_TopHadCandidate_Top_Pt","Filtered jet p_{T} (leading CA 1.5 jet)",50,0,500),"BoostedJet_Top_Pt[0]","(BoostedJet_Top_Pt[0]>10)"),
    Plot(ROOT.TH1F("BoostedTop_TopHadCandidate_NSub32","NSubjettiness ratio #tau_{3}/#tau_{2} (leading CA 1.5 jet)",50,0,1),"BoostedJet_Tau3Filtered[0]/BoostedJet_Tau2Filtered[0]","(BoostedJet_Top_Pt[0]>10)"),
    Plot(ROOT.TH1F("BoostedTop_TopHadCandidate_NSub21","NSubjettiness ratio #tau_{2}/#tau_{1} (leading CA 1.5 jet)",50,0,1),"BoostedJet_Tau2Filtered[0]/BoostedJet_Tau1Filtered[0]","(BoostedJet_Top_Pt[0]>10)"),
    Plot(ROOT.TH1F("BoostedTop_TopHadCandidate_TopMVAOutput","BDT top tag (leading CA 1.5 jet)",50,-1,1),"BoostedJet_TopTag_BDT_Std[0]","(BoostedJet_Top_Pt[0]>10)"),
    Plot(ROOT.TH1F("BoostedTop_TopHadCandidate_Top_M","Filtered top mass (leading CA 1.5 jet)",60,0,300),"BoostedJet_Top_M[0]","(BoostedJet_Top_Pt[0]>10)"),
    Plot(ROOT.TH1F("BoostedTop_TopHadCandidate_W_M","Filtered W mass (leading CA 1.5 jet)",50,0,200),"BoostedJet_Wbtag_M[0]","(BoostedJet_Top_Pt[0]>10)"),
    Plot(ROOT.TH1F("plot1","Hardest filtered jet (in leading CA 1.5 jet)",60,0,300),"BoostedJet_Filterjet1_Pt[0]","(BoostedJet_Filterjet1_Pt[0]>10)"),
    Plot(ROOT.TH1F("plot2","Second filtered jet (in leading CA 1.5 jet)",60,0,300),"BoostedJet_Filterjet2_Pt[0]","(BoostedJet_Filterjet2_Pt[0]>10)"),
    Plot(ROOT.TH1F("plot3","Highest filter jet b-tag (in leading CA 1.5 jet)",44,-.1,1),"BoostedJet_CSV1[0]","(BoostedJet_Filterjet1_Pt[0]>10)"),
    Plot(ROOT.TH1F("plot4","Second filter jet b-tag (in leading CA 1.5 jet)",44,-.1,1),"BoostedJet_CSV2[0]","(BoostedJet_Filterjet1_Pt[0]>10)"),
    Plot(ROOT.TH1F("plot5","Mass of two filter jets (in leading CA 1.5 jet)",50,0,250),"BoostedJet_M2[0]","(BoostedJet_M2[0]>1)"),
    Plot(ROOT.TH1F("plot6","Mass of three filter jets (in leading CA 1.5 jet)",50,0,250),"BoostedJet_M3[0]","(BoostedJet_M3[0]>1)"),
    Plot(ROOT.TH1F("N_Jets","Number of ak4 jets",11,-0.5,10.5),"N_Jets",''),
    Plot(ROOT.TH1F("CSV0","B-tag of leading jet",44,-.1,1),"Jet_CSV[0]",''),
    Plot(ROOT.TH1F("CSV1","B-tag of second jet",44,-.1,1),"Jet_CSV[1]",''),
    Plot(ROOT.TH1F("pt1","p_{T} of leading jet",50,0,500),"Jet_Pt[0]",''),
    Plot(ROOT.TH1F("pt2","p_{T} of second jet",50,0,500),"Jet_Pt[1]",''),
    Plot(ROOT.TH1F("eta1","#eta of leading jet",50,-2.5,2.5),"Jet_Eta[0]",''),
    Plot(ROOT.TH1F("eta2","#eta of second jet",50,-2.5,2.5),"Jet_Eta[1]",''),
    Plot(ROOT.TH1F("N_BTagsM","Number of b-tags",6,-0.5,5.5),"N_BTagsM",''),
    Plot(ROOT.TH1F("Evt_HT_Jets","Sum p_{T} jets",75,0,1500),"Evt_HT_Jets",''),
    Plot(ROOT.TH1F("N_BoostedJets","Number of CA 1.5 jets",5,-0.5,4.5),"N_BoostedJets",''),
    Plot(ROOT.TH1F("ptalljets","p_{T} of all jets",60,0,300),"Jet_Pt",''),
    Plot(ROOT.TH1F("csvalljets","csv of all jets",44,-.1,1),"Jet_CSV",''),
    Plot(ROOT.TH1F("csvallbjets","csv of all jets > 40 GeV",44,-.1,1),"Jet_CSV",'Jet_Pt>40'),
    Plot(ROOT.TH1F("JT" ,"jet-tag categories",9,-0.5,8.5),"3*max(min(N_BTagsM-2,2),0)+max(min(N_Jets-4,2),0)","(N_BTagsM>=2&&N_Jets>=4)")

]
outputpath=plotParallel("allplots",2000000,plots,samples+samples_data,[''],[sel])
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots)
for hld,hl in zip(listOfHistoListsData,listOfHistoLists)
    if "JT" in hld[0].GetName():
        eventYields(hld,hl,samples,"yields")
plotDataMC(listOfHistoListsData,listOfHistoLists,samples,"allplots",False,"")
