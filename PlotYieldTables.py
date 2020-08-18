from __future__ import print_function
import sys
import ROOT

regions = [
    "had_SR",
    "had_CR_ZElEl",
    "had_CR_ZMuMu",
    "had_CR_WEl",
    "had_CR_WMu",
    "had_CR_ttbarEl",
    "had_CR_ttbarMu",
    "had_CR_Gamma"
    ]

processes = [
    "znunujets",
    "wlnujets",
    "zlljets",
    "gammajets",
    "ttbar_",
    "singlet",
    "diboson",
    "qcd",
    "pseudodata_obs",
    "data_obs"
    ]

yield_dict = {}

input_files = sys.argv[1:]

for file in input_files:
    root_file = ROOT.TFile.Open(file,"READ")
    for key in root_file.GetListOfKeys():
        key_name = key.GetName()
        if not "yield" in key_name:
            continue
        if "Up" in key_name or "Down" in key_name:
            continue
        process = None
        for process_ in processes:
            if process_ == "data_obs" and "pseudodata_obs" in key_name:
                continue
            if process_ in key_name:
                process = process_
        if not process:
            continue
        region = None
        for region_ in regions:
            if region_ in key_name:
                region = region_
        if not region:
            continue
        if not region in yield_dict:
            yield_dict[region] = {}
        if not process in yield_dict[region]:
            yield_dict[region][process] = {}
        yield_dict[region][process]["yield"] = root_file.Get(key_name).Integral()
        yield_dict[region][process]["entries"] = root_file.Get(key_name).GetEntries()
    root_file.Close()

print(yield_dict)

for region in regions:
    print("\n")
    print("--------------------------------")
    print("--------------------------------")
    print("category:",region)
    print("--------------------------------")
    print("--------------------------------")
    for process in processes:
        if "data" in process:
            print("--------------------------------")
        yield_ = 0.0
        entries = 0.0
        if region in yield_dict and process in yield_dict[region]:
            yield_ = yield_dict[region][process]["yield"]
            entries = yield_dict[region][process]["entries"]
        print(process,round(yield_,2))
