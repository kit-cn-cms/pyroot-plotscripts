import sys

files=sys.argv[1:]

listOfUncertaintiesToToggle=["CMS_ttHbb_UE","CMS_ttHbb_HDAMP","CMS_ttHbb_FSR","CMS_ttHbb_ISR"]

for f in files:
  theFile=open(f,"r")
  inlist=list(theFile)
  theFile.close()
  outlist=[]
  anyToggled=False
  for line in inlist:
    for unc in listOfUncertaintiesToToggle:
      if unc in line:
        if "#" in line:
          anyToggled=True
          
  for line in inlist:
    newline=line
    if "number of nuisance parameters" in line:
      newline="kmax * #number of nuisance parameters\n"
    for unc in listOfUncertaintiesToToggle:
      if unc in line:
        if "#" in line:
          newline=line.replace("#","")
        else:
          #anyToggled
          if anyToggled==False:
            if not "ttbar" in line:
              newline="#"+line 
          else:
            #print line
            newline="#"+line 
    outlist.append(newline)
  theFile=open(f,"w")
  for line in outlist:
    theFile.write(line)
  theFile.close()


