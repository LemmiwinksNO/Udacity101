# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game. 

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

# PROCESS
# What we need to do is check each row and column and check the numbers.
# ROWS -> You can grab each row with for row in square. Then you can check it.

# Algorithm
# 1. Get number of rows and columns
# 2. Iterate over each row in the square
# 3. Check each row and confirm only uses numbers 1-num_columns and confirm that no
#   number repeats.
#       How?
#
# 4. How do we check columns?
#   Create column lists - column = row1[0] + row2[0] + row3[0]


# A function that takes in a list of lists. Where each list inside the main list is
# a row.
#
# @param [list] square Sudoku square
# @return [boolean] correct Whether it is a valid sudoku square
def check_sudoku2(square):
    size = len(square)  # Extract size of grid

    for row in square:  # Test rows
        # Confirm each item in is an integer between 1 and number of rows
        for item in row:
            if item < 1 or item > size or type(item) != int:
                return False
        # confirm no duplicate numbers in row
        if len(row) != len(set(row)):
            return False

    column = []
    for i in range(size): # Test columns
        del column[:]    # empty test list for each column
        # Build column
        for row in square:
            column.append(row[i])
        # Confirm each item in is an integer between 1 and number of rows
        for item in column:
            if item < 1 or item > size:
                return False
        # confirm no duplicate numbers in column
        if len(column) != len(set(column)):
            return False

    return True


# The professor's solution
def check_sudoku(square):
    n = len(square) # Extract size of grid
    digit = 1 # start with 1
    while digit <= n: # Go through each digit
        i = 0
        while i < n: # Go through each row and column
            row_count = 0
            col_count = 0
            j = 0
            while j < n: # For each entry in ith row/column
                if square[i][j] == digit: #check row count
                    row_count = row_count + 1
                if square[j][i] == digit:
                    col_count = col_count + 1
                j = j + 1
            if row_count != 1 or col_count != 1:
                return False
            i = i + 1 # next row/column
        digit = digit + 1 # next digit
    return True











correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False