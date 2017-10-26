# This program checks if string is palindrome or not

print(" This is palindrome checking string ")

str = input(" ENTER STRING: ")
str = str.casefold()
reverse_str = reversed(str)

if list(str) == list(reverse_str):
    print(" THE STRING IS PALINDROME")
else:
    print(" NOT PALINDROME ")