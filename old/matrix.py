#construction of a matrix
M=[]
r=int(input("Number of rows = "))           #enter rows
c=int(input("Number of columns = "))        #enter columns 
for j in range(0,c):
    row=[]                          #empty list for taking rows
    for i in range(0,r):
        a=int(input("Elements of the row = "))          #row elements 
        row.append(a)
    M.append(row)                           #append rows in matrix

    print(M)
    
'''
Number of rows = 3
Number of columns = 3
Elements of the row = 5
Elements of the row = 6
Elements of the row = 7
[[5, 6, 7]]
Elements of the row = 1
Elements of the row = 2
Elements of the row = 3
[[5, 6, 7], [1, 2, 3]]
Elements of the row = 4
Elements of the row = 5
Elements of the row = 6
[[5, 6, 7], [1, 2, 3], [4, 5, 6]]

'''

