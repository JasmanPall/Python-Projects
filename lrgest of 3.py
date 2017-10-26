# This program finds the largest of 3 numbers

num1 = float(input(" ENTER NUMBER 1: "))
num2 = float(input(" ENTER NUMBER 2: "))
num3 = float(input(" ENTER NUMBER 3: "))

if num1>num2 and num1>num3:
        print(" NUMBER 1 is the greatest")
elif num2>num1 and num2>num3:
        print(" NUMBER 2 is the greatest")
else:
        print(" NUMBER 3 is the greatest")
