import sys
from subprocess import call


infilename=sys.argv[1]
infile=open(infilename,"r")
indclist=list(infile)
reflimit=4.29688

systs=["lumi_13TeV","QCDscale_ttH","QCDscale_ttbar","QCDscale_singlet","pdf_gg","pdf_qqbar","pdf_qg","QCDscale_V","QCDscale_VV","CMS_ttH_CSVLF","CMS_ttH_CSVHF","CMS_ttH_CSVHFStats1","CMS_ttH_CSVHFStats2",
"CMS_ttH_CSVLFStats1","CMS_ttH_CSVLFStats2","CMS_ttH_CSVCErr1","CMS_ttH_CSVCErr2","CMS_scale_j","CMS_ttH_QCDscale_ttbarPlusB","CMS_ttH_QCDscale_ttbarPlus2B","CMS_ttH_QCDscale_ttbarPlusBBbar",
"CMS_ttH_QCDscale_ttbarPlusCCbar","CMS_ttH_Q2scale_ttbarOther","CMS_ttH_Q2scale_ttbarPlusB","CMS_ttH_Q2scale_ttbarPlus2B","CMS_ttH_Q2scale_ttbarPlusBBbar","CMS_ttH_Q2scale_ttbarPlusCCbar","CMS_ttH_NNPDF","binbybin"]
resultlist=[]
improvementlist=[]

for sys in systs:
  print "doing ", sys
  outfilename=infilename+"_"+sys
  outfile=open(infilename+"_"+sys,"w")
  for line in indclist:
    if sys == line.split(" ")[0]:
      continue
    if sys=="binbybin" and "13TeV_BDTbin" in line:
      continue
    outfile.write(line)
  outfile.close()
  limitfile=open("limit.txt","w")
  call(['combine','-M', 'Asymptotic','-m','125','--minosAlgo','stepping' ,outfilename, '--run=blind'],stdout=limitfile)
  limitfile.close()
#  exit(0)
  limitfile=open("limit.txt","r")
  limitlist=list(limitfile)
  for line in limitlist:
    if "Expected 50.0%:" in line:
      thislimitstring=line.replace("\n","").rsplit(" ",1)[1]
  thislimit=float(thislimitstring)
  print sys, thislimit, 1.0-(thislimit/reflimit)
  limitfile.close()
  resultlist.append(thislimit)
  improvementlist.append(1.0-(thislimit/reflimit))
  

print ""

zippedlist=zip(systs,resultlist,improvementlist)
zippedlist.sort(key=lambda x: x[2])
outfile=open("results.txt","w")
for sys in zippedlist:
  print sys[0], sys[1], sys[2]

for sys in zippedlist:
  outfile.write(str(sys[0])+" "+str(sys[1])+" "+str(sys[2])+"\n")
outfile.close()



