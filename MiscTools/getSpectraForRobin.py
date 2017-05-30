import ROOT
import sys
ROOT.gDirectory.cd('PyROOT:/')

infile=sys.argv[1]

inf=ROOT.TFile(infile,"READ")

pTbinnings=[
["20to30","30to40","40to60","60to100","100to1000"],
["20to30","30to50","50to70","70to100","100to1000"],
]

samples=["ttbar","ttH"]
flavors=["lf","c","b"]
flavornumbers=[0,4,5]

for s in samples:
  print "-------------------"
  for flav, flavnum in zip(flavors,flavornumbers):
    for pTbin in pTbinnings:
      print "sample ", s
      print "flavor ", flav
      print "binning 1 ", pTbin
      print "bin  yield  ratio"
      yields=[]
      ratios=[]
      for b in pTbin:
	h=inf.Get(s+"_"+"JetFlavPt"+b)
	num=h.GetBinContent(h.FindBin(flavnum))
	yields.append(num)
      total=0
      for y in yields:
	total+=y
      for y in yields:
	ratios.append(y/float(total))
      for b, y ,r in zip(pTbin,yields, ratios):
	print b, round(y,2), round(r,2)
      sor=0
      for r in ratios:
	sor+=r
      print ""