import math
def f(x):
    return math.log(2*x)*math.sin(3*x-1)

a = 2
b = 3
tol = 0.0001

if f(a) * f(b) >= 0:
    print("="*50)
    print(f"Bisection is not possible".center(50))
    print("="*50)
else:
    for i in range(20):
        c = (a+b)/2
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("="*50)
    print(f"Root = {round(c,3)}".center(50))
    print("="*50)
