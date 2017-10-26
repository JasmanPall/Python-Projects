# This program prints the sum of natural numbers upto the user desire

limit = int(input(" Enter the limit u want: "))

sum = 0
if  limit < 0:
    print(" the range is not in a natural number order")

else:
    for loop in range(1,limit+1):
        sum +=loop

print(" The sum is",sum)