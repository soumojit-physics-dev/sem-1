import math 
def f(x):
    return x**2 /(math.exp(x)*math.sin(x))

a = 2 
b = 4
tol = 0.001

if f(a) * f(b) >= 0:
    print("="*40)
    print("bisection is not possible".center(40))
    print("="*40)
else:
    for i in range(20):
        c = (a+b)/2
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("="*40)
    print(f"ROOT = {c}".center(40))
    print("="*40)    
