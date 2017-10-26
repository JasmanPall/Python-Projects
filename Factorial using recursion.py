# This program prints the factorial of the number using recursion

print(" THIS IS FACTORIAL OF NUMBER USING RECURSION ")

def facto(num):
    if num == 1:
        return num
    else:
        return num * facto(num-1)

num = int(input(" Enter the number jiska factorial chahiye: "))
if num<=1:
    print(" The factorial of",num,"is :",1)
else:
    print(" The factorial of",num,"is :",facto(num))

