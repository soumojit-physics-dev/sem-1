#find the roots of the given equation by bisection method
def f(x):
    return x**2-6*x+9           # given equation
a=eval(input("enter the value of a ="))
b=eval(input("enter the value of b ="))

c=(a+b)/2
tol=0.0001          #check upto this tollerence

while f(c)==0:
    print(c,"is the root ")
    break           #stop checking
while f(a)*f(b)>0:
    print("wrong guess bro")
break               #check again 
    while abs(b-a)>tol:
        c=(a+b)/2
    if f(a)*f(c)<0:
        b=c
    else:
        a=c
print("the root of the function=",(a+b)/2)
    
    
'''

output:

enter the value of a =2
enter the value of b =4
3.0 is the root 
wrong guess bro

'''
