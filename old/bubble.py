#to sort a series of numbers by bubble sort method
N=int(input("Number of elements = "))           #taking inputs of elements from outside
a=[]
for i in range(N):
    val=int(input(f"Enter elements {i+1} = "))
    a.append(val)
print("unsorted list = ",a)
for i in range(N-1):
    for j in range(N-i-1):                  #index positioning of the list
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]                 #swapping elements
        else:
            pass
print("Sorted list = ",a)


'''

OUTPUT=


Number of elements = 5
Enter elements 1 = 50
Enter elements 2 = 30
Enter elements 3 = 2
Enter elements 4 = -9
Enter elements 5 = -16
unsorted list =  [50, 30, 2, -9, -16]
Sorted list =  [-16, -9, 2, 30, 50]
            

'''
