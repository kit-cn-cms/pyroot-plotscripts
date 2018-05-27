import sys
import ROOT

inf=sys.argv[1]
#indc=sys.argv[2]

systs=['CMS_res_j', 'CMS_scale_j', 'CMS_ttH_CSVCErr1', 'CMS_ttH_CSVCErr2', 'CMS_ttH_CSVHF', 'CMS_ttH_CSVHFStats1', 'CMS_ttH_CSVHFStats2', 'CMS_ttH_CSVLF', 'CMS_ttH_CSVLFStats1', 'CMS_ttH_CSVLFStats2', 'CMS_ttH_PSscale_ttbarOther', 'CMS_ttH_PSscale_ttbarPlus2B', 'CMS_ttH_PSscale_ttbarPlusB', 'CMS_ttH_PSscale_ttbarPlusBBbar', 'CMS_ttH_PSscale_ttbarPlusCCbar', 'CMS_ttH_PU', 'CMS_ttH_Q2scale_ttbarOther', 'CMS_ttH_Q2scale_ttbarPlus2B', 'CMS_ttH_Q2scale_ttbarPlusB', 'CMS_ttH_Q2scale_ttbarPlusBBbar', 'CMS_ttH_Q2scale_ttbarPlusCCbar', 'CMS_ttH_eff_el', 'CMS_ttH_eff_mu', 'CMS_ttH_ljets_Trig_el', 'CMS_ttH_ljets_Trig_mu']

f=ROOT.TFile(inf,"READ")

bkgProcs=["ttbarOther","ttbarPlus2B","ttbarPlusB","ttbarPlusCCbar","ttbarPlusBBbar"]
#bkgProcs=["ttbarPlus2B","ttbarPlusB","ttbarPlusBBbar"]
#bkgProcs=["ttbarPlusCCbar",]
#bkgProcs=["ttbarOther",]

cats=["ljets_j4_t4"]

discr="finaldiscr"

results=[]

for c in cats:
  ttH=f.Get("ttH_"+discr+"_"+c)
  #print ttH
  bkgs=[]
  for p in bkgProcs:
    print p+"_"+discr+"_"+c
    bkgs.append(f.Get(p+"_"+discr+"_"+c))
    t=f.Get(p+"_"+discr+"_"+c)
    #print t
  #print bkgs
  stack=bkgs[0].Clone()
  for b in bkgs[1:]:
    stack.Add(b)
  nomttH=ttH.Integral()
  nomBkg=stack.Integral()
  
  for sys in systs:
    print sys
    ttHUp=f.Get("ttH_"+discr+"_"+c+"_"+sys+"Up")
    ttHDown=f.Get("ttH_"+discr+"_"+c+"_"+sys+"Down")
    #print ttHUp, ttHUp
    if ttHUp==None:
      print "no sys for ttH"
      ttHUp=f.Get("ttH_"+discr+"_"+c)
      ttHDown=f.Get("ttH_"+discr+"_"+c)
    
    bkgsUp=[]
    bkgsDown=[]
    
    for p in bkgProcs:
      if "Q2scale" in sys or "PSscale" in sys:
	print sys, p
	if p!=sys.split("_")[-1]:
	  print "add nom"
	  bkgsUp.append(f.Get(p+"_"+discr+"_"+c))
          bkgsDown.append(f.Get(p+"_"+discr+"_"+c))
        else:
	  print "add sys"
	  bkgsUp.append(f.Get(p+"_"+discr+"_"+c+"_"+sys+"Up"))
          bkgsDown.append(f.Get(p+"_"+discr+"_"+c+"_"+sys+"Down"))
      else:    
        bkgsUp.append(f.Get(p+"_"+discr+"_"+c+"_"+sys+"Up"))
        bkgsDown.append(f.Get(p+"_"+discr+"_"+c+"_"+sys+"Down"))
      #print bkgsUp
      #print bkgsDown
      stackUp=bkgsUp[0].Clone()
      for b in bkgsUp[1:]:
	stackUp.Add(b)
      stackDown=bkgsDown[0].Clone()
      for b in bkgsDown[1:]:
	stackDown.Add(b)
    downRatettH=ttHDown.Integral()
    upRatettH=ttHUp.Integral()
    downRateBkg=stackDown.Integral()
    upRateBkg=stackUp.Integral()
    print nomttH, downRatettH, upRatettH, nomBkg, downRateBkg, upRateBkg
    upRatioTTH=upRatettH/nomttH
    downRatioTTH=downRatettH/nomttH
    upRatioBkg=upRateBkg/nomBkg
    downRatioBkg=downRateBkg/nomBkg
    
    s=sys+"  &  "	
    if upRatioBkg>=1:
      s+="+"+str(round(100*(upRatioBkg-1.0),1))
    else:
      s+=""+str(round(100*(upRatioBkg-1.0),1))
    s+="/"
    if downRatioBkg>=1:
      s+="+"+str(round(100*(downRatioBkg-1.0),1))
    else:
      s+=""+str(round(100*(downRatioBkg-1.0),1))
    
    s+="  &  " 
    
    if upRatioTTH>=1:
      s+="+"+str(round(100*(upRatioTTH-1.0),1))
    else:
      s+=""+str(round(100*(upRatioTTH-1.0),1))
    s+="/"
    if downRatioTTH>=1:
      s+="+"+str(round(100*(downRatioTTH-1.0),1))
    else:
      s+=""+str(round(100*(downRatioTTH-1.0),1))
    
    s+="\\\\"
    results.append(s)
    
for r in results:
  print r
    
    
    
    
    
    
    
    
    
