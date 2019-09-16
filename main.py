# ############################################################################
# Color Palette Extraction
# ############################################################################
# Useful links
#   https://medium.com/@andrisgauracs/generating-color-palettes-from-movies-with-python-16503077c025
#   https://buzzrobot.com/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036
# ############################################################################

import cv2
import glob
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from matplotlib import pyplot as plt

def rescaleColor(colorEightBit):
    return [i / 255 for i in colorEightBit]

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

##############################################################################
# Setup paths and clusters number
##############################################################################
(CLST_NUMBER, MAX_ITER) = (15, 1000)
(I_PATH,O_PATH) = ('./in/', './out/')

##############################################################################
# Load images
##############################################################################
filepaths = sorted(glob.glob(I_PATH + '*.jpg'))

path = filepaths[1]
print(path)
frame = cv2.imread(path)


(flatFrame, clusters) = ([], [])
frame = frame.reshape((frame.shape[0] * frame.shape[1], 3))
kmeans = KMeans(n_clusters = CLST_NUMBER).fit(frame)
(palette, labels) = (kmeans.cluster_centers_, kmeans.labels_)
rescale = [rescaleColor(color) for color in palette]
clusters.append(rescale)
sortedClusters = [sorted(cls) for cls in clusters]

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')
plt.imshow(list(map(list, zip(*sortedClusters))))
