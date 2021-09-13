# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:02:06 2021

@author: djwre
"""
import random

#Function for InsertionSort
def InsertionSort(A, n):
    #traverse through 1 to len(arr)
    for i in range(1, n):
        key = A[i]
        
        #move elements of arr [0..i-1], that are
        #greater than key, to one position ahead
        #of the current position
        j = i-1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        


'''        
#driver code to test above
n = 5
A =  random.sample(range(1, 99), n)
InsertionSort(A, n)



for i in range(len(A)):
    print ("%d" %A[i])
        '''
 




