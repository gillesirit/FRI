'''
from sklearn.feature_selection import SelectKBest,chi2,mutual_info_classif

#TESTING WITH ALL FEATURES
# feature selection chi2
def select_all_features_chi2(X_train, y_train, X_test):
    fs = SelectKBest(chi2, k='all')
    fs.fit(X_train, y_train)
    X_train_fs = fs.transform(X_train)
    X_test_fs = fs.transform(X_test)
    return X_train_fs, X_test_fs, fs

# feature selection mutual information
def select_all_features_mutual(X_train, y_train, X_test):
    fs = SelectKBest(mutual_info_classif, k='all')
    fs.fit(X_train, y_train)
    X_train_fs = fs.transform(X_train)
    X_test_fs = fs.transform(X_test)
    return X_train_fs, X_test_fs, fs

#TESTING WITH k BEST FEATURES
# feature selection chi2
def select_k_features_chi2(X_train, y_train, X_test, k):
    fs = SelectKBest(chi2, k=k)
    fs.fit(X_train, y_train)
    X_train_fs = fs.transform(X_train)
    X_test_fs = fs.transform(X_test)
    return X_train_fs, X_test_fs, fs

# feature selection mutual information
def select_k_features_mi(X_train, y_train, X_test,k):
    fs = SelectKBest(mutual_info_classif, k=k)
    fs.fit(X_train, y_train)
    X_train_fs = fs.transform(X_train)
    X_test_fs = fs.transform(X_test)
    return X_train_fs, X_test_fs, fs
'''