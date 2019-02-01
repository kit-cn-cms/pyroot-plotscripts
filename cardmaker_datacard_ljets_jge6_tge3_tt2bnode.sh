#!/bin/bash 
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch 
source $VO_CMS_SW_DIR/cmsset_default.sh 
export SCRAM_ARCH=slc6_amd64_gcc630
cd /nfs/dust/cms/user/kelmorab/CMSSW9/datacards/CMSSW_9_4_9/src
eval `scram runtime -sh`
cd - 

python nfs/dust/cms/user/lreuter/forPhilip/wfnwonf/util/DatacardScript.py ljets_jge6_tge3_tt2bnode /nfs/dust/cms/user/lreuter/forPhilip/pyroot-plotscripts/output_limitInput.root /nfs/dust/cms/user/lreuter/forPhilip/pyroot-plotscripts/ljets_jge6_tge3_tt2bnode_hdecay.txt
