import subprocess 
import sys

inprefix=sys.argv[1]

inputCards={
"datacard_ljets_j4_t2_hdecay.txt" : [],
"datacard_ljets_j4_t3_BLR_hdecay.txt" : [],
"datacard_ljets_j4_t3_hdecay.txt" : ["SL_2DBDTMEM_645444635343","SL_2DBDTMEM_64544463534362","SL_BDTonly_645444635343","SL_BDTonly_64544463534362","combined_BDTonly","combined_2D"],
"datacard_ljets_j4_t4_hdecay.txt" : ["SL_BDTonly_645444635343","SL_BDTonly_64544463534362","combined_BDTonly"],
"datacard_ljets_j4_t4_high_hdecay.txt" : ["SL_2DBDTMEM_645444635343","SL_2DBDTMEM_64544463534362","combined_2D"],
"datacard_ljets_j4_t4_low_hdecay.txt" : ["SL_2DBDTMEM_645444635343","SL_2DBDTMEM_64544463534362","combined_2D"],
"datacard_ljets_j4_t4_MEMONLY_hdecay.txt" : [],
"datacard_ljets_j4_t4_ttbbOpt_hdecay.txt" : [],
"datacard_ljets_j4_t4_ttbbOpt_high_hdecay.txt" : [],
"datacard_ljets_j4_t4_ttbbOpt_low_hdecay.txt" : [],
"datacard_ljets_j4_tge3_tt2bnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"],
"datacard_ljets_j4_tge3_ttbbnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"],
"datacard_ljets_j4_tge3_ttbnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"],
"datacard_ljets_j4_tge3_ttccnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"],
"datacard_ljets_j4_tge3_ttHnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"],
"datacard_ljets_j4_tge3_ttlfnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_j5_t2_hdecay.txt" : [],
"datacard_ljets_j5_t3_BLR_hdecay.txt" : [],
"datacard_ljets_j5_t3_hdecay.txt" : ["SL_2DBDTMEM_645444635343","SL_2DBDTMEM_64544463534362","SL_BDTonly_645444635343","SL_BDTonly_64544463534362","combined_BDTonly","combined_2D"],
"datacard_ljets_j5_tge3_tt2bnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_j5_tge3_ttbbnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_j5_tge3_ttbnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_j5_tge3_ttccnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_j5_tge3_ttHnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_j5_tge3_ttlfnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_j5_tge4_hdecay.txt" : ["SL_BDTonly_645444635343","SL_BDTonly_64544463534362","combined_BDTonly"],
"datacard_ljets_j5_tge4_high_hdecay.txt" : ["SL_2DBDTMEM_645444635343","SL_2DBDTMEM_64544463534362","combined_2D"],
"datacard_ljets_j5_tge4_low_hdecay.txt" : ["SL_2DBDTMEM_645444635343","SL_2DBDTMEM_64544463534362","combined_2D"],
"datacard_ljets_j5_tge4_MEMONLY_hdecay.txt" : [],
"datacard_ljets_j5_tge4_ttbbOpt_hdecay.txt" : [],
"datacard_ljets_j5_tge4_ttbbOpt_high_hdecay.txt" : [],
"datacard_ljets_j5_tge4_ttbbOpt_low_hdecay.txt" : [],
"datacard_ljets_jge6_t2_BLR_hdecay.txt" : [],
"datacard_ljets_jge6_t2_hdecay.txt" : ["SL_2DBDTMEM_64544463534362","SL_BDTonly_64544463534362","SL_DNN_64544463534362","combined_BDTonly","combined_2D"],
"datacard_ljets_jge6_t3_BLR_hdecay.txt" : [],
"datacard_ljets_jge6_t3_hdecay.txt" : ["SL_BDTonly_645444635343","SL_BDTonly_64544463534362","combined_BDTonly"],
"datacard_ljets_jge6_t3_high_hdecay.txt" : ["SL_2DBDTMEM_645444635343","SL_2DBDTMEM_64544463534362","combined_2D"],
"datacard_ljets_jge6_t3_low_hdecay.txt" : ["SL_2DBDTMEM_645444635343","SL_2DBDTMEM_64544463534362","combined_2D"],
"datacard_ljets_jge6_t3_MEMONLY_hdecay.txt" : [],
"datacard_ljets_jge6_t3_ttbbOpt_hdecay.txt" : [],
"datacard_ljets_jge6_t3_ttbbOpt_high_hdecay.txt" : [],
"datacard_ljets_jge6_t3_ttbbOpt_low_hdecay.txt" : [],
"datacard_ljets_jge6_tge3_tt2bnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_jge6_tge3_ttbbnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_jge6_tge3_ttbnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_jge6_tge3_ttccnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_jge6_tge3_ttHnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_jge6_tge3_ttlfnode_hdecay.txt" : ["SL_DNN_645444635343","SL_DNN_64544463534362"] ,
"datacard_ljets_jge6_tge4_hdecay.txt" : ["SL_BDTonly_645444635343","SL_BDTonly_64544463534362","combined_BDTonly"],
"datacard_ljets_jge6_tge4_high_hdecay.txt" : ["SL_2DBDTMEM_645444635343","SL_2DBDTMEM_64544463534362","combined_2D"],
"datacard_ljets_jge6_tge4_low_hdecay.txt" : ["SL_2DBDTMEM_645444635343","SL_2DBDTMEM_64544463534362","combined_2D"],
"datacard_ljets_jge6_tge4_MEMONLY_hdecay.txt" : [],
"datacard_ljets_jge6_tge4_ttbbOpt_hdecay.txt" : [],
"datacard_ljets_jge6_tge4_ttbbOpt_high_hdecay.txt" : [],
"datacard_ljets_jge6_tge4_ttbbOpt_low_hdecay.txt" : [],
"ttH_hbb_13TeV_dl_3j3t.txt" : ["DL_BDTonly","DL_2D","combined_2D","combined_BDTonly"],
"ttH_hbb_13TeV_dl_ge4j3t_both.txt" : ["DL_BDTonly","combined_BDTonly"],
"ttH_hbb_13TeV_dl_ge4j3t_high.txt" : ["DL_2D","combined_2D"],
"ttH_hbb_13TeV_dl_ge4j3t_low.txt" : ["DL_2D","combined_2D"],
"ttH_hbb_13TeV_dl_ge4jge4t_both.txt" : ["DL_BDTonly","combined_BDTonly"],
"ttH_hbb_13TeV_dl_ge4jge4t_high.txt" : ["DL_2D","combined_2D"],
"ttH_hbb_13TeV_dl_ge4jge4t_low.txt" : ["DL_2D","combined_2D"],
}

# figure out stuff

outcards={}
for incard in inputCards:
  for combCard in inputCards[incard]:
    if combCard in outcards:
      outcards[combCard].append(inprefix+incard)
    else:
      outcards[combCard]=[inprefix+incard]

for combination in outcards:
  print "----------------------------------"
  print "creating ", combination
  print "with "
  for incard in outcards[combination]:
    print incard
  cmd="combineCards.py "+" ".join(outcards[combination])+" > "+combination+".txt"
  print cmd
  subprocess.call(cmd, shell=True)