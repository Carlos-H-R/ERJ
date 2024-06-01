# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:36:14 2020

@author: Karla
"""
import pandas as pd
import numpy as np
#from skfeature.utility.mutual_information import su_calculation
from sklearn.metrics import mutual_info_score
from sklearn.datasets import load_iris

def merit_calculation(X, y):
    """
    This function calculates the merit of X given class labels y, where
    merits = (k * rcf)/sqrt(k+k*(k-1)*rff)
    rcf = (1/k)*sum(su(fi,y)) for all fi in X
    rff = (1/(k*(k-1)))*sum(su(fi,fj)) for all fi and fj in X
    Input
    ----------
    X: {numpy array}, shape (n_samples, n_features)
        input data
    y: {numpy array}, shape (n_samples,)
        input class labels
    Output
    ----------
    merits: {float}
        merit of a feature subset X
    """

    n_samples, n_features = X.shape
    rff = 0
    rcf = 0
    for i in range(n_features):
        fi = X[:, i]
        rcf += mutual_info_score(fi, y)
        for j in range(n_features):
            if j > i:
                fj = X[:, j]
                rff += mutual_info_score(fi, fj)
    rff *= 2
    merits = rcf / np.sqrt(n_features + rff)
    return merits


def cfs(X, y):
    """
    This function uses a correlation based heuristic to evaluate the worth of 
    features which is called CFS
    Input
    -----
    X: {numpy array}, shape (n_samples, n_features)
        input data
    y: {numpy array}, shape (n_samples,)
        input class labels
    Output
    ------
    F: {numpy array}
        index of selected features
    Reference
    ---------
    Zhao, Zheng et al. "Advancing Feature Selection Research - ASU Feature Selection Repository" 2010.
    """

    n_samples, n_features = X.shape
    F = []
    # M stores the merit values
    M = []
    while True:
        merit = -100000000000
        idx = -1
        for i in range(n_features):
            if i not in F:
                F.append(i)
                print(F)
                # calculate the merit of current selected features
                t = merit_calculation(X[:, F], y)
                if t > merit:
                    merit = t
                    idx = i
                F.pop()
        F.append(idx)
        M.append(merit)
        
        #número de atributos que se deseja incluir na busca
        if len(M) > 5:
            if M[len(M)-1] <= M[len(M)-2]:
                if M[len(M)-2] <= M[len(M)-3]:
                    if M[len(M)-3] <= M[len(M)-4]:
                        if M[len(M)-4] <= M[len(M)-5]:
                            # acrescentar mais atributos na busca
                            # alem dos 6 primeiros
                            #if M[len(M)-5] <= M[len(M)-6]:
                            break
    return np.array(F)


df = pd.read_csv("iris.csv", sep=';') 
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values

# X, y = dataset.data, dataset.target
# features = dataset.feature_names

n_samples, n_features = X.shape
merits=(cfs(X,y))
print("Atributos mais relevantes: ")
print(merits)