#!/bin/sh

# Run from inside target image directory

echo "Rename files as EXIF CreateDate from all JPG in $(pwd)"

let "filesRenamed=0"

for f in *.JPG
do
	newName=$(exiftool -d "%Y%m%d_%H%M%S" -CreateDate "$f" | awk '{print $4".jpg"}')
	if [ ! -z "$newName" ]
	then
		echo "$newName"
		mv -n "$f" "$newName" #Repalce -n with -f to enable overwriting of files. That should only happen if the files were already renamed
		((filesRenamed+=1))
	fi
    #
done

echo "Renamed $filesRenamed files"