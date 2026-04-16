import math
def f(x,y):
    return x*math.exp(-y)

X = []
n = 100
h = 1/99

x = 0
y = 0

for i in range(99):
    y = y + h * f(x,y)
    x = x + h
    X.append(x)
exact = math.log(0.5*(1**2)+ 1)
print(f"euler = ",y)
print(f"exact =",exact)

