#!/bin/sh

# HPC Server chooser
# Anson Liu

servers=( "[custom]" "copper.ors.hpc.mil" "gaffney.navydsrc.hpc.mil" "onyx.erdc.hpc.mil" "gold.erdc.hpc.mil")

printf "==> Loaded HPC servers:\n"

for i in "${!servers[@]}"; do
	printf "$i - ${servers[i]}\n"
done

printf "\xf0\x9f\x8c\x8e Enter number of HPC server to use: "
read serverChoice

if [ $serverChoice -gt `expr ${#servers[@]} - 1` ]
then
	printf "No HPC server for number $serverChoice.\n"
	exit
fi

if [ $serverChoice -eq 0 ]
then 
	printf "Enter SSH server hostname: "
	read serverChoice
else
	serverChoice=${servers[$serverChoice]}
fi

printf "Selected $serverChoice.\n"

read -n1 -r -p "Press any key to connect or ESC to exit. " key

case $key in
     $'\e') printf "\n"; exit;;
esac

/usr/local/ossh/bin/ssh $serverChoice