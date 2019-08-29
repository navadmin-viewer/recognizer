#!/bin/sh

# Run from inside target image directory

echo "Strip EXIF Orientation data from all JPG in $(pwd)"

find . -type f -name '*.JPG' | xargs exiftool -Orientation=1 -overwrite_original_in_place -n
