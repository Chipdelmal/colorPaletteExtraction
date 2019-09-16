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
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from matplotlib import pyplot as plt

##############################################################################
# Setup paths and clusters number
##############################################################################
(CLST_NUMBER, MAX_ITER) = (8, 1000)
(I_PATH,O_PATH) = ('./in/', './out/')
SELECTION = 2

##############################################################################
# Load images
##############################################################################
filepaths = sorted(glob.glob(I_PATH + '*.jpg'))
path = filepaths[SELECTION]
print(path)

##############################################################################
# Cluster for dominance
##############################################################################
img = cv2.imread(path)
(colors, labels) = aux.calcDominantColors(img, clustersNumber=10, maxIter=1000)
sortedPalette = [sorted(cls) for cls in [colors]][0]
(hexColors, rgbColors) = aux.calcHexAndRGBFromPalette(sortedPalette)

##############################################################################
# Plot palette
##############################################################################
(fig, ax) = plt.subplots(figsize=(10, 5))
ax.axis('off')
plt.imshow(list(map(list, zip(*[sortedPalette]))))
