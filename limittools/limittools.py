import ROOT
import sys
import os
from subprocess import call


class Limitresult:
  def __init__(self,combined,combined_up,combined_down,combined_2up,combined_2down,cats,catlimits,catlimits_up,catlimits_down,catlimits_2up,catlimits_2down):
    self.combined=combined
    self.combined_up=combined_up
    self.combined_down=combined_down
    self.combined_2up=combined_2up
    self.combined_2down=combined_2down
    
    self.cats=cats
    self.catlimits=catlimits
    self.catlimits_up=catlimits_up
    self.catlimits_down=catlimits_down
    self.catlimits_2up=catlimits_2up
    self.catlimits_2down=catlimits_2down
  def dump(self):
    catalias={}
    catalias["ljets_j4_t3"]="= 4 jets, = 3 b-tags"
    catalias["ljets_j4_t4"]="= 4 jets, = 4 b-tags"
    catalias["ljets_j5_t3"]="= 5 jets, = 3 b-tags"
    catalias["ljets_j5_tge4"]="= 5 jets, $\geq$ 4 b-tags"
    catalias["ljets_jge6_t2"]="$\geq$ 6 jets, = 2 b-tags"
    catalias["ljets_jge6_t3"]="$\geq$ 6 jets, = 3 b-tags"
    catalias["ljets_jge6_tge4"]="$\geq$ 6 jets, $\geq$ 4 b-tags"
    catalias["ljets_boosted"]="boosted"
    
    for c in catalias.keys():
      catalias[c+"_high"]=catalias[c]+" high BDT output"
      catalias[c+"_low"]=catalias[c]+" low BDT output"

    print 'combined:',round(self.combined*10)/10.,'^{+'+str(round((self.combined_up-self.combined)*10)/10.)+'}_{'+str(round((self.combined_down-self.combined)*10)/10.)+'}','^{+'+str(round((self.combined_2up-self.combined)*10)/10.)+'}_{'+str(round((self.combined_2down-self.combined)*10)/10.)+'}'
    for cat,limit,limit_up,limit_down,limit_2up,limit_2down in zip(self.cats,self.catlimits,self.catlimits_up,self.catlimits_down,self.catlimits_2up,self.catlimits_2down):
      print catalias[cat]+':',round(limit*10.)/10.,'^{+'+str(round((limit_up-limit)*10)/10.)+'}_{'+str(round((limit_down-limit)*10)/10.)+'}','^{+'+str(round((limit_2up-limit)*10)/10.)+'}_{'+str(round((limit_2down-limit)*10)/10.)+'}'
    

def renameHistos(infname,outfname,sysnames,prune=True):
  print sysnames
  infile=ROOT.TFile(infname,"READ")
  outfile=ROOT.TFile(outfname,"RECREATE")

  keylist=infile.GetListOfKeys()
  
  for key in keylist:
    print key.GetName()
    thisname=key.GetName()
    thish=infile.Get(thisname)
    newname=thisname
    do=True
    #print thisname
    if do and "PSscaleUp" in thisname and "Q2scale" in thisname and thisname[-2:]=="Up":
      #print thish
#     print thisname
      #ttbarOther_CMS_ttH_PSscaleUp_BDT_ljets_j4_t4_low_CMS_ttH_Q2scale_ttbarPlusBUp
      tmp=thisname
      tmp=tmp.replace('_CMS_ttH_PSscaleUp','')
      print 'stripped',tmp
