import csv
import math
import os
import re
import ROOT as r
import sys

# b-tag split mode:
B_OFF = 0
B_RATE = 1      # Use rate only
B_SHAPE = 2     # Split into shape and rate
B_CAT_SHAPE = 4 # Split into shape by category and rate

transformLnN=False

# Define some regular expressions to match samples and signal.  The last
# part of the former expression is a negative look-ahead making sure that
# systematics are not caught by the category definition.

# the sample string identifies things like this
# part1_part2_part3
# part1 = anything without an '_', may end in _obs
# part2 = anything without an '_'
# part3 = anything that is not followed by Up|Down,
#         this makes the sample extraction focus on the non-systematic
#         histograms
sample_re = re.compile(r'([^_]+(?:_obs)?)_([^_]+)_(.*)(?!(?:Up|Down)$)')
sample2_re = re.compile(r'([^_]+(?:_obs)?)_([^_]+)_([^_]+)_(.*)(?!(?:Up|Down)$)')
#sample_re = re.compile(r'([^_]+(?:_obs)?)_([^_]+)_(.*)(?!(?:Up||Down))')
#sample_re = re.compile(r'([^_]+(?:_obs)?)_([^_]+)_([^_]+)_(.*)(?!(?:Up|Down)$)')
signal1_re = re.compile(r'([^_]+(?:_obs)?)_([^_]+)_([^_]+)_(.*)(?!(?:Up|Down)$)')
signal_re = re.compile(r'(ttH).*')
#signal_re = re.compile(r'^(ttH).*_([^_]+)_([^_]+)_(.*)(?!(?:Up|Down)$)')
#signal_re = re.compile(r'^(ttH).*')

# This expression splits into 3 groups:
#   category_name:jet_multiplicity:parton_count
# The latter two are optional.
category_re = re.compile(r'(.*?)(?::(\d+)(?::(\d+))?)?$')

# This is the default logging instance (open file or stream)
log = sys.stderr

class IntegralException(Exception):
    """To catch integrals evaluating to zero.  `combine` does not like this
    for systematics.
    """
    pass

def get_ann_systematics(file, discriminant, categories, samples, data_sample="data_obs",
        signal_sample="ttH", is_13_tev=True):
    """For all samples and categories, this functions produces single bin
    systematics, shifts present in only one bin.  These shift will be
    produced when a process has significant expectation and the systematic
    is expected to contribute to the error.
    """

    print "get_ann_systematics"
    new_sys = []
    filename=file.GetName()
    

    for (c, j, p) in categories:
        bbbfile=r.TFile(filename.replace(".root","BBB_"+c+".root"),"RECREATE")
        data_hist = file.Get("{s}_{d}_{c}".format(s=data_sample, d=discriminant, c=c))
        sig_hist = file.Get("{s}_{d}_{c}".format(s=signal_sample, d=discriminant, c=c))
        bkg_hist = None

        # Build background sum
        for (s, cats) in samples.items():
            s = s if s == "ttH" else s
            if "ttH" in s:
                continue
            
            if s in (data_sample, signal_sample) or c not in cats:
                continue

            hist = file.Get("{s}_{d}_{c}".format(s=s, d=discriminant, c=c))
            if bkg_hist:
                bkg_hist.Add(hist)
            else:
                bkg_hist = hist.Clone()

        # Loop over samples for category and find low stats bins
        for (s, cats) in samples.items():
            file_s = s if s == "ttH" else s

            #if "ttH" in s:
                #continue

            if c not in cats:
                continue

            #hist = file.Get("{s}_{d}_{c}".format(s=file_s, d=discriminant, c=c))

            #for b in range(1, hist.GetNbinsX() + 1):
                #data = data_hist.GetBinContent(b)
                #data_err = math.sqrt(data_hist.GetBinContent(b))

                #sig = sig_hist.GetBinContent(b)
                #sig_err = sig_hist.GetBinError(b)

                #bkg = bkg_hist.GetBinContent(b)
                #bkg_err = bkg_hist.GetBinError(b)

                #val = hist.GetBinContent(b)
                #val_err = hist.GetBinError(b)

                #other_frac = math.sqrt(bkg_err**2 - val_err**2)

                #pruneBinByBin=True
                #if pruneBinByBin:
                ##Changed from data_err/3 -> data_err/5 and sig/bkg < 0.02 -> 0.01 - KPL
                  #if val < .01 or bkg_err < data_err / 5. or other_frac / bkg_err > .95 \
                        #or sig / bkg < .01:
                    #continue

                ##if True:
                ##    continue

                ## FIXME Subtract 1 from bin name for comparability with
                ## original C macro
                #sys_name = "CMS_ttH_{s}_{c}_{e}_BDTbin{b:d}".format(
                        #s=s, c=c, e="13TeV" if is_13_tev else "7TeV", b=b - 1)

                #stub = "{s}_{d}_{c}_".format(s=file_s, d=discriminant, c=c)
                #hist_up = hist.Clone(stub + sys_name + "Up")
                #hist_up.SetBinContent(b, val + val_err)
                #hist_down = hist.Clone(stub + sys_name + "Down")
                #hist_down.SetBinContent(b, val - val_err)

                #bbbfile.WriteObject(hist_up, hist_up.GetName())
                #bbbfile.WriteObject(hist_down, hist_down.GetName())

                #new_sys.append((sys_name, "shape",
                    #dict([(sam, ("1" if sam == s else "-")) for sam in samples.keys()])))
        bbbfile.Close()

    return new_sys


