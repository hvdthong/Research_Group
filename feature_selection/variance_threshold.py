__author__ = 'vdthoang'
from sklearn.feature_selection import VarianceThreshold
from sklearn.datasets import load_boston

# X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
#
# for cols in X:
#     print cols
#
# sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
# print sel.fit_transform(X)

# Load boston housing dataset as an example
boston = load_boston()
X = boston["data"]
Y = boston["target"]
names = boston["feature_names"]

sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
X_transform = sel.fit_transform(X)

