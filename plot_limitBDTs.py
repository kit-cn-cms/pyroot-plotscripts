import sys
sys.argv.append( '-b-' )
from plotutils import *
import itertools

# config ----------------------------------------
# paths
tth_path_nominal='/nfs/dust/cms/user/hmildner/trees0818/tth_nominal.root'
ttbar_path_nominal='/nfs/dust/cms/user/hmildner/trees0818/ttbar_nominal.root'
tth_path_jesup='/nfs/dust/cms/user/hmildner/trees0818/tth_jesup.root'
ttbar_path_jesup='/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesup.root'
tth_path_jesdown='/nfs/dust/cms/user/hmildner/trees0818/tth_jesdown.root'
ttbar_path_jesdown='/nfs/dust/cms/user/hmildner/trees0818/ttbar_jesdown.root'
discriminator="BDT_v3_output"
histofile="test_bdtplots"
combine_histofile='new_bdts'
# end config ----------------------------------------

# no need to change things from here
samples=[Sample('t#bar{t}H bb',ROOT.kBlack,tth_path_nominal,'') , 
         Sample('t#bar{t}l',2,ttbar_path_nominal,'GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0'),
         Sample('t#bar{t}c#bar{c}',5,ttbar_path_nominal,'GenEvt_I_TTPlusCC==1'),
         Sample('t#bar{t}b#bar{b}',3,ttbar_path_nominal,'GenEvt_I_TTPlusBB==3'),
         Sample('t#bar{t}b',4,ttbar_path_nominal,'GenEvt_I_TTPlusBB==1'),
         Sample('t#bar{t}2b',6,ttbar_path_nominal,'GenEvt_I_TTPlusBB==2')
]
# data == ttbar (for now)
data = Sample('data',ROOT.kBlack,ttbar_path_nominal,'')

# names of the systematics (proper names needed e.g. for combination)
weightsystnames=["",
           "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down"]

# corresponding weight names
systweights=["1",
             "Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown",
             "Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down",
             "Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
             "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down"]

# create extra samples with special weights
samples_syst=[]
for sn,sw in zip(weightsystnames,systweights):
    for sample in samples:
        ss=sw
        if sample.selection != '':
            ss='('+sample.selection+')*'+ss
        samples_syst.append(Sample(sample.name+sn,sample.color,sample.path,ss))

# jes up and down are not done by weights
samples_jesup=[Sample('t#bar{t}H bb_CMS_scale_jUp',ROOT.kBlack,tth_path_jesup,'') , 
         Sample('t#bar{t}l_CMS_scale_jUp',2,ttbar_path_jesup,'GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0'),
         Sample('t#bar{t}c#bar{c}_CMS_scale_jUp',5,ttbar_path_jesup,'GenEvt_I_TTPlusCC==1'),
         Sample('t#bar{t}b#bar{b}_CMS_scale_jUp',3,ttbar_path_jesup,'GenEvt_I_TTPlusBB==3'),
         Sample('t#bar{t}b_CMS_scale_jUp',4,ttbar_path_jesup,'GenEvt_I_TTPlusBB==1'),
         Sample('t#bar{t}2b_CMS_scale_jUp',6,ttbar_path_jesup,'GenEvt_I_TTPlusBB==2'),
]
samples_jesdown=[Sample('t#bar{t}H bb_CMS_scale_jDown',ROOT.kBlack,'/nfs/dust/cms/user/hmildner/trees0818/tth_jesdown.root','') , 
         Sample('t#bar{t}l_CMS_scale_jDown',2,ttbar_path_jesdown,'GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0'),
         Sample('t#bar{t}c#bar{c}_CMS_scale_jDown',5,ttbar_path_jesdown,'GenEvt_I_TTPlusCC==1'),
         Sample('t#bar{t}b#bar{b}_CMS_scale_jDown',3,ttbar_path_jesdown,'GenEvt_I_TTPlusBB==3'),
         Sample('t#bar{t}b_CMS_scale_jDown',4,ttbar_path_jesdown,'GenEvt_I_TTPlusBB==1'),
         Sample('t#bar{t}2b_CMS_scale_jDown',6,ttbar_path_jesdown,'GenEvt_I_TTPlusBB==2'),
]

samples_syst=samples_syst+samples_jesup+samples_jesdown+[data]

# definition of analysis bins
s4j3t="(N_Jets==4&&N_BTagsM==3)"
s4j4t="(N_Jets==4&&N_BTagsM>=4)"
s5j3t="(N_Jets==5&&N_BTagsM==3)"
s5j4t="(N_Jets==5&&N_BTagsM>=4)"
s6j2t="(N_Jets>=6&&N_BTagsM==2)"
s6j3t="(N_Jets>=6&&N_BTagsM==3)"
s6j4t="(N_Jets>=6&&N_BTagsM>=4)"
bins=     [s4j3t,s4j4t,s5j3t,s5j4t,s6j2t,s6j3t,s6j4t]
# corresponding labels
binlabels=["4j3t","4j4t","5j3t","5j4t","6j2t","6j3t","6j4t"]
# number of bins in each category
nhistobins=    [20,    10,    20,    10      ,20,   20,    10]

# generate plots
bdts=[]
for b,bl,nb in zip(bins,binlabels,nhistobins):
    bdts.append(Plot(ROOT.TH1F(discriminator+"_"+bl,discriminator+" ("+bl+")",nb,-1,1),discriminator,b))

# function that creates a list of lists with histograms of all samples in all anlysis bins
bdthistos_lol=createHistoLists_fromTree(bdts,samples_syst,'MVATree')

# write the histograms into a root file
writeListOfHistoListsToFile(bdthistos_lol,samples_syst,histofile)

# now open root file again and rename histograms

systnames=weightsystnames+["_CMS_scale_jUp","_CMS_scale_jDown"]
# naming conventions needed for limit script
new_samplenames=['ttH125','ttbarOther','ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B']
new_binlabels=["j4_t3","j4_t4","j5_t3","j5_tge4","jge6_t2","jge6_t3","jge6_tge4"]
new_discriminator='BDT_ljets'

f=ROOT.TFile(histofile+'.root')
#ugly code to write down everything with the correct naming conventions
n_f=ROOT.TFile(combine_histofile+'.root','recreate')
bin_fs=[ROOT.TFile(combine_histofile+'_'+bl+'.root','recreate') for bl in binlabels]
for smp,n_smp in zip([sample.name for sample in samples+[data]],new_samplenames+['data_obs']):
    for sys,n_sys in zip(systnames,systnames):
        if n_smp=='data_obs' and n_sys!='': continue
        for bn,n_bn,bn_f in zip(binlabels,new_binlabels,bin_fs):
            getname=('_'.join([discriminator,bn,smp]))+sys
            newname=('_'.join([n_smp,new_discriminator,n_bn]))+n_sys
            print 'getting',getname
            h=f.Get(getname).Clone(newname)
            print 'renaming to',newname
            n_f.cd()
            h.Write()
            bn_f.cd()
            h.Write()

f.Close()            
n_f.Close()
for bn_f in bin_fs:
    bn_f.Close()
    
