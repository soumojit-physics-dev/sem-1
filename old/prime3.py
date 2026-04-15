# find the previous prime number of the given number 
N=15
for n1 in range(15,2,-1):
    for n2 in range(2,n1):
        if n1%n2==0:
           break            #not a prime,stop checking
    else:
        print(n1,"is the previous prime number")
        break

'''

output:
13 is the previous prime number

'''
