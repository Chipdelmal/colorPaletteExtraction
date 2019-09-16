# ############################################################################
# Color Palette Extraction
#   https://medium.com/@andrisgauracs/generating-color-palettes-from-movies-with-python-16503077c025
# ############################################################################

import cv2
import glob
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
