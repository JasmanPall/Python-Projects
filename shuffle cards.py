# This program shuffles the cards

import random, itertools

print(" THIS IS CARD SHUFFLING ")

deck = list(itertools.product(range(1,14),['Spades', 'Clubs', 'Diamonds', 'Hearts']))

random.shuffle(deck)

num = int(input(" ENTER HOW MANY CARDS U WANT: "))
print(" YOU RECEIVED: ")

for loop in range(num):
    print(deck[loop][0]," OF ",deck[loop][1])