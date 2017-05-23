# pyroot-plotscripts

1) combine
CMSSW_7_1_5
https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideHiggsAnalysisCombinedLimit

2) Our datacard making tool
https://github.com/cms-ttH/ttH-Limits/tree/80X

3) histograms for datacards
https://github.com/kit-cn-cms/pyroot-plotscripts

limits:
  combine -M Asymptotic --minosAlgo stepping -m 125 --run="blind" datacard.txt
  
  
  ## pyroot-plotscripts-base subtree repository
  * The basic pyroot-plotscripts functionality was factorized in a dedicated Gitlab repository:
  https://gitlab.cern.ch/kit-cn-cms/pyroot-plotscripts-base
  * This basic functionality is included as a subtree folder pyroot-plotscripts-base
  * Major changes should be pushed upstream via git subtree push.
  * The upstream repository uses a CI part to make sure that functionality is not broken.
