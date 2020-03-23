import os
import sys
import importlib
import numpy as np
import ROOT
from fnmatch import filter
from optparse import OptionParser

thisdir = os.path.realpath(os.path.dirname(__file__))
syst_module_path = os.path.join(thisdir, "tools")

if not syst_module_path in sys.path:
    sys.path.append(syst_module_path)
import Systematics
debug = 0
def load_rfile(path):
    r = ROOT.TFile.Open(path, "UPDATE")
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
    print("Loading values from histogram '{}'".format(h.GetName()))
    contents = np.zeros(len(binlist))
    for n, i in enumerate(binlist):
        contents[n] = h.GetBinContent(i)
    if debug >= 10:
        print(contents)
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
        bins = range(1, nbins+1)
    return bins

def construct_new_hist(h_nom, name, vals):
    new_hist = h_nom.Clone(name)
    new_hist.Reset()
    bins = load_bins(new_hist)
    for i, val in zip(bins, vals):
        new_hist.SetBinContent(i, val)
    return new_hist

def load_values(key, rfile, syst_list):
    values = None
    keylist = [x.GetName() for x in rfile.GetListOfKeys()]
    print("syst_list:")
    print(syst_list)
    # print("list of keys:")
    # print(keylist)

    for syst in syst_list:
        wildcard = key.replace("$SYSTEMATIC", "*"+syst)
        sublist = filter(keylist, wildcard)
        n = len(sublist)
        if n == 0:
            raise KeyError("Could not find any keys with '{}'".format(wildcard))
        elif not n == 1:
            raise KeyError("Found {} keys with '{}', generation not possible".format(n, wildcard))
        hname = sublist[0]
        h = rfile.Get(hname)
        if values is None:
            values = histo2np(h)
        else:
            values = np.row_stack((values, histo2np(h)))
    if debug >= 5:
        print(values)
    return values

def combine_systs(nom_key, syst_key, rfile, systname, replace_cfg):
    keyword = replace_cfg[systname].get("construction", "")
    syst_list = replace_cfg[systname].get("expand_with", [])
    h_nom = rfile.Get(nom_key)
    name = syst_key.replace("$SYSTEMATIC", systname)
    if not isinstance(h_nom, ROOT.TH1):
        print("ERROR: Could not load histogram '{}' from file '{}'".format(nom_key, rfile.GetName()))
        return
    nom_vals = histo2np(h_nom)
    syst_list = ["{}_{}".format(systname, x) for x in syst_list]
    values = load_values(key = syst_key, rfile = rfile, syst_list = syst_list)
    if values.size != 0:
        residuals = values - nom_vals
        if keyword == "Hessian":
            # compute squared differences
            values = (residuals)**2
            
            # final values is squared sum per bin
            values = (values.sum(axis=0))**0.5
        elif keyword == "MCrelic":
            # values are the root mean squared values of the respective variations
            values = (np.mean(residuals**2, axis=0))**0.5
        else:
            msg = "Did not recognize keyword '{}'!".format(keyword)
            msg += "\nCurrent choices: Hessian, MCrelic"
            raise ValueError(msg)
        if debug >= 3:
            print("nominal (nElements: {}):".format(nom_vals.size))
            print(nom_vals)
            print("varied (nElements: {}):".format(values.size))
            print(values)
        h_up = construct_new_hist(h_nom = h_nom, name = name+"Up", vals = values + nom_vals)
        print("Writing '{}'".format(h_up.GetName()))
        rfile.WriteTObject(h_up, h_up.GetName(), "Overwrite")

        h_down = construct_new_hist(h_nom = h_nom, name = name+"Down", vals = nom_vals - values)
        print("Writing '{}'".format(h_down.GetName()))
        rfile.WriteTObject(h_down, h_down.GetName(), "Overwrite")
    else:
        print("Unable to load values for key '{}'".format(syst_key))

def merge_systs(nom_key, syst_key, rfile, systname, replace_cfg):
    orig_list = replace_cfg[systname].get("merge_with", [])
    if len(orig_list) == 0:
        print("Found no specifications to merge systematic '{}' with something else".format(systname))
        return
    syst_list = orig_list + [systname]
    print("merging {}".format(syst_list))
    h_nom = rfile.Get(nom_key)
    name = syst_key.replace("$SYSTEMATIC", systname)
    if not isinstance(h_nom, ROOT.TH1):
        print("ERROR: Could not load histogram '{}' from file '{}'".format(nom_key, rfile.GetName()))
        return
    nom_vals = histo2np(h_nom)
    for var in ["Up", "Down"]:
        values = load_values(key = syst_key, rfile = rfile, syst_list = [x+var for x in syst_list])
        if values.size != 0:
            # compute squared differences
            values = (values - nom_vals)**2
            # final values is squared sum per bin
            values = (values.sum(axis=0))**0.5

            if debug >= 3:
                print("nominal (nElements: {}):".format(nom_vals.size))
                print(nom_vals)
                print("varied (nElements: {}):".format(values.size))
                print(values)
            if var == "Up": values = values + nom_vals
            else: values = nom_vals - values
            # backup original systematic
            h = rfile.Get(name+var)
            bu_name = "{}_premerge{}".format(name, var)
            rfile.WriteTObject(h, bu_name, "Overwrite")
            h_new = construct_new_hist(h_nom = h_nom, name = name+var, vals = values)
            print("Writing '{}'".format(h_new.GetName()))
            rfile.WriteTObject(h_new, h_new.GetName(), "Overwrite")

        else:
            print("Unable to load values for key '{}'".format(syst_key))

