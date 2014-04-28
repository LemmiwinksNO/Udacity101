def find_element(p,t):
    i = 0
    while i < len(p):
        if p[i] == t:
            return i
        i = i + 1
    return -1
 
def find_element(p,t):
    i = 0
    for e in p:
        if e == t:
            return i
        i += 1
    return -1

# index method <list>.index(<value>)
p = [0, 1, 2]
print p.index(3)

# in -> <value> in <list>
3 in p #=> is 3 in list p?

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.
def find_element(values, value):
    if value in values:
        return values.index(value)
    return -1


# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no
# repeated elements.

def union(list1, list2):
    for e in list2:
        if e not in list1:
            list1.append(e)


# Test
a = [1,2,3]
b = [2,4,6]
union(a,b)
print a
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]

