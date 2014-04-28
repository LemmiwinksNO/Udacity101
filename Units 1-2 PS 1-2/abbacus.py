#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia
#
#  Around the world, abaci have been used in pre-schools and elementary
# 
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------
#                             Sum                123
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a
# given positive integer value.
#
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

import math

def print_abacus(value):
    # Use a loop to cut down on lines
    for num in range(10,0,-1):
        n = value // math.pow(10, num-1)
        value -= n * math.pow(10, num-1)
        # max function prevents negative numbers
        zeroes = "0" * int(max(0,(5-n)))  # unused 0s can be from 0 to 5
        stars = "*" * int(min(5,10-n))    # unused stars can be from 0 to 5
        zeroes2 = "0" * int(max(0, n-5))
        stars2 = "*" * int(min(5, n))
        print "|" + zeroes + stars + "   " + zeroes2 + stars2 + "|"

# The above in 4 lines
def print_abacus(value):
    for num in range(10,0,-1):
        n = value // math.pow(10, num-1)
        value -= n * math.pow(10, num-1)
        print "|" + "0" * int(max(0,(5-n))) + "*" * int(min(5,10-n)) + "   " + "0" * int(max(0, n-5)) + "*" * int(min(5, n)) + "|"


# BETTER SOLUTION!
def print_abacus(value):
    i = 9
    while i >= 0:
        n = value // (10**i)
        value = value%(10**i)
        i -= 1
        print '|' + '00000*****'[:10-n] + '   ' + '00000*****'[10-n:] + '|'

    # NOTE, another way to do this would be to slice => '00000*****'[:10-n] + '   ' + '00000*****'[10-n:] + '1'

# The above in 4 lines
def print_abacus(value):
    for i in range (9,-1,-1):
        n = value // (10**i)
        value = value%(10**i)
        print '|' + '00000*****'[:10-n] + '   ' + '00000*****'[10-n:] + '|'


###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|