import ROOT
import sys
ROOT.gDirectory.cd('PyROOT:/')



infname=sys.argv[1]
outfname=sys.argv[2]

infile=ROOT.TFile(infname,"READ")
outfile=ROOT.TFile(outfname,"RECREATE")


samplesWOttH=['ttbarOther','ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B','singlet','wjets','zjets','ttZ','ttW','diboson']

categories=["j4_t3","j4_t4","j5_t3","j5_tge4","jge6_t2","jge6_t3","jge6_tge4"]

disc="BDT_ljets"

sysnames=["_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down","_CMS_scale_jUp","_CMS_scale_jDown","_CMS_res_jUp","_CMS_res_jDown"]

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


