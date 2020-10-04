x = [100, 200]
y = [100, 200]

if(x==y):
    print("x and y are equal")
else:
    print("x and y are NOT equal")

if(x is y):
    print("x and y are identical")
else:
    print("x and y are NOT identical")

z = x
if(x is z):
    print("x and z are identical")
else:
    print("x and z are NOT identical")

