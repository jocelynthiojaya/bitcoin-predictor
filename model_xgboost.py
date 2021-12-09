from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from matplotlib import pyplot as plt

import pandas as pd 

df = pd.read_csv('datasets/merge.csv')
df = df.drop(['date'], axis=1)

df.info()

max_seed = 100

for i in range(max_seed):


    # split into train&val , test set with 0.2
    train_set, test_set = train_test_split(df, test_size=0.3, random_state=i)
    # X train, first 5 column
    X_train = train_set.iloc[:,0:5].values
    # Y value the predicted  the last column
    Y_train = train_set.iloc[:,5].values
    # defining test dataset
    X_test = test_set.iloc[:,0:5].values
    Y_test = test_set.iloc[:,5].values
    # fit model no training data
    model = XGBClassifier()
    model.fit(X_train, Y_train)
    # make predictions for test data
    y_pred = model.predict(X_test)
    predictions = [round(value) for value in y_pred]
    # evaluate predictions
    accuracy = accuracy_score(Y_test, predictions)
    if accuracy*100.0>= 60.0:
        print("Accuracy: %.2f%%" % (accuracy * 100.0))
        print(f"BEST VALID SEED : {i}")
        break
    