"""observed = map(
            lambda c: get_integral(file, discriminant, c, fmt="{n:.6f}"),
            map(lambda (c, j, p): c, categories))"""
def get_integral(file, discriminant, category, sample="data_obs", uncertainty="", fmt="{n:.3f}", throw=False):

    print "get_integral"
    """Get the integral of the histogram specified by the arguments.  The
    first argument has to be an open ROOT TFile.
    """
    if len(uncertainty) > 0:
        uncertainty = "_" + uncertainty
    h = file.Get("{s}_{d}_{c}{u}".format(s=sample, d=discriminant, c=category, u=uncertainty))
    i = h.Integral()
    if i <= 0. and throw:
        raise IntegralException("The integral for {s}, {d}, {c}, {u} in {f} is zero or even negativ!".format(
            s=sample, d=discriminant, c=category, u=uncertainty, f=file.GetName()))
    return fmt.format(n=h.Integral())

def get_samples(file, discriminant):

    print "get_samples"
    """Reads the contents of `file`, an open ROOT TFile, and tries to
    extract available categories per sample.
    """
    samples = {}
    keylist=file.GetListOfKeys()
    for k in keylist:
        keyname=k.GetName()
        if not discriminant in keyname:
            continue
        #m=False
        #m=False
        #r=False
        if "Up" in keyname or "Down" in keyname:
          continue
        m = sample_re.match(k.GetName())
        #print k.GetName(), m
        m2 = sample2_re.match(k.GetName())
        #print m2
        r = signal1_re.match(k.GetName())

##         if r:
##             #if "ttH" not in r.group(1):
##             #    continue

##             sample, decay, disc, cat = r.groups()

##             if disc != discriminant:
##                 continue

##             r = signal_re.match(sample)
##             if r:
##                 #log.write(" 1 signal = {s}, decay = {y}, disc = {d}, cat = {c}\n".format(s=sample, y=decay, d=disc, c=cat))
##                 sample = r.group(1)

##             sample += "_"+decay

##             if sample not in samples:
##                 samples[sample] = set()
##             samples[sample].add(cat)

##         if m:
##             #if "ttH" in m.group(1):
##             #    continue

##             sample, disc, cat = m.groups()

##             if disc != discriminant:
##                 continue

##             log.write(" 0 background = {s}, disc = {d}, cat = {c}\n".format(s=sample, d=disc, c=cat))
            
