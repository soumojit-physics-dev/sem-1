import math 
def f(x):
    return 3*x**3 - 5*x + 1

a = 0.0
b = 1.0
tol = 0.0001

if f(a) * f(b) >= 0 :
    print("Bisection is not possible")

else:
    for i in range(20) :
        c = (a+b)/2
        if abs(f(c)) < tol:
            break 
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    print("="*30)
    print("the value = ",round(c,3))
    print("="*30)




