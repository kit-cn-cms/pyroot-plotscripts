import ROOT
import sys
import os
from array import array 
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)


def getCanvas(name,ratiopad=False):
    if ratiopad:
        c=ROOT.TCanvas(name,name,1024,1024)
        c.Divide(1,2)
        c.cd(1).SetPad(0.,0.3,1.0,1.0);
        c.cd(1).SetBottomMargin(0.0);
        c.cd(2).SetPad(0.,0.0,1.0,0.3);
        c.cd(2).SetTopMargin(0.0);
        c.cd(1).SetTopMargin(0.07);
        c.cd(2).SetBottomMargin(0.4);
        c.cd(1).SetRightMargin(0.05);
        c.cd(1).SetLeftMargin(0.15);
        c.cd(2).SetRightMargin(0.05);
        c.cd(2).SetLeftMargin(0.15);
        c.cd(2).SetTicks(1,1)
        c.cd(1).SetTicks(1,1)
    else:
        c=ROOT.TCanvas(name,name,1024,768)
        c.SetRightMargin(0.05)
        c.SetTopMargin(0.07)
        c.SetLeftMargin(0.15)
        c.SetBottomMargin(0.15)
        c.SetTicks(1,1)

    return c


infname=sys.argv[1]
outname=sys.argv[2]
print "init"

#acats=["ljets_j4_t4","ljets_j5_tge4","ljets_jge6_t3","ljets_jge6_tge4","ljets_j5_t3","ljets_j4_t3","ljets_jge6_t2"]

scats=["ljets_jge6_tge3","ljets_j5_tge3","ljets_j4_tge3"]
#acats+=["ljets_jge6_tge4_low","ljets_jge6_tge4_high","ljets_jge6_tge4_MEMONLY","ljets_jge6_t3_low","ljets_jge6_t3_high","ljets_jge6_t3_MEMONLY","ljets_jge6_tge3_tt2bnode","ljets_jge6_tge3_ttbbnode","ljets_jge6_tge3_ttbnode","ljets_jge6_tge3_ttccnode","ljets_jge6_tge3_ttlfnode","ljets_jge6_tge3_ttHnode"]
#acats+=["ljets_jge6_tge4_low","ljets_jge6_tge4_high","ljets_jge6_t3_low","ljets_jge6_t3_high","ljets_j4_t4_high","ljets_j5_tge4_high","ljets_j4_t4_high","ljets_j5_tge4_high"]
acats=[]
for sc in scats:
    for node in ["ttlfnode","ttbbnode","ttHnode","ttccnode","ttbnode","tt2bnode"]:
      acats.append(sc+"_"+node)
      
doKStest=True

cats=[]
for c in acats:
  #cats.append(c+"_high")
  #cats.append(c+"_low")
  cats.append(c)

#procs="ttH ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar ttbarIncl".split(" ")
procs="ttbarOther ttbarPlusBBbar ttbarPlus2B ttbarPlusB ttbarPlusCCbar ttH".split(" ")
print procs

print "ok"

systs=['CMS_ttHbb_PDF_2017']
asysts=['CMS_btag_lf_2017', 'CMS_btag_hf_2017', 'CMS_btag_hfstats1_2017', 'CMS_btag_lfstats1_2017', 'CMS_btag_hfstats2_2017', 'CMS_btag_lfstats2_2017', 'CMS_btag_cferr1_2017', 'CMS_btag_cferr2_2017', 'CMS_ttHbb_PU', 'CMS_eff_m_2017', 'CMS_eff_e_2017', 'CMS_effTrigger_m_2017', 'CMS_effTrigger_e_2017', 'CMS_res_j_2017', 'CMS_scaleAbsoluteStat_j_2017', 'CMS_scaleTimePtEta_j_2017', 'CMS_scaleRelativeJEREC1_j_2017', 'CMS_scaleRelativeJEREC2_j_2017', 'CMS_scaleRelativePtEC1_j_2017', 'CMS_scaleRelativePtEC2_j_2017', 'CMS_scaleRelativeStatFSR_j_2017', 'CMS_scaleRelativeStatEC_j_2017', 'CMS_scaleRelativeStatHF_j_2017', 'CMS_scaleAbsoluteScale_j', 'CMS_scaleAbsoluteMPFBias_j', 'CMS_scaleFragmentation_j', 'CMS_scaleSinglePionECAL_j', 'CMS_scaleSinglePionHCAL_j', 'CMS_scaleFlavorQCD_j', 'CMS_scaleRelativeJERHF_j', 'CMS_scaleRelativePtBB_j', 'CMS_scaleRelativePtHF_j', 'CMS_scaleRelativeBal_j', 'CMS_scaleRelativeFSR_j', 'CMS_scalePileUpDataMC_j', 'CMS_scalePileUpPtRef_j', 'CMS_scalePileUpPtBB_j', 'CMS_scalePileUpPtEC1_j', 'CMS_scalePileUpPtEC2_j', 'CMS_scalePileUpPtHF_j', 'CMS_ttHbb_PDF_2017', 'CMS_ttHbb_scaleMuF', 'CMS_ttHbb_scaleMuR', 'CMS_ttHbb_FSR_ttbarOther_2017', 'CMS_ttHbb_FSR_ttbarPlusB_2017', 'CMS_ttHbb_FSR_ttbarPlus2B_2017', 'CMS_ttHbb_FSR_ttbarPlusBBbar_2017', 'CMS_ttHbb_FSR_ttbarPlusCCbar_2017', 'CMS_ttHbb_ISR_ttbarOther_2017', 'CMS_ttHbb_ISR_ttbarPlusB_2017', 'CMS_ttHbb_ISR_ttbarPlus2B_2017', 'CMS_ttHbb_ISR_ttbarPlusBBbar_2017', 'CMS_ttHbb_ISR_ttbarPlusCCbar_2017']

