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
(I_PATH,O_PATH, FILENAME) = ('./in/', './out/', 'frame.jpg')
(CLST_NUM, MAX_ITER, BAR_HEIGHT, WHT_HEIGHT) = (10, 1000, .03, .005)

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
colorsBars = aux.genColorBars(img, BAR_HEIGHT, colors)

##############################################################################
# Put the image back together
##############################################################################
whiteBar = np.full((round(height * WHT_HEIGHT), width, depth), [255,255,255])
newImg = np.row_stack((
    whiteBar, colorsBars, whiteBar,
    img,
    whiteBar, colorsBars, whiteBar
))
imgOut = Image.fromarray(newImg.astype('uint8'), 'RGB')
imgOut.save('./out/' + FILENAME.split('.')[0] + '.png')
