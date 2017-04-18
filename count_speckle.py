import numpy as np
import matplotlib.pyplot as plt
import mahotas as mh
import os

cwd = os.getcwd()
img = mh.imread(os.path.join(cwd, "E10", "Dzien4", "1T04633I.BMP"))

fig, axes = plt.subplots(ncols=4, figsize=(10, 5.5))

T = mh.thresholding.otsu(img)

img_filt = mh.gaussian_filter(img, 10)
labeled, nr_objects = mh.label(img_filt > T)
T_filt = mh.thresholding.otsu(img_filt.astype('uint8'))

obj_areas = np.sum(np.sum(img_filt>T))
print("mean area {}".format(obj_areas/nr_objects))


axes[0].imshow(img, cmap=plt.cm.gray)
axes[0].set_title("orginal image")
axes[1].imshow(img > T_filt, cmap=plt.cm.gray)
axes[1].set_title("Threshold")
axes[2].imshow(img_filt, cmap=plt.cm.gray)
axes[2].set_title("Gauss filt")
axes[3].imshow(img_filt > T_filt, cmap=plt.cm.gray)



plt.show()