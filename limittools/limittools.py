import ROOT
import sys
from subprocess import call

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

def MoveOverUnderflow(infname,outfname):

  infile=ROOT.TFile(infname,"READ")
  outfile=ROOT.TFile(outfname,"RECREATE")

  keylist=infile.GetListOfKeys()

  for key in keylist:
    thisname=key.GetName()
    thishisto=infile.Get(thisname)

    nBins=thishisto.GetNbinsX()
    errMaxBin=thishisto.GetBinError(nBins)
    errOFBin=thishisto.GetBinError(nBins+1)
    newerrorMaxBin=ROOT.TMath.Sqrt(errMaxBin*errMaxBin + errOFBin*errOFBin)
    thishisto.SetBinContent(nBins,thishisto.GetBinContent(nBins)+thishisto.GetBinContent(nBins+1))
    thishisto.SetBinError(nBins,newerrorMaxBin)
    thishisto.SetBinContent(nBins+1,0.0)

    errMinBin=thishisto.GetBinError(1)
    errUFBin=thishisto.GetBinError(0)
    newerrorMinBin=ROOT.TMath.Sqrt(errMinBin*errMinBin + errUFBin*errUFBin)
    thishisto.SetBinContent(1,thishisto.GetBinContent(1)+thishisto.GetBinContent(0))
    thishisto.SetBinError(1,newerrorMinBin)
    thishisto.SetBinContent(0,0.0)

    #write to outfile
    outfile.cd()
    thishisto.Write()

  outfile.Close()

def makeDatacards(filename,outname,categories=None):
  if categories==None:
    categories=["ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t2","ljets_jge6_t3","ljets_jge6_tge4"]
#  print 'mk_datacard_ttbb13TeV', '-d', 'BDT', '-c','"'+(' '.join(categories))+'"','-o', outname+'txt', filename
  call(['mk_datacard_ttbb13TeV', '-d', 'BDT', '-c',' '.join(categories),'-o', outname+'.txt', filename])
  for c in categories:
    call(['mk_datacard_ttbb13TeV', '-d', 'BDT', '-c', c, '-o', outname+'_'+c+'.txt', filename])

def readLimit(fn='higgsCombineTest.Asymptotic.mH125.root'):
  f=ROOT.TFile(fn)
  t=f.Get('limit')
  for e in t:
    if e.quantileExpected==0.5: 
      return e.limit
  f.Close()
    

def calcLimits(datacardname,categories=None):
  
  if categories==None:
    categories=["ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t2","ljets_jge6_t3","ljets_jge6_tge4"]
  call(['combine', '-M', 'Asymptotic', '-m', '125', '-t', '-1',datacardname+'.txt']) 
  limit_comb=readLimit('higgsCombineTest.Asymptotic.mH125.root')
  limit_cats=[]
  for c in categories:
    call(['combine', '-M', 'Asymptotic', '-m', '125', '-t', '-1',datacardname+'_'+c+'.txt']) 
    limit_cats.append(readLimit('higgsCombineTest.Asymptotic.mH125.root'))
  print 'combined:',limit_comb
  for c,l in zip(categories,limit_cats):
    print c,":",l
