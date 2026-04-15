#to determine the sum of infinite series of an exponential function 
import math 
N=int(input("Enter a value = "))
sum=0.0
term=1
x=2
for i in range (1,N):
    sum+=term
    term*=(x/i)
print("calculated sum = ",sum)
exact_value=math.exp(x)
print("exact value = ",exact_value)

'''
OUTPUT=

Enter a value = 20
calculated sum =  7.389056098925863
exact value =  7.38905609893065

'''
