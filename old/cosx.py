# to determine the cos series value 
import math 
x=int(input("enter value of x in degree ="))
x1=(math.pi/180)*x
val=math.cos(x1)
n=1
t=1.0           #first term
sign=-1
sum=1           #stores total sum
tol=0.001
while abs(t)>tol:
    t=sign*t*(x1**2/(n*2*((n*2)-1)))
    n+=1
    sum+=t
print("the sum si : ",sum)
print("the number of terms are :",n)
print("the exact value is :",val)

'''
output:

enter value of x in degree =0
the sum si :  1.0
the number of terms are : 2
the exact value is : 1.0


'''

