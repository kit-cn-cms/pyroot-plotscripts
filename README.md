# pyroot-plotscripts-base

* Repository containing the base parts of the pyroot plot scripts. 
* Repositories which make use of the pyroot plotscripts should use the git subtree module to derive the base part from this repository.
* More information about git subtree module: https://medium.com/@v/git-subtrees-a-tutorial-6ff568381844

### Usage of git subtree module
* On the NAF use module load git to get a newer git version.
* Use the following commands to add the current repository as a subfolder to another repository:
```
git remote add pyroot-subtree ssh://git@gitlab.cern.ch:7999/kit-cn-cms/pyroot-plotscripts-base.git
git subtree add —-prefix=pyroot-plotscripts-base/ pyroot-subtree master
```
* If you would like to push changes to the upstream repo / this repository use the following command on the derived repository:
```
git subtree pull  --prefix=pyroot-plotscripts/pyroot-plotscripts-base pyroot-subtree master
git subtree push -d  --prefix=pyroot-plotscripts/pyroot-plotscripts-base/ pyroot-subtree master
```



### Content

* limittools folder
* CMS_lumi.py
* plot_LimitsSpring17v3.py: Used as a test case for the CI
* plotconfigSpring17v3.py: Used as a test case for the CI
* plotutils.py
* scriptgenerator.py
* scriptgeneratorMEMDBCSV.py: Used as a test case for the CI
* variablebox.py
