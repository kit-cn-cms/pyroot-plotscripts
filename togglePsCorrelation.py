import sys

files=sys.argv[1:]

listOfUncertaintiesToToggle=["CMS_ttHbb_UE","CMS_ttHbb_HDAMP","CMS_ttHbb_FSR","CMS_ttHbb_ISR"]

for f in files:
  theFile=open(f,"r")
  inlist=list(theFile)
  theFile.close()
  outlist=[]
  for line in inlist:
    newline=line
    if "number of nuisance parameters" in line:
      newline="kmax * #number of nuisance parameters\n"
    lineContainsUncToRemove=False
    for unc in listOfUncertaintiesToToggle:
      if unc in line:
        if "#" in line:
          newline=line.replace("#","")
        else:
          newline="#"+line 
    outlist.append(newline)
  theFile=open(f,"w")
  for line in outlist:
    theFile.write(line)
  theFile.close()

