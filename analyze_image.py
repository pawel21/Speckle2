import numpy as np
import matplotlib.pyplot as plt
import os

from scipy import misc
from scipy import ndimage
from scipy.ndimage import label
from scipy.ndimage import center_of_mass
from scipy.spatial import distance
from scipy.stats import kurtosis

CCD_AREA = 0.08602  # cm^2
IMG_PIXELS = 350208
SIGMA = 10

cwd = os.getcwd()
path = os.path.join(cwd, "test", '1T04633E.BMP')

img = misc.imread(path)
fig, axes = plt.subplots(ncols=4, figsize=(10, 5.5))
threshold = np.mean(img)

img_filt = ndimage.gaussian_filter(img, SIGMA)
labeled, nr_objects = label(img_filt > threshold)
T_filt = np.mean(img_filt)

for k in range(1, nr_objects+1):
    location = str(center_of_mass(img, labeled, k))
    print("Object {} center of mass at {}".format(k, location))

speckle_pixel = np.sum(np.sum(img > threshold))
speckle_area = (speckle_pixel / IMG_PIXELS) * CCD_AREA

# find distance between spekle
distance_between_1_2 = distance.euclidean(center_of_mass(img, labeled, 1), center_of_mass(img, labeled, 2))
distance_between_1_3 = distance.euclidean(center_of_mass(img, labeled, 1), center_of_mass(img, labeled, 3))
distance_between_1_4 = distance.euclidean(center_of_mass(img, labeled, 1), center_of_mass(img, labeled, 4))
print("Distace between 1 and 2 = {}".format(distance_between_1_2))
print("Distace between 1 and 3 = {}".format(distance_between_1_3))
print("Distace between 1 and 4 = {}".format(distance_between_1_4))

axes[0].imshow(img, cmap=plt.cm.gray)
axes[0].set_title("orginal image")
axes[1].imshow(img > T_filt, cmap=plt.cm.gray)
axes[1].set_title("Threshold = {0}".format(threshold))
axes[2].imshow(img_filt, cmap=plt.cm.gray)
axes[2].set_title("Gauss filt, $\sigma$ = {0}".format(SIGMA))

axes[3].imshow(img_filt > T_filt, cmap=plt.cm.gray)

x_12 = []
y_12 = []
x_12.append(center_of_mass(img, labeled, 1)[0])
x_12.append(center_of_mass(img, labeled, 2)[0])
y_12.append(center_of_mass(img, labeled, 1)[1])
y_12.append(center_of_mass(img, labeled, 2)[1])

x_13 = []
y_13 = []
x_13.append(center_of_mass(img, labeled, 1)[0])
x_13.append(center_of_mass(img, labeled, 3)[0])
y_13.append(center_of_mass(img, labeled, 1)[1])
y_13.append(center_of_mass(img, labeled, 3)[1])

x_14 = []
y_14 = []
x_14.append(center_of_mass(img, labeled, 1)[0])
x_14.append(center_of_mass(img, labeled, 4)[0])
y_14.append(center_of_mass(img, labeled, 1)[1])
y_14.append(center_of_mass(img, labeled, 4)[1])

axes[3].plot(y_12, x_12, 'r-', lw=3)
axes[3].plot(y_13, x_13, 'r-', lw=3)
axes[3].plot(y_14, x_14, 'r-', lw=3)
axes[3].set_title("numbers of speckle = {0} \n $P = {1:.6f}  cm^2$".format(nr_objects, speckle_area))

plt.show()


