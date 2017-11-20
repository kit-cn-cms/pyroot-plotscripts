import sys
import glob
from namingMaps import *

outfile=open("table.tex","w")
indirs=sys.argv[1:]


# careful here
# names should not be substrings of other names

resultlines=[]
for dirName in indirs:
  #get name
  cutdirname=""
  if "/" in dirName:
    cutdirname=dirName.split("/")[-1].replace("work_","").replace(prefix,"")
  else:
    cutdirname=dirName.replace("work_","").replace(prefix,"")
  transCatName=cutdirname  
  if cutdirname in nameMap:
      transCatName=nameMap[cutdirname]
  print dirName, transCatName
  outline=transCatName.replace("#geq","$\\geq$")+" & "
  #read limit 
  limit=99.9
  limiterrup=1.0
  limiterrdown=1.0
  limitValup=1.0
  limitValdown=1.0
  fl=glob.glob(dirName+"/asymplimit*")
  if fl!=[]:
    infile=open(fl[0],"r")
    inlist=list(infile)
    infile.close()
    for line in inlist:
      if "Expected 16.0" in line:
        limitValdown=float(line.replace("\n","").split(" ")[-1])
      if "Expected 84.0" in line:
        limitValup=float(line.replace("\n","").split(" ")[-1])
      if "Expected 50.0" in line:
        limit=float(line.replace("\n","").split(" ")[-1])
  limiterrup=limitValup-limit
  limiterrdown=limit-limitValdown
  roundedlimit=round(limit,2)
  roundedlimiterrup=round(limiterrup,2)
  roundedlimiterrdown=round(limiterrdown,2)
  outline+="$"+str(roundedlimit)+"^{+"+str(roundedlimiterrup)+"}_{-"+str(roundedlimiterrdown)+"} $& "
    
  #read bestfit 
  mu=99.9
  muerrup=1.0
  muerrdown=1.0
  fl=glob.glob(dirName+"/mlfit*txt")
  if fl!=[]:
    infile=open(fl[0],"r")
    inlist=list(infile)
    infile.close()
    for line in inlist:
      if "Best fit r:" in line:
        print line
        splitline=line.replace("\n","").split()
        print splitline
        substr=splitline[4]
        mu=float(splitline[3])
        muerrdown=float(substr.split("/")[0].replace("-",""))
        muerrup=float(substr.split("/")[1].replace("+",""))
  roundedmu=round(mu,2)
  roundedmuerrup=round(muerrup,2)
  roundedmuerrdown=round(muerrdown,2)
  outline+="$"+str(roundedmu)+"^{+"+str(roundedmuerrup)+"}_{-"+str(roundedmuerrdown)+"} $ & "
  
  #read significance
  sig=0.0
  fl=glob.glob(dirName+"/signi*txt")
  if fl!=[]:
    infile=open(fl[0],"r")
    inlist=list(infile)
    infile.close()
    for line in inlist:
      if "Significance:" in line:
        sig=float(line.replace("\n","").split(" ")[-1])
  roundedsig=round(sig,2)
  outline+=str(roundedsig)+" \\\\\n"

  #write stuff
  
  outfile.write(outline)

outfile.close()
  
  
  
  
  