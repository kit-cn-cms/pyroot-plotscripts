import subprocess
scriptname='plot_nominal'
p = subprocess.Popen(['root-config', '--cflags', '--libs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
cmd= ['g++']+out[:-1].split(' ')+['-lTMVA']+[scriptname+'.cc','-o',scriptname]
subprocess.call(cmd)
