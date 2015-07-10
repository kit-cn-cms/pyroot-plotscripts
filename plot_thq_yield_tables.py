from plotutils import *
samples=[Sample('t#bar{t}H',ROOT.kCyan,'/nfs/dust/cms/user/hmildner/thqtrees/tth2.root',""),
         Sample('tHq',ROOT.kCyan,'/nfs/dust/cms/user/hmildner/thqtrees/thq2.root',""),
         Sample('t#bar{t}',ROOT.kRed+1,'/nfs/dust/cms/user/hmildner/thqtrees/ttbar2.root',"")
]

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


plots=[    
    Plot(ROOT.TH2F("table" ,"table",3,-0.5,2.5,9,-0.5,8.5),"3*max(min(N_BTagsM-2,2),0)+max(min(N_Jets-4,2),0):("+stHq3t+"*1+"+stHq4t+"*2)","N_Jets>=4&&N_BTagsM>=2")
]

listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
tthcats=["4j2t","5j2t","6j2t","4j3t","5j3t","6j3t","4j4t","5j4t","6j4t"]
thqcats=["None","3t","4t"]
canvases=[]
n=0
for hl in listOfhistoLists:
    thq_tth=hl[1].Clone()
    thq_tth.Divide(hl[0])
    thq_tth.Scale(100.)
    hl.append(thq_tth)
    tth_tt=hl[0].Clone()
    tth_tt.Divide(hl[2])
    tth_tt.Scale(100.)
    hl.append(tth_tt)
    thq_tt=hl[1].Clone()
    thq_tt.Divide(hl[2])
    thq_tt.Scale(100.)
    hl.append(thq_tt)


    for h in hl:
        setupHisto(h,ROOT.kBlack,"",False)
        h.GetXaxis().SetTitle("single top category")
        h.GetYaxis().SetTitle("ttH category")
        for (i,c) in list(enumerate(tthcats, start=1)):
            h.GetYaxis().SetBinLabel(i,c)
        for (i,c) in list(enumerate(thqcats, start=1)):
            h.GetXaxis().SetBinLabel(i,c)
        canvas=getCanvas("c"+str(n))
        n+=1
        h.Draw("COLTEXT")
        canvases.append(canvas)

        writeHistoToTable(h,"table"+str(n))
    writeHistoListToTable(hl[:3],[s.name for s in samples],"allthree")


printCanvases(canvases,"table_plots")
