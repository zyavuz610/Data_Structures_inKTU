# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:19:39 2020

@author: zafer

1) a^n
2) 1-n arası toplam sayılar
3) fibonacci
4) fact,
5) dec2bin
"""

def dec2bin(n):
    if n<2:
        print(n,end="")
        return
    k = n%2
    dec2bin(n//2)
    print(k,end="")


dec2bin(125)
