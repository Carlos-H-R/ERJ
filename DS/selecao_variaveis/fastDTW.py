 
"""
Created on Mon Mar 19 10:19:50 2018
@author: Karla
"""

# https://pypi.org/project/fastdtw/
#download fastdtw and install with: pip install fastdtw

import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from sklearn import datasets


# indicate path and file name excel - data in first datasheet
planilha_1=pd.read_excel(r'pre_processados.xlsx', sheet_name='pre_processados')

#outro teste
# iris = datasets.load_iris()
# X = iris.data
# y = X[:,3] # apenas como exemplo de um vetor númerico


# transforming spreadsheets into arrays
matriz=planilha_1.values
print("Matriz dos parametros de entrada")
print(matriz)

#verifica para cada atributo de entrada o DTW em relação a saida (última coluna)
entradas=matriz[:,0:(len(matriz[0])-1)]
y=matriz[:,(len(matriz[0]))-1]
X=entradas






for i in range(0,len(X[0])):
    x=X[:,i]
    distance, path = fastdtw(x, y)
    print("Distance ", distance)
    
       







