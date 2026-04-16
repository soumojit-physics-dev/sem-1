A = [[-3,1,-2],[1,0,4],[2,-4,-2]]
B = [[4,-1,-2],[-3,5,0],[-2,-4,2]]

mul = []
for i in range(3):
    row = []
    for j in range(3):
        sum = []
        for k in range(3):
            sum += A[i][j] * B[i][j]    
        row.append(sum)
    mul.append(row)
print(mul)
