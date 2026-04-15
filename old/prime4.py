#to find a prime number in a given range:
n=21
for n1 in range(2,n):
    for n2 in range(2,n1):
        if n1%n2==0:
            print(n1,"is not a prime number")
            break 
    else:
        print(n1,"is a prime number")

'''
output:

2 is a prime number
3 is a prime number
4 is not a prime number
5 is a prime number
6 is not a prime number
7 is a prime number
8 is not a prime number
9 is not a prime number
10 is not a prime number
11 is a prime number
12 is not a prime number
13 is a prime number
14 is not a prime number
15 is not a prime number
16 is not a prime number
17 is a prime number
18 is not a prime number
19 is a prime number
20 is not a prime number


'''
