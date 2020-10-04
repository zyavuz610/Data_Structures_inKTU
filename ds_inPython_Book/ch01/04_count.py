# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:08:36 2020

@author: zafer
"""


def count(data, target):
  n = 0
  for item in data:
    if item == target:               # found a match
      n += 1
  return n

mylist = [2,3,5,2,3,6,8]
print(count(mylist,3))