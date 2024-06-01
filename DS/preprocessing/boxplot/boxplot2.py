# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:09:45 2021

@author: Karla
A caixa se estende dos valores do 2 quartil e 3 quartil 
dos dados, com uma linha na mediana. 
Os bigodes estendem-se a partir da caixa para mostrar o 
intervalo dos dados. 
o bigode inferior está abaixo: Q1 - whis * (Q3-Q1), 
o bigode superior está acima:  Q3 + whis * (Q3-Q1), 
onde Q1 e Q3 são o primeiro e o terceiro quartis. 
O valor padrão de whis = 1,5 corresponde à definição 
original de boxplots de Tukey.
Os fliers, além dos bigodes, os dados são considerados
outliers e são plotados como pontos individuais.
Os pontos de fliers são aqueles além do final dos bigodes.
"""
 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets


# Load dataset
#data = pd.read_csv('houseprice.csv')
df = pd.read_csv('iris.csv', sep=';')
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
data=X

# Separação de dados
# X_train, X_test, y_train, y_test =  train_test_split(
#             data.drop(['Id', 'SalePrice'], axis=1),
#             data['SalePrice'], test_size=0.3, random_state=0)

#X_train, X_test, y_train, y_test =  train_test_split(X, y, stratify=y, 
#                                                     test_size=0.1, random_state=0)

#---------------------------


# data=np.random.randn(10, 2)
# df = pd.DataFrame(data, columns=['Col1', 'Col2'])
# df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B'])

########################
# USANDO PANDAS
########################

#boxplot dos valores
boxplot = df.boxplot()
#boxplot dos valores segundo a saída categórica
boxplot = df.boxplot(by='species')


########################
# USANDO MATPLOTLIB
########################
import numpy as np
import matplotlib.pyplot as plt

####
# mostra os outliers default
# oculta os outliers (showfliers=False)
# exibe outliers com formato de diamante vermelho

red_diamond = dict(markerfacecolor='r', marker='D')
fig1, ax1 = plt.subplots()
fig1, ax2 = plt.subplots()
fig1, ax3 = plt.subplots()
ax1.set_title(' Outlier 1')
ax2.set_title('Outlier 2')
ax3.set_title('Outlier 3')

data1= data
data2=data*2
data3=data*3


# showmeans exibe a média
ax1.boxplot(data1, flierprops=red_diamond,  showmeans=True, whis=0.90)
ax2.boxplot(data2, flierprops=red_diamond, whis=0.75)
ax3.boxplot(data3, flierprops=red_diamond, whis=3)

# Os entalhes (notch - bool) notch=True
# sem indicar os outliers showfliers=False
# enfatiza o tamanho da mediana
# inclui o intervalo de confiança (IC)
#bigodes Q1 - whis*IQR e Q3 + whis*IQR)