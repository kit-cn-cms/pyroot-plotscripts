#OPEN what does this script do?
import ROOT
import sys
import os
from subprocess import call

filename=os.getenv("OUTFILENAME")


def renameHistosOLD(infname,outfname,sysnames,prune=False):
  cmd="cp -v "+infname+" "+"original_"+infname
  call(cmd,shell=True)
  print sysnames
  infile=ROOT.TFile(infname,"READ")
  outfile=ROOT.TFile(outfname,"RECREATE")

  keylist=infile.GetListOfKeys()
  for key in keylist:
    thisname=key.GetName()
    thish=infile.Get(thisname)
    newname=thisname
    do=True
    if do and "PSscaleUp" in thisname and "Q2scale" in thisname and thisname[-2:]=="Up":
      tmp=thisname
      tmp=tmp.replace('_CMS_ttH_PSscaleUp','')
      print 'stripped',tmp
      newname=tmp.replace('Q2scale','CombinedScale')

    if "PSscaleDown" in thisname and "Q2scale" in thisname and thisname[-4:]=="Down":
      tmp=thisname
      tmp=tmp.replace('_CMS_ttH_PSscaleDown','')
      newname=tmp.replace('Q2scale','CombinedScale')

    if "dummy" in thisname:
      continue
    nsysts=0
    for sys in sysnames:
      if sys in newname:
        newname=newname.replace(sys,"")
        newname+=sys
        nsysts+=1
        
    if nsysts>2:
      print "skipping", thisname
      continue
    
    #filter histograms for systs not belonging to the samples 
    #for now until we have NNPDF syst for other samples
    if prune:
      if "CMS_ttH_NNPDF" in thisname:
        if thisname.split("_",1)[0]+"_" not in ["ttbarPlus2B_","ttbarPlusB_","ttbarPlusBBbar_","ttbarPlusCCbar_","ttbarOther_"]:
          print "wrong syst: removing histogram", thisname
          continue
      if "CMS_ttH_Q2scale_ttbarOther" in thisname and "ttbarOther"!=thisname.split("_",1)[0]:
        print "wrong syst: removing histogram", thisname
        continue
      if ("CMS_ttH_Q2scale_ttbarPlusBUp" in thisname or "CMS_ttH_Q2scale_ttbarPlusBDown" in thisname ) and "ttbarPlusB"!=thisname.split("_",1)[0] :
        print "wrong syst: removing histogram", thisname
        continue
      if "CMS_ttH_Q2scale_ttbarPlusBBbar" in thisname and "ttbarPlusBBbar"!=thisname.split("_",1)[0] :
        print "wrong syst: removing histogram", thisname
        continue
      if "CMS_ttH_Q2scale_ttbarPlusCCbar" in thisname and "ttbarPlusCCbar"!=thisname.split("_",1)[0] :
        print "wrong syst: removing histogram", thisname
        continue
      if "CMS_ttH_Q2scale_ttbarPlus2B" in thisname and "ttbarPlus2B"!=thisname.split("_",1)[0] :
        print "wrong syst: removing histogram", thisname
        continue
    
#add ttbar type to systematics name for PS scale
    if "CMS_ttH_PSscaleUp" in newname or "CMS_ttH_PSscaleDown" in newname:
      
      ttbartype=""
      if "ttbarOther"==thisname.split("_",1)[0]:
        ttbartype="ttbarOther"
      elif "ttbarPlusB"==thisname.split("_",1)[0] :
        ttbartype="ttbarPlusB"
      elif "ttbarPlusBBbar"==thisname.split("_",1)[0] :
        ttbartype="ttbarPlusBBbar"
      elif "ttbarPlusCCbar"==thisname.split("_",1)[0] :
        ttbartype="ttbarPlusCCbar"
      elif "ttbarPlus2B"==thisname.split("_",1)[0] :
        ttbartype="ttbarPlus2B"
      else:
        print "wrong syst: removing histogram", thisname
        continue
      
      if "CMS_ttH_PSscaleUp" in newname:
        newname=newname.replace("CMS_ttH_PSscaleUp","CMS_ttH_PSscale_"+ttbartype+"Up")
      elif "CMS_ttH_PSscaleDown" in newname:
        newname=newname.replace("CMS_ttH_PSscaleDown","CMS_ttH_PSscale_"+ttbartype+"Down")
      else:
        print "wrong syst: removing histogram", thisname

    if newname!=thisname:
      print "changed ", thisname, " to ", newname  
      thish.SetName(newname)
      #outfile.cd()
      thish.Write()
      outfile.Delete(thisname+";1")
  
  outfile.Close()
  infile.Close()    
