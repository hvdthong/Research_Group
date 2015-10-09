__author__ = 'vdthoang'
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

for cols in X:
    print cols

sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
print sel.fit_transform(X)
