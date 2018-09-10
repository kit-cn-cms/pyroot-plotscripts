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
  thish=infile.Get(thisname)
  if "BDTbin" not in thisname:
    outfile.cd()
    thish.Write()
  
outfile.Close()
infile.Close()


