#!/bin/sh

# Mainly For Gaffney HPC

# Onyx HPC may need to swap compile enviroment with module https://www.erdc.hpc.mil/docs/onyxUserGuide.html#relevant
# module swap PrgEnv-cray PrgEnv-intel
# module swap PrgEnv-cray PrgEnv-gnu  
# https://www.erdc.hpc.mil/docs/onyxUserGuide.html#staticDynamic
# export XTPE_LINK_TYPE=dynamic
# export CRAYPE_LINK_TYPE=dynamic
# module unload craype-hugepages2M
# export HUGETLB_MORECORE=no

# PROFILE - alias ll to ls -la
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
alias ll="ls -la"

# Create user home directory usr/local directory if not existing
mkdir -p $HOME/usr/local

# PROFILE - Add user home directory usr/local to paths in .bash_profile
echo 'Make sure you add $HOME/usr/local/ bin OR lib to paths in .bash_profile.'
export PATH=$HOME/usr/local/bin:$PATH
export LD_LIBRARY_PATH=$HOME/usr/local/lib:$LD_LIBRARY_PATH

# Install libevent
cd $HOME
wget https://github.com/libevent/libevent/releases/download/release-2.1.11-stable/libevent-2.1.11-stable.tar.gz
tar xvf libevent-2.1.11-stable.tar.gz
cd libevent-2.1.11-stable
./configure --prefix=$HOME/usr/local
make
make install

# Install Tmux
cd $HOME
wget https://github.com/tmux/tmux/archive/2.9a.tar.gz
tar xvf 2.9a.tar.gz
cd tmux-2.9a
sh autogen.sh
# Specify libevent location https://unix.stackexchange.com/a/17918/80320
DIR="$HOME/usr/local"
./configure --prefix=$HOME/usr/local LIBEVENT_CFLAGS="-I$DIR/include" LIBEVENT_LIBS="-L$DIR/lib -levent"
# ./configure --prefix=$HOME/usr/local CFLAGS="-I$DIR/include" LDFLAGS="-L$DIR/lib"
make
make install

# Optional: Install htop
cd $HOME
wget https://hisham.hm/htop/releases/2.2.0/htop-2.2.0.tar.gz
tar xvf htop-2.2.0.tar.gz
cd htop-2.2.0
sh autogen.sh
./configure --prefix=$HOME/usr/local
make
make install

# Setup cuda on gaffney
# CUDA exists on the login node but not in the standard compute node which will throw an error if mxnet is installed.
# Copy CUDA lib from root to user home
cp -a /usr/local/cuda $HOME/usr/local/
cp -a /usr/local/cuda-8.0 $HOME/usr/local/ # backup cuda-8.0 incase it exists (gaffney)
# PROFILE - Add user cuda directory to paths in .bash_profile
echo 'Make sure you add user CUDA paths in .bash_profile.'
export PATH=$HOME/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=$HOME/usr/local/cuda/lib64:$LD_LIBRARY_PATH


# If supported CUDA is already installed in /usr/local
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

# Onyx has cuda-9.2
# pip uninstall -y mxnet
# pip install mxnet-cu90==1.1.0
# Download cuda 9.0 toolkit
./cuda_9.0.176_384.81_linux-run --silent --toolkit --toolkitpath=$HOME/usr/local/cuda-9.0

# Download cudnn for 9.0 library tgz
# Extract cudnn library files to local cuda9.0 install lib64 directory
cp -a lib64 $HOME/usr/local/cuda-9.0
