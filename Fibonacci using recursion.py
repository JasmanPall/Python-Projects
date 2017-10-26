# This program prints Fibonacci series using recursion

print(" THIS IS FIBONACCI SERIES USING RECURSION ")

def fibo(num):

    if num <= 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)


terms = int(input(" ENTER THE NUMBER OF TERMS"))
if terms < 0:
    print(" PLEASE ENTER A POSITIVE NUMBER")
else:
    print("FIBONACCI SERIES: ")

    for loop in range(terms):
        print(fibo(loop))