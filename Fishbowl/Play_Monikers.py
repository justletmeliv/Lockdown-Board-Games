import json
import random
from random import randrange
import pandas as pd
from tabulate import tabulate

# read json file
with open('Data.json', 'r') as myfile:
    data=myfile.read()

# parse json file
card_list = json.loads(data)

# random choice of ten cards from the card list
your_hand = (random.sample(card_list, 10))
# print (your_hand)
# for card in your_hand:
#     print(card["Title"])
#     print(card["Description"])

# making a table of the hand of cards and their descriptions

data_frame = pd.DataFrame(your_hand)
print(tabulate(data_frame, headers='keys', tablefmt='psql'))
