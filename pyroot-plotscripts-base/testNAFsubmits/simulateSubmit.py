import os
import nafSubmit

print( "removing all data from previous tests...")
os.system("rm -r logs/*")
os.system("rm scripts/*.txt")
os.system("rm scripts/ats*")
os.system("rm scripts/*.sub")


base = os.getcwd()

# helperSubmitNAFJobs:
print("-"*50 + "\ntesting helperSubmitNAFJobs\n")
scripts = [base + "/scripts/test1_helper.sh", base + "/scripts/test2_helper.sh"]
outputs = [base + "/scripts/test1_helper.root", base + "/scripts/test2_helper.root"]
nentries = [1, 2]

success = nafSubmit.helperSubmitNAFJobs(scripts, outputs, nentries)
if success:
    print("helperSubmitNAFJobs test successfull")

# submitArrayToNAF:
print("-"*50 + "\ntesting submitArrayToNAF\n")
scripts = [base + "/scripts/test1_array.sh", base + "/scripts/test2_array.sh"]
outputs = [base + "/scripts/test1_array.root", base + "/scripts/test2_array.root"]
nentries = [3,4]
arrayName = "testArray"

jobidlist = nafSubmit.submitArrayToNAF(scripts, arrayName)
nafSubmit.do_qstat(jobidlist)
failed_jobs = nafSubmit.check_jobs(scripts,outputs,nentries)
if len(failed_jobs)==0:
    print("submitArrayToNAF test successfull")
else:
    print("something went wrong with submitArrayToNAF...")

# submitToNAF:
print("-"*50 + "\ntesting submitToNAF\n")
scripts = [base + "/scripts/test1_single.sh", base + "/scripts/test2_single.sh"]
outputs = [base + "/scripts/test1_single.root", base + "/scripts/test2_single.root"]
nentries = [5,6]

jobids = nafSubmit.submitToNAF(scripts)
nafSubmit.do_qstat(jobids)
failed_jobs = nafSubmit.check_jobs(scripts,outputs,nentries)
if len(failed_jobs) == 0:
    print("submitToNAF test successfull")
else:
    print("something went wrong with submitToNAF...")
