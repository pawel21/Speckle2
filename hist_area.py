# -*- coding: utf-8 -*-
"""
Spyder Editor

This is script to find threshold on all image in dir.
"""
import fnmatch
import matplotlib.pyplot as plt
import numpy as np
import os
from skimage import io
from skimage.filters import threshold_otsu

from timer import timer

@timer
def find_threshold(list_of_bitmap_file):
    threshold_value_for_each_image = []
    for f in list_of_bitmap_file:
        image = io.imread(f)
        thresh = threshold_otsu(image)
        threshold_value_for_each_image.append(thresh)
    return threshold_value_for_each_image

@timer
def find_numbers_of_pixel_greter_than_threshold(list_of_bitmap_file):
    threshold_value_for_each_image = []
    numbers_of_pixel_greter_than_threshold = [] 
    for f in list_of_bitmap_file:
        image = io.imread(f)
        thresh = threshold_otsu(image)
        threshold_value_for_each_image.append(thresh)
        numbers_of_pixel_greter_than_threshold.append(np.sum(np.sum(image>thresh)))
    return numbers_of_pixel_greter_than_threshold

cwd = os.getcwd()

image_dir_path = os.listdir(os.path.join(cwd, "E10", "Dzien4"))
images_path_list = []

for f in image_dir_path:
   if fnmatch.fnmatch(f, '*.BMP'):
       images_path_list.append(os.path.join(cwd, "E10", "Dzien4",f)) 

threshold = find_threshold(images_path_list)       
plt.hist(threshold)

pixel = find_numbers_of_pixel_greter_than_threshold(images_path_list)

#threshold_value_for_each_image = []
#numbers_of_pixel_greter_than_threshold = []       

       # image = io.imread(os.path.join(cwd, "E10", "Dzien4", f))
       # thresh = threshold_otsu(image)
       # threshold_value_for_each_image.append(thresh)
       # numbers_of_pixel_greter_than_threshold.append(np.sum(np.sum(image>thresh)))

#plt.hist(threshold_value_for_each_image)
#plt.hist(numbers_of_pixel_greter_than_threshold)