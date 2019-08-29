#!/bin/sh

while read p || [[ -n $p ]]; do
	pwd
  if cd "$p" 2> /dev/null; then
  	../rename_exif_creation_date.sh
  	../stripOrientation.sh
  	cd "../"
  fi
done < image-directories.txt