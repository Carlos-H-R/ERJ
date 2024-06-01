# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:39:09 2023

@author: karla
"""
import numpy as np 
import matplotlib.pyplot as plt 
import statistics 
from sklearn import datasets

# import some data to play with
iris = datasets.load_iris()


X = iris.data[:, :1]  # primeiro atributo
y = iris.target


# lista para armazenar outliers
outliers = [] 

# desvio padrão 

desv_pad_iris=statistics.stdev(X[:, 0]) 

# média dos seus dados 
media_iris=statistics.mean(X[:, 0]) 

# coloca o limite que determina se é outlier 
limite = desv_pad_iris * 2 # 3 é parâmetro
limite_inferior = media_iris - limite 
limite_superior = media_iris + limite 

# Localiza outliers e anexa à nossa lista 
for outlier in X: 
    if outlier > limite_superior or outlier < limite_inferior: 
        outliers.append(outlier) 
        
# exibe a lista com os 
print("lista outliers=", outliers) 
# conta quantos elementos são 
print("quantidade de outlier = ", len(outliers)) 
# percentual da coluna que é 
print("percentual de outlier: ",(len(outliers)/len(X[:, 0]))*100)