##             if sample not in samples:
##                 samples[sample] = set()
##             samples[sample].add(cat)

        if m:

            if "h"==m.group(1):
                continue
            
            #log.write(" 0 sample = {s}, two = {d}\n".format(s=m2.group(1),d=m2.group(2)))
            #if "ttH" not in m.group(1):
            #    continue

            if "ttH" in m.group(1) and "h" in m.group(2):
                #log.write("here 1\n")
                #print m2
                sample, decay, disc, cat = m2.groups()
                #log.write(" 0 sample = {s}, decay = {y}, disc = {d}, cat = {c}\n".format(s=sample, y=decay, d=disc, c=cat))
            else :
                #log.write("here 2\n")
                sample, disc, cat = m.groups()
                #print sample, disc, cat
                #log.write(" 0 sample = {s}, disc = {d}, cat = {c}\n".format(s=sample, d=disc, c=cat))
            #sample, disc, cat = m.groups()

            if disc != discriminant:
                continue

            ## NEW
            includeSig = True
            m = signal_re.match(sample)
            #log.write(" 0a k.GetName() = {k} \n".format(k=k.GetName()))
            if m and m2 and "h" in m2.group(2):
            #if m:
                #log.write(" 1 signal = {s}, disc = {d}, cat = {c}\n".format(s=sample, d=disc, c=cat))
                #sample = m.group(1)
                #sample = m.group(1) + "_" + m2.group(2)
                sample = m.group(1) + "_" + decay
                #log.write(" 2 sample = {s}, disc = {d}, cat = {c}\n".format(s=sample, d=disc, c=cat))

                ## NEW
                sig_name = sample
                sig_name = sig_name
                sig_hist = file.Get("{s}_{d}_{c}".format(s=sig_name, d=disc, c=cat))

                sum_sig = sig_hist.Integral()
                if not sum_sig>0 :
                    includeSig = False
            
            if sample not in samples:
                samples[sample] = set()
            #samples[sample].add(cat)
            ## NEW
            if includeSig :
                samples[sample].add(cat)

    print "getting samples done"   
    return samples

def get_systematics(file, overrides={}, rename=lambda u: u, samples=False):
    print "get_systematics"
    """Reads `file` and returns a list of (uncertainty, type, {sample:
    value}).

    The parameter `overrides` allows to specify a dict of form
    {uncertainty: value}, and values of "x" n the systematics file are
    replaced by the one specified in the dict.

    A function passed as `rename` allows to alter the uncertainty name,
    _after_ all other processing has happened.

    The parameter `samples` can be set to `True` to obtain the available
    sample names defined in the systematics file.
    """
    reader = csv.DictReader(open(file))
    reader.fieldnames = map(str.strip, reader.fieldnames)
    sys_samples = reader.fieldnames[2:]

    if samples:
        return sys_samples

    sys = []
    # create a list whose elements are the tuples
    # (uncertainty, type, {sample:value})
    # row is a list of the items in the row
    for row in reader:
        # comment character
        # if the line is not empty
        if len(row) >0:            
            # print row
            # if the row starts with comment #
            if re.match("^#", row["Uncertainty"]):
                continue
            # end if re.match
        # end if len
        unc = row.pop("Uncertainty").strip()
        type = row.pop("Type").strip()
        # `row` is a dictionary with sample names as keys.  Strip spaces
        # from the actual value
        row = dict(map(lambda (k,v): (k, v.strip()), row.items()))
        if unc in overrides:
            row = dict(
                    map(
                        lambda (k,v): (k, overrides[unc] if v == "x" else v),
                        row.items()))
        sys.append((rename(unc), type, row))
    return sys

def parse_btag_mode(s):
    if s == "off":
        return B_OFF
    elif s == "rate":
        return B_RATE
    elif s == "shape":
        return B_SHAPE
    elif s == "category":
        return B_CAT_SHAPE
    raise Exception("Invalid b-tag mode '{m}'".format(m=s))

def split_category_string(s):
    """Split a string of form "category:jets:partons" into components.
    Returns a list of a string and two integers.
    """
    print "split_category_string"
    def try_conv(v):
        try:
            return int(v)
        except:
            return v
    return map(try_conv, category_re.match(s).groups())

def split_q2(file, disc, categories):
    """Split Q2-systematics by parton number as specified in `categories`,
    which is a list containing tuples of `(category, jet_multiplicity,
    partons)`.
    """
    print "split_q2"
    for (c, j, p) in categories:
        print c
        print j 
        print p
        for d in ("Up", "Down"):
            try:
                oldname = "ttbar_{d}_{c}_Q2scale_ttH_ttbar{dir}".format(d=disc, c=c, dir=d)
                newname = "ttbar_{d}_{c}_Q2scale_ttH_ttbar{p}p{dir}".format(d=disc, c=c, p=p, dir=d)
                hold = file.Get(oldname)
                hnew = hold.Clone(newname)
                file.WriteObject(hnew, newname)
            except:
                log.write("Can't create Q^2 scale shifts for '{c}'\n".format(c=c))

