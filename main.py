# ############################################################################
# Color Palette Extraction
# ############################################################################
# Useful links
#   https://medium.com/@andrisgauracs/generating-color-palettes-from-movies-with-python-16503077c025
#   https://buzzrobot.com/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036
# ############################################################################

import cv2
import glob
import aux
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

##############################################################################
# Setup paths and clusters number
##############################################################################
(CLST_NUM, MAX_ITER, PLT_HEIGHT) = (8, 1000, .05)
(I_PATH,O_PATH, FILENAME) = ('./in/', './out/', 'loving.jpg')

##############################################################################
# Load images
##############################################################################
path = I_PATH + FILENAME
bgr = cv2.imread(path)
img = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
(height, width, depth) = img.shape

##############################################################################
# Cluster for dominance
##############################################################################
(colors, labels) = aux.calcDominantColors(
        img, cltsNumb=CLST_NUM, maxIter=MAX_ITER
    )
(hexColors, rgbColors) = aux.calcHexAndRGBFromPalette(colors)
pltAppend = aux.genColorBars(img, PLT_HEIGHT, colors)

##############################################################################
# Put the image back together
##############################################################################
newImg = np.row_stack((
    pltAppend * 255,
    np.full((round(height * .02), width, depth), [255,255,255]),
    img,
    np.full((round(height * .02), width, depth), [255,255,255]),
    pltAppend * 255
))
imgOut = Image.fromarray(newImg.astype('uint8'), 'RGB')
imgOut.save('./out/' + FILENAME.split('.')[0] + '.png')
