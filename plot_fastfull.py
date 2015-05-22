from plotutils import *
# samples

samples=[Sample('t#bar{t}H full',ROOT.kBlue,'/nfs/dust/cms/user/hmildner/fastsim/trees/tthbb_full.root','') , Sample('t#bar{t}H fast',ROOT.kGreen+1,'/nfs/dust/cms/user/hmildner/fastsim/trees/tthbb_fast.root','')]


plots=[
    Plot(ROOT.TH1F("N_Jets" ,"Number of jets > 30 GeV",12,-0.5,11.5),"N_Jets",""),
    Plot(ROOT.TH1F("N_BTagsM" ,"Number of b-tags",5,-0.5,4.5),"N_BTagsM",""),
    Plot(ROOT.TH1F("N_PrimaryVertices" ,"Number of PVs",41,-0.5,40.5),"N_PrimaryVertices",""),
    Plot(ROOT.TH1F("JT" ,"jet-tag categories",9,-0.5,8.5),"3*max(min(N_BTagsM-2,2),0)+max(min(N_Jets-4,2),0)",""),
    Plot(ROOT.TH1F("Jet_Pt" ,"jet pt",50,0,500),"Jet_Pt",""),
    Plot(ROOT.TH1F("Jet_Pt1" ,"1st jet pt",40,0,800),"Jet_Pt[0]",""),
    Plot(ROOT.TH1F("Jet_Pt2" ,"2nd jet pt",40,0,800),"Jet_Pt[1]",""),
    Plot(ROOT.TH1F("Jet_Pt3" ,"3rd jet pt",40,0,400),"Jet_Pt[2]",""),
    Plot(ROOT.TH1F("Jet_Pt4" ,"4th jet pt",40,0,400),"Jet_Pt[3]",""),
    Plot(ROOT.TH1F("Jet_Pt5" ,"5th jet pt",20,0,200),"Jet_Pt[4]",""),
    Plot(ROOT.TH1F("Jet_Pt6" ,"6th jet pt",20,0,200),"Jet_Pt[5]",""),
    Plot(ROOT.TH1F("Jet_Eta" ,"jet #eta",50,-2.5,2.5),"Jet_Eta",""),
    Plot(ROOT.TH1F("Jet_CSV" ,"CSVv2 IVF all jets",40,0,1),"Jet_CSV",""),
    Plot(ROOT.TH1F("Jet_CSVb" ,"CSVv2 IVF b-jets",40,0,1),"Jet_CSV","abs(Jet_Flav)>4.5"),
    Plot(ROOT.TH1F("Jet_CSVc" ,"CSVv2 IVF c-jets",40,0,1),"Jet_CSV","abs(Jet_Flav)>3.5&&abs(Jet_Flav)<4.5"),
    Plot(ROOT.TH1F("Jet_CSVl" ,"CSVv2 IVF l-jets",40,0,1),"Jet_CSV","abs(Jet_Flav)<3.5"),
    Plot(ROOT.TH1F("Jet_Charge" ,"jet charge",50,-1,1),"Jet_Charge",""),
    Plot(ROOT.TH1F("Jet_M" ,"jet mass",50,0,50),"Jet_M",""),
    Plot(ROOT.TH1F("Jet_Pt_OverGen" ,"jet pt / genjet pt",60,0.4,1.6),"Jet_Pt/Jet_GenPt",""),
    Plot(ROOT.TH1F("N_HiggsJets" ,"Number of CA 1.2 jets > 200 GeV",4,-0.5,3.5),"N_HiggsJets",""),
    Plot(ROOT.TH1F("HiggsJet_Pt" ,"CA 1.2 jet pt",50,0,1000),"HiggsJet_Pt",""),
    Plot(ROOT.TH1F("HiggsJet_Eta" ,"CA 1.2 jet eta",50,-2.5,2.5),"HiggsJet_Eta",""),
    Plot(ROOT.TH1F("HiggsJet_M2" ,"CA 1.2 jet di-filterjet mass",40,0,200),"HiggsJet_M2","HiggsJet_M2>1"),
    Plot(ROOT.TH1F("HiggsJet_CSV1" ,"CA 1.2 jet filterjet highets CSV",20,0,1),"HiggsJet_CSV1","HiggsJet_M2>1"),
    Plot(ROOT.TH1F("HiggsJet_CSV2" ,"CA 1.2 jet filterjet second highets CSV",20,0,1),"HiggsJet_CSV2","HiggsJet_M2>1"),
    Plot(ROOT.TH1F("N_TopJets" ,"Number of CA 1.5 jets > 200 GeV",4,-0.5,3.5),"N_TopJets",""),
    Plot(ROOT.TH1F("TopJet_Pt" ,"CA 1.5 jet pt",50,0,1000),"TopJet_Pt",""),
    Plot(ROOT.TH1F("TopJet_Eta" ,"CA 1.5 jet eta",50,-2.5,2.5),"TopJet_Eta",""),
    Plot(ROOT.TH1F("TopJet_M" ,"CA 1.5 jet mass",40,0,400),"TopJet_M",""),
    Plot(ROOT.TH1F("TopJet_Top_M" ,"CA 1.5 jet filtered top mass",50,0,250),"TopJet_Top_M",""),
    Plot(ROOT.TH1F("TopJet_W_M" ,"CA 1.5 jet filtered W mass",30,0,150),"TopJet_W_M",""),


]

listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfhistoLists(listOfhistoLists,samples,"plots_fastfull",True,'histoE',True)

