# This program prints the factors of user input number

num = int(input(" ENTER NUMBER: "))
print(" The factors of",num,"are: ")

def factors(num):
    if num == 0:
        print(" Zero has no factors")

    else:
        for loop in range(1,num+1):
            if num % loop == 0:
                factor = loop
                print(factor)

factors(num)