import ROOT
import sys
from array import array 
import subprocess
ROOT.gROOT.SetBatch(True)

mkscript = "mk_datacard_hdecayPSscale13TeV"

infiles=sys.argv[2:]
rootfile=sys.argv[1]


for f in infiles:
  varname=f.split("datacard_")[-1]
  varname=varname.replace("_hdecay.txt","")
  print "isolated varname", varname
  discname=""
  if "ljets" in varname:
    discname="finaldiscr"
  else:
    discname="inputVar"
  
  cmd=mkscript+" -d "+discname+" -c "+varname+" -o "+f+" "+rootfile
  subprocess.call(cmd,shell=True)
  
  "inputs2DV12RAW_datacard_s63_BDT_common5_input_dev_from_avg_disc_btags_hdecay.txt"