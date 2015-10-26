#!/bin/bash

export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /afs/desy.de/user/h/hmildner/CMSSW_7_4_14/src
eval `scram runtime -sh`
cd -

export FILENAMES="/nfs/dust/cms/user/hmildner/trees1019/ttbar_nominal.root"
export OUTFILENAME="testplots.root"
export MAXEVENTS="2000000"
export SKIPEVENTS="1000000"
export PROCESSNAME="ttbarPlusBBbar"
./plot_syst
