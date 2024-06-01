from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

from sklearn.datasets import load_iris
import pandas as pd



# load data
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# dataframe = pd.read_csv(url, names=names)


pima = pd.read_csv('pima.csv',sep=';')
X= pima.iloc[:,0:8]
y= pima.iloc[:,8]
#iris = load_iris()


lda = LDA()
lda.fit(X, y)
importance = lda.coef_
print(importance)


lda2 = LDA(n_components=1)
X_train = lda2.fit_transform(X, y)
importance = lda2.coef_
print(importance)


importance_ranked = sorted(range(len(importance)), key=lambda k: importance[k], reverse=True)
print(importance_ranked)
