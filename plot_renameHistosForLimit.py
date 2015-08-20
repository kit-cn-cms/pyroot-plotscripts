from plotutils import *
# samples
samples=[Sample('t#bar{t}H bb',ROOT.kBlack,'/nfs/dust/cms/user/hmildner/trees0818/tth.root','') , 
         Sample('t#bar{t}l',2,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0'),
         Sample('t#bar{t}c#bar{c}',5,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusCC==1'),
         Sample('t#bar{t}b#bar{b}',3,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusBB==3'),
         Sample('t#bar{t}b',4,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusBB==1'),
         Sample('t#bar{t}2b',6,'/nfs/dust/cms/user/hmildner/trees0818/ttbar.root','GenEvt_I_TTPlusBB==2'),
]

systnames=["",
           "_CMS_ttH_CSVLFup","_CMS_ttH_CSVLFdown",
           "_CMS_ttH_CSVHFup","_CMS_ttH_CSVHFdown",
           "_CMS_ttH_CSVHFStats1up","_CMS_ttH_CSVHFStats1down",
           "_CMS_ttH_CSVLFStats1up","_CMS_ttH_CSVLFStats1down",
           "_CMS_ttH_CSVHFStats2up","_CMS_ttH_CSVHFStats2down",
           "_CMS_ttH_CSVLFStats2up","_CMS_ttH_CSVLFStats2down",
           "_CMS_ttH_CSVCErr1up","_CMS_ttH_CSVCErr1down",
           "_CMS_ttH_CSVCErr2up","_CMS_ttH_CSVCErr2down"]

binlabels=["4j3t","4j4t","5j3t","5j4t","6j2t","6j3t","6j4t"]
var="BDT_v3_output"
histofile='bdts.root'
new_samplenames=['ttH125','ttbarPlusOther','ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B']
new_binlabels=["j4_t3","j4_tge4","j5_t3","j5_tge4","jge6_t2","jge6_t3","jge6_tge4"]
new_histofile='new_bdts.root'
new_var='BDT_ljets'


f=ROOT.TFile(histofile)
n_f=ROOT.TFile(new_histofile,'recreate')
bin_fs=[ROOT.TFile(new_histofile.replace('.root','_'+bl+'.root'),'recreate') for bl in binlabels]
histos=[]
for smp,n_smp in zip([sample.name for sample in samples],new_samplenames):
    for sys,n_sys in zip(systnames,systnames):
        for bn,n_bn,bn_f in zip(binlabels,new_binlabels,bin_fs):
            h=f.Get(('_'.join([var,bn,smp])+sys)).Clone(('_'.join([n_smp,new_var,n_bn]))+n_sys)
            n_f.cd()
            h.Write()
            bn_f.cd()
            h.Write()

f.Close()            
n_f.Close()
for bn_f in bin_fs:
    bn_f.Close()
