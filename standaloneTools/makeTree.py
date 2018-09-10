#DISCLAIMER was in limittools folder
import sys
from subprocess import call
import ROOT

inhistfilename=sys.argv[1]

combinations=[[["ljets_j4_t3"]],
              [["ljets_j5_t3"]],
              [["ljets_jge6_t2"]],
              [["ljets_jge6_t3"]],
              [["ljets_j4_t4_lblr"]],
              [["ljets_j4_t4_hblr"]],
              [["ljets_j4_t4_lblr","ljets_j4_t4_hblr"]],
              [["ljets_j5_tge4_lblr"]],
              [["ljets_j5_tge4_hblr"]],
              [["ljets_j5_tge4_lblr","ljets_j5_tge4_hblr"]],
              [["ljets_jge6_tge4_lblr"]],
              [["ljets_jge6_tge4_hblr"]],
              [["ljets_jge6_tge4_lblr","ljets_jge6_tge4_hblr"]],
              [["ljets_jge6_tge4_lblr","ljets_jge6_tge4_hblr","ljets_j5_tge4_lblr","ljets_j5_tge4_hblr","ljets_j4_t4_lblr","ljets_j4_t4_hblr","ljets_j4_t3","ljets_j5_t3","ljets_jge6_t2","ljets_jge6_t3"]],
             ]

signalsamples=["ttH125_BDT_"]
backgroundsamples=["ttbarOther_BDT_","ttbarPlusBBbar_BDT_","ttbarPlusCCbar_BDT_","ttbarPlusB_BDT_","ttbarPlus2B_BDT_"]

for comb in combinations:
  outdatacardname="datacard_"
  for cat in comb[0]:
    outdatacardname+=cat+"_"
  outdatacardname+=".txt"
  
  catstring=""
  for cat in comb[0]:
    catstring+=cat+" "
  catstring=catstring.rstrip()
#  catstring+="\""

  print catstring
 
  buffname=outdatacardname+"buff"

  call(['mk_datacard_ttbb13TeV','-d', 'BDT','-s','CMS_scale_j','-c',catstring,'-o',outdatacardname ,inhistfilename])
#  call(['grep','-v','CMS_scale_j',buffname,'>',outdatacardname])

  limitfile=open("limit.txt","w")
  call(['combine','-M', 'Asymptotic','-m','125','--minosAlgo','stepping' ,outdatacardname, '--run=blind'],stdout=limitfile)
  limitfile.close()
  limitfile=open("limit.txt","r")
  limitlist=list(limitfile)
  for line in limitlist:
    if "Expected 50.0%:" in line:
      thislimitstring=line.replace("\n","").rsplit(" ",1)[1]
  thislimit=float(thislimitstring)

  signalyield=0.0
  backgroundyield=0.0
  histfile=ROOT.TFile(inhistfilename,"READ")
  for s in signalsamples:
    for cat in comb[0]:
      thishistname=s+cat
      thishist=histfile.Get(thishistname)
      signalyield+=thishist.Integral()
  for s in backgroundsamples:
    for cat in comb[0]:
      thishistname=s+cat
      thishist=histfile.Get(thishistname)
      backgroundyield+=thishist.Integral()
  comb.append(signalyield)
  comb.append(backgroundyield)
  comb.append(thislimit)
#  exit(0)

for comb in combinations:
  combstring=""
  catstring=""
  for cat in comb[0]:
    catstring+=cat+" "
  catstring=catstring.rstrip()

  print ""
  print catstring
  print "S",comb[1]
  print "B",comb[2]
  print "limit",comb[3]



