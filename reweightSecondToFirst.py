import sys
import ROOT
ROOT.gDirectory.cd('PyROOT:/')
ROOT.gROOT.SetBatch(True)

infBDTname=sys.argv[1]
infMEMname=sys.argv[2]
outname=sys.argv[3]

infBDT=ROOT.TFile(infBDTname,"READ")
infMEM=ROOT.TFile(infMEMname,"READ")
outf=ROOT.TFile(outname,"CREATE")

keylist=infBDT.GetListOfKeys()
ih=0
for key in keylist:
  thisname=key.GetName()
  #print thisname
  if "BDTbin" in thisname:
    continue
  
  bdtH=infBDT.Get(thisname)
  memH=infMEM.Get(thisname)
  if bdtH==None or memH==None:
    print "ERROR DID NOT FIND ",thisname
    continue
  newH=memH.Clone()
  intBDT=bdtH.Integral()
  intMEM=memH.Integral()
  #print bdtH.Integral(), memH.Integral(), newH.Integral() 
  if not intMEM>0 :
    print "EMPTY MEM histO??", thisname
  elif "data" in thisname or "SingleMu" in thisname or "SingleEl" in thisname :
    #print "SKIPPING REAL DATA", thisname
    aaaa=2
  elif "_" in thisname:
    if "ttH"==thisname.split("_")[0]:
      print "skippng ttH"
      #aaa=2
    else:
      newH.Scale(intBDT/float(intMEM))
      print "scaled"
  if intMEM==intBDT:
    a=1
    #print thisname, " BDT", intBDT, " MEM ", intMEM , " -> SAME"
  else:
    if intMEM>0:
      print thisname, " BDT", intBDT, " MEM ", intMEM , " -> ", intBDT/float(intMEM) ,newH.Integral()
    else:
      print thisname, " BDT", intBDT, " MEM ", intMEM , " -> ", 0 ,newH.Integral()
  if newH.Integral()!=bdtH.Integral():
    print "PROBLEM PROBLEM ", newH.Integral(), bdtH.Integral()
  #print bdtH.Integral(), memH.Integral(), newH.Integral() 
  outf.cd()
  newH.Write()
  ih+=1
  #if ih>10:
    #break
print "done"
outf.Close()
print "really done"