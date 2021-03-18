#!/bin/bash

regions=( \ 
 "haddZH"       \
) 

yrs=( \ 
 "2016"      \
 "2017"       \
 "2018"       \
 "all"       \
) 
#dologs=( \
## "kFALSE" \
# "kTRUE" \
#)
dolog="kTRUE"
description=""

for region in ${regions[@]}
do
 for year in ${yrs[@]}
 do
    root -l -b -q  'DY_table_stackedRegion.C('\""${region}"\"', '"${dolog}"', '\""${description}"\"','\""${year}"\"'  )'
 done
done
