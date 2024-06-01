# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:11:14 2024

@author: ADM
"""
# Import the necessary libraries first
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2



# load data
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(url, names=names)

dataframe.head()

array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

# Feature extraction
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)

# Summarize scores
np.set_printoptions(precision=3)
print(fit.scores_)

features = fit.transform(X)
# Summarize selected features
print(features[0:5,:])





 #['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# [ 111.52  1411.887   17.605   53.108 2175.565  127.669    5.393  181.304]
# [[148.    0.   33.6  50. ]
#  [ 85.    0.   26.6  31. ]
#  [183.    0.   23.3  32. ]
#  [ 89.   94.   28.1  21. ]
#  [137.  168.   43.1  33. ]]



# Pode-se observar as pontuações de cada atributo e os quatro atributos escolhidos (aqueles com as pontuações mais altas):
#     plas, teste, massa e idade. Essas pontuações o ajudarão a determinar os melhores recursos para treinar seu modelo.

# P.S.: A primeira linha indica os nomes dos recursos. Para o pré-processamento do conjunto de dados, os nomes foram 
# codificados numericamente.


 
# chi-squared test with similar proportions
from scipy.stats import chi2_contingency
from scipy.stats import chi2
alpha=0.05
# defining the table
data = [[37, 24], [18, 22]]
stat, p, dof, expected = chi2_contingency(data)
print('expected=', str(expected))


# interpret test-statistic
prob = 1-alpha
critical = chi2.ppf(prob, dof)
print("critical value is " + str(critical))
print('chi-square= ',str(stat))

if abs(stat) >= critical:
 print('Dependent (reject H0)')
else:
 print('Independent (fail to reject H0)')


print("p value is " + str(p))
# interpret p-value
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (H0 holds true)')
















