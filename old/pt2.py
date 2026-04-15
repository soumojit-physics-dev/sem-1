import math 
def f(x):
    return x*math.exp(-x) -0.1
a=float(input("Enter the value of a = "))
b=float(input("Enter the value of b = "))

if f(a) * f(b) >= 0:
    print("IMPOSSIBLE")
else:
    for i in range(20):
        c = (a+b)/2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("Root is = ",(a+b)/2)


