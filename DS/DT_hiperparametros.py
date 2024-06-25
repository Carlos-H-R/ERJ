# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:03:06 2020

@author: Karla
"""

import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix

import warnings

import warnings
warnings.filterwarnings("ignore")



def modelosDT(ds, name):
    depth={"max_depth":[3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
           "min_samples_split":[2, 4, 6, 8, 10, 12, 14, 16],
           "min_samples_leaf":[2, 4, 6, 8, 10, 12, 14, 16],
           "max_features":[5,10] #If None, then max_features=n_features.
           }       
    
    
    X_train,y_train=ds[0]
    X_test,y_test=ds[1]
     
    DTC=DecisionTreeClassifier(class_weight="balanced")
    
    DTC_Grid=GridSearchCV(DTC,param_grid=depth , cv=6, scoring='accuracy')
    # DTC_Grid=GridSearchCV(DTC,param_grid=depth , cv=6, scoring='f1')
    DTC=DTC_Grid.fit(X_train,y_train) 


    arquivo = open('saidaDTC.txt','w')

    # print('Best parameters found:\n', DTC.best_params_)
    arquivo.write('Best parameters found: %s' % DTC.best_params_)
    arquivo.write('\n')

    # All results
    means = DTC.cv_results_['mean_test_score']
    stds = DTC.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, DTC.cv_results_['params']):
        # print("%0.3f (+/-%0.03f) for %r" % (mean, std * 2, params))
        arquivo.write('media: %0.3f ' % mean)
        std=std*2
        arquivo.write(' desvio: (+/-%0.03f) ' % std)
        arquivo.write(' param: %s ' % params)
        arquivo.write('\n')

    y_true, y_pred = y_test, DTC.predict(X_test)

    # print('Results on the test set:')
    # print(classification_report(y_true, y_pred))
    
    acc=accuracy_score(y_test, y_pred,normalize=False)
    precision=precision_score(y_test, y_pred)
    f1=f1_score(y_test, y_pred, average='micro')    	
    recall=recall_score(y_test, y_pred, average='weighted')
    cm=confusion_matrix(y_test, y_pred)
    print("accuracy", acc)
    print("precision", precision)
    print("recall", recall)    
    print("f1", f1)
    print("cm", cm)
       
    arquivo.write('Results on the test set: \n')
    arquivo.write(' accuracy: %0.03f ' % acc)
    arquivo.write(' precision: %0.03f ' % precision)
    arquivo.write(' recall: %0.03f ' % recall)
    arquivo.write(' f1: %0.03f ' % f1)
    arquivo.write(' cm: ' % cm)
    arquivo.write('\n')



if __name__ == "__main__":
    #########################################################
    # leitura de dados UX
    planilha_1=pd.read_excel(r"base_pacientes_sintomas.xlsx",sheet_name="treino")
    X_train = planilha_1.iloc[:,:-1]
    y_train = planilha_1.iloc[:,-1]

    # # fit scaler media-desvio
    # X = StandardScaler().fit_transform(X)

    # normalizacao com min-max
    # scaler = MinMaxScaler(feature_range=(0, 1))
    # scaler = scaler.fit(X_train)    
    # X_scaled = scaler.transform(X_train)
        

    planilha_1=pd.read_excel(r"base_pacientes_sintomas.xlsx",sheet_name="teste")
    X_test = planilha_1.iloc[:,:-1]
    y_test = planilha_1.iloc[:,-1]

    # X_teste_scaled = scaler.transform(X_test)
    # X_test=X_teste_scaled




    #################################
    data_sets = [(X_train, y_train),(X_test, y_test)]
    name=['Covid-Train']
    modelosDT(data_sets, name=name)
    #modelosRF(data_sets, name=name)
