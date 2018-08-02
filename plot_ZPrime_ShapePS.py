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




def GetCMSandInfoLabels():
    posy = 1.-ROOT.gStyle.GetPadTopMargin()+0.03

    cms = ROOT.TPaveText(
        ROOT.gStyle.GetPadLeftMargin()+0.05,posy+0.035,
        1.-ROOT.gStyle.GetPadRightMargin(), 1.,
        "NDC"
    )
    cms.AddText("#scale[1.5]{CMS private work}")
    cms.SetFillColor(0)
    cms.SetTextFont(43)
    cms.SetTextSize(26)
    cms.SetMargin(0.)
    cms.SetTextAlign(13)

    info = ROOT.TPaveText(
        0.9, posy+0.055,
        #1.-ROOT.gStyle.GetPadRightMargin(), 1.,
        1.-ROOT.gStyle.GetPadRightMargin()/2.0, 1.,
        "NDC"
    )
    info.AddText("#scale[1.5]{35.9 fb^{-1} (13 TeV)}")
    info.SetFillColor(0)
    info.SetTextFont(43)
    info.SetTextSize(26)
    info.SetMargin(0.)
    info.SetTextAlign(33)

    return cms,info


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
systs_avg_max_wtb=[]
systs_avg_max_ntb=[]
systs_avg_min_wtb=[]
systs_avg_min_ntb=[]

for sys in ["MCSF_renfac_env","MCSF_CSVLF","MCSF_CSVHF","MCSF_CSVHFStats1","MCSF_CSVLFStats1","MCSF_CSVHFStats2","MCSF_CSVLFStats2","MCSF_CSVCErr1","MCSF_CSVCErr2","MCSF_toptag","MCSF_Wtag","MCSF_PU","MCSF_PDF","MCSF_Lumi","MCSF_Trigger","ttbarXS","nominal_JES","nominal_JER","ABCD_shape","ABCD_rate"]:
#for sys in ["MCSF_renfac_env","MCSF_CSVLF","MCSF_CSVHF","MCSF_CSVHFStats1"]:

#for sys in ["nominal_JES","nominal_JER"]:
#for sys in ["ABCD_shape","ABCD_rate"]:
    systs.append(sys)
    systs_avg_max_wtb.append(0.0)
    systs_avg_max_ntb.append(0.0)
    systs_avg_min_wtb.append(1.0)
    systs_avg_min_ntb.append(1.0)
    

#procs="ttH_hbb ttH_hcc ttH_hww ttH_hzz ttH_htt ttH_hgg ttH_hgluglu ttH_hzg ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar singlet wjets zjets ttbarW ttbarZ diboson".split(" ")
#procs="SigZprime15001200_tWb SigZprime20001200_tWb SigZprime25001200_tWb SigZprime15001200_ttZ SigZprime20001200_ttZ SigZprime25001200_ttZ SigZprime15001200_ttH SigZprime20001200_ttH SigZprime25001200_ttH ttbar QCDMadgraph".split(" ")
#procs="SigZprime15001200_tWb SigZprime20001200_tWb SigZprime25001200_tWb SigZprime15001200_ttZ SigZprime20001200_ttZ SigZprime25001200_ttZ SigZprime15001200_ttH SigZprime20001200_ttH SigZprime25001200_ttH ttbar".split(" ")


procs="ttbar QCDMadgraph".split(" ")
##procs="QCDMadgraph".split(" ")


#procs=[]
#Signals=["SigGstar1500800","SigGstar15001000","SigGstar15001300","SigGstar17501300","SigGstar20001000","SigGstar20001300","SigGstar20001500","SigGstar22501300","SigGstar22501500","SigGstar25001300","SigGstar25001500","SigGstar25001800","SigGstar27501500","SigGstar30001500","SigGstar30001800","SigGstar30002100","SigGstar35001800","SigGstar35002100","SigGstar35002500","SigGstar40002100","SigGstar40002500","SigGstar40003000"]
#for i in Signals:
    #for channel in ["tWb","ttZ","ttH"]:
        #for width in ["Nar","Wid"]:
            #if i=="SigGstar20001300" and channel=="ttH" and width=="Nar":
                #continue
            #if i=="SigGstar40003000" and channel=="ttZ" and width=="Nar":
                #continue
            #procs.append(i+"_"+channel+width)


