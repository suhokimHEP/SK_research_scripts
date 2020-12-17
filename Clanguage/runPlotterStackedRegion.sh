#!/bin/bash

regions=( \ 
 "TwoEleZH"      \
 "TwoMuZH"       \
) 

dologs=( \
# "kFALSE" \
 "kTRUE" \
)

doHIPs=( \
 "kFALSE" \
 #"kTRUE" \
)

useEOS="kFALSE"
description=""

for region in ${regions[@]}
do
 for dolog in ${dologs[@]}
 do
  for doHIP in ${doHIPs[@]}
  do
   for doctau in ${doctaus[@]}
   do 
    root -l -b -q  'Sig_table_stackedRegion.C('\""${region}"\"', '"${dolog}"', '"${doHIP}"', '"${useEOS}"', '\""${description}"\"')'
   done
  done
 done
done
