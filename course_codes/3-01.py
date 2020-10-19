# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:33:19 2020

@author: zafer
"""

year = 1700
century = (year+99) // 100
print("the century of",year,"is",century)

n,k = 100,0
for i in range(n**2):
    k += i+1
    print(k)
    
for i in range(n):
    for j in range(n):
        print(i,j)
        
# a^n
n,a = 10,3
for i in range(a**n):
    print(i)
    
    
arr = [3,6,5,8,2,4,9,7,3,56,43,23,4,69]
arr2 = sorted(arr)
print(arr2)

#%%
arr = [3,6,5,8,2,4,9,7,3,56,43,23,4,69]
n = len(arr)
for i in range(n):
    for j in range(n-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            '''
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            '''
# n*(n-1)/2 = n^2 -n/2 = O(n^2)
print(arr)