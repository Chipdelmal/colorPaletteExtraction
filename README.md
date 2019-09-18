# Color Palette Extraction

This script calculates the dominant colors of an image by using k-means clustering, and returns the obtained color palette. It can be used in batch to generate the grid of the changes in color palettes in a movie (provided that we have the frames which can be obtained with ffmpeg).

## Instructions

For easiest use (in batch):

1. Place your images in the `./in/` folder.
2. Run `batch.py`.
3. All the processed files will be exported to the `./out/` folder.

<img src="./media/frame.jpg">

To change style parameters:

* **CLST_NUM**: Defines the number of dominant colors to detect.
* **MAX_ITER**: Sets the maximum number of iterations for the _k-means_ algorithm.
* **BAR_HEIGHT**: Defines the height of the dominant colors bar as a proportion of the height of the input image.
* **WHT_HEIGHT**: Sets the white buffer zone as a proportion of the height of the input image.

<img src="./media/loving.jpg" width='100%'>

##  Dependencies

The script needs the following dependencies to be installed either in the base installation or a virtual environment: [cv2](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html), [Pillow](https://pillow.readthedocs.io/en/stable/), [numpy](https://numpy.org/), [sklearn](https://scikit-learn.org/stable/).


<img src="./media/vincent.jpg" width='100%'>

## Still To Do

* Overlay the hex code to the swatch
* Translate the grid generator from _Mathematica_ to _Python_.
* Link to the repo with the frames exporter.

<hr>

<img src="./media/pusheen.jpg" height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/)
