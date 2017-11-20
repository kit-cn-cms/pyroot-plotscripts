import json
import sys

combs={
  "combined_DNNonly": {
      "incombs": {
         "names": ["DL_DNN_3j_ge3t","DL_DNN_ge4j_ge3t", "SL_DNN_4j_ge3t", "SL_DNN_5j_ge3t", "SL_DNN_ge6j_ge3t","combined_DNNonly"  ],
         },
      },
  "SL_DNN": {
      "incombs": {
         "names": ["SL_DNN_4j_ge3t", "SL_DNN_5j_ge3t", "SL_DNN_ge6j_ge3t","SL_DNN"  ],
         },
      },
   "DL_DNN": {
      "incombs": {
         "names": ["DL_DNN_3j_ge3t","DL_DNN_ge4j_ge3t","DL_DNN"  ],
         },
      },
   "combined_SLDNN_DL2D": {
      "incombs": {
         "names": ["ttH_hbb_13TeV_dl_3j3t", "ttH_hbb_13TeV_dl_ge4j3t_low", "ttH_hbb_13TeV_dl_ge4jge4t_low", "ttH_hbb_13TeV_dl_ge4j3t_high", "ttH_hbb_13TeV_dl_ge4jge4t_high", "SL_DNN_4j_ge3t", "SL_DNN_5j_ge3t", "SL_DNN_ge6j_ge3t","combined_SLDNN_DL2D"  ],
         },
      },
  }


infiles=sys.argv[1:]

allCats={}

for inf in infiles:
  injsonfileLJ=open(inf,"r")
  linesLJ=[]
  for line in injsonfileLJ:
    linesLJ.append(line)
  inj=json.loads(linesLJ[0])
  for icat,cat in enumerate(inj["cat_names"]):
    if not inj["cardnames"][icat] in allCats:
      allCats[inj["cardnames"][icat]]={
        "nchannels": 0,
                          "cat_names":inj["cat_names"][icat],
                          "cardnames":inj["cardnames"][icat],
                          "obs":inj["obs"][icat],
                          "upper1sig":inj["upper1sig"][icat],
                          "lower1sig":inj["lower1sig"][icat],
                          "upper2sig":inj["upper2sig"][icat],
                          "lower2sig":inj["lower2sig"][icat],
                          "expected":inj["expected"][icat],
                          }
    
print allCats

for comb in combs:
  resultGroups={
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
  for sub in combs[comb]["incombs"]["names"]:
    resultGroups["cat_names"].append(allCats[sub]["cat_names"])
    resultGroups["cardnames"].append(allCats[sub]["cardnames"])
    resultGroups["obs"].append(allCats[sub]["obs"])
    resultGroups["upper1sig"].append(allCats[sub]["upper1sig"])
    resultGroups["lower1sig"].append(allCats[sub]["lower1sig"])
    resultGroups["upper2sig"].append(allCats[sub]["upper2sig"])
    resultGroups["lower2sig"].append(allCats[sub]["lower2sig"])
    resultGroups["expected"].append(allCats[sub]["expected"])
    resultGroups["nchannels"]+=1
  jo=json.dumps(resultGroups)
  jsonfile=open("reduced_"+comb+".json","w")
  jsonfile.write(jo)
  jsonfile.close()


