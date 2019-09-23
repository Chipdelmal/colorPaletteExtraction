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
FILENAME = 'mononoke1.jpg'
(I_PATH, O_PATH) = ('./in/', './out/')
(CLST_NUM, MAX_ITER) = (6, 1000)
(BAR_HEIGHT, BUF_HEIGHT, BUF_COLOR) = (.05, .005, [255, 255, 255])

##############################################################################
# Run the dominance detection
##############################################################################
path = I_PATH + FILENAME
(imgOut, swatch, palette) = aux.getDominancePalette(
        path,
        clstNum=CLST_NUM, maxIters=MAX_ITER,
        colorBarHeight=BAR_HEIGHT, bufferHeight=BUF_HEIGHT,
        colorBuffer=BUF_COLOR
    )

##############################################################################
# Export the results
##############################################################################
name = path.split('/')[-1].split('.')[0]
imgOut.save(O_PATH + name + '_Frame.png')
swatch.save(O_PATH + name + '_Swatch.png')
aux.writeColorPalette(O_PATH + name + ".tsv", palette)
