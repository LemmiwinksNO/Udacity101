# Procedure that times the execution of a piece of code

import time


def time_execution2(code):
    start = time.clock()
    result = eval(code)  # evaluates string as python expression. So runs string as python.
    run_time = time.clock() - start  # time.clock() here = stop_time
    return result, float(run_time)

# I like this one better
def time_execution(function, inputs):
    start = time.clock()
    result = function(inputs)
    run_time = time.clock() - start  # time.clock() here = stop_time
    return result, run_time


def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1


# Examples
print time_execution(spin_loop, 10 ** 6)[1]
