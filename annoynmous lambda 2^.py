# This program displays 2^n using annonymus lambda function

limit = int(input(" Enter the range: "))

if limit < 0:
    print(" ENTER CORRECT RANGE PLEASE ")

else:
    answer = list(map(lambda x: 2**x,range(limit+1)))

print(" The total range is",limit)

for loop in range(limit+1):
    print(" 2 raised the power by",loop,"is",answer[loop])