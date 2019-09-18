# ############################################################################
# Color Palette Extraction
# ############################################################################
# Useful links
#   https://medium.com/@andrisgauracs/generating-color-palettes-from-movies-with-python-16503077c025
#   https://buzzrobot.com/dominant-colors-in-an-image-using-k-means-clustering-3c7af4622036
# ############################################################################
import aux
import glob

##############################################################################
# Setup paths and clusters number
##############################################################################
(I_PATH, O_PATH) = ('./in/', './out/')
(CLST_NUM, MAX_ITER, BAR_HEIGHT, WHT_HEIGHT) = (6, 1000, .05, .005)

##############################################################################
# Run the dominance detection
##############################################################################
filepaths = glob.glob(I_PATH + '*[.png, .jpg, .jpeg]')
for filename in filepaths:
    (imgOut, swatch, palette) = aux.getDominancePalette(
            filename,
            clstNum=CLST_NUM,
            maxIters=MAX_ITER,
            colorBarHeight=BAR_HEIGHT,
            whiteHeight=WHT_HEIGHT
        )

    ###########################################################################
    # Export the results
    ###########################################################################
    name = filename.split('/')[-1].split('.')[0]
    imgOut.save('./out/' + name + '_Frame.png')
    swatch.save('./out/' + name + '_Swatch.png')
