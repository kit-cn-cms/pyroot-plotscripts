import ROOT
import sys
from array import array 

infname=sys.argv[1]

cats=["ljets_j4_t2","ljets_j5_t2","ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t2","ljets_jge6_t3","ljets_jge6_tge4",]
bprocs=["ttH",]#"ttbarPlusCCbar","ttbarPlusB","ttbarPlus2B","ttbarPlusBBbar",]

inf=ROOT.TFile(infname,"READ")

results=[]
for c in cats:
  print "doin ", c
  bkgs=[]
  for b in bprocs:
    bkgs.append(inf.Get(b+"_finaldiscr_"+c))
    print bkgs[-1]
  stack=bkgs[0].Clone()
  #for b in bkgs[1:]:
    #stack.Add(b)
  probs=array("d",[0.5])
  quants=array("d",[0.0])
  stack.GetQuantiles(1,quants,probs)
  print probs
  print quants
  results.append([c,quants])
  
for r in results:
  print r
  