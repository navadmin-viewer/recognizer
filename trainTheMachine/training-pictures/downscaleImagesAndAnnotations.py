import json

import PIL
from PIL import Image
from PIL import ImageFile

import multiprocessing

# Resize images and rescale SLOTH annotation file to match resizing.

if input("\N{speech balloon} Images and annotation files will be OVERWRITTEN in resize and rescale!\nEnsure original files are backed up. Continue? (y/n): ") != 'y':
	exit()

IMAGE_DIRECTORY_FILE = 'image-directories.txt'
with open(IMAGE_DIRECTORY_FILE) as f:
		imageDirs = [ line.rstrip('\n') for line in f.readlines()]

for imageDir in imageDirs:

	ANNOTATION_FILE = 'annotations.json' # Specify annotation files from SLOTH

	annotation_filePath = imageDir + '/' + ANNOTATION_FILE
	annotationRescaled_filePath = imageDir + '/' + ANNOTATION_RESCALED_FILE

	OUTPUT_WIDTH = 416
	OUTPUT_HEIGHT = 416

	# Resize image and scale raw SLOTH annotation output to match
	try:
		with open(annotation_filePath, 'r') as json_file:
			slothOutput = json.load(json_file)

			resizedCount = 0

			# Worker function to resize/rescale. Return (modified, updatedFileEntry)
			def resizeRescaleFromSLOTHFileEntry(fileEntry):
				imagePath = imageDir + '/' + fileEntry['filename']
				with PIL.Image.open(imagePath) as img:
					width, height = img.size

					# Determine scaling needed for X and Y directions
					scaleX = OUTPUT_WIDTH / width
					scaleY = OUTPUT_HEIGHT / height

					# If image is already the correct size, do not (resize image and rescale annotations)
					if scaleX == 1 and scaleY == 1:
						return (False, None)

					img = img.convert('RGB')
					img_resize = img.resize((OUTPUT_WIDTH, OUTPUT_HEIGHT), Image.LANCZOS)
					img_resize.save(imagePath, 'JPEG', optimize=True, progressive=True)

				# For each annotation in image, apply scale
				for j, singleA in enumerate(fileEntry['annotations']):
					singleA['x'] *= scaleX
					singleA['y'] *= scaleY
					singleA['width'] *= scaleX
					singleA['height'] *= scaleY 
					fileEntry['annotations'][j] = singleA

					# print('Resize and rescaled ' + imagePath)

				return (True, fileEntry)

			# Python Pool.map returns results in order
			# https://stackoverflow.com/questions/41273960/python-3-does-pool-keep-the-original-order-of-data-passed-to-map
			with multiprocessing.Pool() as pool:
				for i, result in enumerate(pool.map(resizeRescaleFromSLOTHFileEntry, slothOutput)):
					if result[0] is True:
						resizedCount += 1
						slothOutput[i] = result[1]

			with open(annotation_filePath, 'w') as output_file:
				json.dump(slothOutput, output_file, indent=4, separators=(',', ': '))

			print(str(resizedCount) + '/' + str(len(slothOutput)) + ' \timages resized in ' + imageDir)

	except OSError as err:
		print("OS error: {0}".format(err))
		continue # Continue with other image directories if annotation file not found.
