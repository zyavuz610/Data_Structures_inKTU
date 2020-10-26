# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:12:59 2020

@author: zafer
"""

# Python da dizi yerine liste veri yapısı mevcut. 
# Dizilerde tüm elemanlar aynı türdür, python da yok
# Listelerde tüm elemanlar aynı tür olmayabilir, pythondaki gibi

lst = list() # boş bir liste
lst = []

lst = list([1,2,3])
lst = [1,2,3]

lst = [1,2,3,'deneme','123']

print(len(lst))
print(lst[3][0])

#%%
lst = [9,7,5,3,1,2,4,6,8,10]

lst2 = lst[0:3]
print(lst2)

#%%
lst = [9,7,5,3,1,2,4,6,8,10]

lst2 = lst[0:7:3]
print(lst2)

#%%
lst = [9,7,5,3,1,2,4,6,8,10]

lst2 = lst[-4:-1:2]
print(lst2)

#%%
lst = [9,7,5,3,1,2,4,6,8,10]

lst2 = lst[::3]
print(lst2)

#%%
lst = [9,7,5,3,1,2,4,6,8,10]

lst2 = lst[::-1]
print(lst2)

#%% liste birleştirme (concatination)
lst = [9,7,5,3,1,2,4,6,8,10]
lst2 = [1,2,3]

print(lst2 + lst)

#%% liste çoğaltma
lst = [1,2,3]
lst2 = lst * 2 # (lst+lst)

print(lst2)

print(3 in lst)
print(4 not in lst)
