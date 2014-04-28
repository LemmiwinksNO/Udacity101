# [Double Gold Star] Memoization is a way to make code run faster by saving
# previously computed results.  Instead of needing to recompute the value of an
# expression, a memoized computation first looks for the value in a cache of
# pre-computed values.

# Define a procedure, cached_execution(cache, proc, proc_input), that takes in
# three inputs: a cache, which is a Dictionary that maps inputs to proc to
# their previously computed values, a procedure, proc, which can be called by
# just writing proc(proc_input), and proc_input which is the input to proc.
# Your procedure should return the value of the proc with input proc_input,
# but should only evaluate it if it has not been previously called.

def cached_execution2(cache, proc, proc_input):
    # cache structure -> { factorial: {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}}

    # If we have procedure in cache
    if proc in cache:
        if proc_input in cache[proc]:  # if we have proc_input stored for this proc
            return cache[proc][proc_input]  # return the stored result
        else:  # get result for this proc_input and proc and store it in cache[proc]
            cache[proc][proc_input] = proc(proc_input)
            return cache[proc][proc_input]
    else:  # if procedure is not in cache
        cache[proc] = {proc_input: proc(proc_input)}
        return cache[proc][proc_input]

# cleaner
def cached_execution(cache, proc, proc_input):
    if proc not in cache:
        cache[proc] = {proc_input: proc(proc_input)}
    elif proc_input not in cache[proc]:
        cache[proc][proc_input] = proc(proc_input)
    return cache[proc][proc_input]



# Here is an example showing the desired behavior of cached_execution:
def factorial(n):
    print "Running factorial"
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


cache = {} # start cache as an empty dictionary
### first execution (should print out Running factorial and the result)
# print cached_execution(cache, factorial, 2)

# print "Second time:"
### second execution (should only print out the result)
# print cached_execution(cache, factorial, 2)


# Here is a more interesting example using cached_execution
# (do not worry if you do not understand this, though,
# it will be clearer after Unit 6):

def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return (cached_execution(cache, cached_fibo, n - 1)
                + cached_execution(cache,  cached_fibo, n - 2))

# cache = {} # new cache for this procedure
# do not try this at home...at least without a cache!
#print cached_execution(cache, cached_fibo, 100)

import time


def time_execution(function, inputs):
    start = time.clock()
    result = function(*inputs)
    run_time = time.clock() - start  # time.clock() here = stop_time
    return result, run_time

print time_execution(cached_execution, (cache, factorial, 50000))[1]
print time_execution(cached_execution, (cache, factorial, 50000))[1]
