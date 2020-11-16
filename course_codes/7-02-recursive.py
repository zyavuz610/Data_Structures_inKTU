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


# a^n = a * a^(n-1)
def mypow(a,n):
    if(n==0):
        return 1
    else:
        return a * mypow(a,n-1)

print(mypow(5,4))

# S(1...n) = 1 + S(1...(n-1))
def mysum(n):
    if n==1:
        return 1
    else:
        return 1 + mysum(n-1)

# Fib(n) = Fib(n-1) + Fib(n-2)
# 0 1 2 3 4 5 6 7  8  9  10 ...
# 0 1 1 2 3 5 8 13 21 34 55 ....
def myfib(n):
    if n<2:
        return n
    else:
        return myfib(n-1) + myfib(n-2)


# n! = n * (n-1)!
def myfact(n):
    if n<2:
        return 1
    else:
        return n * myfact(n-1)

# 25 = Ob(11001)  
def dec2bin(n):
    if n<2:
        print(n,end="")
        return
    k = n%2
    dec2bin(n//2)
    print(k,end="")

dec2bin(125)

