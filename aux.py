
import cv2
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans


def reshapeColor(colorEightBit):
    return [i / 255 for i in colorEightBit]


def upscaleColor(color):
    return [i * 255 for i in color]


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))


def calcDominantColors(img, cltsNumb=10, maxIter=1000):
    frame = img.reshape((img.shape[0] * img.shape[1], 3))
    # Cluster the colors for dominance detection
    kmeans = KMeans(n_clusters=cltsNumb, max_iter=maxIter).fit(frame)
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


def genColorBars(img, heightProp, palette):
    clstNumber = len(palette)
    (height, width, depth) = img.shape
    pltAppend = np.zeros((round(height * heightProp), width, depth))
    (wBlk, hBlk) = (round(width / clstNumber),round(height * heightProp))
    for row in range(hBlk):
        colorIter = -1
        for col in range(width):
            if (col % wBlk == 0) and (colorIter < clstNumber - 1):
                colorIter = colorIter + 1
            pltAppend[row][col] = palette[colorIter]
    return pltAppend * 255
