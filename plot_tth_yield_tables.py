from plotutils import *
# samples
lumi="10"

samples=[
    Sample('t#bar{t}H, H to bb',ROOT.kBlue+1,'/nfs/dust/cms/user/hmildner/trees1027/ttH_nominal.root',lumi) ,   
    Sample('t#bar{t}+light',ROOT.kCyan,'/nfs/dust/cms/user/hmildner/trees1027/ttbar_nominal.root','(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0)'+'*'+lumi),
    Sample('t#bar{t}+c#bar{c}',ROOT.kMagenta,'/nfs/dust/cms/user/hmildner/trees1027/ttbar_nominal.root','(GenEvt_I_TTPlusCC==1)'+'*'+lumi),
    Sample('t#bar{t}+b',ROOT.kRed,'/nfs/dust/cms/user/hmildner/trees1027/ttbar_nominal.root','(GenEvt_I_TTPlusBB==1)'+'*'+lumi),
    Sample('t#bar{t}+2b',ROOT.kRed+2,'/nfs/dust/cms/user/hmildner/trees1027/ttbar_nominal.root','(GenEvt_I_TTPlusBB==2)'+'*'+lumi),
    Sample('t#bar{t}+b#bar{b}',ROOT.kRed+4,'/nfs/dust/cms/user/hmildner/trees1027/ttbar_nominal.root','(GenEvt_I_TTPlusBB==3)'+'*'+lumi),


]


# selecion for categories
b1="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>0.1650&&BoostedTopHiggs_HiggsCandidate_HiggsTag>0.9425)"
b2="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>-0.685&&BoostedTopHiggs_HiggsCandidate_HiggsTag>0.8132)"
b3="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>-0.875&&BoostedTopHiggs_HiggsCandidate_HiggsTag>0.2578)"
boosted=b3
lsel="((N_TightLeptons==1&&N_LooseLeptons==1)&&(N_Jets>=4&&N_BTagsM>=3||N_Jets>=6&&N_BTagsM>=2||N_Jets>=4&&N_BTagsM>=2&&"+boosted+"))"
s4j3t="((N_Jets==4&&N_BTagsM==3)&&!"+boosted+")"
s4j4t="((N_Jets==4&&N_BTagsM>=4)&&!"+boosted+")"
s5j3t="((N_Jets==5&&N_BTagsM==3)&&!"+boosted+")"
s5j4t="((N_Jets==5&&N_BTagsM>=4)&&!"+boosted+")"
s6j2t="((N_Jets>=6&&N_BTagsM==2)&&!"+boosted+")"
s6j3t="((N_Jets>=6&&N_BTagsM==3)&&!"+boosted+")"
s6j4t="((N_Jets>=6&&N_BTagsM>=4)&&!"+boosted+")"

bins=[s4j3t,s4j4t,s5j3t,s5j4t,s6j2t,s6j3t,s6j4t,boosted]
binlabels=["4j3t","4j4t","5j3t","5j4t","6j2t","6j3t","6j4t","boosted"]
s_bins=""
for i, b in enumerate(bins):
    s_bins+=str(i)+"*("+b+")"
    if i<len(bins)-1:
        s_bins+="+"    
        
plots=[    
    Plot(ROOT.TH1F("table" ,"table",len(bins),-0.5,len(bins)-0.5,),s_bins,lsel)    
]

listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
for hl in listOfhistoLists:
    for h,s in zip(hl,samples):
        for i, b in enumerate(binlabels):
            h.GetXaxis().SetBinLabel(i+1,b)
    turn1dHistosToTable(hl,samples,"yields")
    
