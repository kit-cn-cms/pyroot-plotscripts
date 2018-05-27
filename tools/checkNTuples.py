# This script checks the ntuples in the given directory for their health and deletes them if you wish that

import sys
import os
import glob
import ROOT
import subprocess
import xml.etree.ElementTree as ET

removeRecovered=False
deleteTheNTuples=False

def checkROOTFiles(path="",removeRecovered=False):
  isGOOD=True
  rf=ROOT.TFile.Open(path)
  if rf==None or len(rf.GetListOfKeys())==0 or rf.TestBit(ROOT.TFile.kZombie):
    isGOOD=False
    print "BROKEN    ", path
  elif removeRecovered and rf.TestBit(ROOT.TFile.kRecovered):
    isGOOD=False
    print "BROKEN    ", path
  else:
    tree=rf.Get("MVATree")
    if tree==None:
      isGOOD=False
      print "BROKEN    ", path
    else:  
      nevents=tree.GetEntries()
      rf.Close()
      if nevents<=0:
	isGOOD=False
	print "BROKEN    ", path
  if rf!=None:
    rf.Close()
  return isGOOD


#prefix=sys.argv[1
arguments=sys.argv[1:]
if len(arguments)==0 or "-h" in arguments or not "-d" in arguments:
  print "usage"
  print "python getScriptToRerun.py [--removeRecovered] [--delete] -d LOGPATH [-v VETOLIST]"
  print "--removeRecovered: Also flag those jobs as problematic of the keys of the root files could be recovered"
  print "--delete: Actually delete the root files that belong to the problematic jobs"
  print "-d LOGPATH: Path to log files to be analyzed"
  print "-v VETOLIST: these log files are ignored. Use a space separated list here. e.g. -v file1,file2,file3"

indir=""
vetolist=[]
for iarg,arg in enumerate(arguments):
  if "--removeRecovered"==arg:
    removeRecovered=True
  if "--delete"==arg:
    deleteTheNTuples=True
  if "-d"==arg:
    indir=arguments[iarg+1]

infiles=glob.glob(indir+"/*.root")
ntuplesToDelete=[]

for fi in infiles:
  print "checking ", fi
  thisFileIsGoodFile=True
  thisFileIsGoodFile=checkROOTFiles(fi,removeRecovered)
  if not thisFileIsGoodFile:
    print "PROBLEM WITH FILE ", fi
  if deleteTheNTuples and not thisFileIsGoodFile:
    if os.path.exists(fi):
      print "deleting ", fi
      ntuplesToDelete.append(fi)
      os.remove(fi) 

print ""
print "Deleted the following files"
for ntuple in ntuplesToDelete:
  print ntuple
