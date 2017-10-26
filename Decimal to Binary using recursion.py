# This program converts decimal to binary using recursion

print(" THIS IS A CONVERSION PROGRAM")

def convert(num):
    if num >1:
        convert(num//2)
    print(num % 2,end = '')


num = int(input(" ENTER THE NUMBER U WANNA CONVERT: "))
convert(num)