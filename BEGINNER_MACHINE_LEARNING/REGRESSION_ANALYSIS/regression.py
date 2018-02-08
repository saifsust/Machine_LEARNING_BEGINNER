import pandas as pnds
import quandl as qnds
import matplotlib.pyplot as plot
import numpy as nmpy
from  sklearn import datasets
#data read

#data = pnds.read_csv('../DATA_SET/regression.csv')

#print(data.head())
irisData = datasets.load_iris()

#print(dt.data)

iris_x=irisData.data
iris_y=irisData.target
uniqueTarget=nmpy.unique(iris_y)
#print(uniqueTarget)


index =nmpy.random.permutation(iris_x)

iris_x_train=iris_x[index[:-10]]
iris_y_train=iris_y[index[:-10]]
