# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0. 


def greatest(numbers):
    greatest = numbers.pop() if len(numbers) > 0 else 0

    for num in numbers:
        if num > greatest:
            greatest = num

    return greatest


print greatest([4, 23, 1])
#>>> 23
print greatest([])
#>>> 0
