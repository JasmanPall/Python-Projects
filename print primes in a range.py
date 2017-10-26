# This program prints all prime numbers in a particular range


lowerbound = int(input(" ENTER THE LOWER BOUND OF THE RANGE: "))
upperbound = int(input(" ENTER THE UPPER BOUND OF THE RANGE: "))

for num in range(lowerbound,upperbound+1):
    if num > 1:
        for loop in range(2,num):
            if num%loop == 0:
                break
        else:
                print(num)

