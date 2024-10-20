# -*- coding: utf-8 -*-
"""
Created on 

https://pypi.org/project/ReliefF/#files
pip install ReliefF
"""


from ReliefF import ReliefF
import numpy as np
from sklearn import datasets
import pandas as pd
from sklearn import preprocessing


#example of multi class problem
iris = datasets.load_iris()
X = iris.data
y = iris.target
# define the number of selected feature 
rows,feature= iris.data.shape
fs = ReliefF(n_neighbors=1, n_features_to_keep=2)

print("IRIS")
print(iris.data)

X_select = fs.fit_transform(X, y)
print("(No. of tuples, No. of Columns before ReliefF) : "+str(iris.data.shape)+
      "\n(No. of tuples, No. of Columns after ReliefF) : "+str(X_select.shape))
print()

# print("HEART")
# heart = pd.read_csv('heart_disease.csv', sep=';')
# X = heart.iloc[:,:-1]
# y = heart.iloc[:,-1]
# target=pd.Series(y)

# # missing pode ser tratado previamente
# enc = preprocessing.OrdinalEncoder(encoded_missing_value=-1)
# X=enc.fit_transform(X)
 
# fs = ReliefF(n_neighbors=20, n_features_to_keep=2)
# X_train = fs.fit_transform(X, y)
# print("(No. of tuples, No. of Columns before ReliefF) : "+str(heart.shape)+
#       "\n(No. of tuples, No. of Columns after ReliefF) : "+str(X_train.shape))













