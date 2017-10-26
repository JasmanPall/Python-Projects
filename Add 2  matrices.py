# This program adds 2 matrices and prints the solution matrix

matrix1 = [[1,2,3],
           [4,5,6],
           [0,0,1]]

matrix2 = [[8,6,4],
           [4,5,6],
           [5,5,4]]

mresult = [[0,0,0],
           [0,0,0],
           [0,0,0]]

for loop1 in range(len(matrix1)):
    for loop2 in range(len(matrix1[0])):
        mresult[loop1][loop2] = matrix1[loop1][loop2] + matrix2[loop1][loop2]

print(mresult)

for loop3 in mresult:
    print(loop3)