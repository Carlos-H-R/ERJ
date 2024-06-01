# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:02:34 2020

@author: Karla
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
#import statsmodels.formula.api as sm
import statsmodels.api as sm
from scipy import stats
from sklearn.datasets import load_breast_cancer
from scipy.stats import t

def backwardElimination(x, Y, sl, columns):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(Y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
                    columns = np.delete(columns, j)
                    
    regressor_OLS.summary()
    return x, columns


np.random.seed(123)

# # breast_cancer iris data 
# data = load_breast_cancer()

# # Create features and target 
# X = data.data 
# y = data.target 

# iris = load_iris()
# df = pd.DataFrame(iris.data, columns=iris.feature_names)


data = pd.read_csv('data.csv')

data = data.iloc[:,1:]
# yy=data.iloc[:,-1]
label_encoder = LabelEncoder()
data.iloc[:,-1] = label_encoder.fit_transform(data.iloc[:,-1]).astype('float64')
# yd=data.iloc[:,-1]
# correlation
corr = data.corr()
sns.heatmap(corr)


#---------------------------------------
# a correlation higher than 0.9
columns = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] >= 0.9:
            if columns[j]:
                columns[j] = False
selected_columns = data.columns[columns]
data = data[selected_columns]
# ---------------------------------------

# Nível de significância (geralmente 0.05 para um teste bilateral)
alpha = 0.05

# Graus de liberdade (número de observações menos 1)
num_registros = data.shape[0]
#print("Número de registros:", num_registros)
df = num_registros - 1


# Valor crítico (t crítico)
t_critico = t.ppf(1 - alpha / 2, df)

print("Valor crítico (t crítico):", t_critico)


for i in data.columns:
    print('atributo:', i)
    t2, p2 = stats.ttest_ind(data[i],data.iloc[:,-1], equal_var=False) 
    print("The t-statistic= " + str(t2)) 

    if t_critico<t2:
        print('rejeita-se a hipotese nula')
        print("The t-statistic= " + str(t2)) 
        print("p-value = " + str(p2))
        print()
    else:
        print('NÃO é possivel rejeitar a hipótese nula')
        print("The t-statistic= " + str(t2)) 
        print("p-value = " + str(p2))
        print()




selected_columns = selected_columns[1:].values
#dataset has only those columns with correlation less than 0.9
SL = 0.05
data_modeled, selected_columns = backwardElimination(data.iloc[:,1:].values, data.iloc[:,0].values, SL, selected_columns)
result = pd.DataFrame()
result['diagnosis'] = data.iloc[:,-1]
data = pd.DataFrame(data = data_modeled, columns = selected_columns)




# Comparação com valor crítico: O valor t é então comparado com um valor crítico de t da distribuição t com os 
# graus de liberdade apropriados e o nível de significância escolhido (geralmente 0,05). 

# Se o valor t calculado for maior que o valor crítico, podemos rejeitar a hipótese nula de que não há diferença significativa 
# entre as médias.
# Quanto maior o valor absoluto do t-statistic, maior a evidência de uma diferença significativa entre as médias das amostras.

# Interpretação do p-valor: 
# Além de comparar o valor t com o valor crítico, também podemos calcular o p-valor associado 
# ao valor t.
# Um p-valor menor que o nível de significância escolhido (geralmente 0,05) indica que há evidências 
# estatisticamente significativas para rejeitar a hipótese nula.

# Direção da diferença: 
#     Além de testar se há uma diferença significativa entre as médias, também podemos determinar 
# a direção dessa diferença com base no sinal do valor t. 

# Se o valor t for positivo, indica que a média da primeira 
# amostra é maior que a média da segunda amostra; 
# se for negativo, indica o oposto.

# Em resumo, o t-statistic é uma medida usada para avaliar a significância estatística das diferenças entre as médias 
# de duas amostras, levando em consideração a variabilidade dentro das amostras. 




fig = plt.figure(figsize = (20, 25))
j = 0
for i in data.columns:
    plt.subplot(6, 4, j+1)
    j += 1
    sns.distplot(data[i][result['diagnosis']==0], color='g', label = 'benign')
    sns.distplot(data[i][result['diagnosis']==1], color='r', label = 'malignant')
    plt.legend(loc='best')
fig.suptitle('Breast Cance Data Analysis')
fig.tight_layout()
fig.subplots_adjust(top=0.95)
plt.show()