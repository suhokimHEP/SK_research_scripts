#x=1
for i in {0..99}
do
  #x=$(($i-1))
  #echo $x
  if [ $i -lt 10 ] 
  then
       cp Data_EGamma_D.info Data_EGamma_D_75_0${i}.info
  else
       cp Data_EGamma_D.info Data_EGamma_D_75_${i}.info
  fi
done 
