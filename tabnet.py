from pytorch_tabnet.tab_model import TabNetClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import numpy as np
np.random.seed(0)
from matplotlib import pyplot as plt

import pandas as pd 

df = pd.read_csv('datasets/merge.csv')
df = df.drop(['date'], axis=1)

df.info()

# split into train&val , test set with 0.2
train_val, test_set = train_test_split(df, test_size = 0.2, random_state = 1)

# split the train and validation to 0.2 
train_set, val_set = train_test_split(train_val, test_size=0.2, random_state=2)

# X train, first 5 column
X_train = train_set.iloc[:,0:5].values
# Y value the predicted  the last column
Y_train = train_set.iloc[:,5].values

# defining validation dataset
X_val = val_set.iloc[:,0:5].values
Y_val = val_set.iloc[:,5].values

# defining test dataset
X_test = test_set.iloc[:,0:5].values
Y_test = test_set.iloc[:,5].values

# print(Y_train.size)
# print(Y_val.size)
# print(Y_test.size)



clf = TabNetClassifier()  #TabNetRegressor()
# clf.fit(
#   X_train, Y_train,
#   eval_set=[(X_val, Y_val)],
#   max_epochs=50,
#   eval_metric=['auc']
# )



# This illustrates the warm_start=False behaviour
save_history = []
for _ in range(1):
    clf.fit(
        X_train=X_train, y_train=Y_train,
        eval_set=[(X_train, Y_train), (X_val, Y_val)],
        eval_name=['train', 'valid'],
        eval_metric=['auc'],
        max_epochs=5 , patience=20,
        batch_size=1024, virtual_batch_size=128,
        num_workers=0,
        weights=1,
        drop_last=False
    )
#     save_history.append(clf.history["valid_auc"])
    
# assert(np.all(np.array(save_history[0]==np.array(save_history[1]))))

# preds = clf.predict_proba(X_test)[:,1]
# test_auc = roc_auc_score(y_score=preds[:,1], y_true=Y_test)


# preds_valid = clf.predict_proba(X_val)
# valid_auc = roc_auc_score(y_score=preds_valid[:,1], y_true=Y_val)

# print(f"BEST VALID SCORE FOR {dataset_name} : {clf.best_cost}")
# print(f"FINAL TEST SCORE FOR {dataset_name} : {test_auc}")



# clf.predict(X_test)







