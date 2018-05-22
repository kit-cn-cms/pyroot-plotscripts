import os
import sys
dirpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dirpath+"/../")
import nafSubmit

print( "removing all data from previous tests...")
os.system("rm -r logs/*")
os.system("rm -r scripts/*.txt")
os.system("rm -r scripts/ats*")
os.system("rm -r scripts/*.sub")


base = os.getcwd()

# submit.py list of scripts
print("-"*50 + "\ntesting submit.py with multiple scripts\n")
scripts = [base + "/scripts/test1_sup.sh", base + "/scripts/test2_sup.sh"]
outputs = [base + "/scripts/test1_sup.root", base + "/scripts/test2_sup.root"]
nentries = [10,11]
command = "python submit.py "+" ".join(scripts)

os.system(command)
nafSubmit.do_qstat(False)
failed_jobs = nafSubmit.checkJobs(scripts,outputs,nentries)
if len(failed_jobs) == 0:
    print("sup.py test successfull")
else:
    print("sup.py test not successfull")

# submit.py with folder
print("-"*50 + "\ntesting submit.py with folder\n")
scripts = [base + "/scripts/supfolder/test1.sh", base + "/scripts/supfolder/test2.sh"]
outputs = [base + "/scripts/supfolder/test1.root", base + "/scripts/supfolder/test2.root"]
nentries = [12,13]
command = "python submit.py -f scripts/supfolder"

os.system(command)
nafSubmit.do_qstat(False)
failed_jobs = nafSubmit.checkJobs(scripts,outputs,nentries)
if len(failed_jobs) == 0:
    print("sup.py test with folder successfull")
else:
    print("sup.py test with folder not successfull")

# helperSubmitNAFJobs:
print("-"*50 + "\ntesting helperSubmitNAFJobs\n")
scripts = [base + "/scripts/test1_helper.sh", base + "/scripts/test2_helper.sh"]
outputs = [base + "/scripts/test1_helper.root", base + "/scripts/test2_helper.root"]
nentries = [1, 2]

success = nafSubmit.helperSubmitNAFJobs(scripts, outputs, nentries)
if success:
    print("helperSubmitNAFJobs test successfull")
else:
    print("helperSubmitNAFJobs test not successfull")

# submitToNAF:
print("-"*50 + "\ntesting submitToNAF\n")
scripts = [base + "/scripts/test1_single.sh", base + "/scripts/test2_single.sh"]
outputs = [base + "/scripts/test1_single.root", base + "/scripts/test2_single.root"]
nentries = [5,6]

jobids = nafSubmit.submitToNAF(scripts)
jobids2 = nafSubmit.submitToNAF(scripts, holdIDs = jobids)

nafSubmit.do_qstat(jobids+jobids2)
failed_jobs = nafSubmit.checkJobs(scripts,outputs,nentries)
if len(failed_jobs) == 0:
    print("submitToNAF test successfull")
else:
    print("something went wrong with submitToNAF...")

# submitArrayToNAF:
print("-"*50 + "\ntesting submitArrayToNAF\n")
scripts = [base + "/scripts/test1_array.sh", base + "/scripts/test2_array.sh"]
outputs = [base + "/scripts/test1_array.root", base + "/scripts/test2_array.root"]
nentries = [3,4]
arrayName = "testArray"

jobidlist = nafSubmit.submitArrayToNAF(scripts, arrayName)
jobidlist2 = nafSubmit.submitArrayToNAF(scripts, arrayName, holdIDs = jobidlist)
nafSubmit.do_qstat(jobidlist+jobidlist2)
failed_jobs = nafSubmit.checkJobs(scripts,outputs,nentries)
if len(failed_jobs)==0:
    print("submitArrayToNAF test successfull")
else:
    print("something went wrong with submitArrayToNAF...")
