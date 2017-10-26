# This program prints all armstrong numbers in an interval

lowerbound = int(input(" ENTER THE LOWER BOUND RANGE: "))
upperbound = int(input(" ENTER THE UPPER BOUND RANGE: "))

for loop in range(lowerbound,upperbound+1):
    order = len(str(loop))
    temp = loop
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit**order
        temp //= 10

    if loop == sum:
            print(loop)