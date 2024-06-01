# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 20:04:20 2023

@author: ADM
"""

import numpy as np
from sklearn.impute import KNNImputer

#https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html

X = [[-1,0,8],[9,6,8], [2,4,5], [3,6,np.nan],[0, 2, np.nan], [3, 4, 3], [np.nan, 6, 5], [8, 8, 7], [1,4,4]]
print('---------------------------------------------------')
imputer = KNNImputer(n_neighbors=1, missing_values=np.nan)
X=imputer.fit_transform(X)
print(X)