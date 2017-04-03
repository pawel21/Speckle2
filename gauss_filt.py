import matplotlib.pyplot as plt
import numpy as np
import os
from skimage import io
from scipy.ndimage.filters import gaussian_filter

img = io.imread("E10/Dzien4/1T04629J.BMP")

filt_img = gaussian_filter(img, sigma=2)

fig, ax = plt.subplots(ncols=2)

ax[0].imshow(img)
ax[1].imshow(filt_img)

plt.show()