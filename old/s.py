import math                 # importing math module 

x = float(input("Enter a value of x in degree = "))
x1 = math.radians(x)        # degree to radian 

val = math.sin(x1)
print("Exact value using math.sin:", val)

# Taylor series
n = 1
t = x1                      # first term (x)
sum = x1                    # start sum  
tol = 0.001                 # tolerance  

while abs(t) > tol:
    t = -t * x1**2/ ((2*n)*(2*n+1))   # correct recurrence
    sum += t
    n += 1

print("Sum of the sin series :", sum)
print("Number of terms used :",int(n))

