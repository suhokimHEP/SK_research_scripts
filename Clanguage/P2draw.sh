#!/bin/bash
echo "TEST"
voms-proxy-info --all
ls -l
echo "DONE"
export PATH=${PATH}:/cvmfs/cms.cern.ch/common
export CMS_PATH=/cvmfs/cms.cern.ch

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
tar -zxvf cms_setup.tar.gz
cd CMSSW_8_1_0/src
eval `scram runtime -sh`
cd ../../
#cp ../../*.C .
#cp ../../*.list .
#ls -la
#ls la ../../
echo $1

root -l -b -q 'P2draw.C('$1')'
