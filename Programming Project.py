# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:06:02 2021

@author: djwre
"""

import random
from insertionsort import InsertionSort
from heapsort import heapSort
from randomizedselect import RandomizedSelect
from datetime import datetime 


RAND_MAX = 32767

#begin_time = datetime.datetime.now()

m = 5
n = 10000
i = 2 * n / 3
i = int(i)

A = [random.randint(0, RAND_MAX) for _ in range(n)] 
A2 = [random.randint(0, RAND_MAX) for _ in range(n)]  
A3 = [random.randint(0, RAND_MAX) for _ in range(n)]  
A4 = [random.randint(0, RAND_MAX) for _ in range(n)]  
A5 = [random.randint(0, RAND_MAX) for _ in range(n)]  
      





def Alg1(A, n, i):
    InsertionSort(A, n)
    print(A[i])
    
    
def Alg2(A, n, i):
    heapSort(A, n)
    print(A[i])

def Alg3(A, n, i):
    l = 0
    x = RandomizedSelect(A, l, n-1, i)
    print(x)
    





print("Heap Sort1")
now1 = datetime.now()
Alg3(A, n, i)
later1 = datetime.now()
difference1 = (later1 - now1).total_seconds()
print(difference1)


print("Heap Sort2")
now2 = datetime.now()
Alg3(A2, n, i)
later2 = datetime.now()
difference2 = (later2 - now2).total_seconds()
print(difference2)


print("Heap Sort3")
now3 = datetime.now()
Alg3(A3, n, i)
later3 = datetime.now()
difference3 = (later3 - now3).total_seconds()
print(difference3)


print("Heap Sort4")
now4 = datetime.now()
Alg3(A4, n, i)
later4 = datetime.now()
difference4 = (later4 - now4).total_seconds()
print(difference4)


print("Heap Sort5")
now5 = datetime.now()
Alg3(A5, n, i)
later5 = datetime.now()
difference5 = (later5 - now5).total_seconds()
print(difference5)

Average_RT = (difference1 + difference2 + difference3 + difference4 + difference5) / 5

print("Average RT: ", Average_RT)

    




