#!/bin/bash

samples=( \ 
 "DYJetsToLL_M-50"      \
# "ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100"      \
# "TTJets"      \
) 
lists="Tracklists"
output="TTOC"
number="20"
atplace="240"

for sample in ${samples[@]}
do 
  #root -l 'main.C -s ${sample} -i "lists" -o "TTOC" -n 10'
  #root -l -b -q 'ratio161718.C()'
  root -l 'drawer.C('\""${sample}"\"', '\""${lists}"\"', '\""${output}"\"','\""${number}"\"','\""${atplace}"\"')'
  #root -l 'drawer.C('\""${sample}"\"', '\""${lists}"\"', '\""${output}"\"','"${number}"','\""${atplace}"\"')'
  #root -l 'drawer.C('"${sample}"', '"${lists}"', '"${output}"','"${number}"','"${atplace}"')'
 #root -l 'main.C('\""${region}"\"', '"${dolog}"', '"${doHIP}"', '"${useEOS}"', '\""${description}"\"')'
done

