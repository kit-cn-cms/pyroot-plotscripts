import sys
from os import path
import optparse
import importlib 

usage="usage=%prog [options] \n"
usage+="USE: Plotscript.py --categoryname=CATEGORYNAME --rootfile=FILE --outputfile=FILE --directory=PATH -csvfile=FILE \n"

parser = optparse.OptionParser(usage=usage)

parser.add_option("--categoryname", dest="categoryName",
        help="NAME of the category", metavar="categoryName")
parser.add_option("--rootfile", dest="Rootfile",
        help="ROOTFILE including the data used to create the plots", metavar="/path/to/rootfile")
parser.add_option("--outputpath", dest="outputpath",
        help="output path", metavar="/path/to/outputpath")
parser.add_option("--directory", dest="directory",
         help="PATH to pyroot plotscript directory", metavar="/path/to/directory")
parser.add_option("--plotconfig", dest="plotconfig",
        help="Name of plot config", metavar="plotconfig")
parser.add_option("--systconfig", dest="systconfig",
        help="Name of systematics config", metavar="systconfig")

(options, args) = parser.parse_args()

configdir = options.directory +"/configs/"
utildir = options.directory +"/util/"
systconfig=configdir+options.systconfig+".csv"
plotconfig=configdir+options.plotconfig+".py"

if not path.exists(options.Rootfile):
    sys.exit("ERROR: rootfile does not exist!")
elif not path.exists(systconfig):
    sys.exit("ERROR: systconfig does not exist!")
elif not path.exists(plotconfig):
    sys.exit("ERROR: plotconfig does not exist!")


print '''
    # ========================================================
    # loading configs
    # ========================================================
    '''
# loading plt_X.py config

sys.path.append(configdir)
pltcfg = importlib.import_module( options.plotconfig )

# loading X_systematics.py config
sys.path.append(utildir+"/tools/")
Systematics = importlib.import_module("Systematics")
processes=pltcfg.list_of_processes
systematics=Systematics.Systematics(systconfig)
systematics.plotSystematicsForProcesses(processes)
for sample in pltcfg.samples:
    sample.setShapes(systematics.get_shape_systs(sample.nick))







