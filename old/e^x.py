# to determine the sum of infinite series exp(x) for a given range 
n=int(input("enter n value "))
import math
sum = 0.0 
term=1
x=2
for i in range(1,n):
    sum=sum+term
    term=term*(x/i)
#    print("sum=",sum, "term=",term)
print("calculated sum =",sum)
exact_value=math.exp(x)
print("exact_value=",exact_value)

'''
Output

enter n value 5
calculated sum = 6.333333333333333
exact_value= 7.38905609893065

enter n value 10
calculated sum = 7.387301587301587
exact_value= 7.38905609893065

enter n value 15
calculated sum = 7.389055882389215
exact_value= 7.38905609893065

enter n value 20
calculated sum = 7.389056098925863
exact_value= 7.38905609893065

'''

