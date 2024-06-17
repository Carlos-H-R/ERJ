import numpy as np
import pandas as pd
import DT_hiperparametros as DTh


def outlier(data):
    if data == ' ' or data > 51:
        return ' '
    
    else:
        return data
    
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


# Remove os outliers da base de treino para o atributo em questão
x_train['T_primeiros_sintomas_atendimento_medico'] = x_train['T_primeiros_sintomas_atendimento_medico'].map(outlier)

# Preeche os missing values com valor padrão
x_train.fillna(0)
y_train.fillna(0)
x_train = x_train.apply(lambda x: x.map(data_to_number))
x_test = x_test.apply(lambda x: x.map(data_to_number))


# cria um dataset e inicia o modelo
data_sets = [(x_train, y_train),(x_test, y_test)]
DTh.modelosDT(data_sets, name='Modelo_Original')
