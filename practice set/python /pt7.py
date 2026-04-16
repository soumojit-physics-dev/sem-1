import math
 
X = []
n = 100
h = 1/99
x = 0
y = -1

for i in range(99):
    y = y + h * (y**2 * math.exp(x))
    x = x + h
    X.append(round(x,3))

print("="*30)
print("euler method = ",round(y,3))
print("="*30)
print("exact solution = ",round(-math.exp(-x),5))
print("="*30)
print(X)

