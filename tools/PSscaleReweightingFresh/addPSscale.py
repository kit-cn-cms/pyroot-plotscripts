import ROOT
import sys
from array import array 
import subprocess
ROOT.gROOT.SetBatch(True)

oldttbarfilename=sys.argv[1]
newttbarfilename=sys.argv[2]
systfilename=sys.argv[3]
outfilename=sys.argv[4]
suffix=sys.argv[5]

print oldttbarfilename, newttbarfilename, systfilename, outfilename, suffix
inf=ROOT.TFile(oldttbarfilename,"READ")
keylist=inf.GetListOfKeys()
for key in keylist:
  thisname=key.GetName()
  
  if not ("ttbarOther" in thisname or "ttbarPlusBBbar" in thisname or "ttbarPlusB" in thisname or "ttbarPlus2B" in thisname or "ttbarPlusCCbar" in thisname):
    continue
  if "CMS_" in thisname:
    continue
  print "doing ", thisname
  newsuff=suffix
  if "ttbarOther_" in thisname:
    newsuff=suffix.replace("PSscale","PSscale_ttbarOther")
  elif "ttbarPlusB_" in thisname:
    newsuff=suffix.replace("PSscale","PSscale_ttbarPlusB")
  elif "ttbarPlusBBbar_" in thisname:
    newsuff=suffix.replace("PSscale","PSscale_ttbarPlusBBbar")
  elif "ttbarPlus2B_" in thisname:
    newsuff=suffix.replace("PSscale","PSscale_ttbarPlus2B")
  elif "ttbarPlusCCbar_" in thisname:
    newsuff=suffix.replace("PSscale","PSscale_ttbarPlusCCbar")
  #print thisname, type(thisname)
  cmd="./main -i "+oldttbarfilename+" -i "+systfilename+" -i "+newttbarfilename+" -h "+thisname+" -h "+thisname+" -h "+thisname+" -o "+outfilename+" -H "+thisname+newsuff+" -v "
  print cmd
  subprocess.call(cmd,shell=True)
  
  
  
  