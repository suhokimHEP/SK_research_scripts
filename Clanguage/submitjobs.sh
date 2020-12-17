#!/bin/bash

# script to generate submit files
# and optionally to submit to condor

# source xx/LLDJ/setup.sh for ${wversion}

doSubmit=true
maxfilesperjob=400  # 500=6h
wversion="SKdir"
samples=(  \
 "DYJetsToLL_M-50"            \
)


## make info file - put "loggit" on any line you want to keep 
mkdir -p $(pwd)/gitignore/${wversion}
 
makeasubmitdir () {
 printf "Making submits for $1\n"
 
 # go to the directory
 origindir=$(pwd)
 submitdir=$(pwd)/gitignore/${wversion}/$1
 mkdir -p ${submitdir} 
 pushd    ${submitdir}  > /dev/null
 printf " The directory is %s\n" $(pwd)
 
 mkdir -p logs
 
 # write base for submit file
 printf "universe = vanilla\n" > submitfile
 printf "Executable = ${origindir}/runjob.sh\n" >> submitfile
 printf "Should_Transfer_Files = YES \n" >> submitfile
 printf "WhenToTransferOutput = ON_EXIT\n" >> submitfile
 printf "Transfer_Input_Files = ${origindir}/drawer.C,${origindir}/cms_setup.tar.gz,${origindir}/Tracklists/$1.list\n" >> submitfile

 printf "notify_user = $(whoami)@cern.ch\n" >> submitfile
 printf "x509userproxy = $X509_USER_PROXY\n" >> submitfile
 printf "\n" >> submitfile
 printf "Output = logs/runanalyzer_\$(Cluster)_\$(Process).stdout\n" >> submitfile
 printf "Error  = logs/runanalyzer_\$(Cluster)_\$(Process).stderr\n" >> submitfile
 printf "Log    = logs/runanalyzer_\$(Cluster)_\$(Process).log\n" >> submitfile
 printf "\n" >> submitfile

 # make haddfile (make now for merging expected results)
 #haddfile_OneEleSig_histograms="./haddit_OneEleSig_histograms.sh"                           


 #hadddir="${rootdir}/${wversion}"
 #mkdir -p ${hadddir}
 #printf "#!/bin/bash\n\n" > ${haddfile_OneEleSig_histograms}    


 # hadd command to go in haddfile
  # name of final merged file
 #printf "hadd ${hadddir}/$1_OneEleSig_histograms.root"     >>       ${haddfile_OneEleSig_histograms}    

 # breaking up input file list
 nfilesinlist=$( wc -l < "${origindir}/Tracklists/$1.list" )
 filenrlow=0
 jobfilenr=0

 printf " nfilesinlist = ${nfilesinlist} / ${maxfilesperjob} \n\n"
 
 until [ ${filenrlow} -gt ${nfilesinlist} ]
 do

  printf "Arguments = $1 . ${jobfilenr} ${maxfilesperjob} ${filenrlow}\n" >> submitfile
  printf "Queue\n" >> submitfile
  printf "\n" >> submitfile

  # add files to be produced to haddfiles
  #printf "\\"  >> ${haddfile_OneEleSig_histograms}    

  #printf "\n $(pwd)/$1_${jobfilenr}_OneEleSig_histograms.root"     >> ${haddfile_OneEleSig_histograms}    

  # increment filenumber counters
  #printf "NFILES: %s %s %s\n" $nfilesinlist $filenrlow $jobfilenr
  filenrlow=$(( ${filenrlow} + ${maxfilesperjob} ))
  jobfilenr=$(( ${jobfilenr} + 1 ))

 done # until filenrlow > nfilesinlist

 #printf "\n\n" >> ${haddfile_OneEleSig_histograms}    

 if [ ${doSubmit} = true ]
 then
  condor_submit submitfile
 fi
 
 popd > /dev/null
}


# actually call the function
for sample in ${samples[@]} 
do
 # set isMC flag if MC
 if [[ ${sample} == "Data"* ]]
 then
  mc=""
 else
  mc="-m"
 fi

 makeasubmitdir ${sample} ${mc}

done


