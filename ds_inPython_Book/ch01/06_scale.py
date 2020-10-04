# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:12:48 2020

@author: zafer
"""


def scale(data, factor):
  for j in range(len(data)):
    data[j] *= factor
    
mylist = [2,3,5,2,3,6,8]
print(mylist)
scale(mylist,2)
print(mylist)