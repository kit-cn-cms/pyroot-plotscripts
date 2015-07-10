from plotutils import *


# selecion for categories
s4j3t="(N_Jets==4&&N_BTagsM==3)"
s4j4t="(N_Jets==4&&N_BTagsM>=4)"
s5j3t="(N_Jets==5&&N_BTagsM==3)"
s5j4t="(N_Jets==5&&N_BTagsM>=4)"
s6j2t="(N_Jets>=6&&N_BTagsM==2)"
s6j3t="(N_Jets>=6&&N_BTagsM==3)"
s6j4t="(N_Jets>=6&&N_BTagsM>=4)"
stHq="(I_PassesTHQJetSelection>0.5&&Evt_Pt_MET>40&&N_TaggedSingleTopJetsT==3)"
stHq3t="(I_PassesTHQJetSelection>0.5&&Evt_Pt_MET>40&&N_TaggedSingleTopJetsT==3)"
stHq4t="(I_PassesTHQJetSelection>0.5&&Evt_Pt_MET>40&&N_TaggedSingleTopJetsT>=4)"

samples=[Sample('t#bar{t}H, tHq selected',ROOT.kBlue,'/nfs/dust/cms/user/hmildner/thqtrees/tth2.root',stHq),
                  Sample('tHq, tHq selected',ROOT.kGreen+2,'/nfs/dust/cms/user/hmildner/thqtrees/thq2.root',stHq),
                  Sample('t#bar{t} x .01, tHq selected',ROOT.kRed+2,'/nfs/dust/cms/user/hmildner/thqtrees/ttbar2.root',stHq+"*0.01")]


histos=[
    ROOT.TH1F("Evt_HT" ,"HT",20,0,2000),
    ROOT.TH1F("SingleTopJet_Pt" ,"jet p_{T} (tHq-definition)",30,0,300),
    ROOT.TH1F("SingleTopJet_Eta" ,"jet #eta  (tHq-definition)",25,-5,5),
#    ROOT.TH1F("Evt_Pt_MET" ,"MET",50,0,500),
#    ROOT.TH1F("Evt_Pt_PrimaryLepton" ,"Lepton pt",50,0,500),
#    ROOT.TH1F("Evt_Eta_PrimaryLepton" ,"Lepton eta",50,-2.5,2.5),
#    ROOT.TH1F("Jet1_Pt" ,"Jet1 pt",50,0,500),
#    ROOT.TH1F("Jet2_Pt" ,"Jet2 pt",50,0,500),
#    ROOT.TH1F("Jet3_Pt" ,"Jet3 pt",50,0,500),
#    ROOT.TH1F("Jet4_Pt" ,"Jet4 pt",50,0,500),
#    ROOT.TH1F("Jet1_Eta" ,"Jet1 eta",50,-2.5,2.5),
#    ROOT.TH1F("Jet2_Eta" ,"Jet2 eta",50,-2.5,2.5),
#    ROOT.TH1F("Jet3_Eta" ,"Jet3 eta",50,-2.5,2.5),
#    ROOT.TH1F("Jet4_Eta" ,"Jet4 eta",50,-2.5,2.5),
#    ROOT.TH1F("SingleTopJet1_Pt" ,"SingleTopJet1 pt",50,0,500),
#    ROOT.TH1F("SingleTopJet2_Pt" ,"SingleTopJet2 pt",50,0,500),
#    ROOT.TH1F("SingleTopJet3_Pt" ,"SingleTopJet3 pt",50,0,500),
#    ROOT.TH1F("SingleTopJet4_Pt" ,"SingleTopJet4 pt",50,0,500),
#    ROOT.TH1F("SingleTopJet1_Eta" ,"SingleTopJet1 eta",100,-5,5),
#    ROOT.TH1F("SingleTopJet2_Eta" ,"SingleTopJet2 eta",100,-5,5),
#    ROOT.TH1F("SingleTopJet3_Eta" ,"SingleTopJet3 eta",100,-5,5),
#    ROOT.TH1F("SingleTopJet4_Eta" ,"SingleTopJet4 eta",100,-5,5),
    ROOT.TH1F("Evt_SingleTopJet_MaxEta" ,"max abs(#eta) jets (tHq-definition)",20,0,5),
#    ROOT.TH1F("Sphericity" ,"Sphericity",50,0,1),
#    ROOT.TH1F("Aplanarity" ,"Aplanarity",50,0,0.5),
]
variables=[
    "Evt_HT",    
    "SingleTopJet_Pt",
    "SingleTopJet_Eta",
#    "Evt_Pt_MET",
#    "Evt_Pt_PrimaryLepton",
#    "Evt_Eta_PrimaryLepton",
#    "Jet_Pt[0]",
#    "Jet_Pt[1]",
#    "Jet_Pt[2]",
#    "Jet_Pt[3]",
#    "Jet_Eta[0]",
#    "Jet_Eta[1]",
#    "Jet_Eta[2]",
#    "Jet_Eta[3]",
#    "SingleTopJet_Pt[0]",
#    "SingleTopJet_Pt[1]",
#    "SingleTopJet_Pt[2]",
#    "SingleTopJet_Pt[3]",
#    "SingleTopJet_Eta[0]",
#    "SingleTopJet_Eta[1]",
#    "SingleTopJet_Eta[2]",
#    "SingleTopJet_Eta[3]",
    "Evt_SingleTopJet_MaxEta",
#    "Evt_Sphericity",
#    "Evt_Aplanarity",
]

selections=[ "(N_Jets==4&&N_BTagsM==3)"+"&&"+stHq,
             "(N_Jets==5&&N_BTagsM==3)"+"&&"+stHq,
             "(N_Jets>=6&&N_BTagsM==3)"+"&&"+stHq,
             "(N_Jets==4&&N_BTagsM>=4)"+"&&"+stHq,
             "(N_Jets==5&&N_BTagsM>=4)"+"&&"+stHq,
             "(N_Jets>=6&&N_BTagsM>=4)"+"&&"+stHq,
            ]
selectionnames=[", tHq sel. and 4j3t",
                ", tHq sel. and 5j3t",
                ", tHq sel. and 6j3t",
                ", tHq sel. and 4j4t",
                ", tHq sel. and 5j4t",
                ", tHq sel. and 6j4t"]

plots=plotsForSelections_cross_Histos(selections,selectionnames,histos,variables)
listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfhistoLists(listOfhistoLists,samples,"thqplots_in_categories",True)
