# to determine the sum of infinite series of an exponential function
n=int(input("enter a value = "))
x=2
tol=0.001
sum=0.0
term=1.0
while abs(term)>tol:
    sum+=term
    term*=(x/n)
    n=n+1
print("calculted sum=",sum)
print("n value =",n)

'''
OUTPUT:

calculted sum= 7.3887125220458545
n value = 11

'''
