# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:11:37 2023

@author: ADM
"""

# importar pacotes e setar configurações de plots
import pandas as pd
import numpy as np #numpy==1.23
import matplotlib.pyplot as plt
import seaborn as sns
# statsmodels-0.13.2  
from statsmodels.tsa.stattools import adfuller # importar o teste ADF
from statsmodels.tsa.seasonal import seasonal_decompose

#importar pacotes e setar configurações de plots
sns.set_style()


# url do dataset
dataset = "Electric_Production.csv"

#importar o csv para o dataframe
df = pd.read_csv(dataset)

#ver as 5 primeiras entradas
df.head(5)

#Converter DATE para datetime e associar ao index do dateframe
df.index = pd.to_datetime(df.DATE, format="%m-%d-%Y")

#eliminar a coluna DATE, pois ela já seria o indice
df.drop("DATE", inplace=True, axis=1)

#ver dos dados
df.head()

#Plotar o gráfico
plt.plot(df.index, df.Value);


# extrair apenas os valores
X = df.Value.values

#Salvar a decoposição em result

result = seasonal_decompose(df,  model='multiplicative')
#result = seasonal_decompose(df,  model='additive')

#Plotar em tamanho maior
fig, (ax1,ax2,ax3, ax4 ) = plt.subplots(4,1, figsize=(12,5))
result.observed.plot(ax=ax1)
ax1.set_ylabel('original')

result.trend.plot(ax=ax2)
ax2.set_ylabel('tendência')
result.seasonal.plot(ax=ax3)
ax3.set_ylabel('sazonalidade')
result.resid.plot(ax=ax4)
ax4.set_ylabel('residuo')


# aplicar ADF e imprimir o resultado
result = adfuller(X)
print('Dickey-Fuller Aumentado')
print('Teste Estatístico: {:.4f}'.format(result[0]))
print('Valor-p: {:.4f}'.format(result[1]))
for key, value in result[4].items():
    print('\t{}: {:.4f}'.format(key, value))
    if(value<result[0]):
        print('Falha de teste estatístico')
        
if (result[1]>0.05):
    print("---Série não estacionária---")
else:
    print("---Série estacionária---")
    
ma = df.rolling(12).mean()

fig, ax = plt.subplots()
df.plot(ax=ax, legend=False)
ma.plot(ax=ax, legend=False, color='r')
ax.set_ylabel('série  + média móvel 12')
plt.tight_layout()
    
#Removendo Tendência 1    
print()
print('=== Primeira Avaliação ===')
df['dz1'] = (df.Value - df.Value.shift(1))


fig, ax = plt.subplots()
df.dz1.plot(ax=ax, legend=False)
ax.set_ylabel('1ª diferenciação')
plt.tight_layout()


result = adfuller(df.dz1.dropna())
print('Dickey-Fuller Aumentado 1ª diferenciação')
print('Teste Estatístico: {:.4f}'.format(result[0]))
print('Valor-p: {:.4f}'.format(result[1]))
for key, value in result[4].items():
    print('\t{}: {:.4f}'.format(key, value))
    if(value<result[0]):
        print('Falha de teste estatístico')
        
if (result[1]>0.05):
    print("---Série não estacionária---")
else:
    print("---Série estacionária---")

# #aplicar diferenciação na serie original
# X_diff = X.diff(1).dropna()
# ma_X_diff = X_diff.rolling(12).mean()
# #desvio padrão
# std_X_diff = X_diff.rolling(12).std()

# #plotar a diferenciação
# fig, ax = plt.subplots()
# X_diff.plot(ax=ax, legend=False)
# ma_X_diff.plot(ax=ax, legend=False, color='r')
# std_X_diff.plot(ax=ax, legend=False, color='g')
# ax.set_ylabel('diferencia 2 + media movel(red) + std (green)')
# plt.tight_layout()

    
    
#Caso fosso necesário uma segunda diferenciação
df['dz2'] =  df.Value - 2*df.Value.shift(1) + df.Value.shift(2)

fig, ax = plt.subplots()
df.dz2.plot(ax=ax, legend=False)
ax.set_ylabel('2ª diferenciação')
plt.tight_layout()


result = adfuller(df.dz2.dropna())
print('Dickey-Fuller Aumentado 2ª diferenciação')
print('Teste Estatístico: {:.4f}'.format(result[0]))
print('Valor-p: {:.4f}'.format(result[1]))
for key, value in result[4].items():
    print('\t{}: {:.4f}'.format(key, value))
    if(value<result[0]):
        print('Falha de teste estatístico')
        
if (result[1]>0.05):
    print("---Série não estacionária---")
else:
    print("---Série estacionária---")


#Removendo Tendência 2 e sazonalidade
print()
print('=== Segunda Avaliação ===')
# log e media móvel
df_log = np.log(df.Value)
ma_log = df_log.rolling(12).mean()

fig, ax = plt.subplots()
df_log.plot(ax=ax, legend=False)
ma_log.plot(ax=ax, legend=False, color='r')
ax.set_ylabel('log + media')
plt.tight_layout()



#subtrair média do log dos dados, iremos fazer a média em 12, pois iremos fazer anualmente
df_sub = (df_log - ma_log).dropna()
ma_sub = df_sub.rolling(12).mean()
#desvio padrão
std_sub = df_sub.rolling(12).std()

fig, ax = plt.subplots()
df_sub.plot(ax=ax, legend=False)
ma_sub.plot(ax=ax, legend=False, color='r')
std_sub.plot(ax=ax, legend=False, color='g')
ax.set_ylabel('log-media + media movel(red) + std (green)')
plt.tight_layout()


#repetir o ADF
#X_sub = df_sub.Value

# aplicar ADF e imprimir o resultado
result_sub = adfuller(df_sub)
print('Dickey-Fuller Aumentado Serie + log - media')
print('Teste Estatístico: {:.4f}'.format(result_sub[0]))
print('Valor-p: {:.10f}'.format(result_sub[1]))
print('Valores Críticos:')
for key, value in result_sub[4].items():
	print('\t{}: {:.4f}'.format(key, value))
    

#Diferenciação 

#aplicar diferenciação
df_diff = df_sub.diff(1).dropna()
ma_diff = df_diff.rolling(12).mean()
#desvio padrão
std_diff = df_diff.rolling(12).std()

#plotar a diferenciação
fig, ax = plt.subplots()
df_diff.plot(ax=ax, legend=False)
ma_diff.plot(ax=ax, legend=False, color='r')
std_diff.plot(ax=ax, legend=False, color='g')
ax.set_ylabel('diferencia(log-media) + media movel(red) + std (green)')

plt.tight_layout()

#extrair apenas os valores e retirar os valores NA
#X = df_diff.Value.dropna()

# aplicar ADF e imprimir o resultado
result_diff = adfuller(df_diff)
print('Dickey-Fuller Aumentado diferenciacao na serie+log-media')
print('Teste Estatístico: {:.4f}'.format(result_diff[0]))
print('Valor-p: {:.10f}'.format(result_diff[1]))
print('Valores Críticos:')
for key, value in result_sub[4].items():
	print('\t{}: {:.4f}'.format(key, value))    
    
    