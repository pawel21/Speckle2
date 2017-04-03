import matplotlib.pyplot as plt
import numpy as np
import os
from skimage import io
from skimage.filters import threshold_otsu

from scipy import misc
from scipy import ndimage

CCD_AREA = 0.08602 #cm^2
IMG_PIXELS = 350208


img = io.imread("/home/pawel1/Pulpit/Studia/Python/Speckle/E10/Dzien4/1T04633I.BMP")

img = img[100:300, 300:450]
threshold = img.mean()
speckle_pixel = np.sum(np.sum(img > threshold))

eroded_square = ndimage.binary_erosion(img)
reconstruction = ndimage.binary_propagation(eroded_square, mask=img)


fig, axes = plt.subplots(ncols=3, figsize=(8, 4.5))
ax = axes.ravel()
ax[0] = plt.subplot(1, 3, 1)
ax[1] = plt.subplot(1, 3, 2)
ax[2] = plt.subplot(1, 3, 3)

ax[0].imshow(img, cmap=plt.cm.gray)
ax[1].imshow(img > threshold, cmap=plt.cm.gray)
ax[2].imshow(reconstruction)

plt.show()