def load_config(cfg_path):
    if not cfg_path:
        print("Found no config for intermediary systematics!")
        print("Will do nothing")
        print(locals())
        sys.exit(1)
    cfg_path = os.path.abspath(cfg_path)
    cfg_dir = os.path.dirname(cfg_path)
    if not cfg_dir in sys.path:
        sys.path.append(cfg_dir)
    module_name = os.path.basename(cfg_path)
    if module_name.endswith(".py"): module_name = module_name[:-len(".py")]
    replace_cfg_module = importlib.import_module(module_name)
    try:
        replace_cfg = replace_cfg_module.config
    except:
        raise ValueError("could not load dict '{}' from '{}'".format("config", cfg_path))
    return replace_cfg

def replace_in_key(key, process, channel):
    new_key = key.replace("$PROCESS", process)
    new_key = new_key.replace("$CHANNEL", channel)

    return new_key

def load_procs_and_channels(nom_key, separator, rfile):
    # load all keys
    if not separator:
        raise ValueError("Could not find separator!")
    if not nom_key:
        raise ValueError("Could not find nominal histo key!")
    if not rfile:
        raise ValueError("Could not find root file to load from!")
    keys = [x.GetName() for x in rfile.GetListOfKeys()]
    procs = []
    channels = []
    templ_parts = nom_key.split(separator)
    for k in keys:
        parts = k.split(separator)
        if not len(parts) == len(templ_parts): continue
        proc_idx = templ_parts.index("$PROCESS")
        chan_idx = templ_parts.index("$CHANNEL")
        procs = list(set(procs + [parts[proc_idx]]))
        channels = list(set(channels + [parts[chan_idx]]))
    return procs, channels
    

def get_list(**kwargs):
    key = kwargs.get("key", None)
    
    inputs = kwargs.get( key, None)
    if isinstance(inputs, str):
        return [inputs]
    elif not isinstance(inputs, list) or len(inputs) == 0:
        rfile = kwargs.get("rfile", None)
        separator = kwargs.get("separator", None)
        nom_key = kwargs.get("nom_key", None)
        procs, channels = load_procs_and_channels(  nom_key = nom_key,
                                                    separator = separator,
                                                    rfile = rfile
                                                )
        if key == "processes": return procs
        elif key == "channels": return channels
        else: return [""]
    else:
        return inputs

def get_histo_keys(nom_key, syst_key, **kwargs):
    """
    construct histogram keys for processes in different channels
    output: list[(nom_key, syst_key)]
    """
    procs = get_list(key = "processes", nom_key = nom_key, **kwargs)
    channels = get_list(key = "channels", nom_key = nom_key, **kwargs)
    keylist = []
    for p in procs:
        for c in channels:
            keylist.append(
                (replace_in_key(nom_key, p, c),
                replace_in_key(syst_key, p, c))
            )
    return keylist

