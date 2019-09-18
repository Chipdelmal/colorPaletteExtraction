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
(I_PATH, O_PATH) = (
    '/Users/sanchez.hmsc/Desktop/Spirited/',
    '/Users/sanchez.hmsc/Desktop/SpiritedOut/'
)
(CLST_NUM, MAX_ITER, BAR_HEIGHT, WHT_HEIGHT) = (6, 1000, .1, .05)

##############################################################################
# Get filepaths
##############################################################################
filepaths = sorted(glob.glob(I_PATH + '*[.png, .jpg, .jpeg]'))
filesNumber = len(filepaths)

##############################################################################
# Run the dominance detection
##############################################################################
for (i, filename) in enumerate(filepaths):
    print('Processing image ' + str(i + 1) + '/' + str(filesNumber))
    (imgOut, swatch, palette) = aux.getDominancePalette(
            filename,
            clstNum=CLST_NUM, maxIters=MAX_ITER,
            colorBarHeight=BAR_HEIGHT, whiteHeight=WHT_HEIGHT
        )

    ###########################################################################
    # Export the results
    ###########################################################################
    name = filename.split('/')[-1].split('.')[0]
    imgOut.save(O_PATH + name + '_Frame.png')
    # swatch.save('O_PATH' + name + '_Swatch.png')
