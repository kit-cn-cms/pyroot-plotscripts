import ROOT
import sys
from array import array 
ROOT.gROOT.SetBatch(True)

infname=sys.argv[1]

cats=["ljets_j4_t2","ljets_j5_t2","s43_s43_BDT_common5_input_HT","s43_s43_BDT_common5_input_fourth_jet_pt","s53_BDT_common5_input_third_jet_pt","ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t3","ljets_jge6_tge4",]
for c in cats[5:]:
  cats.append(c+"_high")
  cats.append(c+"_low")
  
#procs=["ttH","ttbarOther","ttbarPlusCCbar","ttbarPlusB","ttbarPlus2B","ttbarPlusBBbar",]
#systs=['CMS_ttH_Q2scale_ttbarOther', 'CMS_ttH_Q2scale_ttbarPlusB', 'CMS_ttH_Q2scale_ttbarPlus2B', 'CMS_ttH_Q2scale_ttbarPlusBBbar', 'CMS_ttH_Q2scale_ttbarPlusCCbar', 'CMS_ttH_CSVLF', 'CMS_ttH_CSVHF', 'CMS_ttH_CSVHFStats1', 'CMS_ttH_CSVLFStats1', 'CMS_ttH_CSVHFStats2', 'CMS_ttH_CSVLFStats2', 'CMS_ttH_CSVCErr1', 'CMS_ttH_CSVCErr2', 'CMS_scale_j', 'CMS_ttH_PU', 'CMS_res_j', 'CMS_ttH_eff_mu', 'CMS_ttH_eff_el', 'CMS_ttH_ljets_Trig_mu', 'CMS_ttH_ljets_Trig_el']
systs=["CMS_ttH_PSscale_ttbarOther","CMS_ttH_PSscale_ttbarPlusB","CMS_ttH_PSscale_ttbarPlus2B","CMS_ttH_PSscale_ttbarPlusBBbar","CMS_ttH_PSscale_ttbarPlusCCbar"]


procs="ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar".split(" ")
print procs

inf=ROOT.TFile(infname,"READ")

for c in cats:
  if "ljets" in c:
    discname="finaldiscr"
  else:
    discname="inputVar"
  for p in procs:
    nom=inf.Get(p+"_"+discname+"_"+c)
    for s in systs:
      print p+"_"+discname+"_"+c+"_"+s
      up=inf.Get(p+"_"+discname+"_"+c+"_"+s+"Up")
      down=inf.Get(p+"_"+discname+"_"+c+"_"+s+"Down")
      if up!=None and down!=None:
	up.SetLineColor(ROOT.kRed)
	up.SetTitle("up")
	down.SetTitle("down")
	down.SetLineColor(ROOT.kGreen)
	canvas=ROOT.TCanvas(p+"_"+discname+"_"+c+"_"+s,p+"_"+discname+"_"+c+"_"+s,800,600)
	maxval=max(nom.GetMaximum(), max(up.GetMaximum(),down.GetMaximum()))
	nom.SetMaximum(1.3*maxval)
	nom.Draw("histoE")
	up.Draw("histoSameE")
	down.Draw("histoSameE")
	canvas.SetTitle(nom.GetTitle())
	canvas.BuildLegend()
	canvas.SaveAs("PSscaleShapes/"+p+"_"+discname+"_"+c+"_"+s+".png")
	canvas.SaveAs("PSscaleShapes/"+p+"_"+discname+"_"+c+"_"+s+".pdf")
	ratioc=ROOT.TCanvas(p+"_"+discname+"_"+c+"_"+s,p+"_"+discname+"_"+c+"_"+s,800,300)
	nomr=nom.Clone()
	nomr.Divide(nom)
	nomr.GetYaxis().SetRangeUser(0.5,1.5)
	upr=up.Clone()
	upr.Divide(nom)
	downr=down.Clone()
	downr.Divide(nom)
	nomr.Draw("histoE")
	upr.Draw("samehistoE")
	downr.Draw("samehistoE")
	ratioc.SetTitle(nom.GetTitle())
	ratioc.SaveAs("PSscaleShapes/Ratio_"+p+"_"+discname+"_"+c+"_"+s+".png")
	ratioc.SaveAs("PSscaleShapes/Ratio_"+p+"_"+discname+"_"+c+"_"+s+".pdf")
	#exit(0)