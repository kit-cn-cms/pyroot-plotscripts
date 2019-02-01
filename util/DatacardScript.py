import sys
from os import path
"""
USE: Datascripty.py CATEGORY ROOTFILEPATH OUTPUTFILEPATH
"""
categoryName	= sys.argv[1]
file 			= sys.argv[2]
outputfile 		= sys.argv[3]

#TODO: Add in config directory path
directory = "/nfs/dust/cms/user/lreuter/forPhilip/datacardMaker" 

#Load datacardMaker 
srcdir = path.join(directory, "src")
if not srcdir in sys.path:
    sys.path.append(srcdir)

basedir = path.join(directory, "base")
if not basedir in sys.path:
    sys.path.append(basedir)

from analysisObject import analysisObject
from datacardMaker import datacardMaker
from categoryObject import categoryObject
from identificationLogic import identificationLogic

key_generator=identificationLogic()

analysis=analysisObject()
nominalkey=key_generator.generic_nominal_key
systkey=key_generator.generic_systematics_key

#Create Category Object out of csv file and write to datacard
category=categoryObject(categoryName=categoryName,defaultRootFile=file,
                    defaultnominalkey=nominalkey,systkey=systkey)
#TODO: Add in config csv file path
category.add_from_csv(pathToFile="/nfs/dust/cms/user/lreuter/forPhilip/datacardMaker/systematics_hdecay13TeVJESTest.csv")
#Delete processes that dont exist in file
for process in category:
	if not category[process].key_nominal_hist:
		print "deleted process %s" % process
		category.delete_process(processName=process)
#TODO: Add data_obs to config
print "-"*130
print "create observation"
category.observation = "data_obs"
analysis.add_category(category)
datacard=datacardMaker(analysis,outputfile,hardcodenumbers=True)
