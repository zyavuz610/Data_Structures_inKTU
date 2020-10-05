# same memory address
temp = 95
t2 = temp
print(id(temp))
print(id(t2))

temp = 95.0
t2 = temp
t2 = 100 # a new dynamic variable
print(temp)
print(t2)
print(id(temp))
print(id(t2))

b1 = bool() # an empty bool variable (value is False) 
print(b1)

n1 = int()  # an empty int variable (value is 0)
n1 = int(20)  # an empty int variable (value is 20)
n1 = int('40')  # an empty int variable (value is 40)
print(n1)

f1 = float(input("Please enter your grade: "))
print(f1)

s1 = str() # empty string
s2 = 'hello'
s3 = "world"
s4 = str("hello" + s3)
print(s4)

# list, tuple,
# A list instance stores a sequence of objects. A list is a referential structure,
l1 = list() # empty list
l1 = list([2,3])
print(l1[1])

# The tuple class provides an immutable version of a sequence
t1 = tuple()  # t1 is immutable
print(t1)

t1 = tuple([2,3])  # t1 is immutable or
t1 = (2,3)
print(t1[0])

# set, frozenset
# Python’s set class represents the mathematical notion of a set, namely a collection of elements, without duplicates, and without an inherent order to those elements.
# The frozenset class is an immutable form of the set type

s1 = set() # an empty set
s1 = set({2,3,3}) 
s1 = {8,2,2,3,6,6}
print(s1)
s1.add(5) # ordered
print(s1)

fs1 = frozenset({6,2,3,3,6}) # immutable set, ordered
print(fs1)


# dict (key:value)
#Python’s dict class represents a dictionary, or mapping, from a set of distinct keys to associated values.
             #      key :value
points = {'AA':4.0, 'BA':3.5, 'BB':3.0, 'CB':2.5, 'CC':2.0, 'DC':1.5}
print(points['AA'])
print(points.get('BB'))
l1 = list(points.values()) # list
print(l1[0])

for x in points:
  print(x)
  print(points[x])

for x in points.values():
  print(x)
