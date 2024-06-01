import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import KBinsDiscretizer 
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from feature_engine.discretisation import EqualWidthDiscretiser

# Load dataset
#data = pd.read_csv('houseprice.csv')
data_iris = pd.read_csv('iris.csv', sep=';')
X = data_iris.iloc[:,:-1]
y = data_iris.iloc[:,-1]


# Separação de dados
# X_train, X_test, y_train, y_test =  train_test_split(
#             data.drop(['Id', 'SalePrice'], axis=1),
#             data['SalePrice'], test_size=0.3, random_state=0)

X_train, X_test, y_train, y_test =  train_test_split(X, y, stratify=y, 
                                                     test_size=0.1, random_state=0)

#-------------------------------------------------------------------------
# por frequencia 
# transforma o dataset com o KBinsDiscretizer 
# bins default=5
#encode{‘onehot’, ‘onehot-dense’, ‘ordinal’}, default=’onehot’
#strategy{‘uniform’, ‘quantile’, ‘kmeans’}, default=’quantile’
enc = KBinsDiscretizer(n_bins=4, encode= 'ordinal',  strategy='uniform')
enc.fit(X_train)

# transform the data
train_t= enc.transform(X_train)
test_t= enc.transform(X_test)
#print(enc.binner_dict_)

#-------------------------------------------------------------------------
# por largura fixa
# set up the discretisation transformer
disc = EqualWidthDiscretiser(bins=10, variables=['sepal_width', 'sepal_length'])

# fit the transformer
disc.fit(X_train)

# transform the data
train_t= disc.transform(X_train)
test_t= disc.transform(X_test)
print(disc.binner_dict_)

#-------------------------------------------------------------------------
train_t.groupby('sepal_length')['sepal_length'].count().plot.bar()
plt.ylabel('Number of flowers')

train_t.groupby('sepal_width')['sepal_width'].count().plot.bar()
plt.ylabel('Number of flowers')

#Manutalmente
# dividindo o atributo 'sepal_length' em 10 faixas
bins = pd.qcut(data_iris['sepal_length'], 10)

# O metodo groupby faz com que valores contidos na
# coluna de um DataFrame sejam agrupados por algum criterio.
# Aqui a coluna 'sepal_length' sera agrupada
# pelas faixas definidas pelo metodo qcut acima

grupos = data_iris['sepal_length'].groupby(bins)


# obtendo a media de cada faixa
medias = grupos.mean()
print('-----------------------------------------------')
print("Medias :")
print(medias)

# Avaliando a substituição de valores pela média
# Neste caso, cada registro no bin consiste
# no intervalo que o respectivo valor de 'mean_radius'
# pertence e, assim, a funcao informada em apply
# retornara a respectiva media de cada intervalo.
novo_mean_sepal_length = bins.apply(lambda x : medias[x])
# por fim, a coluna 'sepal_length' do DataFrame original
# eh atualizada

print('-----------------------------------------------')
print('Velho sepal_length')
print(data_iris['sepal_length'])


data_iris['sepal_length'] = novo_mean_sepal_length
print('-----------------------------------------------')
print('Novo sepal_length')
print(data_iris['sepal_length'])
