#to determine whether a given integer is prime number or not:
n=int(input("Enter a n value=")) 
for i in range (2,n):
    if n%i==0:
        print(n,"is not a prime number")
        break                   
else:
    print(n,"is a prime number")

'''

output:
Enter a n value=61
61 is a prime number

'''
