import sys
import ROOT
ROOT.gDirectory.cd('PyROOT:/')
ROOT.gROOT.SetBatch(True)

cats=["ljets_j4_t2","ljets_j5_t2","ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t2","ljets_jge6_t3","ljets_jge6_tge4",]
procs=['ttH','ttH_hbb', 'ttH_hcc', 'ttH_hww', 'ttH_hzz', 'ttH_htt', 'ttH_hgg', 'ttH_hgluglu', 'ttH_hzg', 'ttbarOther', 'ttbarPlusB', 'ttbarPlus2B', 'ttbarPlusBBbar', 'ttbarPlusCCbar', 'singlet', 'wjets', 'zjets', 'ttbarW', 'ttbarZ', 'diboson']

#print procs

groups=[["LF",['ttH_hww', 'ttH_hzz', 'ttH_htt', 'ttH_hgg', 'ttH_hgluglu', 'ttH_hzg','ttbarOther','singlet', 'wjets', 'zjets', 'ttbarW', 'ttbarZ', 'diboson']],
	 ["CF",['ttH_hcc','ttbarPlusCCbar']],
	 ["HF",['ttH','ttH_hbb','ttbarPlusB', 'ttbarPlus2B', 'ttbarPlusBBbar']]
	 ]

systs=["CMS_scale_j","CMS_res_j"]
datacardsysts=["CMS_scale_j","CMS_res_j"]

disc="_finaldiscr_"

infiles=sys.argv[1:]

for inf in infiles:
  if ".root" in inf:
    f=ROOT.TFile(inf,"Update")
    for p in procs:
	for c in cats:
	  for s in systs:
	    hnom=f.Get(p+disc+c)
	    holdUp=f.Get(p+disc+c+"_"+s+"Up")
	    holdDown=f.Get(p+disc+c+"_"+s+"Down")
	    if hnom==None or holdUp==None or holdDown==None:
	      print "no histos for ", p+disc+c
	      continue


	    newhUpRate=hnom.Clone()
	    newhDownRate=hnom.Clone()
	    newhUpRate.SetTitle(p+disc+c+"_"+s.replace("CMS_","CMS_"+"rate"+"_")+"Up")
	    newhUpRate.SetName(p+disc+c+"_"+s.replace("CMS_","CMS_"+"rate"+"_")+"Up")
	    newhDownRate.SetTitle(p+disc+c+"_"+s.replace("CMS_","CMS_"+"rate"+"_")+"Down")
	    newhDownRate.SetName(p+disc+c+"_"+s.replace("CMS_","CMS_"+"rate"+"_")+"Down")
	    
	    newhUpShape=holdUp.Clone()
	    newhDownShape=holdDown.Clone()
	    newhUpShape.SetTitle(p+disc+c+"_"+s.replace("CMS_","CMS_"+"shape"+"_")+"Up")
	    newhUpShape.SetName(p+disc+c+"_"+s.replace("CMS_","CMS_"+"shape"+"_")+"Up")
	    newhDownShape.SetTitle(p+disc+c+"_"+s.replace("CMS_","CMS_"+"shape"+"_")+"Down")
	    newhDownShape.SetName(p+disc+c+"_"+s.replace("CMS_","CMS_"+"shape"+"_")+"Down")	    
	    
	    if newhUpShape.Integral()==0:
	      print "zero integral for ", newhUpShape
	    else:
	      newhUpShape.Scale(hnom.Integral()/newhUpShape.Integral())
	    if newhDownShape.Integral()==0:
	      print "zero integral for ", newhUpShape
	    else:
	      newhDownShape.Scale(hnom.Integral()/newhDownShape.Integral())
	    
	    upint=holdUp.Integral()
	    downint=holdDown.Integral()
	    nomint=hnom.Integral()
	    differenceUp=abs(upint-nomint)
	    differenceDown=abs(downint-nomint)
	    symdiff=max(differenceDown,differenceUp)
	    
	    if nomint==0:
	      newhUpRate.Scale(0.0)
	      newhDownRate.Scale(0.0)
	    else:
	      if differenceUp>differenceDown:
		if upint>nomint:
		  newhUpRate.Scale((nomint+symdiff)/nomint)
		  newhDownRate.Scale((nomint-symdiff)/nomint)
		else:
		  newhUpRate.Scale((nomint-symdiff)/nomint)
		  newhDownRate.Scale((nomint+symdiff)/nomint)
	      else:
		if downint>nomint:
		  newhUpRate.Scale((nomint-symdiff)/nomint)
		  newhDownRate.Scale((nomint+symdiff)/nomint)
		else:
		  newhUpRate.Scale((nomint+symdiff)/nomint)
		  newhDownRate.Scale((nomint-symdiff)/nomint)
	    #check for negative bins
	    for ibin in range(newhUpRate.GetNbinsX()):
	      if newhUpRate.GetBinContent(ibin+1)<0:
		newhUpRate.SetBinContent(ibin+1,0.0001)
	    for ibin in range(newhDownRate.GetNbinsX()):
	      if newhDownRate.GetBinContent(ibin+1)<0:
		newhDownRate.SetBinContent(ibin+1,0.0001)
	    
	    
	    newhUpRate.Write()
	    newhDownRate.Write()
	    newhUpShape.Write()
	    newhDownShape.Write()
	    #print "wrote ", newhUpRate
	    #print "wrote ", newhDownRate
	    #print "wrote ", newhUpShape
	    #print "wrote ", newhDownShape
	    
    f.Close()

  else:
    infl=open(inf,"r")
    outf=open("JECsym_"+inf,"w")
    inlist=list(infl)
    infprocs=[]
    for line in inlist:
      if "process" in line and infprocs==[]:
	print "found process line"
	sl=line.replace("\n","").replace("\t","").replace("  "," ").split(" ")
	print sl
	for pl in sl[1:]:
	  infprocs.append(pl)
	print infprocs
      # now replace jes
      foundOne=False
      for s in datacardsysts:
	  if s in line:
	    foundOne=True
      if foundOne:
	for s in datacardsysts:
	  if s in line:
	    sl=line.replace("\n","").replace("\t","").replace("  "," ").split(" ")
	    print sl
	    newline=sl[0].replace("CMS_","CMS_"+"rate"+"_")+" "+sl[1]
	    for im,m in enumerate(sl[2:]):
		  if m=="-":
		    newline+=" "+"-"
		  else:
		    newline+=" "+"1"
	    newline+="\n"
	    print newline
	    outf.write(newline)
	    newline=sl[0].replace("CMS_","CMS_"+"shape"+"_")+" "+sl[1]
	    for im,m in enumerate(sl[2:]):
		if m=="-":
		    newline+=" "+"-"
		else:
		    newline+=" "+"1"
	    newline+="\n"
	    print newline
	    outf.write(newline)
	      
      else:
	outf.write(line)