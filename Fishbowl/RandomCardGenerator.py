import json
import random
from random import randrange

# read json file
with open('Data.json', 'r') as myfile:
    data=myfile.read()

# parse json file
card_list = json.loads(data)

# show values from json file
print(card_list)

# print the first item on the list
print(card_list[0])

# accessing the first item in the list and printing the name of the card
card_name = card_list[0]["Title"]
print(card_name)

# accessing the first item in the list and printing the description of the card
card_description = card_list[0]["Description"]
print(card_description)

# detecting the length of the list in the json file
print(len(card_list))

# random choice of one card from the card list
random_card = randrange(len(card_list))
print(card_list[random_card]["Title"])
print(card_list[random_card]["Description"])

# random choice of ten cards from the card list
your_hand = (random.sample(card_list, 10))
print (your_hand)
for card in your_hand:
    print(card["Title"])
    print(card["Description"])
# print(your_hand [0]["title"])
# print(your_hand [0]["description"])
