# This program prints the table of multiplication for the desired input number

number=int(input(" ENTER THE NUMBER FOR WHICH U WANT THE MULTIPLICATION TABLE: "))

for loop in range(1,11):
        sol = number * loop
        #print(number,"X",loop,"=",sol) commented for 1 line printing and calculation

        print(number,"X",loop,"=",number*loop)

