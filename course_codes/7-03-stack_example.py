# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:27:04 2020

@author: zafer
"""
from ArrayStack import *

S = ArrayStack()
n = 25

while(n>0):
    S.push(n%2)
    n = n//2

while (not S.is_empty()):
    print(S.pop(),end="")