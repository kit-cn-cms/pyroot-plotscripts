import ROOT
import sys

def renameHistos(infname,outfname,sysnames):
  infile=ROOT.TFile(infname,"READ")
  outfile=ROOT.TFile(outfname,"RECREATE")

  keylist=infile.GetListOfKeys()
  
  for key in keylist:
    thisname=key.GetName()
    thish=infile.Get(thisname)
    newname=thisname
    for sys in sysnames:
      if sys in newname:
        newname=newname.replace(sys,"")
        newname+=sys
  #if "125" in newname:
    #newname=newname.replace("125","")
    print "changed ", thisname, " to ", newname
    thish.SetName(newname)
    outfile.cd()
    thish.Write()
  
  outfile.Close()
  infile.Close()

def addPseudoData(infname,samplesWOttH,categories,sysnames,disc="BDT_ljets"):

  infile=ROOT.TFile(infname,"UPDATE")

  for cat in categories:
    print "getting ", samplesWOttH[0]+"_"+disc+"_"+cat
    oldhist=infile.Get(samplesWOttH[0]+"_"+disc+"_"+cat)
    newhist=oldhist.Clone("data_obs_"+disc+"_"+cat)
    print newhist
    for s in samplesWOttH[1:]:
      print "doiung ", s+"_"+disc+"_"+cat
      bufferhist=infile.Get(s+"_"+disc+"_"+cat)
      print bufferhist
      newhist.Add(bufferhist)
    newhist.Write()
  
  infile.Close()
