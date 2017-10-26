# This program finds all numbers divisible in a list by the user desired input number

my_list = [10, 11, 12 ,13,  14, 15, 17, 19, 20]

number = int(input(" ENTER THE DIVISOR :"))

answer = list(filter(lambda x: (x % number ==0), my_list))

print(" THE NUMBERS DIVISIBLE BY",number,"are:",answer)
