# This program prints the sum of natural numbers using recursion

print("This is sum of natural numbers using recursion ")


def sum(num):
    if num <=1:
        return num
    else:
        return num + sum(num-1)

terms = int(input(" Enter the terms : "))
if terms < 0:
    print("PLEASE ENTER A POSITIVE NUMBER")
else:
    print("The sum is: ",sum(terms))