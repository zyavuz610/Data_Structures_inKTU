# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:39:06 2020

@author: zafer
"""
from ArrayStack import *

S = ArrayStack()

sfile = "source.c"
original = open(sfile) 
print(original)  
    
for line in original:
  S.push(line.rstrip('\n'))
original.close()

tfile = "target.c"
output = open(tfile, 'w')    # reopening file overwrites original
while not S.is_empty():
  output.write(S.pop() + '\n')  # re-insert newline characters
output.close()