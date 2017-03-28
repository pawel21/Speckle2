# -*- coding: utf-8 -*-
"""
Spyder Editor

This is script to find threshold on image.
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from skimage import io
from skimage.filters import threshold_otsu

print(os.getcwd())
image = io.imread("/home/pawel1/Pulpit/Studia/Python/Speckle/E10/Dzien4/1T04629J.BMP")
thresh = threshold_otsu(image)
binary = image > thresh

fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
ax = axes.ravel()
ax[0] = plt.subplot(1, 3, 1, adjustable='box-forced')
ax[1] = plt.subplot(1, 3, 2)
ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0], adjustable='box-forced')

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram')
ax[1].axvline(thresh, color='r')

ax[2].imshow(binary, cmap=plt.cm.gray)
ax[2].set_title('Thresholded')
ax[2].axis('off')

plt.show()