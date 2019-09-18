# ############################################################################
# Color Palette Extraction
# ############################################################################
# Useful links
#   https://medium.com/@andrisgauracs/generating-color-palettes-from-movies-with-python-16503077c025
#   https://buzzrobot.com/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036
# ############################################################################
import aux

##############################################################################
# Setup paths and clusters number
##############################################################################
FILENAME = 'spirited.jpg'
(I_PATH, O_PATH) = ('./in/', './out/')
(CLST_NUM, MAX_ITER, BAR_HEIGHT, WHT_HEIGHT) = (10, 1000, .05, .005)

##############################################################################
# Run the dominance detection
##############################################################################
path = I_PATH + FILENAME
(imgOut, swatch, palette) = aux.getDominancePalette(
        path,
        clstNum=CLST_NUM, maxIters=MAX_ITER,
        colorBarHeight=BAR_HEIGHT, whiteHeight=WHT_HEIGHT
    )

##############################################################################
# Export the results
##############################################################################
imgOut.save('./out/' + FILENAME.split('.')[0] + '_Frame.png')
swatch.save('./out/' + FILENAME.split('.')[0] + '_Swatch.png')
