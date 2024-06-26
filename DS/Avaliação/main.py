import numpy as np
import pandas as pd
import modelos.decision_tree as dt
# import modelos.estatistica as est

from sklearn.impute import KNNImputer
# from sklearn.preprocessing import MinMaxScaler

from ReliefF import ReliefF
from functools import partial


def check_outlier(data, deviation, mean):
    inf = mean - 2*deviation
    sup = mean + 2*deviation
    if data < sup:
        return data
    
    else:
        return np.nan

def outlier(base: pd.DataFrame):
    for index in ['T_primeiros_sintomas_atendimento_medico', 'T_primeiros_sintomas_coleta_amostra_ELISA', 'T_atendimento_medico_internação_hospitalar']:
        deviation = np.std(base[index])
        mean = np.mean(base[index])
        base[index].apply(partial(check_outlier, deviation, mean))
    
def data_clear(data: pd.DataFrame):
    if data == '' or data == ' ':
        return np.nan
    
    else:
        return data
    

# Lê a base e armazena em uma variável
base = pd.read_excel(r'base/lepto_base.xlsx', sheet_name='base_original')


# Seleciona a parte da base para treinamento
x_train = base.iloc[:952,:-1]
y_train = base.iloc[:952,-1]

# Seleciona a parte da base para teste
x_test = base.iloc[952:,:-1]
y_test = base.iloc[952:,-1]


# Criando um imputer para preencher os missing values usando KNN
x_train = x_train.apply(lambda x: x.map(data_clear))

imputer = KNNImputer(n_neighbors=2, weights='uniform')
filled_up = imputer.fit_transform(x_train)
x_train = pd.DataFrame(filled_up, columns=x_train.columns)


# Remove os outliers da base de treino para o atributo em questão
outlier(x_train)


# Preeche os missing values com valor padrão
filled_up = imputer.fit_transform(x_train)
x_train = pd.DataFrame(filled_up, columns=x_train.columns)


# # Normalizando 
# scaler = MinMaxScaler()
# to_normalize = [x_train['T_primeiros_sintomas_atendimento_medico'], x_train['T_primeiros_sintomas_coleta_amostra_ELISA'], x_train['T_atendimento_medico_internação_hospitalar']]
# normalized = scaler.fit_transform(to_normalize)
# x_train['T_primeiros_sintomas_atendimento_medico'] = normalized[0]
# x_train['T_primeiros_sintomas_coleta_amostra_ELISA'] = normalized[1]
# x_train['T_atendimento_medico_internação_hospitalar'] = normalized[2]


# # Seleção de Variáveis
# relief = ReliefF(n_neighbors=2, n_features_to_keep=2)
# relief.fit(x_train,y_train)

# x_train_reduced = relief.transform(x_train)
# x_test_reduced  = relief.transform(y_train)

# # x_train = pd.DataFrame(x_train_reduced, columns=[x_train.)
# # x_test  = pd.DataFrame(x_test_reduced)


# cria um dataset e inicia o modelo
data_sets = [(x_train, y_train),(x_test, y_test)]
dt.decision_tree(data_sets)
