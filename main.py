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



##############################################################################
# Setup paths and clusters number
##############################################################################
(CLST_NUMBER, MAX_ITER) = (8, 1000)
(I_PATH,O_PATH) = ('./in/', './out/')

##############################################################################
# Load images
##############################################################################
filepaths = sorted(glob.glob(I_PATH + '*.jpg'))

path = filepaths[2]
print(path)

# Read image and flatten it
frame = cv2.imread(path)
frame = frame.reshape((frame.shape[0] * frame.shape[1], 3))
# Cluster the colors for dominance detection
kmeans = KMeans(n_clusters = CLST_NUMBER).fit(frame)
(palette, labels) = (kmeans.cluster_centers_, kmeans.labels_)
# Rescale the colors for matplotlib
(clusters, rescale) = ([], [aux.reshapeColor(color) for color in palette])
clusters.append(rescale)
sortedClusters = [sorted(cls) for cls in clusters]
# Plot results
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')
plt.imshow(list(map(list, zip(*sortedClusters))))