def splitNPSF_forSS ( file, disc, categories, allSamples, systematicsToProcess):
    """ Non-prompt scale factor uncertainties
        Should be non-correlated across jet-tag categories
        Make some histograms so they can be non-correlated
        ***Inputs***
           file: a root file with input histograms
           disc: the name of the disciminant histograms to use
           categories: a list of tuples in the format
             (categoryName, numjets, numpartons)
       ***Outputs***
           returns a list of systematics to be added
    """
    print "splitNPSF_forSS"

    debugSplitNPSF = False

    # list of things that are prompt in your systematics input
    promptSystematics = []
    itemsToRemove = []
    for (sysName, sysType, sysSamples) in systematicsToProcess:
        if debugSplitNPSF: log.write("SYST: Name is {s}\n".format(s=sysName))
        if "Prompt" in sysName :            
            promptSystematics.append(sysName)
            if debugSplitNPSF: log.write("--->Removing {s}, adding it to prompt list\n".format(s=sysName))
            itemsToRemove.append((sysName, sysType, sysSamples))

    # If there are no prompt systematics to handle
    # then just return. 
    # Return value is a list of systematics.
    # It is the same as the input list.
    if len(promptSystematics) < 1:
        return systematicsToProcess
    
    for iThing in itemsToRemove:
        systematicsToProcess.remove(iThing)

    
    bkgsEffectedByNPSF = ["ttbar", "ttbarPlusB", "ttbarPlusBBbar", "ttbarPlusCCbar", "wjets"]
    listOfSystematicsToReturn = systematicsToProcess
    for (iCategoryName, iNumJets, iNumPartons) in categories:
        if debugSplitNPSF: log.write("What category is this? = {s}".format(s=iCategoryName))
        # if this isn't a SS dil category, skip it.
        if iCategoryName != "SS_ge4je1t" \
               and iCategoryName != "SS_e3jge2t" \
               and iCategoryName != "SS_ge4jge2t":
            continue

                
        shortCatName = iCategoryName.replace('_', '')        
        for iSystematic in promptSystematics:
            for iSample in bkgsEffectedByNPSF:
                for iShape in ["Up","Down"]:                    
                    oldName = "{s}_{d}_{c}_{sys}{shape}".format(s=iSample,
                                                                d=disc,
                                                                c=iCategoryName,
                                                                sys=iSystematic,
                                                                shape=iShape)
                    newName = "{s}_{d}_{c}_{sys}{short}{shape}".format(s=iSample,
                                                                d=disc,
                                                                c=iCategoryName,
                                                                short=shortCatName,
                                                                sys=iSystematic,
                                                                shape=iShape)
                    if debugSplitNPSF:
                        log.write("\n#####\nTrying to copy histo {0} to {1}\n".format(oldName,
                                                                                     newName))
                    
                    originalHisto = file.Get(oldName)
                    hist_new = originalHisto.Clone(newName)
                    file.WriteObject(hist_new, newName)

            
            # end for each sample
            # create a new systematic entry to return
            # this is a tuple with
            # (a,b,c)
            # a = systematic name
            # b = systematic type (shape, lnN)
            # c = dictionary of sample names and value like '1','-'
            returnDict = {}
            
            for (sampleNumber, sampleName) in allSamples:
                if sampleName in bkgsEffectedByNPSF:
                    returnDict[sampleName] = '1'
                else:
                    returnDict[sampleName] = '-'
            returnVal = ("{sys}{short}".format(short=shortCatName, sys=iSystematic),
                         "shape",
                         returnDict)
            listOfSystematicsToReturn.append(returnVal)
        # end for each sys

    # end for each category

    if debugSplitNPSF: log.write("DEBUG: Returning these systematics\n\n")
    for (a,b,c) in listOfSystematicsToReturn:
        if debugSplitNPSF: log.write("{a}, {b}, {c}\n".format(a=a, b=b, c=c))
    return listOfSystematicsToReturn
# end function

                    

