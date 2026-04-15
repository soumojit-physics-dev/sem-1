import math 
def f(x):
    return math.sin(x) - math.cos(x)/3

a = 3.0
b = 4.0

if f(a) * f(b) >= 0 :
    print("bisection is not applicable")

else: 
    for i in range(20):
        c = (a+b)/2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("="*30)
    print("root is : ",(a+b)/2)
    print("="*30)



"OUTPUT = root is :  3.4633431434631348"
