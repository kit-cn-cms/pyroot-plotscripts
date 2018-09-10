import sys

files=sys.argv[1:]

listOfUncertaintiesToToggle=["CMS_ttHbb_UE","CMS_ttHbb_HDAMP","CMS_ttHbb_FSR","CMS_ttHbb_ISR"]

for f in files:
  theFile=open(f,"r")
  inlist=list(theFile)
  theFile.close()
  outlist=[]
  #DISCLAIMER the following lines were in the other file ---->
  '''
  anyToggled=False
  for line in inlist:
    for unc in listOfUncertaintiesToToggle:
      if unc in line:
        if "#" in line:
          anyToggled=True
  '''
  #DISCLAIMER <----
  for line in inlist:
    newline=line
    if "number of nuisance parameters" in line:
      newline="kmax * #number of nuisance parameters\n"
    #DISCLAIMER the following line was not in the other file
    lineContainsUncToRemove=False

    for unc in listOfUncertaintiesToToggle:
      if unc in line:
        if "#" in line:
          newline=line.replace("#","")
        else:
          #DISCLAIMER the following lines were different in the other file ---->
          newline="#"+line 
          '''
          #anyToggled
          if anyToggled==False:
            if not "ttbar" in line:
              newline="#"+line 
          else:
            #print line
            newline="#"+line
          '''
          #DISCLAIMER <----
    outlist.append(newline)
  theFile=open(f,"w")
  for line in outlist:
    theFile.write(line)
  theFile.close()

