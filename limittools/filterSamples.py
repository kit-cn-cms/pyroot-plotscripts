import ROOT
import sys
ROOT.gDirectory.cd('PyROOT:/')



infname=sys.argv[1]
outfname=sys.argv[2]

infile=ROOT.TFile(infname,"READ")
outfile=ROOT.TFile(outfname,"RECREATE")

samples=['data_obs','ttH125','ttbarOther','ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B','singlet','wjets','ttbarZ','diboson']

keylist=infile.GetListOfKeys()

for key in keylist:
  thisname=key.GetName()
  thish=infile.Get(thisname)
  keepHisto=False
  for s in samples:
    if s in thisname:
      keepHisto=True
  if keepHisto:
    outfile.cd()
    thish.Write()
  
outfile.Close()
infile.Close()
