import ROOT
import sys
import os
from array import array 
from plot_additional_Zprime_MC import *

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

infname=sys.argv[1]
outname=sys.argv[2]
print "init"

ABCDversion="ABCD5"

acats=["withtopbtag_CatA_Zprime_M","withtopbtag_CatB_Zprime_M"]

doKStest=True

cats=[]
for cat in ["withtopbtag","notopbtag"]:
    for Reg in ["CatA","CatB","CatC","CatD"]:
        cats.append(cat+"_"+Reg+"_Zprime_M")

print "ok"
#systs=['CMS_ttHbb_FSR', 'CMS_ttHbb_ISR', 'CMS_ttHbb_HDAMP', 'CMS_ttHbb_UE','CMS_ttHbbFROMTREES_FSR', 'CMS_ttHbbFROMTREES_ISR', 'CMS_ttHbbFROMTREES_HDAMP', 'CMS_ttHbbFROMTREES_UE']
#systs=['CMS_ttHbb_PDF', 'CMS_ttHbb_scaleMuF', 'CMS_ttHbb_scaleMuR']

systs=[]

#for sys in ["MCSF_renfac_env","MCSF_CSVLF","MCSF_CSVHF","MCSF_CSVHFStats1","MCSF_CSVLFStats1","MCSF_CSVHFStats2","MCSF_CSVLFStats2","MCSF_CSVCErr1","MCSF_CSVCErr2","MCSF_toptag","MCSF_Wtag","MCSF_PU","MCSF_PDF","MCSF_Lumi","MCSF_Trigger","ttbarXS","nominal_JES","nominal_JER","ABCD_shape","ABCD_rate"]:
#for sys in ["nominal_JES","nominal_JER"]:
for sys in ["ABCD_shape","ABCD_rate"]:
    systs.append(sys)
    

