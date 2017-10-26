# This program removes all the punctuations from a string

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str = input(" ENTER STRING : ")

no_punct = ""
for char in str:
    if char not in punctuations:
        no_punct = no_punct + char

print(no_punct)