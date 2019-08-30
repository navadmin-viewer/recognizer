import argparse
import pkg_resources

import json
import turicreate

# TrainTheMachine created by Anson Liu
# Used for NAVADMIN Viewer Uniform Recognizer

# run from IDLE shell 
# exec(open('../trainTheMachine.py').read())
# exec(open('trainTheMachine.py').read())

# If you get a TypeError: 'NoneType' object is not iterable error:
# Likely one or more annotations have "label": null 
# Due to a bug when switching annotation classes in SLOTH.

parser = argparse.ArgumentParser(description='Correct SLOTH annotated input and train object detector model.')
parser.add_argument('-e', help='Explore annotated data.', action='store_true')
parser.add_argument('-t', help='Train model.', action='store_true')
parser.add_argument('-i', help='Max iterations.', type=int)
parser.add_argument('-w', help='Pylambda workers.', type=int)
options = parser.parse_args()



# Print Turi Create version and location
print("Turi Create distribution: " + pkg_resources.get_distribution('turicreate').project_name + " " + pkg_resources.get_distribution('turicreate').version + " (" + pkg_resources.get_distribution('turicreate').location + ")")

if options.w and options.w > 0:
	turicreate.config.set_runtime_config('TURI_DEFAULT_NUM_PYLAMBDA_WORKERS', options.w)

IMAGE_DIRECTORY_FILE = 'train-image-directories.txt'
with open(IMAGE_DIRECTORY_FILE) as f:
		imageDirs = [ line.rstrip('\n') for line in f.readlines()]

MODELNAME = 'uniformModel'

sfAll = turicreate.SFrame()

for imageDir in imageDirs:

	ANNOTATION_FILE = 'annotations.json' # Specify annotation files from SLOTH
	ANNOTATION_CORRECTED_FILE = 'annotations_corrected.json' # Specify temporary corrected annotations file created

	annotation_filePath = imageDir + '/' + ANNOTATION_FILE
	annotationCorrected_filePath = imageDir + '/' + ANNOTATION_CORRECTED_FILE

	# Correct SLOTH annotation x,y (origin) output to represent x,y (center) of object
	try:
		with open(annotation_filePath, 'r') as json_file:
			slothOutputUncorrected = json.load(json_file)

			for i, image in enumerate(slothOutputUncorrected):
				for j, singleA in enumerate(image['annotations']):
					singleA['x'] += singleA['width'] / 2
					singleA['y'] += singleA['height'] / 2
					tcCoordinates = {'x':singleA['x'], 'y':singleA['y'], 'width':singleA['width'], 'height':singleA['height']}
					singleA['coordinates'] = tcCoordinates
					singleA.pop('x', None)
					singleA.pop('y', None)
					singleA.pop('width', None)
					singleA.pop('height', None)
					image['annotations'][j] = singleA
				slothOutputUncorrected[i] = image

			with open(annotationCorrected_filePath, 'w') as output_file:
				json.dump(slothOutputUncorrected, output_file, indent=4, separators=(',', ': '))
	except OSError as err:
		print("OS error: {0}".format(err))
		continue # Continue with other image directories if annotation file not found.

	# load images into SFrame
	# +----------------+--------------------------+
	# |      path      |          image           |
	# +----------------+--------------------------+
	# | ./IMG_0037.JPG | Height: 2448 Width: 2448 |
	# | ./IMG_0038.JPG | Height: 2448 Width: 2448 |
	# +----------------+--------------------------+

	imageFrame = turicreate.image_analysis.load_images(imageDir, with_path=True)

	#print(imageFrame)

	# Load SLOTH corrected output in SFrame
	# [
	#     {
	#         "annotations": [
	#             {
	#                 "class": "decoration",
	#                 "height": 643.7782691529284,
	#                 "label": "insignia:small_craft_insignia",
	#                 "type": "rectangle",
	#                 "width": 626.9107162493582,
	#                 "x": 632.5332338838815,
	#                 "y": 969.884291955285
	#             },
	#             {
	#                 ...more annotations for a image
	#  						}
	#         ],
	#         "class": "image",
	#         "filename": "IMG_0037.JPG"
	#     }, ...more images dicts
	# 
	# +-------------------------------+-------+--------------+
	# |          annotations          | class |   filename   |
	# +-------------------------------+-------+--------------+
	# | [{'y': 969.884291955285, '... | image | IMG_0037.JPG |
	# | [{'y': 1090.7684210975378,... | image | IMG_0038.JPG |
	# +-------------------------------+-------+--------------+
	annotationsFrame = turicreate.SFrame.read_json(annotationCorrected_filePath, orient='records')

	# Rename filename column in annotations SFrame to path to match SFrame rows for join
	annotationsFrame.rename({'filename': 'path'}, inplace=True)

	# Append './' to start of filename in sloth output to match imageFrame SFrame path
	annotationsFrame['path'] = annotationsFrame['path'].apply(lambda x: imageDir + '/' + x)

	#print(annotationsFrame)

	# Join SFrames of images and annotations
	# +----------------+--------------------------+-------------------------------+
	# |      path      |          image           |          annotations          |
	# +----------------+--------------------------+-------------------------------+
	# | ./IMG_0037.JPG | Height: 2448 Width: 2448 | [{'y': 969.884291955285, '... |
	# | ./IMG_0038.JPG | Height: 2448 Width: 2448 | [{'y': 1090.7684210975378,... |
	# +----------------+--------------------------+-------------------------------+
	# +-------+
	# | class |
	# +-------+
	# | image |
	# | image |
	# +-------+
	# [2 rows x 4 columns]
	# 
	joinedImageAnnotationFrame = imageFrame.join(annotationsFrame)

	#print(joinedImageAnnotationFrame)

	# Append joined image/annotation SFrame to global SFrame for all image and annotations
	sfAll = sfAll.append(joinedImageAnnotationFrame)

#Print combined SFrame dimensions
print('Combined SFrame [' + str(sfAll.num_rows()) + ' rows x ' + str(sfAll.num_columns()) + ' columns]')

# Annotate ground truths in column
sfAll['image_with_ground_truth'] = turicreate.object_detector.util.draw_bounding_boxes(sfAll["image"], sfAll["annotations"])

# Explore interactively
if options.e:
	sfAll.explore()
	input("Press any key to continue...")

if options.t:
	model = None

	# Train and create model with custom max_iterations if specified CLI param
	if options.i and options.i > 0:
		model = turicreate.object_detector.create(sfAll, feature='image', annotations='annotations', max_iterations=options.i)
	else:
		model = turicreate.object_detector.create(sfAll, feature='image', annotations='annotations')
	#
	# Save the model for later use in Turi Create
	# Important to save in case something after breaks the script
	model.save(MODELNAME + '.model')

	print('Saved model ' + MODELNAME + '.model')

	model.summary()

	# Mean average Precision
	scores = model.evaluate(sfAll)

	print(scores)

	# Export for use in CoreML
	model.export_coreml(MODELNAME.title() + 'Classifier.mlmodel')