#print procs

inf=ROOT.TFile(infname,"READ")

name=outname
if not os.path.exists(name+"SystShapes"):
    os.makedirs(name+"SystShapes")
    
buff=ROOT.TCanvas("buff","buff",800,600)
buff.Print(name+'.pdf[')





counter=0
#for c in cats:
  #print c

  #for p in procs:
    #firstnom=inf.Get(p+"_"+ABCDversion+"_"+c+"_"+ABCDversion+"_nominal")
    #for s,smin,smax in zip(systs,systs_avg_min,systs_avg_max):
        

for s in systs:
  for p in procs:
    systavgmax_wtb=0
    systavgmin_wtb=0
    systavgmax_ntb=0
    systavgmin_ntb=0
    systavgcount=0
    for c in cats:
      firstnom=inf.Get(p+"_"+ABCDversion+"_"+c+"_"+ABCDversion+"_nominal")
      print p+"_"+ABCDversion+"_"+c+"_"+ABCDversion+"_nominal"
              
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
            #raw_input()
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
      nom.SetLineWidth(4)
      if up!=None and down!=None:
	up.SetLineColor(ROOT.kRed)
	up.SetTitle("up")
	down.SetTitle("down")
	down.SetLineColor(ROOT.kGreen+3)
        up.SetLineWidth(4)
        down.SetLineWidth(4)
        
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
	avup=0
	avdown=0
	nnonemptybins=0
	for i in range(nom.GetNbinsX()):
          if nom.GetBinContent(i)>0:
            if maxdiff<abs((nom.GetBinContent(i)-up.GetBinContent(i))/float(nom.GetBinContent(i))):
                maxdiff=abs((nom.GetBinContent(i)-up.GetBinContent(i))/float(nom.GetBinContent(i)))
            if maxdiff<abs((nom.GetBinContent(i)-down.GetBinContent(i))/float(nom.GetBinContent(i))):
                maxdiff=abs((nom.GetBinContent(i)-down.GetBinContent(i))/float(nom.GetBinContent(i)))
                
            if mindiff>abs((nom.GetBinContent(i)-up.GetBinContent(i))/float(nom.GetBinContent(i))):
                mindiff=abs((nom.GetBinContent(i)-up.GetBinContent(i))/float(nom.GetBinContent(i)))
            if mindiff>abs((nom.GetBinContent(i)-down.GetBinContent(i))/float(nom.GetBinContent(i))):
                mindiff=abs((nom.GetBinContent(i)-down.GetBinContent(i))/float(nom.GetBinContent(i)))
            nnonemptybins=nnonemptybins+1
            avup=avup+abs((nom.GetBinContent(i)-up.GetBinContent(i))/float(nom.GetBinContent(i)))
            avdown=avdown+abs((nom.GetBinContent(i)-up.GetBinContent(i))/float(nom.GetBinContent(i)))
        
        avup=avup/float(nnonemptybins)
        avdown=avdown/float(nnonemptybins)
  
          #nom.SetBinContent(i,nom.GetBinContent(i)*(50.0/nom.GetXaxis().GetBinWidth(i)))  
          #up.SetBinContent(i,up.GetBinContent(i)*(50.0/up.GetXaxis().GetBinWidth(i))) 
          #down.SetBinContent(i,down.GetBinContent(i)*(50.0/down.GetXaxis().GetBinWidth(i)))  
            
            
	maxval=max(nom.GetMaximum(), max(up.GetMaximum(),down.GetMaximum()))
	nom.SetMaximum(1.5*maxval)
	#nom.SetTitleSize(0.0)
	nom.Draw("histo")
	#nom.SetTitle(p+"_"+c+" "+s)
	nom.SetTitle("")
	
	Xaxistitle="m(Z') in GeV"
    
        cat=nom.GetName()
        print cat
        #raw_input()
        if ("CatA") in c:
            if ("withtop") in c:
                Xaxistitle="Reg. A (2 b-tag), m(Z') in GeV"
            else:
                Xaxistitle="Reg. A (1 b-tag), m(Z') in GeV"
        if ("CatB") in c:
            if ("withtop") in c:
                Xaxistitle="Reg. B (2 b-tag), m(Z') in GeV"
            else:
                Xaxistitle="Reg. B (1 b-tag), m(Z') in GeV"
        if ("CatC") in c:
            if ("withtop") in c:
                Xaxistitle="Reg. C (2 b-tag), m(Z') in GeV"
            else:
                Xaxistitle="Reg. C (1 b-tag), m(Z') in GeV"
        if ("CatD") in c:
            if ("withtop") in c:
                Xaxistitle="Reg. D (2 b-tag), m(Z') in GeV"
            else:
                Xaxistitle="Reg. D (1 b-tag), m(Z') in GeV"


	
	nom.GetXaxis().SetTitle(Xaxistitle)
	nom.GetXaxis().SetTitleSize(0.06)
	nom.GetYaxis().SetTitle("Events")
	nom.GetYaxis().SetTitleSize(0.08)
	nom.GetYaxis().SetLabelSize(0.06)
	nom.GetXaxis().SetLabelSize(0.06)
	
	#up.SetTitleSize(0.0)
	#down.SetTitleSize(0.0)
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
            maxdifftemp=maxdiff
            if maxdifftemp<0.1:
                maxdifftemp=0.1
            line.GetYaxis().SetRangeUser((1.0-1.2*round(maxdifftemp,1)),(1.0+1.2*round(maxdifftemp,1)))
            line.GetYaxis().SetTitle('#frac{syst}{nominal}')
            line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
            line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.4)
            line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
            line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*1.5)
            #line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*4)
            #line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*4)
            #line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
            #line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*1.5)
            line.GetYaxis().SetTitleOffset(0.6)
            line.GetYaxis().SetNdivisions(103)
            for i in range(line.GetNbinsX()+1):
                line.SetBinContent(i,1)
                line.SetBinError(i,0)
            line.SetLineWidth(1)
            #line.SetTitleSize(0.0)
            line.DrawCopy('histo')
            for hist in [up,down]:
                ratio=hist.Clone()
                ratio.Divide(nom)
                ratio.SetTitle('')
                #ratio.SetTitleSize(0.0)
                ratio.DrawCopy('histoSame')
            canvas.cd(1)
        canvas.Update()
		
		
	canvas.SetTitle(p+"_"+c+" "+s)
	#canvas.BuildLegend()
	legend=ROOT.TLegend()
	legend.SetX1NDC(0.15)
	legend.SetX2NDC(0.95)
	legend.SetY1NDC(0.6)
	legend.SetY2NDC(0.88)
	legend.SetBorderSize(0);
	legend.SetLineStyle(0);
	legend.SetTextFont(42);
	legend.SetTextSize(0.05);
	legend.SetFillStyle(0);	
	
	if "ttbar" in p:
            pnew="Top Background,"
	elif "QCD" in p:
            pnew="QCD,"
        else:
            pnew=p
        
        if "CatA" in c:
            if "withtop" in c:    
                cnew="RegA (2 b-tag),"
            if "notop" in c:    
                cnew="RegA (1 b-tag),"
        if "CatB" in c:
            if "withtop" in c:    
                cnew="RegB (2 b-tag),"
            if "notop" in c:    
                cnew="RegB (1 b-tag),"
        if "CatC" in c:
            if "withtop" in c:    
                cnew="RegC (2 b-tag),"
            if "notop" in c:    
                cnew="RegC (1 b-tag),"
        if "CatD" in c:
            if "withtop" in c:    
                cnew="RegD (2 b-tag),"
            if "notop" in c:    
                cnew="RegD (1 b-tag),"                        
            
	#if doKStest:
	  #legend.AddEntry(nom,pnew+" nominal (%.2f)" % integNom,"l")
          #legend.AddEntry(up,pnew+" "+s+"Up"+" (%.2f, %.2f), KS-prob. %.2f" % (integUp,fracUp,ksUp) +"","l")
          #legend.AddEntry(down,pnew+" "+s+"Down"+" (%.2f, %.2f), KS-prob. %.2f" % (integDown,fracDown,ksDown) +"","l")
          #legend.AddEntry(0, s+"="+str(round(mindiff,3))+"-"+str(round(maxdiff,3)), "")
	#else:
          #legend.AddEntry(nom,pnew+" nominal (%.2f)" % integNom,"l")
          #legend.AddEntry(up,pnew+" "+s+"Up"+" (%.2f, %.2f" % (integUp,fracUp) +")","l")
          #legend.AddEntry(down,pnew+" "+s+"Down"+" (%.2f, %.2f" % (integDown,fracDown) +")","l")
          #legend.AddEntry(0, "relative uncertainty="+str(round(mindiff,3))+"-"+str(round(maxdiff,3)), "")
          
	if doKStest:
	  legend.AddEntry(nom,pnew+" nominal","l")
          legend.AddEntry(up,pnew+" "+s+"Up","l")
          legend.AddEntry(down,pnew+" "+s+"Down","l")
          if maxdiff<0.001:
            legend.AddEntry(0, "relative uncertainty="+str(round(mindiff,3)*100)+"%-(<0.1)%", "")   
          else:
            legend.AddEntry(0, "relative uncertainty="+str(round(mindiff,3)*100)+"%-"+str(round(maxdiff,3)*100)+"%", "")   
          if((avup+avdown)/2.0<0.001):
            legend.AddEntry(0, "avg. rel. uncertainty<0.1%", "")          
          else:    
            legend.AddEntry(0, "avg. rel. uncertainty="+str(round((avup+avdown)/2.0,3)*100)+"%", "")          
	else:
          legend.AddEntry(nom,pnew+" nominal","l")
          legend.AddEntry(up,pnew+" "+s+"Up","l")
          legend.AddEntry(down,pnew+" "+s+"Down","l")
          legend.AddEntry(0, "relative uncertainty="+str(round(mindiff,3)*100)+"%-"+str(round(maxdiff,3)*100)+"%", "")          
          legend.AddEntry(0, "avg. rel. uncertainty="+str(round((avup+avdown)/2.0,3)*100)+"%", "")          
          
	legend.Draw()
        if not os.path.exists(name+"SystShapes/"+p):
            os.makedirs(name+"SystShapes/"+p)
            
            
        cms,info = GetCMSandInfoLabels()
        cms.Draw("same")
        info.Draw("same")                
            
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
        systavgcount=systavgcount+1
        if "withtop" in c:
            systavgmax_wtb=systavgmax_wtb+(avup+avdown)/2.0
            systavgmin_wtb=systavgmin_wtb+(avup+avdown)/2.0
        else:
            systavgmax_ntb=systavgmax_ntb+(avup+avdown)/2.0
            systavgmin_ntb=systavgmin_ntb+(avup+avdown)/2.0
    systavgmax_wtb=systavgmax_wtb/float(systavgcount)
    systavgmax_ntb=systavgmax_ntb/float(systavgcount)
    systavgmin_wtb=systavgmin_wtb/float(systavgcount)
    systavgmin_ntb=systavgmin_ntb/float(systavgcount)
    
        
    
            
    if systavgmin_wtb<systs_avg_min_wtb[systs.index(s)]:
            systs_avg_min_wtb[systs.index(s)]=systavgmin_wtb
    if systavgmax_wtb>systs_avg_max_wtb[systs.index(s)]:
            systs_avg_max_wtb[systs.index(s)]=systavgmax_wtb
            
    if systavgmin_ntb<systs_avg_min_ntb[systs.index(s)]:
            systs_avg_min_ntb[systs.index(s)]=systavgmin_ntb
    if systavgmax_ntb>systs_avg_max_ntb[systs.index(s)]:
            systs_avg_max_ntb[systs.index(s)]=systavgmax_ntb
            
print "syst       2 btag       1 btag"
for s,i,j,k,l in zip(systs,systs_avg_min_wtb, systs_avg_max_wtb,systs_avg_min_ntb, systs_avg_max_ntb):
    print s,":  ",str(round(i*100.0,2)), "-",str(round(j*100.0,2)),"  ",str(round(k*100.0,2)),"-",str(round(l*100.0,2)) 
                        
buff.Print(name+'.pdf]')
	
#exit(0)

