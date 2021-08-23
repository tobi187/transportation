import random as r
DRINKS = 7

our_drinks = []

while len(our_drinks) < 4:
    drink = r.randint(1, 8)
    our_drinks.append(drink)

print(our_drinks)
