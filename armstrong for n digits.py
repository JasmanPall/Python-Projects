# This program checks armstrong for n digits of order


number = int(input(" ENTER number : "))
order = len(str(number))

sum = 0
temp = number

while temp>0:
    digit = temp%10
    sum += digit**order
    temp //=10

if number ==  sum:
    print(" The number is armstrong ")
else:
    print(" The number is not armstrong ")