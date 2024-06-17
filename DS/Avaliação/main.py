import numpy as np
import pandas as pd
import DT_hiperparametros as DTh

base = pd.read_excel(r'./Avaliação/lepto_base.xlsx', sheet_name='base_original')

# preenche todos os espaços vazios com 0
base = base.replace(' ',0)

distribution = np.std(base['T_primeiros_sintomas_atendimento_medico'])
mean = np.mean(base['T_primeiros_sintomas_atendimento_medico'])
print("Standart Deviation",distribution)
print("Mean: ", mean)

# # seleciona a parte da base para treinamento
# x_train = base.iloc[:952,:-1]
# y_train = base.iloc[:952,-1]

# # seleciona a parte da base para teste
# x_test = base.iloc[952:,:-1]
# y_test = base.iloc[952:,-1]

# # cria um dataset e inicia o modelo
# data_sets = [(x_train, y_train),(x_test, y_test)]
# DTh.modelosDT(data_sets, name='Modelo_Original')
