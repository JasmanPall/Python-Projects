# This program prints the HCF and LCM of the desired numbers

num1 = int(input(" ENTER THE 1st Number: "))
num2 = int(input(" ENTER THE 2nd Number: "))

def computeHCF(x,y):

    if x < y:
        smaller = x
    else:
        smaller = y

    for loop in range(1,smaller+1):
        if (x % loop == 0) and (y % loop == 0):
            HCF = loop

    return HCF
print("THE HCF / GCD for",num1,"and",num2,"is: ",computeHCF(num1,num2))

def computeLCM(num1,num2):
    if num1 > num2:
        larger = num1
    else:
        larger = num2
    while(True):
        if(larger % num1 == 0) and (larger % num2 == 0):
            LCM = larger
            break
        larger += 1
    return larger
print(" The LCM for",num1,"and",num2,"is: ",computeLCM(num1,num2))
