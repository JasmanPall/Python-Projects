# This program prints the factorial of a number

numbero = int(input("ENTER THE NUMBER JISKA FACTORIAL CHAHIYE: "))
facto = 1
if numbero<=0:
     print(" THE NUMBER IS 0 OR NEGATIVE")

else:
    for loopi in range(1,numbero+1):
        facto = facto * loopi
    print(" Facto of",numbero,"is",facto)



