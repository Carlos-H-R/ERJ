import numpy as np
import pandas as pd
import modelos.decision_tree as dt
# import modelos.estatistica as est

from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import MinMaxScaler

from skrebate import ReliefF
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
    
def fill_blank(data: pd.DataFrame):
    # imputer = KNNImputer(n_neighbors=10, weights='uniform')
    # filled_up = imputer.fit_transform(data)
    # data['T_primeiros_sintomas_atendimento_medico'] = filled_up[0]
    # data['T_primeiros_sintomas_coleta_amostra_ELISA'] = filled_up[1]
    # data['T_atendimento_medico_internação_hospitalar'] = filled_up[2]

    imputer = KNNImputer(n_neighbors=1, weights='uniform')
    filled_up = imputer.fit_transform(data)
    data = pd.DataFrame(data=filled_up, columns=data.columns)

    return data



# Lê a base e armazena em uma variável
base = pd.read_excel(r'base/lepto_base.xlsx', sheet_name='base_original')
data = base.iloc[:,:-1]
target = base.iloc[:,-1]

# # Seleciona a parte da base para treinamento
# x_train = base.iloc[:952,:-1]
# y_train = base.iloc[:952,-1]

# # Seleciona a parte da base para teste
# x_test = base.iloc[952:,:-1]
# y_test = base.iloc[952:,-1]

x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.15, random_state=64, stratify=target)


# Criando um imputer para preencher os missing values usando KNN
x_train = x_train.apply(lambda x: x.map(data_clear))
x_train = fill_blank(x_train)



# Remove os outliers da base de treino para o atributo em questão
outlier(x_train)


# Preeche os missing values com valor padrão
x_train = fill_blank(x_train)

file = open(file='coisa.csv', mode='+w')
file.write(x_train.to_csv())
file.close()

# # Normalizando 
# scaler = MinMaxScaler()
# to_normalize = [x_train['T_primeiros_sintomas_atendimento_medico'], x_train['T_primeiros_sintomas_coleta_amostra_ELISA'], x_train['T_atendimento_medico_internação_hospitalar']]
# normalized = scaler.fit_transform(to_normalize)
# x_train['T_primeiros_sintomas_atendimento_medico'] = normalized[0]
# x_train['T_primeiros_sintomas_coleta_amostra_ELISA'] = normalized[1]
# x_train['T_atendimento_medico_internação_hospitalar'] = normalized[2]


# Seleção de Variáveis
features = x_train.columns.tolist()
x_train1 = x_train.to_numpy()
y_train1 = y_train.to_numpy()

relief = ReliefF(n_features_to_select=12, n_neighbors=30)
relief.fit(x_train1,y_train1)

number_of_features = 10
top_features = relief.top_features_
reduced_features = top_features[number_of_features:]

for i in reduced_features:
    x_train.drop(columns=features[i], inplace=True)
    x_test.drop(columns=features[i], inplace=True)


# cria um dataset e inicia o modelo
data_sets = [(x_train, y_train),(x_test, y_test)]
dt.decision_tree(data_sets)
