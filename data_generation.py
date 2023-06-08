'''Create synthetic dataset = a CSV file'''
'''Label of a = last element in a raw. Label given as f.'''
import itertools
from itertools import combinations
# FOR LOADING DATA
from pandas import read_csv
import numpy as np
from random import randint
from sklearn.utils import shuffle
import datetime
import os

#clean an existing folder with a trailing / in the name
def clean_folder(folder):
    for f in os.listdir(folder):
        os.remove(folder+f)
    return

'''
    range is the values to be generated inclusive. 
    If _range is one, then the values are 0 or 1 (binary)
'''
def create_a_csv_row(f,dimension,_range):  #binary is _range=1 otherwise categorical _range indicate the candidate values
    row=""
    arr=[]
    for i in range(dimension):
        a=randint(0,_range) 
        arr.append(a)
        row+=str(a)+","
    label=f(arr)
    row+=str(label)
    return row,arr

#size is the number of rows  - f is the class function - range of value (1 means binary)
def create_categorical_dataset(f,dimension,size,categorical_range): #no redundancy
    now = datetime.datetime.now()
    filename_out="tests/sample"+str(size)+"-"+str(categorical_range)+"-"+str(now)+".csv"
    filename_out=filename_out.replace(" ", "")
    result=open(filename_out,'w')
    set_arr=[]
    with result as outfile:
        i=0
        while (i<size):
            row,arr=create_a_csv_row(f,dimension,categorical_range)
            if not(arr in set_arr):
                set_arr.append(arr)
                outfile.write(row+"\n")
                i+=1
    return filename_out                                                         

#GENERATE RANDOM SAMPLE SET OF size ELEMENTS FROM A DATASET
def generate_sample_set(dataset,size):
    rdataset=shuffle(dataset)
    sample_set= rdataset[:size]
    #sample_set.astype(str) #FOR UCI DATA
    return sample_set

#COMPUTE ALL PAIRS FROM SAMPLE SET
def all_pairs(sample_set):
    n=sample_set.shape[0]
    test_list=[]
    for i in range(n):
        test_list.append(sample_set[i])
    set_of_pairs = list(combinations(test_list, 2)) 
    return set_of_pairs

def load_dataset(filename):
    dataset = read_csv(filename, header=None)
    data = dataset.values
    dimension=data.shape[1] - 1
    data.astype(str)
    X = data[:, :-1]
    y = data[:,-1]
    return data, X, y, dimension