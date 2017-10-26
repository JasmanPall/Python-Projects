# This is a simple calculator program

def add(num1,num2):
    sum = num1 + num2
    return sum

def sub(num1,num2):
    difference = num1 - num2
    return difference

def multiply(num1,num2):
    multi = num1 * num2
    return multi

def div(num1,num2):
    divi = num1 / num2
    return divi

print(" THIS IS A CALCULATOR: ")

num1 = int(input(" ENTER NUMBER 1: "))
num2 = int(input(" ENTER NUMBER 2: "))

print(" \n WHICH OPERATION U WANT TO DO: ")
print(" 1. ADD \n 2. SUBTRACT \n 3. MULTIPLY \n 4. DIVIDE \n")
user_input = input("ENTER Choice: ")
if user_input == '1' or user_input == 'add':
    print(" U choose add")
    print(" THE ADDITION OF",num1,"and",num2,"is:",add(num1,num2))

elif user_input == '2' or user_input == 'sub':
    print(" U choose subtract")
    print(" THE SUBTRACTION OF",num1,"and",num2,"is:",sub(num1,num2))

elif user_input == '3' or user_input == 'multiply':
    print(" U choose multiply")
    print(" THE MULTIPLICATION OF",num1,"and",num2,"is:",multiply(num1,num2))

elif user_input == '4' or user_input == 'divide':
    print(" U choose divide")
    print(" THE DIVISION OF", num1, "and", num2, "is:",div(num1, num2))

else:
    print(" U CHOOSE THE WRONG OPTION")