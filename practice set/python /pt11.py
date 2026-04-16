import math 
X = []
n = 100
h = 1/99

x = 0
y = 2

for i in range(99):
    y = y + h * (y - x)
    x = x + h
    X.append(x)

exact = math.exp(1) + 1 + 1 

print("="*50)
print(f"euler = {round(y,3)}".center(50))
print("="*50)
print(f"exact value = {round(exact,3)}".center(50))
print("="*50)


     
