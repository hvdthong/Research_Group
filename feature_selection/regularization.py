__author__ = 'vdthoang'

import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression


# A helper method for pretty-printing linear models
def print_coefficient(coefs, names=None, sort=False):
    lst = zip(coefs, names)
    if sort:
        lst = sorted(lst,  key = lambda x:-np.abs(x[0]))
    return " + ".join("%s * %s" % (round(coef, 3), name) for coef, name in lst)


boston = load_boston()
X = boston["data"]
Y = boston["target"]
names = boston["feature_names"]

lr = LinearRegression()
lr.fit(X, Y)


print 'Linear_models: ', print_coefficient(lr.coef_, names)

# list_coef = lr.coef_
# for i in range(0, len(list_coef)):
#     print str(list_coef[i]) + '\t' + names[i]