#      raw_input()
      newname=tmp.replace('Q2scale','CombinedScale')
      #print newname
      #raw_input()

    if "PSscaleDown" in thisname and "Q2scale" in thisname and thisname[-4:]=="Down":
  #    print thisname
      #ttbarOther_CMS_ttH_PSscaleUp_BDT_ljets_j4_t4_low_CMS_ttH_Q2scale_ttbarPlusBUp
      tmp=thisname
      tmp=tmp.replace('_CMS_ttH_PSscaleDown','')
   #   print 'stripped',tmp
     # raw_input()
      newname=tmp.replace('Q2scale','CombinedScale')
    #  print newname
      #raw_input()

    if "dummy" in thisname:
      continue
    nsysts=0
    for sys in sysnames:
      if sys in newname:
        newname=newname.replace(sys,"")
        newname+=sys
        nsysts+=1
        
    if nsysts>2:
      continue
    
    #filter histograms for systs not belonging to the samples 
    #for now until we have NNPDF syst for other samples
    if prune:
      if "CMS_ttH_NNPDF" in thisname:
        if thisname.split("_",1)[0]+"_" not in ["ttbarPlus2B_","ttbarPlusB_","ttbarPlusBBbar_","ttbarPlusCCbar_","ttbarOther_"]:
          print "wrong syst: removing histogram", thisname
          continue
      if "CMS_ttH_Q2scale_ttbarOther" in thisname and "ttbarOther"!=thisname.split("_",1)[0]:
        print "wrong syst: removing histogram", thisname
        continue
      if ("CMS_ttH_Q2scale_ttbarPlusBUp" in thisname or "CMS_ttH_Q2scale_ttbarPlusBDown" in thisname ) and "ttbarPlusB"!=thisname.split("_",1)[0] :
        print "wrong syst: removing histogram", thisname
        continue
      if "CMS_ttH_Q2scale_ttbarPlusBBbar" in thisname and "ttbarPlusBBbar"!=thisname.split("_",1)[0] :
        print "wrong syst: removing histogram", thisname
        continue
      if "CMS_ttH_Q2scale_ttbarPlusCCbar" in thisname and "ttbarPlusCCbar"!=thisname.split("_",1)[0] :
        print "wrong syst: removing histogram", thisname
        continue
      if "CMS_ttH_Q2scale_ttbarPlus2B" in thisname and "ttbarPlus2B"!=thisname.split("_",1)[0] :
        print "wrong syst: removing histogram", thisname
        continue
    
#add ttbar type to systematics name for PS scale
    if "CMS_ttH_PSscaleUp" in newname or "CMS_ttH_PSscaleDown" in newname:
      
      ttbartype=""
      if "ttbarOther"==thisname.split("_",1)[0]:
        ttbartype="ttbarOther"
      elif "ttbarPlusB"==thisname.split("_",1)[0] :
        ttbartype="ttbarPlusB"
      elif "ttbarPlusBBbar"==thisname.split("_",1)[0] :
        ttbartype="ttbarPlusBBbar"
      elif "ttbarPlusCCbar"==thisname.split("_",1)[0] :
        ttbartype="ttbarPlusCCbar"
      elif "ttbarPlus2B"==thisname.split("_",1)[0] :
        ttbartype="ttbarPlus2B"
      else:
        print "wrong syst: removing histogram", thisname
        continue
      
      if "CMS_ttH_PSscaleUp" in newname:
        newname=newname.replace("CMS_ttH_PSscaleUp","CMS_ttH_PSscale_"+ttbartype+"Up")
      elif "CMS_ttH_PSscaleDown" in newname:
        newname=newname.replace("CMS_ttH_PSscaleDown","CMS_ttH_PSscale_"+ttbartype+"Down")
      else:
        print "wrong syst: removing histogram", thisname


    #if nsysts ==1 and thish.Integral()<0.0:
      #print "nominal histogram has negativ integral"
        #print thish, thish.Integral()
    if prune:
      nbins=thish.GetNbinsX()
      for ibin in range(nbins):
        if thish.GetBinContent(ibin+1)<0.0:
          print "negative bins in ", thish
          print "setting bin ", ibin+1, "from", thish.GetBinContent(ibin+1), "+-", thish.GetBinError(ibin+1), "to 0+-0"
          thish.SetBinContent(ibin+1,0.0)
          thish.SetBinError(ibin+1,0.0)
  #if "125" in newname:
    #newname=newname.replace("125","")
#    print "changed ", thisname, " to ", newname
    thish.SetName(newname)
    outfile.cd()
    thish.Write()
  
  outfile.Close()
  infile.Close()
  