def split_systematics(file, disc, samples, btag_mode=B_CAT_SHAPE):
    print "split_systematics"
    """Split b-tag uncertainties:  copy category histogram w/o systematics
    for rates, systematics of form "CMS_eff_bUp" to a shape uncertainty.

    The parameter `samples` should be a dictionary containing the
    categories per sample.

    Returns a list of systematics to be injected into the systematics file.
    """
    done = set()
    new_sys = []
    r.TH1.SetDefaultSumw2()

    if btag_mode == B_OFF:
        return new_sys

    for (s, cats) in samples.items():
        #s = s if s == "ttH" else s
        s = s if "ttH" in s else s
        for c in cats:
            stub = "_".join((s, disc, c))
            #log.write(" file.Get({s})".format(s=stub))
            orig = file.Get(stub)
            sum = orig.Integral()
            kind = "scale"
            #for kind in ("scale"):
            for dir in ("Up", "Down"):
                try:
                    # Get rate uncertainty from the shape uncertainty
                    shape_old = file.Get("{s}_CMS_{k}_j{dir}".format(s=stub, k=kind, dir=dir))
                    #log.write(" file.Get(\"{s}_CMS_{k}_j{dir}\"".format(s=stub, k=kind, dir=dir))
                    shape_sum = shape_old.Integral()
                    rate = orig.Clone("{s}_CMS_{k}_jRate{dir}".format(s=stub, k=kind, dir=dir))
                    rate.Scale((shape_sum / sum) if sum > 0 else 1)
                    file.WriteObject(rate, rate.GetName())
                    
                    # Treat shape uncertainties, if desired
                    if btag_mode == B_SHAPE:
                        shape = shape_old.Clone("{s}_CMS_{k}_jShape{dir}".format(s=stub, k=kind, dir=dir))
                    elif btag_mode == B_CAT_SHAPE:
                        shape = shape_old.Clone("{s}_{c}_{k}_jShape{dir}".format(s=stub, c=c, k=kind, dir=dir))
                    else:
                        continue

                    shape_sum = shape.Integral()
                    shape.Scale((sum / shape_sum) if shape_sum > 0 else 1)

                    file.WriteObject(shape, shape.GetName())
                except:
                    log.write("Can't create b-tag shape uncertainties for '{s}'"
                                "in '{c}'\n".format(s=c, c=c))
            #new_sys.append((
            #    "CMS_{k}_jRate".format(k=kind),
            #    "shape",
            #    dict([(sam, "1") for sam in samples.keys()])))                   
            if btag_mode == B_SHAPE and 'all' not in done:
                new_sys.append((
                    "CMS_{k}_jShape".format(k=kind),
                    "shape",
                    dict([(sam, "1") for sam in samples.keys()])))
            elif btag_mode == B_CAT_SHAPE and c not in done:
                new_sys.append((
                    "{c}_{k}_jShape".format(c=c, k=kind),
                    "shape",
                    dict([(sam, "1") for sam in samples.keys()])))
        done.add('all')
        done.add(c)
    # For debugging
    #log.write("DEBUG: We are appending these systematics\n")
    #for (a,b,c) in new_sys:
    #    log.write("{a}, {b}, {c}\n".format(a=a, b=b, c=c))
    #log.write("\n\n")
    return new_sys

