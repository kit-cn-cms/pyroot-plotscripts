import ROOT
import sys
ROOT.gDirectory.cd('PyROOT:/')



infname1=sys.argv[1]
infname2=sys.argv[2]
outfname=sys.argv[3]

infile1=ROOT.TFile(infname1,"READ")
infile2=ROOT.TFile(infname2,"READ")
outfile=ROOT.TFile(outfname,"RECREATE")

categoriesToTakeFrom2=["jge6_tge4"]

keylist=infile1.GetListOfKeys()

for key in keylist:
  thisname=key.GetName()
  takeit=False
  for cat in categoriesToTakeFrom2:
    if cat in thisname:
      takeit=True
  if takeit:      
    thish=infile2.Get(thisname)
  else:
    thish=infile1.Get(thisname)
  outfile.cd()
  thish.Write()
  
outfile.Close()
infile1.Close()
infile2.Close()
