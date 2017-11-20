import ROOT
import sys
import os
from array import array 
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

infname=sys.argv[1]
outname=sys.argv[2]
print "init"

#acats=["ljets_j4_t4","ljets_j5_tge4","ljets_jge6_t3","ljets_jge6_tge4","ljets_j5_t3","ljets_j4_t3","ljets_jge6_t2"]

acats=["ljets_jge6_t3","ljets_jge6_tge4","ljets_j4_t4","ljets_j5_tge4"]
#acats+=["ljets_jge6_tge4_low","ljets_jge6_tge4_high","ljets_jge6_tge4_MEMONLY","ljets_jge6_t3_low","ljets_jge6_t3_high","ljets_jge6_t3_MEMONLY","ljets_jge6_tge3_tt2bnode","ljets_jge6_tge3_ttbbnode","ljets_jge6_tge3_ttbnode","ljets_jge6_tge3_ttccnode","ljets_jge6_tge3_ttlfnode","ljets_jge6_tge3_ttHnode"]
acats+=["ljets_jge6_tge4_low","ljets_jge6_tge4_high","ljets_jge6_t3_low","ljets_jge6_t3_high","ljets_j4_t4_high","ljets_j5_tge4_high","ljets_j4_t4_high","ljets_j5_tge4_high"]
#acats=["ljets_j5_t3","ljets_j4_t3"]
#acats=["ljets_j5_t3"]

doKStest=True

cats=[]
for c in acats:
  #cats.append(c+"_high")
  #cats.append(c+"_low")
  cats.append(c)

print "ok"
#systs=['CMS_ttHbb_FSR', 'CMS_ttHbb_ISR', 'CMS_ttHbb_HDAMP', 'CMS_ttHbb_UE','CMS_ttHbbFROMTREES_FSR', 'CMS_ttHbbFROMTREES_ISR', 'CMS_ttHbbFROMTREES_HDAMP', 'CMS_ttHbbFROMTREES_UE']
systs=['CMS_ttHbb_PDF', 'CMS_ttHbb_scaleMuF', 'CMS_ttHbb_scaleMuR']

#procs="ttH_hbb ttH_hcc ttH_hww ttH_hzz ttH_htt ttH_hgg ttH_hgluglu ttH_hzg ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar singlet wjets zjets ttbarW ttbarZ diboson".split(" ")
procs="ttH ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar ttbarIncl".split(" ")
print procs

inf=ROOT.TFile(infname,"READ")

name=outname
if not os.path.exists(name+"SystShapes"):
    os.makedirs(name+"SystShapes")
    
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
    if p=="ttbarIncl":
      firstnom=inf.Get("ttbarOther"+"_"+discname+"_"+c)
      for subp in "ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar".split(" "):
        subnom=inf.Get(subp+"_"+discname+"_"+c)
        firstnom.Add(subnom)
    else:
      firstnom=inf.Get(p+"_"+discname+"_"+c)
    for s in systs:
      nom=firstnom.Clone()
      print p+"_"+discname+"_"+c+"_"+s
      if p=="ttbarIncl":
        up=inf.Get("ttbarOther"+"_"+discname+"_"+c+"_"+s+"Up")
        down=inf.Get("ttbarOther"+"_"+discname+"_"+c+"_"+s+"Down")
        for subp in "ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar".split(" "):
          subup=inf.Get(subp+"_"+discname+"_"+c+"_"+s+"Up")
          subdown=inf.Get(subp+"_"+discname+"_"+c+"_"+s+"Down")
          up.Add(subup)
          down.Add(subdown)
      else:
        up=inf.Get(p+"_"+discname+"_"+c+"_"+s+"Up")
        down=inf.Get(p+"_"+discname+"_"+c+"_"+s+"Down")
      #print down, up
      if up!=None and down!=None:
	up.SetLineColor(ROOT.kRed)
	up.SetTitle("up")
	down.SetTitle("down")
	down.SetLineColor(ROOT.kCyan)
	canvas=ROOT.TCanvas(p+"_"+discname+"_"+c+"_"+s,p+"_"+discname+"_"+c+"_"+s,800,600)
	maxval=max(nom.GetMaximum(), max(up.GetMaximum(),down.GetMaximum()))
	nom.SetMaximum(1.5*maxval)
	nom.Draw("histoE")
	nom.SetTitle(c+"_"+p+" "+s)
	up.Draw("histoSameE")
	down.Draw("histoSameE")
	if doKStest:
          ksUp=nom.KolmogorovTest(up)
          ksDown=nom.KolmogorovTest(down)
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
	if doKStest:
	  legend.AddEntry(nom,c+"_"+p+" (%.2f)" % integNom,"l")
          legend.AddEntry(up,c+"_"+p+" Up"+" (%.2f, %.2f), KS-prob. %.2f" % (integUp,fracUp,ksUp) +"","l")
          legend.AddEntry(down,c+"_"+p+" Down"+" (%.2f, %.2f), KS-prob. %.2f" % (integDown,fracDown,ksDown) +"","l")
	else:
          legend.AddEntry(nom,c+"_"+p+" (%.2f)" % integNom,"l")
          legend.AddEntry(up,c+"_"+p+" Up"+" (%.2f, %.2f" % (integUp,fracUp) +")","l")
          legend.AddEntry(down,c+"_"+p+" Down"+" (%.2f, %.2f" % (integDown,fracDown) +")","l")
	legend.Draw()

        canvas.Print(name+'.pdf')
	canvas.SaveAs(name+"SystShapes/"+p+"_"+discname+"_"+c+"_"+s+".png")
	canvas.SaveAs(name+"SystShapes/"+p+"_"+discname+"_"+c+"_"+s+".pdf")
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
	ratioc.SaveAs(name+"SystShapes/Ratio_"+p+"_"+discname+"_"+c+"_"+s+".png")
	ratioc.SaveAs(name+"SystShapes/Ratio_"+p+"_"+discname+"_"+c+"_"+s+".pdf")
	counter+=1
buff.Print(name+'.pdf]')
	
	#exit(0)
