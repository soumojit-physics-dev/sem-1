import math 
def f(x):
    return x**2*math.sin(x) - math.exp(x)*math.cos(x)
def df(x):
    return 2*x*math.sin(x) + x**2*math.cos(x) - math.exp(x)*math.cos(x) + math.exp(x)*math.sin(x)

x = -4

for i in range(10):
    x = x - f(x)/df(x)
print("*"*50)
print(f"root of the given function is ={round(x,5)}".center(50))
print("*"*50)
