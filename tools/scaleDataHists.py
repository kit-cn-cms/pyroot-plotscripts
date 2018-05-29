#DISCLAIMER: was in limittools folder
import ROOT
import sys
ROOT.gDirectory.cd('PyROOT:/')



infname=sys.argv[1]
outfname=sys.argv[2]

infile=ROOT.TFile(infname,"READ")
outfile=ROOT.TFile(outfname,"RECREATE")

keylist=infile.GetListOfKeys()

for key in keylist:
  thisname=key.GetName()
  if "BDTbin" in thisname:
    continue
  thish=infile.Get(thisname)
  if "ljets_jge6_tge4" in thisname:
      if "ttH125" in thisname:
        thish.Scale(1.48)
      else:
        thish.Scale(1.57)
  outfile.cd()
  thish.Write()
  
outfile.Close()
infile.Close()
