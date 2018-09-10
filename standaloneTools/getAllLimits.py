import sys
import json
import ROOT
from subprocess import call

nameMap={
"ljets_jge6_tge4_hdecay": "L+J #geq 6 jets, #geq 4 b-tags",
"ljets_jge6_tge4_low_hdecay": "L+J #geq 6 jets, #geq 4 b-tags low BDT",
"ljets_jge6_tge4_high_hdecay": "L+J #geq 6 jets, #geq 4 b-tags high BDT",
"ljets_jge6_t3_hdecay": "L+J #geq 6 jets, 3 b-tags",
"ljets_jge6_t3_low_hdecay": "L+J #geq 6 jets, 3 b-tags low BDT",
"ljets_jge6_t3_high_hdecay": "L+J #geq 6 jets, 3 b-tags high  BDT",
"ljets_j5_tge4_hdecay": "L+J 5 jets, #geq 4 b-tags",
"ljets_j5_tge4_low_hdecay": "L+J 5 jets, #geq 4 b-tags low BDT",
"ljets_j5_tge4_high_hdecay": "L+J 5 jets, #geq 4 b-tags high BDT",
"ljets_j4_t4_hdecay": "L+J 4 jets, 4 b-tags",
"ljets_j4_t4_low_hdecay": "L+J 4 jets, 4 b-tags low BDT",
"ljets_j4_t4_high_hdecay": "L+J 4 jets, 4 b-tags high BDT",
"ljets_j5_t3_hdecay": "L+J 4 jets, 3 b-tags",
"ljets_j4_t3_hdecay": "L+J 5 jets, 3 b-tags",
"ljets_jge6_t2_hdecay": "L+J #geq 6 jets, 2 b-tags",
"dl_3j3t": "DL 3 jets, 3 b-tags ",
"dl_ge4j3_both": "DL #geq 4 jets, 3 b-tags",
"dl_ge4j3t_high": "DL #geq 4 jets, 3 b-tags high BDT",
"dl_ge4j3t_low": "DL #geq 4 jets, 3 b-tags low BDT",
"dl_ge4jge4t_both": "DL #geq 4 jets, #geq 4 b-tags",
"dl_ge4jge4t_high": "DL #geq 4 jets, #geq 4 b-tags high BDT",
"dl_ge4jge4t_low": "DL #geq 4 jets, #geq 4  b-tags low BDT",
"DL_BDTonly": "DL BDT-only",
"DL_2D": "DL 2D",
"SL_BDTonly": "L+J BDT-only",
"SL_2D": "L+J 2D",
"combined_2D": "DL+L+J combined 2D",
"combined_BDTonly": "DL+L+J combined BDT-only",
}

resultObject={
  "nchannels": 0,
  "cat_names":[],
  "obs":[],
  "upper1sig":[],
  "lower1sig":[],
  "upper2sig":[],
  "lower2sig":[],
  "expected":[],
  }

def readLimit(fn='higgsCombineTest.Asymptotic.mH125.root'):
  f=ROOT.TFile(fn)
  t=f.Get('limit')
  up=-1.
  down=-1.
  upTwo=-1.
  downTwo=-1.
  limit=-1.
  for e in t:
    if e.quantileExpected>0.1 and e.quantileExpected<0.2: 
      down = e.limit
    elif e.quantileExpected==0.5: 
      limit= e.limit
    elif e.quantileExpected>0.8 and e.quantileExpected<0.9: 
      up = e.limit
    elif e.quantileExpected>0.0 and e.quantileExpected<0.1: 
      downTwo= e.limit
    elif e.quantileExpected>0.1 and e.quantileExpected<1.0: 
      upTwo = e.limit


  f.Close()
  return downTwo, down,limit,up, upTwo

resfile=open("results.txt","w")
limit_cats=[]
infilenames=sys.argv[1:]
for card in infilenames:
  cmd='combine -M Asymptotic --minosAlgo stepping -m 125 --run="blind" '+card
  call(cmd,shell=True) 
  d2, d1, m, u1, u2 = readLimit('higgsCombineTest.Asymptotic.mH125.root')
  err2Up=u2-m
  err1Up=u1-m
  err2Down=m-d2
  err1Down=m-d1
  texString="$%.1f^{+%.1f}_{-%.1f}$" % ( m, err1Up, err1Down)
  
  lims=[d2, d1, m , u1, u2, err2Up, err1Up, m , err1Down, err2Down]
  limstrings=[]
  for i in lims:
    limstrings.append(str(i))
  limstrings.append(texString)
  print limstrings
  outstr=card.replace(".txt","").replace(".root","")+" "+" ".join(limstrings)
  print outstr
  cardName=card.replace(".txt","").replace(".root","")
  resfile.write(outstr+"\n")
  
  # add to res resultObject
  transCatName=cardName
  for cat in nameMap:
    if cat in cardName:
      transCatName=nameMap[cat]
  resultObject["nchannels"]+=1
  resultObject["cat_names"].append(transCatName)
  resultObject["obs"].append(0.0)
  resultObject["expected"].append(m)
  resultObject["upper1sig"].append(err1Up)
  resultObject["lower1sig"].append(err1Down)
  resultObject["upper2sig"].append(err2Up)
  resultObject["lower2sig"].append(err2Down)
  
  
  #limit_cats.append([card.replace(".txt",""),readLimit('higgsCombineTest.Asymptotic.mH125.root')])
  #print limit_cats

resfile.close()

jo=json.dumps(resultObject)
jsonfile=open("results.json","w")
jsonfile.write(jo)
jsonfile.close()

