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
  
  nbins=thish.GetNbinsX()
  thish.SetBinContent(1, thish.GetBinContent(1)+thish.GetBinContent(0))
  thish.SetBinContent(0, 0.0)

  thish.SetBinContent(nbins, thish.GetBinContent(nbins)+thish.GetBinContent(nbins+1))
  thish.SetBinContent(nbins+1, 0.0)

  outfile.cd()
  thish.Write()
  
outfile.Close()
infile.Close()
