#!/bin/sh

# Job scheduling for Uniform Recognizer
# By Anson Liu
# Use this job script for running background test jobs

#PBS -A ONAVY44436545
#PBS -q background
# Selecting 'gpu' queue will autoselect ngpus=1
#PBS -l select=1:ncpus=48
#PBS -l walltime=004:00:00

#PBS -V
#PBS -N trainTheMachine
#PBS -m be
#PBS -M anson.liu@navy.mil,15103868680@tmomail.net 

export PROJECTID=ONAVY44436545
#qsub -A $PROJECTID -q background -l select=1:ncpus=48 -l walltime=04:00:00 -I -V

#oynx qsub -A ONAVY44436545 -q background -l select=1:ncpus=22:mpiprocs=1:ngpus=1 -l walltime=04:00:00 -I -V

# Create a directory $WORKDIR named in the format JOBID.CURRENTDATE to do work in
cd $WORKDIR
JOBID=`echo ${PBS_JOBID} | cut -d '.' -f 1`
[ -z "$JOBID" ] && JOBID="NoJOBID"
CURRENTDATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
mkdir "${JOBID}.${CURRENTDATE}"
cd "${JOBID}.${CURRENTDATE}"
echo "Working in directory $(pwd)"

# Copy dev files from $HOME
cp -a $HOME/trainTheMachine .

# Set omp number threads
# export OMP_NUM_THREADS=${BC_CORES_PER_NODE}
export OMP_NUM_THREADS=48

# Change to needed directory and start application
cd trainTheMachine/training-pictures
echo "Application started on $(date)"
python3 trainTheMachine.py -t -i 100
echo "Application ended on $(date)"