from scriptgenerator import *

weights=['weights/weights_Final_43_V4.xml',
         'weights/weights_Final_44_V4.xml',
         'weights/weights_Final_53_V4.xml',
         'weights/weights_Final_54_V4.xml',
         'weights/weights_Final_62_V4.xml',
         'weights/weights_Final_63_V4.xml',
         'weights/weights_Final_64_V4.xml',]
# category names (are hardcoded this way in limittool)
catnames=["j4_t3",
          "j4_t4",
          "j5_t3",
          "j5_tge4",
          "jge6_t2",
          "jge6_t3",
          "jge6_tge4"]
# dont forget to declare integer variables below
catselections=["(N_Jets==4&&N_BTagsM==3)",
               "(N_Jets==4&&N_BTagsM>=4)",
               "(N_Jets==5&&N_BTagsM==3)",
               "(N_Jets==5&&N_BTagsM>=4)",
               "(N_Jets>=6&&N_BTagsM==2)",
               "(N_Jets>=6&&N_BTagsM==3)",
               "(N_Jets>=6&&N_BTagsM>=4)"]

# all integer variables used
# remaining variables assumed to be float
# no arrays supported yet
intvars=['N_Jets','N_BTagsM']

# binning of bdts -- should be optimzied
bdtbinning=[(20,-1,1),
            (10,-1,1),
            (20,-1,1),
            (10,-1,1),
            (20,-1,1),
            (20,-1,1),
            (10,-1,1)]

# names of systematics, including underscore (these are hardcoded in limit tool)
systnames=["",
           "_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down"]

# names of systematics weights in tree
systweights=["1",
             "Weight_CSVLFup","Weight_CSVLFdown","Weight_CSVHFup","Weight_CSVHFdown",
             "Weight_CSVHFStats1up","Weight_CSVHFStats1down","Weight_CSVLFStats1up","Weight_CSVLFStats1down",
             "Weight_CSVHFStats2up","Weight_CSVHFStats2down","Weight_CSVLFStats2up","Weight_CSVLFStats2down",
             "Weight_CSVCErr1up","Weight_CSVCErr1down","Weight_CSVCErr2up","Weight_CSVCErr2down"]

# program to be run for data and jes samples
createScriptFromWeights("plot_nominal",weights,catnames,catselections,bdtbinning,[""],["1"],intvars )
compileScript("plot_nominal")
# program to be run to produce systematics defined by weights
createScriptFromWeights("plot_syst",weights,catnames,catselections,bdtbinning,systnames,systweights,intvars)
compileScript("plot_syst")
