def factorial(n):
    i = 1
    f = 1
    while i <= n:
        f *= i
        i += 1
    return f
 
def factorial(n):
    result = 1
    while n >=1:
        result *=n
        n = n-1
    return result


print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720