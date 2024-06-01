# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 15:46:12 2021

@author: Karla
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import NeighborhoodComponentsAnalysis as nca
from sklearn.pipeline import Pipeline as pipe

#Data import
#df_base = pd.read_csv('./oakland-street-trees.csv')

df_base = pd.read_csv('iris_v2.csv',sep=';')
columns_iris = ['sepal_length','sepal_width','petal_length','petal_width']


print(df_base.info())

print('Estatística básica dos atributos:')
print(df_base.describe())
print('--------------------------------------------------------------')
print('Número de  atrbutos', df_base.shape[1])
print('--------------------------------------------------------------')


#Numeros de NaN da base
for i in range(df_base.shape[1]):    
    diff=len(df_base) - df_base[df_base.columns[i]].count()
    print('Numeros de NaN da base ',df_base.columns[i],':', diff)
    print(f" Percenual de faltantes {diff/df_base.shape[0]:.2%}")
    
    
print('--------------------------------------------------------------')

NA_val = df_base.isna().sum()

#descartar linhas se houver algum valor NaN:
#df_lih=df_base.dropna(axis = 0)

#descartar colunas se houver algum valor NaN:
#df_cl=df_base.dropna(axis = 1)

#descartar colunas se houver quantidade menor do que x% de 
# valor preenchido:
df_base_v2= df_base.dropna(thresh=len(df_base)*0.90, axis=1)


#Confirmando o numero de dados removidos
print('Numero de atributos removidos:')
print(df_base.shape[1]-df_base_v2.shape[1])


#Um caso de uso muito comum para isso é preencher dados faltantes:
# com 0 para todos os NaN no próprio dataframe (inplace)
#df_base_v2['petal_length'].fillna(0, inplace=True)

#com a média ou a mediana das colunas correspondentes:
#df_base_v2['petal_length'].fillna(df_base_v2['petal_length'].mean(),inplace=True)
#df_base_v2['petal_length'].fillna(df_base_v2['petal_length'].median(),inplace=True)

# preencher com a média dos valores diferentes de nan para o mesmo rótulo
soma=df_base_v2.query("species == 'setosa' and petal_length != 'nan' ")['petal_length'].sum()                    
total=df_base_v2.query("species == 'setosa' and petal_length != 'nan' ")['petal_length'].count()                    
media=soma/total
df_base_v2['petal_length'].fillna(media,inplace=True)


for i in range(df_base_v2.shape[1]):    
    diff=len(df_base_v2) - df_base_v2[df_base_v2.columns[i]].count()
    print('2º Avaliacao de Numeros de NaN da base ',df_base_v2.columns[i],':', diff)
    print(f" Percenual de faltantes {diff/df_base_v2.shape[0]:.2%}")
    


    