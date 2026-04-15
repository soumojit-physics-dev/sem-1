#to find the factors of a given number 
N=int(input("Enter a number = "))
for i in range(1,N+1):
    if N % i == 0:
        print("factors of that given number is ",i)

'''
OUTPUT=
Enter a number = 30
factors of that given number is  1
factors of that given number is  2
factors of that given number is  3
factors of that given number is  5
factors of that given number is  6
factors of that given number is  10
factors of that given number is  15
factors of that given number is  30

'''
