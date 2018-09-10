import ROOT
import sys
import json
from namingMaps import *

infile=sys.argv[1]
mode=sys.argv[2]
outname=sys.argv[3]

procs={
  "ttbarPlusBBbar": { 
    "name": "tt+bb",
    "histos": ["ttbarPlusBBbar"],
    "colors": ROOT.kRed+3,
    },
  "ttbarPlusB": { 
    "name": "tt+b",
    "histos": ["ttbarPlusB"],
    "colors": ROOT.kRed-2,
    },
  "ttbarPlus2B": { 
    "name": "tt+2b",
    "histos": ["ttbarPlus2B"],
    "colors": ROOT.kRed+2,
    },
  "ttbarPlusCCbar": { 
    "name": "tt+cc",
    "histos": ["ttbarPlusCCbar"],
    "colors": ROOT.kRed+1,
    },
  "ttbarOther": { 
    "name": "tt+lf",
    "histos": ["ttbarOther"],
    "colors": ROOT.kRed-7,
    },  
  "ttH": { 
    "name": "ttH",
    "histos": ["ttH_hbb","ttH_hcc","ttH_htt","ttH_hgg","ttH_hgluglu","ttH_hww","ttH_hzz","ttH_hzg"],
    "colors": ROOT.kBlue-4,
    },    
  "EWK": { 
  "name": "EWK",
  "histos": ["zjets","wjets","diboson"],
  "colors": ROOT.kGray+1,
  }, 
  "tandttV": { 
  "name": "t/tt+V",
  "histos": ["singlet","ttbarW","ttbarZ"],
  "colors": ROOT.kMagenta,
  },
}
  
catsDLUnsplit=[
"dl_3j3t_BDT",
"dl_ge4j3t_BDT",
"dl_ge4jge4t_BDT",
]

catsDLSplit=[
"dl_ge4j3t_high_BDT",
"dl_ge4j3t_low_BDT",
"dl_ge4jge4t_high_BDT",
"dl_ge4jge4t_low_BDT",
"dl_3j3t_BDT",
]

catsLJUnsplit=[
"finaldiscr_ljets_jge6_t2",
"finaldiscr_ljets_j4_t3",
"finaldiscr_ljets_j4_t4",
"finaldiscr_ljets_j5_t3",
"finaldiscr_ljets_j5_tge4",
"finaldiscr_ljets_jge6_t3",
"finaldiscr_ljets_jge6_tge4",
]

catsLJSplit=[
"finaldiscr_ljets_j4_t3",
"finaldiscr_ljets_j4_t4_high",
"finaldiscr_ljets_j4_t4_low",
"finaldiscr_ljets_j5_t3",
"finaldiscr_ljets_j5_tge4_high",
"finaldiscr_ljets_j5_tge4_low",
"finaldiscr_ljets_jge6_t3_high",
"finaldiscr_ljets_jge6_t3_low",
"finaldiscr_ljets_jge6_tge4_high",
"finaldiscr_ljets_jge6_tge4_low",
]


results={}

#"processes": [],
  #"colors": [],
  #"yields": [],
  
if mode=="DLUNSPLIT":
  rf=ROOT.TFile(infile,"READ")
  for cat in catsDLUnsplit:
    res={
    "processes": [],
    "colors": [],
    "yields": [],
    }
    for proc in procs:
      total=0.0
      for subproc in procs[proc]["histos"]:
        h=rf.Get(cat+"/"+subproc)
        if h==None:
          continue
        else:
          total+=h.Integral()
      res["processes"].append(procs[proc]["name"])
      res["colors"].append(procs[proc]["colors"])
      res["yields"].append(total)
      print cat, proc, total
    transCatName=cat
    if cat in cateNameMap:
      transCatName=cateNameMap[cat]
    results[transCatName]=res
elif mode=="DLSPLIT":
  rf=ROOT.TFile(infile,"READ")
  for cat in catsDLSplit:
    res={
    "processes": [],
    "colors": [],
    "yields": [],
    }
    for proc in procs:
      total=0.0
      for subproc in procs[proc]["histos"]:
        h=rf.Get(cat+"/"+subproc)
        if h==None:
          continue
        else:
          total+=h.Integral()
      res["processes"].append(procs[proc]["name"])
      res["colors"].append(procs[proc]["colors"])
      res["yields"].append(total)
      print cat, proc, total
    transCatName=cat
    if cat in cateNameMap:
      transCatName=cateNameMap[cat]
    results[transCatName]=res
elif mode=="LJUNSPLIT":
  rf=ROOT.TFile(infile,"READ")
  for cat in catsLJUnsplit:
    res={
    "processes": [],
    "colors": [],
    "yields": [],
    }
    for proc in procs:
      total=0.0
      for subproc in procs[proc]["histos"]:
        h=rf.Get(subproc+"_"+cat)
        if h==None:
          continue
        else:
          total+=h.Integral()
      res["processes"].append(procs[proc]["name"])
      res["colors"].append(procs[proc]["colors"])
      res["yields"].append(total)
      print cat, proc, total

    transCatName=cat
    if cat in cateNameMap:
      transCatName=cateNameMap[cat]
    results[transCatName]=res

elif mode=="LJSPLIT":
  rf=ROOT.TFile(infile,"READ")
  for cat in catsLJSplit:
    res={
    "processes": [],
    "colors": [],
    "yields": [],
    }
    for proc in procs:
      total=0.0
      for subproc in procs[proc]["histos"]:
        h=rf.Get(subproc+"_"+cat)
        if h==None:
          continue
        else:
          total+=h.Integral()
      res["processes"].append(procs[proc]["name"])
      res["colors"].append(procs[proc]["colors"])
      res["yields"].append(total)
      print cat, proc, total
    transCatName=cat
    if cat in cateNameMap:
      transCatName=cateNameMap[cat]
    results[transCatName]=res
else:
  print "unknown mode"
  exit(1)

print results


jo=json.dumps(results)
jsonfile=open(outname+".json","w")
jsonfile.write(jo)
jsonfile.close()






    
    
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  