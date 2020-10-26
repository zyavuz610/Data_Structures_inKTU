# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:59:34 2020

@author: zafer
"""
"""
def func():
    a = 1
    func()

func()
"""

# sum(1..n) = n + sum(n-1)
def mySum(n):
    if(n==1):
        return 1
    return n + mySum(n-1) + mySum(n+1)

print(mySum(5))

"""
mySum(5) --> (15)
    5 + mySum(4) --> (10)
        4 + mySum(3) --> (6)
            3 + mySum(2) --> (3)
                2 + mySum(1)
                    mySum(1) = 1
"""


