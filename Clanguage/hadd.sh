#!/bin/bash

regions=( \ 
# "TwoEleZH"      \
# "TwoMuZH"       \
 "TwoEleOffZ"      \
 "TwoMuOffZ"       \
) 

dologs=( \
 "ZGTo2LG" \
 "DYJetsToLL_M-50" \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1"      \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10"     \
 "ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100"    \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000"   \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1"      \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10"     \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100"    \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000"   \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1"      \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10"     \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100"    \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000"   \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1"      \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10"     \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100"    \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000"   \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1"      \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10"     \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100"    \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000"   \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1"      \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10"     \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100"    \
# "ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000"   \
)
where="/uscms/home/skim2/nobackup"
aversion="Vgamma"
#aversion="Nov20Noreq"

for region in ${regions[@]}
do
 for dolog in ${dologs[@]}
 do
  #hadd -f temproot/new${region}_${dolog}_${aversion}.root ${where}/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/${aversion}/${dolog}_${region}_histograms.root ${where}/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/roots/${aversion}/${dolog}_${region}_histograms.root ${where}/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/roots/${aversion}/${dolog}_${region}_histograms.root
  hadd -f temproot/new${region}_${dolog}_${aversion}.root ${where}/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/roots/${aversion}/${dolog}_${region}_histograms.root ${where}/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/roots/${aversion}/${dolog}_${region}_histograms.root

 done
done
