import sys
import json
import ROOT
import os
import glob
from subprocess import call
from namingMaps import *


def readLimitFromTextFile(textfile=""):
    limit=0.
    limitValdown=0.
    limitValup=0.
    limitValdown2=0.
    limitValup2=0.
    obs=0.
    err2Down=0.
    err1Down=0.
    err2Up=0.
    err1Up=0.
    
    if textfile=="":
      return obs, limit, err2Down, err2Up, err1Down, err1Up
    
    textfile=open(textfile,"r")
    inlist=list(textfile)
    textfile.close()
    for line in inlist:
      if "Expected 16.0" in line:
        limitValdown=float(line.replace("\n","").split(" ")[-1])
      if "Expected 84.0" in line:
        limitValup=float(line.replace("\n","").split(" ")[-1])
      if "Expected 50.0" in line:
        limit=float(line.replace("\n","").split(" ")[-1])
      if "Expected  2.5" in line:
        limitValdown2=float(line.replace("\n","").split(" ")[-1])
      if "Expected 97.5" in line:
        limitValup2=float(line.replace("\n","").split(" ")[-1])
    err2Up=limitValup2-limit
    err1Up=limitValup-limit
    err2Down=limit-limitValdown2
    err1Down=limit-limitValdown
    print obs, limit, limitValdown2, limitValup2, limitValdown, limitValup
    print obs, limit, err2Down, err2Up, err1Down, err1Up
    return obs, limit, err2Down, err2Up, err1Down, err1Up

def dumpToJson(group):
  theName=group["cardnames"][-1]
  print "writing json for ", theName
  
  # sort after limit
  print "unsorted"
  print group
  
  cn=group["cat_names"]
  cc=group["cardnames"]
  exp=group["expected"]
  obs=group["obs"]
  u1=group["upper1sig"]
  u2=group["upper2sig"]
  d1=group["lower1sig"]
  d2=group["lower2sig"]
  zipped=zip(cn,exp,obs,u1,u2,d1,d2,cc)
  zipped.sort(key=lambda x: x[1],reverse=True)
  
  resultObject={
  "nchannels": group["nchannels"],
  "cardnames": zip(*zipped)[7],
  "cat_names":zip(*zipped)[0],
  "obs":zip(*zipped)[2],
  "upper1sig":zip(*zipped)[3],
  "lower1sig":zip(*zipped)[5],
  "upper2sig":zip(*zipped)[4],
  "lower2sig":zip(*zipped)[6],
  "expected":zip(*zipped)[1],
  }
  
  print "sorted"
  print resultObject
  
  jo=json.dumps(resultObject)
  jsonfile=open("results_"+theName+".json","w")
  jsonfile.write(jo)
  jsonfile.close()


inputDirectory=sys.argv[1]



resultGroups={}
for incard in inputCards:
  for gr in inputCards[incard]:
    if not gr in resultGroups:
      resultGroups[gr]={
                        "nchannels": 0,
                        "cat_names":[],
                        "cardnames":[],
                        "obs":[],
                        "upper1sig":[],
                        "lower1sig":[],
                        "upper2sig":[],
                        "lower2sig":[],
                        "expected":[],
                        }
    resultGroups[gr]["cardnames"].append(incard) 
for gr in resultGroups:
  resultGroups[gr]["cardnames"].append(gr)
  resultGroups[gr]["nchannels"]=len(resultGroups[gr]["cardnames"])
  
for gr in resultGroups:
  print ""
  print gr
  print resultGroups[gr]

