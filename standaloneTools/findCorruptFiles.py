import ROOT
import sys
import glob
from multiprocessing import Pool
from tqdm import *
import os
import subprocess

class DevNull:
    def write(self, msg):
        pass

def check_root_files_(path = ""):
    isGOOD = True
    isEMPTY = False
    rf = ROOT.TFile.Open(path)
    if rf == None or len(rf.GetListOfKeys()) == 0:
        isEMPTY = True
        print ("EMPTY        "), path
    elif rf.TestBit(ROOT.TFile.kZombie):
        isGOOD = False
        print ("ZOMBIE        "), path
    elif rf.TestBit(ROOT.TFile.kRecovered):
        isGOOD = False
        print ("BROKEN        "), path
    if rf != None:
        rf.Close()
    # if isEMPTY: return "empty"
    # if isGOOD:  return "good"
    if isEMPTY or not isGOOD:
        return path
    else:
        return ""


def imap_unordered_bar(func, args, n_processes = 8):
    p = Pool(n_processes)
    res_list = []
    # with redirect_stdout(out), redirect_stderr(err):
    with tqdm(total = len(args)) as pbar:
        for i, res in tqdm(enumerate(p.imap_unordered(func, args))):
            pbar.update()
            res_list.append(res)
    pbar.close()
    p.close()
    p.join()
    return res_list

def find_broken_files(indirs = sys.argv[1:], ext = ".root"):
    """find empty or corrupted input root files

    Args:
        indirs (list, optional):    list of input directories. For each item
                                    a wildcard for .root files (*.root) is 
                                    appended. The file list ist generated using
                                    the 'glob' module. Defaults to sys.argv[1:].
    """    
    brokenFiles = []
    emptyFiles = []
    print(indirs)

    fileList = []

    print("#"*40)
    print("checking following directories ")
    print("#"*40)
    #extend wildcard expressions
    notexistent = []
    inputs = []
    for x in indirs:
        inputs += glob.glob(x)
    for dir_ in indirs:
        if os.path.isfile(dir_):
            fileList.append(dir_)
        elif os.path.isdir(dir_):
            fileList += glob.glob(os.path.join(dir_+"*{}".format(ext)))
        else:
            print("ERROR: cannot process {} - it's neither a file nor a dir".format(dir_))
            print("CAREFUL: appending it to list of notexistent files!")
            if ".root" in dir_:
                notexistent.append(dir_)

    # print(fileList)

    print("#"*40)
    print("checking {0} rootfiles ".format(len(fileList)))
    print("#"*40)

    brokenFiles = imap_unordered_bar(check_root_files_, fileList)
    brokenFiles = [x for x in brokenFiles if not x == ""]
    brokenFiles += notexistent

    # removing cutflow file from on existent root files
    for f in notexistent:
        print("deleting cutflow, since root file is missing: {}".format(f+".cutflow.txt"))
        subprocess.call("rm "+f+".cutflow.txt", shell =True)
         

    print("{0} files broken".format(len(brokenFiles)))
    return brokenFiles
    
if __name__ == "__main__":
    
    brokenFiles = find_broken_files()
    with open("broken_files.txt", "w") as f:        
        f.write("\n".join(brokenFiles))
# with open("empty_files.txt", "w") as f:
#     f.write("\n".join(emptyFiles))


