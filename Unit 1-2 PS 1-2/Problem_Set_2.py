# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else: 
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    if a > b and a > c:
        if b > c:
            return b
        else:
            return c
    if b > a and b > c:
        if a > c:
            return a
        else:
            return c
    else:
        if a > b:
            return a
        else:
            return b

def median(a,b,c):
    if a == biggest(a,b,c):
        return bigger(b,c)
    if b == biggest(a,b,c):
        return bigger(a,c)
    else:
        return bigger(a,b)
    
def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)


print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7


# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search, target):
    lastPos = -1
    while True:
        pos = search.find(target, lastPos + 1)
        if pos == -1:
            break
        else:
            lastPos = pos
            
    return lastPos
        

def find_last(search, target):
    return search.rfind(target)



print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0




# 2 GOLD STARS

# Define a procedure, print_multiplication_table,
# that takes as input a positive whole number, and prints out a multiplication,
# table showing all the whole number multiplications up to and including the
# input number. The order in which the equations are printed matters.

# Hint: You can not add an integer and a string, but in homework 1.9
# you came across a method, str, for turning an integer into a string.

def print_multiplication_table(n):
    i = 1  # first column
    while i <= n:  # main loop
        j = 1  # second column
        while j <= n:  # second column loop
            print str(i) + ' * ' + str(j) + ' = ' + str(i * j)
            j += 1
        i += 1



print_multiplication_table(2)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4

print_multiplication_table(3)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 1 * 3 = 3
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4
#>>> 2 * 3 = 6
#>>> 3 * 1 = 3
#>>> 3 * 2 = 6
#>>> 3 * 3 = 9




# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The answer should use as many 5p stamps as possible,
# then 2 pence stamps and finally 1p stamps.

def stamps(total):
    s1,s2,s3 = 0,0,0
    while total >= 5:
        s1 += 1
        total -= 5
    while total >= 2:
        s2 += 1
        total -= 2
    while total >= 1:
        s3 += 1
        total -= 1
    return s1, s2, s3

def stamps(total):
    five = total // 5
    r = total % 5
    two = r//2
    one = r - two*2
    return five, two, one


print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps
print stamps(50)


# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built in functions.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def smaller(a,b):
    if a < b:
        return a
    else:
        return b

def smallest(a,b,c):
    return smaller(a,smaller(b,c))
    
def set_range(a,b,c):
    big = biggest(a,b,c)
    small = smallest(a,b,c)
    return big - small


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6



# A function that always returns the biggest number

def biggest(list)
    biggest = list.pop()
    while len(list) > 0:
        new = list.pop()
        if list.pop() > biggest:
            biggest = new






biggest([5,2,5,6,7,21,23456,547,4,4,2,4,67,7,3])