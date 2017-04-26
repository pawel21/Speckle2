# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:50:31 2017

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import os

from scipy import misc
from scipy import ndimage
from scipy.ndimage import label
from scipy.ndimage import center_of_mass
from scipy.spatial import distance
from scipy.stats import kurtosis

plt.style.use("bmh")
plt.rcParams.update({'font.size': 15})

CCD_AREA = 0.08602  # cm^2
IMG_PIXELS = 350208
SIGMA = 12

cwd = os.getcwd()
path = os.path.join(cwd, "test", '1T03702L.BMP')



def calcurate_distance_between_1_and_n(location_list):
    distance_dict = {}
    for n in range(1, len(location_list)):
        distance_dict["distance between 1 and {}".format(n+1)] = \
                      distance.euclidean(location_list[0], location_list[n])
    return distance_dict    

def calcurate_distance_between_2_and_n(location_list):
    distance_dict = {}
    for n in range(2, len(location_list)):
        distance_dict["distance between 2 and {}".format(n+1)] = \
                      distance.euclidean(location_list[1], location_list[n])
    return distance_dict   

img = misc.imread(path)
fig, axes = plt.subplots(ncols=4, figsize=(10, 5.5))
threshold = np.mean(img)

img_filt = ndimage.gaussian_filter(img, SIGMA)
labeled, nr_objects = label(img_filt > threshold)
T_filt = np.mean(img_filt)

location_list = []
for k in range(1, nr_objects+1):
    location_list.append(center_of_mass(img, labeled, k))
    location = str(center_of_mass(img, labeled, k))
    print("Object {} center of mass at {}".format(k, location))
    



axes[0].imshow(img, cmap=plt.cm.gray)
axes[0].set_title("orginal image")
axes[1].imshow(img > T_filt, cmap=plt.cm.gray)
axes[1].set_title("Threshold = {0}".format(threshold))
axes[2].imshow(img_filt, cmap=plt.cm.gray)
axes[2].set_title("Gauss filt, $\sigma$ = {0}".format(SIGMA))

axes[3].imshow(img_filt > T_filt, cmap=plt.cm.gray)

for k in range(1, nr_objects+1):
    location = (center_of_mass(img, labeled, k))
    axes[3].text(location[1], location[0], '{}'.format(k), size=20, color='red')

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

x_15 = []
y_15 = []
x_15.append(center_of_mass(img, labeled, 1)[0])
x_15.append(center_of_mass(img, labeled, 5)[0])
y_15.append(center_of_mass(img, labeled, 1)[1])
y_15.append(center_of_mass(img, labeled, 5)[1])

x_16 = []
y_16 = []
x_16.append(center_of_mass(img, labeled, 1)[0])
x_16.append(center_of_mass(img, labeled, 6)[0])
y_16.append(center_of_mass(img, labeled, 1)[1])
y_16.append(center_of_mass(img, labeled, 6)[1])

x_17 = []
y_17 = []
x_17.append(center_of_mass(img, labeled, 1)[0])
x_17.append(center_of_mass(img, labeled, 7)[0])
y_17.append(center_of_mass(img, labeled, 1)[1])
y_17.append(center_of_mass(img, labeled, 7)[1])

x_18 = []
y_18 = []
x_18.append(center_of_mass(img, labeled, 1)[0])
x_18.append(center_of_mass(img, labeled, 8)[0])
y_18.append(center_of_mass(img, labeled, 1)[1])
y_18.append(center_of_mass(img, labeled, 8)[1])

axes[3].plot(y_12, x_12, 'r-', lw=3)
axes[3].plot(y_13, x_13, 'r-', lw=3)
axes[3].plot(y_14, x_14, 'r-', lw=3)
axes[3].plot(y_15, x_15, 'r-', lw=3)
axes[3].plot(y_16, x_16, 'r-', lw=3)
axes[3].plot(y_17, x_17, 'r-', lw=3)
axes[3].plot(y_18, x_18, 'r-', lw=3)
axes[3].set_title("numbers of speckle = {0}".format(nr_objects))

plt.show()
