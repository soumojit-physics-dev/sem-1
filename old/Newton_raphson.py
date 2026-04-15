#finding roots by newton raphson method
import math 
def f(x):
    return x**3-2*x-5         # defining the function
def g(x):
    return 3*x**2-2            # derivative of the function 
count=0
tol=eval(input("Enter tolerance: "))

x=eval(input("Enter initial guess: "))        #Initial Guess:
while abs(f(x))>tol:
    x=x-(f(x)/g(x))             #updating the value of x 
    count+=1
print("the root of the function is = ",x)
print("no of repeatation = ",count)


'''
output=

Enter tolerance: 0.001
Enter initial guess: 2
the root of the function is =  2.094568121104185
no of repeatation =  2


'''
