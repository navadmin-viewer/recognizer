#!/bin/sh

# Compress files to tar gzip archive. Run from outside target directory. 
# ./trainTheMachine/hpc/tarCompress.sh

tar --exclude='trainTheMachine/.git' -zcvf trainTheMachine.tar.gz trainTheMachine