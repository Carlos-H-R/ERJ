import numpy as np
import pandas as pd
import modelos.decision_tree as dt

from sklearn.impute import KNNImputer

from functools import partial


def check_outlier(data, deviation, mean):
    inf = mean - 2*deviation
    sup = mean + 2*deviation
    if data < sup:
        return data
    
    else:
        return pd.NA

def outlier(base: pd.DataFrame):
    for index in ['T_primeiros_sintomas_atendimento_medico', 'T_primeiros_sintomas_coleta_amostra_ELISA', 'T_atendimento_medico_internação_hospitalar']:
        deviation = np.std(base[index])
        mean = np.mean(base[index])
        base[index].apply(partial(check_outlier, deviation, mean))

    
def data_clear(data: pd.DataFrame):
    if (type(data) != type(int) and type(data) != type(float)) or data == 666:
        return np.nan
    
    else:
        return data
    

def data_to_number(data: pd.DataFrame):
    if type(data) != type(int) and type(data) != type(float):
        return 666
    
    else:
        return data

# Lê a base e armazena em uma variável
base = pd.read_excel(r'./base/lepto_base.xlsx', sheet_name='base_original')


# Seleciona a parte da base para treinamento
x_train = base.iloc[:952,:-1]
y_train = base.iloc[:952,-1]

# Seleciona a parte da base para teste
x_test = base.iloc[952:,:-1]
y_test = base.iloc[952:,-1]

# Preeche os missing values com valor padrão
x_train.fillna(666)
x_train = x_train.apply(lambda x: x.map(data_to_number))

# Remove os outliers da base de treino para o atributo em questão
outlier(x_train)

# # Preeche os missing values com valor padrão
# x_train.fillna(0)
# x_train = x_train.apply(lambda x: x.map(data_to_number))

x_train = x_train.apply(lambda x: x.map(data_clear))
imputer = KNNImputer(n_neighbors=2, weights='uniform')
for i in atributes

x_train = pd.DataFrame(imputer.fit_transform(x_train))

# cria um dataset e inicia o modelo
data_sets = [(x_train, y_train),(x_test, y_test)]
print(data_sets)
# dt.decision_tree(data_sets)
