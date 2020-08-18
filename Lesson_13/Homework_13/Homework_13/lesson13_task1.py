#          Task 1
# Write a Python program to detect the number of local variables declared in a function.

def func(a, b):
    c = 1
    d = 2
    e = 3
    f = None
    return a + b + c + d

print(func.__code__.co_nlocals)