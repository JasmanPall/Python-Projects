# this program finds if a number is prime or not

number = int(input(" ENTER THE NUMBER U WANNA CHECK: "))
if number>=1:
    for loop in range(2,number):
        if number%loop == 0:
            print("  NUMBER IS NOT PRIME")
            print(loop,"times",number//loop,"is",number)
            break
    else:
            print(" THE NUMBER %i is a prime number" %number)
else:
    print(" NUMBER IS EITHER ZERO OR NEGATIVE")
