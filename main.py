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
# from sklearn.cluster import KMeans
# from sklearn.cluster import MiniBatchKMeans
from matplotlib import pyplot as plt
from PIL import Image

##############################################################################
# Setup paths and clusters number
##############################################################################
(CLST_NUMBER, MAX_ITER) = (8, 1000)
(I_PATH,O_PATH) = ('./in/', './out/')
SELECTION = 1

##############################################################################
# Load images
##############################################################################
filepaths = sorted(glob.glob(I_PATH + '*.jpg'))
path = filepaths[SELECTION]
print(path)

##############################################################################
# Cluster for dominance
##############################################################################
bgr = cv2.imread(path)
img = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
(colors, labels) = aux.calcDominantColors(
        img, clustersNumber=CLST_NUMBER, maxIter=MAX_ITER
    )
sortedPalette = [sorted(cls) for cls in [colors]][0]
(hexColors, rgbColors) = aux.calcHexAndRGBFromPalette(sortedPalette)

(height, width, depth) = img.shape
paletteAppend = np.zeros((round(height * .1), width, depth))

(wBlock, hBlock) = (round(width / CLST_NUMBER), round(height * .1))
for row in range(hBlock):
    colorIter = -1
    for col in range(width):
        if (col % wBlock == 0) and (colorIter < CLST_NUMBER - 1):
            colorIter = colorIter + 1
        paletteAppend[row][col] = sortedPalette[colorIter]

Image.fromarray((paletteAppend * 255).astype('uint8'), 'RGB')
newImg = np.row_stack((
    paletteAppend * 255,
    np.full((round(height * .02), width, depth), [255,255,255]),
    img,
    np.full((round(height * .02), width, depth), [255,255,255]),
    paletteAppend * 255
))
imgOut = Image.fromarray(newImg.astype('uint8'), 'RGB')
imgOut.save("./out/palette.png")
