import ROOT
import sys

infname=sys.argv[1]

infile=ROOT.TFile(infname,"READ")

samples=['ttH125','ttbarOther','ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B','singlet','wjets','zjets','ttbarZ','ttbarW','diboson']

#categories=["j4_t3","j4_t4","j5_t3","j5_tge4","jge6_t2","jge6_t3","jge6_tge4"]
categories=["jge6_tge4"]

disc="BDT_ljets"

sysnames=["_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down","_CMS_scale_jUp","_CMS_scale_jDown","_CMS_res_jUp","_CMS_res_jDown"]


keylist=infile.GetListOfKeys()

for cat in categories:
  print "checking ", cat
  basehist=None
  for key in keylist:
    thisname=key.GetName()
    if cat not in thisname:
      continue
    thish=infile.Get(thisname)
    if basehist==None:
      basehist=thish.Clone()
    else:
      basehist.Add(thish)
  nbins=basehist.GetNbinsX()
  minBin=0
  maxBin=999
  for ibin in range(nbins):
    if basehist.GetBinContent(ibin+1)>0:
      minBin=ibin+1
      break
  for ibin in reversed(range(nbins)):
    if basehist.GetBinContent(ibin+1)>0:
      maxBin=ibin+1
      break
  minval=basehist.GetBinLowEdge(minBin)
  maxval=basehist.GetBinLowEdge(maxBin)+basehist.GetBinWidth(maxBin)
  print cat, minval, maxval
