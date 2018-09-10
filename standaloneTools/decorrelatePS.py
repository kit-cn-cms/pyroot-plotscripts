import sys

incards=sys.argv[1:]

nuisanceStringsToFind=["CMS_ttHbb_ISR","CMS_ttHbb_FSR","CMS_ttHbb_HDAMP","CMS_ttHbb_UE"]

def replaceShapeWithRate(card,nuisanceStringsToFind):
  
  binlist=[]
  processlist=[]
  infile=open(card,"r")
  inlist=list(infile)
  infile.close()
  outfile=open(card,"w")
  outlinelist=[]
  afterHeader=False
  afterNuisStart=False
  for line in inlist:
    replaced=False
    
    newline=line
    #print line
    if "observation" in line:
      afterHeader=True
    if afterHeader:
      if "bin" in line:
        binlist=line.replace("\n","").replace("\t"," ").replace("  "," ").replace("   "," ").strip().split(" ")
        print line
        print binlist
      if "process" in line and "tt" in line:
        print line
        processlist=line.replace("\n","").replace("\t"," ").replace("  "," ").replace("   "," ").strip().split(" ")
        afterNuisStart=True
        print processlist
    if afterNuisStart:
      for nuis in nuisanceStringsToFind:
        if nuis in line and not "group" in line:
          replaced=True
          print "replacing ", line
          print "with"
          dummysplitline=line.replace("shape","lnN").replace("\n","").replace("\t"," ").replace("  "," ").replace("   "," ").strip().split(" ")
          splitline=[]
          for sl in dummysplitline:
            if sl!="":
              splitline.append(sl)
          actualNuisName=splitline[0]
          print splitline
          newlinelist=splitline[:2]
          for icol, col in enumerate(splitline[2:]):
            procname=processlist[1:][icol]
            if col!="-":
              newline=actualNuisName+"_"+procname+" lnN "
              for isubcol, subcol in enumerate(splitline[2:]):
                if isubcol!=icol:
                  newline+=" - "
                else: newline+=" "+col+" "
              newline+="\n"
              print newline
              outlinelist.append(newline)
    if replaced==False:
      outlinelist.append(newline)      
              
  for line in outlinelist:
    outfile.write(line)
  outfile.close()

for card in incards:
  replaceShapeWithRate(card,nuisanceStringsToFind)