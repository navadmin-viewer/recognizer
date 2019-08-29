#!/bin/sh

# Create user home directory usr/local directory if not existing
mkdir -p $HOME/usr/local

wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
tar zxvf Python-3.6.5.tgz
cd Python-3.6.5
make clean
./configure --prefix=$HOME/usr/local/
make
make test
make install

#Gaffney
pip3 uninstall -y mxnet
pip install mxnet-cu80==1.1.0

# Onyx need to swap modules, enable dynamic lib and, and disable hugepage in setupDevEnv.sh
pip3 uninstall -y mxnet
pip3 install mxnet-cu90==1.1.0

pip3 install mxnet-cu92==1.5.0

pip3 uninstall -y mxnet-cu90
pip3 install mxnet-cu90mkl==1.1.0

ln -s libcudart.so.9.2 libcudart.so.9.0

#Preload turicreate cache with darknet.params since compute node has no internet
.trainTheMachine/hpc/osshUtil/sftp $USER@onyx.erdc.hpc.mil <<< $'put darknet.params'
mkdir -p $HOME/tcCache/model_cache
cp darknet.params $HOME/tcCache/model_cache

../Desktop/trainTheMachine/hpc/osshUtil/sftp $USER@onyx.erdc.hpc.mil

module help cudatoolkit/8.0.61_2.3.13_g32c34f9-2.1
cudatoolkit/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8