import ROOT
import sys
f = ROOT.TFile(sys.argv[1])
systs = [ 
    "Nominal",

    "BTAGDISCR_BSTAT1_UP",
    "BTAGDISCR_BSTAT1_DOWN",

    "BTAGDISCR_BSTAT2_UP",
    "BTAGDISCR_BSTAT2_DOWN",

    "BTAGDISCR_LSTAT1_UP",
    "BTAGDISCR_LSTAT1_DOWN",

    "BTAGDISCR_LSTAT2_UP",
    "BTAGDISCR_LSTAT2_DOWN",

    "BTAGDISCR_BPURITY_UP",
    "BTAGDISCR_BPURITY_DOWN",

    "BTAGDISCR_LPURITY_UP",
    "BTAGDISCR_LPURITY_DOWN",

    "BTAGDISCR_CERR1_UP",
    "BTAGDISCR_CERR1_DOWN",

    "BTAGDISCR_CERR2_UP",
    "BTAGDISCR_CERR2_DOWN",
]

procs = ["ttH", "Others", "ttbarOther", "ttbarPlus2B", "ttbarPlusB", "ttbarPlusBBbar", "ttbarPlusCCbar"]

print("""
        #################
        # NJet weights ##
        #################
        """)

for sys in systs:
    d = f.Get(sys)

    for p in procs:
        h = d.Get(p)

        s = "    \"weight_NJet_SF_{}_{}:=(".format(p, sys.replace("BTAGDISCR_",""))
        for i in range(2,10):
            iBin = h.FindBin(i)
            val = h.GetBinContent(iBin)
            if i == 9:
                s+="((N_Jets>={})*{})".format(i, val)
            else:
                s+="((N_Jets=={})*{})+".format(i, val)
        s+=")\","
        print(s)
    print("\n")

for sys in systs:
    tmp = """
    "weight_NJet_SF_ttbb_{sys}:=((weight_NJet_SF_ttbarPlusB_{sys}*(GenEvt_I_TTPlusBB==1))+(weight_NJet_SF_ttbarPlusBBbar_{sys}*(GenEvt_I_TTPlusBB==3))+(weight_NJet_SF_ttbarPlus2B_{sys}*(GenEvt_I_TTPlusBB==2)))",
    "weight_NJet_SF_ttcc_{sys}:=(weight_NJet_SF_ttbarPlusCCbar_{sys}*(GenEvt_I_TTPlusCC==1))",
    "weight_NJet_SF_ttlf_{sys}:=(weight_NJet_SF_ttbarOther_{sys}*(GenEvt_I_TTPlusCC==0&&GenEvt_I_TTPlusBB==0))",
    """.format(sys=sys.replace("BTAGDISCR_",""))
    print(tmp)

print("\n"*2)
print("#"*10)
print("# combined factors with logic for syst csv")
print("#"*10)

for sys in systs:
    tmp = "    \"N_JetWeight_{sys}:= (((isTTbarSample==1)*weight_NJet_SF_ttbb_{sys}*weight_NJet_SF_ttcc_{sys}*weight_NJet_SF_ttlf_{sys})*((isTthSample==1)*weight_NJet_SF_ttH_{sys})*(isTthSample==0&&isTTbarSample==0)*weight_NJet_SF_Others_{sys})\"".format(sys=sys.replace("BTAGDISCR_",""))
    print(tmp)

