import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import sklearn
print(sklearn.__version__)

print(np.__version__)
x, y = make_regression(n_samples= 100, random_state=0)
# print(x[:10])
# print(y[:10])
lr= LinearRegression()

result = cross_validate(lr, x, y)
print(result)
print(result['test_score'])