import matplotlib.pyplot as plt
import numpy as np
import os
from skimage import io
from skimage.filters import threshold_otsu

from scipy import misc

CCD_AREA = 0.08602 #cm^2
IMG_PIXELS = 350208


img = io.imread("/home/pawel1/Pulpit/Studia/Python/Speckle/E10/Dzien4/1T04633I.BMP")


threshold = img.mean()
speckle_pixel = np.sum(np.sum(img > threshold))

speckle_area = (speckle_pixel/IMG_PIXELS) * CCD_AREA
print(speckle_area)
fig, axes = plt.subplots(ncols=2, figsize=(8, 4.5))
ax = axes.ravel()
ax[0] = plt.subplot(1, 2, 1)
ax[1] = plt.subplot(1, 2, 2)

ax[0].imshow(img, cmap=plt.cm.gray)
ax[1].imshow(img > threshold, cmap=plt.cm.gray)
