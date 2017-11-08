import sys
import os
import stat
import subprocess

cmsswpath=os.getenv("CMSSW_BASE")



def create_scripts_limit(cmssw_path,datacard_dir,datacard_file,datacard_name,methods,expectS):
    script='#!/bin/bash\n'
    script+='export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n'
    script+='source $VO_CMS_SW_DIR/cmsset_default.sh\n'
    script+='cd '+cmssw_path+'/src\neval `scram runtime -sh`\n'
    script+='cd '+datacard_dir+' \n'
    if 'Asymptotic' in methods:
		script+='combine -M Asymptotic --minosAlgo stepping -m 125 -n '+datacard_name+' --rMin -10 --rMax 10 --minimizerStrategy 0 --minimizerTolerance 0.00001 --run=blind '+datacard_file+' 2>&1 | tee asymplimit_'+datacard_name+'.txt'+'\n'
    if 'MaximumLikelihood'  in methods:
		script+='combine -M MaxLikelihoodFit -t -1 -n '+datacard_name+' --expectSignal '+str(expectS)+' --rMin -10 --rMax 10 --minimizerStrategy 0 --minimizerTolerance 0.00001 --saveNLL --saveNormalizations --saveShapes --saveWithUncertainties '+datacard_file+' 2>&1 | tee mlfit_'+datacard_name+'.txt'+'\n'
    if 'Significance' in methods:
                script+='combine -M ProfileLikelihood --significance --signalForSignificance 0 -t -1 -n '+datacard_name+' --expectSignal '+str(expectS)+' --rMin -10 --rMax 10 --minimizerTolerance 0.00001 '+datacard_file+' 2>&1 | tee signi_'+datacard_name+'.txt'+'\n'
    filename='scripts/'+'sup_'+datacard_name+'_'+'.sh'
    f=open(filename,'w')
    f.write(script)
    f.close()
    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)

def main(args,methods_=['Significance','MaximumLikelihood','Asymptotic'],cmssw_path_=cmsswpath,expectS_=1):
#def main(args,methods_=['MaximumLikelihood'],cmssw_path_=cmsswpath,expectS_=0):
        if not os.path.exists("scripts"):
          os.makedirs("scripts")
        if not os.path.exists("logs"):
          os.makedirs("logs")
        if not os.path.exists("workdirs"):
          os.makedirs("workdirs")
        
        rootpath=args[0]
        datacards_=args[1:]
        
	datacards=datacards_
	cmssw_path=cmssw_path_
	methods = methods_
	expectS = expectS_
	datacard_dirs=[]
	datacard_files=[]
	for datacard in datacards:
                print datacard
                cardbase=os.path.split(datacard)[1]
                cardworkdir="workdirs/work_"+cardbase.replace(".txt","").replace(".root","")
                if not os.path.exists(cardworkdir):
                  os.makedirs(cardworkdir)
                cmd="cp "+datacard+" "+cardworkdir
                print cmd
                subprocess.call(cmd,shell=True)
                
		if not os.path.isabs(rootpath):
			absrootpath=os.path.join(os.getcwd(),rootpath)
                else:
                  absrootpath=rootpath
                cmd="ln -s "+absrootpath+" "+os.path.join(os.getcwd(),cardworkdir,rootpath)
                print cmd
                subprocess.call(cmd,shell=True)
		#elif os.path.isabs(datacard):
			#datacard_dirs.append(os.path.split(datacard)[0])
                absworkdir=os.path.join(os.getcwd(),cardworkdir)
		datacard_dirs.append(absworkdir)
		datacard_files.append(cardbase)
	
	print datacards_
	print datacard_dirs
	print datacard_files

	for datacard_dir,datacard_file in zip(datacard_dirs,datacard_files):
		create_scripts_limit(cmssw_path,datacard_dir,datacard_file,datacard_file.replace(".txt","").replace(".root",""),methods,expectS)



if __name__ == "__main__":
    main(sys.argv[1:])
