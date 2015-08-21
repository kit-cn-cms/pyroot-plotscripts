from plotutils import *
# samples
samples=[Sample('t#bar{t}H bb',ROOT.kBlack,'/nfs/dust/cms/user/hmildner/trees0818/tth.root','') , 
         Sample('t#bar{t}l',2,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0'),
         Sample('t#bar{t}c#bar{c}',5,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusCC==1'),
         Sample('t#bar{t}b#bar{b}',3,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusBB==3'),
         Sample('t#bar{t}b',4,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusBB==1'),
         Sample('t#bar{t}2b',6,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusBB==2')
]

data = Sample('data',ROOT.kBlack,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','')

systnames=["",
           "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down"]

systweights=["1",
             "Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown",
             "Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down",
             "Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
             "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down"]
samples_syst=[]
for sn,sw in zip(systnames,systweights):
    for sample in samples:
        ss=sw
        if sample.selection != '':
            ss='('+sample.selection+')*'+ss
        samples_syst.append(Sample(sample.name+sn,sample.color,sample.path,ss))

samples_jesup=[Sample('t#bar{t}H bb_CMS_scale_jUp',ROOT.kBlack,'/nfs/dust/cms/user/hmildner/trees0818/tth_jesup.root','') , 
         Sample('t#bar{t}l_CMS_scale_jUp',2,'/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesup.root','GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0'),
         Sample('t#bar{t}c#bar{c}_CMS_scale_jUp',5,'/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesup.root','GenEvt_I_TTPlusCC==1'),
         Sample('t#bar{t}b#bar{b}_CMS_scale_jUp',3,'/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesup.root','GenEvt_I_TTPlusBB==3'),
         Sample('t#bar{t}b_CMS_scale_jUp',4,'/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesup.root','GenEvt_I_TTPlusBB==1'),
         Sample('t#bar{t}2b_CMS_scale_jUp',6,'/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesup.root','GenEvt_I_TTPlusBB==2'),
]

samples_jesdown=[Sample('t#bar{t}H bb_CMS_scale_jDown',ROOT.kBlack,'/nfs/dust/cms/user/hmildner/trees0818/tth_jesdown.root','') , 
         Sample('t#bar{t}l_CMS_scale_jDown',2,'/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesdown.root','GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0'),
         Sample('t#bar{t}c#bar{c}_CMS_scale_jDown',5,'/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesdown.root','GenEvt_I_TTPlusCC==1'),
         Sample('t#bar{t}b#bar{b}_CMS_scale_jDown',3,'/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesdown.root','GenEvt_I_TTPlusBB==3'),
         Sample('t#bar{t}b_CMS_scale_jDown',4,'/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesdown.root','GenEvt_I_TTPlusBB==1'),
         Sample('t#bar{t}2b_CMS_scale_jDown',6,'/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesdown.root','GenEvt_I_TTPlusBB==2'),
]
samples_syst=samples_syst+samples_jesup+samples_jesdown+[data]

s4j3t="(N_Jets==4&&N_BTagsM==3)"
s4j4t="(N_Jets==4&&N_BTagsM>=4)"
s5j3t="(N_Jets==5&&N_BTagsM==3)"
s5j4t="(N_Jets==5&&N_BTagsM>=4)"
s6j2t="(N_Jets>=6&&N_BTagsM==2)"
s6j3t="(N_Jets>=6&&N_BTagsM==3)"
s6j4t="(N_Jets>=6&&N_BTagsM>=4)"

bins=     [s4j3t,s4j4t,s5j3t,s5j4t,s6j2t,s6j3t,s6j4t]
binlabels=["4j3t","4j4t","5j3t","5j4t","6j2t","6j3t","6j4t"]
nbins=    [20,    10,    20,    10      ,20,   20,    10]
bdts=[]
for b,bl,nb in zip(bins,binlabels,nbins):
    bdts.append(Plot(ROOT.TH1F("BDT_v3_output_"+bl,"BDT_v3_output ("+bl+")",nb,-1,1),"BDT_v3_output",b))

bdthistos=createHistoLists_fromTree(bdts,samples_syst,'MVATree')

writeListOfHistoListsToFile(bdthistos,samples_syst,"bdts")
    
