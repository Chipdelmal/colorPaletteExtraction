
import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans


def reshapeColor(colorEightBit):
    # Transforming 0/255 BGR to 0/1 RGB
    # colors = list(colorEightBit)
    # colors.reverse()
    return [i / 255 for i in colorEightBit]


def upscaleColor(color):
    return [i * 255 for i in color]


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))


def calcDominantColors(img, clustersNumber=10, maxIter=1000):
    frame = img.reshape((img.shape[0] * img.shape[1], 3))
    # Cluster the colors for dominance detection
    kmeans = KMeans(n_clusters=clustersNumber, max_iter=maxIter).fit(frame)
    (palette, labels) = (kmeans.cluster_centers_, kmeans.labels_)
    # Rescale the colors for matplotlib
    colors = [reshapeColor(color) for color in palette]
    return (colors, labels)


def calcHexAndRGBFromPalette(palette):
    sortedPalette = [upscaleColor(i) for i in palette]
    (hexColors, rgbColors) = (
            [rgb_to_hex(i) for i in sortedPalette],
            sortedPalette
        )
    return (hexColors, rgbColors)
