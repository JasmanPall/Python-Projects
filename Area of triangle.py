# This program will calculate the area of Triangle and print it

#side1=10
#side2=6
#side3=8

# User input side
side1=float(input("enter side 1 of triangle: "))
side2=float(input("enter side 1 of triangle: "))
side3=float(input("enter side 1 of triangle: "))

#area calculation starts - this is semi perimeter

side=(side1+side2+side3)/2

#area calculation ends- this is the area

area=(side*(side-side1)*(side-side2)*(side-side3))**0.5

print("the area of triangle is %0.2f" %area)