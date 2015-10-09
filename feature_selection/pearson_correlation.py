__author__ = 'vdthoang'

import numpy as np
from scipy.stats import pearsonr
from sklearn.datasets import load_boston

# np.random.seed(0)
# size = 300
# x = np.random.normal(0, 1, size)
# x_low = x + np.random.normal(0, 1, size)
# x_high = x + np.random.normal(0, 10, size)
# print x_high
# print "Lower noise", pearsonr(x, x_low)[0]  # first value is pearson correlation, second is p-value
# print "Higher noise", pearsonr(x, x_high)[0]
#
# from scipy.spatial.distance import correlation, euclidean
# print correlation(np.array(x), np.array(x_low))
# print euclidean(np.array(x), np.array(x_low))
# print spsd(x, x_high)

# Load boston housing dataset as an example
boston = load_boston()
X = boston["data"]
Y = boston["target"]
names = boston["feature_names"]
print names

list_features = []
for i in range(X.shape[1]):
    list_features.append(X[:, i:i+1])

print len(list_features)

list_score = []
for i in range(0, len(list_features)):
    feature_first = list_features[i]
    score = 0
    for j in range(0, len(list_features)):
        feature_second = list_features[j]
        value_pearson = pearsonr(feature_first, feature_second)
        score += value_pearson[0]
    list_score.append(score)

for i in range(0, len(list_score)):
    print names[i] + '\t' + str(float(list_score[i]))
