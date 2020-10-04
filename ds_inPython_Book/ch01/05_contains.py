# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:10:57 2020

@author: zafer
"""


def contains(data, target):
  for item in data:
    if item == target:               # found a match
      return True
  return False

mylist = [2,3,5,2,3,6,8]
print(contains(mylist,10))