def mergeHistFiles(infname1,infname2,categoriesToTakeFrom2,outfname):
  infile1=ROOT.TFile(infname1,"READ")
  infile2=ROOT.TFile(infname2,"READ")
  outfile=ROOT.TFile(outfname,"RECREATE")
  
  transferCategories = [(cat,False) for cat in categoriesToTakeFrom2]
  
  keylist1=infile1.GetListOfKeys()
  
  for key in keylist1:
  
    thisname=key.GetName()
    
    if "BDTbin" in thisname or "data_obs" in thisname:
      continue
    
    takeit=False
    
    for cat,transferred in transferCategories:
      if cat in thisname:
        takeit=True
        transferred=True
    
    if takeit:      
      thish=infile2.Get(thisname)
    else:
      thish=infile1.Get(thisname)
    
    #print thisname, thish
    if thish!=None:
      outfile.cd()
      thish.Write()
  
  keylist2=infile2.GetListOfKeys()

  for key in keylist2:
  
    thisname=key.GetName()
    
    if "BDTbin" in thisname or "data_obs" in thisname:
      continue
    
    takeit=False
    
    for cat,transferred in transferCategories:
      #if cat in thisname:
      if cat in thisname and not transferred:
        takeit=True
    
    thish=infile2.Get(thisname)
    
    #print thisname, thish
    if thish!=None:
      outfile.cd()
      thish.Write()

  outfile.Close()
  infile1.Close()
  infile2.Close()

def replaceQ2scale(infname,toupdate="_CMS_ttH_Q2scale_",updatewith="_CMS_ttH_CombinedScale_"):
  print infname,infname[:-5]+'_backup'+infname[-5:]
#  raw_input('trying to rename' )
  os.rename(infname,infname[:-5]+'_backup'+infname[-5:])
  backup=infname[:-5]+'_backup'+infname[-5:]
  infile=ROOT.TFile(backup)
  outfile=ROOT.TFile(infname,'recreate')
  keylist=infile.GetListOfKeys()
  for key in keylist:
    thisname=key.GetName()
    thishisto=infile.Get(thisname).Clone()
    if toupdate in thisname:
      newname=thisname.replace(toupdate,toupdate+'backup_')
      thishisto.SetName(newname)
      print "updated", thisname, newname
#      raw_input()
    elif updatewith in thisname:
      newname=thisname.replace(updatewith,toupdate)
      thishisto.SetName(newname)     
      print "updated", thisname, newname
#      raw_input()
    outfile.cd()
    thishisto.Write()
  infile.Close()
  outfile.Close()



def addPseudoData(infname,samplesWOttH,categories,sysnames,disc="BDT_ljets"):

  infile=ROOT.TFile(infname,"UPDATE")

  for cat in categories:
    print "getting ", samplesWOttH[0]+"_"+disc+"_"+cat
    oldhist=infile.Get(samplesWOttH[0]+"_"+disc+"_"+cat)
    newhist=oldhist.Clone("data_obs_"+disc+"_"+cat)
    print newhist
    for s in samplesWOttH[1:]:
      print "doiung ", s+"_"+disc+"_"+cat
      bufferhist=infile.Get(s+"_"+disc+"_"+cat)
      print bufferhist
      newhist.Add(bufferhist)
    newhist.Write()
  
  infile.Close()

def addRealData(infname,samplesData,categories,disc="BDT_ljets"):

  infile=ROOT.TFile(infname,"UPDATE")

  for cat in categories:
    print "getting ", samplesData[0]+"_"+disc+"_"+cat
    oldhist=infile.Get(samplesData[0]+"_"+disc+"_"+cat)
    print oldhist, samplesData[0]+"_"+disc+"_"+cat
    newhist=oldhist.Clone("data_obs_"+disc+"_"+cat)
    print newhist
    for s in samplesData[1:]:
      print "doiung ", s+"_"+disc+"_"+cat
      bufferhist=infile.Get(s+"_"+disc+"_"+cat)
      print bufferhist
      newhist.Add(bufferhist)
    newhist.Write()
  
  infile.Close()


def MoveOverUnderflow(infname,outfname):

  infile=ROOT.TFile(infname,"READ")
  outfile=ROOT.TFile(outfname,"RECREATE")

  keylist=infile.GetListOfKeys()

  for key in keylist:
    thisname=key.GetName()
    thishisto=infile.Get(thisname)

    nBins=thishisto.GetNbinsX()
    errMaxBin=thishisto.GetBinError(nBins)
    errOFBin=thishisto.GetBinError(nBins+1)
    newerrorMaxBin=ROOT.TMath.Sqrt(errMaxBin*errMaxBin + errOFBin*errOFBin)
    thishisto.SetBinContent(nBins,thishisto.GetBinContent(nBins)+thishisto.GetBinContent(nBins+1))
    thishisto.SetBinError(nBins,newerrorMaxBin)
    thishisto.SetBinContent(nBins+1,0.0)

    errMinBin=thishisto.GetBinError(1)
    errUFBin=thishisto.GetBinError(0)
    newerrorMinBin=ROOT.TMath.Sqrt(errMinBin*errMinBin + errUFBin*errUFBin)
    thishisto.SetBinContent(1,thishisto.GetBinContent(1)+thishisto.GetBinContent(0))
    thishisto.SetBinError(1,newerrorMinBin)
    thishisto.SetBinContent(0,0.0)

    #write to outfile
    outfile.cd()
    thishisto.Write()

  outfile.Close()

