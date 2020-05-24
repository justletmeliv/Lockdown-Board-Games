#!/usr/bin/env python3

import json
import random
from random import randrange
import pandas as pd
from tabulate import tabulate
import argparse

# create an argument parser which allows us to read in arguments supplied on the command line - will let people set their own user interface size so the table displays nicely.
parser = argparse.ArgumentParser(description = 'Play Fishbowl! A program that gives you a random hand of 10 cards displayed in a table.')
# tells user what the program does.
parser.add_argument(
    # adds the switch '--width' as a recognised term for entering the screen width.
    '--width',
    # tells it to store the entered screen width figure in screen_width.
    dest = 'screen_width',
    # default value is 100.
    default = '100',
    # tells it to store the screen width value in the returned value of parse_args, 'args' (see next line).
    action = 'store',
    # help instructions if someone enters -h.
    help='Please enter a number for the line width of the card description when displayed in the table. The default line width is set at 100, but if this is not readable on your screen please adjust to longer or shorter as needed by typing "--width" and the size number you want.')

# using the filtering set up above, look at what has been entered (e.g. --width 50) and see if it meets the conditions above. If it does, store the value in 'args'.
args = parser.parse_args()

# read json file
with open('Data.json', 'r') as myfile:
    data=myfile.read()

# parse json file
card_list = json.loads(data)

# random choice of ten cards from the card list
your_hand = (random.sample(card_list, 20))
# code which iterates over the array your_hand - each dictionary from the array is stored in variable 'card'. Within the for loop, print title and description for each dictionary.
# print (your_hand)
# for card in your_hand:
#     print(card["Title"])
#     print(card["Description"])

# function to add line breaks on the first space after 50 characters
# also setting up the index number checker so we know where to slice to add line break
def add_line_breaks(description_string, line_width):
    character_counter = 0
    insert_on_next_character = False
    description_string_length = len(description_string)
    string_index_range = range(description_string_length)
    # need a return string so we can make changes without altering the original string's index number (because we're adding characters...)
    # return_string builds up the actual sentence by concatenating characters as they are listed by current_character - this means we can then add characters without messing up the index numbers of the original string.
    # set return_string as an empty string - needs to be an empty string so python knows that += is a concatenation function as both are data type string.
    return_string = ""

# creating the range length of string to be able to slice and add line break
    for character_index in string_index_range:
# current_character - gives you the character at any given index number in the description string based on the json file
        current_character = description_string[character_index]
# what happens if insert_on_next_character is true?
        if insert_on_next_character is True:
            # insert a line break into the return_string, reset insert_on_next_character to false, reset character_counter to 0
            # character = character[:character_index] + " " + character[character_index:] - leaving this in as a 'how to slice things'.
            return_string += "\n"
            insert_on_next_character = False
            character_counter = 0
# return_string will concatenate the output of current_character - so will make the actual description sentence which we can then add line breaks to. Needs to be after the insertion loop so that the line break is added after a space and not the next character.
        return_string += current_character

# if the count is greater than or equal to 50 and character is a space, set insert_on_next_character to true for the next loop
        if character_counter >= line_width and current_character == " ":
            insert_on_next_character = True
# need to increase the value of character_counter by 1 at the end of each loop to make sure it is keeping the right count
        character_counter +=1
# outside the loop, return (put value of return string into card["Description"]) return_string
    return return_string

# add_line_breaks function contains the above for loop and other code and then puts the results of the code above back into card_description with the changes made.
for card in your_hand:
    card["Description"] = add_line_breaks(
        description_string = card["Description"],
        # set the maximum line-width to either default of 100 (stored in screen_width) or the value supplied by the user in 'args' above.)
        line_width = int(args.screen_width))

# making a table of the hand of cards and their descriptions
data_frame = pd.DataFrame(your_hand)
print(tabulate(data_frame, headers='keys', tablefmt='fancy_grid', showindex="never"))
