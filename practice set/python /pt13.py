import math 
def f(x):
    return x**3 - 2*x**2 + 5*x -7

a = 1
b = 2
tol = 0.0001

if f(a) * f(b) >= 0:
    print("Bisection is not applicable")
else:
    for i in range(20):
        c = (a+b)/2
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print(f"rott is : ",c)

