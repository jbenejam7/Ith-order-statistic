# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:44:32 2021

@author: djwre
"""

import random

#to heapify subtree rooted at index i
#n is size of heap
def heapify(arr, n, i):
    largest = i #initialize largest root
    l = 2 * i + 1 #left =  2*i+1
    r = 2 * i + 2 #right = 2*i+1
    
    #see if left child of root exists and is 
    #greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
   
        
    #see if right child of root exists and is 
    #greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
        
    #change root if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] #swap
        
        #heapify the root
        heapify(arr, n, largest)
        
#the main function to sort an array of given size
def heapSort(A, n):
    n = len(A)
    
    #build a maxheap
    #Since last parent will be at ((n//2)-1) we can start at that location
    for i in range((n // 2) - 1, -1, -1):
        heapify(A, n, i)
        
    #one by one extract elements
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i] #swap
        heapify(A, i, 0)
        

'''   
#test code
n = 5
A = random.sample(range(1, 99), n)


heapSort(A, n)

print ("sorted array: ")
for i in range(n):
    print("%d" %A[i])
    '''