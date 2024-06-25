import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


def decision_tree(data_set):
    depth={"criterion":['gini', 'entropy'],
           "max_depth":[3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
           "min_samples_split":[2, 4, 6, 8, 10, 12, 14, 16],
           "min_samples_leaf":[2, 4, 6, 8, 10, 12, 14, 16],
           "max_features":[5,10] #If None, then max_features=n_features.
           }   

    x_train, y_train = data_set[0]
    x_test, y_test = data_set[1]

    DTC = DecisionTreeClassifier(class_weight='balanced', random_state=6)

    DTC_grid = GridSearchCV(estimator=DTC, param_grid=depth, cv=6, scoring='f1')
    DTC = DTC_grid.fit(x_train,y_train)

    y_pred = DTC.predict(x_test)

    recall      = recall_score(y_test,y_pred)
    accuracy    = accuracy_score(y_test,y_pred)
    precision   = precision_score(y_test,y_pred)
    cm          = confusion_matrix(y_test,y_pred)

    print("Results: \n")
    print(f"Acuracia: {accuracy}")
    print(f"Precisao: {precision}")
    print(f"Recall:   {recall}")
    print(f"Conf. M:  {cm}")



def random_forest():
    pass


if __name__ == "main":
    test_base = pd.read_excel(r"base.xlsx",sheet_name='test')
    x_test = test_base.iloc[:,:-1]
    y_test = test_base.iloc[:,-1]

    train_base = pd.read_excel(r"base.xlsx",sheet_name='train')
    x_train = test_base.iloc[:,:-1]
    y_train = test_base.iloc[:,-1]

    data_set = [(x_train,y_train),(x_test,y_test)]