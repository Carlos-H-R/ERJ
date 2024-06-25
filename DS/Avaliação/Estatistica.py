import numpy as np
import pandas as pd


def data_to_number(data: pd.DataFrame):
    if type(data) != type(0) and type(data) != type(1.0):
        return int(0)
    
    else:
        return data
    
def check_balance(colum):
    n0 = 0
    n1 = 0
    for i in colum:
        if i==0:
            n0 += 1
        elif i==1:
            n1 += 1

    if n0 == 0 or n1 == 0:
        return 0
    
    else:
        return n1/n0

# Lê a base e guarda nema variável
base = pd.read_excel(r'./Avaliação/lepto_base.xlsx', sheet_name='base_original')

# Completa os espaços vazios com zero
base_1 = base.fillna(0)
base_1 = base_1.apply(lambda x: x.map(data_to_number))
# print(base)

atributes = base.columns

for atribute in atributes:
    min = np.min(base_1[atribute])
    max = np.max(base_1[atribute])
    distribution = np.std(base_1[atribute])
    mean = np.mean(base_1[atribute])
    frequencia = base[atribute].count()
    frequencia = frequencia/1120
    balaceamento = check_balance(base[atribute])
    
    print(f"\n\n{atribute}")
    print(f"Frequencia: {frequencia}")
    print(f"Standart Deviation: {distribution}")
    print(f"Min: {min}")
    print(f"Max: {max}")
    print(f"Mean: {mean}")
    print(f"Balance: {balaceamento}")
