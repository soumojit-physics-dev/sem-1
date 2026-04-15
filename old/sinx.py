#sum of infinite series of sinx
import math     #importing math module
x=int(input('Enter a value of x in degree = '))
x1=(math.pi/180)*x          #degree to radian 
val=math.sin(x1)            #exact value
n=1
t=x1
sign=-1
sum=x1
tol=0.001
while abs(t)>tol:
    t=sign*t*(x1**2/(n*2*((n*2)+1)))        #updating terms of expansion 
    n+=1                                 #updating no of terms
    sum+=t                               #updating the sum of expansion
print("sum of the series = ",sum )
print("number of terms is = ",n)
print("the exact value is = ",val)


'''

output=

Enter a value of x in degree = 90
sum of the series =  1.0000035425842861
number of terms is =  5
the exact value is =  1.0


'''

                        
