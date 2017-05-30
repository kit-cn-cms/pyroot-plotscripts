import ROOT
import sys
from limittools import addPseudoData  

infname=sys.argv[1]

#samplesWOttH=['ttbarOther','ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B','singlet','wjets','zjets','ttbarZ','ttbarW','diboson']
samplesWOttH=['ttbarOther','ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B']

categories=["j4_t2","j5_t2","j4_t3","j4_t4","j5_t3","j5_tge4","jge6_t2","jge6_t3","jge6_tge4"]

disc="BDT_ljets"

sysnames=["_CMS_ttH_CSVLFUp","_CMS_ttH_CSVLFDown","_CMS_ttH_CSVHFUp","_CMS_ttH_CSVHFDown",
           "_CMS_ttH_CSVHFStats1Up","_CMS_ttH_CSVHFStats1Down","_CMS_ttH_CSVLFStats1Up","_CMS_ttH_CSVLFStats1Down",
           "_CMS_ttH_CSVHFStats2Up","_CMS_ttH_CSVHFStats2Down","_CMS_ttH_CSVLFStats2Up","_CMS_ttH_CSVLFStats2Down",
           "_CMS_ttH_CSVCErr1Up","_CMS_ttH_CSVCErr1Down","_CMS_ttH_CSVCErr2Up","_CMS_ttH_CSVCErr2Down","_CMS_scale_jUp","_CMS_scale_jDown","_CMS_res_jUp","_CMS_res_jDown"]
addPseudoData(infname,samplesWOttH,categories,sysnames,disc)