def write_datacard(file, discriminant, categories, cats, samples, systematics,
        limited_systematics={}, ofile=log, is13TeV=True):
    """
    """
    print "write_datacard"
    filename = file.GetName()
    observed = map(
            lambda c: get_integral(file, discriminant, c, fmt="{n:.6f}"),
            map(lambda (c, j, p): c, categories))

    if "data_obs" in cats:
        del cats["data_obs"]

    bins = []
    for (n, s) in samples:
        bins += cats[s]

    sprocs = "".join(map(lambda (n, s): (" " + s) * len(cats[s]), samples))

    ## OLD
    #nprocs = "".join(map(lambda (n, s): (" " + str(n)) * len(cats[s]), samples))
    
    ## NEW
    nprocs = []
    iProcess = 0
    last_s = "ttH"
    nTTHprocesses=0
    for (n, s) in samples:
        for c in cats[s]:
            #log.write("\t sample = {ss},\t process = {pp}\n".format(ss=s,pp=iProcess))
            if "ttH" in s:
                #nprocs += "0"
                # do different negative numbers for the different tth decay channels
                nprocs.append(str(0-nTTHprocesses))
                nTTHprocesses+=1
                ##nprocs += "".join((" 0") * len(cats[s]))
            else:
                if s != last_s :
                    iProcess += 1
                #nprocs += str(iProcess)
                nprocs.append(str(iProcess))
                ##nprocs += "%s" % (iProcess)
                ##nprocs += "".join((" %s" % (iProcess)) * len(cats[s]))
                last_s = s

    nprocs = " ".join(nprocs)

    ## OLD
    #rates = ["-1"] * len(cats["ttH"])
    #for (n, s) in samples[1:]:
    #    for c in cats[s]:
    #        rates.append(str(get_integral(file, discriminant, c, s, fmt="{n:.6}")))

    ## NEW
    rates = []
    for (n, s) in samples:
        for c in cats[s]:
            #log.write("Samples: {cs}\n".format(cs=s))
            if "ttH" in s:
                rates.append("-1");
            else:
                rates.append(str(get_integral(file, discriminant, c, s, fmt="{n:.6}")))

    # Print preamble
    ofile.write("""imax * # number of channels
jmax * # number of backgrounds
kmax * # number of nuisance parameters
---------------
bin {c}
observation {o}
---------------
shapes * * {f} $PROCESS_{d}_$CHANNEL $PROCESS_{d}_$CHANNEL_$SYSTEMATIC
shapes ttH_hbb * {f} ttH_hbb_{d}_$CHANNEL ttH_hbb_{d}_$CHANNEL_$SYSTEMATIC
shapes ttH_hcc * {f} ttH_hcc_{d}_$CHANNEL ttH_hcc_{d}_$CHANNEL_$SYSTEMATIC
shapes ttH_hww * {f} ttH_hww_{d}_$CHANNEL ttH_hww_{d}_$CHANNEL_$SYSTEMATIC
shapes ttH_hzz * {f} ttH_hzz_{d}_$CHANNEL ttH_hzz_{d}_$CHANNEL_$SYSTEMATIC
shapes ttH_htt * {f} ttH_htt_{d}_$CHANNEL ttH_htt_{d}_$CHANNEL_$SYSTEMATIC
shapes ttH_hgg * {f} ttH_hgg_{d}_$CHANNEL ttH_hgg_{d}_$CHANNEL_$SYSTEMATIC
shapes ttH_hgluglu * {f} ttH_hgluglu_{d}_$CHANNEL ttH_hgluglu_{d}_$CHANNEL_$SYSTEMATIC
shapes ttH_hzg * {f} ttH_hzg_{d}_$CHANNEL ttH_hzg_{d}_$CHANNEL_$SYSTEMATIC
---------------
bin {bs}
process {ps}
process {ns}
rate {rs}
---------------
""".format(
    c=" ".join(map(lambda (c, j, p): c, categories)),
        o=" ".join(map(str, observed)),
        d=discriminant,
        f=filename,
        bs=" ".join(bins),
        ps=sprocs,
        ns=nprocs,
        rs=" ".join(rates)))

    active_unc = []
    debugUncert = False
    fail = False
    listOfFailures = []
    for (unc, type, vals) in systematics:
        if debugUncert: log.write("-----------------------------------------------")
        if debugUncert: log.write("Considering uncert %s\n   type = %s\n   vals = %s\n" % (unc, type, vals))
        active = False

        ofile.write("{u} {t}".format(u=unc, t=type))
        for (n, s) in samples:
            if debugUncert: log.write("This is sample %s (also %s) \n" % (s,n))
            ## OLD
            #file_s = s if s == "ttH" else s
            ## NEW
            s_new = s
            #log.write(" was = {ss}\n".format(ss=s_new))
            if "ttH" in s:
                #log.write(" HELLO WORLD n")
                #s_new = s + "_M125"
                s_new = s_new
            #log.write(" is = {ss}\n".format(ss=s_new))
            file_s = s_new
            #log.write(" file_s = {s}\n".format(s=file_s))
            for c in cats[s]:
                if debugUncert:
                    log.write("This is category %s\n" %c)

                # Switch the lepton uncertainty value
                if unc == "CMS_ttH_eff_lep" and is13TeV:                    
                    if c in ["ge3t", "e3je2t", "ge4je2t"]:                        
                        vals[s] = 1.028
                    else:                        
                        vals[s] = 1.014
                # end if lepton uncertainty

                if unc in limited_systematics and not limited_systematics[unc](c):
                    ofile.write(" -")
                elif type == "shape" and vals[s] != "-":
                    try:
                        get_integral(file, discriminant, c, file_s, unc + "Up", throw=True)
                        get_integral(file, discriminant, c, file_s, unc + "Down", throw=True)
                        ofile.write(" " + vals[s])
                        active = True
                    except IntegralException, e:
                        ofile.write(" -")
                        # Print for everything _except_ for b-tag shape or ANN
                        # uncertainties with inappropriate category
                        if not (not unc.startswith(c) and ("jShape" in unc or "BDTbin" in unc)):
                            log.write("Integral zero or negativ for {s}, {c}, {u}: disabling "
                                    "systematics\n".format(s=s, c=c, u=unc))
                    except:
                        ofile.write(" -")
                        #print "ewhat"

                        barf = True
                        try:
                            # Find parton count for current category
                            parton = filter(lambda (cat, j, p): cat == c, categories)[0][2]
                            m = re.match(r'Q2scale_ttH_ttbar(\d)p$', unc)
                            if m:
                                # Don't complain if we have the wrong
                                # parton count
                                if int(m.group(1)) != parton:
                                    barf = False
                        except:
                            pass

                        # Don't complain if we consider category-specific
                        # uncertainties and are in the wrong category
                        if ("jShape" in unc or "BDTbin" in unc or "Prompt" in unc or "Flip" in unc) and not unc.startswith(c):
                            barf = False

                        if barf:
                            log.write("Integral not available for {s}, {c}, {u}: disabling "
                                    "systematics\n".format(s=s, c=c, u=unc))

                            #log.write("DEBUG: Failure caused by this uncertainty {s} {c} {u}\n\n".format(s=s,c=c,u=unc)) 
                            #fail = True
                            listOfFailures.append((s,c,unc))
                elif vals[s] in ["-", "1"] and not \
                        (unc == "Q2scale_ttH_V" and s in ("wjets", "zjets")):
                    ofile.write(" " + vals[s])
                    if vals[s] == "1":
                        active = True
                else:
                    # Q2 scale for wjets/zjets
                    # This uncertainty depends on the jet multiplicty
                    if unc == "Q2scale_ttH_V" and s in ("wjets", "zjets"):
                        try:
                            # If this category is in your list of categories
                            # find out the parton multiplicty
                            # This pulls out the first entry in the list returned
                            # by the filter
                            # Then pullos out the first entry in the list, then
                            # gets the first value associated with it, which is
                            # the number of jets
                            mult = filter(lambda (cat, j, p): cat == c, categories)[0][1]

                            # The uncertainty will be 10% per jet
                            vals[s] = str(1 + .1 * mult)
                        # This will be triggered if the jet-multiplicity is
                        # not defined (`None`)
                        except:
                            ofile.write(" -")
                            continue
                    active = True
                    ## old function for calculating kappa
                    #new_val = math.e ** (math.sqrt(math.log(1 + (float(vals[s]) - 1)**2)))
                    ## new function for calculating kappa to give expected correct AVERAGE uncertainty