def makeDatacards(filename,outname,categories=None,doHdecay=True,discrname='finaldiscr'):
  if categories==None:
    categories=["ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t2","ljets_jge6_t3","ljets_jge6_tge4"]
#  print 'mk_datacard_ttbb13TeV', '-d', 'finaldiscr', '-c','"'+(' '.join(categories))+'"','-o', outname+'txt', filename
  
  #call(['mk_datacard_ttbb13TeV', '-d', 'finaldiscr', '-c',' '.join(categories),'-o', outname+'.txt', filename])
  #if doHdecay:
    #call(['mk_datacard_hdecay13TeV', '-d', discrname, '-c',' '.join(categories),'-o', outname+'_hdecay.txt', filename])

  for c in categories:
    #call(['mk_datacard_ttbb13TeV', '-d', 'finaldiscr', '-c', c, '-o', outname+'_'+c+'.txt', filename])
    if doHdecay:
      call(['mk_datacard_hdecay13TeV', '-d', discrname, '-c', c, '-o', outname+'_'+c+'_hdecay.txt', filename])
  cardscript=open("newCardScript.sh","w")
  cardscript.write("#!/bin/bash \n")
  #cardscript.write('mk_datacard_ttbb13TeV'+' -d '+' finaldiscr'+' -c '+' '.join(categories)+' -o '+outname+'.txt '+filename+"\n")
  #cardscript.write('mk_datacard_hdecay13TeV'+' -d '+' '+discrname+' '+' -c '+' '.join(categories)+' -o '+outname+'_hdecay.txt '+filename+"\n")
  for c in categories:
    #cardscript.write('mk_datacard_ttbb13TeV '+' -d '+' finaldiscr '+' -c '+c+' -o '+outname+'_'+c+'.txt '+filename+"\n")
    cardscript.write('mk_datacard_hdecay13TeV'+' -d '+' '+discrname+' '+' -c '+c+' -o '+outname+'_'+c+'_hdecay.txt '+filename+"\n")
  cardscript.close()
  
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

def calcLimits(datacardname,categories=None):
  
  if categories==None:
    categories=["ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t2","ljets_jge6_t3","ljets_jge6_tge4"]
  call(['combine', '-M', 'Asymptotic', '-m', '125', '-t', '-1',datacardname+'.txt']) 
  limit_comb=readLimit('higgsCombineTest.Asymptotic.mH125.root')
  limit_cats=[]
  for c in categories:
    call(['stdcombine',datacardname+'_'+c+'.txt']) 
    limit_cats.append(readLimit('higgsCombineTest.Asymptotic.mH125.root'))
  report='combined: '+str(limit_comb)+'\n'
  for c,l in zip(categories,limit_cats):
    report+=c+": "+str(l)+"\n"
  f=open(datacardname+'_limits.txt','w')
  f.write(report)
  print report
  f.close()
  result=Limitresult(limit_comb[2],limit_comb[3],limit_comb[1],limit_comb[4],limit_comb[0], ## finisch this
                     categories,
                     [catl[2] for catl in limit_cats],
                     [catl[3] for catl in limit_cats],
                     [catl[1] for catl in limit_cats],
                     [catl[4] for catl in limit_cats],
                     [catl[0] for catl in limit_cats])
  return result


def rebinHistoOld(h,n,xmin,xmax):
  xmin=round(xmin*100.)/100.
  xmax=round(xmax*100.)/100.

  hr=ROOT.TH1F(h.GetName(),h.GetTitle(),n,xmin,xmax)
  bincontent=0.
  binerror=0
  nbin=1
  sumofc=0.
  for obin in range(h.GetNbinsX()+2):
    if h.GetBinLowEdge(obin+1)<=hr.GetBinLowEdge(nbin+1):
      sumofc+=h.GetBinContent(obin)
      bincontent+=h.GetBinContent(obin)
      binerror=ROOT.TMath.Sqrt(h.GetBinError(obin)*h.GetBinError(obin)+binerror*binerror)
