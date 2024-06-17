import numpy as np
import pandas as pd


def data_to_number(data: pd.DataFrame):
    if type(data) != type(0) and type(data) != type(1.0):
        return int(0)
    
    else:
        return data

# Lê a base e guarda nema variável
base = pd.read_excel(r'./Avaliação/lepto_base.xlsx', sheet_name='base_original')

# Completa os espaços vazios com zero
base = base.fillna(0)
base = base.apply(lambda x: x.map(data_to_number))
print(base)

distribution = np.std(base['T_primeiros_sintomas_atendimento_medico'])
mean = np.mean(base['T_primeiros_sintomas_atendimento_medico'])
print("Standart Deviation",distribution)
print("Mean: ", mean)

frequencia = base.count()
frequencia = frequencia.map(lambda x: x / 1120)
print("\n\n\n",frequencia)
