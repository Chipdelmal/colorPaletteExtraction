
import cv2
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
# from sklearn.cluster import MiniBatchKMeans


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


def genColorBar(img, heightProp, palette):
    clstNumber = len(palette)
    (height, width, depth) = img.shape
    pltAppend = np.zeros((round(height * heightProp), width, depth))
    (wBlk, hBlk) = (round(width / clstNumber), round(height * heightProp))
    for row in range(hBlk):
        colorIter = -1
        for col in range(width):
            if (col % wBlk == 0) and (colorIter < clstNumber - 1):
                colorIter = colorIter + 1
            pltAppend[row][col] = palette[colorIter]
    return pltAppend * 255


def getDominancePalette(
            imgPath,
            clstNum=6,
            maxIters=1000,
            colorBarHeight=.03,
            whiteHeight=.005
        ):
    # Load image
    bgr = cv2.imread(imgPath)
    img = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    (height, width, depth) = img.shape

    # Cluster for dominance
    (colors, labels) = calcDominantColors(
            img, cltsNumb=clstNum, maxIter=maxIters
        )
    (hexColors, rgbColors) = calcHexAndRGBFromPalette(colors)
    colorsBars = genColorBar(img, colorBarHeight, colors)

    # Put the image back together
    whiteBar = np.full(
            (round(height * whiteHeight), width, depth),
            [255, 255, 255]
        )
    newImg = np.row_stack((
            whiteBar, colorsBars,
            img,
            colorsBars, whiteBar
        ))
    palette = calcHexAndRGBFromPalette(colors)
    swatch = Image.fromarray(colorsBars.astype('uint8'), 'RGB')
    imgOut = Image.fromarray(newImg.astype('uint8'), 'RGB')
    return (imgOut, swatch, palette)
