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
