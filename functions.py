a = 4
b = 6
c = sum((a,b))
print(c)
def function1(a,b):
    print("Sum of two numbers", a+b)

def function2(a,b):
    """This is a function to calculate average.
    This works for two numbers only."""
    average = (a+b)/2
    return average
z = function2(4,6)
print(z)
y = function2(3,3)
print(y)
print(function2.__doc__)