# usage: run in folder with LJ datacards with 'python renameSys.py oldname newname'

import ROOT
import subprocess
import sys
from glob import glob

def renameShapes(shapesfile,oldname,newname):
    print 'trying to update',shapesfile,'(can take a minute)'
    f=ROOT.TFile(shapesfile,'update')
    keys=f.GetListOfKeys()
    oldnames=[]
    nchanged=0
    for k in keys:
        kname=k.GetName()
        upsuffixold='_'+oldname+'Up'
        downsuffixold='_'+oldname+'Down'
        upsuffixnew='_'+newname+'Up'
        downsuffixnew='_'+newname+'Down'
        if kname.endswith(upsuffixold) or kname.endswith(downsuffixold):
            o=f.Get(kname).Clone()
            if kname.endswith('Up'):
                o.SetName(kname.replace(upsuffixold,upsuffixnew))
            if kname.endswith('Down'):
                o.SetName(kname.replace(downsuffixold,downsuffixnew))
            o.Write()
            f.Delete(kname+';*')
            nchanged+=1

    f.Close()
    print 'renamed',nchanged,'histos'
    return nchanged

def renameCard( datacardpattern,oldname,newname):
    delim='/'
    toreplace=oldname+' '
    replacewith=newname+' '
    datacards=glob(datacardpattern)
    print 'replacing systematic in',' '.join(datacards)
    command=['sed', '-i', 's'+delim+toreplace+delim+replacewith+delim+'g']+datacards
    subprocess.call(command)
    
def renamePath( datacardpattern,testname):
    delim='/'
    toreplace='common'
    replacewith='test'+testname+'common'
    datacards=glob(datacardpattern)
    print 'replacing paths in',' '.join(datacards)
    command=['sed', '-i', 's'+delim+toreplace+delim+replacewith+delim+'g']+datacards
    subprocess.call(command)
            

def renameSysSL(oldname,newname,testname=""):    
    shapesfile='common/ttH_hbb_13TeV_sl.root'
    datacardpattern='ttH_hbb_13TeV_sl*.txt'
    renameShapes(shapesfile,oldname,newname)
    renameCard(datacardpattern,oldname,newname)
    if testname!="":
      renamePath(datacardpattern,testname)


oldname=sys.argv[1]
newname=sys.argv[2]
renameSysSL(oldname,newname)