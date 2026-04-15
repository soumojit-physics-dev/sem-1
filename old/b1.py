# To find the root of a given function by bisection method

def f(x):
    return x**2 - 6*x + 9   # given equation

a = float(input("Enter the value of a = "))
b = float(input("Enter the value of b = "))

tol = 0.0001

# Check validity
if f(a) * f(b) > 0:
    print("Invalid interval: f(a) and f(b) must have opposite signs.")
else:
    while abs(b - a) > tol:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("The root of the given function is:", c)

