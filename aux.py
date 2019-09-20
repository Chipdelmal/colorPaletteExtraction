
import cv2
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
# from sklearn.cluster import MiniBatchKMeans


def reshapeColor(colorEightBit):
    '''
    Returns a color triplet in the range of 0 to 1 from 0 to 255.
    '''
    return [i / 255 for i in colorEightBit]


def upscaleColor(color):
    '''
    Returns a color triplet of 0 to 255 from 0 to 1.
    '''
    return [i * 255 for i in color]


def rgb_to_hex(rgb):
    '''
    Converts an RGB triplet to its hex equivalent.
    '''
    return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))


def calcDominantColors(img, cltsNumb=10, maxIter=1000):
    '''
    Returns a tuple with the dominant colors arrays and their
        clustering labels (sklearn).
    '''
    frame = img.reshape((img.shape[0] * img.shape[1], 3))
    # Cluster the colors for dominance detection
    kmeans = KMeans(n_clusters=cltsNumb, max_iter=maxIter).fit(frame)
    (palette, labels) = (kmeans.cluster_centers_, kmeans.labels_)
    # Rescale the colors for matplotlib
    colors = [reshapeColor(color) for color in palette]
    return (colors, labels)


def calcHexAndRGBFromPalette(palette):
    '''
    Returns the hex and RGB codes for the colors in a palette.
    '''
    sortedPalette = [upscaleColor(i) for i in palette]
    (hexColors, rgbColors) = (
            [rgb_to_hex(i) for i in sortedPalette],
            sortedPalette
        )
    return {'hex': hexColors, 'rgb':rgbColors}


def genColorSwatch(img, heightProp, palette):
    '''
    Creates a color swatch that is proportional in height to the original
       image (whilst being the same width).
    '''
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


def genColorBar(width, height, color=[0,0,0], depth=3):
    '''
    Creates a solid color bar to act as visual buffer between frames rows.
    '''
    colorBar = np.full(
            (height, width, depth),
            color
        )
    return colorBar

def getDominancePalette(
            imgPath,
            clstNum=6,
            maxIters=1000,
            colorBarHeight=.03,
            whiteHeight=.005,
            colorBuffer=[0,0,0]
        ):
    '''
    Wrapper function that puts together all the elements to create the frame
        with its swatch, and buffer bars.
    '''
    # Load image
    bgr = cv2.imread(imgPath)
    img = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    (height, width, depth) = img.shape

    # Cluster for dominance
    (colors, labels) = calcDominantColors(
            img, cltsNumb=clstNum, maxIter=maxIters
        )
    (hexColors, rgbColors) = calcHexAndRGBFromPalette(colors)
    # Create color swatch
    colorsBars = genColorSwatch(img, colorBarHeight, colors)
    # Put the image back together
    whiteBar = genColorBar(
            width, round(height * whiteHeight), color=colorBuffer
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
