![Navadmin viewer icon](https://raw.githubusercontent.com/navadmin-viewer/recognizer/master/assets/Icon128.png)

## Uniform Recognizer

The Uniform Recognizer detects US military uniform decorations using a trained neural network object detector model. 

![UR demo](https://raw.githubusercontent.com/navadmin-viewer/recognizer/master/assets/URdemo.gif)

The finished project is distributed as part of the free [NAVADMIN Viewer iOS app](https://apps.apple.com/us/app/navadmin-viewer/id1345135985).

#### Training pipeline

The training pipeline consists of:
- Processing image files `renameAndStripEXIFEachDirectory.sh`
- Annotating ground truths in `sloth`
  - Run `../run_sloth.sh` inside each image directory
- Downscaling image files `downscaleAnnotationsAndLinkedImages.py`
- Training an object detection model in `turicreate`
  - Run `trainTheMachine.py -t` 
- Evaluate and export model `evaluateModel.py`


- See `trainTheMachine/training-pictures` for directions.

#### Models

- Trained models will be distributed as [releases](https://github.com/navadmin-viewer/recognizer/releases).
- See `models` for released models.

#### Acknowledgements

- [cvhciKIT/sloth](https://github.com/cvhciKIT/sloth) annotation tool

- [apple/turicreate](https://github.com/apple/turicreate) machine learning models

- [PBS Professional](http://pbspro.org) job scheduling

- This work was supported in part by a grant of computer time from the DoD High Performance Computing Modernization Program at Navy DSRC, ERDC, and ORS.

#### License

- All work in this repository is released under LGPL v3
  - Attribution to Anson Liu required for end products utilizing models created from this repository. 

- All dependencies retain their original licenses.