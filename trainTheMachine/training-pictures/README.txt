Training Workflow

1. Sort images into directories
1a. Put each image directory name as a line in image-directories.txt
2. Enter containing directory of all image directories.
2a. Run renameAndStripEXIFEachDirectory.sh
3. Exit image category directory
5. Enter each image category directory
6. Run ../run_sloth.sh
6a. Load annotations.json file from the current image directory
6b. Make annotations
7. Exit image category directory

8. Backup all image category directories to preserve original full resolution images.
8a. Run downscaleAnnotationsAndLinkedImages.py

9. Run trainTheMachine.py -t
10. Run evaluateModel.py