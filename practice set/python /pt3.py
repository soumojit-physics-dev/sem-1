# to find the solution of differntial eqution 
import math 

def f(t):
    return v0 * math.exp(-a*t)

v0 = 2.0 
a  = 0.2
h  = 0.1
t  = 0
x  = 0
count = 0

file= open("data.txt","w")

while t <= 10:
    file.write(f"{t:.2f}   {x:.6f}\n")
    x = x + h*f(t)
    t = t + h

file.close()
 
x_exact = (v0/a)*(1-math.exp(-a*t))

print("="*30)
print("Euler method x(10)",round(x,3))
print("="*30)
print("Exact value x(10)",round(x_exact,3))
print("="*30)
