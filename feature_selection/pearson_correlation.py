__author__ = 'vdthoang'

import numpy as np
from scipy.stats import pearsonr
np.random.seed(0)
size = 300
x = np.random.normal(0, 1, size)
x_low = x + np.random.normal(0, 1, size)
x_high = x + np.random.normal(0, 10, size)
print x_high
print "Lower noise", pearsonr(x, x_low)[0]  # first value is pearson correlation, second is p-value
print "Higher noise", pearsonr(x, x_high)[0]

from scipy.spatial.distance import correlation, euclidean
print correlation(np.array(x), np.array(x_low))
print euclidean(np.array(x), np.array(x_low))
# print spsd(x, x_high)
