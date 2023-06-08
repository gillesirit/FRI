#BASELINE LogisticRegression using all attributes with cross validation
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from statistics import mean

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def baseline_lr_accuracy(X, y,number_of_folds):
    skf = StratifiedKFold(n_splits=number_of_folds, shuffle=True)
    model = LogisticRegression(solver='lbfgs',max_iter=10000) 
    results=cross_val_score(model,X,y,cv=skf)
    return results.mean()

def baseline_dt_accuracy(X, y,number_of_folds):
    skf = StratifiedKFold(n_splits=number_of_folds, shuffle=True)
    model = DecisionTreeClassifier(max_depth =5, random_state = 42)
    results=cross_val_score(model,X,y,cv=skf)
    return results.mean()

def baseline_rf_accuracy(X, y,number_of_folds):
    skf = StratifiedKFold(n_splits=number_of_folds, shuffle=True)
    model = RandomForestClassifier()
    results=cross_val_score(model,X,y,cv=skf)
    return results.mean()