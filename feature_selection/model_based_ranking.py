__author__ = 'vdthoang'

from sklearn.cross_validation import cross_val_score, ShuffleSplit
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import numpy as np

# Load boston housing dataset as an example
boston = load_boston()
X = boston["data"]
Y = boston["target"]
names = boston["feature_names"]

rf = LinearRegression()
scores = []
for i in range(X.shape[1]):
     score = cross_val_score(rf, X[:, i:i+1], Y, scoring="r2", cv=ShuffleSplit(len(X), 4, .25))
     scores.append((round(np.mean(score), 3), names[i]))
list_scores = sorted(scores, reverse=True)

for value in list_scores:
    print value[1] + '\t' + str(value[0])




