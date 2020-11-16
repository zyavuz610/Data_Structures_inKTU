# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:44:13 2020

@author: zafer
"""

from ArrayQueue import *
import random

cash = ArrayQueue()
credit = ArrayQueue()

n = 10
for i in range(n):
    print(i,"---------------------------------")
    r = random.randrange(1,4)
    if r==1:
        cash.enqueue("Customer "+str(i))
        print("Customer"+str(i)+" added to Cash Queue")
    elif r==2:
        credit.enqueue("Customer "+str(i))
        print("Customer"+str(i)+" added to Credit Queue")
    elif r==3 and (not cash.is_empty()):
        s = cash.dequeue()
        print(s+" deleted from Cash Queue")
    elif r==4 and (not credit.is_empty()):
        s = credit.dequeue()
        print(s+" deleted from Credit Queue")
    print("Cash:")
    cash.printQueue()
    print("Credit:")
    credit.printQueue()
    print("---------------------------------")