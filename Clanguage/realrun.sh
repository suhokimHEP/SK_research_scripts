#!/bin/bash

samples=( \ 
# "140"      \
 "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8"      \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100"      \
# "TTJets"      \
) 
lists="Tracklists"
output="TTOC"
number="20"
atplace="240"
intval=140
int=(128 180 193 245)
#for sample in ${samples[@]}
#do 
#  #root -l 'main.C -s ${sample} -i "lists" -o "TTOC" -n 10'
#  #root -l -b -q 'ratio161718.C()'
#  #root -l -b 'P2draw.C('${intval}')'
#  #root -l 'drawer.C('\""${sample}"\"', '\""${lists}"\"', '\""${output}"\"','\""${number}"\"','\""${atplace}"\"')'
 root -l 'ROIdrawer.C('\""${sample}"\"', '\""${lists}"\"', '\""${output}"\"','\""${number}"\"','\""${atplace}"\"')'
#  #root -l 'drawer.C('\""${sample}"\"', '\""${lists}"\"', '\""${output}"\"','"${number}"','\""${atplace}"\"')'
#  #root -l 'drawer.C('"${sample}"', '"${lists}"', '"${output}"','"${number}"','"${atplace}"')'
# #root -l 'main.C('\""${region}"\"', '"${dolog}"', '"${doHIP}"', '"${useEOS}"', '\""${description}"\"')'
#done
#for value in ${int[@]} #int
#do
# root -l -b -q 'P2draw.C('${value}')'
#done
