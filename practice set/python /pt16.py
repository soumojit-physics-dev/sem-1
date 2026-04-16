A = [4.82,-7.53,8.39,2.93,-1.56,-5.62]

n = len(A)

for i in range(n):
    for j in range(0,n-i-1):
        if A[j] < A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]

print(A) 


B = []
n = 48
print("factors of", n, "are :")
for i in range(1,n+1):
    if n % i == 0:
        B.append(i)
print(B)


text = "soumojit@soumojit-ideacentre-510S-08IKL:~/Desktop/practice set/python $ python3 pt16.py"
count = text.count("t")
print("Number of t = ",count)

import math

x = 2.31
sum = 0

for k in range(10):
    term = x**k/math.factorial(k)
    sum += term 
print("sum =",sum)


S = 0
n = 5

for i in range(1,n+1):
    term = i/(i+1)**2
    S += term 
print("addition = ",S)














