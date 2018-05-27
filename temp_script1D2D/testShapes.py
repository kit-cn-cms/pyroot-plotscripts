import sys
import ROOT
ROOT.gDirectory.cd('PyROOT:/')
ROOT.gROOT.SetBatch(True)

infname=sys.argv[1]
#outname=sys.argv[2]

inf=ROOT.TFile(infname,"READ")
#outf=ROOT.TFile(outname,"RECREATE")

systs=['CMS_ttH_Q2scale_ttbarOther', 'CMS_ttH_Q2scale_ttbarPlusB', 'CMS_ttH_Q2scale_ttbarPlus2B', 'CMS_ttH_Q2scale_ttbarPlusBBbar', 'CMS_ttH_Q2scale_ttbarPlusCCbar', 'CMS_ttH_CSVLF', 'CMS_ttH_CSVHF', 'CMS_ttH_CSVHFStats1', 'CMS_ttH_CSVLFStats1', 'CMS_ttH_CSVHFStats2', 'CMS_ttH_CSVLFStats2', 'CMS_ttH_CSVCErr1', 'CMS_ttH_CSVCErr2', 'CMS_scale_j', 'CMS_ttH_PU', 'CMS_res_j', 'CMS_ttH_eff_mu', 'CMS_ttH_eff_el', 'CMS_ttH_ljets_Trig_mu', 'CMS_ttH_ljets_Trig_el']

#systs=['CMS_ttH_eff_mu', ]


cats=["ljets_j4_t2","ljets_j5_t2","ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t2","ljets_jge6_t3","ljets_jge6_tge4",]
#cats=["ljets_j4_t3",]


procs="ttH_hbb ttH_hcc ttH_hww ttH_hzz ttH_htt ttH_hgg ttH_hgluglu ttH_hzg ttbarOther ttbarPlusB ttbarPlus2B ttbarPlusBBbar ttbarPlusCCbar singlet wjets zjets ttbarW ttbarZ diboson".split(" ")
print procs

disc="_finaldiscr_"

raw_input()

for s in systs:
  for c in cats:
    #hbase=inf.Get("ttbarOther"+disc+c)
  #print hbase
  #nSetToZero=0
    #nBins=hbase.GetNbinsX()
    for p in procs:
      hnom=inf.Get(p+disc+c)
      hup=inf.Get(p+disc+c+"_"+s+"Up")
      hdown=inf.Get(p+disc+c+"_"+s+"Down")
      if hup==None or hdown==None:
	  #print "DID not find histograms for ", p+disc+c+"_"+s
	  a=2
      else:
	  print c, p, s, hnom.Integral(), hup.Integral(), hdown.Integral()
	  if ( hnom.Integral()-hup.Integral() > 0 and hnom.Integral()-hdown.Integral()>0) or ( hnom.Integral()-hup.Integral() < 0 and hnom.Integral()-hdown.Integral()<0):
	    print "WARNGING"
	  #if hnom.Integral()<=0 and (hup.Integral()>0 or hdown.Integral()>0):
	    #print "WARNING nominal is zero but shapes are not ", c, p, s, iBin, hup.Integral(), hdown.Integral()
	  #else:
	    #if ( hnom.Integral()-hup.Integral() > 0 and hnom.Integral()-hdown.Integral()>0) or ( hnom.Integral()-hup.Integral() < 0 and hnom.Integral()-hdown.Integral()<0):
	      #print "SAME SIDE SYST", c, p, s, iBin, hnom.Integral(), hup.Integral(), hdown.Integral()
	    











