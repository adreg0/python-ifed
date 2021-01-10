import time
import pandas as pd
import numpy as np

def default():
    '''Returns the length of verified elements by linear search and time taken for execution '''
    start = time.time()
    verified_elements = []

    for element in subset_elements:
        if element in all_elements:
            verified_elements.append(element)

    print(len(verified_elements))
    print('Duration using linear search: {} seconds'.format(time.time() - start))

def usingnp():
    '''Uses numpy vectorisation and returns the length of verified_elements and the time taken for execution.'''
    start = time.time()
    verified_elements=[]
    a=np.array(subset_elements)
    verified_elements=a[np.in1d(subset_elements, all_elements)]
    print(len(verified_elements))
    print('Duration using numpy: {} seconds'.format(time.time() - start))

def usingset():
    ''' Uses python set for returning the length of elements and the time taken for execution.'''
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
