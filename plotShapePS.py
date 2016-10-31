import ROOT
import sys
import os
from array import array 
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

infname=sys.argv[1]
print "init"

#acats=["ljets_j4_t4","ljets_j5_tge4","ljets_jge6_t3","ljets_jge6_tge4","ljets_j5_t3","ljets_j4_t3"]
#acats=["ljets_j5_t3","ljets_j4_t3"]
acats=["ljets_j5_t3"]

cats=[]
for c in acats:
  cats.append(c+"_high")
  cats.append(c+"_low")

print "ok"
#procs=["ttH","ttbarOther","ttbarPlusCCbar","ttbarPlusB","ttbarPlus2B","ttbarPlusBBbar",]
systs=['CMS_ttH_Q2scale_ttbarOther', 'CMS_ttH_Q2scale_ttbarPlusB', 'CMS_ttH_Q2scale_ttbarPlus2B', 'CMS_ttH_Q2scale_ttbarPlusBBbar', 'CMS_ttH_Q2scale_ttbarPlusCCbar', 'CMS_ttH_CSVLF', 'CMS_ttH_CSVHF', 'CMS_ttH_CSVHFStats1', 'CMS_ttH_CSVLFStats1', 'CMS_ttH_CSVHFStats2', 'CMS_ttH_CSVLFStats2', 'CMS_ttH_CSVCErr1', 'CMS_ttH_CSVCErr2', 'CMS_scale_j', 'CMS_ttH_PU', 'CMS_res_j', 'CMS_ttH_eff_mu', 'CMS_ttH_eff_el', 'CMS_ttH_ljets_Trig_mu', 'CMS_ttH_ljets_Trig_el', 'CMS_ttH_PSscale_ttbarOther', 'CMS_ttH_PSscale_ttbarPlusB', 'CMS_ttH_PSscale_ttbarPlus2B', 'CMS_ttH_PSscale_ttbarPlusBBbar', 'CMS_ttH_PSscale_ttbarPlusCCbar']
#systs=["CMS_ttH_PSscale_ttbarOther","CMS_ttH_PSscale_ttbarPlusB","CMS_ttH_PSscale_ttbarPlus2B","CMS_ttH_PSscale_ttbarPlusBBbar","CMS_ttH_PSscale_ttbarPlusCCbar"]

procs="ttH_hbb ttH_hcc ttH_hww ttH_hzz ttH_htt ttH_hgg ttH_hgluglu ttH_hzg ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar singlet wjets zjets ttbarW ttbarZ diboson".split(" ")
#procs="ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar".split(" ")
print procs

inf=ROOT.TFile(infname,"READ")

name="allshapes"
if not os.path.exists(name+"Shapes"):
    os.makedirs(name+"Shapes")
    
buff=ROOT.TCanvas("buff","buff",800,600)
buff.Print(name+'.pdf[')

counter=0
for c in cats:
  print c
  if "ljets" in c:
    discname="finaldiscr"
  else:
    discname="inputVar"
  for p in procs:
    firstnom=inf.Get(p+"_"+discname+"_"+c)
    for s in systs:
      nom=firstnom.Clone()
      print p+"_"+discname+"_"+c+"_"+s
      up=inf.Get(p+"_"+discname+"_"+c+"_"+s+"Up")
      down=inf.Get(p+"_"+discname+"_"+c+"_"+s+"Down")
      #print down, up
      if up!=None and down!=None:
	up.SetLineColor(ROOT.kRed)
	up.SetTitle("up")
	down.SetTitle("down")
	down.SetLineColor(ROOT.kGreen)
	canvas=ROOT.TCanvas(p+"_"+discname+"_"+c+"_"+s,p+"_"+discname+"_"+c+"_"+s,800,600)
	maxval=max(nom.GetMaximum(), max(up.GetMaximum(),down.GetMaximum()))
	nom.SetMaximum(1.5*maxval)
	nom.Draw("histoE")
	nom.SetTitle(c+"_"+p+" "+s)
	up.Draw("histoSameE")
	down.Draw("histoSameE")
	integNom=nom.Integral()
	integDown=down.Integral()
	integUp=up.Integral()
	fracUp=0
	fracDown=0
	if integNom!=0:
	  fracDown=integDown/integNom
	  fracUp=integUp/integNom
		  
	canvas.SetTitle(c+"_"+p+" "+s)
	#canvas.BuildLegend()
	legend=ROOT.TLegend()
	legend.SetX1NDC(0.15)
	legend.SetX2NDC(0.95)
	legend.SetY1NDC(0.7)
	legend.SetY2NDC(0.88)
	legend.SetBorderSize(0);
	legend.SetLineStyle(0);
	legend.SetTextFont(42);
	legend.SetTextSize(0.03);
	legend.SetFillStyle(0);	
	legend.AddEntry(nom,c+"_"+p+" (%.2f)" % integNom,"l")
	legend.AddEntry(up,c+"_"+p+" Up"+" (%.2f, %.2f" % (integUp,fracUp) +")","l")
	legend.AddEntry(down,c+"_"+p+" Down"+" (%.2f, %.2f" % (integDown,fracDown) +")","l")
	legend.Draw()

        canvas.Print(name+'.pdf')
	canvas.SaveAs(name+"Shapes/"+p+"_"+discname+"_"+c+"_"+s+".png")
	canvas.SaveAs(name+"Shapes/"+p+"_"+discname+"_"+c+"_"+s+".pdf")
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
	ratioc.SaveAs(name+"Shapes/Ratio_"+p+"_"+discname+"_"+c+"_"+s+".png")
	ratioc.SaveAs(name+"Shapes/Ratio_"+p+"_"+discname+"_"+c+"_"+s+".pdf")
	counter+=1
buff.Print(name+'.pdf]')
	
	#exit(0)
