#        Task2
# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def width(a):
    def length(b):
        return a * b
    return length

print(width(3)(4))

perimeter = width(4)
print(perimeter(5))
