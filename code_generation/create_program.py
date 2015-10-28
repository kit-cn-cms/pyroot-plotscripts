from scriptgenerator import *

b1="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>0.1650&&BoostedTopHiggs_HiggsCandidate_HiggsTag>0.9425)"
b2="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>-0.685&&BoostedTopHiggs_HiggsCandidate_HiggsTag>0.8132)"
b3="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>-0.875&&BoostedTopHiggs_HiggsCandidate_HiggsTag>0.2578)"
b1ex64="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>0.1650&&BoostedTopHiggs_HiggsCandidate_HiggsTag>0.9425&&(N_Jets<6||N_BTagsM<4))"
b2ex64="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>-0.685&&BoostedTopHiggs_HiggsCandidate_HiggsTag>0.8132&&(N_Jets<6||N_BTagsM<4))"
b3ex64="(BoostedTopHiggs_TopHadCandidate_TopMVAOutput>-0.875&&BoostedTopHiggs_HiggsCandidate_HiggsTag>0.2578&&(N_Jets<6||N_BTagsM<4))"
noboost="(0)"

bofchoice=b1ex64
suffix="b1ex64"
boostedweight='FinalBDT_BoostedJets_Cat_DB_WP1_Greed_6J4T_BDTG.weights.xml'
boosted_binning=(10,-0.9,0.9)

weights=['/afs/desy.de/user/h/hmildner/pyroot-plotscripts/code_generation/weights/weights_Final_43_V4.xml',
         '/afs/desy.de/user/h/hmildner/pyroot-plotscripts/code_generation/weights/weights_Final_44_V4.xml',
         '/afs/desy.de/user/h/hmildner/pyroot-plotscripts/code_generation/weights/weights_Final_53_V4.xml',
         '/afs/desy.de/user/h/hmildner/pyroot-plotscripts/code_generation/weights/weights_Final_54_V4.xml',
         '/afs/desy.de/user/h/hmildner/pyroot-plotscripts/code_generation/weights/weights_Final_62_V4.xml',
         '/afs/desy.de/user/h/hmildner/pyroot-plotscripts/code_generation/weights/weights_Final_63_V4.xml',
         '/afs/desy.de/user/h/hmildner/pyroot-plotscripts/code_generation/weights/weights_Final_64_V4.xml',
         '/afs/desy.de/user/h/hmildner/pyroot-plotscripts/code_generation/weights/'+boostedweight]

# category names (are hardcoded this way in limittool)
catnames=["j4_t3",
          "j4_t4",
          "j5_t3",
          "j5_tge4",
          "jge6_t2",
          "jge6_t3",
          "jge6_tge4",
          "boosted"]
# dont forget to declare integer variables below
lsel="(Evt_Odd==0&&N_TightLeptons==1&&N_LooseLeptons==1)"
boosted="("+bofchoice+"&&"+lsel+"&&(N_Jets>=4&&N_BTagsM>=2))"
s4j3t="("+lsel+"&&(N_Jets==4&&N_BTagsM==3)&&!"+boosted+")"
s4j4t="("+lsel+"&&(N_Jets==4&&N_BTagsM>=4)&&!"+boosted+")"
s5j3t="("+lsel+"&&(N_Jets==5&&N_BTagsM==3)&&!"+boosted+")"
s5j4t="("+lsel+"&&(N_Jets==5&&N_BTagsM>=4)&&!"+boosted+")"
s6j2t="("+lsel+"&&(N_Jets>=6&&N_BTagsM==2)&&!"+boosted+")"
s6j3t="("+lsel+"&&(N_Jets>=6&&N_BTagsM==3)&&!"+boosted+")"
s6j4t="("+lsel+"&&(N_Jets>=6&&N_BTagsM>=4)&&!"+boosted+")"
catselections=[s4j3t,s4j4t,s5j3t,s5j4t,s6j2t,s6j3t,s6j4t,boosted]

# all integer variables used
# remaining variables assumed to be float
# no arrays supported yet
intvars=['N_Jets','N_BTagsM','N_TightLeptons','N_LooseLeptons','Evt_Odd']

# binning of bdts -- should be optimzied

bdtbinning=[(20,-0.9,0.92),
            (10,-0.84,0.84),
            (20,-0.92,0.87),
            (10,-0.86,0.84),
            (20,-0.82,0.86),
            (20,-0.9,0.87),
            (10,-0.78,0.72),
            boosted_binning]

# names of systematics, including underscore (these are hardcoded in limit tool)
systnames=["",
           "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down"]

# names of systematics weights in tree
systweights=["20",
             "20*Weight_CSVLFup","20*Weight_CSVLFdown","20*Weight_CSVHFup","20*Weight_CSVHFdown",
             "20*Weight_CSVHFStats1up","20*Weight_CSVHFStats1down","20*Weight_CSVLFStats1up","20*Weight_CSVLFStats1down",
             "20*Weight_CSVHFStats2up","20*Weight_CSVHFStats2down","20*Weight_CSVLFStats2up","20*Weight_CSVLFStats2down",
             "20*Weight_CSVCErr1up","20*Weight_CSVCErr1down","20*Weight_CSVCErr2up","20*Weight_CSVCErr2down"]

# program to be run for data and jes samples
createScriptFromWeights("plot_nominal_"+suffix,weights,catnames,catselections,bdtbinning,[""],["20"],intvars )
compileScript("plot_nominal_"+suffix)
# program to be run to produce systematics defined by weights
createScriptFromWeights("plot_syst_"+suffix,weights,catnames,catselections,bdtbinning,systnames,systweights,intvars)
compileScript("plot_syst_"+suffix)
