import sys
import glob

outfile=open("table.tex","w")
indirs=sys.argv[1:]


# careful here
# names should not be substrings of other names
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
"dl_ge4jge4t_low": "DL #geq 4 jets, #geq 4 b-tags low BDT",
"DL_BDTonly": "DL BDT-only",
"DL_2D": "DL 2D",
"SL_BDTonly": "L+J BDT-only",
"SL_2D": "L+J 2D",
"combined_2D": "DL+L+J combined 2D",
"combined_BDTonly": "DL+L+J combined BDT-only",
}

resultlines=[]
for dirName in indirs:
  #get name
  transCatName=dirName
  for cat in nameMap:
    if cat in dirName:
      transCatName=nameMap[cat]
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
  
  
  
  
  