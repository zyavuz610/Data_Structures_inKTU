# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:01:08 2020

@author: zafer
"""

#%% faktöryel
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))

#%% ruler
def draw_line(tick_length, tick_label=''):
  """Draw one line with given tick length (followed by optional label)."""
  line = '-' * tick_length
  if tick_label:
    line += ' ' + tick_label
  print(line)

def draw_interval(center_length):
  """Draw tick interval based upon a central tick length."""
  if center_length > 0:                   # stop when length drops to 0
    draw_interval(center_length - 1)      # recursively draw top ticks
    draw_line(center_length)              # draw center tick
    draw_interval(center_length - 1)      # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
  """Draw English ruler with given number of inches and major tick length."""
  draw_line(major_length, '0')            # draw inch 0 line
  for j in range(1, 1 + num_inches):
    draw_interval(major_length - 1)       # draw interior ticks for inch
    draw_line(major_length, str(j))       # draw inch j line and label


if __name__ == '__main__':
  draw_ruler(2,4)
  print('='*30)
  draw_ruler(1,5)
  print('='*30)
  draw_ruler(3,3)
  
#%% binary search
def binary_search(data, target, low, high):
  """Return True if target is found in indicated portion of a Python list.
  The search only considers the portion from data[low] to data[high] inclusive.
  """
  if low > high:
    return False                    # interval is empty; no match
  else:
    mid = (low + high) // 2
    if target == data[mid]:         # found a match
      return True
    elif target < data[mid]:
      # recur on the portion left of the middle
      return binary_search(data, target, low, mid - 1)
    else:
      # recur on the portion right of the middle
      return binary_search(data, target, mid + 1, high)
  
data = [2,3,5,9,1,20,3,5,78,8,85,32,33,42,12,15]
data = sorted(data)
print(binary_search(data, 16, 0, len(data)))