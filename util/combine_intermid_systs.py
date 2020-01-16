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

def histo2np(h, binlist = None):
    if not binlist:
        binlist = load_bins(h)
    contents = np.zeros(len(binlist))
    for n, i in enumerate(binlist):
        contents[n] = h.GetBinContent(i)
    return contents

def load_bins(h):
    bins = []
    if isinstance(h, ROOT.TH2):
        nbinsX = h.GetNbinsX()
        nbinsY = h.GetNbinsY()
        bins = [h.GetBin(x,y) for x in range(1,nbinsX+1) 
                for y in range(1,nbinsY+1)]
    else: 
        nbins = h.GetNbinsX()
        bins = *range(1, nbins+1)
    return bins

def construct_new_hist(h_nom, name, vals):
    new_hist = h_nom.Clone(name)
    bins = load_bins(h)
    for i, val in zip(bins, vals):
        new_hist.SetBinContent(i, val)
    return new_hist

def combine_hessian_systs(nom_key, syst_key, rfile, systname, syst_list):
    h_nom = rfile.Get(nom_key)
    name = syst_key.replace(systname)
    if not isinstance(h_nom, ROOT.TH1):
        print("ERROR: Could not load histogram '{}'".format(nom_key))
        return
    nom_vals = histo2np(h)
    

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

def replace_in_key(key, process, channel):
    new_key = key.replace("$PROCESS", process)
    new_key = new_key.replace("$CHANNEL", channel)

    return new_key

def get_list(inputs):
    if isinstance(inputs, str):
        return [inputs]
    elif not isinstance(inputs, list):
        return [""]
    else:
        return inputs

def get_histo_keys(nom_key, syst_key, **kwargs):
    """
    construct histogram keys for processes in different channels
    output: list[(nom_key, syst_key)]
    """
    procs = get_list(kwargs.get("processes", "default"))
    channels = get_list(kwargs.get("channels", "default"))
    keylist = []
    for p in procs:
        for c in channels:
            keylist.append(
                (replace_in_key(nom_key, p, c),
                replace_in_key(syst_key, p, c))
            )
    return keylist

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
    proc_keys = get_histo_keys(nom_key = h_nominal_key,
                                syst_key = h_syst_key,
                                **kwargs
                                )
    for syst in replace_cfg:
        keyword = replace_cfg[syst].get("construction", "")
        syst_list = replace_cfg[syst].get("expand_with", [])
        if keyword == "Hessian":
            for nom_key, syst_key in proc_keys:
                combine_hessian_systs(  nom_key = nom_key, 
                                        syst_key = syst_key,
                                        rfile = rfile,
                                        syst_name = syst,
                                        syst_list = syst_list)
        else:
            print("ERROR: unrecognized mode '{}' for syst '{}'".format(keyword, syst))


if __name__ == "__main__":
    pass