#    h.GetBinLowEdge(obin)>=hr.GetBinLowEdge(nbin) or obin == h.GetNbinsX()+1:
    else:
      sumofc+=h.GetBinContent(obin)
      hr.SetBinContent(nbin,bincontent)
      hr.SetBinError(nbin,binerror)
      bincontent=h.GetBinContent(obin)
      binerror=ROOT.TMath.Sqrt(h.GetBinError(obin)*h.GetBinError(obin))
      nbin+=1
      if nbin == hr.GetNbinsX():
        lastobin=obin
        break

  for obin in range(lastobin+1,h.GetNbinsX()+2):
    bincontent+=h.GetBinContent(obin)
    binerror=ROOT.TMath.Sqrt(h.GetBinError(obin)*h.GetBinError(obin)+binerror*binerror)
  hr.SetBinContent(hr.GetNbinsX(),bincontent)
  hr.SetBinError(hr.GetNbinsX(),binerror)



  return hr
  

def rebinHistosOld(inputpath,rebinnedpath,samples,discrname,binlabels,systematics,binning):
  nhistobins=[x[0] for x in  binning]
  minxvals=[x[1] for x in  binning]
  maxxvals= [x[2] for x in  binning]
  

  fin=ROOT.TFile(inputpath,'readonly')
  fout=ROOT.TFile(rebinnedpath,'recreate')

  for bl,n,xmin,xmax in zip(binlabels,nhistobins,minxvals,maxxvals):
    for sample in samples:
      for syst in systematics:
        hn=sample.nick+'_'+discrname+'_'+bl+syst
        h=fin.Get(hn)
        h=rebinHistoOld(h,n,xmin,xmax)
        fout.cd()
        h.Write()
    

  fin.Close()
  fout.Close()


def getXminXmax(hs,minc,nbins):
  h=hs[0].Clone('sum_tmp')
  for hi in hs[1:]:
    h.Add(hi)
  xmin=-999
  xmax=999
  xminhiedge=-999
  xmaxlowedge=999
  content=0.
  for obin in range(h.GetNbinsX()+2):
    content+=h.GetBinContent(obin)
    if content>minc*5: 
      xminhiedge=h.GetBinLowEdge(obin+1)
      break
  content=0.
  for obin in range(h.GetNbinsX()+1,0,-1):
    content+=h.GetBinContent(obin)
    if content>minc: 
      xmaxlowedge=h.GetBinLowEdge(obin)
      break
  print xmaxlowedge,xminhiedge
  width=(xmaxlowedge-xminhiedge)/(nbins-2.)
  print width
  xmax=xmaxlowedge+width
  xmin=xminhiedge-width
  xmin=round(xmin*1000.)/1000.
  xmax=round(xmax*1000.)/1000.
  return xmin,xmax

  

def rebinHistosMinEvents(inputpath,rebinnedpath,samples,discrname,binlabels,systematics,binning):
  nhistobins=[x[0] for x in  binning]
  mincontents=[x[1] for x in  binning]

  fin=ROOT.TFile(inputpath,'readonly')
  fout=ROOT.TFile(rebinnedpath,'recreate')

  for bl,n,minc in zip(binlabels,nhistobins,mincontents):
    hnominals=[]
    for sample in samples:
      hnominals.append(fin.Get(sample.nick+'_'+discrname+'_'+bl))
    xmin,xmax=getXminXmax(hnominals,minc,n)
    for sample in samples:
      # find xmin and xmax
      for syst in systematics:
        hn=sample.nick+'_'+discrname+'_'+bl+syst
        h=fin.Get(hn)
        h=rebinHistoOld(h,n,xmin,xmax)
        fout.cd()
        h.Write()

  fin.Close()
  fout.Close()

def getXminXmaxFromError(hs,maxerror,nbins):
  h=hs[0].Clone(hs[0].GetName()+'_rebinning')
  for hi in hs[1:]:
    h.Add(hi)
  xmin=-999
  xmax=999
  xminhiedge=-999
  xmaxlowedge=999
  content=0.
  error=0.
  for obin in range(h.GetNbinsX()+2):
    content+=h.GetBinContent(obin)
    error=ROOT.TMath.Sqrt(error*error+h.GetBinError(obin)*h.GetBinError(obin))
