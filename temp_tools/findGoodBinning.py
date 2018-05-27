#OPEN: what does this script do?
import ROOT
import sys
from array import array
ROOT.gROOT.SetBatch(True)
ROOT.gDirectory.cd('PyROOT:/')

inRootFileName=sys.argv[1]
inRootFile=ROOT.TFile(inRootFileName,"READ")

targetEvents=3.0
categories=["j4t3","j4t4","j5t3","j5t4","j6t2","j6t3","j6t4","boosted"]
processes=["ttbarOther","ttbarPlusCCbar","ttbarPlusBBbar","ttbarPlusB","ttbarPlus2B","singlet","zjets","wjets","ttbarW","ttbarZ","diboson","QCD"]
discName="finaldiscr"

for cat in categories:
  print ""
  print "Doing category ", cat
  listOfHistos=[]
  for proc in processes:
    
    h=inRootFile.Get(proc+"_"+discName+"_"+cat)
    if h!=None:
      listOfHistos.append(h.Clone())
    else:
      print "Did not find ", proc+"_"+discName+"_"+cat
  hstack=listOfHistos[0].Clone()
  for b in listOfHistos[1:]:
    hstack.Add(b)
  print hstack.Integral() , " events after stacking"
  integral=hstack.Integral()
  targetprob=targetEvents/float(integral)
  print " fraction of 2.0 events", targetprob
  lowerprob=targetprob
  upperprob=1.0-targetprob
  
  probs=array("d",[lowerprob,upperprob])
  probs=array("d",[lowerprob,upperprob])
  quants=array("d",[0.0,0.0])
  hstack.GetQuantiles(2,quants,probs)
  print probs
  print quants
  lowerquant=quants[0]
  upperquant=quants[1]
  #bla=0
  #for ibin in range(448,500,1):
    #print ibin, hstack.GetBinCenter(ibin), hstack.GetBinContent(ibin)
    #bla+=hstack.GetBinContent(ibin)
  #print bla
  
  # get highest and lowest filled bins
  nbins=hstack.GetNbinsX()
  highestBin=nbins
  lowestBin=0
  for ib in range(nbins):
    bc=hstack.GetBinContent(ib+1)
    if bc>0:
      lowestBin=ib+1
      break
  for ib in reversed(range(nbins)):
    bc=hstack.GetBinContent(ib+1)
    if bc>0:
      highestBin=ib+1
      break
  print "lowest highest bin", lowestBin, highestBin
  lowestValue=hstack.GetBinLowEdge(lowestBin)
  highestValue=hstack.GetBinLowEdge(highestBin)+hstack.GetBinWidth(highestBin)
  print "lowest highest value", lowestValue, highestValue
  valueRange=highestValue-lowestValue
  print "range ", valueRange
  lowertargetBinWidth=(lowerquant-lowestValue)/valueRange  
  uppertargetBinWidth=(highestValue-upperquant)/valueRange  
  print "lower upper binwidth", lowertargetBinWidth, uppertargetBinWidth
  targetbinwidth=max(lowertargetBinWidth,uppertargetBinWidth)
  targetNbinsFloat=valueRange/targetbinwidth
  print targetNbinsFloat
  targetNbins=int(targetNbinsFloat)
  #print "target n bins", targetNbins
  print "Binning ", lowestValue, highestValue, targetNbins
  print "Binning ", lowestValue, highestValue, min(targetNbins,20)
  
  
  
  # now crosscheck
  lowercheckbin=hstack.FindBin(lowestValue+targetbinwidth)
  uppercheckbin=hstack.FindBin(highestValue-targetbinwidth)
  print lowestBin, lowercheckbin, uppercheckbin, highestBin
  print hstack.Integral(lowestBin-1, lowercheckbin+1), hstack.Integral(uppercheckbin-1, highestBin+1)
  
  
  #exit(0)








