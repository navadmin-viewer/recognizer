Training Workflow

1. Sort images into directories
1a. Put each image directory name as a line in image-directories.txt
2. Enter each image category directory
2a. Run rename_exif_creation_date.sh
2b. Run stripOrientation.sh
3. Exit image category directory
4. Backup all image category directories to preserve original full resolution images.
5. Run downscaleImagesAndAnnotations.py
6. Enter each image category directory
7. Run ../run_sloth.sh
7a. Load annotations.json file from the current image directory
7b. Make annotations
8. Exit image category directory
9. Run trainTheMachine.py
10. Run evaluateModel.py