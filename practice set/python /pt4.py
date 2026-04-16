import math 
def f(x):
    return 5*x*math.sin(x) - 3*x 
def df(x):
    return 5*math.sin(x) + 5*x*math.cos(x) - 3

x=2.5

for i in range(10):
    x = x - f(x)/df(x)
print("="*30)
print(f"Root is = {round(x,3)}")   
print("="*30)
"""
==============================
Root is = 2.498
==============================
"""
