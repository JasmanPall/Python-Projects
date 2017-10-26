# This program prints the multiplication of 2 matrices

print(" This is matrix multiplication ")

m1 = [[2,3,2],
      [3,2,3],
      [1,5,1]]

m2 = [[5,3,5],
      [3,2,3],
      [5,2,2]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for loop in m1:
    print(loop)
print("\n")
for loop in m2:
    print(loop)
print("\n")
for loop1 in range(len(m1)):
    for loop2 in range(len(m2[0])):
        for loop3 in range(len(m2)):
            result[loop1][loop2] += m1[loop1][loop3] * m2[loop3][loop2]

for loop in result:
    print(loop)