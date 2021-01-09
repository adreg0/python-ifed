import time
import pandas as pd
import numpy as np

def default():
    '''
    Uses normal linear search.
    
    '''
    start = time.time()
    verified_elements = []

    for element in subset_elements:
        if element in all_elements:
            verified_elements.append(element)

    print(len(verified_elements))
    print('Duration using linear search: {} seconds'.format(time.time() - start))

def usingnp():
    '''
    used numpy vectorisation---> It consumed much lesser time than the regular linear search. 
    By using np.in1d, boolean values will be obtained which represents whether an element in one array is present in another array.
    Verified_elements array is obtained in lesser time by using this boolean array over the subset_elements array 
    
    '''
    start = time.time()
    verified_elements=[]
    a=np.array(subset_elements)
    verified_elements=a[np.in1d(subset_elements, all_elements)]
    print(len(verified_elements))
    print('Duration using numpy: {} seconds'.format(time.time() - start))

def usingset():
    '''
    Set is a python datastructure which avoids duplicate occurences of values unlike list or tuple.
    Sets are implemeted with the aid of hash tables which stores objects based on hash value and this makes search faster.

    '''
    start = time.time()
    b=set(all_elements)
    verified_elements=[]
    for i in subset_elements:
        if i in b:
            verified_elements.append(i)
    print(len(verified_elements))
    print('Duration using set: {} seconds'.format(time.time() - start))

with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')

print("-----------Traditional linear search-------------")
default()
print("-----------Using numpy vectorisation-------------")
usingnp()
print("-----------Using set datastructure---------------")
usingset()