#filter non existent systs
systs=[]
for asyst in asysts:
    if not "_j" in asyst:
      continue
    systs.append(asyst)  

#for p in procs:
    #for s in ["CMS_scaleFlavorQCD_j_2017","JESPileUpDataMC_j_2017","JESPileUpPtRef_j_2017","JESPileUpPtBB_j_2017","JESPileUpPtEC1_j_2017","JESPileUpPtEC2_j_2017","JESPileUpPtHF_j_2017","CMS_scaleAbsoluteMPFBias_j_2017","CMS_ttHbb_ISR_ttbarPlusBBbar","CMS_ttHbb_FSR_ttbarPlusBBbar","CMS_ttHbb_UE_ttbarPlusBBbar"]:
        #systs.append(s)

#procs="ttH_hbb ttH_hcc ttH_hww ttH_hzz ttH_htt ttH_hgg ttH_hgluglu ttH_hzg ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar singlet wjets zjets ttbarW ttbarZ diboson".split(" ")
#procs="ttH ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar ttbarIncl singlet wjets zjets diboson ttbarZ ttbarW".split(" ")


inf=ROOT.TFile(infname,"READ")

name=outname
if not os.path.exists(name+"SystShapes"):
    os.makedirs(name+"SystShapes")
    
buff=ROOT.TCanvas("buff","buff",800,800)
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
    elif p=="ttH":
      firstnom=inf.Get("ttH_hbb"+"_"+discname+"_"+c)
      for subp in "ttH_hcc ttH_hww ttH_hzz ttH_htt ttH_hgg ttH_hgluglu ttH_hzg".split(" "):
        subnom=inf.Get(subp+"_"+discname+"_"+c)
        firstnom.Add(subnom)  
    else:
      firstnom=inf.Get(p+"_"+discname+"_"+c)
    if firstnom==None:
        continue
    for s in systs:
      nom=firstnom.Clone()
      print p+"_"+discname+"_"+c+"_"+s
      if p=="ttbarIncl":
        up=inf.Get("ttbarOther"+"_"+discname+"_"+c+"_"+s+"Up")
        down=inf.Get("ttbarOther"+"_"+discname+"_"+c+"_"+s+"Down")
        if up==None or down==None:
            print "did not find", "ttbarOther"+"_"+discname+"_"+c+"_"+s+"Up"
            continue
        for subp in "ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar".split(" "):
          subup=inf.Get(subp+"_"+discname+"_"+c+"_"+s+"Up")
          subdown=inf.Get(subp+"_"+discname+"_"+c+"_"+s+"Down")
          if subup==None or subdown==None:
            print "did not find subup", subp+"_"+discname+"_"+c+"_"+s+"Up"
            #print continue
            continue
          print "what"
          up.Add(subup)
          down.Add(subdown)
      elif p=="ttH":
        up=inf.Get("ttH_hbb"+"_"+discname+"_"+c+"_"+s+"Up")
        down=inf.Get("ttH_hbb"+"_"+discname+"_"+c+"_"+s+"Down")
        if up==None or down==None:
            print "did not find", "ttH_hbb"+"_"+discname+"_"+c+"_"+s+"Up"
            continue
        for subp in "ttH_hcc ttH_hww ttH_hzz ttH_htt ttH_hgg ttH_hgluglu ttH_hzg".split(" "):
          subup=inf.Get(subp+"_"+discname+"_"+c+"_"+s+"Up")
          subdown=inf.Get(subp+"_"+discname+"_"+c+"_"+s+"Down")
          if subup==None or subdown==None:
            print "did not find subup", subp+"_"+discname+"_"+c+"_"+s+"Up"
            #print continue
            continue
          print "what"
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
        canvas=getCanvas(p+"_"+discname+"_"+c+"_"+s,True)
        #canvas=ROOT.TCanvas(p+"_"+discname+"_"+c+"_"+s,p+"_"+discname+"_"+c+"_"+s,800,600)
        canvas.cd(1)
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
        
        canvas.cd(2)
        nomr=nom.Clone()
        nomr.Divide(nom)
        upr=up.Clone()
        upr.Divide(nom)
        downr=down.Clone()
        downr.Divide(nom)
        upperRatioMax=max(upr.GetMaximum(),downr.GetMaximum())
        lowerRatioMin=min(upr.GetMinimum(),downr.GetMinimum())
        nomr.GetYaxis().SetRangeUser(lowerRatioMin*0.9,upperRatioMax*1.1)
        print upperRatioMax, lowerRatioMin
        exit(0)
        #nomr.GetYaxis().SetRangeUser(0.5,1.5)
        nomr.Draw("histoE")
        upr.Draw("samehistoE")
        downr.Draw("samehistoE")

        canvas.Print(name+'.pdf')
        canvas.SaveAs(name+"SystShapes/"+p+"_"+discname+"_"+c+"_"+s+".png")
        canvas.SaveAs(name+"SystShapes/"+p+"_"+discname+"_"+c+"_"+s+".pdf")
        ratioc=ROOT.TCanvas(p+"_"+discname+"_"+c+"_"+s,p+"_"+discname+"_"+c+"_"+s,800,300)
      
        ratioc.SetTitle(nom.GetTitle())
        ratioc.SaveAs(name+"SystShapes/Ratio_"+p+"_"+discname+"_"+c+"_"+s+".png")
        ratioc.SaveAs(name+"SystShapes/Ratio_"+p+"_"+discname+"_"+c+"_"+s+".pdf")
        counter+=1
      else:
          print "did not find", p+"_"+discname+"_"+c+"_"+s+"Up"
buff.Print(name+'.pdf]')
        
        #exit(0)
