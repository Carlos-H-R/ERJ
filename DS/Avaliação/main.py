import numpy as np
import pandas as pd
import modelos.decition_tree as dt

from functools import partial


def check_outlier(data, deviation, mean):
    inf = mean - 2*deviation
    sup = mean + 2*deviation
    if inf < data < sup:
        return data
    
    else:
        return pd.NA

def outlier(base: pd.DataFrame):
    for index in ['T_primeiros_sintomas_atendimento_medico', 'T_primeiros_sintomas_coleta_amostra_ELISA', 'T_atendimento_medico_internação_hospitalar']:
        deviation = np.std(base[index])
        mean = np.mean(base[index])
        base[index].apply(partial(check_outlier, deviation, mean))

    
def data_to_number(data: pd.DataFrame):
    if type(data) != type(0) and type(data) != type(1.0):
        return int(0)
    
    else:
        return data

# Lê a base e armazena em uma variável
base = pd.read_excel(r'./Avaliação/lepto_base.xlsx', sheet_name='base_original')


# Seleciona a parte da base para treinamento
x_train = base.iloc[:952,:-1]
y_train = base.iloc[:952,-1]

# Seleciona a parte da base para teste
x_test = base.iloc[952:,:-1]
y_test = base.iloc[952:,-1]

# Preeche os missing values com valor padrão
x_train.fillna(0)
x_train = x_train.apply(lambda x: x.map(data_to_number))


# Remove os outliers da base de treino para o atributo em questão
outlier(x_train)

# Preeche os missing values com valor padrão
x_train.fillna(0)
x_train = x_train.apply(lambda x: x.map(data_to_number))

# cria um dataset e inicia o modelo
data_sets = [(x_train, y_train),(x_test, y_test)]
dt.decision_tree(data_sets)
