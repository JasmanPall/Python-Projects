# This program prints the fibonacci series upto the desired length of the user

leng = int(input(" ENTER THE LENGTH OF FIBONACCI SERIES: "))
num1 = 0
num2 = 1

if leng>0:
    print(num1)
    for loop in range(1,leng):
        print(num2)
        num1,num2=num2,num1+num2
else:
    print("U ENTERED LENGTH AS 0 OR NEGATIVE") 