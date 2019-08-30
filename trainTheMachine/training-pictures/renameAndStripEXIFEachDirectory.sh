#!/bin/sh

# Rename all .JPG images to their EXIF CreateDate and remove EXIF orientation. 
# This also removes all EXIF metadata. So you may want to do metadata processing beforehand.

# Run this script from the containing directory of ALL image directories and rename-strip-downscale-image-directories.txt


while read p || [[ -n $p ]]; do
	pwd
  if cd "$p" 2> /dev/null; then
  	../renameExifCreateDate.sh
  	../stripOrientation.sh
  	cd "../"
  fi
done < rename-strip-downscale-image-directories.txt