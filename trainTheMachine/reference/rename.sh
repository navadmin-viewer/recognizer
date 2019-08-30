#!/bin/sh

declare -a filenames

find . -type d -maxdepth 1 -mindepth 1 | xargs -I{} find {} -type d -maxdepth 1 -mindepth 1 | xargs -I{} find {} -maxdepth 1 -type f | xargs -I{} filenames+={}

echo "${#filenames[@]} elements"
