#to sort a series of numbers by selection method 
N=int(input("enter no of elements = "))
a=[]
for i in range(N):
    val=int(input(f" value of {i+1} : "))
    a.append(val)
for i in range(N):
    min=i
    for j in range(i+1,N):
        if a[j]<a[min]:
            min=j
    a[i],a[min]=a[min],a[i]
    print(a)
print("sorted list = ",a)


'''
output=

enter no of elements = 8
 value of 1 : 60
 value of 2 : 5
 value of 3 : -12
 value of 4 : 49
 value of 5 : 99
 value of 6 : -2
 value of 7 : 75
 value of 8 : -69
[-69, 5, -12, 49, 99, -2, 75, 60]
[-69, -12, 5, 49, 99, -2, 75, 60]
[-69, -12, -2, 49, 99, 5, 75, 60]
[-69, -12, -2, 5, 99, 49, 75, 60]
[-69, -12, -2, 5, 49, 99, 75, 60]
[-69, -12, -2, 5, 49, 60, 75, 99]
[-69, -12, -2, 5, 49, 60, 75, 99]
[-69, -12, -2, 5, 49, 60, 75, 99]
sorted list =  [-69, -12, -2, 5, 49, 60, 75, 99]


'''
