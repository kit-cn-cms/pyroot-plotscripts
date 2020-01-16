import os
import sys
import importlib
import numpy as np
import ROOT


def load_rfile(path):
    r = ROOT.TFile.Open(path)
    if not isinstance(r, ROOT.TFile):
        print("ERROR: could not load file '{}'".format(path))
        r = None
    elif not (r.IsOpen() and not r.IsZombie() and not r.TestBit(ROOT.TFile.kRecovered)):
        print("ERROR: file '{}' is corrupted!".format(path))
        r = None
    return r

def combine_hessian_systs(nom_key, syst_key, rfile, systname, syst_list):
    pass
    

def load_config(cfg_path):
    if not cfg_path:
        print("Found no config for intermediary systematics!")
        print("Will do nothing")
        print(locals())
        sys.exit(1)
    replace_cfg_module = importlib.import_module(cfg_path)
    try:
        replace_cfg = replace_cfg_module.config
    except:
        print("ERROR: could not load dict '{}' from '{}'".format("config", cfg_path))
        raise ValueError
    return replace_cfg

def combine_intermid_syst(h_nominal_key, h_syst_key, syst_csvpath,
                            rfile_path, **kwargs):
    if not os.path.exists(rfile_path):
        print("ERROR: file '{}' does not exist!".format(rfile_path))
        raise ValueError
    rfile = load_rfile(rfile_path)
    if not rfile:
        raise ValueError
    replace_cfg_path = kwargs.get("replace_config", None)
    replace_cfg = load_config(replace_cfg_path)
    for syst in replace_cfg:
        keyword = replace_cfg[syst].get("construction", "")
        syst_list = replace_cfg[syst].get("expand_with", [])
        if keyword == "Hessian":
            combine_hessian_systs(  nom_key = h_nominal_key, 
                                    syst_key = h_syst_key,
                                    rfile = rfile,
                                    syst_name = syst,
                                    syst_list = syst_list)
        else:
            print("ERROR: unrecognized mode '{}' for syst '{}'".format(keyword, syst))


if __name__ == "__main__":
    pass