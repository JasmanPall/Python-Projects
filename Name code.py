# This program will display 10 outputs for the names in the lists

a = ["Euclid", "Archimedes", "Newton","Descartes", "Fermat", "Turing", "Euler", "Einstein", "Boole", "Fibonacci", "Nash"]

# Code for the longest word
max = 0
for loop in range(0,len(a)):
    if len(a[loop])>max:
        max = len(a[loop])
        count = loop
print("\nThe longest word is",a[count],"and the length is",max)


# Code for the shortest word
short = len(a[0])
count = 0
for loop in range(1,len(a)):
    if len(a[loop])<len(a[0]):
        short = len(a[loop])
        count = loop
print("\nThe shortest word is",a[count],"and the length is",short)


# Printing The number of names in the list
count = 0
for loop in a:
    count += 1
print("\nThe number of names in the list are:",count)


# Creating a string that has all the first characters of each name
char = ""
j = 0
for loop in a:
    char += loop[j]
print("\nThe String that has all first characters of each name would be:",char)


# Creating a string that has all the last characters of each name
char= ""
j = 0
for loop in range(0, len(a)):
    j = len(a[loop]) - 1
    char+= a[loop][j]
print("\nThe string that has all the last characters of each name would be:",char)


# Input a character from user and count the number of times it is there in the list
char = input("\nPlease enter the character u want to search in the list: ")
count = 0
for loop in range (0,len(a)):
    for j in range (0,len(a[loop])):
        if a[loop][j] == char:
            count = count + 1
print("The Character",char,"appears in the list",count,"times")

# Sorting the list alphabetically Without predefined function
for j in range(len(a)):
   for loop in range (len(a)-1):
        if (a[loop])> (a[loop + 1]):
            a[loop+1],a[loop] = a[loop],a[loop+1]

print("\nNo Predefined Sorting: ",a)


# Sorting the list using pre defined function
a.sort()
print("PreDefined Sorting is: ",a)


# Reverse Sorting in reverse order without using predefined functions
for j in range(len(a)):
    for loop in range(len(a)-1):
        if a[loop]<a[loop+1]:
            a[loop],a[loop+1]=a[loop+1],a[loop]

print("\nNo Predefined Reverse Sorting: ",a)


# Reverse Sorting using predefined function
a.sort(reverse=True)
print("Predefined Reverse Sorting is: ",a)


#Display the number of vowels in the whole list
count = 0
for loop in range(len(a)):
    for j in range(len(a[loop])):
        if a[loop][j] =='A' or a[loop][j] =='E' or a[loop][j] =='I' or a[loop][j] =='O' or a[loop][j] =='U' or a[loop][j] =='a' or a[loop][j] =='e' or a[loop][j] =='i' or a[loop][j] =='o' or a[loop][j] =='u':
            count += 1

print("\nThe total number of vowels in the lsit are: ",count)




