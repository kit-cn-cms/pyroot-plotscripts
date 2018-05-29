#DISCLAIMER was in limittools folder
import ROOT
import sys
ROOT.gDirectory.cd('PyROOT:/')



infname1=sys.argv[1]
infname2=sys.argv[2]
outfname=sys.argv[3]

infile1=ROOT.TFile(infname1,"READ")
infile2=ROOT.TFile(infname2,"READ")
outfile=ROOT.TFile(outfname,"RECREATE")

#categoriesToTakeFrom2=["jge6_tge4"]

keylist1=infile1.GetListOfKeys()
keylist2=infile2.GetListOfKeys()
listofnames=[]

for key in keylist1:
  thisname=key.GetName()
  listofnames.append(thisname)
  thish=infile1.Get(thisname)
  outfile.cd()
  thish.Write()
for key in keylist2:
  thisname=key.GetName()
  if thisname in listofnames:
    continue
  thish=infile2.Get(thisname)
  outfile.cd()
  thish.Write()

outfile.Close()
infile1.Close()
infile2.Close()
