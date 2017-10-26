# Solving quadratic equations

import cmath

a=float(input("Enter the number for a : "))
b=float(input("Enter the number for b : "))
c=float(input("Enter the number for c : "))

print(" Your quadratic equation is: %ix^2 + %ix + %i " %(a,b,c))

# Calculating Discriminant

d= (b**2)-(4*a*c)
solution1= (-b-(((b**2)-(4*a*c))**0.5))/(2*a)
solution2= (-b+(((b**2)-(4*a*c))**0.5))/(2*a)

print("The solutions to the equation are %i and %i" %(solution1,solution2))

# EASIER VISIBILITY TO CODE

solution1= (-b-(d**0.5))/(2*a)
solution2= (-b+(d**0.5))/(2*a)

print("The solutions to the equation are %i and %i" %(solution1,solution2))

#using predefined functions

sol1= (-b - cmath.sqrt(d))/(2*a)
sol2= (-b + cmath.sqrt(d))/(2*a)

print('The solutions to the equation using cmath are {0} and {1}'.format(sol1,sol2))
#print('The solution are {0} and {1}'.format(sol1,sol2))