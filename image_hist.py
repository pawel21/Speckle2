import numpy as np
import matplotlib.pyplot as plt
import os

from scipy import misc
from scipy.stats import kurtosis
from scipy.stats import skew

cwd = os.getcwd()
path = os.path.join(cwd, "test", '1T03702L.BMP')

img = misc.imread(path)
fig, axes = plt.subplots()
axes.hist(img.ravel(), bins=256)
axes.set_xlabel("Intersity")

print("Mean = {}".format(np.mean(img.ravel())))
print("Variance = {}".format(np.var(img.ravel())))
print("Standard deviration = {}".format(np.std(img.ravel())))
print("Kurtosis = {}".format(kurtosis(img.ravel())))
print("Skewness = {}".format(skew(img.ravel())))

plt.show()