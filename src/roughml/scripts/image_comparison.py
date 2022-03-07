import numpy as np
from pathlib import Path
import cv2

def mse(img1, img2):
	# get difference of images by subtracting the pixel intensities
	# square this difference and get the sum
	error = np.sum((img1 - img2) ** 2)
	# divide the sum of squares by the total number of pixels
	error = error / (img1.shape[0] * img1.shape[1])

	return error

# get current working dir
cwd = Path.cwd()
# complete path to scripts folder
cwd = str(cwd) + "/src/" + "roughml/" + "scripts/"

# input preferred images to compare
image1 = "fake_00.png"
image2 = "fake_00.png"
image1 = cv2.imread(cwd + image1)
image2 = cv2.imread(cwd + image2)

# get mean square error
mymse = mse(image1, image2)
print("Mean Square Error: ", mymse)

# if mean square error has a value images are different, otherwise they are equal
if mymse > 0:
	print("Images are different")
else:
	print("Images are equal")