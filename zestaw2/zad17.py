import math

### NOT WORKING

def derivative(x):
    return 2*x
    # return (x**x)*(math.log10(x)+1)

def function(x):
    return x**x - 2020


x = function(0)
eps = 0.0001
for _ in range(100000):
    x = x - function(x)/derivative(x)
    # print(x)

print(x)