# loop over groups and read limits
for gr in resultGroups:
  for subgr in resultGroups[gr]["cardnames"]:
    #check existence of indir
    print subgr
    intextfile=""
    indir1=inputDirectory+"/"+"work_"+subgr
    indir2=inputDirectory+"/"+"work_"+prefix+subgr
    if os.path.exists(indir1):
      print "found1 ", indir1
      intextfile=glob.glob(indir1+"/asymplimit*")
    elif os.path.exists(indir2):
      print "found2 ", indir2
      #print indir2+"/asymplimit*"
      intextfile=glob.glob(indir2+"/asymplimit*")
    print intextfile
    if len(intextfile)==0:
      intextfile=[""]
    obs, limit, err2Down, err2Up, err1Down, err1Up = readLimitFromTextFile(intextfile[0])
    resultGroups[gr]["obs"].append(obs)
    resultGroups[gr]["expected"].append(limit)
    resultGroups[gr]["upper1sig"].append(err1Up)
    resultGroups[gr]["lower1sig"].append(err1Down)
    resultGroups[gr]["upper2sig"].append(err2Up)
    resultGroups[gr]["lower2sig"].append(err2Down)
    transCatName=subgr
    if subgr in nameMap:
      transCatName=nameMap[subgr]
      print "found name", transCatName, " for ", subgr
    elif prefix+subgr in nameMap:
      transCatName=nameMap[prefix+subgr]
      print "found name", transCatName, " for ", subgr
    else:
      print "did not find name for ", subgr
      transCatName=subgr
    print transCatName
    resultGroups[gr]["cat_names"].append(transCatName)  

print "writing jsons"
for gr in resultGroups:
  dumpToJson(resultGroups[gr])
    
#resultObject={
  #"nchannels": 0,
  #"cat_names":[],
  #"obs":[],
  #"upper1sig":[],
  #"lower1sig":[],
  #"upper2sig":[],
  #"lower2sig":[],
  #"expected":[],
  #}

#def readLimit(fn='higgsCombineTest.Asymptotic.mH125.root'):
  #f=ROOT.TFile(fn)
  #t=f.Get('limit')
  #up=-1.
  #down=-1.
  #upTwo=-1.
  #downTwo=-1.
  #limit=-1.
  #for e in t:
    #if e.quantileExpected>0.1 and e.quantileExpected<0.2: 
      #down = e.limit
    #elif e.quantileExpected==0.5: 
      #limit= e.limit
    #elif e.quantileExpected>0.8 and e.quantileExpected<0.9: 
      #up = e.limit
    #elif e.quantileExpected>0.0 and e.quantileExpected<0.1: 
      #downTwo= e.limit
    #elif e.quantileExpected>0.1 and e.quantileExpected<1.0: 
      #upTwo = e.limit


  #f.Close()
  #return downTwo, down,limit,up, upTwo

#resfile=open("results.txt","w")
#limit_cats=[]
#infilenames=sys.argv[1:]
#for card in infilenames:
  #cmd='combine -M Asymptotic --minosAlgo stepping -m 125 --run="blind" '+card
  #call(cmd,shell=True) 
  #d2, d1, m, u1, u2 = readLimit('higgsCombineTest.Asymptotic.mH125.root')
  #err2Up=u2-m
  #err1Up=u1-m
  #err2Down=m-d2
  #err1Down=m-d1
  #texString="$%.1f^{+%.1f}_{-%.1f}$" % ( m, err1Up, err1Down)
  
  #lims=[d2, d1, m , u1, u2, err2Up, err1Up, m , err1Down, err2Down]
  #limstrings=[]
  #for i in lims:
    #limstrings.append(str(i))
  #limstrings.append(texString)
  #print limstrings
  #outstr=card.replace(".txt","").replace(".root","")+" "+" ".join(limstrings)
  #print outstr
  #cardName=card.replace(".txt","").replace(".root","")
  #resfile.write(outstr+"\n")
  
  ## add to res resultObject
  #transCatName=cardName
  #for cat in nameMap:
    #if cat in cardName:
      #transCatName=nameMap[cat]
  #resultObject["nchannels"]+=1
  #resultObject["cat_names"].append(transCatName)
  #resultObject["obs"].append(0.0)
  #resultObject["expected"].append(m)
  #resultObject["upper1sig"].append(err1Up)
  #resultObject["lower1sig"].append(err1Down)
  #resultObject["upper2sig"].append(err2Up)
  #resultObject["lower2sig"].append(err2Down)
  
  
  ##limit_cats.append([card.replace(".txt",""),readLimit('higgsCombineTest.Asymptotic.mH125.root')])
  ##print limit_cats

#resfile.close()

#jo=json.dumps(resultObject)
#jsonfile=open("results.json","w")
#jsonfile.write(jo)
#jsonfile.close()

