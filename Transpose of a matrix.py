# This program transposes the matrix

print(" THIS IS MATRIX TRANSPOSE ")

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

result = [[0,0,0],
           [0,0,0],
           [0,0,0]]

for loop1 in range(len(matrix)):
    for loop2 in range(len(matrix[0])):
        result[loop2][loop1] = matrix[loop1][loop2]

for loop in result:
    print(loop)