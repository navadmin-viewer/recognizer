#!/bin/sh

# SFTP upload to gaffney login home directory. Run from outside directory. Use kerberized shell kshell
# ./trainTheMachine/hpc/sftp_put_mac.sh
# ./trainTheMachine/hpc/choose_server.sh 
# vi trainTheMachine/hpc/pbs.sh
# vi trainTheMachine/hpc/pbsStd.sh 
# qsub trainTheMachine/hpc/pbs.sh
# qsub trainTheMachine/hpc/pbsStd.sh 

# Login to compute node
# qstat -fx JOBID | grep -i exec_vnode
# ssh
# watch -d -n 0.5 nvidia-smi

./trainTheMachine/hpc/osshUtil/sftp $USER@gaffney.navydsrc.hpc.mil <<< $'put trainTheMachine.tar.gz'