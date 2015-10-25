from scriptgenerator import *

weights=['weights/weights_Final_43_V4.xml',
         'weights/weights_Final_44_V4.xml',
         'weights/weights_Final_53_V4.xml',
         'weights/weights_Final_54_V4.xml',
         'weights/weights_Final_62_V4.xml',
         'weights/weights_Final_63_V4.xml',
         'weights/weights_Final_64_V4.xml',]
catnames=["j4_t3",
          "j4_t4",
          "j5_t3",
          "j5_tge4",
          "jge6_t2",
          "jge6_t3",
          "jge6_tge4"]
catselections=["(N_Jets==4&&N_BTagsM==3)",
               "(N_Jets==4&&N_BTagsM>=4)",
               "(N_Jets==5&&N_BTagsM==3)",
               "(N_Jets==5&&N_BTagsM>=4)",
               "(N_Jets>=6&&N_BTagsM==2)",
               "(N_Jets>=6&&N_BTagsM==3)",
               "(N_Jets>=6&&N_BTagsM>=4)"]
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


createScriptFromWeights("plot_syst",weights,catnames,catselections,systnames,systweights)
createScriptFromWeights("plot_nominal",weights,catnames,catselections,[""],["1"])
