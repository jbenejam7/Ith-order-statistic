# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 19:53:27 2021

@author: djwre
"""

import random


def Partition(A, p, r):
    x = A[r]
    i = p -1
    for j in range(p, r - 1):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i] #swap
    A[i+1],A[r] = A[r],A[i+1] #swap
    return i + 1



def RandomizedPartition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i],A[r] #swap
    return Partition(A, p, r)
    
    

def RandomizedSelect(A, p, r, i):
    if p == r:
        return A[p]
    q = RandomizedPartition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return RandomizedSelect(A, p, q-1, i)
    else:
        return RandomizedSelect(A, q+1, r, i-k)













