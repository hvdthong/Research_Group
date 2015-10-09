__author__ = 'vdthoang'
from sklearn.datasets import load_boston
from sklearn.feature_selection import RFECV
from sklearn.svm import SVR

boston = load_boston()
X = boston["data"]
Y = boston["target"]
names = boston["feature_names"]


estimator = SVR(kernel="linear")
selector = RFECV(estimator, step=1, cv=5)
selector = selector.fit(X, Y)

print selector.ranking_
print names


