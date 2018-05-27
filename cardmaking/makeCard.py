
import ROOT
import subprocess
import sys
from glob import glob
from array import array
ROOT.gROOT.SetBatch(True)
ROOT.gDirectory.cd('PyROOT:/')


outname=sys.argv[1]
mode=sys.argv[2]

print "making card"
outcardfile=open(outname,"w")

if mode=="comb":
  catlist=["sl_j4t2=slBDTonly_datacard_ljets_j4_t2.txt","sl_j5t2=slBDTonly_datacard_ljets_j5_t2.txt","sl_j4t3=slBDTonly_datacard_ljets_j4_t3.txt","sl_j4t4=slBDTonly_datacard_ljets_j4_t4.txt","sl_j5t3=slBDTonly_datacard_ljets_j5_t3.txt","sl_j5t4=slBDTonly_datacard_ljets_j5_t4.txt","sl_j6t2=slBDTonly_datacard_ljets_j6_t2.txt","sl_j6t3=slBDTonly_datacard_ljets_j6_t3.txt","sl_j6get4=slBDTonly_datacard_ljets_j6_t4.txt","dl_j3t2=ttH_hbb_13TeV_dl_3j2t.txt","dl_j3t3=ttH_hbb_13TeV_dl_3j3t.txt","dl_gej4t2=ttH_hbb_13TeV_dl_ge4j2t.txt","dl_gej4t3=ttH_hbb_13TeV_dl_ge4j3t.txt","dl_gej4get4=ttH_hbb_13TeV_dl_ge4jge4t.txt"]
elif mode=="sl":
  catlist=["sl_j4t2=slBDTonly_datacard_ljets_j4_t2.txt","sl_j5t2=slBDTonly_datacard_ljets_j5_t2.txt","sl_j4t3=slBDTonly_datacard_ljets_j4_t3.txt","sl_j4t4=slBDTonly_datacard_ljets_j4_t4.txt","sl_j5t3=slBDTonly_datacard_ljets_j5_t3.txt","sl_j5t4=slBDTonly_datacard_ljets_j5_t4.txt","sl_j6t2=slBDTonly_datacard_ljets_j6_t2.txt","sl_j6t3=slBDTonly_datacard_ljets_j6_t3.txt","sl_j6get4=slBDTonly_datacard_ljets_j6_t4.txt",]
elif mode=="dl":
  catlist=["dl_j3t2=ttH_hbb_13TeV_dl_3j2t.txt","dl_j3t3=ttH_hbb_13TeV_dl_3j3t.txt","dl_gej4t2=ttH_hbb_13TeV_dl_ge4j2t.txt","dl_gej4t3=ttH_hbb_13TeV_dl_ge4j3t.txt","dl_gej4get4=ttH_hbb_13TeV_dl_ge4jge4t.txt"]
else:
  print "unknown mode"
  exit(0)

subprocess.call(["combineCards.py"]+catlist,stdout=outcardfile)

outcardfile.close()
  











