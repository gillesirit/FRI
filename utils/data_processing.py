# FOR LOADING DATA
from pandas import read_csv
from itertools import combinations  
import os
from sklearn.preprocessing import OneHotEncoder

#clean an existing folder with a trailing / in the name
def clean_folder(folder):
    for f in os.listdir(folder):
        os.remove(folder+f)
    return

#COMPUTE ALL PAIRS FROM SAMPLE SET
def all_pairs(sample_set):
    n=sample_set.shape[0]
    test_list=[]
    for i in range(n):
        test_list.append(sample_set[i])
    set_of_pairs = list(combinations(test_list, 2)) 
    return set_of_pairs

def get_info(filename):
    df = read_csv(filename,header=None,dtype="int")
    size=df.shape[0]
    dimension=df.shape[1]-1
    number_of_class = df.iloc[:,dimension].nunique()
    return size,dimension,number_of_class
    
def load_dataset(filename):
    df = read_csv(filename,header=None,dtype="int")
    data = df.values
    dimension=df.shape[1]-1
    X = data[:, :-1]
    y = data[:,-1]
    return data, X, y, dimension

def load_dataset_string(filename):
    df = read_csv(filename,header=None,dtype="string")
    data = df.values
    dimension=df.shape[1]-1
    X = data[:, :-1]
    y = data[:,-1]
    return data, X, y, dimension

def load_dataset_one_hot(filename):
    df = read_csv(filename,header=None,dtype="int")
    data = df.values
    enc = OneHotEncoder(handle_unknown='ignore',drop='if_binary')
    enc.fit(data)
    dimension=df.shape[1]-1
    X = data[:, :-1]
    y = data[:,-1]
    return data, X, y, dimension

def feature_index_rank(list_of_scores):
    sorted_list = sorted(range(len(list_of_scores)), key=lambda i: list_of_scores[i], reverse=True)
    sorted_my_list = [list_of_scores[i] for i in sorted_list]
    return sorted_list

def remove_column(filename,new_file_name,columns_to_remove):
    df = read_csv(filename)
    df = df.drop(df.columns[columns_to_remove], axis=1)
    df.to_csv(new_file_name, index=False,header=False)
    return