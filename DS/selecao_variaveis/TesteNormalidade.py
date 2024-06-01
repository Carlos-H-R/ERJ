# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:35:05 2024

@author: ADM
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:02:34 2020

@author: Karla
"""

import numpy as np
import warnings
warnings.filterwarnings("ignore")
#import statsmodels.formula.api as sm
from scipy import stats



np.random.seed(123)

# # breast_cancer iris data 
# data = load_breast_cancer()

# # Create features and target 
# X = data.data 
# y = data.target 

# iris = load_iris()
# df = pd.DataFrame(iris.data, columns=iris.feature_names)


amostra1 = [85, 90, 70, 95, 91]
amostra2 = [86, 96, 80, 65, 70, 80, 70, 90, 75]


stat_normal, p_normal = stats.shapiro(amostra1)

# Imprimindo os resultados
print("Estatística de teste:", stat_normal)
print("Valor p:", p_normal)
if p_normal > 0.05:
    print("amostra1 parecem ser normalmente distribuídos.")
    print()
else:
    print("amostra1 não parecem ser normalmente distribuídos.")
    print()
    
stat_normal, p_normal = stats.shapiro(amostra2)

# Imprimindo os resultados
print("Estatística de teste:", stat_normal)
print("Valor p:", p_normal)
if p_normal > 0.05:
    print("amostra2 parecem ser normalmente distribuídos.")
    print()
else:
    print("amostra2 não parecem ser normalmente distribuídos.")
    print()


stat_normal, p_normal = stats.jarque_bera(amostra1)

# Imprimindo os resultados
print("Estatística de teste:", stat_normal)
print("Valor p:", p_normal)
if p_normal > 0.05:
    print("amostra1 parecem ser normalmente distribuídos.")
    print()
else:
    print("amostra1 não parecem ser normalmente distribuídos.")
    print()
    
    
stat_normal, p_normal = stats.jarque_bera(amostra2)

# Imprimindo os resultados
print("Estatística de teste:", stat_normal)
print("Valor p:", p_normal)
if p_normal > 0.05:
    print("amostra2 parecem ser normalmente distribuídos.")
    print()
else:
    print("amostra2 não parecem ser normalmente distribuídos.")
    print()
    