def combine_intermid_syst(**kwargs):
    print("debug level: {}".format(debug))
    # check if the most basic arguments are given
    h_nominal_key = kwargs.get("h_nominal_key", None)
    h_syst_key = kwargs.get("h_syst_key", None)
    rfile_path = kwargs.get("rfile_path", None)
    if any(x is None for x in [h_nominal_key, h_syst_key, rfile_path]):
        msg = "Parsing error!\n"
        msg += str(locals())
        raise ValueError(msg)
    # load root file
    if not os.path.exists(rfile_path):
        raise ValueError("file '{}' does not exist!".format(rfile_path))
    rfile = load_rfile(rfile_path)
    if not rfile:
        raise ValueError()
    # load config with specifications for merging systematics
    replace_cfg_path = kwargs.get("replace_config", None)
    replace_cfg = load_config(replace_cfg_path)
    # load csv file with systematics. This is necessary in order to perform
    # a check whether a given systematic is relevant for a given process
    syst_csv_path = kwargs.get("syst_csvpath", "")
    process = kwargs.get("processes","")
    if not syst_csv_path:
        raise ValueError("Could not load path to csv with systematics!")
    elif not os.path.exists(syst_csv_path):
        raise ValueError("Could not find file with systematics in '{}'".format(syst_csv_path))
    systematics = Systematics.Systematics(syst_csv_path, relevantProcesses = [process])

    #load processes (if none are given already)
    procs = get_list(key = "processes", nom_key = h_nominal_key, rfile = rfile, **kwargs)
    systematics.getSystematicsForProcesses(procs)

    # for each process, check if a given systematic in the replace config is relevant.
    # if yes, continue with merging. If not, skip this uncertainty
    for process in procs:
        process_systs = systematics.get_shape_systs(process)
        subdict = {}
        subdict.update(kwargs)
        if "processes" in subdict:
            subdict["processes"] = process
        
        proc_keys = get_histo_keys( nom_key = h_nominal_key, 
                                    syst_key = h_syst_key, 
                                    rfile = rfile, **subdict)
        
        # do two iterations through systematics in replace config
        # first iteration will construct/merge uncertainties
        # second iteration combine uncertainties
        for syst in replace_cfg:
            if not syst in process_systs:
                print("systematic '{}' does not belong to process '{}'".format(syst, process))
                continue

            for nom_key, syst_key in proc_keys:
                combine_systs(  nom_key = nom_key, syst_key = syst_key,
                                systname = syst,
                                rfile = rfile, replace_cfg = replace_cfg)
        
        #WIP: include logic to merge two uncertainties here
        for syst in replace_cfg:
            if not syst in process_systs:
                print("systematic '{}' does not belong to process '{}'".format(syst, process))
                continue
            for nom_key, syst_key in proc_keys:
                merge_systs(  nom_key = nom_key, syst_key = syst_key,
                                systname = syst,
                                rfile = rfile, replace_cfg = replace_cfg)



    # the final output should be 'DONE' so the nafInterface module can check on the jobs
    print("DONE")

def parse_arguments():
    parser = OptionParser()
    parser.add_option(  "-n", "--nominal",
                        help = " ".join(
                            """
                            Use this as nominal key for histograms.
                            Default: '$PROCESS__$CHANNEL'
                            """.split()
                        ),
                        default = "$PROCESS__$CHANNEL",
                        dest = "h_nominal_key",
                        type = "str"
                    )
    parser.add_option(  "-s", "--systematic",
                        help = " ".join(
                            """
                            Use this as systematic key for histograms.
                            Default: '$PROCESS__$CHANNEL__$SYSTEMATIC'
                            """.split()
                        ),
                        default = "$PROCESS__$CHANNEL__$SYSTEMATIC",
                        dest = "h_syst_key",
                        type = "str"
                    )
    parser.add_option(  "--separator",
                        help = " ".join(
                            """
                            separator that separates keywords in histo channels.
                            Is needed if either processes or channels are not 
                            specified! (default: '__')
                            """.split()
                        ),
                        dest = "separator",
                        default = "__",
                        type = "str"
                    )
    parser.add_option(  "-r", "--rootfile",
                        help = " ".join(
                            """
                            load histograms from this file
                            """.split()
                        ),
                        dest = "rfile_path",
                        type = "str"
                    )
    parser.add_option(  "-f", "--systcsv",
                        help = " ".join(
                            """
                            load systematics from this .csv file
                            """.split()
                        ),
                        dest = "syst_csvpath",
                        type = "str"
                    )
    parser.add_option(  "-c", "--config",
                        help = " ".join(
                            """
                            path to config .py file containing meta info
                            for merging respective histograms
                            """.split()
                        ),
                        dest = "replace_config",
                        type = "str"
                    )
    parser.add_option(  "--process",
                        help = " ".join(
                            """
                            do merging of histograms for these processes.
                            Can be a comma-separated list or called multiple
                            times.
                            """.split()
                        ),
                        dest = "processes",
                        action = "append"
                    )
    parser.add_option(  "--channel",
                        help = " ".join(
                            """
                            do merging of histograms for these channels.
                            Can be a comma-separated list or called multiple
                            times.
                            """.split()
                        ),
                        dest = "channels",
                        action = "append"
                    )
    parser.add_option(  "-v", "--verbosity",
                        help = " ".join(
                            """
                            manages amount of output. Default: 0
                            """.split()
                        ),
                        dest = "verbosity",
                        default = 0,
                        type = "int"
                    )

    options, args = parser.parse_args()
    if options.processes:
        tmp = []
        for p in options.processes:
            tmp += p.split(",")
        options.processes = tmp
    
    if options.channels:
        tmp = []
        for p in options.channels:
            tmp += p.split(",")
        options.channels = tmp

    global debug 
    debug = options.verbosity

    return options, args

if __name__ == "__main__":
    options, args = parse_arguments()
    print(options)
    print(type(options))
    combine_intermid_syst(**vars(options))
