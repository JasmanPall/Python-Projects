# This program checks if the year is leap or not

year=float(input(" ENTER THE YEAR U WANNA CHECK: "))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("The Year %i is a leap year" %year)
        else:
            print("The Year %i is a not leap year" %year)
    else:
        print("The Year %i is a leap year" %year)
else:
    print("The Year %i is a not leap year" %year)


