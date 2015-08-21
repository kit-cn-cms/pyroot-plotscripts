from plotutils import *
# samples
systnames=["",
           "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown",
           "_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down",
           "_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down",
           "_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down",
           "_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down",
           "_CMS_scale_jUp","_CMS_scale_jDown"]

new_samplenames=['ttH125','ttbarOther','ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B']
new_binlabels=["j4_t3","j4_t4","j5_t3","j5_tge4","jge6_t2","jge6_t3","jge6_tge4"]
new_histofile='new_bdts.root'
new_var='BDT_ljets'


n_f=ROOT.TFile(new_histofile,'readonly')
lolT_samplecomp=[]
lolT_systcomp_tth=[]
for n_smp in new_samplenames+['data_obs']: #samples
    if n_smp!='data_obs':
        lolT_samplecomp.append([])
    for n_sys in systnames:                  #systematics
        if n_smp=='data_obs': continue     
        if n_smp=='ttH125':
            lolT_systcomp_tth.append([])
        for n_bn in new_binlabels:             #categories
            newname=('_'.join([n_smp,new_var,n_bn]))+n_sys
            print newname
            h=n_f.Get(newname)
            if n_smp=='ttH125':
                lolT_systcomp_tth[-1].append(h)
            if n_sys=='':
                lolT_samplecomp[-1].append(h)


print lolT_samplecomp
lol_samplecomp=transposeLOL(lolT_samplecomp)
print lol_samplecomp
lol_systcomp_tth=transposeLOL(lolT_systcomp_tth)

samples=[]
systsamples_tth=[]
systcolors=[i+1 for i in range(len(systnames))]
samplecolors=[i+1 for i in range(len(new_samplenames))]
for syst,color in zip(systnames,systcolors):
    systsamples_tth.append(Sample('ttH125'+syst,color,'',''))

for sn,color in zip(new_samplenames,samplecolors):
    samples.append(Sample(sn,color,'',''))           



writeListOfhistoLists(lol_systcomp_tth,systsamples_tth,"systcomp",False)
print samples
writeListOfhistoLists(lol_samplecomp,samples,"samplecomp",False)
writeListOfhistoLists(lol_samplecomp,samples,"samplecomp_norm",True)
    

n_f.Close()
