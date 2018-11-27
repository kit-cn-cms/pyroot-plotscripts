# from __future__ import unicode_literals
import os
import sys
import glob
import ROOT
ROOT.ROOT.EnableImplicitMT()
categoriesJT=[
	("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
	("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
	("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
	("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
	("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
	("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
	("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
]

path_karim="/nfs/dust/cms/user/kelmorab/ttH_2018/ntuples_v2"
path_matsch="/nfs/dust/cms/user/kelmorab/ttH_2018/ntuples_v3"
path_pkeicher="/nfs/dust/cms/user/pkeicher/ttH_2018/naf_jobs_for_Karim/ntuples"
path_mwassmer="/nfs/dust/cms/user/mwassmer/ttH_2018/ntuples"
default_sample_paths = []
default_sample_paths.append(path_karim+'/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_new_pmx/*1_nominal*.root')
default_sample_paths.append(path_mwassmer+'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_new_pmx/*1_nominal*.root')
default_sample_paths.append(path_karim+'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/*1_nominal*.root')
default_sample_paths.append(path_karim+'/DYJets*/*1_nominal*.root')
default_sample_paths.append(path_mwassmer+'/WJets*/*1_nominal*.root')
default_sample_paths.append(path_pkeicher+'/TTW*/*1_nominal*.root')
default_sample_paths.append(path_pkeicher+'/TTZ*/*1_nominal*.root')
default_sample_paths.append(path_mwassmer+'/WW_*/*1_nominal*.root')
default_sample_paths.append(path_mwassmer+'/WZ_*/*1_nominal*.root')
default_sample_paths.append(path_mwassmer+'/ZZ_*/*1_nominal*.root')
default_sample_paths.append(path_pkeicher+'/ST_*/*1_nominal*.root')
default_sample_paths.append(path_mwassmer+'/ttHTo*/*1_nominal*.root')
default_sample_paths.append(path_karim+'/SingleMuon*/*1_nominal*.root')
default_sample_paths.append(path_karim+'/SingleElectron*/*1_nominal*.root')


plot_template = 'Plot(ROOT.TH1D(%(HNAME)s,%(TITLE)s,30,%(LOWEDGE)s,%(UPEDGE)s),%(VARNAME)s,%(SELECTION)s,%(LABEL)s),'
analyze_flag = "Plot("

def find_elements_in_brackets(lineargs):
	start = None
	end = None
	opened = 0
	closed = 0
	for i, arg in enumerate(lineargs):
		if "(" in arg:
			# print "setting start to", i
			opened += arg.count("(")
			if start is None: start = i
		if ")" in arg:
			closed += arg.count(")")
		if opened == closed and not opened == 0 and not closed == 0:
			end = i+1
			# print "FOUND END AT", end
			break
	return start, end

def parse_hist_args(histodef):
	#cut everything before the first bracket away. Also remove bracket at the end
	histoargs = histodef[histodef.index("(")+1:-1]
	histoargs = histoargs.split(",")

	#check if there was something with brackets in the histo arguments
	start, end = find_elements_in_brackets(histoargs)
	if not (start is None or end is None):
		histoargs = histoargs[:start] + [",".join(histoargs[start:end])] + histoargs[end:]
	return histoargs

def parse_line_args(line):
	# print "found", line
	lineargs = line[len(analyze_flag):]
	if lineargs.endswith("),"):
		lineargs = lineargs[:-2]
	elif lineargs.endswith(")"):
		lineargs = lineargs[:-1]
	lineargs = lineargs.split(",")
	#reassemble TH1 definition
	start, end = find_elements_in_brackets(lineargs)
			
	if not (start is None or end is None):
		lineargs = [",".join(lineargs[start:end])] + lineargs[end:]
	else:
		if start is None:
			print "COULD NOT FIND START"
		if end is None:
			print "COULD NOT FIND END"
		print "could not find TH1 definition, will skip this line"
		print lineargs
		print line
		lineargs = [" "]

	return lineargs

def load_variable(line, varinfos, selection_line):
	exec(selection_line)
	lineargs = parse_line_args(line)
	# print lineargs
	if not len(lineargs) == 4:
		print line
		print lineargs
		print "This line has too few arguments! Skipping"
		return None
	histodef = lineargs[0]
	varname = lineargs[1]
	selection = lineargs[2]
	label = lineargs[3]
	hargs = parse_hist_args(histodef)
	if not len(hargs) == 5:
		print "ERROR: Wrong number of histo arguments for TH1D! Skipping"
		print hargs
		print line
		return None
	hname = hargs[0]
	htitle = hargs[1]
	hbins = hargs[2]
	if not varname in varinfos:
		#DANGERZONE
		#The structure of this dict should contain the EXACT same keywords as
		#in 'plot_template'! It's used to replace the keywords later
		varinfos[varname] = {
			"HNAME" 	: hname,
			"TITLE"	: htitle,
			"SELECTION"	: selection,
			"real_selection": selection if '"' in selection else eval(selection),
			"LABEL"		: label,
			"VARNAME"	: varname
		}
	else:
		print "ERROR: Already loaded variable '%s'" % varname

def collect_file_infos(filepath):
	lines = []
	prefix_line = None
	selection_line = None
	with open(filepath) as f:
		lines = f.read().splitlines()
	read = False
	infos = {}
	for i, line in enumerate(lines):
		line = line.strip()
		if line == "discriminatorPlots=plots":
			print "DONE collecting!"
			break
		if line.startswith("#"):
			# print "-"*150
			# print "skipping line"
			# print line
			# print "-"*150
			continue
		# print line
		if not selection_line and "selection" in line:
			selection_line = line
			# print "evaluating line"
			# print selection_line
			exec(selection_line)

		elif prefix_line is None and "prefix" in line:
			prefix_line = line
			# print "evaluating line"
			# print prefix_line
			exec(prefix_line)
			prefix = eval(line[:line.index("=")])

		if not read and line.endswith("["):
			if not (selection_line is None or prefix_line is None):
				read = True
				print "saving prefix", prefix
				infos[prefix] = {}

		if read and line.startswith(analyze_flag):
			load_variable(line = line, varinfos = infos[prefix], selection_line = selection_line)
			# print varinfos.keys()

		if read and line.endswith("]"):
			read = False
			if len(infos[prefix]) == 0:
				print "Deleting entry for prefix '%s' because it's empty!" % prefix
				del infos[prefix]
				
			prefix_line = None
			selection_line = None

	print "collected these prefixes"
	print infos.keys()
	return infos

def create_chain(ntuplepaths = None):
	chain = ROOT.TChain("MVATree")
	if not ntuplepaths is None and len(ntuplepaths) != 0:
		for path in ntuplepaths:
			if os.path.exists(path):
				chain.Add(path)
	else:
		for entry in default_sample_paths:
			chain.Add(entry)
	return chain

def guess_ranges(infos, ntuplepaths=None):
	chain = create_chain(ntuplepaths)
	TDF = ROOT.RDataFrame
	df = TDF(chain)
	branchlist = [x.GetName() for x in chain.GetListOfBranches()]
	print "list of branches:"
	print branchlist
	# print df
	# nevents = chain.GetEntries()
	nevents = df.Count().GetValue()
	print "Looking for edges with {0} events".format(nevents)
	varlist = []
	for prefix in infos:
		varlist = list(set(varlist + infos[prefix].keys()))
	filterdict = {}
	for v in varlist:
		print "get edges for variable '%s'" % v
		for prefix in infos:
			if not v in infos[prefix]:
				continue
			valdic = infos[prefix][v]
			vstring = eval(v) if '"' in v else v
			print vstring
			if not vstring in branchlist:
				print "WARNING: Branch '%s' does not exist!" % v
				print "You will have to find the edges on your own"
				maxval = "FIXME"
				minval = "FIXME"
			else:
				print "selection:"
				print valdic["real_selection"]
				selec = valdic["real_selection"]
				if not selec in filterdict:
					filterdict[selec] = {
						"filtered_events" : df.Filter(selec),
						}
					filterdict[selec]["count"] = filterdict[selec]["filtered_events"].Count().GetValue()	
				filtered_events = filterdict[selec]["filtered_events"]
				print "selected events: {0}/{1}".format(filterdict[selec]["count"], nevents)
				minvalgraph = filtered_events.Min(vstring)
				maxvalgraph = filtered_events.Max(vstring)
				minval = round(minvalgraph.GetValue(), 2)
				maxval = round(maxvalgraph.GetValue(), 2)

			valdic["LOWEDGE"] = minval
			valdic["UPEDGE"] = maxval

def write_histo_lines(vardictionary):
	lines = []
	for prefix in vardictionary:
		lines.append("PREFIX: " + prefix)
		dic = vardictionary[prefix]
		for var in dic:
			l = plot_template % (dic[var])
			lines.append("\t"+l)
	with open("guessed_ranges.txt", "w") as f:
		f.write("\n".join(lines))

def main(args = sys.argv[1:]):
	filepath = args[0]
	ntuplepaths = args[1:]
	infos = collect_file_infos(filepath)
	guess_ranges(infos = infos, ntuplepaths = ntuplepaths)
	write_histo_lines(vardictionary = infos)

if __name__ == '__main__':
	main()

