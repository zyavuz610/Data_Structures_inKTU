import sys

try:
    n = int(sys.argv[1])
except:
    n = 10

import sys                              # provides getsizeof function
data = []
for k in range(n):                      # NOTE: must fix choice of n
  a = len(data)                         # number of elements
  b = sys.getsizeof(data)               # actual size in bytes
  print('{2}:Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b,k))
  data.append(k**2)                     # increase length by one
  if k%5 == 0:
      data.extend([0]*2)