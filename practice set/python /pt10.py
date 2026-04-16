import math 

X = []
n = 100
h = 1/99

x = 0
y = 0

for i in range(99):
    y = y + h * (math.exp(y)*math.sin(x))
    x = x + h
    X.append(x)

exact=-math.log(math.cos(1))

print("="*50)
print(f"euler = {round(y,3)}".center(50))
print("="*50)
print(f"exact value = {round(exact,3)}".center(50))
print("="*50)

