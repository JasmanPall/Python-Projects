# This program swaps values of variables.

a=0
b=1

a=int(input("Enter a: "))
print(" Value of a is: ",a)
b=int(input("Enter b: "))
print(" Value of b is: ",b)

# Swap variable without temp variable
a,b=b,a

print(" \n Now Value of a is:",a)
print(" and Now Value of b is:",b)