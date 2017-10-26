# This program checks if the number is armstrong or not

number = int(input(" ENTER THE NUMBER U WANNA CHECK : "))
temp = number
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp = temp // 10

if number == sum:
    print(" The number is armstrong ")
else:
    print(" The number is not armstrong ")
