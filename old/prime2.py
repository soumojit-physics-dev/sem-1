# to find a prime number next to the given number
N=30
for n1 in range(15,N):
    for n2 in range(2,n1):
        if n1%n2==0:
            break               #not a prime,stop checking
    else:   
        print(n1,"is a prime number after 15")
        break

'''

output:
17 is a prime number after 15

'''
