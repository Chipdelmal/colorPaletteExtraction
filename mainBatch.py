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
(CLST_NUM, MAX_ITER) = (6, 1000)
(BAR_HEIGHT, BUF_HEIGHT, BUF_COLOR) = (.1, .1, [0, 0, 0])

##############################################################################
# Get filepaths
##############################################################################
filepaths = sorted(glob.glob(I_PATH + '*[.png, .jpg, .jpeg]'))
filesNumber = len(filepaths)

##############################################################################
# Run the dominance detection
##############################################################################
for (i, filename) in enumerate(filepaths):
    print('* Processing image '+str(i+1)+'/'+str(filesNumber), end='\r')
    (imgOut, swatch, palette) = aux.getDominancePalette(
            filename,
            clstNum=CLST_NUM, maxIters=MAX_ITER,
            colorBarHeight=BAR_HEIGHT, bufferHeight=BUF_HEIGHT,
            colorBuffer=BUF_COLOR
        )

    ###########################################################################
    # Export the results
    ###########################################################################
    name = filename.split('/')[-1].split('.')[0]
    imgOut.save(O_PATH + name + '_Frame.png')
