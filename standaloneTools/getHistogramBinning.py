#DISCLAIMER: was in limittools folder
import ROOT
import sys
from array import array

infname=sys.argv[1]

infile=ROOT.TFile(infname,"READ")

samples=['ttH125','ttbarOther','ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B','singlet','wjets','zjets','ttbarZ','ttbarW','diboson']

categories=["j4_t3","j4_t4","j5_t3","j5_tge4","jge6_t2","jge6_t3","jge6_tge4"]
targetNbins=[20,10,20,10,20,20,10]

#categories=["jge6_tge4","j5_tge4","j4_t4"]

disc="BDT_ljets"

sysnames=["_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down","_CMS_scale_jUp","_CMS_scale_jDown","_CMS_res_jUp","_CMS_res_jDown"]


keylist=infile.GetListOfKeys()

for cat,targetbin in zip(categories,targetNbins):
  print "checking ", cat
  basehist=None
  for key in keylist:
    thisname=key.GetName()
    if cat not in thisname:
      continue
    if "BDTbin" in thisname or "data_obs" in thisname or "ttH125_BDT" in thisname:
      continue
    issyshist=False
    countsyst=0
    for sys in sysnames:
      if sys in thisname:
        countsyst+=1
    if countsyst>=1:
      continue
    #print thisname
    thish=infile.Get(thisname)
    #print thisname, thish.GetNbinsX(), thish.GetBinCenter(1), thish.GetBinCenter(thish.GetNbinsX()+1)
    if basehist==None:
      #print "base", thisname
      basehist=thish.Clone()
    else:
      #print "add", thisname
      basehist.Add(thish)

  ttbarSum=basehist.GetIntegral()
  lowerprob=float(1.0/targetbin/float(5.0))
  upperprob=1.0-float(1.0/targetbin/float(5.0))
  
  probs=array("d",[lowerprob,upperprob])
  quants=array("d",[0.0,0.0])
  basehist.GetQuantiles(2,quants,probs)
  print quants



#    for ibin in range(basehist.GetNbinsX()):
#      print ibin, basehist.GetBinCenter(ibin+1), basehist.GetBinContent(ibin+1)
#      if basehist.GetBinContent(ibin+1)<0:
#        print thisname, ibin+1, basehist.GetBinContent(ibin+1)
#        exit(0)#
#
#  nbins=basehist.GetNbinsX()
#  minBin=0
#  maxBin=2000
#  
#  for ibin in range(nbins):
#    #print ibin, basehist.GetBinCenter(ibin+1), basehist.GetBinContent(ibin+1)
#    if basehist.GetBinContent(ibin+1)>0:
#      minBin=ibin+1
#      break
#  for ibin in reversed(range(nbins)):
#    if basehist.GetBinContent(ibin+1)>0:
#      maxBin=ibin+1
#      break
#  minval=basehist.GetBinLowEdge(minBin)
#  maxval=basehist.GetBinLowEdge(maxBin)+basehist.GetBinWidth(maxBin)
#  print cat, minBin, maxBin, minval, maxval






print "all done"
