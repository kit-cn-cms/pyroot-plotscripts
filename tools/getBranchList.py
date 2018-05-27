#OPEN what does this script do?
import ROOT
import sys

infn=sys.argv[1]

inf=ROOT.TFile(infn,"READ")
t=inf.Get("MVATree")

outf=open("../txtfiles/branchlist.txt","w")
brl=t.GetListOfBranches()
for br in brl:
  name=br.GetName()
  outf.write(name+"\n")

outf.close()