#procs="ttH_hbb ttH_hcc ttH_hww ttH_hzz ttH_htt ttH_hgg ttH_hgluglu ttH_hzg ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar singlet wjets zjets ttbarW ttbarZ diboson".split(" ")
#procs="SigZprime15001200_tWb SigZprime20001200_tWb SigZprime25001200_tWb SigZprime15001200_ttZ SigZprime20001200_ttZ SigZprime25001200_ttZ SigZprime15001200_ttH SigZprime20001200_ttH SigZprime25001200_ttH ttbar QCDMadgraph".split(" ")
#procs="ttbar".split(" ")
procs="QCDMadgraph".split(" ")
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

  for p in procs:
    firstnom=inf.Get(p+"_"+ABCDversion+"_"+c+"_"+ABCDversion+"_nominal")
    for s in systs:
        
      if ("ABCD_shape" in s) or ("ABCD_rate" in s):
        if ("withtopbtag" in c): 
            RegA=inf.Get(p+"_"+ABCDversion+"_withtopbtag_CatA_Zprime_M_"+ABCDversion+"_nominal").Clone()
            RegB=inf.Get(p+"_"+ABCDversion+"_withtopbtag_CatB_Zprime_M_"+ABCDversion+"_nominal").Clone()
            RegC=inf.Get(p+"_"+ABCDversion+"_withtopbtag_CatC_Zprime_M_"+ABCDversion+"_nominal").Clone()
            RegD=inf.Get(p+"_"+ABCDversion+"_withtopbtag_CatD_Zprime_M_"+ABCDversion+"_nominal").Clone()
            firstnom=RegB.Clone()
            firstnom.Multiply(RegC)
            firstnom.Divide(RegD)
            ##upRegB=inf.Get(p+"_"+ABCDversion+"_withtopbtag_CatB_Zprime_M_"+ABCDversion+"_"+s+"Up")
            ##upRegC=inf.Get(p+"_"+ABCDversion+"_withtopbtag_CatC_Zprime_M_"+ABCDversion+"_"+s+"Up")
            ##upRegD=inf.Get(p+"_"+ABCDversion+"_withtopbtag_CatD_Zprime_M_"+ABCDversion+"_"+s+"Up")
            ##downRegB=inf.Get(p+"_"+ABCDversion+"_withtopbtag_CatB_Zprime_M_"+ABCDversion+"_"+s+"Down")
            ##downRegC=inf.Get(p+"_"+ABCDversion+"_withtopbtag_CatC_Zprime_M_"+ABCDversion+"_"+s+"Down")
            ##downRegD=inf.Get(p+"_"+ABCDversion+"_withtopbtag_CatD_Zprime_M_"+ABCDversion+"_"+s+"Down")            
            ##upRegB.Multiply(upRegC)
            ##upRegB.Divide(upRegD)
            ##downRegB.Multiply(downRegC)
            ##downRegB.Divide(downRegD)
            
                        
        elif("notopbtag" in c):   
            RegA=inf.Get(p+"_"+ABCDversion+"_notopbtag_CatA_Zprime_M_"+ABCDversion+"_nominal").Clone()
            RegB=inf.Get(p+"_"+ABCDversion+"_notopbtag_CatB_Zprime_M_"+ABCDversion+"_nominal").Clone()
            RegC=inf.Get(p+"_"+ABCDversion+"_notopbtag_CatC_Zprime_M_"+ABCDversion+"_nominal").Clone()
            RegD=inf.Get(p+"_"+ABCDversion+"_notopbtag_CatD_Zprime_M_"+ABCDversion+"_nominal").Clone()
            firstnom=RegB.Clone()
            firstnom.Multiply(RegC)
            firstnom.Divide(RegD)
            
            ##upRegB=inf.Get(p+"_"+ABCDversion+"_notopbtag_CatB_Zprime_M_"+ABCDversion+"_"+s+"Up")
            ##upRegC=inf.Get(p+"_"+ABCDversion+"_notopbtag_CatC_Zprime_M_"+ABCDversion+"_"+s+"Up")
            ##upRegD=inf.Get(p+"_"+ABCDversion+"_notopbtag_CatD_Zprime_M_"+ABCDversion+"_"+s+"Up")
            ##downRegB=inf.Get(p+"_"+ABCDversion+"_notopbtag_CatB_Zprime_M_"+ABCDversion+"_"+s+"Down")
            ##downRegC=inf.Get(p+"_"+ABCDversion+"_notopbtag_CatC_Zprime_M_"+ABCDversion+"_"+s+"Down")
            ##downRegD=inf.Get(p+"_"+ABCDversion+"_notopbtag_CatD_Zprime_M_"+ABCDversion+"_"+s+"Down")            
            ##upRegB.Multiply(upRegC)
            ##upRegB.Divide(upRegD)
            ##downRegB.Multiply(downRegC)
            ##downRegB.Divide(downRegD)       
            
        
        if ("ABCD_rate" in s):
            nom=firstnom.Clone()
            up=firstnom.Clone()
            down=firstnom.Clone()
            up.Scale(1.0+Zprime_withtopbtag_systrate)
            down.Scale(1.0-Zprime_withtopbtag_systrate)
        if ("ABCD_shape" in s):
            x0ABCD=0.0
            x0widABCD=0.0
            for i in range(firstnom.GetNbinsX()):
              if(RegA.GetBinContent(i)>0 and RegB.GetBinContent(i)>0 and RegC.GetBinContent(i)>0 and RegD.GetBinContent(i)>0):
                print "regA: ",RegA.GetBinContent(i),"regB: ",RegB.GetBinContent(i),"regC: ",RegC.GetBinContent(i),"regD: ",RegD.GetBinContent(i)
                #print RegA.GetBinContent(i)*RegD.GetBinContent(i))/(RegB.GetBinContent(i)*RegC.GetBinContent(i))
                x0ABCD=x0ABCD+RegA.GetBinCenter(i)*1.0/(1.0/float(RegA.GetBinContent(i))+1.0/float(RegB.GetBinContent(i))+1.0/float(RegC.GetBinContent(i))+1.0/float(RegD.GetBinContent(i)))
                print "xotempo", x0ABCD
                x0widABCD=x0widABCD+1.0/(1.0/float(RegA.GetBinContent(i))+1.0/float(RegB.GetBinContent(i))+1.0/float(RegC.GetBinContent(i))+1.0/float(RegD.GetBinContent(i)))
            print "x0ABCD   ",x0ABCD,  "x0widABCD   ",x0widABCD 
            x0ABCD=x0ABCD/x0widABCD
            print "x0ABCD   ",x0ABCD
            raw_input()
            f1=ROOT.TF1("fit","[0]*(x-"+str(x0ABCD)+")+1.0",1000,5050)
            f2=ROOT.TF1("fit","-[0]*(x-"+str(x0ABCD)+")+1.0",1000,5050)
            if ("withtopbtag" in c): 
                f1.SetParameter(0,Zprime_withtopbtag_systshape_m)
                f2.SetParameter(0,Zprime_withtopbtag_systshape_m)
            if ("notopbtag" in c): 
                f1.SetParameter(0,Zprime_notopbtag_systshape_m)
                f2.SetParameter(0,Zprime_notopbtag_systshape_m)
            #f1.SetParameter(0,Zprime_withtopbtag_systshape_m)
            #f1.SetParameter(1,0.0)  
            #f1.SetParameter(2,2000.0)  
            #f1.FixParameter(2,2000.0)
            #f2.SetParameter(2,2000.0)  
            #f2.FixParameter(2,2000.0)
            
            nom=firstnom.Clone()
            up=firstnom.Clone()
            down=firstnom.Clone()
            up.Multiply(f1,1.0)
            down.Multiply(f2,1.0)
      else:  
        nom=firstnom.Clone()
        print p+"_"+ABCDversion+"_"+c+"_"+ABCDversion+"_"+s
        up=inf.Get(p+"_"+ABCDversion+"_"+c+"_"+ABCDversion+"_"+s+"Up")
        down=inf.Get(p+"_"+ABCDversion+"_"+c+"_"+ABCDversion+"_"+s+"Down")
      #nom.Rebin(2)
      #up.Rebin(2)
      #down.Rebin(2)
      print down, up
      if up!=None and down!=None:
	up.SetLineColor(ROOT.kRed)
	up.SetTitle("up")
	down.SetTitle("down")
	down.SetLineColor(ROOT.kCyan)
	
        
	canvas=ROOT.TCanvas(p+"_"+c+"_"+s,p+"_"+c+"_"+s,1024,1024)
        canvas.Divide(1,2)
        canvas.cd(1).SetPad(0.,0.3,1.0,1.0);
        canvas.cd(1).SetBottomMargin(0.0);
        canvas.cd(2).SetPad(0.,0.0,1.0,0.3);
        canvas.cd(2).SetTopMargin(0.0);
        canvas.cd(1).SetTopMargin(0.07);
        canvas.cd(2).SetBottomMargin(0.4);
        canvas.cd(1).SetRightMargin(0.05);
        canvas.cd(1).SetLeftMargin(0.15);
        canvas.cd(2).SetRightMargin(0.05);
        canvas.cd(2).SetLeftMargin(0.15);
        canvas.cd(2).SetTicks(1,1)
        canvas.cd(1).SetTicks(1,1)        
        
	maxdiff=0
	mindiff=1
	for i in range(nom.GetNbinsX()):
          if nom.GetBinContent(i)>0:
            if maxdiff<abs((nom.GetBinContent(i)-nom.GetBinContent(i))/(nom.GetBinContent(i))):
                maxdiff=abs((nom.GetBinContent(i)-nom.GetBinContent(i))/(nom.GetBinContent(i)))
            if maxdiff<abs((nom.GetBinContent(i)-up.GetBinContent(i))/(nom.GetBinContent(i))):
                maxdiff=abs((nom.GetBinContent(i)-up.GetBinContent(i))/(nom.GetBinContent(i)))
                
            if mindiff>abs((nom.GetBinContent(i)-down.GetBinContent(i))/(nom.GetBinContent(i))):
                mindiff=abs((nom.GetBinContent(i)-down.GetBinContent(i))/(nom.GetBinContent(i)))
            if mindiff>abs((nom.GetBinContent(i)-up.GetBinContent(i))/(nom.GetBinContent(i))):
                mindiff=abs((nom.GetBinContent(i)-up.GetBinContent(i))/(nom.GetBinContent(i)))
  
          #nom.SetBinContent(i,nom.GetBinContent(i)*(50.0/nom.GetXaxis().GetBinWidth(i)))  
          #up.SetBinContent(i,up.GetBinContent(i)*(50.0/up.GetXaxis().GetBinWidth(i))) 
          #down.SetBinContent(i,down.GetBinContent(i)*(50.0/down.GetXaxis().GetBinWidth(i)))  
            
            
	maxval=max(nom.GetMaximum(), max(up.GetMaximum(),down.GetMaximum()))
	nom.SetMaximum(1.5*maxval)
	nom.Draw("histo")
	nom.SetTitle(p+"_"+c+" "+s)
	nom.GetXaxis().SetTitle("m(Z') in GeV")
	nom.GetYaxis().SetTitle("Events")
	up.Draw("histoSame")
	down.Draw("histoSame")
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
		
        if True:
            canvas.cd(2)
            line=nom.Clone()
            line.Divide(nom)
            line.GetYaxis().SetRangeUser((1.0-1.1*maxdiff),(1.0+1.1*maxdiff))
            line.GetYaxis().SetTitle('#frac{syst}{nominal}')
            line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
            line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
            line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
            line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*1.5)
            line.GetYaxis().SetTitleOffset(0.9)
            line.GetYaxis().SetNdivisions(505)
            for i in range(line.GetNbinsX()+1):
                line.SetBinContent(i,1)
                line.SetBinError(i,0)
            line.SetLineWidth(1)
            line.DrawCopy('histo')
            for hist in [up,down]:
                ratio=hist.Clone()
                ratio.Divide(nom)
                ratio.SetTitle('')
                ratio.DrawCopy('histoSame')
            canvas.cd(1)
        canvas.Update()
		
		
	canvas.SetTitle(p+"_"+c+" "+s)
	#canvas.BuildLegend()
	legend=ROOT.TLegend()
	legend.SetX1NDC(0.15)
	legend.SetX2NDC(0.95)
	legend.SetY1NDC(0.7)
	legend.SetY2NDC(0.88)
	legend.SetBorderSize(0);
	legend.SetLineStyle(0);
	legend.SetTextFont(42);
	legend.SetTextSize(0.02);
	legend.SetFillStyle(0);	
	if doKStest:
	  legend.AddEntry(nom,p+"_"+c+" (%.2f)" % integNom,"l")
          legend.AddEntry(up,p+"_"+c+" Up"+" (%.2f, %.2f), KS-prob. %.2f" % (integUp,fracUp,ksUp) +"","l")
          legend.AddEntry(down,p+"_"+c+" Down"+" (%.2f, %.2f), KS-prob. %.2f" % (integDown,fracDown,ksDown) +"","l")
          legend.AddEntry(0, s+"="+str(round(mindiff,3))+"-"+str(round(maxdiff,3)), "")
	else:
          legend.AddEntry(nom,p+"_"+c+" (%.2f)" % integNom,"l")
          legend.AddEntry(up,p+"_"+c+" Up"+" (%.2f, %.2f" % (integUp,fracUp) +")","l")
          legend.AddEntry(down,p+"_"+c+" Down"+" (%.2f, %.2f" % (integDown,fracDown) +")","l")
          legend.AddEntry(0, s+"="+str(round(mindiff,3))+"-"+str(round(maxdiff,3)), "")
	legend.Draw()
        if not os.path.exists(name+"SystShapes/"+p):
            os.makedirs(name+"SystShapes/"+p)
        canvas.Print(name+'.pdf')
	canvas.SaveAs(name+"SystShapes/"+p+"/"+p+"_"+c+"_"+s+".png")
	canvas.SaveAs(name+"SystShapes/"+p+"/"+p+"_"+c+"_"+s+".pdf")
	
	#ratioc=ROOT.TCanvas(p+"_"+c+"_"+s,p+"_"+c+"_"+s,800,300)
	#nomr=nom.Clone()
	#nomr.Divide(nom)
	#nomr.GetYaxis().SetRangeUser(0.5,1.5)
	#upr=up.Clone()
	#upr.Divide(nom)
	#downr=down.Clone()
	#downr.Divide(nom)
	#nomr.Draw("histo")
	#upr.Draw("samehisto")
	#downr.Draw("samehisto")
	#ratioc.SetTitle(nom.GetTitle())
	#ratioc.SaveAs(name+"SystShapes/"+p+"/Ratio_"+p+"_"+c+"_"+s+".png")
	#ratioc.SaveAs(name+"SystShapes/"+p+"/Ratio_"+p+"_"+c+"_"+s+".pdf")
	#counter+=1
buff.Print(name+'.pdf]')
	
#exit(0)

