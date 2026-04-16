#newton raphson 

import math 
def f(x) :
    return x**3 + 5*x**2 - 19*x + 3 
def df(x):
    return 3*x**2 + 10*x - 19

x=3

for i in range(10):
    x = x -f(x)/df(x)
print("="*30)
print("The root : ",round(x,3))
print("="*30)

#cos series 

import math 

x=2*math.pi/7
sum = 0

for k in range(10):
    term = (-1)**k * x**(2*k)/math.factorial(2*k)
    sum += term 
print("="*30)
print("cos (2pi/7) : ",round(sum,3))
print("="*30)