#    if 'jets_j5_tge4' in h.GetName(): print 'left:',content,error
    if content>0 and (error/content)<maxerror/3.: 
      xminhiedge=h.GetBinLowEdge(obin+1)
      break
  content=0.
  error=0.
  for obin in range(h.GetNbinsX()+1,0,-1):
    content+=h.GetBinContent(obin)
    error=ROOT.TMath.Sqrt(error*error+h.GetBinError(obin)*h.GetBinError(obin))
    if 'j5_tge4' in h.GetName(): print 'right:',content,error
    if content>0 and (error/content)<maxerror: 
      xmaxlowedge=h.GetBinLowEdge(obin)
      break
  if 'j5_tge4' in h.GetName(): print 'edges',xmaxlowedge,xminhiedge
  width=(xmaxlowedge-xminhiedge)/(nbins-2.)
  if 'j5_tge4' in h.GetName(): print 'width', width
  xmax=xmaxlowedge+width
  xmin=xminhiedge-width
  xmin=round(xmin*1000.)/1000.
  xmax=round(xmax*1000.)/1000.
  if 'j5_tge4' in h.GetName(): print 'minmax', xmin,xmax
  return xmin,xmax


def rebinHistosMCerror(inputpath,rebinnedpath,samples,discrname,binlabels,systematics,binning):
  nhistobins=[x[0] for x in  binning]
  mcerrors=[x[1] for x in  binning]

  fin=ROOT.TFile(inputpath,'readonly')
  fout=ROOT.TFile(rebinnedpath,'recreate')

  for bl,n,mcerror in zip(binlabels,nhistobins,mcerrors):
    hnominals=[]
    for sample in samples[1:]:
      hnominals.append(fin.Get(sample.nick+'_'+discrname+'_'+bl))
    xmin,xmax=getXminXmaxFromError(hnominals,mcerror,n)
    for sample in samples:
      # find xmin and xmax
      for syst in systematics:
        hn=sample.nick+'_'+discrname+'_'+bl+syst
        h=fin.Get(hn)
        h=rebinHistoOld(h,n,xmin,xmax)
        fout.cd()
        h.Write()

  fin.Close()
  fout.Close()


def mergeLimitFiles(newfn,newcats,oldfn,oldcats_w_overlap,samples,discrname,systs,outfile):
  fnew=ROOT.TFile(newfn,'readonly')
  fold=ROOT.TFile(oldfn,'readonly')
  fout=ROOT.TFile(outfile,'recreate')
  oldcats=[]
  for c in oldcats_w_overlap:
    if not c in newcats:
      oldcats.append(c)

  for sample in samples:
    for syst in systs:
      for c in oldcats:
        hn=sample.nick+'_'+discrname+'_'+c+syst
        h=fold.Get(hn)
        fout.cd()
        h.Write()
      for c in newcats:
        hn=sample.nick+'_'+discrname+'_'+c+syst
        h=fnew.Get(hn)
        fout.cd()
        h.Write()
  fnew.Close()
  fold.Close()
  fout.Close()
  samplesWOttH=[]
  for s in samples:
    if 'tth' not in s.nick.lower():
      samplesWOttH.append(s.nick)
  addPseudoData(outfile,samplesWOttH,oldcats+newcats,systs,discrname)

def gausSFperBin(h,r):
  sfhisto=h.Clone('sfhisto')
  for i in range(sfhisto.GetNbinsX()+1):
    content=sfhisto.GetBinContent(i)
    error=sfhisto.GetBinError(i)
    sf=0.
    if content>0:
      varied=r.Gaus(content,error)
      if varied>0:
        sf=varied/content
    print 'content',content
    print 'sf',sf
    sfhisto.SetBinContent(i,sf)
    sfhisto.SetBinError(i,0)
  return sfhisto
      

def createToyShapes(oldpath,newpath,samples,discrname,cats,systs,seed):
  fnew=ROOT.TFile(newpath,'recreate')
  fold=ROOT.TFile(oldpath,'readonly')
  random=ROOT.TRandom3()
  random.SetSeed(seed)
  for sample in samples:
    for c in cats:
      nnominal=sample.nick+'_'+discrname+'_'+c
      hnominal=fold.Get(nnominal)
      sfhisto=gausSFperBin(hnominal,random)
      for s in systs:
        n=sample.nick+'_'+discrname+'_'+c+s
        hnew=fold.Get(n).Clone()
        hnew.Multiply(sfhisto)
        fnew.cd()
        hnew.Write()
  fold.Close()
  fnew.Close()
        

  
  
