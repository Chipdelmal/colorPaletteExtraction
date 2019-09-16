# ############################################################################
# Color Palette Extraction
# ############################################################################
# Useful links
#   https://medium.com/@andrisgauracs/generating-color-palettes-from-movies-with-python-16503077c025
# ############################################################################

import cv2
import glob
import numpy as np
# from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from matplotlib import pyplot as plt

def rescaleColor(colorEightBit):
    return [i / 255 for i in colorEightBit]

##############################################################################
# Setup paths and clusters number
##############################################################################
(CLST_NUMBER, MAX_ITER) = (10, 100)
(I_PATH,O_PATH) = ('./in/', './out/')

##############################################################################
# Load images
##############################################################################
filepaths = sorted(glob.glob(I_PATH + '*.jpg'))

path = filepaths[0]
frame = cv2.imread(path)

# (rows, cols, rgb)  = frame.shape
# (flattenedFrame, clstdColors) = ([None] * (rows * cols), [])
# for (i, row) in enumerate(frame):
#     for (j, col) in enumerate(row):
#         flattenedFrame.append(list(col))
# kmeans = MiniBatchKMeans(n_clusters=CLST_NUMBER, max_iter=100).fit(flattenedFrame)

(flatFrame, clusters) = ([], [])
for row in frame:
    for col in row:
        flatFrame.append(list(col))
kmeans = MiniBatchKMeans(n_clusters=CLST_NUMBER, max_iter=MAX_ITER).fit(flatFrame)
palette = kmeans.cluster_centers_
rescale = [rescaleColor(color) for color in palette]
clusters.append(rescale)
clusters
