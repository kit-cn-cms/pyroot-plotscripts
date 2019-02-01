import sys
from os import path
import optparse #enables parser
"""
USE: Datascripty.py --categoryName=CATEGORYNAME --rootfile=FILE 
					--outputfile=FILE --directory=PATH
					--csvfile=FILE
Use all of these options! Only for readability.

"""
usage="usage=%prog [options] \n"
usage+="USE: Datascripty.py --categoryname=CATEGORYNAME --rootfile=FILE --outputfile=FILE --directory=PATH -csvfile=FILE \n"
usage+="Use all of these options! Only for readability.\n"
usage+="Optional: --dataobs=NAME"

parser = optparse.OptionParser(usage=usage)

parser.add_option("-n", "--categoryname", dest="categoryName",
        help="NAME of the category", metavar="categoryName")
parser.add_option("-r", "--rootfile", dest="Rootfile",
        help="ROOTFILE including the data used to create the datacard", metavar="/path/to/rootfile")
parser.add_option("-o", "--outputfile", dest="outputfile",
        help="write datacard to FILE", metavar="/path/to/outputfile")
parser.add_option("-d", "--directory", dest="directory",
         help="PATH to datacardMaker directory", metavar="/path/to/datacardMaker")
parser.add_option("-c", "--csvfile", dest="csvFile",
        help="FILE to csv file used to create systematics", metavar="/path/to/csvfile")
parser.add_option("--dataobs", dest="dataobs",
        help="Name of observed data", metavar="dataobs",default="data_obs")

(options, args) = parser.parse_args()

if not path.exists(options.Rootfile):
    sys.exit("ERROR: rootfile does not exist!")
elif not path.exists(options.csvFile):
    sys.exit("ERROR: csvfile does not exist!")

#Load datacardMaker 
srcdir = path.join(options.directory, "src")
if not srcdir in sys.path:
    sys.path.append(srcdir)

basedir = path.join(options.directory, "base")
if not basedir in sys.path:
    sys.path.append(basedir)

#Import Objects from datacardMaker
from analysisObject import analysisObject
from datacardMaker import datacardMaker
from categoryObject import categoryObject
from identificationLogic import identificationLogic

#Initialize identificationLogic to get generic keys
key_generator=identificationLogic()

nominalkey=key_generator.generic_nominal_key
systkey=key_generator.generic_systematics_key

#Initialize analysisObject
analysis=analysisObject()

#Create Category Object out of csv file and write to datacard
category=categoryObject(categoryName=options.categoryName,defaultRootFile=options.Rootfile,
                    defaultnominalkey=nominalkey,systkey=systkey)

category.add_from_csv(pathToFile=options.csvFile)
#Delete processes that dont exist in file
for process in category:
	if not category[process].key_nominal_hist:
		print "deleted process %s" % process
		category.delete_process(processName=process)
#TODO: Add data_obs to config
category.observation = options.dataobs
analysis.add_category(category)
datacard=datacardMaker(analysis,options.outputfile,hardcodenumbers=True)
