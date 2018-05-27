import ROOT
import sys
from array import array 
ROOT.gROOT.SetBatch(True)

infname=sys.argv[1]

cats=["ljets_j4_t2","ljets_j5_t2","ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t2","ljets_jge6_t3","ljets_jge6_tge4",]
#procs=["ttH","ttbarOther","ttbarPlusCCbar","ttbarPlusB","ttbarPlus2B","ttbarPlusBBbar",]
systs=['CMS_ttH_Q2scale_ttbarOther', 'CMS_ttH_Q2scale_ttbarPlusB', 'CMS_ttH_Q2scale_ttbarPlus2B', 'CMS_ttH_Q2scale_ttbarPlusBBbar', 'CMS_ttH_Q2scale_ttbarPlusCCbar', 'CMS_ttH_CSVLF', 'CMS_ttH_CSVHF', 'CMS_ttH_CSVHFStats1', 'CMS_ttH_CSVLFStats1', 'CMS_ttH_CSVHFStats2', 'CMS_ttH_CSVLFStats2', 'CMS_ttH_CSVCErr1', 'CMS_ttH_CSVCErr2', 'CMS_scale_j', 'CMS_ttH_PU', 'CMS_res_j', 'CMS_ttH_eff_mu', 'CMS_ttH_eff_el', 'CMS_ttH_ljets_Trig_mu', 'CMS_ttH_ljets_Trig_el']

procs="ttH_hbb ttH_hcc ttH_hww ttH_hzz ttH_htt ttH_hgg ttH_hgluglu ttH_hzg ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar singlet wjets zjets ttbarW ttbarZ diboson".split(" ")
print procs

inf=ROOT.TFile(infname,"READ")

for c in cats:
  for p in procs:
    nom=inf.Get(p+"_finaldiscr_"+c)
    for s in systs:
      print p+"_finaldiscr_"+c+"_"+s
      up=inf.Get(p+"_finaldiscr_"+c+"_"+s+"Up")
      down=inf.Get(p+"_finaldiscr_"+c+"_"+s+"Down")
      if up!=None and down!=None:
	up.SetLineColor(ROOT.kRed)
	down.SetLineColor(ROOT.kGreen)
	canvas=ROOT.TCanvas(p+"_finaldiscr_"+c+"_"+s,p+"_finaldiscr_"+c+"_"+s,800,600)
	nom.Draw("histo")
	up.Draw("histoSame")
	down.Draw("histoSame")
	canvas.SaveAs("shapes/"+p+"_finaldiscr_"+c+"_"+s+".png")
	#exit(0)