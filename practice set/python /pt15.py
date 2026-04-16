import math 
def f(x):
    return 5*x*math.sin(x) - 3*x
def df(x):
    return 5*math.sin(x) + 5*x*math.cos(x) -3

x = -4

for i in range(10):
    x = x -f(x)/df(x)
print("root is = ",x)
