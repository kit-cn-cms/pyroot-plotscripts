# pyroot-plotscripts
Collection of scripts we use for plotting and datacard making

Useful tools
1) combine
Calculate limits with
CMSSW_7_1_5
https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideHiggsAnalysisCombinedLimit

2) Our datacard making tool
This is needed to actually make the datacards
https://github.com/cms-ttH/ttH-Limits/tree/80X

3) histograms for datacards
These are the plotscripts themselves
https://github.com/kit-cn-cms/pyroot-plotscripts

Quick blinded expected limits:
  combine -M Asymptotic --minosAlgo stepping -m 125 --run="blind" datacard.txt
  
  
  ## DrawParallel
  * The plotscript can now parallelize the Draw step (where the histograms are actually printed to the canvases)
  * This can speed up things if you have a lot of plots with errorbars
  * To do this you have to modify the code a bit
  * See for example plot_controlPlots_DrawParallelExample.py
  
  ## pyroot-plotscripts-base subtree repository
  * The basic pyroot-plotscripts functionality was factorized in a dedicated Gitlab repository:
  https://gitlab.cern.ch/kit-cn-cms/pyroot-plotscripts-base
  * This includes the scriptgenerator and plotutils etc.
  * To use these now you have to add to your scripts the following lines
    '''
    import sys
    sys.path.append('pyroot-plotscripts-base')
    sys.path.append('pyroot-plotscripts-base/limittools')
    '''   
  * This basic functionality is included as a subtree folder pyroot-plotscripts-base
  * No worries, you can work as usual with THIS repository
  * To get the newest versions of the code from this repository do :
     * git remote add pyroot-subtree https://gitlab.cern.ch/kit-cn-cms/pyroot-plotscripts-base
     * git fetch pyroot-subtree
     * git pull -s recursive -X -s patience pyroot-subtree master
  * BUT: Major changes should be pushed upstream via git subtree push (you can also do this after collecting some changes to the core code).
  * To do this do as follows:
     * Do NOT cmsenv/source CMSSW
     * You need git 1.9:    module load git/1.9 or even consider to install Git 2.13
     * Enter the plotscript directory
     * git subtree pull  --prefix=pyroot-plotscripts-base pyroot-subtree master
     * git subtree push --prefix=pyroot-plotscripts-base/ pyroot-subtree master
  * The upstream repository uses a CI part to make sure that functionality is not broken.
  
  ## Installation of Git 2.13
  1. Download the source code
  ```wget https://www.kernel.org/pub/software/scm/git/git-2.13.3.tar.xz```
  2. Unpack the tar file
  ``` tar xvf git-2.13.3.tar.xz```
  3. Configure and make git
  ```cd git-2.13.3
  mkdir ../git-install
  ./configure --prefix=$PWD/../git-install
  make -j 12
  make -j 12 install
  ```
  4. Make and install git subtree package
  ``` cd contrib/subtree
  make -j 12
  make -j 12 install
  ```
