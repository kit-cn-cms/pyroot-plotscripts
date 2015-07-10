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


samples_tth=[Sample('t#bar{t}H',ROOT.kCyan,'/nfs/dust/cms/user/hmildner/thqtrees/tth2.root',""),
             Sample('t#bar{t}H, 3-tag tHq bin',ROOT.kBlue,'/nfs/dust/cms/user/hmildner/thqtrees/tth2.root',stHq3t),
             Sample('t#bar{t}H, 4-tag tHq bin',ROOT.kBlue+4,'/nfs/dust/cms/user/hmildner/thqtrees/tth2.root',stHq4t)]

samples_thq=[Sample('tHq',ROOT.kGreen,'/nfs/dust/cms/user/hmildner/thqtrees/thq2.root',""),
             Sample('tHq, 3-tag tHq bin',ROOT.kGreen+2,'/nfs/dust/cms/user/hmildner/thqtrees/thq2.root',stHq3t),
             Sample('tHq, 4-tag tHq bin',ROOT.kGreen+4,'/nfs/dust/cms/user/hmildner/thqtrees/thq2.root',stHq4t)]

samples_tt=[
         Sample('t#bar{t}',ROOT.kRed,'/nfs/dust/cms/user/hmildner/thqtrees/ttbar2.root',""),
         Sample('t#bar{t}, 3-tag tHq bin',ROOT.kRed+2,'/nfs/dust/cms/user/hmildner/thqtrees/ttbar2.root',stHq3t),
         Sample('t#bar{t}, 4-tag tHq bin',ROOT.kRed+4,'/nfs/dust/cms/user/hmildner/thqtrees/ttbar2.root',stHq4t)
]

samples_selected=[Sample('t#bar{t}H, tHq selected',ROOT.kBlue,'/nfs/dust/cms/user/hmildner/thqtrees/tth2.root',stHq),
                  Sample('tHq, tHq selected',ROOT.kGreen+2,'/nfs/dust/cms/user/hmildner/thqtrees/thq2.root',stHq),
                  Sample('t#bar{t} x .01, tHq selected',ROOT.kRed+2,'/nfs/dust/cms/user/hmildner/thqtrees/ttbar2.root',stHq+"*0.01")]

plots=[
    Plot(ROOT.TH1F("JT" ,"jet-tag categories",9,-0.5,8.5),"3*max(min(N_BTagsM-2,2),0)+max(min(N_Jets-4,2),0)","N_BTagsM>=2")]


listOfhistoLists_tth=createHistoLists_fromTree(plots,samples_tth,'MVATree')
listOfhistoLists_thq=createHistoLists_fromTree(plots,samples_thq,'MVATree')
listOfhistoLists_tt=createHistoLists_fromTree(plots,samples_tt,'MVATree')
listOfhistoLists_selected=createHistoLists_fromTree(plots,samples_selected,'MVATree')
for hl in listOfhistoLists_tth + listOfhistoLists_thq + listOfhistoLists_tt + listOfhistoLists_selected:
    for h in hl:
        h.GetXaxis().SetBinLabel(1,'4j2t')
        h.GetXaxis().SetBinLabel(2,'5j2t')
        h.GetXaxis().SetBinLabel(3,'6j2t')
        h.GetXaxis().SetBinLabel(4,'4j3t')
        h.GetXaxis().SetBinLabel(5,'5j3t')
        h.GetXaxis().SetBinLabel(6,'6j3t')
        h.GetXaxis().SetBinLabel(7,'4j4t')
        h.GetXaxis().SetBinLabel(8,'5j4t')
        h.GetXaxis().SetBinLabel(9,'6j4t')


writeListOfhistoLists(listOfhistoLists_tth,samples_tth,"tth",False,False,True)
writeListOfhistoLists(listOfhistoLists_thq,samples_thq,"thq",False,False,True)
writeListOfhistoLists(listOfhistoLists_tt,samples_tt,"tt",False,False,True)
writeListOfhistoLists(listOfhistoLists_selected,samples_selected,"thqselected",False,False,False)
