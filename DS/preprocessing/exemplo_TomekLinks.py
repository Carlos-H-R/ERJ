# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:04:44 2024

@author: ADM
"""

from collections import Counter
from sklearn.datasets import make_classification
from imblearn.under_sampling import TomekLinks
from imblearn.under_sampling import RandomUnderSampler
 
X, y = make_classification(n_classes=2, class_sep=2,
                           weights=[0.1, 0.9], n_informative=4, n_redundant=1, flip_y=0,
n_features=20, n_clusters_per_class=1, n_samples=1000, random_state=10)

print('Original dataset shape %s' % Counter(y))
tl = TomekLinks()

X_res, y_res = tl.fit_resample(X, y)
print('Resampled dataset shape %s' % Counter(y_res))



from sklearn.datasets import load_iris
from imblearn.datasets import make_imbalance
import matplotlib.pyplot as plt

iris = load_iris(as_frame=True)

sampling_strategy = {0: 10, 1: 20, 2: 47}
X, y = make_imbalance(iris.data, iris.target, sampling_strategy=sampling_strategy)


fig, axs = plt.subplots(ncols=3, figsize=(10, 5))
autopct = "%.2f"
iris.target.value_counts().plot.pie(autopct=autopct, ax=axs[0])
axs[0].set_title("Original")
y.value_counts().plot.pie(autopct=autopct, ax=axs[1])
axs[1].set_title("Imbalanced")
fig.tight_layout()

# select only 2 classes since the ratio make sense in this case
binary_mask = y.isin([0, 1])
binary_y = y[binary_mask]
binary_X = X[binary_mask]

 #sampling_strategy pode receber um valor flutuante. Para métodos de subamostragem, 
 # ele corresponde à proporção alfa definida por Nm= alfa x N, em que Nm e N são 
 # o número de amostras na classe majoritária após a reamostragem e o número de amostras na classe minoritária, 
 # respectivamente.
 

sampling_strategy = 0.8
rus = RandomUnderSampler(sampling_strategy=sampling_strategy)
X_res, y_res = rus.fit_resample(binary_X, binary_y)
ax = y_res.value_counts().plot.pie(autopct=autopct)
_ = ax.set_title("Under-sampling")

# Com o método de limpeza, o número de amostras em cada classe não será igualado, mesmo que seja direcionado.


sampling_strategy = "not minority"
tl = TomekLinks(sampling_strategy=sampling_strategy)
X_res, y_res = tl.fit_resample(X, y)
ax = y_res.value_counts().plot.pie(autopct=autopct)
_ = ax.set_title("Cleaning")