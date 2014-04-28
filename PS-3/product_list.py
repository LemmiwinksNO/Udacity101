# Define a procedure, product_list,
# takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together. 


# A function that takes as input a list of numbers and returns a number
# that is the result of multiplying all those numbers together.
#
# @param [list] numbers List of numbers
# @return [float] result Result of multiplying all numbers in list together.
def product_list(numbers):
    # Get first number if there is a first number
    result = numbers.pop() if len(numbers) > 0 else 0

    # Iterate over the rest of the list
    for num in numbers:
        result = result * num

    return result


print product_list([9])
#>>> 9

print product_list([1, 2, 3, 4])
#>>> 24

print product_list([])
#>>> 1