#                    new_val= float(vals[s])
#                    if transformLnN:
#                        new_val = (float(vals[s]) - 1) + math.sqrt( 1 + (float(vals[s]) - 1)**2 )
                    ofile.write(" "+vals[s])
        ofile.write("\n")

        if active:
            active_unc.append(unc)

    ofile.write("---------------\n")

    if fail:
        log.write("Crashing because the following uncertainties\n"
                  +"Are missing histograms")
        for (iSample, iCategory, iUncertainty) in listOfFailures:
            log.write("DEBUG: {s} {c} {u}".format(s=iSample, c=iCategory, u=iUncertainty))
        raise Exception("FAILED TO FIND ALL UNCERTAINTIES! "
                "INCOMPLETE DATACARD PRODUCED!")

    return active_unc

def create_datacard(ifile, ofile, disc, all_categories,
        disabled_systematics=[], disabled_samples=[], limited_systematics={},
        btag_mode=B_CAT_SHAPE, print_summary=False):
    print "create_datacard"
    """Create a datacard for `ifile` (an open ROOT file) using the
    discriminant `disc` and categories, jet multiplicities, parton counts
    defined in `all_categories`.
    """
    print os.path.dirname(__file__)
    sysfile = os.path.join(os.path.dirname(__file__), "systematics_hdecay13TeVJESTest.csv")
    all_category_names = map(lambda (c, j, p): c, all_categories)

    is_13_tev = True
    def rename(unc):
        if unc == "lumi":
            return unc + "_13TeV_2016" if is_13_tev else unc + "_7TeV"
        return unc

    # This replaces "x" in the systematics csv file with the values specified
    # for certain uncertainties
    overrides = {
            "lumi_13TeV_2017": "1.023" if is_13_tev else "1.023",
            "CMS_ttH_eff_lep": "1.015" if is_13_tev else "1.015",
            "CMS_ttHbb_bgnorm_ttbarPlusB_2017": "1.5",
            "CMS_ttHbb_bgnorm_ttbarPlus2B_2017": "1.5",
            "CMS_ttHbb_bgnorm_ttbarPlusBBbar_2017": "1.5",
            "CMS_ttHbb_bgnorm_ttbarPlusCCbar_2017": "1.5",
            "CMS_ttHbb_bgnorm_ttbarPlusB": "1.5",
            "CMS_ttHbb_bgnorm_ttbarPlus2B": "1.5",
            "CMS_ttHbb_bgnorm_ttbarPlusBBbar": "1.5",
            "CMS_ttHbb_bgnorm_ttbarPlusCCbar": "1.5",
            }

    # Retrieve list of samples (ordered) from systematics file
    samples = get_systematics(sysfile, samples=True)
    samplesAll = samples
    # Get available categories for every sample
    all_samples = get_samples(ifile, disc)

    # Trim previous to the samples defined in the systematics file and filter
    # categories to the ones defined above
    cats = dict(map(
            lambda (k, cs): (k, filter(lambda c: c in cs, all_category_names)),
            filter(
                lambda (k, cs): k in samples,
                all_samples.items())))

    # Enumerate samples for combine
    # nums = dict([(s, n) for (n, s) in enumerate(samples)])
    samples = filter(lambda s: s not in disabled_samples, samples)
    samples = enumerate(samples)

    #for (n, s) in samples:
    #    for c in cats[s]:
    #        log.write("-1 Samples: {cs}\n".format(cs=s))
    print "getting systematics"
    systematics = get_systematics(sysfile, overrides=overrides, rename=rename)
    #print systematics
    all_uncertainties = map(lambda (u, t, vs): u, systematics)
    systematics = filter(lambda (u, t, vs): u not in disabled_systematics, systematics)
    #systematics += split_systematics(ifile, disc, cats, btag_mode)
    print "adding bin by bin uncertainties"
    systematics += get_ann_systematics(ifile, disc, all_categories, cats, is_13_tev=is_13_tev)

    ## Filter out b-tag rate uncertainties
    #if btag_mode == B_OFF:
        #systematics = filter(lambda (u, t, vs): "jRate" not in u, systematics)

    new_cats = set()
    for (s, cs) in cats.items():
        for c in cs:
            new_cats.add(c)
    new_cats = list(new_cats)
    categories = filter(lambda (c, j, p): c in new_cats, all_categories)

    #for (n, s) in samples:
    #    for c in cats[s]:
    #        log.write("0 Samples: {cs}\n".format(cs=s))

    # keep only essential samples
    samples = filter(lambda (n, s): s in cats, samples)

    #for (n, s) in samples:
    #    for c in cats[s]:
    #        log.write("1 Samples: {cs}\n".format(cs=s))

    #split_q2(ifile, disc, categories)


    # split up the non-prompt scale factor uncertainties
    # remove baseline NPSF uncertainties
    #systematics = splitNPSF_forSS (ifile, disc, categories, samples, systematics)

    #log.write ("\n>>>>>>>>>>>>>>>>>>>>>>AFTER SPLIT<<<<<<<<<<<<<<<<<<<\n")
    #for (sysName, sysType, sysSamples) in systematics:
    #    log.write("SYST: Name is {s}\n".format(s=sysName))
    print "starting write datacard"
    active_unc = write_datacard(ifile, disc, categories, cats, samples,
            systematics, limited_systematics, ofile=ofile, is13TeV=is_13_tev)

    if not print_summary:
        return

    category_names = map(lambda (c, j, p): c, categories)

    cstring = " ".join(map(lambda c: c if c in category_names else "[" + c + "]",
        all_category_names)).replace("] [", " ")
    sstring = " ".join(map(lambda s: s if s in all_samples.keys() and s not in disabled_samples else "[" + s + "]",
        samplesAll)).replace("] [", " ")
    ustring = " ".join(map(lambda u: u if u in active_unc else "[" + u + "]",
        all_uncertainties)).replace("] [", " ")

    log.write("""
Executive Summary
=================

Included in Datacard
--------------------
Categories:    {cs}
Samples:       {ss}
Uncertainties: {us}
~~~
Disabled objects present within []s
""".format(cs=cstring, ss=sstring, us=ustring))
