
sPath=/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/old2018lldj/lists


for file in *.list 
do

  
  cmp --silent $file $sPath/$file || echo $file "is different"

done


echo "Checking infos"
for file in *.info 
do

  cmp --silent $file $sPath/$file || echo $file "is different"

done

